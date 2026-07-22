# 01 — Visão do Produto MCP Brain

## 🧩 Problema

Empresas têm **base documental enorme e mal organizada** (Drive, SharePoint, Confluence, Notion, sistemas internos, PDFs, e-mails) e querem que seus **agentes de IA** consigam acessar esse conhecimento de forma:

- **Padronizada** (uma interface só, em vez de N integrações).
- **Confiável** (com governança, permissões, auditoria).
- **Contextual** (não só retrieval, mas grafo de entidades/relacionamentos).
- **Edge-friendly** (Turso = SQLite distribuído = funciona em regiões onde Postgres pesado não vai).

Hoje a maioria das empresas **reimplementa isso do zero** cada vez que cria um agente novo. MCP Brain oferece isso **como produto**.

## 👥 Público-alvo

| Persona | Papel | Necessidade |
|---|---|---|
| **CTO / Head de IA em empresa média-grande** | Decide o que comprar | Reduzir tempo de cada projeto de agente |
| **Engenheiro de IA / Platform Engineer** | Integra e mantém | Interface padronizada, fácil de plugar |
| **Usuário final** (interno à empresa cliente) | Faz perguntas ao agente | Respostas com base na documentação real |

_Persona primária a definir — pode ser o engenheiro._

## 💡 Proposta de valor

> **"MCP Brain é a camada de memória corporativa que pluga em qualquer agente via MCP."**

**Pilares:**

1. **Ingestão multi-fonte** — Drive, SharePoint, S3, Confluence, Notion, upload manual.
2. **Turso como banco** — vetorial (embeddings) + relacional (metadados) num único banco edge-distribuído.
3. **Grafo de conhecimento** — entidades e relações extraídas automaticamente, expostas como navegação.
4. **MCP server padrão** — qualquer agente compatível com MCP (Claude, Cursor, Agno, LangGraph) consome via tools.
5. **Governança** — permissões por fonte, auditoria, retenção.

## 🎯 Objetivos de sucesso (métricas)

_— a definir conforme modelo de negócio escolhido —_

Sugestões:
- **Time-to-first-answer** pra novo cliente: < 1 dia.
- **% de fontes suportadas** no Go-To-Market (meta: Drive + SharePoint + S3 + upload na V1).
- **Acurácia de retrieval** em benchmark interno (NDCG@10 > 0.7).
- **NPS de developer** que integrou.

## 🚫 Fora de escopo (versão inicial)

- _a definir_

Sugestões razoáveis de exclusão:
- Geração de documento (Brain **lê e organiza**, não escreve no lugar do usuário na V1).
- Marketplace de conectores de fonte (começar com 3-4 fontes built-in).
- Mobile app.
- Multi-idioma na UI (PT-BR + EN only na V1).

## 📝 Notas / Premissas

- Turso já está no seu stack (Mnemosyne usa). Isso é **vantagem técnica**: você conhece os limites.
- Spec MCP é pública (modelcontextprotocol.io) e tem adoção crescente (Anthropic, OpenAI começaram a suportar).
- "Brain" é metáfora — nome provisório. Pode virar marca depois.
- É **produto**, não projeto para cliente específico — modelo de receita e GTM precisam ser definidos.
