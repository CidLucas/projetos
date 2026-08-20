# 🗺 Roadmap — Assistente Pessoal (MVP)

> **Gerado:** 2026-08-20 · **Base:** ADR-001 (lib agno runtime) + ADR-002 (WhatsApp/frontend)
> **Princípio:** cada fase entrega valor utilizável; nada de "framework primeiro, produto depois".

---

## Fase 0 — Fundação da lib `blu_agno_runtime`

**Objetivo:** runtime Agno multi-tenant no monorepo, testado, com migrations no
Neon. Sem produto ainda — é a base.

| # | Tarefa | Tipo | Prioridade | Critério de pronto |
|---|---|---|---|---|
| 0.1 | Scaffold lib `libs/blu_agno_runtime` (pyproject, estrutura src/, pytest, ruff) | código | alta | `uv run pytest` verde no monorepo |
| 0.2 | Portar `auth/principal.py` + `IdentityAdapter` Protocol da memory_api (Principal{tenant_id,user_id,role,scopes} + ContextVar) | código | alta | testes unitários; adapter Claims resolve de claims |
| 0.3 | Portar `AuthGate` middleware (valida token via blu_auth, resolve principal, injeta ContextVar) | código | alta | request com token válido → ContextVar preenchida; inválido → 401 |
| 0.4 | Portar `mcp/connection.py` — MCPConnection (streamable HTTP + ClientSession + MCPTools por request, teardown limpo) do agente-bloquo | código | alta | conexão real ao tool_pool (staging) lista tools |
| 0.5 | Portar `mcp/token_manager.py` — token exchange (OAuth → JWT local MCP) | código | média | troca de token de teste funciona |
| 0.6 | `storage/tenant.py` — `TenantPostgresDb(PostgresDb)` com coluna `tenant_id` + filtro em todas as queries | código | alta | sessões de 2 tenants isoladas em testes |
| 0.7 | `control/plane.py` — control plane: resolve_identity do sub do token | código | alta | resolve_identity(sub) → {tenant,user,role} |
| 0.8 | Migrations `db/migrations/` — `0001_control_plane.sql` (schema `agent_runtime`: tenants, users, memberships, scope_grants) + aplicador com checksum | código | alta | `make migrate` idempotente em Neon de teste; checksum denuncia alteração |
| 0.9 | `factory.py` — Agent builder: tiers de modelo via blu_llm_service, guardrails base, session_id | código | média | agente responde com modelo do tier correto |
| 0.10 | CI no monorepo (lint + testes da lib) | infra | média | pipeline verde |

**Entregável da fase:** lib publicável + schema Neon aplicado. **Gate:** 0.2–0.8 verdes.

---

## Fase 1 — `assistente_api` (backend + WhatsApp + primeiras tools)

**Objetivo:** o assistente conversa por WhatsApp e executa tarefas reais
(Google Docs/Agenda, Notion, navegação web básica).

| # | Tarefa | Tipo | Prioridade | Critério de pronto |
|---|---|---|---|---|
| 1.1 | Scaffold `services/assistente_api` (FastAPI, config pydantic-settings, health, structlog) | código | alta | `/health` OK no deploy |
| 1.2 | AuthGate + tenant resolution plugada (Claims → ControlPlane) | código | alta | chamada com token de tenant A não vê sessão de B |
| 1.3 | Rota `POST /api/v1/chat` — message → agente (Agno + blu_agno_runtime) → resposta | código | alta | chat ponta-a-ponta com sessão persistida |
| 1.4 | Webhook WhatsApp (Twilio) — validar assinatura (webhook.py da lib), inbound → agente → reply via tool_pool `send_whatsapp_message` | código | alta | WhatsApp real responde (sandbox Twilio) |
| 1.5 | Tool **Google Docs** no tool_pool (client já existe na lib — expor @mcp.tool) | código | alta | agente cria/lê/edita doc via tool_pool |
| 1.6 | Tool **Google Agenda** — create/update event (query_calendar já existe; adicionar create) | código | alta | agente agenda reunião |
| 1.7 | Tool **Notion** no tool_pool (nova) | código | média | agente cria página/busca no Notion |
| 1.8 | Tool **navegação web** — toolkit Playwright embutido com observation (AX tree/Markdown via ariaSnapshot) | código | alta | agente navega, extrai conteúdo, volta com resposta |
| 1.9 | Sessões multi-tenant via TenantPostgresDb (histórico entre turns) | código | alta | histórico persiste; 2 tenants não cruzam |
| 1.10 | Deploy Neon + Cloud Run (mesmo padrão do monorepo) | infra | alta | ambiente staging no ar |

**Entregável da fase:** assistente funcional no WhatsApp + Google Docs/Agenda + navegação web.
**Gate:** demo "leia este doc, me resuma e agende reunião" ponta-a-ponta.

---

## Fase 2 — Frontend admin (pequeno)

**Objetivo:** relatórios + gestão. App React+Vite em `apps/`, sem chat.

| # | Tarefa | Tipo | Prioridade | Critério de pronto |
|---|---|---|---|---|
| 2.1 | Scaffold `apps/assistente-admin` (React+TS+Vite, padrão monorepo, auth via Supabase/blu_auth) | código | alta | login funciona |
| 2.2 | Tela **Relatórios** — sessões por tenant, uso de tools, custos LLM (langfuse), erros | código | alta | tabelas reais de dados do Neon |
| 2.3 | Tela **Gestão** — tenants, usuários, membros (papéis), grants de escopo | código | alta | CRUD real via control plane |
| 2.4 | API de admin no assistente_api (endpoints /admin/*) | código | alta | frontend consome API real |
| 2.5 | Deploy do frontend (mesmo padrão formly-web/blu-web) | infra | média | URL acessível |

**Entregável da fase:** admin utilizável (ver dados reais, gerir tenants).

---

## Fase 3 — Hardening, browser worker e migração

**Objetivo:** produção de verdade + abrir caminho para migração LangGraph→Agno.

| # | Tarefa | Tipo | Prioridade | Critério de pronto |
|---|---|---|---|---|
| 3.1 | **Browser worker separado** (Playwright+Chromium) exposto via MCP/HTTP — desacoplar do agente | código | média | agente usa worker remoto; escala horizontal |
| 3.2 | Quotas por tenant (antes da escrita — padrão memory_api F-18) | código | média | tenant estoura teto → bloqueado |
| 3.3 | Auditoria de uso (api_events por tenant — padrão memory_api) | código | média | log de tools por tenant |
| 3.4 | Validação comparativa LangGraph vs Agno (custo, latência, acurácia em tarefas reais) | pesquisa | alta | relatório com recomendação |
| 3.5 | Se validado: portar agents_api (blu_agent_framework/LangGraph) → blu_agno_runtime, um agente por vez | código | alta | agentes do Blu em Agno com mesmo comportamento |

**Entregável da fase:** produção hardening + decisão de migração tomada com dados.

---

## Escopo explícito

### ✅ Inclui (MVP)
- Lib blu_agno_runtime (auth multi-tenant, MCP, storage, control plane, factory)
- assistente_api FastAPI + Agno; chat via WhatsApp (Twilio) e endpoint
- Tools: Google Docs, Google Agenda, Notion, navegação web (Playwright)
- Frontend admin pequeno (relatórios + gestão)
- Neon: schema `agent_runtime` + migrations
- Multi-tenant real (isolamento por tenant desde o dia 1)

### ❌ Não inclui (agora)
- Frontend de chat (chat é WhatsApp)
- Integração Telegram
- Migração LangGraph→Agno (só validação na Fase 3)
- Browser worker (Fase 3, MVP usa embutido)
- Ferramentas extras (Slack, Drive, etc.) — entra via tool_pool quando quiser
- Nada específico do Blu na lib (agente-bloquo = cliente, não tocar)

## Riscos e mitigações

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| Webhook Twilio lento (timeout ~5s p/ reply) | média | alto | processamento assíncrono (fila) + reply imediato "recebi" |
| Agno MCPTools HTTP frágil | média | médio | padrão _mcp_connection já debugado no agente-bloquo; testes de integração |
| Playwright embutido pesa imagem/cold start | média | médio | separar worker na F3; limite de sessões no MVP |
| Migração LangGraph custosa | alta | médio | Fase 3 valida com dados antes; tool_pool é contrato estável |
| Escopo vazando pro Blu (agente-bloquo) | baixa | alto | lib compartilhada só p/ runtime; tools específicas no tool_pool |
