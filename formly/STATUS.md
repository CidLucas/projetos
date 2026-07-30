# Status — Formly

> Última atualização: 2026-07-30
> **Produto:** SaaS próprio (Deep Blue)
> **Fase:** Descoberta
> **Responsável:** Lucas Cid

## 🩺 Saúde geral

🟡 **Em descoberta** — definindo escopo da V1, modos de interação, e páginas.

## 📊 Resumo executivo

| Item | Status |
|---|---|
| Escopo macro definido | 🟢 Google Doc criado (2026-07-30) |
| Escopo detalhado (páginas) | 🟢 definido (Criador, Resposta, Dashboard) |
| Stack escolhida | 🟢 definida (Next.js App Router + FastAPI + PostgreSQL/Supabase + Groq + S3) |
| Arquitetura documentada | 🟢 `docs/02-arquitetura.md` criado |
| Schema do banco | 🟢 definido (5 tabelas: users, surveys, questions, responses, answers, contacts) |
| Protótipo Fase 0 | 🔴 não iniciado |
| Repo de código | 🟢 https://github.com/CidLucas/formly |
| PLANO.md | 🟢 criado (41 tasks, 4 workstreams, 9 decisões) |
| Modelo de precificação | 🟡 premissas no Google Doc |

## 🔑 Decisões recentes

| # | Decisão | Data |
|---|---|---|
| 1 | Múltiplos modos de interação no criador: drag & drop, importação de texto, chat assistido | 2026-07-30 |
| 2 | Estrutura de requisitos: mesmo modelo do Blue V3 e Context-MCP (6 seções por página) | 2026-07-30 |
| 3 | Fluxo do criador em 6 etapas (não 3 modos): Input → Refinamento → Geração → Ajuste → Publicação → Distribuição | 2026-07-30 |
| 4 | Publicação gera página web funcional com componentes ligados na API | 2026-07-30 |
| 5 | Stack: PostgreSQL (Supabase) + Next.js App Router + Supabase Auth + S3 | 2026-07-30 |
| 6 | Schema: 5 tabelas (surveys, questions, responses, answers, contacts) com JSONB pra config flexível | 2026-07-30 |

## 🎯 Próximas ações

- [ ] **Lucas** — validar estrutura de páginas proposta (Criador, Resposta, Dashboard)
- [ ] **Lucas** — detalhar o fluxo de cada modo de interação do criador
- [ ] **Hermes** — enriquecer requisitos com input do Lucas

## 📅 Histórico de atualizações

| Data | Atualização |
|---|---|
| 2026-07-30 | Bootstrap do projeto no hub. Google Doc importado. Requisitos iniciados. |
