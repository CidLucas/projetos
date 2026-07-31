# Formly — Roadmap Detalhado

> **Produto Deep Blue** | Última atualização: 2026-07-31

---

## Fase 0 — Fundação (semanas 1-3)

**Objetivo:** Protótipo funcional com transcrição real.

### 0.1 — Landing + Auth
- [x] Landing page: "Precisa de um questionário?" + input + áudio
- [ ] Auth page: Google OAuth + magic link
- [ ] Lead capture: salva e-mail no Supabase antes de gerar questionário

### 0.2 — Geração por IA
- [ ] Endpoint `POST /v1/forms/generate` — recebe prompt, chama DeepSeek Flash, retorna JSON
- [ ] Prompt engineering: template que gera questionário com título + perguntas + opções
- [ ] Fallback: se LLM falhar, retorna template genérico

### 0.3 — Builder mínimo
- [ ] Renderizar questionário gerado como lista editável
- [ ] Tipos: texto curto, texto longo (+ áudio companion), múltipla escolha (única)
- [ ] Editar título e descrição
- [ ] Adicionar/remover/reordenar perguntas
- [ ] Salvar no Supabase

### 0.4 — Áudio (transcrição REAL)
- [ ] Endpoint `POST /v1/audio/transcribe` → Groq Whisper
- [ ] Gravador de áudio no builder (criador dita prompt)
- [ ] Gravador de áudio no respondente (companion do texto longo)
- [ ] Player com waveform + transcrição

### 0.5 — Página de resposta pública
- [ ] Rota pública: `/r/{form_id}` — renderiza o questionário
- [ ] Submit de respostas (texto + áudio)
- [ ] Respondente anônimo (padrão) ou identificado (e-mail opcional)
- [ ] Confirmação de envio
- [ ] Link público + QR code

### 0.6 — Infra
- [x] Serviço `formly` scaffolded no monorepo
- [ ] Supabase: schema completo (forms, questions, responses, answers, contacts, sendings)
- [x] DuckDNS: `formly.duckdns.org`
- [ ] Observabilidade bootstrap ativa

**Gate:** Criar questionário por IA → editar → publicar → responder com texto e áudio.

---

## Fase 1 — MVP (semanas 4-9)

**Objetivo:** Produto completo com todos os tipos de pergunta e envio.

### 1.1 — Todos os 11 tipos de pergunta
- [ ] Texto curto, Texto longo (+ áudio), Múltipla escolha (única e múltipla)
- [ ] Escala Likert (5 e 7 pontos)
- [ ] NPS (0-10)
- [ ] Ranking (drag and drop)
- [ ] Matriz de escala
- [ ] Upload de arquivo (PDF, imagem)
- [ ] Data/Hora
- [ ] Número

### 1.2 — Temas visuais
- [ ] 3-4 temas pré-construídos
- [ ] Customização: cor, logo, fonte
- [ ] Preview em tempo real

### 1.3 — Modos de navegação
- [ ] Modo etapas (uma pergunta por vez, barra de progresso)
- [ ] Modo scroll (todas visíveis)

### 1.4 — Envio por e-mail
- [ ] Tela Send: seleção de contatos (Google + CSV upload + manual)
- [ ] Resend para e-mails transacionais
- [ ] Mensagem personalizada opcional
- [ ] Report de entrega (enviados, falhas, bounces)

### 1.5 — Home logada
- [ ] `/home` — lista de questionários do usuário
- [ ] Status: draft, published, closed
- [ ] Botão "+ Novo questionário"
- [ ] Ações: editar, enviar, ver resultados, duplicar, excluir

### 1.6 — Dashboard de respostas v1
- [ ] KPIs: total, taxa de resposta
- [ ] Visualização por tipo: barras, lista de textos
- [ ] Exportação CSV

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
| Fase 0 — Protótipo com áudio real | 1-3 | 🔴 Em andamento |
| Fase 1 — MVP completo | 4-9 | ⚪ Planejado |
| Fase 2 — Beta público | 10-12 | ⚪ Planejado |
| Fase 3 — Agentes IA | 13-18 | ⚪ Planejado |
| Fase 4 — Produto completo | 19-24 | ⚪ Planejado |
