# Rastro — Consultoria de Fluxo de Propostas + MCP Brain Lite

> **Slug:** `rastro`
> **Cliente:** Rastro ([rastro.cc](https://rastro.cc/)) — agência-studio de inteligência criativa (Rio de Janeiro)
> **Tipo:** Consultoria + Implementação (Fase A + Fase B)
> **Contrato:** Deep Blue → Rastro (direto, sem intermediário)
> **Fase atual:** Descoberta / Pré-proposta
> **Início:** 2026-08-03 (estimado)
> **Responsável:** Lucas Cid

---

## 🎯 Resumo

A Rastro é uma agência-studio com +10 anos de mercado, 3 divisões (Agency, Films, Labs) e clientes como Nubank, HBO Max, Globo, iFood, Itaú, Unilever. Eles já usam Claude intensamente e têm um pipeline de IA próprio — incluindo uma wiki LLM de 60MB.

O problema: **dificuldade em vender projetos**. O fluxo de criação de propostas, orçamentos e briefings está fragmentado — conhecimento preso em pessoas, documentos espalhados, sem uma base central acessível a todo o time.

**Solução proposta:** engajamento em duas fases:

| Fase | O quê | Duração |
|---|---|---|
| **Fase A — Consultoria** | Revisão do fluxo atual de propostas, diagnóstico, recomendações de melhoria de processos e documentos | 1–2 semanas |
| **Fase B — Implementação** | Deploy do MCP Brain Lite como memória central corporativa, ingestão do corpus documental, configuração dos MCPs nos Claude Desktop do time (5–10 pessoas), treinamento | 2–3 semanas |

**Produto utilizado:** [MCP Brain Lite](https://github.com/CidLucas/mcp_brain_lite) — conector MCP remoto que expõe o corpus documental da empresa via gateway FastAPI+FastMCP sobre banks Mnemosyne, com 3 escopos (pessoal, corporativo, restrito) e auth OAuth 2.1 via Supabase.

## 📚 Índice

- [STATUS.md](./STATUS.md) — saúde, blockers, próximas ações, perguntas categorizadas
- [docs/01-visao.md](./docs/01-visao.md) — problema, público, proposta de valor, escopo detalhado
- [docs/02-arquitetura.md](./docs/02-arquitetura.md) — stack proposta, componentes, fluxos, segurança
- [docs/03-roadmap.md](./docs/03-roadmap.md) — fases, milestones, cronograma
- [docs/04-reunioes.md](./docs/04-reunioes.md) — log cronológico de conversas/decisões

## 🔑 Decisões-chave

| # | Decisão | Data | ADR |
|---|---------|------|-----|
| 001 | MCP Brain Lite como produto-base (não Brain completo) | 2026-07-29 | — |
| 002 | Modelo de engajamento: Fase A (consultoria) + Fase B (implementação) | 2026-07-29 | — |
| 003 | Escopos: pessoal + corporativo (sem restrito na V1) | 2026-07-29 | — |

## 🔗 Links úteis

- **Site da Rastro:** [rastro.cc](https://rastro.cc/)
- **Portfólio:** [work.rastro.cc](https://work.rastro.cc/)
- **Instagram:** [@_rastro](https://instagram.com/_rastro)
- **Repo MCP Brain Lite:** `CidLucas/mcp_brain_lite` (privado)
- **Repo MCP Brain:** `CidLucas/mcp_brain` (privado)
- **Hub de documentação:** `CidLucas/projetos`
