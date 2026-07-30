# 📱 Requisitos de Aplicação — Formly

> **Versão:** v0.1 — 2026-07-30
> **Baseado em:** Google Doc de escopo + input de voz do Lucas
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

**Formly** é uma fábrica de questionários com áudio como canal nativo de resposta. O criador monta pesquisas conversando com uma IA (chat) e refinando manualmente (editor direto). O respondente acessa um link público e responde com texto ou áudio. O criador visualiza os resultados num dashboard.

### Páginas

| Página | Arquivo | Quem usa |
|---|---|---|
| **Criador (Builder)** | `pagina-01-criador.md` | Quem monta o questionário |
| **Respondente** | `pagina-02-respondente.md` | Quem responde a pesquisa |
| **Dashboard** | `pagina-03-dashboard.md` | Quem criou a pesquisa (ver resultados) |

### Públicos

| Persona | Necessidade |
|---|---|
| **Criador** (consultor, RH, pesquisador) | Montar questionário rápido, distribuir, ver resultados |
| **Respondente** (cliente, funcionário, público) | Responder pesquisa com mínima fricção |
| **Admin/Curador** (Deep Blue) | Gerenciar templates, temas, monitorar uso |

---

## 2. Elementos de UI (Shell)

### Layout global (criador)

```
┌──────────────────────────────────────────────────────┐
│ Topbar: [Formly logo] [Questionário: Nome] [Publicar] │
├──────────────────────┬───────────────────────────────┤
│                      │                               │
│    Chat Panel        │    Canvas / Preview            │
│    (conversa c/ IA)  │    (questionário renderizado)  │
│                      │                               │
│    [input voz/texto] │    ┌─────────────────────┐     │
│                      │    │ 1. Qual seu nome?   │     │
│                      │    │    [______________]  │     │
│                      │    │ 2. Avalie o serviço │     │
│                      │    │    ○ 1 ○ 2 ○ 3 ○ 4 ○ 5│  │
│                      │    │ 3. Conte sua exp.   │     │
│                      │    │    [🎤 Gravar áudio] │     │
│                      │    └─────────────────────┘     │
│                      │                               │
└──────────────────────┴───────────────────────────────┘
```

### Layout global (respondente)

```
┌──────────────────────────────────────┐
│ Logo + Nome da pesquisa + Progresso  │
├──────────────────────────────────────┤
│                                      │
│   Pergunta atual (uma por tela)      │
│                                      │
│   [ componentes de resposta ]        │
│                                      │
│   [← Anterior]          [Próximo →]  │
│                                      │
└──────────────────────────────────────┘
```

### Design System

- **A definir:** Blu Design System (existente) vs novo DS próprio do Formly
- **Temas:** múltiplos temas visuais pré-construídos (DNA completo: tipografia, espaçamento, tom)
- **Brand kit:** upload de logo + cores do criador → questionário parece ser dele
- **Responsivo:** web app funciona em desktop e mobile

---

## 3. Fluxos

### 3.1 Criar questionário (fluxo 4 passos + publicação)

```
PASSO 1: INPUT
  Usuário descreve o que precisa (texto ou 🎤 voz)
  Ex: "Preciso de uma pesquisa de satisfação pós-evento com 8 perguntas"
  Forma de interação: Conversa (chat)

PASSO 2: REFINAMENTO
  Sistema faz 1-2 perguntas para afinar o escopo
  Ex: "Qual o público? Quer incluir pergunta de áudio?"
  Forma de interação: Conversa (chat)

PASSO 3: GERAÇÃO
  Sistema propõe esqueleto com tipos de pergunta
  Aparece no canvas: lista de perguntas com tipos sugeridos
  Forma de interação: Visual (canvas) — IA gerou, usuário vê

PASSO 4: AJUSTE
  Usuário refina — 3 formas de interação COEXISTEM:
  a) Conversa: "Troca a pergunta 5 por uma de áudio"
  b) Edição direta: clica no texto e edita
  c) Drag & drop: reordena perguntas
  d) Painel de propriedades: muda tipo, opções, obrigatoriedade

PASSO 5: PUBLICAÇÃO
  Usuário clica "Publicar"
  → Link público gerado
  → QR code gerado
  → Página web funcional com todos os componentes renderizados
  → Componentes já ligados na API (prontos para receber respostas)

PASSO 6: DISTRIBUIÇÃO
  Usuário seleciona contatos (lista de e-mails / números)
  → Envia link por e-mail, WhatsApp, ou copia link
  → (Fase 3) envio direto para listas de contatos
```

### 3.2 Responder questionário

```
1. Respondente acessa link público
2. Vê tela de abertura (título, descrição, logo)
3. Pergunta por pergunta (uma por tela)
   - Responde com texto, escolha, ou áudio
   - Áudio é enviado → transcrito (Groq) → armazenado
4. Se resposta é incompleta → agente de follow-up pergunta mais
5. Tela de revisão final antes de enviar
6. Tela de agradecimento
```

### 3.3 Visualizar resultados

```
1. Criador acessa dashboard da pesquisa
2. Vê respostas agregadas (gráficos, contagens)
3. Filtra por período, pergunta
4. Exporta CSV/PDF
5. (Fase 4) Gera relatório IA com insights
```

---

## 4. Regras de Negócio

### Componentes de pergunta (tipos)

| Tipo | Entrada do respondente | Comportamento |
|---|---|---|
| **Múltipla escolha** | Selecionar 1 ou N opções | Opções definidas pelo criador |
| **Texto curto** | Input texto 1 linha | Máx. 500 caracteres |
| **Parágrafo** | Textarea multilinha | Máx. 5000 caracteres |
| **Áudio** | Gravação de voz | Transcrição automática (Groq), áudio armazenado |
| **Escala** | 1-5 / 1-10 | Label nos extremos (ex: "Péssimo" — "Excelente") |
| **Upload de arquivo** | Selecionar arquivo | Formatos: PDF, imagem, DOCX (v1) |

### Publicação

- Link público único por questionário (UUID)
- Página renderiza componentes do design system escolhido
- Componentes já conectados ao backend (POST /api/responses/:surveyId)
- Sem necessidade de build/deploy — publicação é instantânea

### Distribuição

- V1: link copiável + QR code
- V1: envio manual (criador copia link e envia por onde quiser)
- Fase 3: envio direto por WhatsApp, e-mail, SMS
- Contatos: lista gerenciada pelo criador (nome + e-mail/telefone)

### Planos (limites)

| Limite | Free | Pro | Business |
|---|---|---|---|
| Questionários ativos | 3 | Ilimitado | Ilimitado |
| Respostas/mês | 100 | 1.000 | Ilimitado |
| Áudio | ❌ | ✅ | ✅ |
| Exportação | CSV | CSV + PDF | CSV + PDF |
| Análise IA | ❌ | ❌ | 5/mês |

---

## 5. Integrações

| Integração | Propósito | Status |
|---|---|---|
| **Groq (Whisper)** | Transcrição de áudio | A definir |
| **Supabase Auth** | Autenticação de criadores | A definir |
| **Stripe** | Cobrança (planos + add-on IA) | Fase 2 |
| **PostgreSQL** | Dados estruturados (perguntas, respostas) | A definir |
| **S3 / Blob storage** | Armazenamento de áudios e uploads | A definir |
| **OCI GenAI / Groq** | Geração de questionários + análise IA | A definir |
| **E-mail (Resend/SES)** | Envio de links de distribuição | Fase 3 |
| **WhatsApp Business API** | Envio de links por WhatsApp | Fase 3 |

---

## 6. Cenários de Teste

### Builder
- [ ] Criador descreve pesquisa por texto → IA gera esqueleto em < 10s
- [ ] Criador dita pesquisa por áudio → transcrito → IA gera esqueleto
- [ ] IA faz pergunta de refinamento → criador responde → esqueleto ajustado
- [ ] Criador edita pergunta diretamente no canvas (clica + digita)
- [ ] Criador reordena perguntas por drag & drop
- [ ] Criador muda tipo de pergunta (múltipla escolha → áudio)
- [ ] Criador adiciona pergunta via chat ("adiciona uma pergunta de escala")
- [ ] Criador remove pergunta via chat ("remove a pergunta 3")
- [ ] Preview em tempo real reflete mudanças
- [ ] Publicar → link gerado → página funcional

### Respondente
- [ ] Acessa link → vê questionário com tema correto
- [ ] Responde pergunta de múltipla escolha → avança
- [ ] Grava áudio → barra de progresso → transcrito
- [ ] Resposta incompleta → agente de follow-up pergunta mais
- [ ] Revisão final → vê todas as respostas → confirma envio
- [ ] Tela de agradecimento

### Distribuição
- [ ] Criador copia link → cola em qualquer lugar → funciona
- [ ] QR code escaneável → abre questionário no celular
- [ ] Selecionar contatos → enviar e-mail com link
