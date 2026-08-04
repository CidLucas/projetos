# Formly — Roadmap Detalhado

> **Produto Deep Blue** | Última atualização: 2026-08-04

---

## Fase 0 — Fundação (semanas 1-3)

**Objetivo:** Protótipo funcional com transcrição real e realinhamento ao protótipo canônico.

### 0.1 — Landing + Auth
- [x] Landing page: "Precisa de um questionário?" + input + áudio
- [x] Auth page: "Só mais uma coisa" — Google/e-mail (dev login; Supabase OAuth pendente)
- [x] Lead capture: e-mail salvo no localStorage antes de gerar questionário

### 0.2 — Geração por IA
- [x] Endpoint de IA: `POST /api/ai/skeleton` + `/refinement-questions` + `/refine` (DeepSeek Flash via blu_llm_service)
- [x] Prompt engineering: BUILDER_SYSTEM_PROMPT com os 12 tipos de pergunta
- [ ] Fallback: se LLM falhar, retorna template genérico

### 0.3 — Builder (realinhado ao protótipo)
- [x] Cards empilhados em coluna 560px (estilo builder.html)
- [x] 12 tipos de pergunta com preview por tipo
- [x] Editar título inline (textarea auto-resize) e hint
- [x] Adicionar/remover/reordenar/duplicar perguntas
- [x] Autosave + salvar/publicar → `/send/:id`
- [x] Intento da landing (texto/áudio) chega ao builder via sessionStorage

### 0.4 — Áudio (transcrição REAL)
- [x] Endpoint `POST /api/transcribe` → Groq Whisper (até 25MB, qualquer duração)
- [x] Gravador na landing: gravação livre, timer visível, limite 2 min
- [x] Transcrição editável + pede e-mail antes de prosseguir
- [ ] Gravador de áudio no respondente (companion do texto longo — UI presente, testar E2E)
- [ ] Player com waveform + transcrição

### 0.5 — Página de resposta pública
- [x] Rota pública: `/s/{slug}` — renderiza o questionário com os 12 tipos
- [x] Submit de respostas (texto + valores por tipo) + partial
- [x] Modo etapas (progress bar) + modo scroll (botão sticky)
- [x] Tela de abertura (`.screen-intro`) e conclusão (`.screen-done`)
- [ ] Respondente identificado (e-mail opcional) — pendente
- [ ] Link público + QR code — pendente

### 0.6 — Infra
- [x] Backend FastAPI + PostgreSQL 16 (Docker) — 5 tabelas
- [x] Frontend Vite + React 18 + TS
- [x] Dev login (`/api/dev/login`) — 404 quando Supabase configurado
- [ ] Supabase: schema completo em produção
- [ ] Observabilidade bootstrap ativa

**Gate:** Criar questionário por IA/áudio → editar → publicar → responder com texto e áudio. 🟢 Parcialmente atingido (falta QR + respondente identificado).

---

## Fase 1 — MVP (semanas 4-9)

**Objetivo:** Produto completo com todos os tipos de pergunta e envio.

### 1.1 — Tipos de pergunta
- [x] **12 tipos no backend** (enum: text_short, text_long, multiple_choice, audio, scale, file_upload, nps, ranking, matrix, datetime, number, dyn_list) — R2
- [x] UI no builder para os 12 tipos — R4/R5
- [ ] Testes E2E de resposta por tipo via API pública

### 1.2 — Temas visuais
- [ ] 3-4 temas pré-construídos
- [ ] Customização: cor, logo, fonte
- [ ] Preview em tempo real

### 1.3 — Modos de navegação
- [x] Modo etapas (uma pergunta por vez, barra de progresso)
- [x] Modo scroll (todas visíveis, botão sticky)

### 1.4 — Envio por e-mail
- [x] Tela Send: seleção de contatos (busca + CSV upload + manual)
- [x] Endpoint `/distribute` + Resend configurado (envio real validado; free só p/ e-mail verificado)
- [x] Mensagem personalizada opcional
- [x] Banner com link público quando modo simulado
- [ ] Report de entrega (enviados, falhas, bounces)
- [ ] Verificar domínio próprio no Resend (hoje: `onboarding@resend.dev`)

### 1.5 — Home logada
- [ ] `/home` — lista de questionários do usuário
- [ ] Status: draft, published, closed
- [ ] Botão "+ Novo questionário"
- [ ] Ações: editar, enviar, ver resultados, duplicar, excluir

### 1.6 — Dashboard de respostas v1
- [x] KPIs: total de respostas, taxa de resposta, tempo médio
- [x] Barras por pergunta (multiple_choice/scale/nps/ranking/matrix com %, texto/dyn_list com "Ver mais")
- [x] Exportação CSV
- [x] Fix serialize_survey — stats por pergunta carregando de verdade (2026-08-04)
- [ ] Filtro de período (dropdown 7/30/90 dias)

### 1.7 — Qualidade pós-teste (2026-08-04)
- [x] Ranking reordenável em mobile (botões ↑/↓ + drag) — R10
- [x] Botão "Enviar →" sticky no rodapé do builder — R11
- [x] Tela de Preview (`/preview/:id`) antes de enviar — R11

**Gate:** MVP completo — criar, editar, enviar, responder, ver resultados.

---

## Fase 2 — Beta (semanas 10-12)

### 2.1 — Onboarding
- [ ] Fluxo guiado: primeiro questionário em 3 passos
- [ ] Templates sugeridos

### 2.2 — Planos e pagamento
- [ ] Free: 3 questionários, 100 respostas/mês, sem áudio
- [ ] Pro (R$ 49-79): ilimitado, áudio, exportação
- [ ] Stripe integration

### 2.3 — Domínio próprio
- [ ] `formly.app` (ou similar) — futuro
- [ ] Página institucional

---

## Fase 3 — Agentes inteligentes (semanas 13-18)

### 3.1 — Agente de follow-up
- [ ] Detecta respostas curtas/superficiais
- [ ] Gera pergunta de aprofundamento contextual
- [ ] Máx. 1 follow-up por pergunta

### 3.2 — Agente de validação
- [ ] Sugere perguntas complementares ao criar questionário

### 3.3 — Distribuição avançada
- [ ] WhatsApp (blu_twilio_client)
- [ ] Embed (iframe)

---

## Fase 4 — Análise & Monetização (semanas 19-24)

### 4.1 — Relatórios IA
- [ ] Agente analisa respostas → documento de insights
- [ ] Análise estatística: correlações, tendências

### 4.2 — Add-on
- [ ] R$ 29-49 por análise avulsa
- [ ] Ou incluso no plano Business

### 4.3 — Exportação avançada
- [ ] PDF formatado
- [ ] Google Sheets
- [ ] Relatórios recorrentes agendados

---

## Resumo de Marcos

| Marco | Semana | Status |
|---|---|---|
| Fase 0 — Protótipo com áudio real | 1-3 | 🟡 Quase completo (falta QR, respondente identificado, deploy) |
| Fase 1 — MVP completo | 4-9 | 🟡 Em andamento (Send mock, Supabase pendente) |
| Fase 2 — Beta público | 10-12 | ⚪ Planejado |
| Fase 3 — Agentes IA | 13-18 | ⚪ Planejado |
| Fase 4 — Produto completo | 19-24 | ⚪ Planejado |
