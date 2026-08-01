# 📋 Requisitos — Formly

> **Produto:** Formly — Fábrica de Questionários com Áudio + IA
> **Versão:** v0.2 — 2026-08-01
> **Base:** Site HTML estático (5 arquivos em `formly/site/` no GitHub)
> **Última atualização:** 2026-08-01
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 🗂 Índice

| Arquivo | O que cobre |
|---|---|
| [`requisitos-app.md`](./requisitos-app.md) | 📱 Requisitos de aplicação — Design System, estrutura de 5 páginas, tipos de pergunta (11) |
| [`pagina-00-landing.md`](./pagina-00-landing.md) | 🏠 Landing — "Precisa de um questionário?" + input + áudio |
| [`pagina-01-auth.md`](./pagina-01-auth.md) | 🔐 Auth — Google OAuth + magic link e-mail |
| [`pagina-02-builder.md`](./pagina-02-builder.md) | 📝 Builder — Cards de pergunta editáveis, 11 tipos, amostras |
| [`pagina-03-send.md`](./pagina-03-send.md) | 📤 Send — Seleção de contatos + CSV + mensagem + disparo |
| [`pagina-04-analytics.md`](./pagina-04-analytics.md) | 📊 Analytics — KPIs, gráfico de barras, exportação CSV |
| [`pagina-05-resposta.md`](./pagina-05-resposta.md) | 📋 Página pública do respondente — ⚠️ aspirational (não implementada no site) |

---

## 🎨 Design System (extraído do CSS real do site)

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

## 🏗 Estrutura do Site

```
formly.duckdns.org
│
├── / (index.html)        → Landing
├── /auth.html            → Autenticação
├── /builder.html         → Builder (criador)
├── /send.html            → Envio
└── /analytics.html       → Dashboard de resultados
```

**Fluxo:** Landing → Auth → Builder → Send → Analytics

---

## ⚠️ Status atual

- 🟢 **Site HTML:** 5 páginas implementadas como protótipo estático
- 🟢 **Design System:** Definido e implementado em CSS custom properties
- 🟡 **Tipos de pergunta:** 7 dos 11 tipos com UI implementada no builder
- 🔴 **Página do respondente:** Não implementada (`/r/{id}`)
- 🔴 **Backend/API:** Não implementado
- 🔴 **Autenticação real:** Apenas UI (Google + e-mail simulados)
- 🟡 **Stack:** Vite + React 18 + Blu DS — mas o site atual usa HTML/CSS puro

---

## 📝 Como usar estes arquivos

1. Comece pelo [`requisitos-app.md`](./requisitos-app.md) — visão geral da aplicação
2. Cada página do site tem seu próprio arquivo de requisitos (pagina-00 a pagina-05)
3. O Google Doc completo está em: https://docs.google.com/document/d/1el2fWACIuMcc8HQ73k7lm5JuZxdam-nWonFYgwgqYRU/edit
