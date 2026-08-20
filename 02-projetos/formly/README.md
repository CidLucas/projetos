# Formly — Fábrica de Questionários com Áudio + IA

> **Slug:** `formly`
> **Tipo:** SaaS próprio (B2B/B2C)
> **Domínio:** Produtividade / Pesquisa
> **Fase atual:** Fase 0 — Protótipo funcional (realinhado ao protótipo visual)
> **Início:** 2026-07-30
> **Responsável:** Lucas Cid
> **Última atualização:** 2026-08-04

---

## 🎯 Resumo

Plataforma web para **criação, coleta e análise de questionários** com:
- **Áudio como canal de resposta nativo** (transcrição automática via Groq Whisper)
- **IA como camada de geração** (DeepSeek Flash gera o questionário a partir de descrição/áudio)
- **12 tipos de pergunta** — do texto curto à matriz de escala, com design system próprio (wine/pine/paper)

**Proposta:** competir em nichos BR onde Typeform é overkill e Google Forms é básico demais.

**Status atual:** protótipo funcional rodando (frontend Vite + backend FastAPI + PostgreSQL Docker), com as 5 telas do protótipo aprovado implementadas e realinhadas ao design system canônico.

## 📚 Índice

- [STATUS.md](./STATUS.md) — saúde, blockers, próximas ações
- [docs/00-escopo-proposta.md](./docs/00-escopo-proposta.md) — escopo e proposta
- [docs/01-roadmap.md](./docs/01-roadmap.md) — roadmap com progresso
- [docs/02-arquitetura.md](./docs/02-arquitetura.md) — arquitetura e schema
- [docs/02-requisitos.md](./docs/02-requisitos.md) — requisitos detalhados
- [requisitos/README.md](./requisitos/README.md) — índice dos requisitos visuais
- [site/](./site/) — protótipo HTML canônico (5 telas)

## 🔗 Links úteis

- **Repo de código:** https://github.com/CidLucas/formly
- **PLANO.md:** https://github.com/CidLucas/formly/blob/main/PLANO.md
- **Protótipo canônico:** https://github.com/CidLucas/projetos/tree/main/formly/site
- **Google Doc (escopo):** https://docs.google.com/document/d/1V539iHGWJq-4qMA30YS7FbRCo023rwYm7rwbMkfGhEw/edit
- **Stack:** Vite + React 18 + FastAPI + PostgreSQL + Groq Whisper + DeepSeek Flash
