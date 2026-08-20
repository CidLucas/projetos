# 03 — Roadmap — MCP Brain

## 🗺 Fases

### Fase 0 — Descoberta (atual 🟡)
- [ ] Posicionamento de 1 frase
- [ ] Casos de uso de referência (3)
- [ ] Decisão: grafo é core ou opcional?
- [ ] Decisão: self-hosted vs SaaS vs ambos
- [ ] Análise de concorrentes (Glean, Hebbia, contexto, Mem, Notion AI)
- [ ] Modelo de precificação (ideia inicial)

### Fase 1 — Especificação
- [ ] Arquitetura detalhada
- [ ] Schema do Turso (docs, chunks, vectors, entities, edges)
- [ ] Contrato MCP (tools expostas)
- [ ] Conectores prioritários da V1
- [ ] Plano de segurança / multi-tenancy

### Fase 2 — Build V1
- [ ] Setup do repo (mono ou polirepo)
- [ ] Pipeline de ingestão (1 fonte: upload)
- [ ] Retrieval híbrido (vector + BM25)
- [ ] MCP server com 3-4 tools
- [ ] CLI de demo
- [ ] Deploy demo público

### Fase 3 — Validação / Beta
- [ ] Mais conectores (Drive, SharePoint, S3)
- [ ] Grafo de conhecimento (extração + query)
- [ ] Painel admin mínimo
- [ ] 2-3 clientes beta
- [ ] Iteração com feedback

### Fase 4 — GA (General Availability)
- [ ] Pricing público
- [ ] Documentação de developer
- [ ] Site / landing
- [ ] Suporte básico
- [ ] SLA

## 📅 Milestones

| Marco | Data alvo | Status |
|---|---|---|
| M1 — Posicionamento + escopo V1 fechados | _a definir_ | 🔴 |
| M2 — Demo fim-a-fim (upload → Q&A via MCP) | _a definir_ | 🔴 |
| M3 — Beta com 1 cliente-piloto | _a definir_ | 🔴 |
| M4 — GA | _a definir_ | 🔴 |

## ⚠️ Riscos do roadmap

- **Concorrência** — Glean e Hebbia já estão no mercado com muito funding. Diferenciação precisa ser clara (Turso + grafo + simplicidade?).
- **Adoção do MCP** — se a spec não pegar tração, o "MCP" como interface vira âncora.
- **Multi-tenancy + segurança** — se for SaaS, compliance (SOC2, LGPD, GDPR) é caro e demorado.
- **Custo por tenant** — embeddings + LLM calls + storage escalam com uso. Precisa de pricing que cubra.
- **Complexidade do grafo** — extração automática de entidades é ruidosa; pode ser feature da V2 em vez de V1.
