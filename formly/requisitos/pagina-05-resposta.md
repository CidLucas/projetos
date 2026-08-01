# 📋 Página 05 — Página do Respondente (Pública)

> **Status:** 🔴 Não implementada no site (aspirational)
> **Rota prevista:** `/r/{form_id}`
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Página pública acessada pelo respondente via link compartilhado. Exibe as perguntas do questionário com design responsivo e coleta respostas (texto ou áudio). É o **diferencial principal** do Formly.

> ⚠️ Esta página **não existe** no protótipo atual. As especificações abaixo são aspiracionais, baseadas no Google Doc de escopo e conversas com Lucas.

### Layout previsto

```
┌──────────────────────────────────────────┐
│  [Logo do criador]                       │
│  Pesquisa de Satisfação                  │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━  3/8       │
├──────────────────────────────────────────┤
│                                          │
│    Como você avalia o atendimento?       │
│                                          │
│    ○ Péssimo                             │
│    ○ Ruim                                │
│    ● Regular                             │
│    ○ Bom                                 │
│    ○ Excelente                           │
│                                          │
├──────────────────────────────────────────┤
│  [← Anterior]                [Próximo →] │
├──────────────────────────────────────────┤
│  Criado com Formly                       │
└──────────────────────────────────────────┘
```

---

## 2. Elementos de UI (previstos)

### 2.1 Shell

| Elemento | Tipo | Detalhes |
|---|---|---|
| Logo do criador | imagem | Brand kit (se configurado) |
| Título | heading | Nome do questionário |
| Barra de progresso | barra | "3/8" ou percentual |
| Área da pergunta | container | Uma pergunta por vez, centralizada |
| Navegação | ← / → | Anterior / Próximo |
| Footer | texto | "Criado com Formly" |

### 2.2 Componentes por tipo de pergunta

Os mesmos 11 tipos do Builder, renderizados como componentes de input para o respondente:

| Tipo | Componente |
|---|---|
| TEXTO CURTO | `<input text>` com contador |
| TEXTO LONGO | `<textarea>` + opção de gravar áudio |
| MÚLTIPLA [○] | Radio buttons estilizados |
| [✓✓] | Checkboxes estilizados |
| ESCALA | Likert dots interativos |
| NPS | Grid 0-10 selecionável |
| RANKING | Drag & drop para ordenar |
| MATRIZ | Grade de opções |
| ARQUIVO | Upload drag & drop |
| DATA | Date picker |
| NÚMERO | Number input |

### 2.3 Gravador de Áudio (diferencial)

| Elemento | Tipo | Detalhes |
|---|---|---|
| Botão Gravar | btn circular | 🎤, pulsando durante gravação |
| Timer | texto | mm:ss |
| Waveform | visualização | Barras animadas |
| Preview | player | ▶️ ouvir, 🔄 regravar |
| Transcrição | texto editável | Resultado do Groq Whisper |
| Status | indicador | "Transcrevendo..." → texto |

### 2.4 Tela de Encerramento

| Elemento | Tipo | Detalhes |
|---|---|---|
| Ícone | ✅ animado | Checkmark |
| Mensagem | texto | Customizável pelo criador |
| Link | CTA | "Criado com Formly" |

---

## 3. Fluxos (previstos)

### Resposta com texto

```
1. Respondente acessa link → página carrega
2. Primeira pergunta aparece
3. Responde → "Próximo"
4. Repete até a última
5. Tela de revisão (opcional)
6. "Enviar" → tela de agradecimento
```

### Resposta com áudio

```
1. Respondente chega em pergunta de áudio
2. Clica 🎤 → navegador pede permissão
3. Grava → para → preview + transcrição automática
4. Pode corrigir transcrição ou regravar
5. "Próximo"
```

---

## 4. Regras (previstas)

- **Modos de exibição:** uma pergunta por vez (tipo Typeform) ou scroll contínuo (tipo Google Forms)
- **Rascunho automático:** salvo em localStorage a cada avanço
- **Submissão única:** cookie/session bloqueia reenvio
- **Anonimato:** padrão sem coleta de e-mail
- **Validação:** obrigatória não respondida = shake + mensagem
- **Áudio:** max 3 min, formato WebM/OGG → MP3, transcrição Groq Whisper
- **Acessibilidade:** WCAG AA, navegação por teclado, labels ARIA

---

## 5. Integrações (previstas)

| Integração | Rota | Status |
|---|---|---|
| Carregar questionário | `GET /v1/public/forms/{id}` | 🔴 |
| Enviar resposta | `POST /v1/public/forms/{id}/responses` | 🔴 |
| Upload áudio | S3 presigned URL | 🔴 |
| Transcrição | `POST /v1/audio/transcribe` (Groq) | 🔴 |

---

## 6. Cenários de Teste (previstos)

- [ ] Acessar link → primeira pergunta visível
- [ ] Navegação ← → funciona
- [ ] Barra de progresso atualiza
- [ ] Validação de obrigatória
- [ ] Gravação de áudio + transcrição
- [ ] Tela de agradecimento
- [ ] Rascunho restaurado ao reabrir
- [ ] Responsivo (320px+)

---

> **Status:** 🔴 Página não existe no site. Especificação aspiracional baseada no escopo original.
