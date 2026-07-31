# Formly — Requisitos Detalhados

> Fase 0 · Fundação | 2026-07-31

---

## 1. Stack & Infra

### 1.1 Monorepo
- **Repo:** `CidLucas/monorepo`
- **Backend:** `services/formly/` (FastAPI, UV workspace)
- **Frontend:** `apps/formly_app/` (Vite + React 18 + Blu DS)
- **Libs reutilizadas:** `blu_auth`, `blu_supabase_client`, `blu_llm_service`, `blu_google_suite_client`, `blu_parsers`, `blu_observability_bootstrap`

### 1.2 Infra
- **Domínio:** `formly.duckdns.org` → `177.19.44.93`
- **Banco:** Supabase (PostgreSQL + RLS)
- **Storage:** S3/R2 (áudios e arquivos)
- **Email:** Resend (transacionais)
- **Observabilidade:** OpenTelemetry + Langfuse (blu_observability_bootstrap)

### 1.3 APIs externas
- **LLM:** DeepSeek Flash (geração de questionários)
- **STT:** Groq Whisper (transcrição de áudio)

---

## 2. Banco de Dados

### 2.1 Tabelas

```sql
-- Questionários
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

-- Perguntas
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

-- Respostas
CREATE TABLE responses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    form_id UUID NOT NULL REFERENCES forms(id) ON DELETE CASCADE,
    respondent_email TEXT,  -- opcional, se capturado
    completed BOOLEAN DEFAULT false,
    started_at TIMESTAMPTZ DEFAULT now(),
    completed_at TIMESTAMPTZ
);

-- Respostas por pergunta
CREATE TABLE answers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    response_id UUID NOT NULL REFERENCES responses(id) ON DELETE CASCADE,
    question_id UUID NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    value JSONB NOT NULL,  -- string, number, [strings], {row: value}
    audio_url TEXT,         -- URL do áudio no S3 (se gravou)
    transcription TEXT,     -- transcrição do áudio
    created_at TIMESTAMPTZ DEFAULT now()
);

-- Contatos do usuário
CREATE TABLE contacts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES auth.users(id),
    email TEXT NOT NULL,
    name TEXT,
    source TEXT DEFAULT 'manual',  -- google | csv | manual
    created_at TIMESTAMPTZ DEFAULT now(),
    UNIQUE(client_id, email)
);

-- Envios
CREATE TABLE sendings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    form_id UUID NOT NULL REFERENCES forms(id) ON DELETE CASCADE,
    client_id UUID NOT NULL REFERENCES auth.users(id),
    status TEXT DEFAULT 'sending',  -- sending | sent | partial | failed
    total INT DEFAULT 0,
    sent INT DEFAULT 0,
    failed INT DEFAULT 0,
    bounced INT DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- Log de envio individual
CREATE TABLE sending_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sending_id UUID NOT NULL REFERENCES sendings(id) ON DELETE CASCADE,
    email TEXT NOT NULL,
    status TEXT NOT NULL,  -- sent | failed | bounced | opened
    error TEXT,
    sent_at TIMESTAMPTZ DEFAULT now()
);
```

### 2.2 RLS (Row Level Security)

```sql
-- forms: só o dono vê
ALTER TABLE forms ENABLE ROW LEVEL SECURITY;
CREATE POLICY "forms_owner" ON forms
    FOR ALL USING (client_id = auth.uid());

-- questions: via form
ALTER TABLE questions ENABLE ROW LEVEL SECURITY;
CREATE POLICY "questions_via_form" ON questions
    FOR ALL USING (
        form_id IN (SELECT id FROM forms WHERE client_id = auth.uid())
    );

-- responses/answers: dono do form vê
ALTER TABLE responses ENABLE ROW LEVEL SECURITY;
CREATE POLICY "responses_via_form" ON responses
    FOR SELECT USING (
        form_id IN (SELECT id FROM forms WHERE client_id = auth.uid())
    );
-- INSERT público (respondente não logado)
CREATE POLICY "responses_insert_public" ON responses
    FOR INSERT WITH CHECK (true);
```

---

## 3. API Endpoints

### 3.1 Forms (autenticado)
| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/v1/forms/generate` | Gera questionário por IA (prompt → JSON) |
| `GET` | `/v1/forms` | Lista questionários do usuário |
| `POST` | `/v1/forms` | Cria questionário manualmente |
| `GET` | `/v1/forms/{id}` | Detalhes do questionário + perguntas |
| `PUT` | `/v1/forms/{id}` | Atualiza título, descrição, settings |
| `DELETE` | `/v1/forms/{id}` | Remove questionário |
| `POST` | `/v1/forms/{id}/publish` | Publica (muda status → published) |

### 3.2 Questions (autenticado)
| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/v1/forms/{id}/questions` | Lista perguntas do form |
| `POST` | `/v1/forms/{id}/questions` | Adiciona pergunta |
| `PUT` | `/v1/forms/{id}/questions/{qid}` | Atualiza pergunta |
| `DELETE` | `/v1/forms/{id}/questions/{qid}` | Remove pergunta |
| `PUT` | `/v1/forms/{id}/questions/reorder` | Reordena perguntas |

### 3.3 Responses (público + autenticado)
| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/r/{form_id}` | Página pública do questionário (HTML) |
| `GET` | `/v1/public/forms/{id}` | Dados públicos do questionário (JSON) |
| `POST` | `/v1/public/forms/{id}/responses` | Submete resposta (anônimo) |
| `GET` | `/v1/forms/{id}/responses` | Lista respostas (dono) |
| `GET` | `/v1/forms/{id}/responses/stats` | Agregações por pergunta (dono) |

### 3.4 Send (autenticado)
| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/v1/contacts` | Lista contatos do usuário |
| `POST` | `/v1/contacts` | Adiciona contato |
| `POST` | `/v1/contacts/upload-csv` | Upload CSV de contatos |
| `POST` | `/v1/forms/{id}/send` | Dispara envio para contatos |

### 3.5 Áudio
| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/v1/audio/transcribe` | Recebe áudio, retorna transcrição (Groq) |

---

## 4. Frontend — Páginas

### 4.0 Landing (`/`)
- Logo "formly" + "Precisa de um questionário?"
- Input de texto + botão Gravar áudio
- Enter → `/auth`

### 4.1 Auth (`/auth`)
- Google OAuth + magic link e-mail
- Primeiro uso: cria conta no Supabase
- Após login → `/builder?prompt=...`

### 4.2 Builder (`/builder`)
- Recebe `?prompt=` → chama `POST /v1/forms/generate`
- Renderiza questionário gerado como lista editável
- Adicionar/remover/reordenar perguntas
- Preview em tempo real (toggle Editor/Preview)
- Botão Publicar → abre sheet de envio

### 4.3 Send (sheet/modal)
- Selecionar contatos (Google Contacts + CSV + manual)
- Mensagem opcional
- Disparar envio
- Tela de confirmação com link público

### 4.4 Analytics (`/analytics/{form_id}`)
- KPIs: respostas, taxa, tempo
- Gráficos por tipo de pergunta
- Exportar CSV/PDF

### 4.5 Página pública (`/r/{form_id}`)
- Renderiza questionário com tema
- Responde (texto + áudio)
- Tela de obrigado ao final

---

## 5. Requisitos Não-Funcionais

| Requisito | Meta |
|---|---|
| Tempo de resposta API | < 500ms p95 |
| Geração IA (prompt → JSON) | < 5s |
| Transcrição áudio (1 min) | < 3s (Groq) |
| Página pública (LCP) | < 1.5s |
| Uptime | 99.5% |
| Observabilidade | OpenTelemetry em todos os serviços |

---

> **Autor:** Hermes PM  
> **Status:** Aguardando início da Fase 0
