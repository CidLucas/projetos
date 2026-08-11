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
│            (sem strip de métricas — métricas vivem em D)                 │
├───────────────────────────────────────────────────────┬──────────────────┤
│ B · VISÃO DA ABA ATIVA                               │ C · PAINEL       │
│   [Kanban] 5 colunas:                                │   DIREITO        │
│   💬 Conversa │ 🧾 Orçamento │ 📎 Fechamento │        │   (faixa         │
│   ✅ Fechado  │ 🔁 Recorrência                        │    vertical,     │
│                                                       │    FIXA ~380px)  │
│   [x] Card 1        [x] Card 2     [ ] Card 3         │                  │
│   ← barra de ações em lote →                          │                  │
│   [Follow-up] lista de pendências · [Histórico]       │                  │
│   timeline · [Rotinas] config + feed (seções 3.6-3.8) │                  │
├───────────────────────────────────────────────────────┴──────────────────┤
│ D · QUADRINHOS:  [Insights do agente] [Métricas da sala] [Interlocutores] │
└──────────────────────────────────────────────────────────────────────────┘
```

Layout do design inicial (decisões 11/08): **Topo (abas discretas) + Quadro + Painel direito fixo + Quadrinhos (D)**. **Não existe strip de métricas** — nenhuma faixa horizontal de KPIs acima das abas; as métricas da sala ficam no quadrinho D.

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

## 3B. Aba Follow-up (visão de pendências)

> Conceito: o dono não caça pendência — a aba junta tudo que precisa de atenção nos clientes. **Pendências nascem automáticas** (decisão 12/08): parados, orçamentos sem resposta, recorrências atrasadas, aprovações quando há pendência real — o agente cria e o dono resolve. O contador no nome da aba (ex.: "Follow-up 5") = total de pendências ativas.

### 3B.1 Cabeçalho da visão
- **Elemento:** `CabecalhoVisaoFollowUp`
- **Propósito:** resumir e filtrar a fila de pendências
- **Conteúdo (informações):** título "Follow-up" + subtítulo ("5 clientes precisam de atenção") + total em valor potencial (ex.: "R$ 12.400 em jogo")
- **Opções (filtros):** Nível (todos/oportunidade/alerta/risco), Tipo (todos/parado/orçamento/recorrência/aprovação), Responsável (todos/dono/membro…)
- **Ações:** múltiplos filtros combináveis; "Limpar filtros" quando ativo; ordenar por (urgência/recência/valor potencial)
- **Estados:** filtro ativo (badge com contagem) / inativo
- **Visibilidade:** sempre na aba Follow-up

### 3B.2 Lista de follow-ups
- **Elemento:** `ListaFollowUp`
- **Propósito:** apresentar as pendências em ordem de atenção — o que está vermelho aparece primeiro
- **Conteúdo (informações):** cards de pendência (3B.3) ordenados por semáforo 🔴 → 🟡 → 🟢 e depois por recência
- **Ações:** scroll; clique no card abre o painel direito (C) com o cliente; seleção múltipla (checkbox) → barra de lote (3B.4)
- **Estados:** loading (esqueleto) / vazio ("Nada pendente 🎉") / erro (recarregar)
- **Visibilidade:** sempre na aba Follow-up

### 3B.3 Card de follow-up
- **Elemento:** `FollowUpCard`
- **Propósito:** o dono entende o que está pendente, por quê, e resolve sem abrir mais nada
- **Conteúdo (informações):**
  - Nome do cliente (avatar) + coluna atual (ex.: "Orçamento")
  - Motivo legível (ex.: "Parado há 5 dias", "Orçamento sem resposta há 3 dias", "Recorrência atrasada", "Resposta aguardando aprovação")
  - Nível (semáforo) + tempo relativo ("há 2d")
  - Valor potencial (R$) — contexto de prioridade
  - Ação sugerida pelo agente (ex.: "Gerar follow-up de retomada", "Relembrar orçamento", "Aprovar resposta")
- **Opções por card:**
  - **Concluir** — pendência resolvida (registra no Histórico)
  - **Adiar** — snooze de 1/3/7 dias ou data escolhida (volta a aparecer depois)
  - **Ver no kanban** — troca para a aba Kanban e abre o card no painel direito
  - **Aprovar** — só quando a pendência é uma aprovação (resposta/artefato)
  - **Gerar rascunho** — dispara a ação sugerida pelo agente (ex.: gera follow-up como rascunho no painel)
  - **Dispensar** — não é pendência; some da lista **permanentemente** (decisão 12/08 — não volta sozinha; se voltar a ser pendência de novo, nasce de novo)
- **Ações:** clique → abre painel direito; checkbox (seleção múltipla)
- **Estados:** default / hover / selecionado / disabled (sem permissão — papéis fixos) / expirado (atrasado além do prazo — destaque)
- **Feedback:** toast ("Follow-up concluído", "Adiado para sexta-feira")
- **Visibilidade:** sempre que há pendência

### 3B.4 Barra de ações em lote (Follow-up)
- **Elemento:** `BarraAcoesLoteFollowUp`
- **Propósito:** resolver várias pendências de uma vez
- **Conteúdo (informações):** contador ("3 selecionados") + ações
- **Ações:** Concluir selecionados · Adiar selecionados (escolher snooze) · Aprovar selecionados · Limpar seleção (Esc)
- **Estados:** visível com 2+ selecionados; ações desabilitadas se o card não atende o critério
- **Feedback:** toast contando quantos foram afetados ("2 concluídos")
- **Visibilidade:** substitui o cabeçalho da lista enquanto há seleção

---

## 3C. Aba Histórico (auditoria da dimensão)

> Conceito: memória e auditoria — tudo que aconteceu nos clientes, em ordem cronológica. Eventos não são editáveis; o dono usa para saber o que foi feito, quando e por quem.

### 3C.1 Cabeçalho da visão
- **Elemento:** `CabecalhoVisaoHistorico`
- **Propósito:** navegar e restringir o histórico
- **Conteúdo (informações):** título "Histórico" + subtítulo com janela atual (ex.: "Últimos 30 dias · 214 eventos")
- **Opções (filtros):** Período (7d/30d/90d/tudo), Tipo de evento (todos/mensagem/movimento/artefato/aprovação/follow-up/rotina/cliente criado), Cliente (específico ou todos), Responsável (todos/dono/membro/agente)
- **Ações:** busca por texto livre (ex.: "orçamento", nome de cliente); filtros combináveis; "Limpar filtros" quando ativo; **Exportar** (CSV ou PDF — respeita os filtros ativos; decisão 12/08)
- **Estados:** filtro ativo (badge) / inativo
- **Feedback:** toast "Exportação gerada" + download
- **Visibilidade:** sempre na aba Histórico

### 3C.2 Timeline do histórico
- **Elemento:** `TimelineHistorico`
- **Propósito:** mostrar os eventos em ordem cronológica, agrupados por dia
- **Conteúdo (informações):**
  - Agrupamento por dia (Hoje / Ontem / "12 de agosto") com separador + contagem
  - Cada evento: ícone por tipo (💬 mensagem, ↔ movimento, 📎 artefato, ✓ aprovação, 🔔 follow-up, 🔁 rotina, ➕ cliente criado), texto legível ("Resposta enviada para Maria", "Card movido para Orçamento", "Orçamento #123 gerado", "Aprovado por Lucas", "Follow-up concluído", "Rotina 'Follow-up semanal' executada"), hora, cliente (avatar/nome), responsável, artefato linkado quando houver
- **Ações:** clique no evento → abre o contexto (card no kanban + painel, ou preview do artefato, ou detalhe da execução da rotina); "Carregar mais" no fim da lista
- **Estados:** loading (esqueleto) / vazio ("Sem histórico ainda") / erro (recarregar)
- **Visibilidade:** sempre na aba Histórico

### 3C.3 Item de evento
- **Elemento:** `ItemEventoHistorico`
- **Propósito:** uma linha legível de auditoria
- **Conteúdo (informações):** ícone do tipo + texto do evento + hora + responsável (avatar) + cliente (quando aplicável)
- **Ações:** clique abre o contexto; hover mostra detalhe estendido (metadados: quem, quando, o quê, onde)
- **Estados:** default / hover / com contexto indisponível (evento de item excluído — desabilitado com tooltip)
- **Visibilidade:** sempre que há eventos

---

## 3D. Aba Rotinas (automação da dimensão)

> Conceito: o que o agente faz automaticamente nos clientes. Reusa a Rotina API existente (catálogo built-in + rotina custom via builder chat + gatilhos manual/schedule/event/numeric/cron + "rodar agora" + feed de execução).

### 3D.1 Cabeçalho da visão
- **Elemento:** `CabecalhoVisaoRotinas`
- **Propósito:** resumir o estado das automações e criar novas
- **Conteúdo (informações):** título "Rotinas" + subtítulo ("3 ativas · 1 pausada") + botão "Nova rotina" (abre o builder)
- **Ações:** "Nova rotina" abre o `BuilderRotina` (3D.4)
- **Estados:** — | **Visibilidade:** sempre na aba Rotinas

### 3D.2 Catálogo de rotinas built-in
- **Elemento:** `CatalogoRotinas`
- **Propósito:** o dono adiciona automações prontas da dimensão sem configurar nada — **built-in** (decisão 12/08): as rotinas que todo negócio de clientes precisa já vêm no catálogo, embasadas nas funções existentes da Rotina API (reorganizar, não reconstruir)
- **Conteúdo (informações):** cards de sugestão com nome, o que faz, frequência sugerida e gatilho:
  - **"Reengajamento de clientes parados"** — lista clientes ativos sem compra/contato há X dias e envia mensagem de retomada (schedule, ex.: toda segunda 8h) · função existente: clientes sem compra por M dias
  - **"Análise de churn"** — segmenta clientes em ativos, em risco, inativos e novos (com NPS quando houver) e entrega resumo mensal (schedule mensal) · função existente: segmentação ativo/em risco/inativo + NPS
  - **"Revisão de orçamentos vencidos"** — lembrete/renegociação de orçamento sem resposta (schedule diário)
  - **"Saudação de novos contatos"** — primeiro contato automático quando cliente é criado (event: cliente criado)
  - **"Cobrança de inadimplentes"** — lista inadimplentes com compras passadas sem retorno e prepara follow-up (schedule) · função existente: clientes inadimplentes
- **Opções por card:** Adicionar (cria a rotina com padrão, ajustável depois) · Ver exemplo (mostra o que ela fará)
- **Estados:** já adicionada (marcada como ativa, sem botão Adicionar) / vazio (sem sugestões — raro)
- **Visibilidade:** sempre que houver sugestões não adicionadas; some quando todas ativas (fica só a lista)

### 3D.3 Lista de rotinas configuradas
- **Elemento:** `RotinaCard`
- **Propósito:** o dono acompanha e controla cada automação da dimensão
- **Conteúdo (informações):**
  - Nome da rotina + descrição curta
  - Gatilho/frequência legível ("Toda segunda às 8h", "Quando cliente fica 3 dias sem resposta", "Mensal, dia 1")
  - Responsável (agente IA)
  - Status: ativa (toggle) / pausada
  - Última execução: quando + resultado (ok / erro / parcial — ex.: "2 de 5 mensagens enviadas")
- **Opções:**
  - **Rodar agora** — dispara manualmente (registra no feed e no Histórico)
  - **Editar** — abre o `BuilderRotina` preenchido
  - **Pausar / Retomar** — interrompe/retoma a agenda (mantém configuração)
  - **Ver execuções** — filtra o feed para esta rotina
  - **Excluir** — com confirmação
- **Estados:** ativa / pausada / executando agora (spinner no botão) / erro na última execução (alerta visual)
- **Feedback:** toast ("Rotina executada", "Rotina pausada")
- **Visibilidade:** sempre que há rotinas configuradas

### 3D.4 Builder de rotina (chat)
- **Elemento:** `BuilderRotina`
- **Propósito:** criar/editar rotina em linguagem natural — o dono descreve, o agente devolve estruturado para confirmar
- **Conteúdo (informações):** chat com o agente (entrada "Descreva a rotina…") + proposta estruturada: gatilho (schedule/event/numeric/cron/manual) · ação (enviar mensagem, gerar relatório, mover cards, revisar) · filtro (quais clientes) · canal (WhatsApp/e-mail/interno)
- **Ações:** enviar descrição → agente propõe → o dono confirma ("Criar rotina") ou refina no chat; editar rotina existente reabre o builder preenchido
- **Estados:** digitando / gerando proposta (loading) / proposta pronta (resumo para confirmar) / erro (não entendeu — pede refinamento)
- **Feedback:** toast "Rotina criada" ao confirmar
- **Visibilidade:** overlay (Região E) aberto pelo "Nova rotina" ou "Editar"

### 3D.5 Feed de execuções
- **Elemento:** `FeedExecucoes` (reusa padrão existente)
- **Propósito:** o dono vê o que o agente já fez pelas rotinas
- **Conteúdo (informações):** execuções recentes (mais nova primeiro): rotina, quando, o que fez ("3 mensagens de follow-up enviadas", "2 cards movidos para Recorrência"), resultado (ok/erro/parcial)
- **Ações:** clique na execução → detalhe (lista do que foi feito) ou link para o Histórico; filtro "só desta rotina" (via 3D.3)
- **Estados:** vazio ("Nenhuma execução ainda") / loading
- **Visibilidade:** sempre na aba Rotinas (abaixo da lista)

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
- **Propósito:** ver e responder a troca de mensagens com o cliente, com o ciclo **notificada → respondida pelo agente → aprovada pelo dono → enviada**, em qualquer canal
- **Conteúdo (informações):** linha do tempo de mensagens — cliente (cinza) e agente (azul); cada mensagem com **canal** (WhatsApp · e-mail · direto — badge no bubble; decisão 12/08: WhatsApp, e-mail ou mensagem direta, extensível a outros canais); cada mensagem do agente com status: `Rascunho` → `Aguardando aprovação` → `Enviada`; notificação visual quando chega mensagem nova
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
- **Conteúdo (informações):** atalhos do cliente por canal: **Abrir WhatsApp · Enviar e-mail · Mensagem direta** · Agendar follow-up (calendário) · (outros canais conforme integração — decisão 12/08: arquitetura de canais extensível)
- **Ações:** cada atalho abre o canal externo / cria evento; "Mensagem direta" abre a conversa interna sem sair do painel
- **Estados:** disabled quando o canal não está configurado para o cliente (com explicação)
- **Visibilidade:** sempre

### 4.9 Interlocutores
- **Elemento:** `Interlocutores`
- **Conteúdo (informações):** quem está envolvido no card: responsável, agente IA, cliente (avatar + nome + papel)
- **Ações:** clique mostra contato; iniciar conversa interna
- **Visibilidade:** sempre

---

## 5. Região D — Quadrinhos (no plano)

> Decisão 11/08: os quadrinhos ficam no plano. As métricas da sala **moram aqui** (nunca numa strip horizontal no topo).

### 5.1 Q1 — Insights do agente
- **Elemento:** `InsightsSala`
- **Propósito:** sugestões proativas da IA sobre a dimensão — o dono vê o que merece atenção sem procurar
- **Conteúdo (informações):** 2–3 cards de sugestão (ex.: "Cliente X parado há 5 dias — gerar follow-up?", "Orçamento de Y sem resposta há 3 dias")
- **Opções por card:** Ver no kanban (abre o card no quadro) · Aplicar (gera follow-up/rascunho) · Dispensar
- **Estados:** vazio ("Sem insights agora") / loading
- **Visibilidade:** sempre

### 5.2 Q2 — Métricas da sala
- **Elemento:** `MetricasSala`
- **Propósito:** os indicadores da dimensão em um quadrinho compacto — no lugar da antiga strip do topo
- **Conteúdo (informações):** Pipeline (R$), Win rate, Ticket médio, NRR, Total de clientes, Segmentos
- **Opções:** período 30d / 90d / 1y; clique em uma métrica abre a fonte (lista filtrada/Estratégia)
- **Estados:** loading / sem dados ("Conecte seu CRM ou importe clientes")
- **Visibilidade:** sempre na aba Kanban

### 5.3 Q3 — Interlocutores
- **Elemento:** `InterlocutoresSala`
- **Propósito:** quem participa dos processos da dimensão — o dono sabe com quem falar
- **Conteúdo (informações):** pessoas envolvidas (dono, membros, agente IA) com avatar, nome e papel
- **Ações:** clique abre contato/conversa interna
- **Estados:** vazio ("Sem membros — convide em Admin")
- **Visibilidade:** sempre

---

## 6. Overlays (Região E)

### 6.1 Overlay "Novo cliente"
- **Elemento:** `OverlayFormulario`
- **Campos:** nome, contato (WhatsApp / e-mail / mensagem direta — ao menos um canal), segmento, valor potencial, responsável, coluna inicial (padrão Conversa)
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
| `CabecalhoVisaoFollowUp` | B (Follow-up) | cabeçalho + filtros da fila de pendências |
| `ListaFollowUp` | B (Follow-up) | pendências ordenadas por urgência |
| `FollowUpCard` | B (Follow-up) | pendência com motivo, nível e ação sugerida |
| `BarraAcoesLoteFollowUp` | B (Follow-up) | concluir/adiar/aprovar pendências em lote |
| `CabecalhoVisaoHistorico` | B (Histórico) | filtros + busca do histórico |
| `TimelineHistorico` | B (Histórico) | eventos cronológicos agrupados por dia |
| `ItemEventoHistorico` | B (Histórico) | linha de auditoria com ícone por tipo |
| `CabecalhoVisaoRotinas` | B (Rotinas) | resumo de automações + criar rotina |
| `CatalogoRotinas` | B (Rotinas) | sugestões prontas da dimensão |
| `RotinaCard` | B (Rotinas) | rotina configurada com gatilho, status e última execução |
| `BuilderRotina` | B/E (Rotinas) | criar/editar rotina por chat (linguagem natural) |
| `FeedExecucoes` | B (Rotinas) | execuções recentes com resultado |
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
| U10 | **Nunca há strip de métricas** no topo — métricas da sala ficam no quadrinho D |
| U11 | Contador da aba Follow-up = total de pendências ativas; concluir/adiar/dispensar atualiza o contador (e a Home) |
| U12 | Concluir follow-up e adiar (snooze) registram no Histórico; dispensar não registra conclusão |
| U13 | Pendência de aprovação (resposta/artefato) só mostra "Aprovar" para quem tem papel de aprovador |
| U14 | Histórico é imutável (auditoria): eventos não são editáveis nem removíveis pela UI |
| U15 | Todo evento relevante entra no Histórico: criação/edição de cliente, mensagem, movimento, aprovação, artefato, follow-up, execução de rotina |
| U16 | Rotinas reusam a Rotina API existente; gatilhos: manual / schedule / event / numeric / cron |
| U17 | "Rodar agora" dispara imediatamente e registra no feed de execuções + no Histórico |
| U18 | Erro/parcial na execução de rotina vira alerta visual no card e entra na Home |
| U19 | Canais de mensagem: WhatsApp, e-mail ou mensagem direta (decisão 12/08) — arquitetura extensível a outros canais; badge de canal em cada mensagem |
| U20 | Histórico tem exportação CSV/PDF respeitando os filtros ativos |
| U21 | "Dispensar" no Follow-up é permanente; a pendência só volta se nascer de novo |

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
- [ ] Follow-up: pendências ordenadas 🔴 primeiro; badge da aba bate com o contador
- [ ] Follow-up: Concluir card → some da lista + registra no Histórico + contador da aba e da Home atualizam
- [ ] Follow-up: Adiar (1/3/7 dias) → card some e volta na data; aparece de novo no feed no dia
- [ ] Follow-up: selecionar 3 cards → barra de lote → Concluir selecionados → toast "3 concluídos"
- [ ] Follow-up: pendência de aprovação mostra "Aprovar" só para aprovador
- [ ] Histórico: evento de mensagem/movimento/artefato/rotina aparece com ícone, hora e responsável
- [ ] Histórico: filtro por tipo + cliente + período combinados; busca por texto livre
- [ ] Histórico: clique em evento de artefato abre o preview; evento de card abre o painel
- [ ] Histórico: evento de item excluído → desabilitado com tooltip, sem quebrar a lista
- [ ] Rotinas: adicionar sugestão do catálogo → aparece na lista ativa
- [ ] Rotinas: "Rodar agora" → feed atualiza + Histórico registra + toast
- [ ] Rotinas: builder chat ("toda segunda, follow-up para parados há 5 dias") → proposta estruturada → confirmar → rotina criada
- [ ] Rotinas: pausar interrompe a agenda e mantém a configuração; retomar volta
- [ ] Rotinas: execução com erro/parcial → alerta no card + entra na Home
- [ ] Rotinas: sem rotinas configuradas → catálogo + CTA visíveis
- [ ] Canais: mensagem exibe badge do canal (WhatsApp/e-mail/direto); enviar direto não sai do painel
- [ ] Canais: cliente sem canal configurado → atalho disabled com explicação
- [ ] Histórico: Exportar CSV/PDF respeita filtros ativos → download + toast
- [ ] Follow-up: Dispensar é permanente — pendência não volta sozinha; só nasce de novo

---

## 10. Decisões

### Tomadas (11/08)
| # | Decisão |
|---|---|
| D1 | Painel direito **fixo** (~380px), não sobreposição |
| D2 | Região D (quadrinhos) **no plano** do design inicial |
| D3 | **Sem strip de métricas** no topo — métricas vivem no quadrinho D (e dentro das abas quando fizer sentido) |
| D4 | Ações em lote aprovadas: Mover / Gerar artefato / Aprovar pendências / Marcar lido / Arquivar / Excluir |

### Tomadas (12/08)
| # | Decisão |
|---|---|
| D5 | **Abas discretas mantidas como especificadas.** O comentário "sem faixa" era sobre a **faixa de analytics** (KPIs no topo) — já resolvido em D3/U10. Descrição visual das abas: mantém o que está (o desenho já está definido). |
| D6 | **Canais de mensagem:** WhatsApp, e-mail ou mensagem direta; arquitetura **extensível a outros canais** (U19) |
| D7 | Coluna **"Fechamento"** aprovada (era Artefatos) |
| D8 | **Pendências do Follow-up nascem automáticas** (parado, orçamento sem resposta, recorrência atrasada; aprovação quando há pendência real) |
| D9 | **"Dispensar" no Follow-up é permanente** (U21) |
| D10 | **Histórico com exportação** CSV/PDF respeitando filtros (U20) |
| D11 | **Catálogo de rotinas built-in** na aba Rotinas, embasado nas funções existentes da Rotina API (reengajamento, churn/NPS, orçamentos, saudação, inadimplentes) + **BuilderRotina** para criar rotina custom |

### Em aberto
1. **Seleção múltipla:** checkbox visível no hover vs. fixo no card? (proposta: hover + "selecionar tudo" no cabeçalho da coluna)
