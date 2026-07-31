# Formly — Roadmap Detalhado

> **Produto Deep Blue** | Última atualização: 2026-07-31

---

## Fase 0 — Fundação (semanas 1-3)

**Objetivo:** Provar o conceito com um protótipo funcional mínimo.

### 0.1 — Landing + Auth
- [x] Landing page: "Precisa de um questionário?" + input + áudio
- [ ] Auth page: Google OAuth + magic link
- [ ] Lead capture: salva e-mail no Supabase antes de gerar questionário

### 0.2 — Geração por IA
- [ ] Endpoint `POST /v1/forms/generate` — recebe prompt (texto ou transcrição), chama LLM, retorna JSON do questionário
- [ ] Prompt engineering: template que gera questionário com título + perguntas + opções
- [ ] Fallback: se LLM falhar, retorna template genérico

### 0.3 — Builder mínimo
- [ ] Renderizar questionário gerido como lista editável
- [ ] Tipos suportados na Fase 0: texto curto, texto longo, múltipla escolha (única)
- [ ] Editar título e descrição
- [ ] Adicionar/remover/reordenar perguntas
- [ ] Salvar no Supabase

### 0.4 — Página de resposta pública
- [ ] Rota pública: `/r/{form_id}` — renderiza o questionário
- [ ] Submit de respostas (texto)
- [ ] Confirmação de envio

### 0.5 — Teste de custo
- [ ] 100+ transcrições Groq Whisper
- [ ] Medir custo real por minuto de áudio
- [ ] Validar viabilidade econômica

### 0.6 — Infra
- [ ] Serviço `formly` rodando no monorepo (já scaffolded)
- [ ] Supabase: tabelas `forms`, `questions`, `responses`
- [ ] DuckDNS: `formly.duckdns.org` → servidor
- [ ] Observabilidade bootstrap ativa

**Gate de saída:** Protótipo funcional — criar questionário por IA → editar → publicar → responder.

---

## Fase 1 — MVP (semanas 4-9)

**Objetivo:** Produto usável com áudio e identidade visual.

### 1.1 — Áudio como companion
- [ ] Gravador de áudio no builder (criador dita perguntas)
- [ ] Gravador de áudio no respondente (companion do texto longo)
- [ ] Player com waveform + transcrição em tempo real
- [ ] Armazenamento S3/R2

### 1.2 — Todos os 11 tipos de pergunta
- [ ] Texto curto, Texto longo (+ áudio), Múltipla escolha (única e múltipla)
- [ ] Escala Likert (5 e 7 pontos)
- [ ] NPS (0-10)
- [ ] Ranking (drag and drop)
- [ ] Matriz de escala
- [ ] Upload de arquivo (PDF, imagem)
- [ ] Data/Hora
- [ ] Número

### 1.3 — Temas visuais
- [ ] 3-4 temas pré-construídos (design systems completos)
- [ ] Customização: cor primária, logo, fonte
- [ ] Preview em tempo real no builder

### 1.4 — Modos de navegação
- [ ] Modo etapas (uma pergunta por vez, barra de progresso)
- [ ] Modo scroll (todas visíveis)

### 1.5 — Distribuição básica
- [ ] Link público gerado automaticamente
- [ ] QR code para acesso rápido
- [ ] Página web pública do questionário

### 1.6 — Dashboard de respostas (v1)
- [ ] KPIs: total de respostas, taxa de resposta
- [ ] Visualização por tipo: barras, lista de textos
- [ ] Exportação CSV

**Gate de saída:** MVP completo — criar, editar, enviar, responder, ver resultados.

---

## Fase 2 — Lançamento beta (semanas 10-12)

**Objetivo:** Primeiros usuários reais com cobrança.

### 2.1 — Onboarding
- [ ] Fluxo guiado: primeiro questionário em 3 passos
- [ ] Templates sugeridos ("Pesquisa de clima", "Feedback de evento", "NPS")

### 2.2 — Planos e pagamento
- [ ] Free: 3 questionários, 100 respostas/mês, sem áudio
- [ ] Pro (R$ 49-79): ilimitado, áudio, exportação
- [ ] Stripe integration

### 2.3 — Domínio próprio
- [ ] `formly.app` (ou similar)
- [ ] Página institucional (landing de marketing)

### 2.4 — Envio por e-mail
- [ ] Seleção de contatos (Google Contacts + CSV upload)
- [ ] Resend para e-mails transacionais
- [ ] Report de entrega (enviados, falhas, bounces)

**Gate de saída:** Beta público — usuários reais pagando.

---

## Fase 3 — Agentes inteligentes (semanas 13-18)

**Objetivo:** Diferenciais de IA que justificam o premium.

### 3.1 — Agente de follow-up
- [ ] Detecta respostas curtas/superficiais em texto longo
- [ ] Gera pergunta de aprofundamento contextual
- [ ] Máximo de 1 follow-up por pergunta
- [ ] Tom conversacional, não insistente

### 3.2 — Agente de validação (criador)
- [ ] Ao montar questionário, sugere perguntas complementares
- [ ] Detecta gaps: "Você perguntou sobre satisfação mas não sobre recommendação"

### 3.3 — Distribuição avançada
- [ ] Envio por WhatsApp (blu_twilio_client)
- [ ] Embutível em sites (iframe/embed)

---

## Fase 4 — Análise & Monetização (semanas 19-24)

**Objetivo:** Serviço adicional de alto valor.

### 4.1 — Relatórios IA
- [ ] Agente analisa todas as respostas
- [ ] Gera documento de insights (Google Docs)
- [ ] Análise estatística: correlações, tendências, segmentações

### 4.2 — Add-on por pesquisa
- [ ] Cobrança avulsa: R$ 29-49 por análise
- [ ] Ou inclusa no plano Business (R$ 149-199/mês)

### 4.3 — Exportação avançada
- [ ] PDF formatado (relatório executivo)
- [ ] Google Sheets (dados brutos)
- [ ] Agendamento de relatórios recorrentes

---

## Resumo de Marcos

| Marco | Semana | Status |
|---|---|---|
| Fase 0 — Protótipo funcional | 1-3 | 🔴 Não iniciado |
| Fase 1 — MVP com áudio | 4-9 | ⚪ Planejado |
| Fase 2 — Beta público | 10-12 | ⚪ Planejado |
| Fase 3 — Agentes IA | 13-18 | ⚪ Planejado |
| Fase 4 — Produto completo | 19-24 | ⚪ Planejado |
