# 📐 Arquitetura — Assistente Pessoal (navegação web + integrações)

> **Status:** Aprovada (decisão do dono 2026-08-20)
> **ADR raiz:** [decisions/001-lib-agno-runtime-multitenant.md](../decisions/001-lib-agno-runtime-multitenant.md)

---

## 1. Decisão central

**Uma lib comum no monorepo (`blu_agno_runtime`)** — runtime Agno multi-tenant —
em vez de uma segunda Agent API. O assistente pessoal é o **primeiro consumidor**
da lib; o agente-bloquo e futuros agentes Agno passam a consumi-la depois
(estratégia de migração LangGraph → Agno).

## 2. Diagrama

```
┌──────────────┐       ┌─────────────────────────────────────────────┐
│ Telegram / UI│ ───▶  │ assistente_api (FastAPI + Agno + blu_agno_runtime)│
└──────────────┘       │  • agent loop (Agno)                         │
                       │  • tools: navegação web, Google, Notion      │
                       │  • AuthGate → Principal (ContextVar)         │
                       └───────┬─────────────────────┬────────────────┘
                               │ MCP (HTTP)          │ Postgres (Neon)
                       ┌───────▼────────┐   ┌────────▼─────────────────┐
                       │ tool_pool_api  │   │ Neon — schema agent_runtime│
                       │ (google suite, │   │ control plane + sessions  │
                       │  docs, notion) │   │ (migrations numeradas)    │
                       └───────┬────────┘   └──────────────────────────┘
                               │
                       ┌───────▼────────┐
                       │ browser_worker │  Playwright + Chromium
                       │ (Fase 2, opc.) │
                       └────────────────┘
```

## 3. Componentes da lib `blu_agno_runtime`

| Módulo | Responsabilidade | Origem do padrão |
|---|---|---|
| `auth/principal.py` | `Principal` frozen dataclass {tenant_id, user_id, role, scopes} + ContextVar | memory_api (portar) |
| `auth/identity.py` | `IdentityAdapter` Protocol — `resolve(claims) → Principal` | memory_api (portar) |
| `auth/middleware.py` | `AuthGate` — valida token (blu_auth), resolve principal, injeta ContextVar | memory_api (portar) |
| `mcp/connection.py` | `MCPConnection` — streamable HTTP + ClientSession + MCPTools, conexão por request com teardown | agente-bloquo `_mcp_connection` (portar) |
| `mcp/token_manager.py` | Token exchange (OAuth/provider → JWT local MCP) | agente-bloquo `MCPTokenManager` (portar) |
| `storage/tenant.py` | `TenantPostgresDb(PostgresDb)` — coluna `tenant_id` dedicada, filtro em todas as queries | Agno PostgresDb + extensão própria |
| `control/plane.py` | Control plane: tenants, users, memberships, scope_grants (schema `agent_runtime`) | memory_api (espelhar) |
| `factory.py` | Agent builder: tiers de modelo via blu_llm_service, guardrails, progressive disclosure | agente-bloquo + agents_api |
| `db/migrations/` | `NNNN_nome.sql` + aplicador com checksum (`make migrate`) | memory_api (espelhar) |

## 4. Multi-tenant no Neon (padrão memory_api)

### 4.1 Schema próprio `agent_runtime` (não `public`)

```sql
-- 0001_control_plane.sql
CREATE SCHEMA IF NOT EXISTS agent_runtime;

agent_runtime.tenants      (id uuid PK, name, plan, created_at)
agent_runtime.users        (id uuid PK, external_user_id text UNIQUE, email)
agent_runtime.memberships  (tenant_id, user_id, role owner|admin|member, PK(tenant_id,user_id))
agent_runtime.scope_grants (tenant_id, user_id, scope, granted_at)
```

### 4.2 Session storage multi-tenant

O Agno `PostgresDb` não tem `tenant_id` nativo → `TenantPostgresDb` adiciona
coluna `tenant_id` na session_table e **filtra toda query por tenant** (get,
read, update, delete, upsert). Alternativa descartada: `user_id` composto
`{tenant}:{user}` (frágil, vaza isolamento no logging) e `metadata` JSON (filtro
feio e lento no Postgres).

### 4.3 Regra de ferro (F-20 da memory_api)

**Identidade vem exclusivamente do token.** Nenhum campo de roteamento
(tenant, user, escopo) chega por argumento de tool — o `Principal` é montado
das claims validadas (custom claims `tenant_id`/`role`/`scopes` carimbadas no
access token via hook do Supabase) e vive num ContextVar por requisição. Um
argumento de roteamento que o modelo mande nem existe no schema das tools.

### 4.4 Migrations

SQL numerado (`0001_control_plane.sql`, `0002_...`) aplicado em ordem
lexicográfica por aplicador com checksum — **migration aplicada é imutável**.
Mesmo padrão do memory_api (`make memory-migrate`).

## 5. Estratégia de migração (LangGraph → Agno)

```
Fase 1 (agora)  → lib blu_agno_runtime + assistente_api (primeiro consumidor)
Fase 2          → validar: qualidade, custo, dev velocity vs LangGraph
Fase 3 (se ok)  → portar agentes do agents_api (blu_agent_framework/LangGraph)
                  para a lib Agno, um por um, por baixo do factory
```

O tool_pool_api é o contrato estável (MCP) — trocar o runtime de orquestração
não muda as tools.

## 6. O que NÃO entra na lib

- Tools específicas (navegação web, Google Docs, Notion) → vivem no
  tool_pool_api (hub) ou como toolkits do assistente, nunca na lib
- Browser/Chromium → worker separado (Fase 2) ou embutido (MVP)
- Lógica de produto do Blu → agents_api continua LangGraph até Fase 3
