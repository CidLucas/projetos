# 👥 Clientes — Tela de Requisitos de UI (Blue V3)

> Última atualização: 2026-08-11 | Status: 🟡 Em andamento (esmiuçando para design)
> Segue o padrão de [template-tela.md](./template-tela.md). Fluxo do kanban em [kanbans.md](./kanbans.md).
> **Princípio:** elementos puros — informação + ação. Nenhum elemento é amarrado ao design atual da Blu; tudo nasce como novo conceito.

---

## 1. Layout macro da tela

```
┌──────────────────────────────────────────────────────────────────────────┐
│ A · Topo:  [Kanban] [Follow-up] [Histórico] [Rotinas]   …   [+ Novo]     │
│            (abas discretas — sem faixa horizontal)                       │
├───────────────────────────────────────────────────────┬──────────────────┤
│ B · QUADRO PRINCIPAL (kanban)                         │ C · PAINEL       │
│   💬 Conversa │ 🧾 Orçamento │ 📎 Fechamento │        │   DIREITO        │
│   ✅ Fechado  │ 🔁 Recorrência                        │   (faixa         │
│                                                       │    vertical —    │
│   [x] Card 1        [x] Card 2     [ ] Card 3         │    card          │
│   ...                                                 │    selecionado)  │
│                                                       │                  │
│   ← seleção múltipla + barra de ações em lote →       │                  │
├───────────────────────────────────────────────────────┴──────────────────┤
│ D · (opcional — adiado por padrão)  [Insights] [Métricas] [Interlocutores]│
└──────────────────────────────────────────────────────────────────────────┘
```

Layout mínimo do design inicial: **Topo (abas) + Quadro + Painel direito**. A região D fica de fora por enquanto — só entra se provar valor depois.

---

## 2. Região A — Topo

### 2.1 Navegação por abas (discretas, sem strip)
- **Elemento:** `NavegacaoAbas` (novo conceito)
- **Propósito:** trocar entre as 4 visões da sala **sem faixa horizontal** — abas como texto discreto com indicador de estado (cor + peso + contador), sem fundo, sem borda, sem barra sublinhada
- **Abas (ordem):** Kanban (padrão) · Follow-up · Histórico · Rotinas
- **Conteúdo (informações):** nome da aba + contador de pendência (ex.: Follow-up "5")
- **Opções:** nenhuma além da própria troca de aba (abas fixas da dimensão)
- **Ações:** clique troca a visão; persiste a última aba por sessão
- **Estados:** ativa (destaque de cor) / inativa / com pendência (contador)
- **Visibilidade:** sempre
- **Feedback:** transição suave da visão

### 2.2 Busca
- **Elemento:** `CampoBusca`
- **Propósito:** achar cliente por nome, contato ou segmento
- **Conteúdo (informações):** placeholder "Buscar cliente..."; resultados em painel suspenso (nome, contato, coluna atual)
- **Ações:** digitar filtra; Enter confirma e abre o primeiro resultado
- **Estados:** vazio / digitando (sugestões) / sem resultados ("Nenhum cliente encontrado") / loading
- **Visibilidade:** sempre no topo

### 2.3 Filtros do quadro
- **Elemento:** `Filtros`
- **Propósito:** restringir o quadro por atributos do cliente
- **Opções:** Segmento (todos/…), Responsável (todos/dono/membro…), Risco (todos/oportunidade/alerta/risco), Valor (faixa mín–máx)
- **Ações:** múltiplos filtros combináveis; "Limpar filtros" aparece quando há filtro ativo
- **Estados:** ativo (badge com contagem de filtros) / inativo
- **Visibilidade:** sempre

### 2.4 Botão "Novo cliente"
- **Elemento:** `BotaoPrimario` (ícone +)
- **Propósito:** criar cliente do zero
- **Ações:** abre overlay de criação (Região E)
- **Estados:** default / hover / disabled (sem permissão de criar — papéis fixos)
- **Visibilidade:** sempre

---

## 3. Região B — Quadro principal (kanban)

### 3.1 Quadro
- **Elemento:** `QuadroKanban`
- **Propósito:** mostrar o estágio de cada cliente no fluxo do começo ao fim e permitir mover/agir em lote
- **Conteúdo (informações):** 5 colunas (kanbans.md §3.2): 💬 Conversa → 🧾 Orçamento → 📎 Fechamento → ✅ Fechado → 🔁 Recorrência; cada coluna com contador
- **Ações:** scroll horizontal; arrastar cards; clicar card abre o painel direito; **seleção múltipla** (ver 3.5)
- **Estados:** loading (esqueleto) / vazio (mensagem + CTA "Adicionar primeiro cliente") / erro (recarregar)
- **Feedback:** animação ao mover; toast em falha

### 3.2 Coluna
- **Elemento:** `ColunaKanban`
- **Conteúdo (informações):** nome da etapa, contador ("Conversa · 12"), cor da coluna (identidade da etapa)
- **Opções (menu da coluna):** recolher/expandir coluna, ordenar coluna (valor/prazo/recência)
- **Ações:** área de soltar cards; recolher (mostra só o cabeçalho)
- **Estados:** recolhida / vazia (dropzone visível) / cheia
- **Visibilidade:** sempre

### 3.3 Card de cliente
- **Elemento:** `CartaoCliente`
- **Propósito:** resumo do cliente em uma linha — o dono entende onde ele está e o que precisa sem abrir nada
- **Conteúdo (informações):**
  - Nome do cliente
  - Badge de etapa interna (ex.: "Aguardando aprovação", "Rascunho", "Enviado")
  - Semáforo 🟢 no prazo / 🟡 parado há X dias / 🔴 urgente (borda esquerda)
  - Valor potencial (R$)
  - Prazo ou recência ("há 2d")
  - Responsável (avatar)
- **Opções (menu "..." do card):** Mover para…, Gerar artefato…, Aprovar pendência, Duplicar, Arquivar, Excluir (com confirmação)
- **Ações:** clique → abre painel direito; arrastar → mover de coluna; **checkbox de seleção** (ver 3.5); ações rápidas no hover (aprovar, mover, comentar)
- **Estados:** default / hover / arrastando (elevado) / selecionado (checkbox marcado + destaque) / semáforo por cor / disabled
- **Visibilidade:** sempre que há clientes

### 3.4 Barra de ações em lote (seleção múltipla)
- **Elemento:** `BarraAcoesLote`
- **Propósito:** agir em vários cards de uma vez — aparece quando 2 ou mais cards estão selecionados
- **Conteúdo (informações):** contador ("5 selecionados") + ações
- **Opções/ações:**
  - **Mover para…** (escolher coluna de destino — aplica em todos)
  - **Gerar artefato…** (escolher tipo — gera para todos)
  - **Aprovar pendências** (aprova respostas/artefatos pendentes dos selecionados)
  - **Marcar lido** (mensagens novas)
  - **Arquivar** / **Excluir** (com confirmação dupla)
  - **Limpar seleção** (X ou Esc)
- **Estados:** visível só com seleção ativa; ações desabilitadas se nenhum card atende o critério
- **Feedback:** toast de sucesso contando quantos foram afetados ("3 movidos para Orçamento"); confirmação antes de excluir
- **Visibilidade:** substitui a barra de filtros do quadro enquanto há seleção

### 3.5 Seleção de cards
- **Elemento:** `SelecaoMultipla` (comportamento do quadro)
- **Ações:**
  - Checkbox no card (hover ou fixo) → marca individual
  - Clique com **Shift** → seleciona intervalo (na mesma coluna)
  - Clique com **Ctrl/Cmd** → alterna card sem perder seleção
  - **Selecionar tudo na coluna** (checkbox no cabeçalho da coluna)
  - Clique em card já selecionado sem teclado → abre o painel (sem desmarcar)
  - Esc → limpa seleção
- **Estados:** card selecionado (contorno/destaque), coluna toda selecionada (checkbox cheio)
- **Visibilidade:** comportamento do quadro; a barra de lote aparece com 2+

---

## 4. Região C — Painel direito (faixa vertical)

> Painel lateral fixo (~380px), abre ao clicar num card. **Conceito:** o dono gerencia o cliente do começo ao fim sem sair daqui.

### 4.1 Cabeçalho do painel
- **Elemento:** `CabecalhoPainel`
- **Conteúdo (informações):** nome do cliente + semáforo + valor potencial; menu "..." (editar, duplicar, arquivar, excluir)
- **Ações:** fechar (X); editar abre overlay de formulário
- **Visibilidade:** sempre que um card está selecionado

### 4.2 Conversa (mensagens com o cliente)
- **Elemento:** `ConversaCliente`
- **Propósito:** ver e responder a troca de mensagens com o cliente, com o ciclo **notificada → respondida pelo agente → aprovada pelo dono → enviada**
- **Conteúdo (informações):** linha do tempo de mensagens — cliente (cinza) e agente (azul); cada mensagem do agente com status: `Rascunho` → `Aguardando aprovação` → `Enviada`; notificação visual quando chega mensagem nova
- **Ações:** expandir mensagem; copiar; reenviar (se falhou); ver detalhe do status
- **Estados:** mensagem pendente (contorno de atenção) / thread vazia ("Nenhuma mensagem ainda") / loading
- **Visibilidade:** sempre no painel

### 4.3 Campo de resposta
- **Elemento:** `CampoResposta`
- **Propósito:** o dono escreve direto ou pede rascunho ao agente
- **Conteúdo (informações):** caixa de texto + botão "Gerar resposta (IA)" + botão enviar
- **Opções:** Enviar direto (se tiver permissão) ou Gerar com IA → rascunho fica "Aguardando aprovação"
- **Ações:** Enter envia; Esc limpa; atalho para IA
- **Estados:** escrevendo / enviando (disabled) / vazio (placeholder)
- **Feedback:** toast de envio; aviso "rascunho gerado pela IA — revise antes de aprovar"

### 4.4 Aprovação inline
- **Elemento:** `AprovacaoInline`
- **Propósito:** aprovar/editar/rejeitar qualquer pendência (resposta ou artefato) sem trocar de tela
- **Conteúdo (informações):** pendência resumida + botões
- **Opções:** Aprovar · Editar · Rejeitar (pede motivo opcional)
- **Estados:** pendente / aprovado / rejeitado
- **Visibilidade:** só quando existe pendência (resposta ou artefato)

### 4.5 Informações do cliente
- **Elemento:** `InformacoesCliente`
- **Conteúdo (informações):** contato (WhatsApp, e-mail), segmento, valor potencial, origem do contato, criado em, responsável
- **Ações:** botão Editar → overlay de formulário
- **Estados:** campo sem valor (placeholder "—")
- **Visibilidade:** sempre

### 4.6 Etapa atual + mover
- **Elemento:** `ControleEtapa`
- **Conteúdo (informações):** coluna atual + aprovador da etapa
- **Opções:** dropdown "Mover para…" com as 5 colunas (pular etapa exige confirmação)
- **Ações:** mover atualiza o card e registra no Histórico
- **Feedback:** toast "Movido para Orçamento"

### 4.7 Artefatos (fechamento do cliente)
- **Elemento:** `ArtefatosCliente`
- **Propósito:** gerar e acompanhar os documentos do cliente **a partir do orçamento aprovado** — o dono escolhe o que o cliente precisa
- **Conteúdo (informações):** lista de artefatos gerados (tipo, status: gerado/enviado/assinado) + botão "Gerar artefato"
- **Opções do menu "Gerar artefato":**
  - **Orçamento** — cotação enviada ao cliente (estágio Orçamento)
  - **Plano de trabalho** — quando o orçamento aprovado é de **serviço** (escopo, etapas, prazos)
  - **Nota fiscal** — sempre que houver venda fechada
  - **Contrato** — quando houver acordo formal (assinatura)
  - **Pedido de envio** — quando o cliente **compra um produto** (envio/entrega)
- **Ações:** gerar (usa template de documento), visualizar (preview), baixar PDF, enviar ao cliente, assinar
- **Estados:** vazio ("Nenhum artefato") / gerando / erro de geração
- **Feedback:** toast sucesso/erro; artefato entra na lista e no Histórico
- **Visibilidade:** sempre no painel

### 4.8 Integrações (atalhos)
- **Elemento:** `AtalhosIntegracao`
- **Conteúdo (informações):** atalhos do cliente: Abrir WhatsApp · Enviar e-mail · Agendar follow-up (calendário) · (outras conforme integração)
- **Ações:** cada atalho abre o canal externo / cria evento
- **Estados:** disabled quando a integração não está configurada (com explicação)
- **Visibilidade:** sempre

### 4.9 Interlocutores
- **Elemento:** `Interlocutores`
- **Conteúdo (informações):** quem está envolvido no card: responsável, agente IA, cliente (avatar + nome + papel)
- **Ações:** clique mostra contato; iniciar conversa interna
- **Visibilidade:** sempre

---

## 5. Região D — Elementos abaixo (opcional, adiado)

> Decisão: **não entra no design inicial.** O layout mínimo é Topo + Quadro + Painel direito. Se depois provar valor, candidatos:

- **Insights do agente** — sugestões proativas (ex.: "Cliente X parado há 5 dias")
- **Métricas da sala** — pipeline, win rate, ticket médio, NRR (período 30/90/1y)
- **Interlocutores da sala** — quem participa dos processos

---

## 6. Overlays (Região E)

### 6.1 Overlay "Novo cliente"
- **Elemento:** `OverlayFormulario`
- **Campos:** nome, contato (WhatsApp/e-mail), segmento, valor potencial, responsável, coluna inicial (padrão Conversa)
- **Ações:** Salvar (cria card + registra Histórico) · Cancelar
- **Validação:** nome obrigatório; contato válido
- **Feedback:** toast "Cliente criado"; erro de duplicidade

### 6.2 Overlay "Editar cliente" (mesmo formulário preenchido)

### 6.3 Overlay "Visualizar artefato"
- **Conteúdo (informações):** preview do documento + ações (Baixar, Enviar, Assinar)

### 6.4 Confirmações
- Excluir card/artefato → confirmação; Rejeitar pendência → motivo opcional; Mover pulando etapas → aviso.

---

## 7. Biblioteca de elementos (novo conceito — para o design system)

> Elementos puros, sem herança do design atual. Nome + propósito; o desenho vem depois.

| Elemento | Região | Propósito |
|---|---|---|
| `NavegacaoAbas` | A | abas discretas sem faixa horizontal, com contador |
| `CampoBusca` | A | busca rápida com sugestões |
| `Filtros` | A | restringir quadro por atributos combináveis |
| `BotaoPrimario` | A | criar cliente |
| `QuadroKanban` | B | colunas do fluxo, arrastar, seleção múltipla |
| `ColunaKanban` | B | etapa com contador, cor, dropzone |
| `CartaoCliente` | B | resumo do cliente: badge, semáforo, valor, prazo, responsável |
| `SelecaoMultipla` | B | checkbox por card/coluna, Shift/Ctrl, selecionar tudo |
| `BarraAcoesLote` | B | mover/gerar/aprovar/arquivar em massa |
| `Semafaro` | B/C | indicador 🟢🟡🔴 de atenção |
| `CabecalhoPainel` | C | identidade do item + fechar/editar |
| `ConversaCliente` | C | thread de mensagens com status de envio |
| `CampoResposta` | C | responder direto ou gerar rascunho IA |
| `AprovacaoInline` | C | aprovar/editar/rejeitar pendência no lugar |
| `InformacoesCliente` | C | dados de contato/segmento/valor |
| `ControleEtapa` | C | mover entre colunas com confirmação |
| `ArtefatosCliente` | C | gerar/listar artefatos (orçamento, plano, NF, contrato, envio) |
| `AtalhosIntegracao` | C | WhatsApp, e-mail, calendário |
| `Interlocutores` | C | quem está envolvido |
| `OverlayFormulario` | E | criar/editar com validação |
| `OverlayArtefato` | E | preview + ações do documento |

---

## 8. Regras de negócio de UI (resumo)

| # | Regra |
|---|---|
| U1 | Aba padrão = Kanban; última aba persiste por sessão |
| U2 | Colunas do kanban são fixas (etapas da dimensão) — não renomear/remover na UI |
| U3 | Pendência aparece com contador na aba Follow-up e na Home |
| U4 | Todo movimento de card e todo artefato gerado registram no Histórico |
| U5 | Pular etapas exige confirmação |
| U6 | Papéis fixos: aprovador vê Aprovar; criador vê Gerar; visualizador só vê |
| U7 | Sem permissão de criar → "Novo cliente" desabilitado |
| U8 | Ações em lote só aparecem com 2+ selecionados; excluir em lote exige confirmação dupla |
| U9 | Artefato só é gerado a partir de orçamento aprovado (exceto o próprio orçamento) |

---

## 9. Cenários de teste (UI)

- [ ] Criar cliente → card na Conversa + toast + Histórico
- [ ] Gerar resposta IA → "Aguardando aprovação" → Aprovar → "Enviada"
- [ ] Rejeitar resposta → motivo opcional → rascunho volta para edição
- [ ] Selecionar 3 cards (Ctrl+clique) → barra de lote → Mover para Orçamento → 3 movidos + Histórico
- [ ] Selecionar coluna inteira (checkbox do cabeçalho) → gerar artefato em lote
- [ ] Orçamento aprovado → menu de artefatos mostra Plano de trabalho, NF, Contrato, Pedido de envio
- [ ] Cliente de produto → gerar "Pedido de envio"; cliente de serviço → "Plano de trabalho"
- [ ] Filtros combinados → quadro filtra; Limpar filtros volta ao todo
- [ ] Nenhum cliente → estado vazio com CTA
- [ ] Permissão visualizador → sem botões de ação

---

## 10. Decisões em aberto

1. **Abas discretas:** texto + indicador de cor, sem fundo/borda (conforme pedido) — confirmar que é essa a leitura de "sem strip"?
2. **Painel direito:** faixa vertical fixa ~380px vs. sobreposição? (proposta: fixa)
3. **Região D (quadrinhos abaixo):** confirmar que fica de fora do design inicial?
4. **Seleção múltipla:** checkbox fixo visível no card vs. só no hover? (proposta: visível no hover + cabeçalho da coluna com "selecionar tudo")
5. **Ações em lote mínimas:** Mover / Gerar artefato / Aprovar / Marcar lido / Arquivar / Excluir — sobra ou falta alguma?
6. **WhatsApp como canal de mensagens:** confirma? (define integração e o envio)
7. **Coluna "Fechamento"** (era Artefatos): nome bom? Ajuda a indicar que ali se formaliza (plano/NF/contrato/envio).
