# Formly — Escopo e Proposta

> **Produto Deep Blue** | Fase: Descoberta | Última atualização: 2026-07-30

---

## 1. Situação Atual

Ferramentas de questionário existentes (Typeform, SurveyMonkey, Google Forms) são maduras mas genéricas. Nenhuma delas oferece **áudio como canal de resposta nativo** com transcrição integrada, nem **análise por IA** como parte do ecossistema.

Ao mesmo tempo, consultorias, RH, pesquisa de mercado e negócios em geral precisam cada vez mais de:
- Coleta de dados qualitativos (áudio captura nuances que texto não captura)
- Análise rápida dos resultados (não só gráficos, mas *insights*)
- Redução de fricção para o respondente (falar é mais fácil que digitar)

**Oportunidade:** Um criador de questionários focado no mercado BR, com áudio como canal padrão e IA como camada de análise, pode competir em nichos onde Typeform é overkill e Google Forms é básico demais.

---

## 2. O Que Propomos — Formly

**Fábrica de questionários** — plataforma web onde o usuário cria, distribui e analisa pesquisas com o mínimo de fricção possível.

### 2.1. Experiência do criador (quem monta o questionário)

- **Módulos arrastáveis** — o criador monta o questionário por blocos: múltipla escolha, texto curto, parágrafo, áudio, escala, upload de arquivo
- **Áudio como input do criador** — além de digitar, o criador pode ditar a pergunta em áudio e ela é transcrita automaticamente. Reduz fricção de criação
- **Temas / design systems** — vários temas visuais pré-construídos para o criador escolher (não só cor e logo, mas DNA visual completo: tipografia, espaçamento, tom)
- **Edição fina pós-IA** — o criador pode pedir para a IA gerar um questionário (ex.: "monta uma pesquisa de clima") e depois editar cada detalhe manualmente. A IA acelera, o humano refina
- **Validação por agente** — ao criar uma pergunta, um agente verifica se todos os pontos necessários estão cobertos e sugere perguntas complementares
- **Brand kit** — upload de logo, cores, tipografia da marca do criador. O questionário parece ser dele, não do Formly

### 2.2. Experiência do respondente (quem responde a pesquisa)

- Link público acessível por qualquer dispositivo
- Tipos de resposta: múltipla escolha, texto curto, parágrafo, **áudio** (diferencial)
- Áudio é transcrito automaticamente (API Groq / Whisper)
- **Agente de follow-up** — se uma resposta em texto não cobre todos os pontos que a pergunta pede, um agente faz perguntas complementares na hora, como um entrevistador faria
- Progresso visível (barra de etapas), revisão final antes de enviar
- Respostas armazenadas em base estruturada

### 2.3. Distribuição

- Link compartilhável público (v1)
- QR code para acesso rápido (v1)
- Página web pública do questionário (v1)
- **Fases seguintes:** envio direto para redes de contatos (WhatsApp, e-mail), embutível em sites

### 2.4. Visualização de resultados

- Dashboard com respostas agregadas
- Filtros básicos (por período, por pergunta)
- Exportação (CSV, PDF)

### 2.5. (Upsell futuro) Análise por IA

- Agente que lê todas as respostas e gera relatório de insights
- Análise estatística (correlações, tendências, segmentações)
- Vendido como add-on por pesquisa ou assinatura premium

---

## 3. O Que NÃO Está Incluso (v1)

- White-label completo com domínio próprio do cliente (brand kit sim, domínio não)
- API pública para terceiros
- Integrações nativas com CRM/planilhas (só exportação CSV)
- Coleta de vídeo
- Aplicativo mobile nativo (a web app é responsiva)
- Múltiplos idiomas (v1: PT-BR)
- Mercado de templates público (templates são curados pela Deep Blue)

---

## 4. Diferenciais Competitivos

| Concorrente | Áudio nativo? | Transcrição? | Agente de follow-up? | Temas customizáveis? | Análise IA? | Foco BR? |
|---|---|---|---|---|---|---|
| Typeform | ❌ | ❌ | ❌ | Limitado | ❌ (beta) | ❌ |
| Google Forms | ❌ | ❌ | ❌ | ❌ | ❌ | Parcial |
| SurveyMonkey | ❌ | ❌ | ❌ | ❌ | ❌ (add-on caro) | ❌ |
| Jotform | ❌ | ❌ | ❌ | Limitado | ❌ | ❌ |
| **Formly** | ✅ | ✅ (integrada) | ✅ (valida resposta na hora) | ✅ (design systems múltiplos) | ✅ (upsell) | ✅ |

**Diferencial de entrada:** áudio como canal de resposta nativo + criação por voz.  
**Diferencial de retenção:** agente de follow-up que aprofunda respostas incompletas.  
**Diferencial de monetização:** análise por IA como add-on.

---

## 5. Stack Sugerida

| Camada | Tecnologia |
|---|---|
| Frontend | Next.js / React + Tailwind |
| Backend | FastAPI (Python) |
| Banco | PostgreSQL (dados estruturados) + S3/Blob (áudios) |
| Transcrição | Groq Whisper API (STT) |
| IA / Análise | OCI GenAI (Llama) ou Groq |
| Auth | Supabase Auth ou Clerk |
| Infra | Vercel (front) + Railway/Render (back) |
| Pagamento | Stripe (assinatura + add-on) |

> Stack pode mudar após validação técnica. Groq para transcrição é barato e rápido; OCI GenAI para análise mantém consistência com stack Deep Blue.

---

## 6. Fases do Produto

### Fase 0 — Fundação (2-3 semanas)
**Objetivo:** Provar que o conceito funciona, validar custo de transcrição.

| Entregável | Detalhe |
|---|---|
| Builder básico | Criar questionário com 4 tipos de pergunta (múltipla escolha, texto curto, parágrafo, áudio) |
| Página de resposta | Respondente acessa link, responde (texto + áudio com transcrição Groq) |
| Dashboard simples | Ver respostas agregadas, exportar CSV |
| Teste de custo | 100+ transcrições Groq → medir custo real por resposta |

### Fase 1 — MVP com identidade (4-6 semanas)
**Objetivo:** Produto usável, com personalidade visual, pronto para beta fechado.

| Entregável | Detalhe |
|---|---|
| Módulos arrastáveis | Interface de builder com drag-and-drop de blocos de pergunta |
| Temas / design systems | 3-4 temas visuais pré-construídos (DNA completo: cor, tipografia, tom) |
| Áudio para o criador | Ditar pergunta → transcrição automática |
| Geração IA + edição fina | "Me faz uma pesquisa de clima" → IA gera → humano edita |
| Brand kit básico | Upload de logo + cores do criador |
| Distribuição | Link público + QR code + página web pública |

### Fase 2 — Lançamento beta (3-4 semanas)
**Objetivo:** Primeiros usuários reais, cobrança, onboarding.

| Entregável | Detalhe |
|---|---|
| Onboarding | Fluxo de primeiro questionário guiado |
| Planos (Free / Pro) | Limites por plano + Stripe |
| Domínio próprio | formly.app (ou similar) |
| Página institucional | Landing page pública |

### Fase 3 — Agentes inteligentes (4-6 semanas)
**Objetivo:** Os diferenciais de IA que justificam o premium.

| Entregável | Detalhe |
|---|---|
| Agente de follow-up | Valida se resposta cobre todos os pontos da pergunta; se não, aprofunda |
| Agente de validação (criador) | Ao montar questionário, sugere perguntas complementares |
| Distribuição avançada | Envio por WhatsApp, e-mail, SMS para listas de contatos |

### Fase 4 — Análise & Monetização (4-6 semanas)
**Objetivo:** Serviço adicional de alto valor.

| Entregável | Detalhe |
|---|---|
| Relatórios IA | Agente analisa respostas e gera documento de insights |
| Análise estatística | Correlações, tendências, segmentações |
| Add-on por pesquisa | Cobrança avulsa R$ 29-49/pesquisa ou inclusa no plano Business |

| Marco | Estimativa | Status |
|---|---|---|
| Fase 0 pronta | ~3 semanas | — |
| MVP (Fase 1) | ~9 semanas | — |
| Beta público (Fase 2) | ~13 semanas | — |
| Agentes (Fase 3) | ~18 semanas | — |
| Produto completo (Fase 4) | ~24 semanas | —

---

## 7. Modelo de Negócio (Premissa)

| Plano | Preço/mês (sugestão) | Inclui |
|---|---|---|
| **Free** | R$ 0 | Até 3 questionários ativos, 100 respostas/mês, sem áudio |
| **Pro** | R$ 49-79 | Questionários ilimitados, áudio, exportação, até 1.000 respostas/mês |
| **Business** | R$ 149-199 | Tudo acima + respostas ilimitadas + análise IA em até 5 pesquisas/mês |
| **Add-on IA** | R$ 29-49/pesquisa | Análise avulsa para qualquer plano |

> Premissas a validar com benchmark de mercado e disposição a pagar.

---

## 8. Riscos

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| Mercado muito competitivo (Typeform, GF) | Alta | Médio | Nicho BR + áudio + agentes como diferenciais reais |
| Custo de transcrição (Groq) escala mal | Média | Alto | Cache de transcrições, limite por plano, testar custo real na Fase 0 |
| Áudio não é adotado pelos respondentes | Média | Alto | Fazer o áudio ser *opção*, não obrigação; testar adoção no beta |
| Agente de follow-up irrita em vez de ajudar | Média | Médio | Implementar como opcional (criador escolhe ativar); tom Conversacional e educado |
| Concorrente copia áudio em 3 meses | Média | Médio | Agentes inteligentes são o fosso real; áudio é isca |
| Build interno compete com projetos contratados | Alta | Médio | Fase 0 como projeto paralelo; decidir alocação após validação |
| Complexidade dos design systems atrasa MVP | Média | Médio | Começar com 2 temas, expandir na Fase 2 |

---

## 9. Próximos Passos

1. **Validar escopo** — Lucas revisa e ajusta este documento
2. **Decidir nome final e domínio** — formly.app? formly.com.br? Definir
3. **Pesquisa rápida de mercado** — Preços praticados, concorrentes BR
4. **Protótipo Fase 0** — Builder simples + página de resposta + transcrição Groq
5. **Teste de custo** — 100 transcrições Groq → custo real
6. **Decidir go/no-go** para Fase 1 com dados reais
7. **Definir design systems** — 2-3 temas visuais para o MVP

---

> **Autor:** Hermes PM com input de Lucas Cid  
> **Status:** Aguardando revisão do fundador  
> **Próximo passo:** Lucas revisa e aprova/ajusta escopo
