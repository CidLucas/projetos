# 02 — Arquitetura da Solução

## 🧱 Stack proposta

| Camada | Tecnologia | Por quê |
|---|---|---|
| **Motor de busca/grafo** | [Mnemosyne](https://pypi.org/project/mnemosyne-memory/) | Vetor + grafo integrados, mesmo motor já usado no MCP Brain Lite |
| **Gateway MCP** | FastAPI + FastMCP | Exposição do corpus como ferramentas MCP (`memory_search`, `memory_recall`, `graph_neighbors`) |
| **Auth** | Supabase Auth (OAuth 2.1, DCR + PKCE) | Control plane de identidade, já implementado no Brain Lite |
| **Control plane** | Supabase (Postgres) | Quem existe, quem pode abrir o quê, grants de escopo |
| **Banks (armazenamento)** | Mnemosyne em disco (`/data/tenants/{t}/`) | 3 banks: `corp` (curadoria), `personal` (1 escritor), `restricted` (V2) |
| **Cliente** | Claude Desktop (MCP config) | O agente que consome as ferramentas |
| **Deploy** | Docker em VPS (Hetzner/O CI) | Simples, barato, já documentado no Brain Lite |
| **Observabilidade** | OTLP → ops-centro | Métricas, traces, healthcheck |

## 🔄 Arquitetura de alto nível

```
┌─────────────────────────────────────────────────────────┐
│                   Rastro (5-10 pessoas)                  │
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ Claude   │  │ Claude   │  │ Claude   │   ...        │
│  │ Desktop  │  │ Desktop  │  │ Desktop  │              │
│  │ (Pessoa1)│  │ (Pessoa2)│  │ (Pessoa3)│              │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘              │
│       │             │             │                     │
│       │  MCP (stdio → HTTP)       │                     │
│       │             │             │                     │
└───────┼─────────────┼─────────────┼─────────────────────┘
        │             │             │
        ▼             ▼             ▼
┌─────────────────────────────────────────────────────────┐
│               MCP Brain Lite Gateway                     │
│            (FastAPI + FastMCP + OAuth)                   │
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐   │
│  │ Auth     │  │ Control  │  │ Tools MCP             │   │
│  │ Supabase │  │ Plane    │  │ • memory_search       │   │
│  │ OAuth    │  │ (grants) │  │ • memory_recall       │   │
│  │ 2.1      │  │          │  │ • graph_neighbors     │   │
│  └──────────┘  └──────────┘  │ • list_sources        │   │
│                               └──────────┬───────────┘   │
└──────────────────────────────────────────┼──────────────┘
                                           │
                                           ▼
┌─────────────────────────────────────────────────────────┐
│               Banks Mnemosyne (disco)                    │
│                                                         │
│  /data/tenants/rastro/                                  │
│  ├── corp/         ← propostas, briefings, orçamentos,  │
│  │                    wiki LLM, cases, templates        │
│  ├── personal/     ← 1 por usuário (anotações, rascunhos)│
│  └── restricted/   ← V2 (grant-based)                   │
└─────────────────────────────────────────────────────────┘
```

## 🔄 Fluxo principal — Consulta ao corpus

```
[Pessoa no Claude Desktop]
        │  "Me mostra propostas de branded content com orçamento acima de R$ 100k"
        ▼
[Claude Desktop invoca tool MCP: memory_search]
        │
        ▼
[Gateway FastAPI + FastMCP]
        │  1. Valida token OAuth (Supabase)
        │  2. Resolve tenant + escopos do usuário
        │  3. Cache de instância Mnemosyne por tenant
        ▼
[Mnemosyne bank corp]
        │  Busca híbrida: vetor (similaridade) + keyword (BM25/FTS)
        │  + expansão via grafo (entidades relacionadas)
        ▼
[Resultados ranqueados + fontes]
        │
        ▼
[Claude Desktop sintetiza resposta com citações]
```

## 🔄 Fluxo principal — Ingestão de documento

```
[Curador(a) designado(a)]
        │  Upload de PDF/DOCX/TXT/MD via endpoint de ingestão
        ▼
[Gateway: valida auth + escopo (só curador escreve no corp)]
        │
        ▼
[Pipeline Mnemosyne (assíncrono)]
        │  1. Chunking
        │  2. Embedding
        │  3. Extração de entidades + relações (LLM)
        │  4. Indexação no banco corp
        ▼
[Documento disponível para consulta]
```

## 🔌 Integrações

| Integração | Propósito |
|---|---|
| **Supabase** | Auth (OAuth 2.1), control plane (usuários, grants, tenants) |
| **Mnemosyne** | Motor de busca vetorial + grafo de conhecimento |
| **Claude Desktop (x5–10)** | Clientes MCP — cada pessoa conecta seu Claude ao gateway |
| **ops-centro** | Observabilidade (OTLP traces + métricas + healthcheck) |

## 🔐 Segurança

| Camada | Mecanismo |
|---|---|
| **Autenticação** | OAuth 2.1 via Supabase (DCR + PKCE). Cada pessoa tem credencial própria |
| **Autorização** | Grants por escopo: `corp:read` (todos), `corp:write` (só curadores), `personal` (1 dono) |
| **Isolamento** | Banks Mnemosyne em disco separados por tenant e escopo. Sem cruzamento entre tenants |
| **Trânsito** | TLS no gateway |
| **Auditoria** | Log de queries no ops-centro (quem consultou o quê, quando) |

## 📐 Decisões arquiteturais

| # | Decisão | Justificativa |
|---|---|---|
| **A1** | MCP Brain Lite (não Brain completo) | Brain completo tem stack multi-tenant com Qdrant+FalkorDB — overkill para 1 tenant de 5–10 pessoas. Brain Lite é monolítico, simples de deploy e manter |
| **A2** | Mnemosyne em disco (não Turso/SQLite) | Brain Lite já usa banks em disco. Para 60MB de corpus, não tem gargalo de I/O |
| **A3** | Curadoria humana no `corp` | O corpus de propostas é sensível — não pode ter ingestão automática sem revisão. Curadores designados aprovam o que entra |
| **A4** | Sem ingestão automática de Drive/SharePoint na V1 | Upload manual + curadoria garante qualidade. Conectores automáticos são V2 |
| **A5** | 1 tenant = "rastro" | Sem multi-tenancy — desnecessário para um único cliente |
