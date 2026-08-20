# 🏢 Visão da Empresa — Deep Blue

> Contexto de quem somos — alimenta todos os agentes e procedimentos.

## Missão

IA aplicada a negócios: agentes, automações e produtos que resolvem problemas
reais de PMEs e clientes corporativos.

## Posicionamento

- **IA como ferramenta de negócio** (não "IA por IA") — cada entrega resolve
  um problema concreto e mensurável.
- **Produtos próprios + projetos de cliente** (ex.: SENAC, Cladtek, Rastro).
- **Execução com agentes**: pipeline de produção de código automatizado,
  documentado em [01-procedimentos](../01-procedimentos/).

## Stack tecnológica

| Camada | Tecnologia |
|---|---|
| Backend | FastAPI (Python 3.12) |
| Frontend | React + TypeScript + Vite |
| Banco | Supabase + Neon (Postgres) |
| Agentes | Agno (novo padrão) · LangGraph (legado, migrando) |
| Integração | MCP (tool_pool_api como hub) |
| Browser/automação | Playwright |
| Orquestração | Hermes Agent (crons, watchdog, filas) |
| Deploy | GCP (Cloud Run), Neon |
| Observabilidade | Langfuse, Grafana Cloud |

## Produtos próprios

- **Plataforma Blu** — escritório virtual com IA para PMEs
- **Agente Bloqüo** — agente com RAG + MCP
- **MCP Brain** — conector de agentes IA a bases corporativas
- **Assistente Pessoal** — navegação web autônoma + integrações (em build)

## Clientes

- SENAC · Cladtek · Rastro · Guanabara · (ver [clientes.md](./clientes.md) quando criado)

## Materiais

- [materiais/](./materiais/) — assets, textos, referências (inclui LinkedIn)
