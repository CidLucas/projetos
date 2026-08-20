# 🤝 Clientes — Deep Blue

> Resumo comercial de cada cliente: propostas, apresentações, documentação.
> **Detalhes técnicos/execução** ficam em `02-projetos/<projeto>/`.

| Cliente | Segmento | Status | Proposta/Deck | Projeto (execução) |
|---|---|---|---|---|
| [SENAC](./senac/) | Educação | Pré-kickoff | — | [02-projetos/senac](../02-projetos/senac/) |
| [Cladtek](./cladtek/) | Petróleo (tubos) | Pré-contrato | — | [02-projetos/cladtek](../02-projetos/cladtek/) |
| [Rastro](./rastro/) | Publicidade | Pré-proposta | [v5](./rastro/propostas/proposta-rastro-v5.md) · [v6](./rastro/propostas/proposta-rastro-v6.md) | [02-projetos/rastro](../02-projetos/rastro/) |
| [Guanabara](./guanabara/) | Supermercados | Proposta enviada | [v6](./guanabara/propostas/proposta-v6.html) | [02-projetos/guanabara](../02-projetos/guanabara/) |
| [Formly](./formly/) | Produto interno | — | — | [02-projetos/formly](../02-projetos/formly/) |
| [MCP Brain](./mcp-brain/) | B2B próprio | Descoberta | — | [02-projetos/mcp-brain](../02-projetos/mcp-brain/) |

## Estrutura por cliente

```
clientes/<cliente>/
├── README.md          ← resumo: quem é, contexto, status comercial
├── propostas/         ← propostas comerciais (versões)
├── apresentacoes/     ← decks e materiais de apresentação
└── docs/              ← documentação específica do cliente (briefing, contrato)
```

## Regra

- **Resumo** (README de cada cliente) — visão rápida de 5-10 linhas.
- **Execução técnica** — sempre em `02-projetos/` (não duplicar aqui).
- Propostas/contratos são confidenciais — não commitar dados sensíveis além do necessário.
