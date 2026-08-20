# 📱 Requisitos de Aplicação — Formly

> **Versão:** v0.2 — 2026-08-01
> **Baseado em:** Site HTML estático (5 arquivos) + Google Doc de escopo
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)
> **Status:** 🟡 Site estático implementado; backend e página do respondente pendentes

---

## 1. Visão Geral

**Formly** é uma plataforma web para criação, coleta e análise de questionários. Diferencia-se dos concorrentes (Typeform, Google Forms, SurveyMonkey) por oferecer **áudio como canal de resposta nativo** com transcrição automática e **análise por IA**.

### Objetivo da aplicação

Permitir que um usuário:
1. **Descreva** o questionário que precisa (texto ou áudio) — Landing
2. **Autentique-se** via Google ou e-mail — Auth
3. **Crie/edite** questionários com múltiplos tipos de pergunta — Builder
4. **Envie** para contatos (manual, CSV) — Send
5. **Analise** resultados com KPIs e gráficos — Analytics
6. **(Futuro)** Colete respostas do público com suporte a áudio — Página do Respondente

### Páginas

| # | Página | Arquivo | Status |
|---|---|---|---|
| 0 | **Landing** | `pagina-00-landing.md` | ✅ Implementado |
| 1 | **Auth** | `pagina-01-auth.md` | ✅ Implementado |
| 2 | **Builder** | `pagina-02-builder.md` | ✅ Implementado |
| 3 | **Send** | `pagina-03-send.md` | ✅ Implementado |
| 4 | **Analytics** | `pagina-04-analytics.md` | ✅ Implementado |
| 5 | **Página do Respondente** | `pagina-05-resposta.md` | 🔴 Aspirational |

### Fluxo de navegação

```
Landing → Auth → Builder → Send → Analytics
  │         │        │         │         │
  │         │        │    ← Voltar    ← Voltar
  └─ Enter ─┘        │
                [Enviar →]
```

### Público-alvo

- **Criador:** profissional que precisa aplicar pesquisas (RH, consultor, pesquisador, professor)
- **Respondente:** público final que acessa o link e responde
- **Analista:** mesmo criador, visualizando resultados

---

## 2. Elementos de UI — Design System

O Formly implementa um design system próprio com CSS custom properties — **não é Blu DS**. Tema editorial com paleta vinho/papel e tipografia serif.

### Cores

| Token | Valor | Uso |
|---|---|---|
| `--wine` | `#7A2E3F` | Primária — logo, botões, foco, destaques |
| `--wine-soft` | `#F5E8EB` | Background hover/selecionado |
| `--wine-dark` | `#5C1E2C` | Hover de botões primários |
| `--pine` | `#3B5B52` | Secundária — CSV zone preenchido |
| `--pine-soft` | `#E8F0ED` | Background CSV zone preenchido |
| `--paper` | `#E7E6E0` | Background geral |
| `--paper2` | `#F3F2EE` | Background secundário (inputs, listas) |
| `--card` | `#FCFBF8` | Background de cards e inputs |
| `--muted` | `#6E6D66` | Texto secundário, placeholders |
| `--line` | `#C9C7BE` | Bordas, divisores |

### Tipografia

| Token | Font Stack | Uso |
|---|---|---|
| `--display` | `'Helvetica Neue', Helvetica, Arial, sans-serif` | Títulos, labels, botões, badges |
| `--body` | `Georgia, 'Times New Roman', Times, serif` | Texto corrido, inputs, descrições |
| `--mono` | `'SF Mono', 'Fira Code', monospace` | Badges, contadores, labels pequenas |

### Espaçamento

| Token | Valor |
|---|---|
| `--s` | `8px` |
| `--m` | `16px` |
| `--l` | `24px` |
| `--xl` | `40px` |
| `--r` | `6px` (bordas pequenas) |
| `--rl` | `12px` (bordas de cards) |
| `--ease` | `cubic-bezier(.4,0,.2,1)` |
| `--fast` | `150ms` |
| `--norm` | `250ms` |

### Layout

- **Landing/Auth:** tela cheia centralizada, max-width 360-480px
- **Builder:** max-width 560px centralizado, header + corpo de cards
- **Send/Analytics:** max-width 560px centralizado
- **Respondente:** layout limpo e focado, largura máxima ~700px centralizado

---

## 3. Fluxos

### Fluxo principal (implementado no site)

```
[Landing] → descreve (texto/áudio) → Enter
    ↓
[Auth] → Google OAuth ou magic link e-mail
    ↓
[Builder] → vê 6 perguntas de amostra → edita → "+ Pergunta" → [Enviar →]
    ↓
[Send] → seleciona contatos (+ CSV opcional) → mensagem opcional → [Enviar]
    ↓
[Analytics] → KPIs + gráfico de barras → [Exportar CSV]
```

### Fluxo futuro (com página do respondente)

```
[Criador publica questionário]
    → Link público gerado
         ↓
[Respondente acessa /r/{id}]
    → Responde perguntas (texto ou áudio)
    → Áudio é transcrito automaticamente (Groq)
         ↓
[Criador acessa Analytics]
    → Vê respostas agregadas
    → Exporta (CSV, PDF)
```

---

## 4. Regras de Negócio

### Questionários — Tipos de Pergunta (11 tipos)

| # | Badge | Tipo canônico | Componente de resposta | V1 |
|---|---|---|---|---|
| 1 | TEXTO CURTO | short_text | `<input type="text">` | ✅ |
| 2 | TEXTO LONGO | long_text | `<textarea>` + contador + áudio | ✅ |
| 3 | MÚLTIPLA [○] | single_choice | Radio buttons (option cards) | ✅ |
| 4 | [✓✓] | multiple_choice | Checkboxes (option cards) | ✅ |
| 5 | ESCALA | likert_scale | Likert 5 pontos (dots + linha) | ✅ |
| 6 | NPS | nps | Grid 0-10 numerado | ✅ |
| 7 | RANKING | ranking | Drag-to-reorder com grips | ✅ |
| 8 | MATRIZ | matrix | Grade de opções | ❌ V2 |
| 9 | ARQUIVO | file_upload | Upload drag & drop | ❌ V2 |
| 10 | DATA | date | Date picker | ❌ V2 |
| 11 | NÚMERO | number | Number input | ❌ V2 |

### Planos e Cobrança (premissa)

| Plano | Preço/mês | Questionários | Respostas/mês | Áudio | Exportação | IA |
|---|---|---|---|---|---|---|
| Free | R$ 0 | 3 ativos | 100 | ❌ | CSV | ❌ |
| Pro | R$ 49-79 | Ilimitados | 1.000 | ✅ | CSV+PDF | ❌ |
| Business | R$ 149-199 | Ilimitados | Ilimitadas | ✅ | CSV+PDF | ✅ |

### Áudio (futuro)

- **Gravação:** direto no navegador (MediaRecorder API)
- **Transcrição:** Groq Whisper
- **Armazenamento:** S3/R2, URL assinada
- **Fallback:** se transcrição falhar, áudio disponível para escuta manual

### Respostas (futuro)

- **Anônimas por padrão** (sem coleta de e-mail)
- **Uma resposta por sessão** (cookie/session)
- **Rascunho automático:** localStorage

### Fora de escopo (V1)

- Skip logic / branching condicional
- White-label (domínio próprio)
- API pública
- Integrações nativas (CRM, planilhas)
- Coleta de vídeo
- App mobile nativo
- Multi-idioma

---

## 5. Integrações

| Integração | Tipo | Descrição | Status |
|---|---|---|---|
| **Design System** | CSS | Tokens vinho/papel, sem dependência externa | ✅ |
| **Groq Whisper** | API STT | Transcrição de áudio | 🔴 |
| **S3 / R2** | Storage | Áudios e arquivos | 🔴 |
| **Supabase Auth** | Autenticação | Login/cadastro | 🔴 |
| **Resend** | Email | Envio de questionários e magic links | 🔴 |
| **Stripe** | Pagamento | Assinaturas | 🔴 |
| **DeepSeek Flash** | LLM | Geração de questionários | 🔴 |
| **PostgreSQL (Supabase)** | Banco | Dados estruturados | 🔴 |

---

## 6. Cenários de Teste

### Landing
- [ ] Input visível com autofocus, placeholder correto
- [ ] Enter com texto → auth.html
- [ ] Botão gravar → animação → auth.html

### Auth
- [ ] Google OAuth UI renderiza com ícone SVG
- [ ] Magic link e-mail aceita input
- [ ] Ambos redirecionam para builder.html

### Builder
- [ ] 6 perguntas de amostra renderizadas
- [ ] 7 tipos de pergunta com UI interativa
- [ ] "+ Pergunta" adiciona card
- [ ] "Enviar →" redireciona para send.html

### Send
- [ ] Lista de contatos com seleção individual e "Todos"
- [ ] CSV zone simulada funciona
- [ ] "Enviar questionário →" redireciona para analytics.html

### Analytics
- [ ] KPIs renderizados (12, 80%, 4min)
- [ ] Barras animam no load
- [ ] "Exportar CSV" responde

### Cross-página
- [ ] Fluxo completo: Landing → Auth → Builder → Send → Analytics
- [ ] Botões Voltar funcionam (Send → Builder, Analytics → Send)
- [ ] Tema vinho/papel consistente em todas as páginas
- [ ] Responsivo em todas as páginas (< 600px)
