# 📐 Escopo — Assistente Pessoal (MVP)

> **Status:** Consolidado (2026-08-20) — decisões ADR-001, ADR-002, ADR-003
> **Docs relacionados:** [02-arquitetura](./02-arquitetura.md) · [03-roadmap](./03-roadmap.md) · [04-requisitos](./04-requisitos.md)

---

## 1. Visão em 1 parágrafo

Um assistente pessoal multi-tenant que recebe tarefas em linguagem natural e as
executa de verdade: **navega na web** como um humano (remote control +
simplified view), **opera Google Docs/Agenda, Notion e WhatsApp**, e **controla
as finanças via Open Finance (Polp)** — classificação de gastos, saldos e
relatórios. Tudo atrás de uma API única (FastAPI) sobre um runtime Agno
multi-tenant (`blu_agno_runtime`), com frontend pequeno de relatórios e admin.

## 2. Decisões de arquitetura (fechadas)

| # | Decisão | ADR |
|---|---------|-----|
| 1 | **Lib comum `blu_agno_runtime`** (Agno multi-tenant no Neon) em vez de segunda Agent API | [001](../decisions/001-lib-agno-runtime-multitenant.md) |
| 2 | **Canal WhatsApp via Twilio** (lib `blu_twilio_client` compartilhada com o Blu) + **frontend admin pequeno** | [002](../decisions/002-whatsapp-twilio-frontend-admin.md) |
| 3 | **Open Finance (Polp)** — controle financeiro e classificação de gastos | [003](../decisions/003-open-finance-polp.md) |

## 3. Escopo funcional (resumo)

| Área | MVP | Fase |
|---|---|---|
| **Navegação web** | Playwright embutido, observation AX tree/Markdown, ações click/type/navigate, allowlist de domínios | F1 |
| **Google** | Docs (client já existe), Agenda (create/update), Gmail/Sheets via tool_pool | F1 |
| **Notion** | Tool nova no tool_pool: criar página, buscar, ler | F1 |
| **WhatsApp** | Twilio via tool_pool (send/batch/status já existem) + webhook de entrada com validação HMAC | F1 |
| **Open Finance** | Consumir dados Polp já sincronizados: saldos, transações, categorização de gastos | F2 |
| **Frontend admin** | Relatórios (sessões, tools, custos, erros, financeiro) + gestão (tenants, usuários, grants, integrações) | F2 |
| **Multi-tenancy** | Control plane + sessions no Neon (schema `agent_runtime`), identidade só do token | F0 |

## 4. Fora de escopo (agora)

- Frontend de chat (chat é WhatsApp)
- Integração Telegram
- Migração LangGraph → Agno (só validação na F3)
- Browser worker separado (F3; MVP usa Playwright embutido)
- Novas ferramentas (Slack, Drive, etc.) — entram via tool_pool sob demanda
- Nada específico do Blu na lib (agente-bloquo = cliente, não tocar)

## 5. Reuso do monorepo (pouco trabalho novo)

| Peça | Estado | Ação |
|---|---|---|
| `blu_twilio_client` | Pronta + em uso pelo Blu | Consumir via tool_pool (zero código Twilio novo) |
| `send_whatsapp_message` / `send_whatsapp_batch` / `check_whatsapp_status` | Tools MCP prontas no tool_pool | Expor ao assistente |
| `GoogleDocsClient`, `GoogleCalendarClient`, `GoogleSheetsClient`, `GoogleGmailClient` | Prontos na lib | Expor @mcp.tool() faltantes |
| `query_calendar` | Tool pronta | Reusar |
| **Polp (Open Finance)** | backend_api: connect/sync/webhook prontos; routines: FIN-01 (saldos), FIN-02 (gastos por categoria); tabelas `polp_accounts/transactions/bills/integrations/webhook_events` | Expor como tools ao assistente |
| `blu_llm_service` (tiers) | Pronta | Usar no factory da lib |
| `blu_auth` (Supabase) | Pronta | Usar no AuthGate |
| `blu_lgpd` | Obrigatória | Dados financeiros pessoais = dados pessoais |

## 6. Métricas de sucesso do MVP

- Tarefa ponta-a-ponta: "leia este doc, me resuma e agende reunião" → execução real
- "quanto gastei em restaurantes este mês?" → resposta com dados reais do Polp
- 2 tenants com sessões isoladas (nunca vazam contexto)
- Cold start < 5s; resposta com tools < 30s
