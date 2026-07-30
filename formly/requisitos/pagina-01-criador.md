# 📝 Página 01 — Criador de Questionário

> **Status:** ⚠️ Aspiracional — sem código ainda. Baseado no Google Doc + input do Lucas (2026-07-30)
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Tela principal onde o usuário **constrói questionários**. O diferencial do Formly é oferecer **três modos de interação** para montar o questionário, permitindo que o usuário escolha o que for mais natural para cada momento:

1. **Modo Canvas (drag & drop):** manipulação direta de "caixinhas" visuais — arrasta tipos de pergunta, edita inline, reordena
2. **Modo Documento (importação de texto):** cola um documento com todas as perguntas e especificações, o sistema faz o parsing e monta o esqueleto
3. **Modo Chat (conversa assistida):** conversa com o assistente IA para definir perguntas, revisar, refinar, e depois aplicar no canvas

### Layout proposto

```
┌─────────────────────────────────────────────────────────────┐
│  ← Meus questionários   |   [Nome do questionário]          │
│                         |   [▾ Modo: Canvas | Documento | Chat] │
├──────────┬──────────────────────────────────┬───────────────┤
│ Sidebar  │                                   │  Painel de    │
│ de       │        ÁREA PRINCIPAL             │  Preview      │
│ tipos    │        (Canvas / Editor / Chat)   │  (mobile)     │
│          │                                   │               │
│ 📝 Texto │  ┌───────────────────────┐        │  ┌──────────┐ │
│ 🔘 Esc.  │  │ Pergunta 1: texto    │        │  │ Preview  │ │
│ ✏️ Longa │  └───────────────────────┘        │  │   do     │ │
│ 🎤 Áudio │  ┌───────────────────────┐        │  │  form    │ │
│ 📋 Meta  │  │ Pergunta 2: áudio    │        │  └──────────┘ │
│          │  └───────────────────────┘        │               │
│ [+ Add]  │                                   │               │
│          │  ┌───────────────────────┐        │               │
│          │  │ + Nova pergunta       │        │               │
│          │  └───────────────────────┘        │               │
├──────────┴──────────────────────────────────┴───────────────┤
│  [Personalizar]  [Preview]  [💾 Salvar]  [🚀 Publicar]       │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Estrutura de Elementos

### 2.1 Seletor de Modo

- **Tipo:** segmented control / tabs
- **Posição:** topo da área principal, abaixo do header
- **Conteúdo/Dados:** 3 modos — Canvas, Documento, Chat
- **Interações:** clique troca a área principal, preserva o conteúdo já criado
- **Regra:** o usuário pode alternar entre modos a qualquer momento. O que foi criado em um modo aparece nos outros

### 2.2 Sidebar de Tipos de Pergunta

- **Tipo:** painel lateral esquerdo (coluna ~220px)
- **Posição:** fixo à esquerda
- **Conteúdo/Dados:**

| Ícone | Tipo | Descrição |
|---|---|---|
| 📝 | Texto curto | Resposta em uma linha |
| ✏️ | Texto longo | Parágrafo / múltiplas linhas |
| 🔘 | Múltipla escolha | Opções com radio/checkbox |
| 🎤 | Áudio | Gravação de voz (diferencial) |
| 📋 | Metadados | Nome, e-mail, data (campos padrão) |

- **Interações:**
  - **Modo Canvas:** arrastar tipo para o canvas → cria nova pergunta
  - Clique no tipo → adiciona pergunta ao final da lista
- **Condições de visibilidade:** sempre visível no criador

### 2.3 Área Principal — Modo Canvas (drag & drop)

- **Tipo:** lista vertical de cards editáveis
- **Conteúdo/Dados:** cards de pergunta, um abaixo do outro

#### Card de Pergunta (caixinha)

| Elemento | Tipo | Descrição |
|---|---|---|
| Alça de arraste | handle (⋮⋮) | canto esquerdo, permite reordenar |
| Número da pergunta | badge | "1.", "2.", etc. |
| Tipo de pergunta | dropdown inline | alterna entre tipos (texto, escolha, áudio, etc.) |
| Título da pergunta | input text | "Qual sua idade?" — editável inline |
| Opções (se múltipla escolha) | lista editável | adicionar/remover/editar opções |
| Toggle "Obrigatória" | switch | define se a resposta é obrigatória |
| Botão ⋯ (mais) | dropdown | Duplicar, Mover para cima/baixo, Excluir |
| Preview do tipo | miniatura | ícone + miniatura do componente de resposta |

- **Interações:**
  - Arrastar pela alça → reordena perguntas
  - Clicar no título → edita inline
  - Clicar no tipo → dropdown de tipos alterna o componente
  - ⋯ → ações da pergunta
- **Estados visuais:**
  - Normal: card com borda sutil, fundo branco
  - Drag: sombra elevada, borda destacada
  - Foco: borda azul/accent

#### Botão "+ Nova pergunta"

- **Tipo:** área clicável no final da lista
- **Posição:** após a última pergunta
- **Conteúdo/Dados:** linha dashed, "+" ícone, "Nova pergunta"
- **Interações:** clique → dropdown rápido com tipos, seleciona → cria card

### 2.4 Área Principal — Modo Documento (importação de texto)

- **Tipo:** editor de texto + preview lado a lado
- **Layout:** duas colunas: esquerda (editor) + direita (preview do esqueleto)

#### Editor de texto

| Elemento | Tipo | Descrição |
|---|---|---|
| Área de texto | textarea grande | usuário cola ou digita o documento com perguntas |
| Placeholder | texto guia | "Cole aqui seu documento com as perguntas. Ex: 1. Qual sua idade? (texto curto, obrigatória)..." |
| Botão "Processar" | btn primário | faz parsing do texto e gera esqueleto |
| Indicador de parsing | spinner/status | "Analisando documento..." |

#### Preview do esqueleto (pós-processamento)

| Elemento | Tipo | Descrição |
|---|---|---|
| Lista de perguntas detectadas | cards resumidos | mostra o que o parser entendeu |
| Badge de tipo | pill | indica tipo detectado (texto, escolha, áudio) |
| Badge de obrigatoriedade | pill | "Obrigatória" / "Opcional" |
| Botão "Aplicar ao Canvas" | btn primário | transfere o esqueleto para o modo Canvas para edição fina |
| Botão "Corrigir" | btn outline | permite ajustar o que o parser entendeu antes de aplicar |

#### Sintaxe esperada no documento (exemplo)

```
1. Qual é o seu nome?
   tipo: texto curto
   obrigatória: sim

2. Como você avalia nosso atendimento?
   tipo: múltipla escolha
   opções: Ótimo, Bom, Regular, Ruim
   obrigatória: sim

3. Conte um pouco sobre sua experiência:
   tipo: texto longo

4. Deixe um recado em áudio:
   tipo: áudio
```

- **Interações:**
  - Colar texto → editor preenche
  - Clicar "Processar" → parsing acontece, preview atualiza
  - Clicar "Aplicar ao Canvas" → muda para modo Canvas com perguntas populadas
  - Clicar "Corrigir" → permite editar cada pergunta detectada antes de aplicar

### 2.5 Área Principal — Modo Chat (conversa assistida)

- **Tipo:** interface de chat (similar a ChatGPT/Claude)
- **Layout:** painel único com histórico de mensagens + input

#### Elementos do Chat

| Elemento | Tipo | Descrição |
|---|---|---|
| Histórico de mensagens | scroll vertical | bolhas user (direita) + assistente (esquerda) |
| Mensagem do assistente | bolha | propõe perguntas, sugere ajustes, mostra preview |
| Preview inline | card dentro da bolha | esqueleto de pergunta que o assistente propôs |
| Botão "Aplicar" | btn inline | na bolha do assistente, aplica aquela pergunta ao canvas |
| Botão "Editar" | btn inline | edita a pergunta sugerida antes de aplicar |
| Botão "Recusar" | btn inline | descarta a sugestão |
| Input do usuário | textarea + send | campo de digitação com placeholder contextual |
| Sugestões rápidas | chips | "Adicionar pergunta de múltipla escolha", "Rever pergunta 3", etc. |

#### Fluxo do Chat

```
Usuário: "Quero criar um questionário de satisfação para uma clínica médica"
    ↓
Assistente: "Ótimo! Vou sugerir algumas perguntas:
    1. Como você avalia o atendimento na recepção? (múltipla escolha: Ótimo, Bom, Regular, Ruim)
       [Aplicar] [Editar] [Recusar]
    2. O tempo de espera foi adequado? (múltipla escolha: Sim, Não, Poderia ser melhor)
       [Aplicar] [Editar] [Recusar]
    ..."

Usuário: "Adiciona uma pergunta de áudio no final, pedindo um depoimento"
    ↓
Assistente: "Adicionei: 'Deixe um depoimento em áudio sobre sua experiência' (áudio, opcional)
       [Aplicar] [Editar] [Recusar]"

Usuário: "Aplica todas no canvas"
    ↓
Assistente: "✅ Todas as perguntas foram aplicadas. Você pode editá-las no modo Canvas."
    → Canvas populado com as perguntas
```

### 2.6 Painel de Preview (mobile)

- **Tipo:** miniatura interativa
- **Posição:** coluna direita (300px, collapsible)
- **Conteúdo/Dados:** simulação de como o questionário aparece no celular
- **Interações:**
  - Atualiza em tempo real conforme o canvas muda
  - Clicável — permite navegar entre perguntas no preview
  - Toggle expandir/recolher
- **Estados visuais:** moldura de celular (bordas arredondadas, proporção 9:16)

### 2.7 Barra Inferior (ações globais)

| Botão | Ícone | Descrição |
|---|---|---|
| Personalizar | 🎨 | Abre painel de personalização (cores, logo, textos) |
| Preview | 👁 | Abre preview em tela cheia (desktop + mobile) |
| Salvar | 💾 | Salva rascunho |
| Publicar | 🚀 | Publica questionário, gera link |

---

## 3. Fluxos de Processo

### 3.1 Criar questionário via Canvas (drag & drop)

```
1. Usuário clica "Criar novo questionário"
   → Modo Canvas abre, vazio
   
2. Usuário arrasta "📝 Texto curto" da sidebar para o canvas
   → Card de pergunta aparece: "Nova pergunta" com tipo "Texto curto"

3. Usuário clica no título → edita: "Qual é o seu nome?"
   Usuário ativa toggle "Obrigatória"

4. Usuário arrasta "🔘 Múltipla escolha" → novo card
   Edita título: "Como você avalia nosso atendimento?"
   Adiciona opções: "Ótimo", "Bom", "Regular", "Ruim"

5. Usuário arrasta ⋮⋮ da pergunta 2 para cima → reordena

6. Usuário arrasta "🎤 Áudio" → novo card
   Edita título: "Deixe um recado em áudio"

7. Clica "🚀 Publicar"
   → Diálogo de confirmação: nome, slug, visibilidade
   → Link gerado: formly.app/f/clinica-satisfacao
```

### 3.2 Criar questionário via Documento

```
1. Usuário seleciona modo "Documento"
   → Editor de texto + preview vazio

2. Usuário cola um bloco de texto com perguntas formatadas
   
3. Clica "Processar"
   → Spinner: "Analisando documento..."
   → Preview lado direito mostra 5 perguntas detectadas:
     [1] Qual o seu nome? — Texto curto — Obrigatória
     [2] Como avalia? — Múltipla escolha (4 opções) — Obrigatória
     ...

4. Usuário revisa o preview
   → Clica "Corrigir" na pergunta 2, ajusta opções
   
5. Clica "Aplicar ao Canvas"
   → Modo muda automaticamente para Canvas
   → 5 cards de pergunta populados
   
6. Usuário faz ajustes finos no Canvas (arrastar, editar)

7. Salva e publica
```

### 3.3 Criar questionário via Chat

```
1. Usuário seleciona modo "Chat"

2. Usuário digita: "Preciso de um questionário de NPS para uma academia"
   
3. Assistente responde com sugestões de perguntas
   → Cada sugestão aparece como card inline com [Aplicar] [Editar] [Recusar]

4. Usuário clica [Aplicar] nas que gosta
   Usuário clica [Editar] em uma, ajusta o texto
   Usuário clica [Recusar] em outra

5. Usuário: "Adiciona uma pergunta de áudio no final: 'Conte sua experiência'"
   → Assistente adiciona e confirma

6. Usuário: "Aplica tudo no canvas"
   → Canvas é populado
   → Chat fica em segundo plano (acessível via toggle)

7. Usuário revisa no Canvas e publica
```

### 3.4 Alternar entre modos

```
1. Usuário está no Canvas com 3 perguntas criadas
2. Clica no modo "Chat"
   → Chat abre, assistente contextualiza: "Vi que você tem 3 perguntas.
      Quer que eu sugira mais alguma?"
3. Conversa no chat, adiciona 2 perguntas
4. Volta para o Canvas — 5 perguntas agora
```

---

## 4. Regras de Negócio

### Modos de interação

- O usuário pode alternar entre modos **a qualquer momento**
- O conteúdo criado em qualquer modo é **compartilhado** entre os modos
- Ao importar de documento, as perguntas **substituem ou mesclam** com as existentes (perguntar antes)
- O chat é **contextual** — sabe o que já existe no questionário

### Tipos de pergunta

| Tipo | Componente de resposta | Validações |
|---|---|---|
| Texto curto | `<input text>` | max caracteres |
| Texto longo | `<textarea>` | max caracteres |
| Múltipla escolha | radio (única) ou checkbox (múltipla) | min/max seleções |
| Áudio | botão gravar + waveform | max duração (ex: 3 min) |

### Perguntas

- Máximo de perguntas: 50 (Free), 200 (Pro), ilimitado (Business)
- Toda pergunta tem: título, tipo, obrigatoriedade
- Pergunta pode ser opcional (toggle off)
- Perguntas são numeradas automaticamente (1., 2., ...)

### Personalização do questionário

- Cores: cor primária (accent), cor de fundo
- Logo: upload de imagem (max 500KB, PNG/SVG recomendado)
- Texto de abertura: título + descrição
- Texto de encerramento: mensagem pós-submissão

### Publicação

- URL: `formly.app/f/<slug>` (slug editável)
- Questionário pode ser "não listado" (só acessível pelo link)
- Pode ser pausado (não aceita novas respostas) sem perder dados

---

## 5. Integrações

| Integração | Descrição | Status |
|---|---|---|
| Nenhuma ainda | Produto em fase de descoberta | 🔴 |

---

## 6. Cenários de Teste

### Canvas
- [ ] Arrastar tipo da sidebar → cria card de pergunta
- [ ] Editar título da pergunta inline
- [ ] Mudar tipo da pergunta via dropdown
- [ ] Reordenar perguntas arrastando pela alça (⋮⋮)
- [ ] Excluir pergunta → confirmação, lista renumera
- [ ] Preview mobile atualiza em tempo real

### Documento
- [ ] Colar texto formatado → parser extrai perguntas corretamente
- [ ] Parser detecta tipos (texto curto, múltipla escolha, áudio)
- [ ] Parser detecta obrigatoriedade
- [ ] Preview mostra resumo do que foi extraído
- [ ] "Corrigir" permite ajustar pergunta antes de aplicar
- [ ] "Aplicar ao Canvas" → canvas populado, modo troca automaticamente
- [ ] Documento mal formatado → mensagem de erro amigável

### Chat
- [ ] Assistente sugere perguntas contextualizadas
- [ ] Botão [Aplicar] adiciona pergunta ao canvas
- [ ] Botão [Editar] permite modificar sugestão antes de aplicar
- [ ] Botão [Recusar] descarta sugestão
- [ ] Chat mantém contexto do questionário existente
- [ ] "Aplica tudo no canvas" → transfere todas as sugestões aceitas

### Cross-mode
- [ ] Criar no Canvas, mudar para Chat → chat vê o que foi criado
- [ ] Adicionar no Chat, voltar ao Canvas → cards aparecem
- [ ] Importar documento com Canvas já populado → pergunta se mescla ou substitui
