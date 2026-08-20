# 02 — Arquitetura — Formly

> **Versão:** v0.2 — 2026-08-04
> **Decisões baseadas em:** realinhamento ao protótipo canônico + implementação real

---

## 🧱 Stack (efetiva)

| Camada | Tecnologia | Decisão |
|---|---|---|
| Frontend | **Vite + React 18 + TS** | Zustand + react-router-dom + Phosphor Icons. Design system próprio wine/pine/paper (não Blu DS) |
| Backend | **FastAPI** (Python) | Async, Pydantic, SQLAlchemy |
| Banco | **PostgreSQL 16** (Docker `formly-pg` em dev; Supabase em produção) | Relacional, JSONB |
| Transcrição | **Groq Whisper** (`whisper-large-v3-turbo`) | STT rápido; `POST /api/transcribe`, máx 25MB |
| LLM | **DeepSeek Flash** (via `blu_llm_service`) | Geração do questionário (skeleton/refine/refinement) |
| Auth | **JWT dev** (`/api/dev/login`) agora; **Supabase Auth** em produção | dev login retorna 404 se `SUPABASE_URL` configurada |
| E-mail | **Resend** (planejado — Fase 1) | Hoje o Send usa mock |
| Storage | S3/R2 (planejado) | Áudios/arquivos futuros |
| Infra | EC2 + Tailscale (dev) | Front :5173, Back :8000 |

## 🎨 Design System (canônico)

Tokens extraídos do protótipo (`site/*.html`) e implementados em `apps/formly_app/src/styles/global.css`:

| Categoria | Tokens |
|---|---|
| Primária | `--wine: #7A2E3F`, `--wine-soft: #F5E8EB`, `--wine-dark: #5C1E2C` |
| Secundária | `--pine: #3B5B52`, `--pine-soft: #E8F0ED` |
| Superfície | `--paper: #E7E6E0`, `--paper-2: #F3F2EE`, `--card: #FCFBF8` |
| Texto | `--muted: #6E6D66`, `--line: #C9C7BE`, `--ink: #1a1a1a` |
| Fontes | `--display` (Helvetica Neue), `--body` (Georgia), `--mono` (SF Mono) |
| Raio | `--radius-sm: 6px`, `--radius: 12px` |

## 🗃 Schema do Banco (PostgreSQL — 5 tabelas)

```
┌─────────────────────────────────────────────────────────────┐
│                        PostgreSQL                            │
│                                                             │
│  surveys                 questions                contacts  │
│  ───────                 ─────────                ─────────  │
│  id (UUID)               id (UUID)                id (UUID)  │
│  user_id (FK)            survey_id (FK)           user_id (FK)
│  title                   position (int)           name       │
│  slug (único, público)   type (enum 12)           email      │
│  status (draft|pub)      title (text)             phone      │
│  description             required (bool)          groups (text[])
│  theme                   config (JSONB)                     │
│  logo_url                created_at                         │
│  brand_colors (JSONB)                                        │
│  created_at / updated_at                                     │
│                                                             │
│  ┌────────────────────┐    ┌────────────────────────────┐   │
│  │     responses      │    │         answers            │   │
│  │     ─────────      │    │         ───────            │   │
│  │  id (UUID)         │    │  id (UUID)                 │   │
│  │  survey_id (FK)    │    │  response_id (FK)          │   │
│  │  respondent_ref    │    │  question_id (FK)          │   │
│  │  status            │    │  value_text (text)         │   │
│  │  started_at        │    │  value_choices (JSONB)     │   │
│  │  completed_at      │    │  audio_url / transcription │   │
│  │  time_spent_secs   │    │  file_url / file_name      │   │
│  └────────────────────┘    │  scale_value (int)         │   │
│                            │  created_at                │   │
│                            └────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### `questions.type` — 12 tipos (enum `QuestionType`)

| # | Tipo | config JSONB |
|---|---|---|
| T01 | `text_short` | `{"max_chars": 500, "placeholder": "..."}` |
| T02 | `text_long` | `{"max_chars": 400, "audio_enabled": true}` |
| T03 | `multiple_choice` (única) | `{"options": [...], "multiple": false}` |
| T04 | `multiple_choice` (múltipla) | `{"options": [...], "multiple": true}` |
| T05 | `scale` | `{"min": 1, "max": 5, "labels": [...], "na_option": true}` |
| T06 | `nps` | `{"min": 0, "max": 10}` |
| T07 | `ranking` | `{"options": [...]}` |
| T08 | `matrix` | `{"rows": [...], "columns": [...]}` |
| T09 | `file_upload` | `{"allowed_types": [...], "max_size_mb": 10}` |
| T10 | `datetime` | `{"include_time": true}` |
| T11 | `number` | `{"min": 1, "max": 500}` |
| T12 | `dyn_list` | `{"suggestions": [...], "placeholder": "..."}` |

## 📡 Rotas de API (efetivas)

### Criador (auth dev)
```
POST   /api/surveys/                    ← Criar
GET    /api/surveys/                    ← Listar
GET    /api/surveys/{id}                ← Carregar (com perguntas — serialize_survey)
PATCH  /api/surveys/{id}                ← Atualizar (autosave)
POST   /api/surveys/{id}/publish        ← Publicar (gera slug)
POST   /api/surveys/{id}/distribute     ← Enviar p/ contatos (Resend real ou simulado)
GET    /api/surveys/{id}/responses      ← Listar respostas
GET    /api/surveys/{id}/stats          ← Métricas (total, taxa, tempo médio)
GET    /api/surveys/{id}/export         ← CSV (com BOM)
GET    /api/contacts                    ← Contatos
POST   /api/dev/login                   ← JWT dev (404 se Supabase ativo)
```

### IA
```
POST   /api/ai/skeleton                 ← Prompt → questionário (DeepSeek)
POST   /api/ai/refinement-questions     ← Perguntas de refinamento
POST   /api/ai/refine                   ← Refinar com respostas
```

### Respondente (público)
```
GET    /api/public/surveys/{slug}                  ← Questionário público
POST   /api/public/surveys/{slug}/responses        ← Enviar resposta
POST   /api/public/surveys/{slug}/responses/partial ← Rascunho parcial
```

### Transcrição
```
POST   /api/transcribe                  ← Áudio → Groq Whisper → texto (máx 25MB)
```

## 🗺 Frontend — 6 rotas

| Rota | Página | Origem |
|---|---|---|
| `/` | Landing — "Precisa de um questionário?" + input/áudio | `index.html` |
| `/auth` | Auth — "Só mais uma coisa" + Google/e-mail | `auth.html` |
| `/builder/:id?` | Builder — cards empilhados, 12 tipos, botão enviar sticky | `builder.html` |
| `/preview/:id` | Preview — form como o respondente vê, antes de enviar | `formly-tipos-v2.html` |
| `/send/:id` | Send — contatos + CSV + mensagem + envio Resend | `send.html` |
| `/s/:slug` | Survey — página pública de resposta (etapas/scroll) | `formly-tipos-v2.html` |
| `/dashboard/:id` | Analytics — KPIs + barras + export | `analytics.html` |

## 🔐 Segurança

- **Dev login protegido:** `/api/dev/login` retorna 404 quando `SUPABASE_URL` está configurada — nunca ativo em produção
- **Auth:** JWT HS256 local (dev); Supabase Auth + RLS em produção
- **Limite de upload:** 25MB por arquivo de áudio
- **CORS:** restrito a localhost:5173 (dev)
- **LGPD:** deleção em cascata (excluir survey → responses + answers)

## 🚀 Deploy (planejado)

```
                    EC2 (dev) — Tailscale 100.69.231.7
                 ┌──────────────┐
  Usuário ──────→│ Vite :5173   │
                 │ (dev server) │
                 └──────┬───────┘
                        │ /api proxy
                 ┌──────▼───────┐
                 │ FastAPI :8000 │────→ Groq (Whisper)
                 │ (uvicorn)     │────→ DeepSeek Flash (LLM)
                 └──────┬───────┘
                 ┌──────▼───────┐
                 │ PostgreSQL 16│ (Docker formly-pg)
                 └──────────────┘
```

Produção: Supabase (PostgreSQL + Auth + RLS) + Vercel (front) + Railway (back) — quando configurado.

## 📐 Decisões arquiteturais (ADR)

| # | Decisão | Data | Justificativa |
|---|---|---|---|
| 1 | PostgreSQL (Docker dev / Supabase prod) | 2026-07-30 | Dados relacionais surveys→questions→answers; RLS nativo |
| 2 | JSONB pra `questions.config` | 2026-07-30 | Cada tipo tem parâmetros diferentes |
| 3 | Vite + React 18 (não Next.js) | 2026-07-30 | Padrão Blu V3; SPA simples |
| 4 | **12 tipos de pergunta** (não 6/11) | 2026-08-01 | Alinhado ao protótipo canônico (formly-tipos-v2) |
| 5 | **Design system próprio** wine/pine/paper (não Blu DS) | 2026-08-01 | Protótipo aprovado pelo cliente define o tema editorial |
| 6 | **Sem entrada manual de JWT** no fluxo | 2026-08-01 | Protótipo não tem token bar; dev login silencioso |
| 7 | Gravação de áudio limitada a 2 min | 2026-08-04 | Decisão de produto (evita áudios gigantes) |
