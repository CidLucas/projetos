# 🤖 Assistente Pessoal

> **Slug:** `assistente-pessoal`
> **Tipo:** Produto próprio (projeto futuro)
> **Fase atual:** Pesquisa / descoberta
> **Início:** 2026-08-20

---

## 🎯 Resumo

Assistente pessoal com IA capaz de **navegar a web de forma autônoma**: controla um browser real (remote control via Playwright/Puppeteer/CDP) e enxerga as páginas como **visão simplificada** (Accessibility Tree / Markdown) em vez de pixels brutos.

## 📚 Subprojetos / Áreas

| Área | Status |
|---|---|
| [navegação web](./navegação%20web/) | Pesquisa concluída — dossiê + fontes |
| [docs/01-visao.md](./docs/01-visao.md) | Visão do MVP (assistente + lib agno runtime) |

## 🔑 Decisões-chave

| # | Decisão | Data | ADR |
|---|---------|------|-----|
| 1 | Paradigma do sistema: remote control + simplified view (AX tree/Markdown) | 2026-08-20 | (na pesquisa) |
| 2 | **Lib comum `blu_agno_runtime` (Agno multi-tenant no Neon) em vez de segunda Agent API** | 2026-08-20 | [decisions/001](./decisions/001-lib-agno-runtime-multitenant.md) |

## 🔗 Links úteis

- **Repo de código (proposto):** lib `blu_agno_runtime` no monorepo + `assistente_api`
- **Dossiê de pesquisa:** [navegação web/dossie-pesquisa.md](./navegação%20web/dossie-pesquisa.md)
- **Arquitetura:** [docs/02-arquitetura.md](./docs/02-arquitetura.md)
