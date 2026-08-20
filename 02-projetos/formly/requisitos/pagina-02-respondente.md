# 📝 Página 02 — Respondente (Questionário Público)

> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Página pública onde o respondente acessa o questionário via link. Exibe uma pergunta por vez, coleta respostas em texto ou áudio, e oferece um agente de follow-up quando a resposta é incompleta. Ao final, revisão e envio.

### Layout

```
┌──────────────────────────────────────────┐
│  [Logo]  Pesquisa de Satisfação          │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━  3/8        │
├──────────────────────────────────────────┤
│                                          │
│                                          │
│    ⭐ Como você avalia o atendimento?    │
│                                          │
│    ○ 1 — Péssimo                        │
│    ○ 2 — Ruim                           │
│    ● 3 — Regular                        │
│    ○ 4 — Bom                            │
│    ○ 5 — Excelente                      │
│                                          │
│                                          │
├──────────────────────────────────────────┤
│  [← Anterior]                [Próximo →] │
└──────────────────────────────────────────┘
```

---

## 2. Estrutura de Elementos

### 2.1 Shell da página pública

| Elemento | Tipo | Detalhes |
|---|---|---|
| Logo | imagem | Logo do criador (brand kit) ou placeholder |
| Título da pesquisa | texto | Nome do questionário |
| Barra de progresso | barra horizontal | "3/8" ou barra percentual |
| Área da pergunta | container central | Uma pergunta por vez, centralizada |
| Navegação | barra inferior | ← Anterior / Próximo → |
| Rodapé | texto | "Criado com Formly" (v1) ou white-label (futuro) |

### 2.2 Componentes de resposta (por tipo)

**📝 Texto curto:**
| Elemento | Tipo | Detalhes |
|---|---|---|
| Label | texto | A pergunta |
| Input | campo texto | Placeholder configurado pelo criador |
| Contador | texto | "0/500" caracteres |
| Validação | inline | Se obrigatório e vazio → "Campo obrigatório" |

**📄 Parágrafo:**
| Elemento | Tipo | Detalhes |
|---|---|---|
| Label | texto | A pergunta |
| Textarea | área de texto | Placeholder, linhas redimensionáveis |
| Contador | texto | "0/5000" caracteres |

**☑️ Múltipla escolha:**
| Elemento | Tipo | Detalhes |
|---|---|---|
| Label | texto | A pergunta |
| Opções | radio (única) ou checkbox (múltipla) | Lista vertical |
| Feedback visual | destaque | Opção selecionada com cor do tema |
| "Outro" | input condicional | Se criador permitiu resposta livre adicional |

**🎤 Áudio:**
| Elemento | Tipo | Detalhes |
|---|---|---|
| Label | texto | A pergunta |
| Botão gravar | btn circular vermelho | Pressiona para gravar |
| Temporizador | texto | "0:00 / 2:00" durante gravação |
| Onda de áudio | visualização | Animação durante gravação |
| Preview | player | Ouvir antes de confirmar |
| Regravar | btn | Descarta e grava de novo |
| Status transcrição | indicador | "Transcrevendo..." → texto aparece |
| Texto transcrito | área editável | Respondente pode corrigir a transcrição |

**⭐ Escala:**
| Elemento | Tipo | Detalhes |
|---|---|---|
| Label | texto | A pergunta |
| Escala | radio buttons inline | 1 a 5 (ou 1 a 10) |
| Labels extremos | texto | "Péssimo" à esquerda, "Excelente" à direita |
| Número selecionado | destaque | Número escolhido em destaque |

**📎 Upload de arquivo:**
| Elemento | Tipo | Detalhes |
|---|---|---|
| Label | texto | A pergunta |
| Área de upload | drag & drop | Arraste arquivo ou clique |
| Formatos aceitos | texto | "PDF, JPG, PNG, DOCX (máx. 10MB)" |
| Preview do arquivo | miniatura | Nome, tamanho, ícone do tipo |
| Remover | btn ✕ | Remove arquivo selecionado |

### 2.3 Agente de Follow-up

| Elemento | Tipo | Detalhes |
|---|---|---|
| Trigger | condicional | Se resposta é curta/vaga e follow-up está ativo |
| Mensagem do agente | balão de chat inline | "Você mencionou [X]. Poderia detalhar um pouco mais?" |
| Campo adicional | textarea | Input extra para complementar |
| Pular | btn texto | "Prefiro não responder" |

### 2.4 Tela de revisão

| Elemento | Tipo | Detalhes |
|---|---|---|
| Lista de respostas | cards | Uma card por pergunta, resposta abaixo |
| Editar resposta | btn ✏️ | Volta para aquela pergunta |
| Indicador de áudio | ícone 🎤 | Mostra que tem transcrição |
| Botão Enviar | btn primário | Confirma todas as respostas |
| Texto legal | disclaimer | "Ao enviar, você concorda..." (se configurado) |

### 2.5 Tela de agradecimento

| Elemento | Tipo | Detalhes |
|---|---|---|
| Ícone | ✅ | Check animado |
| Mensagem | texto | "Obrigado por responder!" (customizável) |
| Texto adicional | parágrafo | Mensagem de encerramento do criador |
| Link | opcional | "Criado com Formly" |

---

## 3. Fluxos de Processo

### 3.1 Responder questionário

```
1. Respondente acessa link
   → Carrega tema + logo + título

2. Tela de abertura (opcional, se criador configurou)
   → Título + descrição + botão "Começar"

3. Para cada pergunta:
   a) Renderiza componente do tipo correto
   b) Respondente interage (digita, seleciona, grava)
   c) Validação inline (obrigatório vazio = erro)
   d) Se áudio: grava → envia → transcrição aparece → confirma
   e) Se follow-up ativo e resposta curta: agente pergunta mais
   f) Clica "Próximo" → salva resposta → vai para próxima
   g) Clica "Anterior" → volta para pergunta anterior (resposta mantida)

4. Tela de revisão
   → Lista todas as perguntas com respostas
   → Pode editar qualquer uma (volta para aquela pergunta)
   → Clica "Enviar"

5. Envio
   → Todas as respostas enviadas para API
   → Áudios já foram enviados durante a gravação
   → Tela de agradecimento
```

### 3.2 Áudio (gravação + transcrição)

```
1. Respondente clica 🎤 Gravar
   → Navegador solicita permissão de microfone
   → Temporizador inicia
   → Onda de áudio animada

2. Respondente clica ⏹ Parar (ou atinge tempo máximo)
   → Áudio é enviado para servidor (S3)
   → Servidor envia para Groq Whisper
   → Transcrição retorna

3. Transcrição aparece como texto editável
   → Respondente pode corrigir erros de transcrição
   → Pode ouvir o áudio de novo (preview)
   → Pode regravar

4. Respondente clica "Próximo"
   → Áudio (S3 URL) + transcrição (texto) salvos
```

### 3.3 Follow-up do agente

```
1. Respondente envia resposta curta (ex: "Foi bom")
2. Sistema avalia: resposta cobre todos os aspectos da pergunta?
3. Se NÃO e follow-up está ativo:
   → Agente: "Obrigado! Poderia me contar o que especificamente foi bom?"
   → Campo extra aparece abaixo da resposta original
4. Respondente complementa (ou clica "Prefiro não responder")
5. Ambas as respostas (original + complemento) são salvas
```

---

## 4. Regras de Negócio

### Progresso

- Barra de progresso mostra posição atual / total
- Respostas são salvas a cada "Próximo" (localStorage + servidor)
- Se fechar browser e voltar, retoma de onde parou (se mesmo dispositivo)
- Tempo máximo para completar: 7 dias (respostas parciais expiram)

### Áudio

- Formatos: WebM, MP4, WAV (depende do navegador)
- Duração máxima: configurada pelo criador (30s, 60s, 120s)
- Upload acontece durante a gravação (streaming)
- Transcrição é cacheada (mesmo áudio = mesma transcrição)
- Respondente sempre pode corrigir a transcrição

### Validação

- Pergunta obrigatória sem resposta → não deixa avançar
- Mensagem de erro inline, não modal
- Upload: valida tipo e tamanho antes de enviar
- Áudio: valida duração mínima (2s) para evitar gravações vazias

### Follow-up

- Criador escolhe ativar/desativar por pergunta
- Agente só aparece se resposta é considerada "incompleta" (heurística: < 20 palavras em parágrafo, ou resposta genérica)
- Máximo 1 follow-up por pergunta
- Respondente pode pular o follow-up

### Tema

- Herda o tema escolhido pelo criador
- Logo e cores do brand kit aplicados
- Responsivo: funciona em mobile (320px+) e desktop
- Modo escuro: se o tema tiver variante dark, respeita `prefers-color-scheme`

---

## 5. Integrações

| Elemento | Integração | Status |
|---|---|---|
| Carregar questionário | GET /api/surveys/:slug/public | A construir |
| Enviar resposta texto | POST /api/responses/:surveyId | A construir |
| Upload de áudio | S3 presigned URL → PUT | A construir |
| Transcrição | POST /api/transcribe (→ Groq) | A construir |
| Salvar progresso | POST /api/responses/:surveyId/partial | A construir |
| Follow-up IA | POST /api/follow-up (LLM avalia completude) | Fase 3 |

---

## 6. Cenários de Teste

### Navegação
- [ ] Acessa link → vê tela de abertura (se configurada)
- [ ] Clica Começar → primeira pergunta aparece
- [ ] Responde pergunta de texto → Próximo → segunda pergunta
- [ ] Voltar → resposta anterior mantida
- [ ] Fechar browser no meio → reabrir link → retoma de onde parou

### Tipos de resposta
- [ ] Múltipla escolha (única): seleciona 1 → Próximo
- [ ] Múltipla escolha (múltipla): seleciona 3 → Próximo
- [ ] Texto curto: digita 300 caracteres → contador mostra 300/500
- [ ] Parágrafo: digita texto longo → textarea expande
- [ ] Áudio: grava 30s → vê transcrição → corrige → Próximo
- [ ] Áudio: regrava → transcrição anterior descartada
- [ ] Escala: seleciona 4 → destaque no 4
- [ ] Upload: arrasta PDF → preview → Próximo
- [ ] Upload: formato inválido → erro inline

### Validação
- [ ] Obrigatória vazia → erro "Campo obrigatório" → não avança
- [ ] Upload > 10MB → erro "Arquivo muito grande"
- [ ] Áudio < 2s → erro "Gravação muito curta"

### Follow-up
- [ ] Resposta curta ("bom") → agente pergunta mais
- [ ] Resposta longa (30+ palavras) → sem follow-up
- [ ] Clica "Prefiro não responder" → segue sem complemento

### Revisão e envio
- [ ] Tela de revisão mostra todas as respostas
- [ ] Clica ✏️ → volta para pergunta → edita → volta para revisão
- [ ] Clica Enviar → loading → tela de agradecimento
- [ ] Respostas chegam no dashboard do criador
