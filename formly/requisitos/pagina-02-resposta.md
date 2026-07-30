# 📋 Página 02 — Página de Resposta (Respondente)

> **Status:** ⚠️ Aspiracional — sem código ainda. Baseado no Google Doc + input do Lucas (2026-07-30)
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Página pública acessada pelo respondente através de um link compartilhado. O respondente responde às perguntas — digitando texto ou **gravando áudio** (diferencial do Formly). O áudio é transcrito automaticamente após o envio.

### Layout

```
┌──────────────────────────────────────────────┐
│  [Logo do criador]                           │
│  Título do questionário                      │
│  Descrição / texto de abertura               │
├──────────────────────────────────────────────┤
│                                              │
│  ┌──────────────────────────────────────┐    │
│  │  1. Qual é o seu nome?         [1/5] │    │
│  │  ┌──────────────────────────────────┐│    │
│  │  │ Digite sua resposta...           ││    │
│  │  └──────────────────────────────────┘│    │
│  └──────────────────────────────────────┘    │
│                                              │
│         [← Anterior]   [Próxima →]           │
│                                              │
│  Barra de progresso: ████████░░░░ 60%        │
├──────────────────────────────────────────────┤
│  Formly — Criado com Formly                  │
└──────────────────────────────────────────────┘
```

---

## 2. Estrutura de Elementos

### 2.1 Header

| Elemento | Tipo | Descrição |
|---|---|---|
| Logo do criador | imagem (opcional) | se configurado, aparece centralizado no topo |
| Título | heading | título do questionário definido pelo criador |
| Descrição | parágrafo | texto de abertura explicando o propósito |

### 2.2 Área de Pergunta

- **Tipo:** card centralizado com transição entre perguntas
- **Modos de exibição (configurável pelo criador):**
  - **Uma por vez (tipo Typeform):** cada pergunta em um card separado, navega com ← →
  - **Scroll contínuo (tipo Google Forms):** todas as perguntas visíveis, scroll vertical

#### Componentes por tipo de pergunta

| Tipo | Componente | Elementos |
|---|---|---|
| **Texto curto** | input text | campo de 1 linha, placeholder, contador de caracteres (se houver limite) |
| **Texto longo** | textarea | múltiplas linhas, redimensionável, placeholder, contador |
| **Múltipla escolha (única)** | radio buttons | círculos clicáveis + labels, seleção exclusiva |
| **Múltipla escolha (múltipla)** | checkboxes | quadrados clicáveis + labels, seleção múltipla |
| **Áudio** | gravador | botão 🎤 gravar/parar, waveform/duração, botão reproduzir antes de enviar |

### 2.3 Gravador de Áudio (diferencial)

| Elemento | Tipo | Descrição |
|---|---|---|
| Botão Gravar | btn circular grande | 🎤 Microfone, pulsando durante gravação |
| Timer | texto | duração da gravação (mm:ss) |
| Waveform | visualização | barras animadas durante gravação |
| Preview | player | após gravar: ▶️ reproduzir, 🔄 regravar |
| Status da transcrição | badge | "Transcrevendo..." → "Transcrição concluída" |
| Fallback | alerta | se transcrição falhar: "Não foi possível transcrever. O áudio será enviado para escuta manual." |

- **Interações:**
  - Clique no 🎤 → inicia gravação (pede permissão do microfone)
  - Clique novamente → para gravação
  - Preview permite ouvir antes de avançar
  - Regravar substitui a gravação anterior
- **Estados visuais:**
  - Parado: ícone microfone cinza
  - Gravando: ícone vermelho pulsando, waveform animada
  - Gravado: player com waveform estática, duração
  - Transcrevendo: spinner "Transcrevendo seu áudio..."
  - Erro: alerta amarelo

### 2.4 Navegação

| Elemento | Tipo | Descrição |
|---|---|---|
| Botão "Anterior" | btn secundário | volta para pergunta anterior (desabilitado na primeira) |
| Botão "Próxima" / "Enviar" | btn primário | avança (desabilitado se pergunta obrigatória não respondida) |
| Barra de progresso | progress bar | % concluído, ou "3/5" |
| Indicador de pergunta | texto | "Pergunta 3 de 5" |

### 2.5 Tela de Encerramento

| Elemento | Tipo | Descrição |
|---|---|---|
| Ícone de conclusão | checkmark animado | ✓ verde com animação |
| Mensagem personalizada | texto | definida pelo criador ("Obrigado por responder!") |
| Link opcional | CTA | "Criar seu próprio questionário no Formly" |

### 2.6 Footer

| Elemento | Tipo | Descrição |
|---|---|---|
| Powered by Formly | texto/link | link para formly.app |
| Política de privacidade | link | opcional, configurável pelo criador |

---

## 3. Fluxos de Processo

### 3.1 Responder questionário (texto)

```
1. Respondente acessa o link
   → Página carrega com título + descrição

2. Vê a primeira pergunta (ex: "Qual é o seu nome?")
   → Digita no campo de texto

3. Clica "Próxima" (ou "Enter")
   → Próxima pergunta aparece (animação slide/fade)
   → Barra de progresso atualiza

4. Responde pergunta de múltipla escolha
   → Seleciona uma opção (radio)
   → Clica "Próxima"

5. Chega na última pergunta
   → Botão muda para "Enviar"

6. Clica "Enviar"
   → Respostas enviadas para o backend
   → Tela de encerramento aparece com mensagem do criador
```

### 3.2 Responder com áudio

```
1. Respondente chega em uma pergunta do tipo "Áudio"

2. Clica no botão 🎤
   → Navegador pede permissão do microfone
   → Gravação inicia: timer roda, waveform anima

3. Clica 🎤 novamente (ou atinge tempo máximo)
   → Gravação para
   → Player de preview aparece
   → Transcrição inicia automaticamente: "Transcrevendo..."

4. Transcrição concluída
   → Texto aparece abaixo do player: "Depoimento sobre a experiência..."
   → Respondente pode ouvir o áudio e verificar transcrição

5. Se quiser regravar:
   → Clica 🔄 "Regravar"
   → Gravação anterior é descartada

6. Clica "Próxima"
   → Áudio + transcrição são enviados juntos
```

### 3.3 Validação e erros

```
1. Respondente clica "Próxima" sem responder pergunta obrigatória
   → Campo vibra/shake, borda fica vermelha
   → Mensagem: "Esta pergunta é obrigatória"

2. Respondente tenta enviar com pergunta obrigatória incompleta
   → Scrolla automaticamente até a pergunta não respondida
   
3. Erro de rede ao enviar
   → Toast: "Erro ao enviar. Suas respostas foram salvas."
   → Respostas ficam em localStorage para retry
```

---

## 4. Regras de Negócio

### Permissões do navegador

- **Microfone:** solicitado apenas quando o respondente interage com uma pergunta de áudio
- **Sem áudio no questionário:** permissão nunca é solicitada

### Gravação de áudio

- **Formato:** WebM/OGG (codec do navegador), convertido para MP3 no backend
- **Duração máxima:** 3 minutos (configurável pelo criador)
- **Qualidade:** configurável (baixa/média/alta) para otimizar custo de transcrição
- **Fallback:** se transcrição falhar (timeout, erro da API), áudio fica disponível para o criador escutar manualmente no dashboard

### Transcrição

- **API:** Groq Whisper (STT)
- **Idioma:** PT-BR (detecção automática)
- **Timestamps:** não necessários na V1
- **Custo:** estimado ~R$ 0,006/minuto de áudio (a validar)

### Respostas

- **Rascunho automático:** respostas são salvas em localStorage a cada avanço de pergunta
- **Retomada:** se respondente fechar e reabrir o link, respostas parciais são restauradas
- **Submissão única:** após enviar, mesmo link não permite nova resposta (cookie/session)
- **Anonimato:** padrão é não coletar identificação (a menos que o criador adicione campo de nome/e-mail)

### Acessibilidade

- Navegação por teclado (Tab, Enter, setas)
- Labels ARIA em todos os campos
- Contraste adequado (WCAG AA)
- Suporte a leitores de tela

---

## 5. Integrações

| Integração | Descrição | Status |
|---|---|---|
| **Groq Whisper API** | Transcrição de áudio após upload | 🔴 não implementado |
| **S3 / Blob Storage** | Upload e storage dos arquivos de áudio | 🔴 não implementado |
| **Backend Formly** | POST /api/responses — envio das respostas | 🔴 não implementado |

---

## 6. Cenários de Teste

### Navegação
- [ ] Acessar link → primeira pergunta visível
- [ ] Responder texto curto → "Próxima" avança
- [ ] "Anterior" volta para pergunta anterior (resposta preservada)
- [ ] Barra de progresso reflete % concluído
- [ ] Chegar na última pergunta → botão muda para "Enviar"

### Áudio
- [ ] Clicar 🎤 → pede permissão do microfone
- [ ] Conceder permissão → gravação inicia
- [ ] Gravar 30s → parar → preview disponível
- [ ] Reproduzir preview → áudio toca
- [ ] Regravar → gravação anterior descartada
- [ ] Transcrição aparece após upload
- [ ] Negar permissão → mensagem explicativa: "Você pode pular esta pergunta ou conceder acesso ao microfone"

### Validação
- [ ] Avançar sem responder obrigatória → erro, campo vibra
- [ ] Enviar com obrigatória vazia → scrolla até a pergunta
- [ ] Enviar tudo OK → tela de encerramento

### Resiliência
- [ ] Fechar navegador no meio → reabrir link, respostas restauradas
- [ ] Enviar com rede lenta → spinner, timeout tratado
- [ ] Já respondeu antes → mensagem "Você já respondeu este questionário"

### Responsividade
- [ ] Mobile (375px) → layout adequado, touch-friendly
- [ ] Tablet → 2 colunas? ou centralizado
- [ ] Desktop → largura máxima ~700px centralizado
