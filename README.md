# 📂 Projetos Ativos

Repositório de documentação padrão para os projetos em andamento.
Todo profile Hermes entrega os artefatos aqui seguindo o [`TEMPLATE-DELIVERABLE.md`](./TEMPLATE-DELIVERABLE.md).

## 🗂 Estrutura

```
.
├── README.md                      ← este arquivo
├── TEMPLATE-PROJETO.md            ← template base pra novos projetos
├── TEMPLATE-DELIVERABLE.md        ← padrão de entrega pra todos os profiles
├── __profiles__/                  ← entregáveis por profile/agente
├── senac/                          ← Projeto SENAC
├── cladtek/                        ← Projeto Cladtek
├── mcp-brain/                      ← Projeto MCP Brain
├── plataforma-blu/                 ← Plataforma Blu (escritório virtual IA)
└── agente-bloquo/                  ← Agente Bloqüo (RAG + MCP)
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

Os perfis de agente documentam seus entregáveis em `__profiles__/<nome>/`.

## 📋 Projetos

| Slug | Nome | Cliente / Tipo | Fase |
|---|---|---|---|
| [plataforma-blu](./plataforma-blu) | Plataforma Blu — Escritório virtual com IA | Produto próprio | Build |
| [agente-bloquo](./agente-bloquo) | Agente Bloqüo — RAG + MCP autônomo | Produto próprio | Build |
| [senac](./senac) | SENAC — Relatórios de Diário de Bordo com IA | SENAC (via Templo) | Pré-contrato |
| [cladtek](./cladtek) | Cladtek — Sistema agêntico de engenharia (desenhos + BID) | Cladtek (via Templo) | Pré-contrato |
| [mcp-brain](./mcp-brain) | Conector de agentes IA a bases corporativas | Produto B2B próprio | Descoberta |

## 🔧 Como adicionar um novo projeto

1. Copie `TEMPLATE-PROJETO.md` para `<novo-slug>/README.md`
2. Crie a estrutura: `mkdir -p <novo-slug>/{docs,decisions,assets}`
3. Preencha os 4 docs padrão
4. Atualize a tabela acima
5. Commit: `feat: add <novo-slug> project`

## 📦 Como entregar artefatos (todos os profiles)

Consulte [`TEMPLATE-DELIVERABLE.md`](./TEMPLATE-DELIVERABLE.md) para saber:
- Onde entregar cada tipo de artefato (GitHub / Google Drive / EC2 Preview)
- O formato esperado
- O checklist de entrega

## 🔗 Preview Server (Tailscale)

Previews HTML são servidos em:
```
http://100.69.231.7:8080/previews/<projeto>/
```
Acessível apenas via Tailscale (tailnet).
