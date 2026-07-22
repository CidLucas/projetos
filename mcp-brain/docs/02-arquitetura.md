# 02 — Arquitetura — MCP Brain

> _Esboço inicial. Vai evoluir conforme o posicionamento e a stack forem fechados._

## 🧱 Stack proposta (inicial)

| Camada | Tecnologia | Por quê |
|---|---|---|
| Banco de dados | **Turso** (SQLite distribuído) | já no stack do Lucas; edge; vetorial + relacional num só lugar |
| Vector search | sqlite-vss / libSQL vector | nativo no Turso |
| Grafo de conhecimento | tabela `edges` em Turso + LLM de extração | não precisa de Neo4j na V1 |
| Ingestão | conectores por fonte + LLM de extração | Drive, SharePoint, S3, upload |
| LLM (extração + Q&A) | _a definir_ | _a definir_ |
| Orquestrador de agentes | _a definir_ (Agno?) | padrão Lucas |
| API / Backend | FastAPI (provável) | padrão consistente |
| MCP server | SDK oficial MCP (Python ou TS) | exposição pros agentes externos |
| Frontend | _a definir_ | painel admin (fontes, permissões, métricas) |
| Deploy | _a definir_ | _a definir_ |

## 🔄 Fluxo principal (alto nível)

### Ingestão
```
[Fonte: Drive / SharePoint / S3 / upload]
            ↓
   [Sync incremental]
            ↓
   [Chunking + Embedding]
            ↓
   [Extração de entidades + relações (LLM)]
            ↓
   [Turso: docs + vectors + graph]
```

### Q&A via MCP
```
[Agente externo (Claude, Cursor, Agno, etc.)]
            ↓   (chama tool MCP `brain_query`)
[MCP Brain server]
            ↓
   [Retrieval: hybrid search (vector + keyword + graph)]
            ↓
   [LLM sintetiza resposta com citações]
            ↓
[Resposta com fontes + trechos + entidades]
```

## 🧩 Componentes principais

- **Connectors:** módulos por fonte (Drive, SharePoint, S3, upload). Cada um com sync incremental.
- **Pipeline de ingestão:** chunking → embedding → extração de entidades/relação → write no Turso.
- **Pipeline de retrieval:** hybrid (vector + BM25 + expansão via grafo) + reranker.
- **MCP server:** expõe `brain_query`, `brain_search`, `brain_get_entity`, `brain_graph_neighbors`.
- **Admin API:** gerencia fontes, permissões, métricas.
- **Audit log:** quem consultou o quê, quando.

## 🔌 Integrações externas

- **Turso** (banco).
- **Fontes de documento:** Google Drive, Microsoft SharePoint, AWS S3, upload direto, _futuro: Confluence, Notion_.
- **Spec MCP** pra exposição pros agentes.

## 🔐 Considerações de segurança

- **Multi-tenancy** se for SaaS (isolamento por `org_id` em todas as queries).
- **Permissões por fonte** — espelhar ACLs do Drive/SharePoint.
- **Criptografia em trânsito** (TLS) e **em repouso** (Turso).
- **LGPD / GDPR** — política de retenção configurável, direito ao esquecimento.
- **Audit log** de todo acesso.

## 📐 Decisões arquiteturais (resumo)

Ver [`../decisions/`](../decisions/) para ADRs completos.
_— nenhum registrado —_

## 🧪 Estratégia de testes

- _a definir_ — provavelmente: golden set de Q&A por domínio, eval de retrieval (NDCG, recall@k), e teste de contrato MCP.
