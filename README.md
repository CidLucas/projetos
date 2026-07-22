# 📂 Projetos Ativos

Repositório de documentação padrão para os projetos em andamento.

## 🗂 Estrutura

```
.
├── README.md                      ← este arquivo
├── TEMPLATE-PROJETO.md            ← template base pra novos projetos
├── senac/                          ← Projeto SENAC
├── cladtek/                  ← Projeto Cladtek
└── mcp-brain/                     ← Projeto MCP Brain
```

Cada projeto segue o mesmo padrão:

```
<projeto>/
├── README.md          ← visão geral + índice
├── STATUS.md          ← saúde atual, blockers, próximas ações
├── docs/
│   ├── 01-visao.md        ← problema, público, proposta de valor
│   ├── 02-arquitetura.md  ← stack, componentes, fluxos
│   ├── 03-roadmap.md      ← fases, milestones, tarefas de alto nível
│   └── 04-reunioes.md     ← log cronológico de conversas/decisões
├── decisions/         ← ADRs (Architecture Decision Records)
└── assets/            ← diagramas, prints, exports
```

## 📋 Projetos

| Slug | Nome | Cliente / Tipo | Fase |
|---|---|---|---|
| [senac](./senac) | SENAC — Relatórios de Diário de Bordo com IA | SENAC (educação profissional, via Templo) | Descoberta |
| [cladtek](./cladtek) | Pipeline de aprovação de desenhos técnicos | Cladtek (óleo & gás) | Descoberta |
| [mcp-brain](./mcp-brain) | Conector de agentes IA a bases corporativas via Turso + grafo | Produto B2B próprio | Descoberta |

## 🔧 Como adicionar um novo projeto

1. Copie `TEMPLATE-PROJETO.md` para `<novo-slug>/README.md`
2. Crie a estrutura: `mkdir -p <novo-slug>/{docs,decisions,assets}`
3. Preencha os 4 docs padrão
4. Atualize a tabela acima
5. Commit: `git add . && git commit -m "feat: add <novo-slug> project"`
