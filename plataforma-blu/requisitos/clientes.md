# 👥 Clientes — Tela de Requisitos de UI (Blue V3)

> Última atualização: 2026-08-13 | Status: 🟡 Em andamento (painel direito contextual — ver §4; decisões em aberto no fim)
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
│   [Kanban] 5 colunas:                                │   CONTEXTUAL     │
│   💬 Conversa │ 🧾 Orçamento │ 📎 Fechamento │        │   (fixo ~380px)  │
│   ✅ Fechado  │ 🔁 Recorrência                        │   muda por ABA:  │
│                                                       │   Kanban→Cliente │
│   [x] Card 1        [x] Card 2     [ ] Card 3         │   Follow→Pendênc.│
│   ← barra de ações em lote →                          │   Histórico→Perf.│
│   [Follow-up] lista de pendências · [Histórico]       │   Rotinas→Rotina │
│   lista por cliente · [Rotinas] config + feed (3B-3D) │   Preview (doc)  │
├───────────────────────────────────────────────────────┴──────────────────┤
│ D · QUADRINHOS:  [Insights do agente] [Métricas da sala] [Interlocutores] │
└──────────────────────────────────────────────────────────────────────────┘
```

Layout do design inicial (decisões 11/08): **Topo (abas discretas) + Quadro + Painel direito fixo + Quadrinhos (D)**. **Não existe strip de métricas** — nenhuma faixa horizontal de KPIs acima das abas; as métricas da sala ficam no quadrinho D. **O painel direito é contextual** (refinamento 13/08): muda de modo conforme a aba ativa e o item selecionado — ver §4.

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
  - Checkbox no card **só no hover** (decisão D12 — não fixo no card)
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
- **Ações:** scroll; clique no card abre o painel direito em **Modo Pendência** (4.11); seleção múltipla (checkbox) → barra de lote (3B.4)
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

## 3C. Aba Histórico (memória por cliente)

> Conceito (revisado 12/08): o histórico é **por cliente**, não por evento. Cada linha da lista é um cliente, com um card sumarizado do que aconteceu com ele (e do que foi gerado para ele: contratos, notas, orçamentos). Clicar abre o histórico completo daquele cliente — incluindo acesso direto aos artefatos. **Não há timeline global** de eventos da sala; a linha do tempo existe dentro de cada cliente.

### 3C.1 Cabeçalho da visão
- **Elemento:** `CabecalhoVisaoHistorico`
- **Propósito:** navegar e restringir a lista de clientes
- **Conteúdo (informações):** título "Histórico" + subtítulo (ex.: "128 clientes · 214 eventos nos últimos 30 dias")
- **Opções (filtros):** Período (7d/30d/90d/tudo), Tipo de atividade (todos/mensagem/movimento/artefato/aprovação/follow-up/rotina), Responsável (todos/dono/membro/agente)
- **Ações:** busca por texto livre (nome de cliente, artefato, palavra-chave); filtros combináveis; "Limpar filtros" quando ativo; **Exportar** (CSV ou PDF — respeita os filtros ativos; decisão 12/08)
- **Estados:** filtro ativo (badge) / inativo
- **Feedback:** toast "Exportação gerada" + download
- **Visibilidade:** sempre na aba Histórico

### 3C.2 Lista de clientes com histórico
- **Elemento:** `ListaHistoricoClientes`
- **Propósito:** o dono navega o histórico pela pessoa — cada cliente é uma linha, com o que interessa dele à vista
- **Conteúdo (informações):** cards de cliente (3C.3) ordenados por atividade mais recente; contadores no subtítulo (clientes com atividade no período)
- **Ações:** scroll; clique no card abre o painel em **Modo Perfil** (4.13 — relatório do cliente); "Carregar mais" no fim da lista
- **Estados:** loading (esqueleto) / vazio ("Sem histórico ainda") / erro (recarregar)
- **Visibilidade:** sempre na aba Histórico

### 3C.3 Card de cliente no histórico
- **Elemento:** `CartaoHistoricoCliente`
- **Propósito:** resumo do histórico de UM cliente — o dono vê de longe o que já rolou com ele e o que foi gerado
- **Conteúdo (informações):**
  - Nome do cliente (avatar) + coluna atual
  - Resumo de atividades ("3 mensagens · 2 artefatos · orçamento aceito")
  - Últimas ações (2–3 linhas, ex.: "Orçamento #123 enviado — 12/08", "Contrato assinado", "Resposta enviada")
  - Contadores de artefatos por tipo (📎 contrato · NF · orçamento) com badge
  - Data da última atividade ("há 2d") + valor potencial (R$)
- **Ações:** clique → abre o painel em **Modo Perfil** (4.13, relatório do cliente); menu "..." → Abrir no kanban, Exportar relatório do cliente
- **Estados:** default / hover / selecionado
- **Visibilidade:** sempre que há clientes com histórico

### 3C.4 Detalhe do histórico do cliente (relatório do cliente)
- **Elemento:** `DetalheHistoricoCliente`
- **Propósito:** tudo do cliente num lugar só — o dono responde "qual contrato eu fiz, qual nota eu emiti para ele" sem sair da aba
- **Conteúdo (informações):**
  - Identidade do cliente (nome, contato, segmento, valor potencial, coluna atual)
  - **Artefatos gerados** — lista por tipo com status (contrato, nota fiscal, orçamento, pedido de envio, plano de trabalho): visualizar/baixar direto
  - **Linha do tempo do cliente** — eventos só dele, cronológicos (mensagens, movimentos, aprovações, follow-ups, execuções de rotina)
  - Resumo de métricas do cliente (nº de interações, ticket, recorrência)
- **Ações:** visualizar/baixar artefato; "Abrir no kanban" (leva ao card/painel); "Exportar relatório do cliente" (PDF); ver detalhe de um evento
- **Estados:** loading / vazio ("Nenhum evento ainda") / erro
- **Visibilidade:** **Modo Perfil** do painel direito (4.13) — decisão 13/08 (D16): o relatório do cliente vive no painel; fechar (X) ou voltar na trilha retorna à lista

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
- **Ações:** clique no card → abre o painel em **Modo Rotina** (4.14 — configuração)
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

## 4. Região C — Painel direito (faixa vertical, contextual)

> Painel lateral fixo (~380px). **Conceito (refinado 13/08):** o painel é a **lupa da sala** — mostra o detalhe do item selecionado e muda de **modo** conforme a aba ativa e o que foi clicado. Não é só o cliente do kanban: cada aba tem o seu modo, e o painel mantém uma **trilha** (breadcrumb) quando o dono navega para dentro de um item (ex.: cliente → artefato → preview).

```
┌──────────────────────────────────────┐
│ C · PAINEL CONTEXTUAL (fixo ~380px)  │
│   Trilha: Cliente › Artefato › Prev  │
├──────────────────────────────────────┤
│ Modo muda conforme ABA + seleção:    │
│  · Kanban      → Modo Cliente        │
│  · Follow-up   → Modo Pendência      │
│  · Histórico   → Modo Perfil         │
│  · Rotinas     → Modo Rotina         │
│  · (qualquer)  → Modo Preview (doc)  │
└──────────────────────────────────────┘
```

### 4.0 Contêiner e modos

- **Elemento:** `PainelContextual`
- **Propósito:** servir de detalhe para o item selecionado em qualquer aba — o dono entende e age sobre o que clicou sem trocar de visão
- **Modos:** Cliente (4.3–4.10) · Pendência (4.11–4.12) · Perfil (4.13) · Rotina (4.14–4.15) · Preview (4.16)
- **Regra de troca (U24):** clicar num item de outra aba **substitui o modo**; navegar para dentro do item (ex.: visualizar artefato) **empilha** na trilha
- **Estados:** aberto (item selecionado) / fechado (X ou Esc limpa a trilha) / loading / erro
- **Feedback:** transição suave entre modos; toast nas ações
- **Visibilidade:** sempre à direita; sem item selecionado mostra estado vazio "Selecione um item para ver o detalhe" (proposta — decisão em aberto 3)

### 4.1 Cabeçalho do painel

- **Elemento:** `CabecalhoPainel` (contextual)
- **Propósito:** identificar o que está aberto e dar as ações do modo
- **Conteúdo (informações):** ícone do modo + identidade do item (nome + semáforo + valor) + menu "..." com ações do modo
- **Opções (menu por modo):** Cliente — editar/duplicar/arquivar/excluir · Pendência — concluir/adiar/dispensar · Perfil — exportar relatório · Rotina — rodar agora/pausar/excluir · Preview — baixar/enviar/assinar
- **Ações:** fechar (X); **"Abrir no kanban"** (disponível em qualquer modo exceto Cliente — U25: troca para a aba Kanban e abre o Modo Cliente do item)
- **Visibilidade:** sempre que o painel está aberto

### 4.2 Trilha de navegação

- **Elemento:** `TrilhaNavegacao`
- **Propósito:** o dono sabe onde está dentro do item e volta um nível sem perder o contexto
- **Conteúdo (informações):** breadcrumb da pilha (ex.: "Maria › Orçamento #123 › Preview")
- **Ações:** clique em nível anterior desempilha (volta); X fecha o painel
- **Estados:** nível único (sem breadcrumb) / 2+ níveis (breadcrumb visível)
- **Visibilidade:** 2+ níveis de pilha

---

### Modo Cliente (aba Kanban — card de cliente)

> Abre ao clicar num `CartaoCliente` (ou "Abrir no kanban" vindo de outro modo). **Conceito:** o dono gerencia o cliente do começo ao fim sem sair daqui.

### 4.3 Conversa (mensagens com o cliente)

- **Elemento:** `ConversaCliente`
- **Propósito:** ver e responder a troca de mensagens com o cliente, com o ciclo **notificada → respondida pelo agente → aprovada pelo dono → enviada**, em qualquer canal
- **Conteúdo (informações):** linha do tempo de mensagens — cliente (cinza) e agente (azul); cada mensagem com **canal** (WhatsApp · e-mail · direto — badge no bubble; decisão 12/08: WhatsApp, e-mail ou mensagem direta, extensível a outros canais); cada mensagem do agente com status: `Rascunho` → `Aguardando aprovação` → `Enviada`; notificação visual quando chega mensagem nova
- **Ações:** expandir mensagem; copiar; reenviar (se falhou); ver detalhe do status
- **Estados:** mensagem pendente (contorno de atenção) / thread vazia ("Nenhuma mensagem ainda") / loading
- **Visibilidade:** sempre no painel

### 4.4 Campo de resposta

- **Elemento:** `CampoResposta`
- **Propósito:** o dono escreve direto ou pede rascunho ao agente
- **Conteúdo (informações):** caixa de texto + botão "Gerar resposta (IA)" + botão enviar
- **Opções:** Enviar direto (se tiver permissão) ou Gerar com IA → rascunho fica "Aguardando aprovação"
- **Ações:** Enter envia; Esc limpa; atalho para IA
- **Estados:** escrevendo / enviando (disabled) / vazio (placeholder)
- **Feedback:** toast de envio; aviso "rascunho gerado pela IA — revise antes de aprovar"

### 4.5 Aprovação inline

- **Elemento:** `AprovacaoInline`
- **Propósito:** aprovar/editar/rejeitar qualquer pendência (resposta ou artefato) sem trocar de tela
- **Conteúdo (informações):** pendência resumida + botões
- **Opções:** Aprovar · Editar · Rejeitar (pede motivo opcional)
- **Estados:** pendente / aprovado / rejeitado
- **Visibilidade:** só quando existe pendência (resposta ou artefato)

### 4.6 Informações do cliente

- **Elemento:** `InformacoesCliente`
- **Conteúdo (informações):** contato (WhatsApp, e-mail), segmento, valor potencial, origem do contato, criado em, responsável
- **Ações:** botão Editar → overlay de formulário
- **Estados:** campo sem valor (placeholder "—")
- **Visibilidade:** sempre

### 4.7 Etapa atual + mover

- **Elemento:** `ControleEtapa`
- **Conteúdo (informações):** coluna atual + aprovador da etapa
- **Opções:** dropdown "Mover para…" com as 5 colunas (pular etapa exige confirmação)
- **Ações:** mover atualiza o card e registra no Histórico
- **Feedback:** toast "Movido para Orçamento"

### 4.8 Artefatos (fechamento do cliente)

- **Elemento:** `ArtefatosCliente`
- **Propósito:** gerar e acompanhar os documentos do cliente **a partir do orçamento aprovado** — o dono escolhe o que o cliente precisa
- **Conteúdo (informações):** lista de artefatos gerados (tipo, status: gerado/enviado/assinado) + botão "Gerar artefato"
- **Opções do menu "Gerar artefato":**
  - **Orçamento** — cotação enviada ao cliente (estágio Orçamento)
  - **Plano de trabalho** — quando o orçamento aprovado é de **serviço** (escopo, etapas, prazos)
  - **Nota fiscal** — sempre que houver venda fechada
  - **Contrato** — quando houver acordo formal (assinatura)
  - **Pedido de envio** — quando o cliente **compra um produto** (envio/entrega)
- **Ações:** gerar (usa template de documento), visualizar (**empilha Modo Preview** — 4.16), baixar PDF, enviar ao cliente, assinar
- **Estados:** vazio ("Nenhum artefato") / gerando / erro de geração
- **Feedback:** toast sucesso/erro; artefato entra na lista e no Histórico
- **Visibilidade:** sempre no painel

### 4.9 Integrações (atalhos)

- **Elemento:** `AtalhosIntegracao`
- **Conteúdo (informações):** atalhos do cliente por canal: **Abrir WhatsApp · Enviar e-mail · Mensagem direta** · Agendar follow-up (calendário) · (outros canais conforme integração — decisão 12/08: arquitetura de canais extensível)
- **Ações:** cada atalho abre o canal externo / cria evento; "Mensagem direta" abre a conversa interna sem sair do painel
- **Estados:** disabled quando o canal não está configurado para o cliente (com explicação)
- **Visibilidade:** sempre

### 4.10 Interlocutores

- **Elemento:** `Interlocutores`
- **Conteúdo (informações):** quem está envolvido no card: responsável, agente IA, cliente (avatar + nome + papel)
- **Ações:** clique mostra contato; iniciar conversa interna
- **Visibilidade:** sempre

---

### Modo Pendência (aba Follow-up — card de follow-up)

> Abre ao clicar num `FollowUpCard`. **Conceito:** o dono resolve a pendência com contexto — vê o porquê, o valor em jogo e a ação sugerida, sem caçar o cliente no kanban.

### 4.11 Contexto da pendência

- **Elemento:** `PainelPendencia`
- **Propósito:** apresentar a pendência em foco com tudo que ela precisa para ser resolvida
- **Conteúdo (informações):** cliente (avatar + nome) + coluna atual; motivo legível ("Parado há 5 dias", "Orçamento sem resposta há 3 dias"); nível (semáforo); valor potencial em jogo (R$); outras pendências do mesmo cliente (se houver — navegação entre elas)
- **Ações:** **Ver conversa** — empilha o Modo Cliente do mesmo cliente (trilha: Pendência › Cliente) · **Ver no kanban** — troca para a aba Kanban e abre o Modo Cliente
- **Estados:** loading / erro
- **Visibilidade:** sempre no Modo Pendência

### 4.12 Ação sugerida + resolver

- **Elemento:** `AcaoSugeridaPendencia` (reusa padrão da 3B.3)
- **Conteúdo (informações):** ação sugerida pelo agente (ex.: "Gerar follow-up de retomada", "Relembrar orçamento", "Aprovar resposta") + botão "Gerar rascunho" (rascunho abre no Modo Cliente para revisão)
- **Ações:** **Concluir** · **Adiar** (1/3/7 dias ou data escolhida) · **Dispensar** (permanente — U21) · **Aprovar** (só aprovador, quando pendência de aprovação)
- **Estados:** concluído / adiado / expirado (atrasado além do prazo — destaque)
- **Feedback:** toast ("Follow-up concluído", "Adiado para sexta-feira"); concluir/adiar registram no Histórico e atualizam contadores (U28)
- **Visibilidade:** sempre no Modo Pendência

---

### Modo Perfil (aba Histórico — card de cliente)

> Abre ao clicar num `CartaoHistoricoCliente`. **Conceito (D16):** o relatório do cliente (3C.4) vive no painel — artefatos, timeline e exportação sem sair da lista.

### 4.13 Perfil do cliente (relatório)

- **Elemento:** `PainelPerfilCliente` (reusa `DetalheHistoricoCliente` 3C.4)
- **Propósito:** tudo do cliente num lugar só — o dono responde "qual contrato eu fiz, qual nota eu emiti para ele" sem sair da aba
- **Conteúdo (informações):** identidade (nome, contato, segmento, valor potencial, coluna atual) · **artefatos gerados** por tipo com status (contrato, NF, orçamento, pedido de envio, plano de trabalho) · **linha do tempo do cliente** (eventos só dele, cronológicos) · resumo de métricas do cliente
- **Ações:** visualizar artefato (**empilha Modo Preview** — 4.16) · baixar · **"Abrir no kanban"** (Modo Cliente) · **Exportar relatório do cliente** (PDF)
- **Estados:** loading / vazio ("Nenhum evento ainda") / erro
- **Visibilidade:** sempre no Modo Perfil

---

### Modo Rotina (aba Rotinas — rotina configurada)

> Abre ao clicar num `RotinaCard`. **Conceito (D17):** a configuração da rotina vive no painel — o dono ajusta gatilho/ação/filtro/canal sem abrir o builder; o chat continua para criar ou edição guiada.

### 4.14 Configuração da rotina

- **Elemento:** `PainelRotina`
- **Propósito:** ver e ajustar a configuração da rotina no lugar
- **Conteúdo (informações):** nome + descrição; **gatilho/frequência legível** ("Toda segunda às 8h", "Quando cliente fica 3 dias sem resposta"); **ação** (enviar mensagem, gerar relatório, mover cards, revisar); **filtro** (quais clientes); **canal** (WhatsApp/e-mail/interno); status (ativa/pausada)
- **Ações:** editar campos direto (frequência, filtro, canal — salva na hora) · **Editar com IA** — abre o `BuilderRotina` preenchido (chat) · **Rodar agora** · **Pausar/Retomar** · **Ver execuções** (filtra o feed 3D.5) · **Excluir** (confirmação)
- **Estados:** ativa / pausada / executando agora (spinner no botão) / erro na última execução (alerta visual)
- **Feedback:** toast ("Rotina atualizada", "Rotina executada", "Rotina pausada")
- **Visibilidade:** sempre no Modo Rotina

### 4.15 Última execução

- **Elemento:** `UltimaExecucaoRotina`
- **Conteúdo (informações):** quando + resultado (ok / erro / parcial — ex.: "2 de 5 mensagens enviadas") + o que foi feito
- **Ações:** clique → detalhe da execução / link para o Histórico
- **Estados:** nunca executou ("Ainda não executou — Rodar agora?") / erro (alerta visual)
- **Visibilidade:** sempre no Modo Rotina

---

### Modo Preview (documento / contrato)

> Abre ao clicar em "visualizar" num artefato (de qualquer modo). **Conceito (D15):** o preview de documento acontece **dentro do painel**, não em overlay — o dono confere o documento sem perder o contexto do item.

### 4.16 Preview do documento

- **Elemento:** `PainelPreview` (substitui o `OverlayArtefato` 6.3)
- **Propósito:** conferir o documento/contrato antes de enviar ou assinar
- **Conteúdo (informações):** renderização do documento (template + dados do cliente) + tipo/nome do artefato + status (gerado/enviado/assinado)
- **Ações:** **Baixar PDF** · **Enviar ao cliente** · **Assinar** · **Abrir documento completo** (nova aba/overlay grande, quando o preview em 380px não bastar) · **Voltar** (desempilha para o modo anterior)
- **Estados:** loading (gerando) / erro de geração / sem preview (tipo sem template)
- **Feedback:** toast de envio/assinatura; artefato atualiza status e entra no Histórico
- **Visibilidade:** sempre que um artefato é visualizado

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

### 6.3 ~~Overlay "Visualizar artefato"~~ — substituído (D15, 13/08)
- Preview de documento/contrato agora acontece **dentro do painel direito** (Modo Preview — 4.16). Não existe mais overlay de artefato; "Abrir documento completo" só quando o preview em 380px não bastar.

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
| `PainelContextual` | C | contêiner do detalhe que troca de modo por aba/item + trilha (U24) |
| `TrilhaNavegacao` | C | breadcrumb da pilha (voltar um nível) |
| `PainelPendencia` | C (Follow-up) | pendência em foco + ação sugerida + resolver |
| `AcaoSugeridaPendencia` | C (Follow-up) | ação do agente + Gerar rascunho |
| `PainelPerfilCliente` | C (Histórico) | relatório do cliente: artefatos + timeline + exportar (D16) |
| `PainelRotina` | C (Rotinas) | configuração da rotina + status + ações (D17) |
| `UltimaExecucaoRotina` | C (Rotinas) | resultado da última execução |
| `PainelPreview` | C | preview de documento/contrato no painel (substitui OverlayArtefato — D15) |
| `CabecalhoVisaoFollowUp` | B (Follow-up) | cabeçalho + filtros da fila de pendências |
| `ListaFollowUp` | B (Follow-up) | pendências ordenadas por urgência |
| `FollowUpCard` | B (Follow-up) | pendência com motivo, nível e ação sugerida |
| `BarraAcoesLoteFollowUp` | B (Follow-up) | concluir/adiar/aprovar pendências em lote |
| `CabecalhoVisaoHistorico` | B (Histórico) | filtros + busca da lista de clientes |
| `ListaHistoricoClientes` | B (Histórico) | clientes com histórico, um card por cliente |
| `CartaoHistoricoCliente` | B (Histórico) | resumo do histórico do cliente + contadores de artefatos |
| `DetalheHistoricoCliente` | B (Histórico) | relatório do cliente: artefatos + timeline dele |
| `CabecalhoVisaoRotinas` | B (Rotinas) | resumo de automações + criar rotina |
| `CatalogoRotinas` | B (Rotinas) | sugestões prontas da dimensão |
| `RotinaCard` | B (Rotinas) | rotina configurada com gatilho, status e última execução |
| `BuilderRotina` | B/E (Rotinas) | criar/editar rotina por chat (linguagem natural) |
| `FeedExecucoes` | B (Rotinas) | execuções recentes com resultado |
| `OverlayFormulario` | E | criar/editar com validação |
| ~~`OverlayArtefato`~~ | — | substituído por `PainelPreview` (D15) |

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
| U15 | Todo evento relevante entra no histórico do cliente: criação/edição, mensagem, movimento, aprovação, artefato, follow-up, execução de rotina |
| U16 | Rotinas reusam a Rotina API existente; gatilhos: manual / schedule / event / numeric / cron |
| U17 | "Rodar agora" dispara imediatamente e registra no feed de execuções + no Histórico |
| U18 | Erro/parcial na execução de rotina vira alerta visual no card e entra na Home |
| U19 | Canais de mensagem: WhatsApp, e-mail ou mensagem direta (decisão 12/08) — arquitetura extensível a outros canais; badge de canal em cada mensagem |
| U20 | Histórico tem exportação CSV/PDF respeitando os filtros ativos |
| U21 | "Dispensar" no Follow-up é permanente; a pendência só volta se nascer de novo |
| U22 | **Histórico é por cliente** (revisão 12/08): lista de clientes com card sumarizado; não existe timeline global de eventos — a linha do tempo vive dentro do detalhe de cada cliente |
| U23 | **Painel direito é contextual** (13/08): o conteúdo muda conforme a aba ativa e o item selecionado — Modo Cliente (Kanban) · Modo Pendência (Follow-up) · Modo Perfil (Histórico) · Modo Rotina (Rotinas) · Modo Preview (documento/contrato) |
| U24 | Clicar item de outra aba **substitui** o modo do painel; navegar para dentro do item (ex.: visualizar artefato) **empilha** na trilha; X/Esc fecha e limpa a trilha |
| U25 | **"Abrir no kanban"** existe em qualquer modo (exceto Cliente) e leva ao Modo Cliente do item |
| U26 | Preview de documento acontece **dentro do painel** (Modo Preview) — não existe mais overlay de artefato (D15); "Abrir documento completo" só quando o preview em 380px não bastar |
| U27 | Configuração de rotina vive no **Modo Rotina** do painel (edição direta de campos); `BuilderRotina` (chat) fica para criação e edição guiada |
| U28 | Concluir/adiar pendência no Modo Pendência registra no Histórico e atualiza os contadores (aba + Home) — mesmo efeito da 3B.3 |

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
- [ ] Histórico: lista é por cliente — cada card mostra resumo de atividades + contadores de artefatos
- [ ] Histórico: filtro por tipo + período + responsável combinados; busca por texto livre
- [ ] Histórico: clique no card abre o detalhe do cliente com artefatos (visualizar/baixar) + timeline só dele
- [ ] Histórico: cliente sem atividade no período não aparece na lista filtrada
- [ ] Histórico: exportar relatório do cliente (PDF) e exportar a lista (CSV/PDF com filtros)
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
- [ ] Painel contextual: clicar card no Kanban → Modo Cliente; trocar para Follow-up e clicar pendência → Modo Pendência **substitui**; X fecha e limpa a trilha
- [ ] Painel contextual: trilha Cliente › Artefato › Preview — "voltar" desempilha um nível; breadcrumb só aparece com 2+ níveis
- [ ] Painel: "Abrir no kanban" em qualquer modo (exceto Cliente) → aba Kanban + Modo Cliente do item
- [ ] Modo Pendência: Concluir → toast + some da lista + registra no Histórico + contadores atualizam; Aprovar só para aprovador; "Ver conversa" empilha Modo Cliente do mesmo cliente
- [ ] Modo Perfil: clique no cartão do histórico → relatório do cliente no painel (artefatos + timeline dele); visualizar artefato → Modo Preview; Exportar relatório do cliente (PDF)
- [ ] Modo Rotina: clique na rotina → configuração no painel; editar campo direto salva na hora; "Editar com IA" abre o builder preenchido; Rodar agora → feed + Histórico + toast
- [ ] Modo Preview: visualizar documento/contrato → preview no painel com Baixar/Enviar/Assinar; voltar → modo anterior; sem template → estado "sem preview"

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
| D12 | **Seleção múltipla: checkbox só no hover** (não fixo no card); "selecionar tudo" no cabeçalho da coluna |
| D13 | **Histórico por cliente** (revisão 12/08): lista de clientes com card sumarizado + detalhe por cliente (artefatos acessíveis + timeline só dele); sem timeline global (U22). **Aba Rotinas aprovada como está.** |

### Tomadas (13/08) — painel direito contextual
| # | Decisão |
|---|---|
| D14 | **Painel direito é contextual** — muda de modo conforme a aba ativa e o item selecionado: Modo Cliente (Kanban) · Modo Pendência (Follow-up) · Modo Perfil (Histórico) · Modo Rotina (Rotinas) · Modo Preview (documento/contrato). Cada aba tem o seu modo (direção do fundador 13/08: "cada aba vai mostrar uma coisa diferente no painel"). Trilha/breadcrumb quando o dono navega para dentro do item (U23/U24) |
| D15 | **Preview de documento/contrato acontece dentro do painel** (Modo Preview — 4.16), não em overlay. `OverlayArtefato` (6.3) deixa de existir; "Abrir documento completo" só quando o preview em 380px não bastar (U26) |
| D16 | **Detalhe do histórico vira Modo Perfil do painel** — o relatório do cliente (3C.4) abre no painel ao clicar no cartão da aba Histórico, com artefatos (visualizar → Modo Preview), timeline do cliente e exportação (4.13) |
| D17 | **Configuração de rotina vive no Modo Rotina do painel** — edição direta de gatilho/ação/filtro/canal; o `BuilderRotina` (chat) fica para criação e edição guiada (4.14–4.15, U27) |

### Em aberto (novas — 13/08)

1. **Modo Pendência:** painel dedicado de pendência (proposta) vs reutilizar o Modo Cliente com a pendência em destaque? A proposta (painel dedicado) resolve mais rápido sem trocar de contexto, mas cria um modo extra.
2. **Edição de rotina no painel:** campos diretos + "Editar com IA" (proposta) vs só o builder chat? Campos diretos são mais rápidos para ajustes pequenos (frequência/canal), mas duplicam a lógica do builder.
3. **Painel sem seleção:** estado vazio "Selecione um item" (proposta) vs painel recolhido em faixa fina? Vazio comunica que o painel existe; recolhido ganha espaço no centro.
4. **Trocar de aba com painel aberto:** manter o item (proposta — o mesmo cliente aparece em várias visões, o painel não pisca) vs fechar ao trocar de aba?
