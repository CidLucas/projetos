# ✏️ Página 01 — Criador (Builder)

> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

O **Criador** é a experiência core do Formly — um builder híbrido onde o usuário monta questionários **conversando com uma IA** (chat) e **editando diretamente** os elementos na tela (canvas). Inspirado em v0.dev / Bolt.new: o chat gera, o canvas exibe, e o usuário refina nos dois canais simultaneamente.

### Layout

```
┌──────────────────────────────────────────────────────────────┐
│ 🧠 Formly    [Nome do Questionário]            [🔗 Publicar] │
├─────────────────────────┬────────────────────────────────────┤
│                         │                                    │
│  ┌───────────────────┐  │  ┌────────────────────────────┐   │
│  │ 💬 Chat           │  │  │ 📋 Preview                 │   │
│  │                   │  │  │                            │   │
│  │ IA: "Vi que você  │  │  │  1. 📝 Qual seu nome?     │   │
│  │ está montando uma │  │  │     [___________________]  │   │
│  │ pesquisa de clima.│  │  │                            │   │
│  │ Quer incluir      │  │  │  2. ⭐ Avalie o serviço    │   │
│  │ perguntas de      │  │  │     ○ 1 ○ 2 ○ 3 ○ 4 ○ 5  │   │
│  │ múltipla escolha?"│  │  │                            │   │
│  │                   │  │  │  3. 🎤 Conte sua exp.     │   │
│  │ Você: "Sim, e     │  │  │     [🎙️ Gravar áudio]     │   │
│  │ também uma de     │  │  │                            │   │
│  │ áudio no final"   │  │  │  [+ Adicionar pergunta]   │   │
│  │                   │  │  │                            │   │
│  │ [🎤 ou digite...] │  │  └────────────────────────────┘   │
│  └───────────────────┘  │                                    │
│                         │  ┌────────────────────────────┐   │
│                         │  │ ⚙️ Propriedades            │   │
│                         │  │ (ao selecionar pergunta)    │   │
│                         │  │ Tipo: [Múlt. escolha ▾]    │   │
│                         │  │ Obrigatória: [✓]            │   │
│                         │  │ Opções: [+ adicionar]       │   │
│                         │  └────────────────────────────┘   │
└─────────────────────────┴────────────────────────────────────┘
```

---

## 2. Estrutura de Elementos

### 2.1 Topbar

| Elemento | Tipo | Detalhes |
|---|---|---|
| Logo | ícone + texto | 🧠 Formly |
| Nome do questionário | input inline editável | Clique → edita título |
| Status | indicador | Rascunho / Publicado |
| Botão Publicar | btn primário | Gera link público |
| Botão Preview | btn secundário | Abre preview em nova aba |

### 2.2 Chat Panel (coluna esquerda)

| Elemento | Tipo | Detalhes |
|---|---|---|
| Área de mensagens | scroll vertical | Bolhas user (direita) + IA (esquerda) |
| Mensagem IA | bolha | Markdown, pode conter cards interativos (ex: "Aceitar esqueleto proposto?") |
| Mensagem user | bolha | Texto ou transcrição de áudio |
| Input | campo texto | Placeholder: "Descreva seu questionário ou peça uma mudança..." |
| Botão 🎤 | btn ícone | Grava áudio do criador → transcreve → envia como texto |
| Spinner "Pensando..." | indicador | Enquanto IA processa |

### 2.3 Canvas / Preview (coluna direita)

| Elemento | Tipo | Detalhes |
|---|---|---|
| Lista de perguntas | coluna vertical | Ordem editável por drag & drop |
| Card de pergunta | card | Número, tipo (ícone), texto da pergunta |
| ↳ Ícone do tipo | ícone à esquerda | 📝 texto, ☑️ múltipla, 🎤 áudio, ⭐ escala, 📎 upload |
| ↳ Preview da resposta | mock | Mostra como o respondente verá (input, opções, gravador) |
| ↳ Handle de arraste | ícone ≡ | Reordenar pergunta |
| ↳ Botão ⋮ | menu contextual | Editar, duplicar, excluir |
| Botão "+ Adicionar pergunta" | btn outline | Insere nova pergunta no final |
| Seletor de tema | dropdown | Escolhe tema visual do questionário |
| Indicador de progresso | barra | "5/10 perguntas" |

### 2.4 Painel de Propriedades (coluna direita, condicional)

Aparece quando uma pergunta está selecionada no canvas:

| Elemento | Tipo | Detalhes |
|---|---|---|
| Tipo de pergunta | select | 📝 Texto curto, 📄 Parágrafo, ☑️ Múltipla escolha, 🎤 Áudio, ⭐ Escala, 📎 Upload |
| Texto da pergunta | textarea | Editável |
| Obrigatória | toggle | Sim / Não |
| Placeholder | input | Texto de ajuda para o respondente |
| **Opções (se múltipla escolha)** | lista editável | Adicionar/remover/editar opções |
| **Labels da escala (se escala)** | 2 inputs | Label mínimo + Label máximo |
| **Máx. caracteres (se texto)** | number | Limite de caracteres |
| **Formatos aceitos (se upload)** | checkboxes | PDF, imagem, DOCX |
| Agente de follow-up | toggle | Ativar/desativar aprofundamento de resposta |

### 2.5 Modal de Publicação

| Elemento | Tipo | Detalhes |
|---|---|---|
| Link público | input readonly + btn copiar | `https://formly.app/s/abc123` |
| QR code | imagem | Gerado automaticamente |
| Preview do questionário | iframe/thumbnail | Miniatura de como ficou |
| Aba "Distribuir" | tab | Lista de contatos + envio |
| Lista de contatos | tabela/lista | Nome, e-mail/telefone, checkbox selecionar |
| Campo de busca | input | Filtrar contatos |
| Botão "Enviar por e-mail" | btn | Dispara envio (Fase 3) |
| Botão "Enviar por WhatsApp" | btn | Abre WhatsApp Web com link (Fase 3) |
| Botão "Copiar link" | btn outline | Copia para clipboard |

### 2.6 Gerenciador de Contatos (seção do criador)

| Elemento | Tipo | Detalhes |
|---|---|---|
| Lista de contatos | tabela | Nome, e-mail, telefone, total de pesquisas respondidas |
| Adicionar contato | btn + modal | Nome, e-mail, telefone |
| Importar CSV | btn upload | Upload de lista de contatos |
| Grupos | tags | Organizar contatos em grupos (ex: "Clientes", "Equipe") |

---

## 3. Fluxos de Processo

### 3.1 Fluxo completo de criação (4 passos + publicação)

```
┌─────────────────────────────────────────────────────────┐
│ PASSO 1: INPUT                                          │
│ ─────────────                                           │
│ Usuário digita ou fala no chat:                         │
│ "Preciso de uma pesquisa de satisfação pós-evento       │
│  com 8 perguntas, público corporativo"                  │
│                                                         │
│ Interação: CONVERSA (chat)                              │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ PASSO 2: REFINAMENTO                                    │
│ ─────────────────────                                   │
│ IA responde com 1-2 perguntas de afinação:              │
│ "Certo! Algumas perguntas:                              │
│  1. Quer incluir áudio como opção de resposta?          │
│  2. Prefere escala 1-5 ou 1-10?"                        │
│                                                         │
│ Usuário responde no chat                                │
│ Interação: CONVERSA (chat)                              │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ PASSO 3: GERAÇÃO                                        │
│ ─────────────────                                       │
│ IA monta esqueleto e exibe no canvas:                   │
│                                                         │
│  1. 📝 Nome completo (texto curto)                      │
│  2. 📝 Empresa (texto curto)                            │
│  3. ⭐ Satisfação geral (escala 1-5)                    │
│  4. ⭐ Organização (escala 1-5)                         │
│  5. ⭐ Conteúdo (escala 1-5)                            │
│  6. ☑️ O que mais gostou? (múltipla escolha)            │
│  7. 📄 Sugestões de melhoria (parágrafo)                │
│  8. 🎤 Comentário livre (áudio)                         │
│                                                         │
│ Interação: VISUAL (canvas) — IA gerou, usuário vê       │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ PASSO 4: AJUSTE                                         │
│ ───────────────                                         │
│ 3 formas de interação COEXISTINDO:                      │
│                                                         │
│ A) CONVERSA: "Troca a pergunta 6 por escala"            │
│    → IA processa, canvas atualiza                       │
│                                                         │
│ B) EDIÇÃO DIRETA: Clica no texto da pergunta 1          │
│    → Edita inline, muda placeholder                     │
│                                                         │
│ C) DRAG & DROP: Arrasta pergunta 8 para posição 3       │
│    → Reordena instantaneamente                          │
│                                                         │
│ D) PAINEL DE PROPRIEDADES: Clica na pergunta 3          │
│    → Abre painel direito, muda tipo, obrigatoriedade    │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ PASSO 5: PUBLICAÇÃO                                     │
│ ──────────────────                                      │
│ Usuário clica "Publicar"                                │
│ → Sistema valida: todas as perguntas têm texto?         │
│ → Gera link único: formly.app/s/abc123                  │
│ → Gera QR code                                          │
│ → Página web renderiza com design system + componentes  │
│ → Todos os componentes já ligados na API                │
│   (POST /api/responses/:surveyId)                       │
│                                                         │
│ Modal de publicação abre com:                           │
│  • Link copiável                                        │
│  • QR code                                              │
│  • Preview em thumbnail                                 │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ PASSO 6: DISTRIBUIÇÃO                                   │
│ ─────────────────────                                   │
│ Da modal de publicação, usuário pode:                   │
│                                                         │
│ V1:                                                     │
│  • Copiar link (colar onde quiser)                      │
│  • Baixar QR code (imprimir, postar)                    │
│                                                         │
│ FASE 3:                                                 │
│  • Selecionar contatos da lista                         │
│  • Enviar por e-mail (template com link)                │
│  • Enviar por WhatsApp (link direto)                    │
│  • Agendar follow-up (reenviar para quem não respondeu) │
└─────────────────────────────────────────────────────────┘
```

### 3.2 Edição de questionário já publicado

```
1. Criador acessa questionário publicado no dashboard
2. Clica "Editar" → volta ao builder
3. Alterações são salvas como rascunho
4. Clica "Publicar alterações" → atualiza link público
5. Respostas já coletadas não são afetadas
```

---

## 4. Regras de Negócio

### Comportamento do chat

- IA tem contexto do questionário inteiro (memória da conversa)
- IA pode propor cards interativos: "Aceitar esqueleto?", "Qual tema prefere?"
- IA NÃO edita diretamente — sempre propõe, usuário confirma
- Chat e canvas são bidirecionais: mudar no canvas atualiza contexto do chat, e vice-versa

### Comportamento do canvas

- Sempre mostra o estado real do questionário
- Drag & drop para reordenar
- Clique em pergunta → painel de propriedades abre
- Preview inline de cada tipo de resposta
- Preview em tempo real das mudanças do chat
- Indicador visual quando IA está sugerindo alteração (borda pulsante na pergunta afetada)

### Tipos de pergunta e seus controles

| Tipo | Controles no painel de propriedades |
|---|---|
| 📝 Texto curto | Placeholder, máx. caracteres, obrigatória |
| 📄 Parágrafo | Placeholder, máx. caracteres, obrigatória |
| ☑️ Múltipla escolha | Opções (add/remove/edit), seleção única ou múltipla, obrigatória |
| 🎤 Áudio | Duração máx. (30s/60s/120s), obrigatória, follow-up |
| ⭐ Escala | Mín 1–Máx 10, labels dos extremos, obrigatória |
| 📎 Upload | Formatos aceitos (checkbox), tamanho máx., obrigatória |

### Temas

- 3-4 temas pré-construídos na Fase 1
- Cada tema define: cores, tipografia, espaçamento, bordas, tom
- Brand kit: logo + cor primária do criador (sobrescreve tema)
- Preview mostra tema selecionado

---

## 5. Integrações

| Elemento | Integração | Status |
|---|---|---|
| Chat IA | LLM (Groq/OCI) com prompt de sistema + histórico | A construir |
| Transcrição de voz (criador) | Groq Whisper | A construir |
| Geração de esqueleto | LLM com output estruturado (JSON schema das perguntas) | A construir |
| Salvar questionário | POST/PUT /api/surveys | A construir |
| Publicar | POST /api/surveys/:id/publish → retorna link | A construir |
| Upload de áudio (criador) | S3 presigned URL | A construir |
| Envio de e-mail | Resend / SES | Fase 3 |
| Envio WhatsApp | WhatsApp Business API | Fase 3 |

---

## 6. Cenários de Teste

### Passo 1 — Input
- [ ] Digitar descrição da pesquisa → IA responde em < 5s
- [ ] Gravar áudio com descrição → transcrito → IA responde
- [ ] Descrição vazia → IA pede mais detalhes
- [ ] Descrição muito vaga ("faz uma pesquisa") → IA faz perguntas de refinamento

### Passo 2 — Refinamento
- [ ] IA pergunta sobre incluir áudio → usuário diz sim → esqueleto inclui pergunta de áudio
- [ ] IA pergunta sobre escala → usuário escolhe 1-5 → esqueleto usa 1-5
- [ ] Usuário responde "não sei" → IA escolhe default razoável

### Passo 3 — Geração
- [ ] Esqueleto aparece no canvas em < 10s
- [ ] Tipos de pergunta são variados (não tudo igual)
- [ ] Número de perguntas corresponde ao pedido
- [ ] Preview de cada tipo renderiza corretamente

### Passo 4 — Ajuste
- [ ] Comando no chat "troca pergunta 3 por áudio" → canvas atualiza tipo
- [ ] Comando no chat "remove pergunta 5" → pergunta some do canvas
- [ ] Comando no chat "adiciona pergunta de texto no final" → nova pergunta aparece
- [ ] Edição direta: clicar no texto → editar → salvar
- [ ] Drag & drop: arrastar pergunta → reordenar → salvar
- [ ] Painel de propriedades: mudar tipo, opções, obrigatoriedade
- [ ] Alteração no chat + alteração direta simultâneas → sem conflito

### Passo 5 — Publicação
- [ ] Clicar Publicar → questionário validado
- [ ] Questionário sem perguntas → erro "Adicione pelo menos 1 pergunta"
- [ ] Pergunta sem texto → erro "Todas as perguntas precisam de texto"
- [ ] Link gerado → copiável → funcional
- [ ] QR code gerado → escaneável
- [ ] Página pública renderiza com tema correto
- [ ] Componentes respondem (POST funciona)

### Passo 6 — Distribuição
- [ ] Copiar link → cola no navegador → questionário abre
- [ ] Selecionar contatos → enviar e-mail → e-mail chega com link (Fase 3)
- [ ] WhatsApp → abre com link preenchido (Fase 3)

### Edge cases
- [ ] Criador fecha browser durante edição → rascunho salvo
- [ ] Dois criadores editando mesmo questionário → ? (v1: último salva ganha)
- [ ] Questionário publicado é editado → link permanece mesmo, conteúdo atualiza
