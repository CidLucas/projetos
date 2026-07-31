# Formly — Escopo e Proposta

> **Produto Deep Blue** | Fase: Descoberta | Última atualização: 2026-07-31

---

## 1. Situação Atual

Ferramentas de questionário existentes (Typeform, SurveyMonkey, Google Forms) são maduras mas genéricas. Nenhuma delas oferece **áudio como canal de resposta nativo** com transcrição integrada, nem **análise por IA** como parte do ecossistema.

**Oportunidade:** Um criador de questionários focado no mercado BR, com áudio como canal padrão e IA como camada de análise.

---

## 2. O Que Propomos — Formly

**Fábrica de questionários** — plataforma web onde o usuário cria, distribui e analisa pesquisas.

### 2.1. Experiência do criador
- **Módulos arrastáveis** — monta o questionário por blocos de pergunta
- **Áudio como input** — dita perguntas, transcreve automaticamente
- **Geração por IA** — "me faz uma pesquisa de clima" → IA gera → humano edita
- **Agente de validação** — sugere perguntas complementares (Fase 3)
- **Temas visuais** — design systems pré-construídos + brand kit
- **11 tipos de pergunta** — do texto curto à matriz de escala

### 2.2. Experiência do respondente
- Link público acessível por qualquer dispositivo
- Responde com texto e/ou áudio (áudio é companion do texto longo)
- Áudio transcrito via Groq Whisper
- Agente de follow-up que aprofunda respostas superficiais (Fase 3)
- Respondente pode ser anônimo ou identificado (e-mail opcional)

### 2.3. Distribuição
- Link público + QR code (Fase 0)
- Envio por e-mail com seleção de contatos + CSV upload (Fase 1)
- WhatsApp e embed (Fase 3)

### 2.4. Resultados
- Dashboard com respostas agregadas
- Exportação CSV, PDF
- Relatórios IA (Fase 4)

---

## 3. Stack

| Camada | Tecnologia |
|---|---|
| Frontend | **Vite + React 18 + Blu DS** + Zustand + React Query + Phosphor Icons |
| Backend | **FastAPI** (Python) no monorepo `CidLucas/monorepo` |
| Banco | **Supabase** (PostgreSQL + RLS) |
| Storage | **S3 / R2** (áudios e arquivos) |
| Transcrição | **Groq Whisper** (STT) |
| LLM | **DeepSeek Flash** |
| Auth | **Supabase Auth** (Google OAuth + magic link) |
| Email | **Resend** (transacionais) |
| Google Workspace | **`blu_google_suite_client`** (import Forms, export Docs/Sheets) |
| File Parsing | **Blue Parsis** (`blu_parsers`) |
| Observabilidade | **OpenTelemetry** (`blu_observability_bootstrap`) |
| Infra | Servidor próprio, **DuckDNS** (`formly.duckdns.org`) |

### Libs reutilizadas do monorepo
| Lib | Uso |
|---|---|
| `blu_auth` | JWT / Supabase Auth |
| `blu_supabase_client` | Conexão Supabase |
| `blu_llm_service` | LLM routing (DeepSeek) |
| `blu_google_suite_client` | Google Forms, Docs, Sheets |
| `blu_parsers` | PDF, CSV parsing |
| `blu_observability_bootstrap` | OpenTelemetry + Langfuse |

---

## 4. Fases do Produto (5 fases, 24 semanas)

### Fase 0 — Fundação (semanas 1-3)
- Landing page + Auth (Google OAuth + magic link)
- Geração por IA: prompt → questionário
- Builder mínimo: 3 tipos de pergunta (texto curto, texto longo + áudio companion, múltipla escolha única)
- Áudio: transcrição REAL via Groq Whisper (não simulada)
- Página pública de resposta
- Link público + QR code
- Schema Supabase + observabilidade

### Fase 1 — MVP (semanas 4-9)
- Todos os 11 tipos de pergunta
- Gravador de áudio no builder (criador dita perguntas)
- Temas visuais (3-4) + brand kit
- Modos de navegação (etapas / scroll)
- Envio por e-mail (contatos Google + CSV + Resend)
- Dashboard de respostas v1

### Fase 2 — Beta (semanas 10-12)
- Onboarding guiado
- Planos Free/Pro + Stripe
- Domínio próprio (futuro)
- Report de entrega (enviados, falhas, bounces)

### Fase 3 — Agentes IA (semanas 13-18)
- Agente de follow-up (aprofunda respostas)
- Agente de validação (sugere perguntas)
- WhatsApp + embed

### Fase 4 — Análise (semanas 19-24)
- Relatórios IA (insights, correlações)
- Add-on por pesquisa
- Exportação avançada (PDF, Google Sheets)

---

## 5. O Que NÃO Está Incluso (v1)
- White-label com domínio próprio
- API pública para terceiros
- Coleta de vídeo
- App mobile nativo
- Múltiplos idiomas (v1: PT-BR)

---

## 6. Diferenciais Competitivos

| Concorrente | Áudio? | Transcrição? | Agente follow-up? | IA análise? | Foco BR? |
|---|---|---|---|---|---|
| Typeform | ❌ | ❌ | ❌ | ❌ (beta) | ❌ |
| Google Forms | ❌ | ❌ | ❌ | ❌ | Parcial |
| SurveyMonkey | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Formly** | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 7. Modelo de Negócio

| Plano | Preço/mês | Inclui |
|---|---|---|
| Free | R$ 0 | 3 questionários, 100 respostas/mês, sem áudio |
| Pro | R$ 49-79 | Ilimitado, áudio, exportação |
| Business | R$ 149-199 | + análise IA em 5 pesquisas/mês |
| Add-on IA | R$ 29-49/pesquisa | Análise avulsa |

---

## 8. Riscos

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| Custo transcrição escala mal | Média | Alto | Testar custo real na Fase 0, cache, limite por plano |
| Áudio não adotado | Média | Alto | Opcional, não obrigatório |
| Concorrente copia áudio | Média | Médio | Agentes IA são o fosso real |
| Build compete com projetos | Alta | Médio | Fase 0 como paralelo |

---

## 9. Decisões de Arquitetura

| # | Decisão |
|---|---|
| D001 | Stack: Vite + React 18 + Blu DS |
| D002 | Monorepo único: `apps/formly_app/` + `services/formly/` |
| D003 | LLM: DeepSeek Flash |
| D004 | Google Workspace: `blu_google_suite_client` |
| D005 | File Parsing: Blue Parsis |
| D006 | Observabilidade: `blu_observability_bootstrap` |
| D007 | Domínio dev: DuckDNS `formly.duckdns.org` |
| D008 | Fase 0: transcrição REAL (Groq) |
| D009 | Home logada: `/home` |
| D010 | Respondente: anônimo ou identificado (e-mail opcional) |

---

> **Autor:** Hermes PM com input de Lucas Cid  
> **Status:** Fase 0 — protótipo em andamento  
> **Próximo passo:** Auth page + endpoint `/v1/forms/generate`
