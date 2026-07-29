# Rastro — Consultoria de Fluxo de Propostas + Rastro Brain

> **Slug:** `rastro`
> **Cliente:** Rastro ([rastro.cc](https://rastro.cc/)) — agência-studio de inteligência criativa (Rio de Janeiro)
> **Tipo:** Consultoria + Implementação (Fase A + Fase B)
> **Contrato:** Deep Blue → Rastro (direto, sem intermediário)
> **Investimento:** R$ 25.000 (2 meses)
> **Fase atual:** Escopo fechado — aguardando apresentação da proposta
> **Início:** A definir
> **Responsável:** Lucas Cid
> **Case autorizado:** ✅

---

## 🎯 Resumo

A Rastro é uma agência-studio com +10 anos de mercado, 3 divisões (Agency, Films, Labs) e clientes como Nubank, HBO Max, Globo, iFood, Itaú, Unilever. Eles já usam Claude intensamente e têm o **[Rastro Mind](https://rastro-mind-25619.netlify.app/)** — uma wiki LLM de 60MB com conhecimento institucional.

O problema: o Rastro Mind é uma ilha fora do Claude. O time não consegue consultar o conhecimento da empresa de dentro do assistente que já usam o dia todo.

**Solução:** implantar a **Rastro Brain** — instância do MCP Brain Lite que conecta o corpus documental da Rastro aos Claude Desktop do time via MCP, com grafo de conhecimento automático (Mnemosyne) e curadoria humana.

| Fase | O quê | Duração | Pagamento |
|---|---|---|---|
| **Fase A — Consultoria** | Revisão do fluxo de propostas, inventário documental, diagnóstico | ~3 semanas | R$ 12.500 na entrega |
| **Fase B — Implementação** | Deploy da Rastro Brain, ingestão do corpus, conexão dos MCPs, treinamento | ~5 semanas | R$ 12.500 na entrega |

**Produto:** [MCP Brain Lite](https://github.com/CidLucas/mcp_brain_lite) — gateway FastAPI+FastMCP sobre Mnemosyne, OAuth 2.1 via Supabase, escopos pessoal + corporativo.

**Curadoria:** Fábio e Lucas Diárea (Rastro)
**Deploy:** Provável EC2

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
