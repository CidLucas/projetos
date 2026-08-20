# 👁 Visão — Assistente Pessoal (MVP)

> **Status:** Rascunho inicial (decisão de arquitetura fechada; escopo de MVP em definição)

---

## Problema

O dono gerencia múltiplos projetos, integrações (Google Workspace, Notion,
bancos, memórias) e navega na web diariamente. Não existe um agente único que
una: navegação web autônoma (como um humano), acesso a ferramentas
(Google Docs/Agenda, Notion) e memória persistente — com isolamento
multi-tenant no banco.

## Proposta de valor

Um assistente pessoal que recebe tarefas em linguagem natural e as executa de
verdade: navega na web (remote control + simplified view), lê/escreve no
Google Docs e Agenda, gerencia Notion, e lembra contexto entre sessões — tudo
atrás de uma API única (FastAPI) sobre um runtime Agno multi-tenant.

## Público

- **Primário:** o próprio dono (single-user no MVP, multi-tenant por design)
- **Futuro:** outros usuários/empresas (o control plane já nasce multi-tenant)

## Escopo do MVP (proposta — a refinar)

**Inclui:**
1. Lib `blu_agno_runtime` no monorepo (auth multi-tenant, MCP connection, storage)
2. `assistente_api` — FastAPI + Agno, 1 endpoint de chat/tarefa, AuthGate com Principal
3. Tools: navegação web (Playwright, observation AX tree/Markdown), Google Docs
   (client já existe na lib) + Agenda (query_calendar já existe no tool_pool),
   Notion (tool nova no tool_pool)
4. Neon: schema `agent_runtime` + migrations (control plane + sessions)
5. Sessões persistentes por tenant (TenantPostgresDb)

**Fica para depois (Fase 2+):**
- Browser worker separado (Playwright+Chromium) se o browser for central
- Portar agents_api (LangGraph) para a lib Agno
- Frontend/webchat do assistente
- Notion/Google fora do tool_pool (decisão: tudo no tool_pool = hub)

## Métricas de sucesso do MVP

- Conseguir uma tarefa ponta-a-ponta: "leia este doc, me resuma e agende uma
  reunião" → execução real via Google + resposta final
- Sessões de 2 tenants diferentes isoladas (nunca vazam contexto)
- Cold start do assistente < 5s; resposta com tools < 30s

## Fora de escopo (regra de ouro)

- Não vira mais uma Agent API LangGraph
- Não mistura escopo do Blu (agents_api continua LangGraph até Fase 3)
- Não usa o repo agente-bloquo como base direta (é do cliente Bloquo)
