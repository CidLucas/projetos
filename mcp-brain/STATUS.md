# Status — MCP Brain

> Última atualização: 2026-07-22

## 🩺 Saúde geral

🟡 **Em descoberta** — definindo posicionamento, escopo da V1, e quais features são o mínimo vendável.

## 📊 Resumo executivo

| Item | Status |
|---|---|
| Posicionamento claro | 🟡 parcial |
| Escopo da V1 definido | 🔴 não |
| Stack escolhida | 🟡 Turso confirmado; resto a definir |
| Repos de código criado | 🔴 não |
| Primeiro cliente-piloto | 🔴 não |
| Prazo de lançamento | 🔴 não |

## 🚧 Blockers / Riscos

- _nenhum registrado_

## 🎯 Próximas ações (próximas 7 dias)

- [ ] **Lucas** — definir 1 frase de posicionamento ("X pra Y")
- [ ] **Lucas** — listar 3 casos de uso de referência (1 simples, 1 médio, 1 ambicioso)
- [ ] **Lucas** — decidir se o grafo é **núcleo do produto** ou **feature opcional** da V1
- [ ] **Hermes** — esboçar arquitetura em `docs/02-arquitetura.md` com base no posicionamento
- [ ] **Lucas** — mapear concorrentes: Glean, Hebbia, Mem, contexto, Notion AI Q&A, etc.

## ❓ Perguntas em aberto

1. V1 é self-hosted (empresa roda na própria infra) ou SaaS multi-tenant (você roda)?
2. Conecta em quais fontes? (Drive, SharePoint, S3, Confluence, Notion, sistemas internos?)
3. O "grafo de conhecimento" é exposto via MCP como tool/consulta, ou só usado internamente pra melhorar retrieval?
4. Qual a persona primária — admin/IT da empresa, usuário final, ou developer de agentes?
5. Modelo de cobrança — por usuário, por GB indexado, por chamada MCP?
6. O que é o "brain" tecnicamente — só RAG sobre docs, ou algo mais estruturado (ontologias, entidades, regras)?

## 📅 Histórico de atualizações

| Data | Atualização |
|---|---|
| 2026-07-22 | Criação do projeto. Pasta + docs placeholder. |
