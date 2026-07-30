# 📝 Página 01 — Criador de Questionário

> **Status:** ⚠️ Aspiracional — sem código ainda. Baseado no Google Doc + input do Lucas (2026-07-30, revisado)
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Tela principal onde o usuário **constrói questionários** em um **fluxo contínuo**, não em modos separados. O usuário começa descrevendo o que precisa (texto ou voz), o sistema faz perguntas de refinamento, gera um esqueleto, e o usuário ajusta usando **três formas de interação complementares**:

1. **Conversa (chat/voz)** — descrever, responder perguntas do sistema, pedir ajustes
2. **Manipulação direta** — arrastar caixinhas, reordenar, editar inline
3. **Edição textual** — editar o esqueleto como texto antes ou depois da versão visual

**Essas formas não são modos separados — coexistem na mesma tela e o usuário flui entre elas naturalmente.**

### Layout proposto

```
┌──────────────────────────────────────────────────────────────────┐
│  ← Meus questionários     |     [Nome do questionário]           │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  💬 O que você precisa?                                    │  │
│  │  ┌──────────────────────────────────────────────────────┐  │  │
│  │  │ Descreva o questionário que você quer criar...       │  │  │
│  │  │ ou 🎤 ditar                                          │  │  │
│  │  └──────────────────────────────────────────────────────┘  │  │
│  │                                                    [Enviar] │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  🤖 Assistente: Entendi! Algumas perguntas:               │  │
│  │  • Qual o público-alvo?                                   │  │
│  │  • Quantas perguntas você imagina?                        │  │
│  │  • Precisa de áudio ou só texto?                          │  │
│  │  ┌──────────────────────────────────────────────────┐    │  │
│  │  │ [Responder...]                            [Enviar]│    │  │
│  │  └──────────────────────────────────────────────────┘    │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ─────────── após 1-2 rounds, sistema gera esqueleto ──────────  │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  📋 Esqueleto gerado                          [Editar texto]│  │
│  │                                                            │  │
│  │  ┌─ ⋮⋮ ───────────────────────────────────────────────┐   │  │
│  │  │ 1. [Texto curto ▾] Qual é o seu nome?  [Obrigatória ✓]│  │
│  │  └─────────────────────────────────────────────────────┘   │  │
│  │  ┌─ ⋮⋮ ───────────────────────────────────────────────┐   │  │
│  │  │ 2. [Múltipla escolha ▾] Como avalia o atendimento?  │   │  │
│  │  │    ○ Ótimo  ○ Bom  ○ Regular  ○ Ruim  [+ opção]    │   │  │
│  │  └─────────────────────────────────────────────────────┘   │  │
│  │  ┌─ ⋮⋮ ───────────────────────────────────────────────┐   │  │
│  │  │ 3. [Áudio ▾] Deixe um depoimento         [Opcional] │   │  │
│  │  └─────────────────────────────────────────────────────┘   │  │
│  │                                                            │  │
│  │  [+ Nova pergunta]  [🔄 Refinar com assistente]            │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  [🎨 Personalizar]  [👁 Preview]  [💾 Salvar]  [🚀 Publicar] │
│  └────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 2. Estrutura de Elementos

### 2.1 Área de Input Inicial (Fase 1 — Descrever)

- **Tipo:** caixa de texto grande + opção de voz
- **Posição:** topo da área principal, destaque visual
- **Conteúdo/Dados:**
  - Textarea grande com placeholder: "Descreva o questionário que você quer criar... Ex: 'Preciso de uma pesquisa de satisfação para pacientes de uma clínica médica, com umas 5-6 perguntas'"
  - Botão 🎤 para ditar (voice input)
  - Botão "Enviar"
- **Interações:**
  - Digitar texto livre → clicar Enviar
  - Clicar 🎤 → grava voz, transcreve, preenche o campo
- **Estados visuais:**
  - Vazio: placeholder visível
  - Com texto: botão Enviar habilitado
  - Ditando: 🎤 pulsando, transcrição aparecendo em tempo real

### 2.2 Conversa de Refinamento (Fase 2 — Refinar)

- **Tipo:** thread de chat inline (2-3 mensagens)
- **Posição:** abaixo do input inicial
- **Conteúdo/Dados:**
  - Bolhas do assistente com perguntas de refinamento
  - Campo de resposta do usuário
- **Interações:**
  - Usuário responde perguntas do assistente
  - 1-2 rounds até o sistema ter informação suficiente
  - Usuário pode pular ("Já sei o que quero, gera o esqueleto")
- **Estados visuais:**
  - Digitando: input ativo
  - Processando: "Analisando suas respostas..."
  - Concluído: thread colapsa, esqueleto aparece abaixo

### 2.3 Esqueleto Visual (Fase 3 — Ajustar)

O esqueleto aparece como **cards de pergunta** que o usuário pode manipular de 3 formas.

#### 2.3.1 Cards de Pergunta (caixinhas)

Cada pergunta é um card expansível:

| Elemento | Tipo | Interação |
|---|---|---|
| **Alça de arraste** (⋮⋮) | handle esquerdo | Arrasta para reordenar |
| **Número** | badge | "1.", "2.", automático |
| **Tipo de pergunta** | dropdown inline | Alterna entre: Texto curto, Texto longo, Múltipla escolha, Áudio, Upload de documento |
| **Título** | input editável | Clique → edita inline |
| **Opções** (múltipla escolha) | lista editável | Adicionar/remover/editar opções inline |
| **Toggle "Obrigatória"** | switch | Ativa/desativa |
| **Menu ⋯** | dropdown | Duplicar, Excluir, Mover para cima/baixo |
| **Preview do tipo** | miniatura | Mostra como o respondente verá esse componente |

- **Estados visuais:**
  - Normal: card branco com borda sutil
  - Arrastando: sombra elevada, opacidade levemente reduzida na origem
  - Foco: borda destacada na cor accent

#### 2.3.2 "Nova pergunta" (final da lista)

- **Tipo:** área de placeholder
- **Interação:** clique → dropdown com tipos de pergunta → cria card

#### 2.3.3 Barra de Ações do Esqueleto

| Ação | Descrição |
|---|---|
| **+ Nova pergunta** | Adiciona card ao final |
| **🔄 Refinar com assistente** | Volta a conversar com o sistema sobre ajustes pontuais |
| **[Editar como texto]** | Abre visão textual do esqueleto para edição rápida |

### 2.4 Edição Textual do Esqueleto (Fase 3b)

- **Tipo:** painel toggle — editável como texto puro
- **Acionamento:** botão "[Editar como texto]" no topo do esqueleto visual
- **Conteúdo/Dados:**
  - Textarea com o esqueleto em formato legível/estruturado
  - Exemplo:

```
1. Qual é o seu nome?
   tipo: texto curto
   obrigatória: sim

2. Como você avalia o atendimento?
   tipo: múltipla escolha
   opções: Ótimo, Bom, Regular, Ruim
   obrigatória: sim

3. Deixe um depoimento em áudio:
   tipo: áudio
   obrigatória: não
```

- **Interações:**
  - Editar texto livremente
  - Clicar "Aplicar alterações" → re-parse e atualiza cards visuais
  - Clicar "Cancelar" → descarta alterações textuais
  - Pode ser usado **antes** da primeira geração visual (sistema entrega o texto, usuário edita, depois gera os cards)
  - Pode ser usado **depois** (a qualquer momento para edições rápidas)
- **Estados visuais:**
  - Fechado: só botão "[Editar como texto]"
  - Aberto: textarea ocupa o espaço do esqueleto visual, botões Aplicar/Cancelar

### 2.5 Chat de Ajuste (Fase 3c)

- **Tipo:** thread de chat reaberta para ajustes
- **Acionamento:** botão "🔄 Refinar com assistente"
- **Contexto:** o assistente já sabe o esqueleto atual
- **Interações:**
  - "Troca a pergunta 2 por uma de múltipla escolha"
  - "Adiciona uma pergunta de NPS no final"
  - "A pergunta 3 ficou muito longa, resume"
  - Sistema aplica as mudanças diretamente nos cards visuais

### 2.6 Preview

- **Tipo:** toggle visual (desktop + mobile)
- **Posição:** acessível via botão na barra inferior
- **Conteúdo/Dados:** simulação fiel de como o questionário aparece para o respondente
- **Interações:** navegar entre perguntas, testar validações

### 2.7 Barra Inferior (ações globais)

| Ação | Descrição |
|---|---|
| 🎨 **Personalizar** | Cores, logo, textos de abertura/encerramento |
| 👁 **Preview** | Visualização completa (desktop + mobile) |
| 💾 **Salvar** | Salva rascunho |
| 🚀 **Publicar** | Gera link público |

---

## 3. Fluxo de Processo (completo)

### Etapa 1: Input

```
1. Usuário chega no criador (em branco)
   → Vê uma caixa de texto grande, convidativa

2. Usuário digita ou dita:
   "Preciso de um questionário de NPS para uma academia,
    umas 5 perguntas, incluindo uma de áudio para depoimento"
   
   → Clica [Enviar] ou 🎤 grava e envia
```

### Etapa 2: Refinamento (1-2 rounds)

```
3. Sistema processa o input e responde:
   "Entendi! Algumas perguntas rápidas:
    • O questionário é para alunos ou ex-alunos?
    • Quer uma escala de 0-10 na pergunta de NPS?
    • Alguma pergunta demográfica (idade, gênero)?"

4. Usuário responde:
   "Alunos atuais. Sim, escala 0-10. Não precisa demográfico."
   
   → (Opcional: sistema faz mais 1 pergunta se necessário)

5. Sistema: "Perfeito! Gerando o esqueleto..."
```

### Etapa 3: Geração + Ajuste

```
6. Esqueleto aparece como cards visuais:

   ┌─ ⋮⋮ ────────────────────────────────────────┐
   │ 1. [Múltipla escolha ▾] NPS: Recomendaria?  │
   │    0 1 2 3 4 5 6 7 8 9 10    [Obrigatória ✓] │
   └──────────────────────────────────────────────┘
   ┌─ ⋮⋮ ────────────────────────────────────────┐
   │ 2. [Texto curto ▾] O que mais gosta?         │
   └──────────────────────────────────────────────┘
   ┌─ ⋮⋮ ────────────────────────────────────────┐
   │ 3. [Texto longo ▾] O que pode melhorar?      │
   └──────────────────────────────────────────────┘
   ┌─ ⋮⋮ ────────────────────────────────────────┐
   │ 4. [Múltipla escolha ▾] Frequência semanal   │
   │    ○ 1-2x  ○ 3-4x  ○ 5x+     [Obrigatória ✓] │
   └──────────────────────────────────────────────┘
   ┌─ ⋮⋮ ────────────────────────────────────────┐
   │ 5. [Áudio ▾] Deixe um depoimento  [Opcional] │
   └──────────────────────────────────────────────┘

7. Usuário ajusta:
   
   Forma A — Manipulação direta:
   • Arrasta ⋮⋮ da pergunta 5 para posição 1 (áudio primeiro)
   • Clica no título da pergunta 2, edita: "O que você mais gosta na academia?"
   • Muda tipo da pergunta 3 de "Texto longo" para "Áudio"
   
   Forma B — Edição textual:
   • Clica "[Editar como texto]"
   • Vê o esqueleto em formato texto
   • Troca "Texto longo" por "Áudio" na pergunta 3
   • Adiciona uma opção na pergunta 4
   • Clica "Aplicar alterações" → cards atualizam
   
   Forma C — Chat de ajuste:
   • Clica "🔄 Refinar com assistente"
   • "Troca a pergunta 4 para ser sobre horários preferidos"
   • Sistema atualiza os cards

8. Usuário satisfeito → clica [💾 Salvar] ou [🚀 Publicar]
```

---

## 4. Regras de Negócio

### Fluxo único (não são modos separados)

- As 3 formas de interagir **coexistem** na mesma tela
- O usuário **não escolhe** um modo — ele flui entre as formas conforme a necessidade
- O estado é **compartilhado**: editar no texto reflete nos cards, arrastar cards reflete no texto
- O chat de refinamento (etapa 2) é **obrigatório na primeira criação**, opcional depois

### Ordem das etapas

```
ETAPA 1: INPUT
  → Usuário descreve (texto ou voz)

ETAPA 2: REFINAMENTO
  → Sistema pergunta (1-2 rounds)
  → Usuário pode pular ("Gerar esqueleto")

ETAPA 3: GERAÇÃO
  → Sistema propõe esqueleto visual

ETAPA 4: AJUSTE (loop)
  → Usuário manipula (arrasta, edita inline)
  → OU edita como texto
  → OU conversa com assistente
  → Pode alternar entre as 3 formas livremente

ETAPA 5: PUBLICAÇÃO
  → Salvar + Publicar
```

### Edição textual — regras

- Disponível **antes** da geração visual (sistema pode entregar o texto primeiro, usuário edita, depois gera os cards)
- Disponível **depois** (toggle a qualquer momento)
- Sintaxe clara e legível (não é código — é texto estruturado simples)
- Parse reverso: cards visuais → texto é sempre possível

### Tipos de pergunta

| Tipo | Componente de resposta |
|---|---|
| Texto curto | `<input text>` |
| Texto longo | `<textarea>` |
| Múltipla escolha (única) | Radio buttons |
| Múltipla escolha (múltipla) | Checkboxes |
| Áudio | Gravador de voz |
| Upload de documento | File input (PDF, imagem) |

### Perguntas

- Máximo por questionário: 50 (Free), 200 (Pro), ilimitado (Business)
- Toda pergunta tem: título, tipo, obrigatoriedade (toggle)
- Objetivo do assistente na etapa 2: chegar a 80%+ de completude antes de gerar o esqueleto

---

## 5. Integrações

| Integração | Descrição | Status |
|---|---|---|
| **LLM (OCI/Groq)** | Assistente de refinamento + geração de esqueleto | 🔴 |
| **STT (Groq Whisper)** | Transcrição do input de voz na etapa 1 | 🔴 |
| **Backend Formly** | Salvar questionário, gerar link | 🔴 |

---

## 6. Cenários de Teste

### Fluxo completo feliz

- [ ] Etapa 1: Usuário digita descrição → sistema entende
- [ ] Etapa 1: Usuário dita descrição → transcrito corretamente
- [ ] Etapa 2: Sistema faz perguntas pertinentes (1-2 rounds)
- [ ] Etapa 2: Usuário responde → sistema refina entendimento
- [ ] Etapa 2: Usuário pula refinamento → vai direto para geração
- [ ] Etapa 3: Sistema gera esqueleto com tipos corretos de pergunta
- [ ] Etapa 4: Arrastar ⋮⋮ reordena cards
- [ ] Etapa 4: Clicar título → edita inline
- [ ] Etapa 4: Mudar tipo via dropdown → card se adapta
- [ ] Etapa 4: Adicionar opção em múltipla escolha
- [ ] Etapa 5: Salvar persiste, Publicar gera link

### Edição textual

- [ ] Abrir "[Editar como texto]" → vê esqueleto formatado
- [ ] Editar texto → "Aplicar alterações" → cards atualizam
- [ ] Cards visuais → texto sempre consistente (ida e volta)
- [ ] Cancelar edição textual → cards voltam ao estado anterior
- [ ] Usar edição textual ANTES da geração visual → mesma experiência

### Chat de ajuste

- [ ] "🔄 Refinar com assistente" com esqueleto existente → assistente contextualizado
- [ ] "Troca a pergunta X por tipo Y" → sistema aplica
- [ ] "Adiciona pergunta sobre Z" → sistema adiciona
- [ ] Chat mantém histórico da conversa inicial

### Cross-interação

- [ ] Editar no texto → cards atualizam em tempo real
- [ ] Arrastar cards → texto atualiza se aberto
- [ ] Chat altera pergunta → card atualiza
- [ ] Voltar ao chat depois de editar cards → assistente sabe o estado atual
