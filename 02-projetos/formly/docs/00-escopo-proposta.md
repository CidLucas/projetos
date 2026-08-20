# Formly — Escopo e Proposta

> **Produto Deep Blue** | Fase: 0 — Protótipo funcional | Última atualização: 2026-08-04

---

## 1. Situação Atual

Ferramentas de questionário existentes (Typeform, SurveyMonkey, Google Forms) são maduras mas genéricas. Nenhuma delas oferece **áudio como canal de resposta nativo** com transcrição integrada, nem **análise por IA** como parte do ecossistema.

**Oportunidade:** Um criador de questionários focado no mercado BR, com áudio como canal padrão e IA como camada de análise.

---

## 2. O Que Propomos — Formly

**Fábrica de questionários** — plataforma web onde o usuário cria, distribui e analisa pesquisas.

### 2.1. Experiência do criador
- **Cards editáveis** — monta o questionário por blocos de pergunta (realinhado ao protótipo aprovado)
- **Áudio como input** — dita a pesquisa na landing, transcreve automaticamente, edita antes de seguir
- **Geração por IA** — "me faz uma pesquisa de clima" → IA gera → humano edita
- **Agente de validação** — sugere perguntas complementares (Fase 3)
- **Temas visuais** — design system próprio wine/pine/paper (canônico do protótipo)
- **12 tipos de pergunta** — do texto curto à matriz de escala, NPS, ranking, lista dinâmica

### 2.2. Experiência do respondente
- Link público acessível por qualquer dispositivo (`/s/{slug}`)
- Responde com texto e/ou áudio (áudio é companion do texto longo)
- Áudio transcrito via Groq Whisper
- Modo etapas (progress bar) ou scroll (botão sticky)
- Agente de follow-up que aprofunda respostas superficiais (Fase 3)
- Respondente anônimo (padrão) ou identificado (e-mail opcional — pendente)

### 2.3. Distribuição
- Link público (Fase 0)
- Envio por e-mail com seleção de contatos + CSV upload (Fase 1 — mock hoje)
- WhatsApp e embed (Fase 3)

### 2.4. Resultados
- Dashboard com KPIs e barras por pergunta (analytics.html)
- Exportação CSV (Fase 0)
- Relatórios IA (Fase 4)

---

## 3. Stack (efetiva)

| Camada | Tecnologia |
|---|---|
| Frontend | **Vite + React 18 + TS** + Zustand + react-router-dom + Phosphor Icons |
| Backend | **FastAPI** (Python) + SQLAlchemy |
| Banco | **PostgreSQL 16** (Docker dev) / Supabase (produção) |
| Transcrição | **Groq Whisper** (STT) |
| LLM | **DeepSeek Flash** via `blu_llm_service` |
| Auth | JWT dev (agora) → **Supabase Auth** (produção) |
| Email | **Resend** (Fase 1) |
| Infra | EC2 + Tailscale (dev); Vercel + Railway (prod futuro) |

---

## 4. Fases do Produto (5 fases, 24 semanas)

### Fase 0 — Fundação (semanas 1-3) — 🟡 quase completa
- ✅ Landing page + Auth (dev login; Supabase OAuth pendente)
- ✅ Geração por IA: prompt → questionário (skeleton/refine)
- ✅ Builder: 12 tipos de pergunta, cards editáveis (realinhado ao protótipo)
- ✅ Áudio: transcrição REAL via Groq Whisper, gravação livre com limite 2 min
- ✅ Página pública de resposta (`/s/{slug}`) com 12 tipos
- ⏳ Link público + QR code (pendente)
- ⏳ Supabase schema + observabilidade (pendente)

### Fase 1 — MVP (semanas 4-9)
- ✅ 12 tipos de pergunta (backend + UI)
- ⏳ Temas visuais (3-4) + brand kit
- ✅ Modos de navegação (etapas / scroll)
- ⏳ Envio por e-mail real (contatos + CSV + Resend) — hoje mock
- ✅ Dashboard de respostas v1 (KPIs + barras + export)

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
| **Formly** | ✅ | ✅ | ✅ (F3) | ✅ (F4) | ✅ |

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
| D001 | Stack: Vite + React 18 (SPA) — não Next.js |
| D002 | Monorepo único: `apps/formly_app/` + `services/formly/` |
| D003 | LLM: DeepSeek Flash |
| D004 | Design system próprio wine/pine/paper (protótipo canônico) |
| D005 | 12 tipos de pergunta (realinhamento ao protótipo) |
| D006 | Sem entrada manual de JWT — dev login silencioso / Supabase Auth em prod |
| D007 | Gravação de áudio limitada a 2 minutos |
| D008 | Fase 0: transcrição REAL (Groq) |
| D009 | Respondente: anônimo ou identificado (e-mail opcional) |
| D010 | Banco: PostgreSQL (Docker dev / Supabase prod) |

---

> **Autor:** Hermes PM com input de Lucas Cid
> **Status:** Fase 0 — protótipo funcional commitado (2026-08-04)
> **Próximo passo:** Supabase Auth real + envio de e-mail (Resend)
