# 🛒 Compras (Supply) — Tela de Requisitos de UI (Blue V3)

> Última atualização: 2026-08-12 | Status: 🟡 Proposta para validação (antes do design)
> Segue o padrão de [template-tela.md](./template-tela.md). Fluxo do kanban em [kanbans.md](./kanbans.md) §4.
> **Princípio:** elementos puros — informação + ação. Nenhum elemento é amarrado ao design atual da Blu; tudo nasce como novo conceito.
> **Direção (12/08):** sala própria de Compras com **controle de estoque/inventário incorporado** — vira uma dimensão de **supply holístico** (comprar para repor, estoque alimenta o kanban, recebimento atualiza o estoque). Funções de estoque/fornecedores já existem no backend (routines_api) — reorganizar, não reconstruir.

---

## 1. Layout macro da tela

```
┌──────────────────────────────────────────────────────────────────────────┐
│ A · Topo:  [Kanban] [Decisões] [Estoque] [Fornecedores]                  │
│            [Histórico] [Rotinas]                      …   [+ Nova compra]│
│            (abas discretas — sem faixa horizontal, sem strip)            │
├───────────────────────────────────────────────────────┬──────────────────┤
│ B · VISÃO DA ABA ATIVA                               │ C · PAINEL       │
│   [Kanban] 6 colunas:                                │   DIREITO        │
│   📥 Solicitação │ 💬 Cotação │ ⚖️ Aprovação │        │   (faixa         │
│   📦 Pedido │ 🚚 Recebimento │ 💳 Pago               │    vertical,     │
│                                                       │    FIXA ~380px)  │
│   [x] Card 1        [x] Card 2     [ ] Card 3         │                  │
│   ← barra de ações em lote →                          │                  │
│   [Decisões] pendências · [Estoque] SKUs ·            │                  │
│   [Fornecedores] ratings · [Histórico] por item ·     │                  │
│   [Rotinas] config + feed (seções 3B-3F)              │                  │
├───────────────────────────────────────────────────────┴──────────────────┤
│ D · QUADRINHOS:  [Insights supply] [Métricas da sala] [Interlocutores]   │
└──────────────────────────────────────────────────────────────────────────┘
```

Layout do design inicial: **Topo (abas discretas) + Visão da aba + Painel direito fixo + Quadrinhos (D)**. Não existe strip de métricas (U10 vale para todas as salas).

---

## 2. Região A — Topo

### 2.1 Navegação por abas (discretas, sem strip)
- **Elemento:** `NavegacaoAbas` (mesmo conceito de Clientes)
- **Propósito:** trocar entre as 6 visões da sala sem faixa horizontal — texto discreto com indicador (cor + peso + contador)
- **Abas (ordem):** Kanban (padrão) · Decisões · Estoque · Fornecedores · Histórico · Rotinas
- **Conteúdo (informações):** nome da aba + contador de pendência (ex.: Decisões "5", Estoque "2 críticos")
- **Ações:** clique troca a visão; persiste a última aba por sessão
- **Estados:** ativa (destaque de cor) / inativa / com pendência (contador)
- **Visibilidade:** sempre
- **Feedback:** transição suave da visão

### 2.2 Busca
- **Elemento:** `CampoBusca`
- **Propósito:** achar item de compra, SKU ou fornecedor rápido
- **Conteúdo (informações):** placeholder "Buscar item, SKU ou fornecedor..."; resultados em painel suspenso (nome, fornecedor, coluna atual)
- **Ações:** digitar filtra; Enter confirma e abre o primeiro resultado
- **Estados:** vazio / digitando (sugestões) / sem resultados ("Nenhum resultado") / loading
- **Visibilidade:** sempre no topo

### 2.3 Filtros
- **Elemento:** `Filtros`
- **Propósito:** restringir a visão por atributos da compra/estoque
- **Opções:** Fornecedor (todos/…), Status (todos/em cotação/aguardando aprovação/atrasado), Categoria (todos/matéria-prima/insumo/produto/serviço), Urgência (todos/ruptura/abaixo do mínimo/ok)
- **Ações:** múltiplos filtros combináveis; "Limpar filtros" quando ativo
- **Estados:** ativo (badge com contagem) / inativo
- **Visibilidade:** sempre

### 2.4 Botão "Nova compra"
- **Elemento:** `BotaoPrimario` (ícone +)
- **Propósito:** abrir uma solicitação de compra do zero
- **Ações:** abre overlay de criação (Região E)
- **Estados:** default / hover / disabled (sem permissão de criar — papéis fixos)
- **Visibilidade:** sempre

---

## 3. Região B — Aba Kanban (fluxo de compras)

> Colunas fixas (kanbans.md §4.2): 📥 Solicitação → 💬 Cotação → ⚖️ Aprovação → 📦 Pedido enviado → 🚚 Recebimento → 💳 Pago. **Pular etapas exige confirmação.**

### 3.1 Quadro
- **Elemento:** `QuadroKanban` (reusa de Clientes)
- **Conteúdo (informações):** 6 colunas com contador; cada card = uma unidade de compra (item único ou lista consolidada)
- **Ações:** scroll horizontal; arrastar cards; clicar card abre o painel direito; seleção múltipla (checkbox no hover + selecionar tudo na coluna — padrão D12)
- **Estados:** loading (esqueleto) / vazio (CTA "Nova compra") / erro (recarregar)
- **Feedback:** animação ao mover; toast em falha

### 3.2 Coluna
- **Elemento:** `ColunaKanban`
- **Conteúdo (informações):** nome da etapa, contador ("Cotação · 8"), cor da coluna
- **Opções (menu):** recolher/expandir, ordenar (valor/urgência/fornecedor)
- **Ações:** área de soltar; recolher (só cabeçalho)
- **Estados:** recolhida / vazia (dropzone) / cheia

### 3.3 Card de compra
- **Elemento:** `CartaoCompra`
- **Propósito:** resumo da compra em uma linha — o dono vê onde está e o que falta
- **Conteúdo (informações):**
  - Item(s) (nome + quantidade) ou lista consolidada ("Lista de reposição — 12 itens")
  - Badge de etapa interna (ex.: "Aguardando aprovação", "3 cotações recebidas", "Em transporte")
  - Semáforo 🟢/🟡/🔴 (atraso, fornecedor sem resposta, estoque crítico)
  - Valor (R$) + prazo ("entrega até 18/08" ou "há 2d")
  - Fornecedor (avatar/nome) + responsável
- **Opções (menu "..."):** Mover para…, Aprovar, Rejeitar, Gerar pedido, Duplicar, Cancelar (com confirmação)
- **Ações:** clique → abre painel direito; arrastar → mover; checkbox (seleção múltipla)
- **Estados:** default / hover / arrastando / selecionado / semáforo por cor / disabled
- **Visibilidade:** sempre que há compras

### 3.4 Barra de ações em lote
- **Elemento:** `BarraAcoesLote` (padrão de Clientes)
- **Ações:** Mover para… · Aprovar selecionadas · Rejeitar · Gerar pedido · Marcar recebido · Cancelar (confirmação dupla) · Limpar seleção (Esc)
- **Feedback:** toast contando afetados ("3 aprovadas")

### 3.5 Sub-estados por coluna (referência kanbans.md §4)
- **Solicitação:** `Criada → Validada → (entra na cotação)`
- **Cotação:** `Cotando → Aguardando resposta dos fornecedores → Cotações recebidas (comparativo)`
- **Aprovação:** `Aguardando aprovação → Aprovada / Rejeitada (motivo)`
- **Pedido enviado:** `Pedido emitido → Confirmado pelo fornecedor`
- **Recebimento:** `Em transporte → Recebido (conferência) → (atualiza estoque)`
- **Pago:** `Aguardando pagamento → Pago (integra Financeiro)`

---

## 3B. Aba Decisões (pendências de compra)

> Conceito (padrão Follow-up de Clientes, D8): pendências nascem automáticas — aprovações, cotações comparativas prontas, fornecedores sem resposta, itens em estoque crítico.

### 3B.1 Cabeçalho
- **Elemento:** `CabecalhoVisaoDecisoes`
- **Conteúdo (informações):** título "Decisões" + subtítulo ("5 itens precisam de ação") + valor em jogo (R$)
- **Opções (filtros):** Tipo (aprovação/cotação/atraso/estoque crítico), Urgência, Fornecedor
- **Ações:** ordenar (urgência/valor); "Limpar filtros"
- **Visibilidade:** sempre na aba Decisões

### 3B.2 Lista de decisões
- **Elemento:** `ListaDecisoes` (padrão `ListaFollowUp`)
- **Conteúdo:** cards de decisão ordenados 🔴 → 🟡 → 🟢
- **Estados:** loading / vazio ("Nada pendente 🎉") / erro

### 3B.3 Card de decisão
- **Elemento:** `DecisionCard` (adaptado — já existe)
- **Conteúdo (informações):**
  - Item/compra + fornecedor
  - Motivo legível ("Compra acima do limite — aprovar R$ 1.240", "3 cotações recebidas — escolher fornecedor", "Fornecedor sem resposta há 3 dias", "Estoque crítico: 2 SKUs abaixo do mínimo")
  - Semáforo + tempo relativo + valor
  - Ação sugerida pelo agente ("Aprovar", "Escolher melhor cotação", "Relembrar fornecedor", "Gerar solicitação de reposição")
- **Opções:** Aprovar · Rejeitar (motivo opcional) · Adiar (snooze 1/3/7d) · Ver no kanban · Gerar rascunho · Dispensar (permanente — padrão D9)
- **Ações:** clique abre o painel direito; checkbox (lote: aprovar/rejeitar/adiar selecionadas)
- **Estados:** default / hover / selecionado / disabled (papéis) / expirado

### 3B.4 Barra de ações em lote (Decisões)
- **Elemento:** `BarraAcoesLoteDecisoes`
- **Ações:** Aprovar selecionadas · Rejeitar · Adiar · Limpar seleção

---

## 3C. Aba Estoque / Inventário (nova — supply holístico)

> Conceito: o dono vê o que tem, o que está acabando e o que falta — e age (repor) sem trocar de sala. A aba liga estoque → compras: item abaixo do mínimo gera solicitação direto no kanban. Backend já expõe níveis de estoque, mínimo, ruptura e cobertura média.

### 3C.1 Cabeçalho do estoque
- **Elemento:** `CabecalhoVisaoEstoque`
- **Conteúdo (informações):** título "Estoque" + subtítulo ("128 SKUs · 3 abaixo do mínimo · 1 em ruptura") + valor total em estoque (R$)
- **Opções (filtros):** Categoria, Status (ok/abaixo do mínimo/ruptura), Fornecedor principal, Local (se houver múltiplos)
- **Ações:** ordenar (mais crítico/valor/cobertura); "Limpar filtros"; busca por SKU/nome
- **Estados:** filtro ativo (badge)
- **Visibilidade:** sempre na aba Estoque

### 3C.2 Lista de itens de estoque
- **Elemento:** `ListaEstoque`
- **Propósito:** inventário navegável — cada linha é um SKU/produto
- **Conteúdo (informações):** cards de item (3C.3) ordenados por status 🔴 ruptura → 🟡 abaixo do mínimo → 🟢 ok, depois por cobertura (dias)
- **Ações:** scroll; clique abre o detalhe do item (3C.4); seleção múltipla → lote (3C.5)
- **Estados:** loading (esqueleto) / vazio ("Sem itens — adicione ou importe seu inventário") / erro
- **Visibilidade:** sempre na aba Estoque

### 3C.3 Card de item de estoque
- **Elemento:** `CartaoEstoque`
- **Conteúdo (informações):**
  - Nome do item + SKU (código)
  - Quantidade atual + unidade (ex.: "12 un · min 20")
  - Status: 🟢 ok / 🟡 abaixo do mínimo / 🔴 ruptura (estoque zerado)
  - Cobertura média ("3 dias") + valor do item (R$)
  - Fornecedor principal (avatar/nome)
- **Opções (menu "..."):** Repor (abre overlay de solicitação), Ajustar estoque, Editar mínimo, Ver compras do item, Arquivar
- **Ações:** clique → detalhe do item; checkbox (lote)
- **Estados:** default / hover / selecionado / status por cor
- **Visibilidade:** sempre que há itens

### 3C.4 Detalhe do item (estoque)
- **Elemento:** `DetalheItemEstoque`
- **Propósito:** tudo do item num lugar — o dono decide repor com contexto
- **Conteúdo (informações):**
  - Identidade (nome, SKU, categoria, fornecedor, preço unitário)
  - Curva de consumo (últimos 30/90 dias — simples: entrada/saída e média diária)
  - Nível atual vs mínimo vs ponto de reposição sugerido
  - Compras recentes do item (histórico de pedidos + fornecedores usados)
- **Ações:** Repor (gera solicitação de compra pré-preenchida: item + quantidade sugerida), Editar mínimo, Exportar ficha do item
- **Estados:** loading / erro
- **Visibilidade:** painel interno da aba (proposta: substitui a lista, com voltar)

### 3C.5 Barra de ações em lote (estoque)
- **Elemento:** `BarraAcoesLoteEstoque`
- **Ações:** Repor selecionados (gera uma solicitação consolidada) · Ajustar estoque · Arquivar · Limpar seleção
- **Feedback:** toast ("3 itens enviados para Solicitação")

---

## 3D. Aba Fornecedores

> Conceito: quem abastece a operação — o dono avalia por performance (rating, lead time, atraso) e age (cotar, pedir) sem trocar de sala. Backend já expõe performance de fornecedores (lead time médio, taxa de atraso, alertas).

### 3D.1 Cabeçalho
- **Elemento:** `CabecalhoVisaoFornecedores`
- **Conteúdo (informações):** título "Fornecedores" + subtítulo ("12 ativos · 2 com alerta") + botão "Novo fornecedor"
- **Opções (filtros):** Status (ativo/pausado), Categoria, Rating mínimo, Com alerta
- **Ações:** busca por nome; ordenar (rating/lead time/total comprado)
- **Visibilidade:** sempre na aba Fornecedores

### 3D.2 Lista de fornecedores
- **Elemento:** `ListaFornecedores`
- **Conteúdo (informações):** cards de fornecedor (3D.3) ordenados por rating
- **Estados:** loading / vazio ("Nenhum fornecedor — adicione o primeiro") / erro

### 3D.3 Card de fornecedor
- **Elemento:** `CartaoFornecedor`
- **Conteúdo (informações):**
  - Nome (avatar) + categorias que atende
  - Rating ★ (1–5) + lead time médio ("3 dias") + taxa de atraso ("8%")
  - Total comprado (R$) no período + nº de pedidos
  - Contato (WhatsApp/e-mail — canais U19) + status (ativo/pausado)
  - Alerta (ex.: "2 pedidos atrasados") quando houver
- **Opções (menu "..."):** Nova cotação, Novo pedido, Ver compras, Editar, Pausar/Ativar
- **Ações:** clique → detalhe do fornecedor (pedidos, ratings por período, contatos)
- **Estados:** default / hover / com alerta / pausado
- **Visibilidade:** sempre que há fornecedores

---

## 3E. Aba Histórico (por compra — padrão D13)

> Conceito (mesmo da revisão de Clientes, D13/U22): o histórico é **por unidade** (compra/item), não timeline global de eventos. Cada linha é uma compra com card sumarizado; clicar abre o detalhe com artefatos (pedido, NF, contrato) e a linha do tempo só dela.

### 3E.1 Cabeçalho
- **Elemento:** `CabecalhoVisaoHistorico`
- **Conteúdo (informações):** título "Histórico" + subtítulo ("214 compras · 1.040 eventos")
- **Opções (filtros):** Período (7d/30d/90d/tudo), Tipo de atividade, Fornecedor, Responsável
- **Ações:** busca por texto (item, fornecedor, nº do pedido); **Exportar** CSV/PDF (com filtros — U20)
- **Visibilidade:** sempre na aba Histórico

### 3E.2 Lista de compras com histórico
- **Elemento:** `ListaHistoricoCompras`
- **Conteúdo (informações):** cards de compra (3E.3) ordenados por atividade mais recente
- **Estados:** loading / vazio ("Sem histórico ainda") / erro

### 3E.3 Card de compra no histórico
- **Elemento:** `CartaoHistoricoCompra`
- **Conteúdo (informações):** item(s) + fornecedor, resumo ("2 pedidos · 1 NF · pago"), últimas ações, contadores de artefatos (📄 pedido · NF · contrato), data da última atividade, valor
- **Ações:** clique → detalhe (3E.4); menu → Abrir no kanban, Exportar relatório da compra

### 3E.4 Detalhe do histórico da compra
- **Elemento:** `DetalheHistoricoCompra`
- **Conteúdo (informações):** identidade da compra, artefatos gerados (pedido de compra, nota fiscal, contrato — visualizar/baixar), linha do tempo só da compra (cotações, aprovação, envio, recebimento, pagamento)
- **Ações:** visualizar/baixar artefato; Abrir no kanban; Exportar relatório (PDF)

---

## 3F. Aba Rotinas (automação supply)

> Conceito (mesmo de Clientes): o que o agente faz automaticamente na dimensão. Reusa Rotina API + funções existentes (reposição, tendências de compras, performance de fornecedores). Padrão D11: catálogo built-in + builder custom.

### 3F.1 Cabeçalho
- **Elemento:** `CabecalhoVisaoRotinas`
- **Conteúdo (informações):** título "Rotinas" + subtítulo ("3 ativas · 1 pausada") + botão "Nova rotina" (builder)

### 3F.2 Catálogo de rotinas built-in (supply)
- **Elemento:** `CatalogoRotinas`
- **Conteúdo (informações):** sugestões prontas, embasadas nas funções existentes:
  - **"Reposição automática de estoque"** — detecta SKUs abaixo do mínimo (ou próximos de ruptura) e gera lista de compras (schedule, ex.: segunda 8h) · função existente: estoque abaixo do mínimo/ruptura
  - **"Cotação recorrente"** — dispara mensagens de cotação para fornecedores de itens recorrentes (schedule) · padrão kanbans.md §4.3
  - **"Revisão de fornecedores"** — resumo mensal de performance (lead time, atraso, rating) (schedule mensal) · função existente: performance de fornecedores
  - **"Análise de compras"** — resumo mensal de volume, ticket médio e variação (schedule mensal) · função existente: tendências de compras
  - **"Alertas de ruptura"** — avisa quando item chega ao ponto de reposição (event/numeric)
- **Opções por card:** Adicionar · Ver exemplo
- **Estados:** já adicionada (marca) / vazio

### 3F.3 Lista de rotinas configuradas
- **Elemento:** `RotinaCard`
- **Conteúdo (informações):** nome, descrição, gatilho legível ("Toda segunda 8h", "Quando SKU fica abaixo do mínimo"), status (ativa/pausada), última execução + resultado (ok/erro/parcial)
- **Opções:** Rodar agora · Editar (builder) · Pausar/Retomar · Ver execuções · Excluir (confirmação)

### 3F.4 Builder de rotina (chat)
- **Elemento:** `BuilderRotina`
- **Conteúdo (informações):** chat ("Descreva a rotina…") + proposta estruturada: gatilho (manual/schedule/event/numeric/cron) · ação (gerar lista, enviar cotação, atualizar estoque, revisar fornecedores) · filtro (quais itens/fornecedores) · canal (WhatsApp/e-mail/interno)
- **Ações:** enviar → agente propõe → confirmar ou refinar
- **Estados:** digitando / gerando proposta / proposta pronta / erro (pede refinamento)

### 3F.5 Feed de execuções
- **Elemento:** `FeedExecucoes`
- **Conteúdo (informações):** execuções recentes: rotina, quando, o que fez ("Lista de reposição gerada — 12 itens", "8 cotações enviadas"), resultado
- **Ações:** clique → detalhe / link para o Histórico
- **Estados:** vazio ("Nenhuma execução ainda")

---

## 4. Região C — Painel direito (faixa vertical, contextual)

> Painel lateral fixo (~380px), abre ao clicar num card. **Conceito:** o dono gerencia a compra do começo ao fim sem sair daqui. **Contextual (padrão Clientes 13/08 — D14):** o painel muda de modo conforme a aba ativa e o item selecionado — Kanban → Modo Compra (4.1–4.9) · Decisões → Modo Decisão (pendência em foco + aprovar) · Estoque → Modo ItemEstoque (detalhe 3C.4 no painel) · Fornecedores → Modo Fornecedor (perfil + rating + pedidos) · Histórico → Modo PerfilCompra (3E.4 no painel) · Rotinas → Modo Rotina (configuração) · qualquer aba → Modo Preview (documento/contrato/NF). Trilha/breadcrumb ao navegar para dentro do item.

### 4.1 Cabeçalho do painel
- **Elemento:** `CabecalhoPainel`
- **Conteúdo (informações):** item(s) + fornecedor + valor; menu "..." (editar, duplicar, cancelar)
- **Ações:** fechar (X); editar abre overlay

### 4.2 Comparativo de cotações
- **Elemento:** `ComparativoCotacoes`
- **Propósito:** decidir fornecedor com tudo na tela — preço, prazo, frete, rating
- **Conteúdo (informações):** tabela/cards das cotações recebidas: fornecedor, preço, prazo, frete, disponibilidade, rating; melhor escolha sugerida pelo agente (destaque)
- **Ações:** escolher (define o vencedor → move para Aprovação/Pedido); reabrir cotação
- **Estados:** sem cotações ("Nenhuma cotação ainda — disparar?") / loading / erro

### 4.3 Mensagens (canais)
- **Elemento:** `ConversaCompra`
- **Conteúdo (informações):** troca com fornecedores por canal (WhatsApp/e-mail/direto — badge de canal U19); mensagens do agente com status Rascunho → Aguardando aprovação → Enviada
- **Ações:** expandir, copiar, reenviar (se falhou), campo de resposta + "Gerar mensagem (IA)"

### 4.4 Aprovação inline
- **Elemento:** `AprovacaoInline`
- **Conteúdo (informações):** pendência resumida + botões
- **Opções:** Aprovar · Editar · Rejeitar (motivo opcional)
- **Visibilidade:** só quando existe pendência

### 4.5 Informações da compra
- **Elemento:** `InformacoesCompra`
- **Conteúdo (informações):** item(s), categoria, fornecedor, valor, prazo, solicitado por, aprovador, criado em
- **Ações:** Editar → overlay

### 4.6 Etapa atual + mover
- **Elemento:** `ControleEtapa`
- **Opções:** dropdown "Mover para…" com as 6 colunas (pular exige confirmação)
- **Feedback:** toast "Movido para Pedido enviado"

### 4.7 Artefatos da compra
- **Elemento:** `ArtefatosCompra`
- **Conteúdo (informações):** artefatos gerados (pedido de compra, nota fiscal, contrato, comprovante) com status (gerado/enviado/assinado) + botão "Gerar artefato"
- **Opções do menu "Gerar artefato":** Pedido de compra · Nota fiscal · Contrato · Comprovante de pagamento
- **Ações:** gerar (template — api/documents), visualizar, baixar PDF, enviar ao fornecedor, assinar

### 4.8 Integrações (atalhos)
- **Elemento:** `AtalhosIntegracao`
- **Conteúdo (informações):** atalhos: Abrir WhatsApp · Enviar e-mail · Mensagem direta · Agendar recebimento (calendário) · (outros canais — extensível)
- **Estados:** disabled quando canal não configurado

### 4.9 Interlocutores
- **Elemento:** `Interlocutores`
- **Conteúdo (informações):** quem está envolvido: responsável, aprovador, agente IA, fornecedor
- **Ações:** clique mostra contato; iniciar conversa interna

---

## 5. Região D — Quadrinhos (no plano)

### 5.1 Q1 — Insights supply
- **Elemento:** `InsightsSala`
- **Conteúdo (informações):** 2–3 sugestões proativas (ex.: "2 SKUs em ruptura — gerar reposição?", "Fornecedor X com 2 pedidos atrasados", "Cotação de Y sem resposta há 3 dias")
- **Opções:** Ver no kanban · Aplicar (gera ação) · Dispensar
- **Estados:** vazio ("Sem insights agora")

### 5.2 Q2 — Métricas da sala
- **Elemento:** `MetricasSala`
- **Conteúdo (informações):** Gastos no período (R$), Ticket médio, Lead time médio, Taxa de atraso, Estoque em valor (R$), Itens em ruptura
- **Opções:** período 30d / 90d / 1y; clique abre a fonte (aba correspondente)
- **Estados:** loading / sem dados ("Conecte seus fornecedores ou importe")

### 5.3 Q3 — Interlocutores
- **Elemento:** `InterlocutoresSala`
- **Conteúdo (informações):** pessoas envolvidas (dono, membros, agente IA)
- **Estados:** vazio ("Sem membros — convide em Admin")

---

## 6. Overlays (Região E)

### 6.1 Overlay "Nova compra" (solicitação)
- **Elemento:** `OverlayFormulario`
- **Campos:** item(s) (nome, quantidade, unidade, categoria), fornecedor (ou "cotar"), valor estimado, prazo, prioridade (normal/urgente), canal de envio
- **Ações:** Salvar (cria card na Solicitação + registra Histórico) · Cancelar
- **Validação:** item obrigatório; quantidade > 0
- **Feedback:** toast "Solicitação criada"; erro de duplicidade

### 6.2 Overlay "Repor estoque" (a partir do Estoque)
- **Elemento:** `OverlayReposicao`
- **Campos pré-preenchidos:** item(s) selecionados + quantidade sugerida (mínimo − atual + consumo), fornecedor principal
- **Ações:** Criar solicitação (gera card no kanban, coluna Solicitação) · Cancelar
- **Feedback:** toast "3 itens enviados para Solicitação"; link "Ver no kanban"

### 6.3 Overlay "Novo fornecedor"
- **Campos:** nome, contatos (WhatsApp/e-mail), categorias, rating inicial, notas
- **Feedback:** toast "Fornecedor criado"

### 6.4 Overlay "Visualizar artefato"
- **Conteúdo:** preview do documento + ações (Baixar, Enviar, Assinar)

### 6.5 Confirmações
- Cancelar compra / excluir → confirmação; Rejeitar → motivo opcional; Pular etapas → aviso.

---

## 7. Biblioteca de elementos (novo conceito — para o design system)

> Elementos puros, sem herança do design atual. Nome + propósito; o desenho vem depois. Elementos marcados (⬅️ Clientes) reusam o conceito já especificado na sala Clientes.

| Elemento | Região | Propósito |
|---|---|---|
| `NavegacaoAbas` ⬅️ | A | abas discretas sem faixa, com contador |
| `CampoBusca` ⬅️ | A | busca com sugestões |
| `Filtros` ⬅️ | A | restringir por atributos combináveis |
| `BotaoPrimario` ⬅️ | A | nova compra |
| `QuadroKanban` ⬅️ | B | colunas do fluxo, arrastar, seleção múltipla |
| `ColunaKanban` ⬅️ | B | etapa com contador, cor, dropzone |
| `CartaoCompra` | B | resumo da compra: itens, fornecedor, valor, semáforo |
| `BarraAcoesLote` ⬅️ | B | mover/aprovar/rejeitar/gerar pedido em massa |
| `Semafaro` ⬅️ | B/C | indicador 🟢🟡🔴 |
| `ListaDecisoes` ⬅️ (`ListaFollowUp`) | 3B | pendências ordenadas por urgência |
| `DecisionCard` (adaptado) | 3B | aprovação/cotação/atraso com ação sugerida |
| `CabecalhoVisaoEstoque` | 3C | filtros + resumo do inventário |
| `ListaEstoque` | 3C | SKUs ordenados por status/critério |
| `CartaoEstoque` | 3C | item com quantidade, mínimo, cobertura, status |
| `DetalheItemEstoque` | 3C | curva de consumo + nível vs mínimo + reposição |
| `BarraAcoesLoteEstoque` | 3C | repor/ajustar/arquivar em lote |
| `ListaFornecedores` | 3D | fornecedores com rating/lead time/atraso |
| `CartaoFornecedor` | 3D | performance + contato + alertas |
| `ListaHistoricoCompras` ⬅️ (`ListaHistoricoClientes`) | 3E | compras com histórico, um card por compra |
| `CartaoHistoricoCompra` ⬅️ | 3E | resumo do histórico + contadores de artefatos |
| `DetalheHistoricoCompra` ⬅️ | 3E | artefatos + timeline só da compra |
| `CatalogoRotinas` ⬅️ | 3F | sugestões built-in da dimensão |
| `RotinaCard` ⬅️ | 3F | rotina com gatilho, status, última execução |
| `BuilderRotina` ⬅️ | 3F | criar/editar rotina por chat |
| `FeedExecucoes` ⬅️ | 3F | execuções recentes com resultado |
| `CabecalhoPainel` ⬅️ | C | identidade do item + fechar/editar |
| `ComparativoCotacoes` | C | decidir fornecedor: preço/prazo/frete/rating |
| `ConversaCompra` ⬅️ (`ConversaCliente`) | C | troca com fornecedor por canal com status |
| `AprovacaoInline` ⬅️ | C | aprovar/editar/rejeitar no lugar |
| `InformacoesCompra` ⬅️ | C | dados da compra |
| `ControleEtapa` ⬅️ | C | mover entre colunas com confirmação |
| `ArtefatosCompra` ⬅️ (`ArtefatosCliente`) | C | gerar/listar pedido, NF, contrato, comprovante |
| `AtalhosIntegracao` ⬅️ | C | WhatsApp, e-mail, direto, calendário |
| `Interlocutores` ⬅️ | C | quem está envolvido |
| `InsightsSala` ⬅️ | D | sugestões proativas da IA |
| `MetricasSala` ⬅️ | D | indicadores da dimensão |
| `InterlocutoresSala` ⬅️ | D | quem participa dos processos |
| `OverlayFormulario` ⬅️ | E | criar/editar com validação |
| `OverlayReposicao` | E | repor estoque → solicitação pré-preenchida |
| ~~`OverlayArtefato`~~ ⬅️ | — | substituído por `PainelPreview` (padrão D15) |
| `PainelContextual` ⬅️ | C | contêiner do detalhe que troca de modo por aba/item (padrão D14) |
| `PainelPreview` ⬅️ | C | preview de documento/contrato/NF no painel |

> **Construir de verdade (núcleo novo):** `CartaoEstoque` + `ListaEstoque` + `DetalheItemEstoque` (inventário) e `ComparativoCotacoes` (decisão de fornecedor). O resto reusa os conceitos da sala Clientes (kanban, abas, painel, histórico, rotinas).

---

## 8. Regras de negócio de UI (resumo)

| # | Regra |
|---|---|
| U1 | Aba padrão = Kanban; última aba persiste por sessão |
| U2 | Colunas do kanban são fixas (etapas da dimensão) — não renomear/remover na UI |
| U3 | Pendência aparece com contador na aba Decisões e na Home |
| U4 | Todo movimento de card e todo artefato gerado registram no Histórico |
| U5 | Pular etapas exige confirmação |
| U6 | Papéis fixos: aprovador vê Aprovar; criador vê Gerar; visualizador só vê |
| U7 | Sem permissão de criar → "Nova compra" desabilitado |
| U8 | Ações em lote só aparecem com 2+ selecionados; excluir/cancelar em lote exige confirmação dupla |
| U10 | **Nunca há strip de métricas** no topo — métricas da sala ficam no quadrinho D |
| U12 | Concluir decisão e adiar (snooze) registram no Histórico; dispensar não registra |
| U14 | Histórico é imutável (auditoria): eventos não são editáveis nem removíveis pela UI |
| U15 | Todo evento relevante entra no histórico da compra: criação, cotação, aprovação, pedido, recebimento, pagamento, artefato, execução de rotina |
| U16 | Rotinas reusam a Rotina API existente; gatilhos: manual / schedule / event / numeric / cron |
| U17 | "Rodar agora" dispara imediatamente e registra no feed + no Histórico |
| U18 | Erro/parcial na execução de rotina vira alerta visual no card e entra na Home |
| U19 | Canais de mensagem: WhatsApp, e-mail ou mensagem direta — extensível a outros canais; badge de canal em cada mensagem |
| U20 | Histórico tem exportação CSV/PDF respeitando os filtros ativos |
| U21 | "Dispensar" é permanente; a pendência só volta se nascer de novo |
| U22 | Histórico é por unidade (compra/item) — não existe timeline global de eventos |
| C1 | Compra acima do limite (configurável, ex.: R$ 500) exige aprovação explícita |
| C2 | Aprovação de compra gera transação/despesa no Financeiro (integração) |
| C3 | Fornecedores têm rating; cotação nova considera rating + histórico |
| C4 | Cotação sem resposta do fornecedor em X dias → alerta na Home |
| C5 | Compras recorrentes podem virar rotina automática (ex.: reposição semanal) |
| C6 | Item abaixo do mínimo → semáforo amarelo e sugestão de reposição; em ruptura → vermelho e entra nas pendências |
| C7 | "Repor" no Estoque gera solicitação de compra pré-preenchida no kanban (coluna Solicitação) |
| C8 | Recebimento no kanban atualiza o estoque (quantidade + último custo) |
| C9 | Checkbox de seleção múltipla aparece só no hover (padrão D12) |

---

## 9. Cenários de teste (UI)

- [ ] Criar solicitação → card na Solicitação + toast + Histórico
- [ ] Rotina de cotação dispara → mensagens aos fornecedores → respostas entram no comparativo
- [ ] Escolher fornecedor no comparativo → card move para Aprovação com vencedor destacado
- [ ] Compra acima do limite → exige aprovação; sem papel de aprovador → botão some
- [ ] Aprovar → gera Pedido de compra (artefato) + integra Financeiro
- [ ] Recebimento → estoque atualiza (quantidade/lote) + card move para Pago
- [ ] Estoque: SKU abaixo do mínimo → amarelo + sugestão; ruptura → vermelho + pendência em Decisões
- [ ] Repor (1 item e em lote) → solicitação pré-preenchida no kanban
- [ ] Detalhe do item mostra curva de consumo e compras recentes
- [ ] Fornecedor com 2 pedidos atrasados → alerta no card + insight em Q1
- [ ] Histórico: lista por compra; detalhe com artefatos (pedido/NF) + timeline só da compra
- [ ] Rotinas: catálogo built-in → adicionar → ativa; "Rodar agora" → feed + Histórico
- [ ] Filtros combinados; exportação CSV/PDF com filtros
- [ ] Permissão visualizador → sem botões de ação

---

## 10. Decisões

### Propostas (validar)
| # | Decisão |
|---|---|
| S1 | **Sala própria "Compras"** com 6 abas: Kanban · Decisões · Estoque · Fornecedores · Histórico · Rotinas |
| S2 | **Estoque/Inventário incorporado** como aba (supply holístico) — item abaixo do mínimo gera reposição; recebimento atualiza estoque |
| S3 | Histórico por compra (padrão D13 de Clientes) |
| S4 | Catálogo de rotinas built-in supply (reposição, cotação recorrente, revisão de fornecedores, análise de compras, alertas de ruptura) |

### Em aberto
1. **Nome da sala:** "Compras" vs "Supply" vs "Compras & Estoque"? (afeta a sidebar)
2. **6 abas é o ideal?** (Clientes tem 4; aqui entram Estoque e Fornecedores como abas — alternativa: Fornecedores vira painel/quadrinho e sobra 5 abas)
3. **Estoque mínimo e ponto de reposição:** quem configura (overlay do item / Admin) e valores iniciais sugeridos?
4. **Origem da lista de compras:** rotina de reposição gera automaticamente (e o dono só aprova) ou gera como rascunho para o dono revisar antes? (kanbans.md §6.5)
5. **Limite de aprovação:** valor padrão (R$ 500?) e configurável onde?
6. **Estoque com múltiplos locais** (filiais/depósitos) já na Fase 1 ou depois?
7. **Painel contextual** (padrão Clientes 13/08 — D14/D15): validar os modos por aba (Compra/Decisão/ItemEstoque/Fornecedor/PerfilCompra/Rotina) e o preview de documento dentro do painel (substitui o overlay de artefato).
