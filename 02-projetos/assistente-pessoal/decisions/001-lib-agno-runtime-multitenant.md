# ADR-001 — Lib comum Agno multi-tenant em vez de segunda Agent API

- **Data:** 2026-08-20
- **Status:** Aceita
- **Decisor:** Lucas Cid

## Contexto

O assistente pessoal (navegação web + Google Docs/Agenda + Notion) precisa de
um runtime de agente. Hoje existem: `agents_api` (LangGraph via
`blu_agent_framework`, multi-tenant p/ o Blu), `tool_pool_api` (hub MCP com
Google Suite), `memory_api` (multi-tenant no Neon com control plane), e o
`agente-bloquo` (Agno, single-tenant, cliente Bloquo).

Pergunta: outra Agent API (LangGraph) ou um agente Agno com skills? E quantas
imagens?

## Decisão

1. **Lib comum no monorepo:** `blu_agno_runtime` — runtime Agno multi-tenant,
   extraído dos padrões do agente-bloquo (`_mcp_connection`, MCPTokenManager)
   e da memory_api (Principal, IdentityAdapter, AuthGate, control plane).
2. **Multi-tenant no Neon no padrão da memory_api:** schema próprio
   `agent_runtime`, migrations SQL numeradas com checksum, control plane
   (tenants/users/memberships/scope_grants), identidade exclusivamente do token.
3. **Session storage:** `TenantPostgresDb(PostgresDb)` com coluna `tenant_id`
   dedicada e filtro em toda query (Agno não tem tenant nativo).
4. **Uma imagem nova** (`assistente_api`) no MVP; browser worker separado na
   Fase 2 se o browser for central.
5. **Migração LangGraph → Agno faseada:** assistente é o caso de teste; portar
   agentes do agents_api só depois de validar (Fase 3).

## Alternativas consideradas

| Alternativa | Por que foi recusada |
|---|---|
| Segunda Agent API LangGraph | Duplica orquestração; assistente é single-user primeiro, escopo diferente do Blu; acopla dois mundos |
| Agente dentro da agents_api | Força escopo pessoal no produto do cliente/multi-tenant do Blu |
| Agente-bloquo como base direta | É repo do cliente Bloquo — vazar escopo; serve só como fonte de padrões |
| `user_id` composto `{tenant}:{user}` no Agno | Frágil, vaza isolamento em logs e queries |
| `metadata` JSON com tenant_id | Filtro JSON lento/feio no Postgres; sem índice dedicado |

## Consequências

- **Positivas:** contrato MCP (tool_pool) fica estável; migração de framework
  vira troca de backend do factory; padrões debugados (MCP HTTP, token exchange)
  herdam de graça; agente-bloquo e futuros agentes consomem a mesma lib.
- **Negativas:** trabalho de extração da lib antes do MVP do assistente;
  manutenção de mais uma lib no monorepo; blu_agent_framework (LangGraph) e
  blu_agno_runtime (Agno) coexistem durante a Fase 2.

## Links

- [docs/02-arquitetura.md](../docs/02-arquitetura.md)
- Padrões-fonte: `services/memory_api/src/memory_api/auth/*`, `control/plane.py`,
  `db/migrations/` · `agente-bloquo/src/agent.py` (`_mcp_connection`)
