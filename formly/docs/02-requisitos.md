# Formly — Requisitos Detalhados

> Fase 0 · Fundação — implementada | 2026-08-04

---

## 1. Stack & Infra (efetiva)

### 1.1 Repositórios
- **Repo de código:** `CidLucas/formly` (monorepo do produto: `apps/formly_app/` + `services/formly/`)
- **Backend:** `services/formly/` — FastAPI + SQLAlchemy, venv Python 3.12
- **Frontend:** `apps/formly_app/` — Vite + React 18 + TS + Zustand + react-router-dom + Phosphor Icons
- **Hub (docs/requisitos):** `CidLucas/projetos` → `formly/`

### 1.2 Infra (dev)
- **Backend:** uvicorn `:8000` (script `scripts/dev-backend.sh`)
- **Frontend:** Vite `:5173` (proxy `/api` → 8000)
- **Banco:** PostgreSQL 16 em Docker (container `formly-pg`, porta 5432)
- **Acesso dev:** Tailscale `100.69.231.7` (front :5173 / back :8000)

### 1.3 APIs externas
- **LLM:** DeepSeek Flash via `blu_llm_service` (geração de questionários)
- **STT:** Groq Whisper `whisper-large-v3-turbo` (transcrição de áudio, máx 25MB)

---

## 2. Banco de Dados (implementado)

### 2.1 Tabelas (5 — SQLAlchemy `models.py`)

| Tabela | Campos principais |
|---|---|
| `surveys` | id, user_id, title, slug (único), status, description, theme, logo_url, brand_colors (JSONB), created_at, updated_at |
| `questions` | id, survey_id (FK), position, type (enum 12), title, required, config (JSONB) |
| `responses` | id, survey_id (FK), respondent_ref, status (complete/partial), started_at, completed_at, time_spent_secs |
| `answers` | id, response_id (FK), question_id (FK), value_text, value_choices (JSONB), audio_url, transcription, file_url, file_name, scale_value |
| `contacts` | id, user_id, name, email, phone, groups (text[]) |

### 2.2 Enum `QuestionType` — 12 tipos

`text_short, text_long, multiple_choice, audio, scale, file_upload, nps, ranking, matrix, datetime, number, dyn_list`

---

## 3. API Endpoints (implementados)

### 3.1 Surveys (auth dev)
| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/api/surveys/` | Lista |
| `POST` | `/api/surveys/` | Cria |
| `GET` | `/api/surveys/{id}` | Detalhes + perguntas |
| `PATCH` | `/api/surveys/{id}` | Atualiza (autosave) |
| `POST` | `/api/surveys/{id}/publish` | Publica (gera slug) |
| `GET` | `/api/surveys/{id}/responses` | Respostas (com time_spent_secs) |
| `GET` | `/api/surveys/{id}/stats` | Métricas |
| `GET` | `/api/surveys/{id}/export` | CSV (com BOM) |

### 3.2 IA
| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/api/ai/skeleton` | Prompt → questionário |
| `POST` | `/api/ai/refinement-questions` | Perguntas de refinamento |
| `POST` | `/api/ai/refine` | Refina com respostas |

### 3.3 Público
| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/api/public/surveys/{slug}` | Questionário público |
| `POST` | `/api/public/surveys/{slug}/responses` | Envia resposta |
| `POST` | `/api/public/surveys/{slug}/responses/partial` | Rascunho parcial |

### 3.4 Outros
| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/api/transcribe` | Áudio → texto (Groq) |
| `POST` | `/api/dev/login` | JWT dev (404 se Supabase ativo) |
| `GET` | `/api/contacts` | Contatos |

---

## 4. Frontend — Páginas (implementadas)

### 4.0 Landing (`/`) — ✅
"Precisa de um questionário?" + input grande + botão "Gravar áudio" pill com dot pulsante.
- Enter no input → review (e-mail se não salvo) → `/builder`
- Gravar: MediaRecorder, **timer visível, limite 2 min**, para no clique
- Transcrição editável → e-mail → `/builder?description=...`

### 4.1 Auth (`/auth`) — ✅ (dev)
"Só mais uma coisa" — botão "Continuar com Google" + divider + form e-mail.
- Em dev: ambos chamam `/api/dev/login` (JWT local)
- TODO no código: plugar Supabase OAuth quando configurado

### 4.2 Builder (`/builder/:id?`) — ✅
Cards empilhados (coluna 560px), header com título editável + "+ Pergunta" / "Enviar →".
- Card: título (textarea auto-resize), badge de tipo (13 opções), hint, preview do componente, toolbar (obrigatória, mover, duplicar, excluir), config por tipo
- Autosave 2s → `PATCH /api/surveys/{id}`; "Enviar →" → publica → `/send/{id}`
- Sem JWT manual; intent da landing em `sessionStorage.formly_intent`

### 4.3 Send (`/send/:id`) — ✅ (envio real via Resend)
"Enviar: {título}" — busca contatos, "Todos/Selecionados (N)", lista com checkboxes, divider + CSV (parse client-side), mensagem opcional, botão "Enviar questionário →".
- Chama `POST /api/surveys/{id}/distribute` com contatos selecionados + e-mails CSV + mensagem
- Sem seleção → aviso "Selecione ao menos um contato ou importe um CSV"
- Resend configurado → envio real; sem `RESEND_API_KEY` → modo simulado com banner verde + link público copiável
- Sucesso → navega `/dashboard/{id}`; erro → reabilita botão

### 4.4 Analytics (`/dashboard/:id`) — ✅
`.back`, título + "Exportar CSV", 3 KPIs (Respostas + "de N enviados", Taxa de resposta, Tempo médio), "Respostas por pergunta" com barras animadas (fix serialize_survey), empty state com copiar link público.

### 4.5 Survey (`/s/:slug`) — ✅
Abertura (`.screen-intro`), modo etapas com progress bar ou scroll com botão sticky, 12 tipos com classes wine/pine/paper, conclusão (`.screen-done`), envia `time_spent_secs`. Ranking com botões ↑/↓ (mobile) + drag (desktop).

### 4.6 Preview (`/preview/:id`) — ✅
Renderiza o questionário como o respondente vê (reusa componentes do Survey), sem envio real. Header: "← Voltar" (builder) + "Confirmar e enviar →" (send).

---

## 5. Requisitos Não-Funcionais

| Requisito | Meta | Estado |
|---|---|---|
| Tempo resposta API | < 500ms p95 | 🟢 OK em dev |
| Geração IA (prompt → JSON) | < 5s | 🟡 depende DeepSeek |
| Transcrição áudio (1 min) | < 3s (Groq) | 🟢 OK |
| Página pública (LCP) | < 1.5s | 🟢 SPA leve |
| Sem scroll horizontal em textos longos | — | 🟢 overflow-wrap + auto-resize (R8) |
| Gravação de áudio | livre até 2 min | 🟢 limite implementado |
| Observabilidade | OpenTelemetry | 🔴 pendente |

---

> **Autor:** Hermes PM
> **Status:** Fase 0 implementada e commitada (2026-08-04)
