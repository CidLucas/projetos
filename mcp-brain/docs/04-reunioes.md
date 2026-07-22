# 04 — Log de Reuniões e Decisões — MCP Brain

> Formato: 1 entrada por conversa/reunião relevante. Cronológico inverso (mais recente em cima).

---

## 2026-07-22 — Criação do projeto

**Participantes:** Lucas + Hermes
**Canal:** Telegram (DM)

**Resumo:**
- Lucas descreveu o produto: conector de agentes de IA à base de arquivos corporativa, usando Turso como banco e grafo de conhecimento. Exposição via MCP.
- Tipo: **produto B2B próprio** (não projeto pra cliente específico).
- Fase: descoberta — sem posicionamento nem escopo V1 fechado.
- Diferencial identificado: combinação Turso (já conhecido) + MCP (spec em ascensão) + grafo.
- Estrutura padrão de documentação criada no repo `CidLucas/projetos`.

**Próximos passos:**
- Lucas definir 1 frase de posicionamento.
- Lucas listar 3 casos de uso de referência.
- Lucas decidir se grafo é core da V1 ou feature V2.
- Lucas decidir self-hosted vs SaaS.
- Hermes esboçar arquitetura inicial.

**Decisões tomadas:**
- Documentação versionada no GitHub (não Google Drive) por enquanto.
- Estrutura padrão: `README + STATUS + docs/{01-visao,02-arquitetura,03-roadmap,04-reunioes} + decisions/ + assets/`.
- Stack provisória: Turso (confirmado) + FastAPI + MCP SDK + Agno (provável).

**Perguntas registradas:** ver `STATUS.md` (6 perguntas em aberto).

**Concorrentes初步 mapeados (a aprofundar):** Glean, Hebbia, Mem, contexto, Notion AI Q&A.
