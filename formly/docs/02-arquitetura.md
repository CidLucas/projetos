# 02 — Arquitetura — Formly

> **Versão:** v0.1 — 2026-07-30
> **Decisões baseadas em:** alinhamento com Lucas Cid (2026-07-30)

---

## 🧱 Stack

| Camada | Tecnologia | Decisão |
|---|---|---|
| Frontend | **Next.js App Router** + React + Tailwind | App Router (server components, streaming, SSR/SSG) |
| Backend | **FastAPI** (Python) | Padrão Deep Blue, async, validação Pydantic |
| Banco | **PostgreSQL** (via Supabase) | Dados relacionais, JSONB pra config flexível |
| Arquivos | **S3** (AWS) ou Cloudflare R2 | Binários (áudios, uploads, logos) |
| Transcrição | **Groq Whisper** | STT rápido e barato |
| LLM | OCI GenAI (Llama) ou Groq | Builder assistido + análise de resultados |
| Auth | **Supabase Auth** | Integrado com PostgreSQL, OAuth social |
| Pagamento | Stripe | Assinatura (Free/Pro/Business) + add-on IA |
| E-mail | Resend | Transacional (link de pesquisa, convite) |
| Infra | Vercel (front) + Railway (back) | Deploy simples, escala automática |

---

## 🗃 Schema do Banco (PostgreSQL)

### Tabelas principais

```
┌─────────────────────────────────────────────────────────────┐
│                        PostgreSQL                            │
│                                                             │
│  users                    surveys                 contacts  │
│  ─────                    ───────                ─────────  │
│  id (UUID)                id (UUID)              id (UUID)  │
│  email                    user_id (FK)           user_id (FK)
│  name                     title                  name       │
│  plan (free/pro/biz)      slug (único, público)  email      │
│  stripe_customer_id       status (draft|pub|arch) phone      │
│                           theme                  groups (text[])
│                           logo_url (S3)                     │
│                           brand_colors (JSONB)              │
│                           created_at                        │
│                           published_at                      │
│                                                             │
│  ┌────────────────────┐                                     │
│  │     questions      │                                     │
│  │     ─────────      │                                     │
│  │  id (UUID)         │                                     │
│  │  survey_id (FK)    │                                     │
│  │  position (int)    │  ← ordem (1, 2, 3...)              │
│  │  type (enum)       │  ← text_short, text_long,          │
│  │  title (text)      │     multiple_choice, audio,        │
│  │  required (bool)   │     scale, file_upload             │
│  │  config (JSONB)    │  ← opções, max_chars, labels...    │
│  │  created_at         │                                     │
│  └────────────────────┘                                     │
│                                                             │
│  ┌────────────────────┐    ┌────────────────────────────┐   │
│  │     responses      │    │         answers            │   │
│  │     ─────────      │    │         ───────            │   │
│  │  id (UUID)         │    │  id (UUID)                 │   │
│  │  survey_id (FK)    │    │  response_id (FK)          │   │
│  │  respondent_ref    │    │  question_id (FK)          │   │
│  │  status            │    │  value_text (text)         │   │
│  │  started_at        │    │  value_choices (JSONB)     │   │
│  │  completed_at      │    │  audio_url (S3)            │   │
│  │  time_spent_secs   │    │  transcription (text)      │   │
│  └────────────────────┘    │  file_url (S3)             │   │
│                            │  file_name (text)          │   │
│                            │  scale_value (int)         │   │
│                            │  created_at                │   │
│                            └────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Detalhe: `questions.config` (JSONB)

Cada tipo de pergunta armazena seus parâmetros dentro de `config`:

| Tipo | Exemplo de `config` |
|---|---|
| `text_short` | `{"max_chars": 500, "placeholder": "Seu nome completo"}` |
| `text_long` | `{"max_chars": 5000, "placeholder": "Conte sua experiência..."}` |
| `multiple_choice` | `{"options": ["Ótimo","Bom","Regular","Ruim"], "multiple": false}` |
| `audio` | `{"max_duration_secs": 60, "follow_up_enabled": true}` |
| `scale` | `{"min": 1, "max": 5, "label_min": "Péssimo", "label_max": "Excelente"}` |
| `file_upload` | `{"allowed_types": ["pdf","jpg","png"], "max_size_mb": 10}` |

### Detalhe: `answers`

Uma linha por pergunta respondida. O campo usado depende do tipo:

| Tipo de pergunta | Campo preenchido |
|---|---|
| `text_short` / `text_long` | `value_text` |
| `multiple_choice` (única) | `value_text` (a opção escolhida) |
| `multiple_choice` (múltipla) | `value_choices` (array de opções) |
| `audio` | `audio_url` + `transcription` |
| `scale` | `scale_value` |
| `file_upload` | `file_url` + `file_name` |

---

## 📡 Fluxos de API

### Criador

```
POST   /api/surveys                    ← Criar novo questionário
GET    /api/surveys                    ← Listar questionários do usuário
GET    /api/surveys/:id                ← Carregar questionário (editar)
PATCH  /api/surveys/:id                ← Atualizar questionário/perguntas
POST   /api/surveys/:id/publish        ← Publicar (gera slug)
PATCH  /api/surveys/:id/status         ← Pausar/Reabrir/Arquivar
DELETE /api/surveys/:id                ← Excluir

GET    /api/contacts                   ← Listar contatos
POST   /api/contacts                   ← Adicionar contato
PATCH  /api/contacts/:id               ← Editar contato
DELETE /api/contacts/:id               ← Excluir contato
POST   /api/contacts/import            ← Importar CSV

POST   /api/surveys/:id/distribute     ← Disparar envio (e-mail/WhatsApp)
```

### Respondente (público)

```
GET    /api/public/surveys/:slug       ← Carregar questionário público
POST   /api/public/surveys/:slug/responses  ← Enviar resposta
POST   /api/public/surveys/:slug/responses/:id/partial  ← Salvar parcial
```

### Transcrição

```
POST   /api/transcribe                 ← Enviar áudio → Groq Whisper → retorna texto
```

### Dashboard

```
GET    /api/surveys/:id/stats          ← Métricas agregadas
GET    /api/surveys/:id/responses      ← Lista de respostas (paginado, filtrável)
GET    /api/surveys/:id/export?format=csv  ← Exportar
```

---

## 🔐 Segurança

- **Row Level Security (RLS):** surveys, contacts, responses — cada user só acessa o seu
- **Rota pública:** `/api/public/*` não requer auth
- **Presigned URLs S3:** upload/download direto, sem passar pelo servidor
- **Rate limit:** 100 respostas/mês (Free), 1000 (Pro), ilimitado (Business)
- **GDPR/LGPD:** deleção em cascata (excluir survey → responses + answers + arquivos)

---

## 🚀 Deploy

```
                    Vercel
                 ┌──────────┐
  Usuário ──────→│ Next.js  │
                 │ (Edge)   │
                 └────┬─────┘
                      │ API calls
                 ┌────▼─────┐
  Railway /      │ FastAPI  │────→ Groq (Whisper + LLM)
  Render         │ (Python) │────→ S3 (presigned URLs)
                 └────┬─────┘────→ Resend (e-mail)
                      │
                 ┌────▼─────┐
                 │ Supabase │
                 │(PostgreSQL│
                 │ + Auth)  │
                 └──────────┘
```

---

## 📐 Decisões arquiteturais (ADR)

| # | Decisão | Data | Justificativa |
|---|---|---|---|
| 1 | PostgreSQL via Supabase (não Turso) | 2026-07-30 | Dados altamente relacionais (surveys→questions→answers), RLS nativo, Supabase Auth integrado |
| 2 | JSONB pra `questions.config` | 2026-07-30 | Cada tipo de pergunta tem parâmetros diferentes; evitar tabela por tipo ou colunas nullable |
| 3 | S3 pra binários (áudio/upload) | 2026-07-30 | PostgreSQL não é eficiente pra blobs; presigned URLs eliminam gargalo de upload |
| 4 | Next.js App Router | 2026-07-30 | Server components reduzem JS no cliente, SSR pra página pública melhor SEO, streaming |
| 5 | Supabase Auth (não Clerk) | 2026-07-30 | Integração nativa com PostgreSQL, RLS, OAuth social incluso |
