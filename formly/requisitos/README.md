# 📋 Requisitos — Formly

> **Produto:** Formly — Fábrica de Questionários com Áudio + IA
> **Versão:** v0.3 — 2026-08-04
> **Base:** Site HTML estático (5 arquivos em `formly/site/` no GitHub) — **implementado no app React**
> **Última atualização:** 2026-08-04
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 🗂 Índice

| Arquivo | O que cobre |
|---|---|
| [`requisitos-app.md`](./requisitos-app.md) | 📱 Requisitos de aplicação — Design System, estrutura de 5 páginas, tipos de pergunta (12) |
| [`pagina-00-landing.md`](./pagina-00-landing.md) | 🏠 Landing — "Precisa de um questionário?" + input + áudio |
| [`pagina-01-auth.md`](./pagina-01-auth.md) | 🔐 Auth — Google OAuth + magic link e-mail |
| [`pagina-02-builder.md`](./pagina-02-builder.md) | 📝 Builder — Cards de pergunta editáveis, 12 tipos, amostras |
| [`pagina-03-send.md`](./pagina-03-send.md) | 📤 Send — Seleção de contatos + CSV + mensagem + disparo |
| [`pagina-04-analytics.md`](./pagina-04-analytics.md) | 📊 Analytics — KPIs, gráfico de barras, exportação CSV |
| [`pagina-05-resposta.md`](./pagina-05-resposta.md) | 📋 Página pública do respondente (`/s/{slug}`) — 12 tipos |

---

## 🎨 Design System (extraído do CSS real do site e implementado no app)

O Formly implementa um tema **editorial vinho/papel** — não é Blu DS. Tokens:

| Categoria | Tokens |
|---|---|
| **Cor primária** | `--wine: #7A2E3F`, `--wine-soft: #F5E8EB`, `--wine-dark: #5C1E2C` |
| **Cor secundária** | `--pine: #3B5B52`, `--pine-soft: #E8F0ED` |
| **Superfície** | `--paper: #E7E6E0`, `--paper2: #F3F2EE`, `--card: #FCFBF8` |
| **Texto** | `--muted: #6E6D66`, `--line: #C9C7BE` |
| **Display** | `'Helvetica Neue', Helvetica, Arial, sans-serif` |
| **Body** | `Georgia, 'Times New Roman', Times, serif` |
| **Mono** | `'SF Mono', 'Fira Code', monospace` |

---

## 🏗 Estrutura do App (implementado em React)

```
formly_app (Vite)
│
├── /                → Landing
├── /auth            → Autenticação (dev login; Supabase OAuth pendente)
├── /builder/:id?    → Builder (criador) — cards empilhados
├── /send/:id        → Envio (contatos + CSV)
├── /s/:slug         → Página pública do respondente (12 tipos)
└── /dashboard/:id   → Analytics (KPIs + barras + export)
```

**Fluxo:** Landing → Auth → Builder → Send → Analytics

---

## ✅ Status atual (2026-08-04)

- 🟢 **Design System:** wine/pine/paper implementado em `global.css` (R1)
- 🟢 **12 tipos de pergunta:** enum no backend + UI no builder/survey (R2, R4, R5)
- 🟢 **Landing + Auth:** implementadas (R3, R7) — sem entrada manual de JWT
- 🟢 **Builder:** cards empilhados estilo protótipo (R4)
- 🟢 **Send:** contatos + busca + CSV + mensagem (R6)
- 🟢 **Analytics:** KPIs + barras + export CSV (R6)
- 🟢 **Página do respondente:** `/s/{slug}` com os 12 tipos (R5)
- 🟢 **Áudio:** gravação livre com timer + limite 2 min + transcrição editável + e-mail (R9)
- 🟢 **Textos longos:** quebra de linha sem scroll horizontal (R8)
- 🟡 **Auth real:** apenas dev login — Supabase OAuth é TODO no código
- 🟡 **Envio de e-mail:** mock no Send — Resend é Fase 1

---

## 📝 Como usar estes arquivos

1. Comece pelo [`requisitos-app.md`](./requisitos-app.md) — visão geral da aplicação
2. Cada página tem seu próprio arquivo de requisitos (pagina-00 a pagina-05)
3. O Google Doc completo está em: https://docs.google.com/document/d/1el2fWACIuMcc8HQ73k7lm5JuZxdam-nWonFYgwgqYRU/edit
4. A implementação real está em https://github.com/CidLucas/formly (commit do realinhamento: 2026-08-04)
