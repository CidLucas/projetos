# 🗺 Roadmap — Assistente Pessoal (MVP)

> **Gerado:** 2026-08-20 · **Revisado:** 2026-08-20 (Open Finance incluído)
> **Base:** ADR-001 (lib agno runtime) + ADR-002 (WhatsApp/frontend) + ADR-003 (Open Finance)
> **Princípio:** cada fase entrega valor utilizável; nada de "framework primeiro, produto depois".

---

## Fase 0 — Fundação da lib `blu_agno_runtime`

**Objetivo:** runtime Agno multi-tenant no monorepo, testado, com migrations no Neon.

| # | Tarefa | Tipo | Prioridade | Critério de pronto |
|---|---|---|---|---|
| 0.1 | Scaffold lib `libs/blu_agno_runtime` (pyproject, src/, pytest, ruff) | código | alta | `uv run pytest` verde |
| 0.2 | `auth/principal.py` + `IdentityAdapter` Protocol (Principal{tenant_id,user_id,role,scopes} + ContextVar) — portar da memory_api | código | alta | testes unitários; Claims resolve de claims |
| 0.3 | `AuthGate` middleware (blu_auth → resolve principal → ContextVar) | código | alta | token válido → ContextVar; inválido → 401 |
| 0.4 | `mcp/connection.py` — MCPConnection (streamable HTTP + MCPTools por request) do agente-bloquo | código | alta | conexão real ao tool_pool lista tools |
| 0.5 | `mcp/token_manager.py` — token exchange (OAuth → JWT local MCP) | código | média | troca de token de teste funciona |
| 0.6 | `storage/tenant.py` — `TenantPostgresDb(PostgresDb)` com coluna `tenant_id` + filtro em todas as queries | código | alta | sessões de 2 tenants isoladas em testes |
| 0.7 | `control/plane.py` — resolve_identity do sub do token | código | alta | resolve_identity(sub) → {tenant,user,role} |
| 0.8 | Migrations `db/migrations/` — `0001_control_plane.sql` (schema `agent_runtime`) + aplicador com checksum | código | alta | `make migrate` idempotente; checksum denuncia alteração |
| 0.9 | `factory.py` — Agent builder (tiers via blu_llm_service, guardrails, session_id) | código | média | agente responde com modelo do tier |
| 0.10 | CI (lint + testes da lib) | infra | média | pipeline verde |

**Gate:** 0.2–0.8 verdes.

---

## Fase 1 — `assistente_api` (backend + WhatsApp + primeiras tools)

**Objetivo:** o assistente conversa por WhatsApp e executa tarefas reais.

| # | Tarefa | Tipo | Prioridade | Critério de pronto |
|---|---|---|---|---|
| 1.1 | Scaffold `services/assistente_api` (FastAPI, config, health, structlog) | código | alta | `/health` OK |
| 1.2 | AuthGate + tenant resolution plugada (Claims → ControlPlane) | código | alta | tenant A não vê sessão de B |
| 1.3 | Rota `POST /api/v1/chat` — mensagem → agente (Agno + lib) → resposta | código | alta | chat ponta-a-ponta com sessão persistida |
| 1.4 | Webhook WhatsApp (Twilio) — validação de assinatura (webhook.py da lib), inbound → agente → reply via tool_pool | código | alta | WhatsApp real responde (sandbox Twilio) |
| 1.5 | Tool **Google Docs** no tool_pool (client existe — expor @mcp.tool) | código | alta | agente cria/lê/edita doc |
| 1.6 | Tool **Google Agenda** — create/update event (query_calendar existe) | código | alta | agente agenda reunião |
| 1.7 | Tool **Notion** no tool_pool (nova) | código | média | agente cria página/busca |
| 1.8 | Tool **navegação web** — toolkit Playwright com observation AX tree/Markdown (ariaSnapshot) | código | alta | agente navega, extrai, responde |
| 1.9 | Sessões multi-tenant via TenantPostgresDb | código | alta | histórico persiste; tenants não cruzam |
| 1.10 | Deploy Neon + Cloud Run | infra | alta | staging no ar |

**Gate:** demo "leia o doc, me resuma e agende reunião" ponta-a-ponta.

---

## Fase 2 — Open Finance + Frontend admin

**Objetivo:** controle financeiro real + relatórios/gestão.

| # | Tarefa | Tipo | Prioridade | Critério de pronto |
|---|---|---|---|---|
| 2.1 | Tool **saldo/cash position** no assistente (reusa FIN-01 do routines sobre `polp_accounts`) | código | alta | "quanto tenho?" responde com dados reais |
| 2.2 | Tool **gastos por categoria/período** (reusa FIN-02 sobre `polp_transactions`) | código | alta | "quanto gastei em restaurantes?" com dados reais |
| 2.3 | **Classificação de gastos por LLM** — refina/classifica transações sem categoria do Polp | código | alta | categorização automática visível no admin |
| 2.4 | Notificação financeira via WhatsApp (webhook `transaction/created` → resumo) | código | média | evento do Polp gera mensagem |
| 2.5 | Scaffold `apps/assistente-admin` (React+TS+Vite, padrão monorepo, auth Supabase) | código | alta | login funciona |
| 2.6 | Tela **Relatórios** — sessões, uso de tools, custos LLM, erros | código | alta | dados reais do Neon |
| 2.7 | Tela **Financeiro** — saldos, gastos por categoria, classificação LLM | código | alta | dados reais do Polp |
| 2.8 | Tela **Gestão** — tenants, usuários, membros, grants | código | alta | CRUD via control plane |
| 2.9 | API de admin no assistente_api (`/admin/*`) | código | alta | frontend consome API real |
| 2.10 | Deploy frontend | infra | média | URL acessível |

**Gate:** "quanto gastei em restaurantes este mês?" com dados reais + admin utilizável.

---

## Fase 3 — Hardening, browser worker e migração

**Objetivo:** produção de verdade + abrir caminho para migração LangGraph→Agno.

| # | Tarefa | Tipo | Prioridade | Critério de pronto |
|---|---|---|---|---|
| 3.1 | **Browser worker separado** (Playwright+Chromium) exposto via MCP/HTTP | código | média | agente usa worker remoto; escala |
| 3.2 | Quotas por tenant (antes da escrita — padrão memory_api F-18) | código | média | tenant estoura teto → bloqueado |
| 3.3 | Auditoria de uso (api_events por tenant) | código | média | log de tools por tenant |
| 3.4 | Validação comparativa LangGraph vs Agno (custo, latência, acurácia) | pesquisa | alta | relatório com recomendação |
| 3.5 | Se validado: portar agents_api (LangGraph) → blu_agno_runtime | código | alta | agentes do Blu em Agno |

**Gate:** produção hardening + decisão de migração com dados.

---

## Riscos e mitigações

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| Webhook Twilio lento (timeout ~5s) | média | alto | processamento assíncrono (fila) + reply imediato |
| Agno MCPTools HTTP frágil | média | médio | padrão `_mcp_connection` já debugado; testes de integração |
| Playwright embutido pesa imagem | média | médio | worker separado na F3; limite de sessões |
| Qualidade da classificação LLM de gastos | média | médio | prompt de refino + fallback p/ categoria do Polp |
| Migração LangGraph custosa | alta | médio | F3 valida com dados; tool_pool é contrato estável |
| Escopo vazando pro Blu | baixa | alto | lib compartilhada só p/ runtime; tools específicas no tool_pool |
