# Formly — Requisitos Detalhados

> Fase 0 · Fundação | 2026-07-31

---

## 1. Stack & Infra

### 1.1 Monorepo
- **Repo:** `CidLucas/monorepo`
- **Backend:** `services/formly/` (FastAPI, UV workspace)
- **Frontend:** `apps/formly_app/` (Vite + React 18 + Blu DS + Zustand + React Query)
- **Libs:** `blu_auth`, `blu_supabase_client`, `blu_llm_service`, `blu_google_suite_client`, `blu_parsers`, `blu_observability_bootstrap`

### 1.2 Infra
- **Domínio:** `formly.duckdns.org` → `177.19.44.93`
- **Banco:** Supabase (PostgreSQL + RLS)
- **Storage:** S3/R2 (áudios e arquivos)
- **Email:** Resend (transacionais)
- **Observabilidade:** OpenTelemetry + Langfuse

### 1.3 APIs externas
- **LLM:** DeepSeek Flash (geração de questionários)
- **STT:** Groq Whisper (transcrição de áudio) — **Fase 0: transcrição REAL**

---

## 2. Banco de Dados

### 2.1 Tabelas

```sql
CREATE TABLE forms (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES auth.users(id),
    title TEXT NOT NULL,
    description TEXT,
    theme TEXT DEFAULT 'default',
    settings JSONB DEFAULT '{}',
    status TEXT DEFAULT 'draft',  -- draft | published | closed
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE questions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    form_id UUID NOT NULL REFERENCES forms(id) ON DELETE CASCADE,
    type TEXT NOT NULL,  -- short_text | long_text | multiple_choice | etc.
    title TEXT NOT NULL,
    description TEXT,
    required BOOLEAN DEFAULT true,
    config JSONB DEFAULT '{}',  -- choices, scale, file_types, etc.
    sort_order INT NOT NULL DEFAULT 0,
    page INT DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE responses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    form_id UUID NOT NULL REFERENCES forms(id) ON DELETE CASCADE,
    respondent_email TEXT,       -- NULL = anônimo, preenchido = identificado
    completed BOOLEAN DEFAULT false,
    started_at TIMESTAMPTZ DEFAULT now(),
    completed_at TIMESTAMPTZ
);

CREATE TABLE answers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    response_id UUID NOT NULL REFERENCES responses(id) ON DELETE CASCADE,
    question_id UUID NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    value JSONB NOT NULL,        -- string, number, [strings], {row: value}
    audio_url TEXT,              -- S3 (se gravou áudio)
    transcription TEXT,          -- transcrição Groq
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE contacts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES auth.users(id),
    email TEXT NOT NULL,
    name TEXT,
    source TEXT DEFAULT 'manual',  -- google | csv | manual
    created_at TIMESTAMPTZ DEFAULT now(),
    UNIQUE(client_id, email)
);

CREATE TABLE sendings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    form_id UUID NOT NULL REFERENCES forms(id) ON DELETE CASCADE,
    client_id UUID NOT NULL REFERENCES auth.users(id),
    status TEXT DEFAULT 'sending',
    total INT DEFAULT 0, sent INT DEFAULT 0,
    failed INT DEFAULT 0, bounced INT DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE sending_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sending_id UUID NOT NULL REFERENCES sendings(id) ON DELETE CASCADE,
    email TEXT NOT NULL,
    status TEXT NOT NULL,  -- sent | failed | bounced | opened
    error TEXT,
    sent_at TIMESTAMPTZ DEFAULT now()
);
```

### 2.2 RLS

```sql
ALTER TABLE forms ENABLE ROW LEVEL SECURITY;
CREATE POLICY "forms_owner" ON forms FOR ALL USING (client_id = auth.uid());

ALTER TABLE questions ENABLE ROW LEVEL SECURITY;
CREATE POLICY "questions_via_form" ON questions FOR ALL USING (
    form_id IN (SELECT id FROM forms WHERE client_id = auth.uid())
);

ALTER TABLE responses ENABLE ROW LEVEL SECURITY;
CREATE POLICY "responses_select_owner" ON responses FOR SELECT USING (
    form_id IN (SELECT id FROM forms WHERE client_id = auth.uid())
);
CREATE POLICY "responses_insert_public" ON responses FOR INSERT WITH CHECK (true);

ALTER TABLE answers ENABLE ROW LEVEL SECURITY;
CREATE POLICY "answers_select_owner" ON answers FOR SELECT USING (
    response_id IN (
        SELECT r.id FROM responses r
        JOIN forms f ON f.id = r.form_id
        WHERE f.client_id = auth.uid()
    )
);
CREATE POLICY "answers_insert_public" ON answers FOR INSERT WITH CHECK (true);
```

---

## 3. API Endpoints

### 3.1 Forms
| Método | Rota | Auth | Descrição |
|---|---|---|---|
| `POST` | `/v1/forms/generate` | Sim | Prompt → questionário (DeepSeek) |
| `GET` | `/v1/forms` | Sim | Lista questionários do usuário |
| `POST` | `/v1/forms` | Sim | Cria manualmente |
| `GET` | `/v1/forms/{id}` | Sim | Detalhes + perguntas |
| `PUT` | `/v1/forms/{id}` | Sim | Atualiza |
| `DELETE` | `/v1/forms/{id}` | Sim | Remove |
| `POST` | `/v1/forms/{id}/publish` | Sim | Publica |

### 3.2 Questions
| Método | Rota | Auth |
|---|---|---|
| `GET` | `/v1/forms/{id}/questions` | Sim |
| `POST` | `/v1/forms/{id}/questions` | Sim |
| `PUT` | `/v1/forms/{id}/questions/{qid}` | Sim |
| `DELETE` | `/v1/forms/{id}/questions/{qid}` | Sim |
| `PUT` | `/v1/forms/{id}/questions/reorder` | Sim |

### 3.3 Responses
| Método | Rota | Auth |
|---|---|---|
| `GET` | `/r/{form_id}` | Não (HTML) |
| `GET` | `/v1/public/forms/{id}` | Não (JSON) |
| `POST` | `/v1/public/forms/{id}/responses` | Não |
| `GET` | `/v1/forms/{id}/responses` | Sim (dono) |
| `GET` | `/v1/forms/{id}/responses/stats` | Sim (dono) |

### 3.4 Send
| Método | Rota | Auth |
|---|---|---|
| `GET` | `/v1/contacts` | Sim |
| `POST` | `/v1/contacts` | Sim |
| `POST` | `/v1/contacts/upload-csv` | Sim |
| `POST` | `/v1/forms/{id}/send` | Sim |

### 3.5 Áudio
| Método | Rota | Auth |
|---|---|---|
| `POST` | `/v1/audio/transcribe` | Não |


---

## 4. Frontend — Páginas

### 4.0 Landing (`/`)
- "Precisa de um questionário?" + input + botão Gravar áudio
- Enter → `/auth?prompt=...`

### 4.1 Auth (`/auth`)
- Google OAuth + magic link
- Após login → `/builder?prompt=...`

### 4.2 Home (`/home`)
- Lista de questionários do usuário (cards)
- Cada card: título, status (draft/published/closed), data, nº de respostas
- Ações: Editar, Enviar, Ver resultados, Duplicar, Excluir
- Botão "+ Novo questionário" → `/`

### 4.3 Builder (`/builder`)
- `?prompt=` → `POST /v1/forms/generate` → renderiza
- Lista editável: reordenar, adicionar, remover perguntas
- Toggle Editor/Preview
- Gravar áudio para ditar perguntas (criador)
- Publicar → sheet de envio

### 4.4 Send (`/send/{form_id}`)
- Selecionar contatos (Google + CSV + manual)
- Mensagem opcional
- Disparar → confirmação com link público

### 4.5 Analytics (`/analytics/{form_id}`)
- KPIs: respostas, taxa
- Gráficos por tipo de pergunta
- Exportar CSV/PDF

### 4.6 Página pública (`/r/{form_id}`)
- Renderiza questionário com tema
- Responde com texto e/ou áudio
- Respondente anônimo (padrão) ou e-mail opcional
- Tela de obrigado

---

## 5. Requisitos Não-Funcionais

| Requisito | Meta |
|---|---|
| Tempo resposta API | < 500ms p95 |
| Geração IA (prompt → JSON) | < 5s |
| Transcrição áudio (1 min) | < 3s (Groq) |
| Página pública (LCP) | < 1.5s |
| Uptime | 99.5% |
| Observabilidade | OpenTelemetry em todos os serviços |

---

> **Autor:** Hermes PM  
> **Status:** Fase 0 em andamento
