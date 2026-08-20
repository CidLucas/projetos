# 📊 Financeiro — Tela de Requisitos de UI (Blue V3)

> Última atualização: 2026-08-12 | Status: 🟡 Em andamento (spec v1 para design — decisões D1–D6 tomadas; em aberto no fim)
> Segue o padrão de [template-tela.md](./template-tela.md). Proposta em [proposta-financeiro.md](./proposta-financeiro.md). Padrão do painel contextual em [clientes.md](./clientes.md).
> **Princípio:** elementos puros — informação + ação. Nenhum elemento é amarrado ao design atual da Blu; tudo nasce como novo conceito.
> **Fonte do comportamento atual:** `apps/blu_web/src/pages/app/FinanceiroRoom.tsx` — mas especificado como novo conceito, sem referência a componentes atuais.

---

## 1. Layout macro da tela

```
┌──────────────────────────────────────────────────────────────────────────┐
│ A · Topo:  [Decisões 3] [Processos 2] [Fluxo] [Contas] [Rotinas]         │
│            (abas discretas — sem faixa horizontal; sem strip de métricas)│
│            (sem strip de métricas — métricas vivem em D)                 │
├───────────────────────────────────────────────────────┬──────────────────┤
│ B · VISÃO DA ABA ATIVA                                │ C · PAINEL       │
│   Decisões → FilaDecisoes (semáforo + valor + ação    │   CONTEXTUAL     │
│              sugerida)                                │   (fixo ~380px)  │
│   Processos→ QuadroProcessos 4 colunas:               │   muda por ABA:  │
│              💾 Coleta │ ✅ Dados │ 📄 Relatório │     │   Decisões→Decis.│
│              🏁 Final                                 │   Processos→Proc.│
│   Fluxo    → Contas a pagar + Histórico               │   Fluxo→Fatura/  │
│   Contas   → ListaContas + saldo consolidado          │    Transação     │
│   Rotinas  → catálogo + configuradas + feed           │   Contas→Conta   │
│                                                       │   Rotinas→Rotina │
│                                                       │   (qualquer)→Prev│
├───────────────────────────────────────────────────────┴──────────────────┤
│ D · QUADRINHOS:  [Insights do agente] [Métricas + comparações] [Contas]  │
└──────────────────────────────────────────────────────────────────────────┘
```

Layout do design inicial (decisões 12/08): **Topo (abas discretas) + Quadro + Painel direito fixo + Quadrinhos (D)**. **Não existe strip de métricas** — nenhuma faixa horizontal de KPIs acima das abas; as métricas da sala ficam no quadrinho D com comparações (Q2/Q2b). **O painel direito é contextual** — muda de modo conforme a aba ativa e o item selecionado (ver §4). **Dois mundos na sala:** dinheiro (fila/fluxo — sem kanban) e processos (missões em etapas com kanban de aprovação).

---

## 2. Região A — Topo

### 2.1 Navegação por abas (discretas, sem strip)
- **Elemento:** `NavegacaoAbas` (novo conceito)
- **Propósito:** trocar entre as 5 visões da sala **sem faixa horizontal** — abas como texto discreto com indicador de estado (cor + peso + contador), sem fundo, sem borda, sem barra sublinhada
- **Abas (ordem):** Decisões (padrão) · Processos · Fluxo · Contas · Rotinas
- **Conteúdo (informações):** nome da aba + contador de pendência quando houver (ex.: Decisões "3" · Processos "2")
- **Opções:** nenhuma além da própria troca de aba (abas fixas da dimensão)
- **Ações:** clique troca a visão; persiste a última aba por sessão (U1)
- **Estados:** ativa (destaque de cor) / inativa / com pendência (contador)
- **Visibilidade:** sempre
- **Feedback:** transição suave da visão

### 2.2 Busca
- **Elemento:** `CampoBusca`
- **Propósito:** achar transação, conta, processo ou decisão por texto
- **Conteúdo (informações):** placeholder "Buscar no financeiro..."; resultados em painel suspenso agrupados por aba (Decisões / Processos / Transações / Contas)
- **Ações:** digitar filtra; Enter confirma e abre o primeiro resultado no painel contextual
- **Estados:** vazio / digitando (sugestões) / sem resultados ("Nada encontrado") / loading
- **Visibilidade:** sempre no topo

### 2.3 Filtros da visão ativa
- **Elemento:** `Filtros`
- **Propósito:** restringir a visão da aba ativa por atributos
- **Opções (por aba):**
  - Decisões: Nível (todos/urgente/alerta/oportunidade) · Tipo (pagamento/fatura/categorização/conciliação/alerta)
  - Processos: Etapa (todas/coleta/dados/relatório/final) · Tipo de processo (todos/fechamento/balanço/NF/fluxo) · Semáforo
  - Fluxo: Período (hoje/7d/30d/tudo) · Tipo (faturas/transações) · Conta · Categoria
  - Contas: Tipo (conta/cartão) · Status (sincronizado/erro/desconectado)
- **Ações:** múltiplos filtros combináveis; "Limpar filtros" aparece quando há filtro ativo
- **Estados:** ativo (badge com contagem de filtros) / inativo
- **Visibilidade:** sempre

### 2.4 Botão "Nova missão"
- **Elemento:** `BotaoPrimario` (ícone +)
- **Propósito:** criar um processo financeiro do zero (via chat com o agente)
- **Ações:** abre o overlay de criação de missão (Região E — 6.1); o processo nasce na etapa Coleta
- **Estados:** default / hover / disabled (sem permissão de criar — Admin por sala)
- **Visibilidade:** sempre

---

## 3. Região B — Visão da aba ativa

### 3.1 Aba Decisões

> Conceito: o coração da sala. Junta **tudo que precisa do dono agora** — pagamentos a aprovar, faturas que vencem, alertas do agente. O agente propõe; quem tem permissão decide.

### 3.1.1 Cabeçalho da visão
- **Elemento:** `CabecalhoVisaoDecisoes`
- **Propósito:** resumir e filtrar a fila de decisões
- **Conteúdo (informações):** título "Decisões" + subtítulo ("3 pendentes · R$ 4.820 em jogo")
- **Opções (filtros):** Nível (todos/urgente/alerta/oportunidade) · Tipo (pagamento/fatura/categorização/conciliação/alerta) · Conta
- **Ações:** filtros combináveis; "Limpar filtros" quando ativo; ordenar por (urgência/recência/valor)
- **Estados:** filtro ativo (badge) / inativo
- **Visibilidade:** sempre na aba Decisões

### 3.1.2 Fila de decisões
- **Elemento:** `FilaDecisoes`
- **Propósito:** o dono vê o que precisa dele **sem caçar** — ordenado por atenção (🔴 primeiro)
- **Conteúdo (informações):** lista de `CartaoDecisao` (3.1.3) ordenada por semáforo (🔴→🟡→🟢) e recência
- **Ações:** scroll; clique → painel Modo Decisão (4.3); seleção múltipla → barra de lote (3.1.4)
- **Estados:** loading (esqueleto) / vazio ("Nenhuma decisão pendente ✓") / erro (recarregar)
- **Visibilidade:** sempre na aba Decisões

### 3.1.3 Card de decisão
- **Elemento:** `CartaoDecisao`
- **Propósito:** a decisão em uma linha — o dono entende o quê, quanto e até quando sem abrir
- **Conteúdo (informações):**
  - Tipo com ícone (Pagar boleto 🧾 · Pagar fatura 💳 · Categorizar 🏷 · Conciliação 💚 · Alerta ⚠)
  - Título legível (ex.: "Fatura Nubank vence em 2 dias · R$ 1.240", "Boleto energia — vence amanhã")
  - Semáforo 🟢/🟡/🔴 (borda esquerda) + badge ("Urgente" / "Amanhã" / "Parado há 3d")
  - Valor (mono) + vencimento/recência ("há 2h", "vence amanhã")
  - Origem (banco/cartão) + ação sugerida do agente ("Pagar agora", "Relembrar", "Revisar gastos")
- **Opções (menu "..."):** Ver no fluxo (leva à transação/fatura) · Adiar · Dispensar · Excluir (com confirmação)
- **Ações:** clique → painel Modo Decisão; **ações rápidas no hover**: Agendar · Depois · Rejeitar; checkbox de seleção (hover); sem permissão de aprovar → botões desabilitados com dica
- **Estados:** default / hover / selecionado / urgente (destaque) / disabled (sem permissão)
- **Feedback:** toast (""Pagamento agendado"", ""Adiado — lembrete em 2 horas"", ""Rejeitado — Blu anotou"")
- **Visibilidade:** sempre que há decisões

### 3.1.4 Barra de ações em lote (Decisões)
- **Elemento:** `BarraAcoesLote` (mesmo padrão Clientes)
- **Conteúdo (informações):** contador ("3 selecionadas") + ações
- **Ações:** Agendar selecionadas · Adiar selecionadas (escolher snooze 1/3/7d ou data) · Rejeitar selecionadas (motivo opcional) · Limpar seleção (Esc)
- **Estados:** visível com 2+ selecionados; ações desabilitadas sem permissão
- **Feedback:** toast contando ("2 pagamentos agendados")
- **Visibilidade:** substitui o cabeçalho enquanto há seleção

---

### 3.2 Aba Processos (Missões — fluxo de processos financeiros)

> Conceito (direção do fundador 12/08): todo **processo financeiro vira uma missão com etapas** — Fechamento mensal (DRE), Balanço anual, Nota Fiscal, Relatório de fluxo de caixa (D5). A aba mostra em que etapa cada processo está e o que falta fazer. **Etapas base: Coleta → Aprovação dos dados → Aprovação do relatório → Relatório final** (D2); cada tipo de processo pode ajustar depois. **Quem move o card = quem tem autorização** (D3 — permissões por sala no Admin). O agente coleta/prepara; quem aprova destrava as portas; no fim sai o relatório final com comparações (D4).

### 3.2.1 Quadro de processos
- **Elemento:** `QuadroProcessos` (reusa o padrão `QuadroKanban` do novo conceito)
- **Propósito:** o dono vê o estágio de cada processo financeiro do começo ao fim e destrava as aprovações
- **Conteúdo (informações):** 4 colunas fixas: 💾 **Coleta de dados** → ✅ **Aprovação dos dados** → 📄 **Aprovação do relatório** → 🏁 **Relatório final**; cada coluna com contador
- **Ações:** scroll horizontal; arrastar cards (quem tem permissão); clicar card abre o painel; **seleção múltipla** (3.2.3)
- **Estados:** loading (esqueleto) / vazio (mensagem + CTA "Nova missão") / erro (recarregar)
- **Feedback:** animação ao mover; toast em falha
- **Visibilidade:** sempre na aba Processos

### 3.2.2 Card de processo
- **Elemento:** `CartaoProcesso`
- **Propósito:** resumo do processo em uma linha — o dono vê o que está em jogo e onde está travado
- **Conteúdo (informações):**
  - Nome da missão + período (ex.: "Fechamento mensal — Julho", "Balanço anual 2026", "NF — Junho")
  - Badge de sub-estado: "Aguardando aprovação" · "Dados incompletos" · "Em atraso" · "Aprovado" · "Entregue"
  - Semáforo 🟢 no prazo / 🟡 parado há X dias / 🔴 atrasado (borda esquerda)
  - Responsável (avatar) + aprovador da porta atual (avatar/role)
  - Valor/período quando aplicável (mono)
- **Opções (menu "..."):** Gerar relatório · Ver histórico · Aprovar etapa (quem tem permissão) · Arquivar · Excluir (confirmação)
- **Ações:** clique → painel Modo Processo; arrastar → mover entre etapas (porta de aprovação: mover para frente exige permissão de aprovar OU permissão de mover — configurado no Admin; **pular etapa exige confirmação** U5); checkbox de seleção
- **Estados:** default / hover / arrastando / selecionado / semáforo por cor / disabled (sem permissão)
- **Feedback:** toast (""Dados aprovados — relatório gerado"", ""Rejeitado — voltou para Coleta"")
- **Visibilidade:** sempre que há processos

### 3.2.3 Seleção múltipla + ações em lote (Processos)
- **Elemento:** `SelecaoMultipla` + `BarraAcoesLote` (mesmos padrões Clientes)
- **Ações:** checkbox no hover; Shift/Ctrl para intervalos; selecionar tudo na coluna; com 2+ → barra de lote: **Aprovar etapa dos selecionados** · **Mover para…** (escolher etapa) · **Arquivar** · **Limpar seleção** (Esc)
- **Estados:** ações desabilitadas se o usuário não tem permissão para a ação em algum selecionado
- **Feedback:** toast contando (""2 relatórios aprovados"")
- **Visibilidade:** comportamento do quadro; barra com 2+

### 3.2.4 Origem das missões
- **Elemento:** (comportamento)
- **Ações:** "+ Nova missão" (chat — 6.1) cria o processo na etapa Coleta; o agente **propõe processos** proativamente (ex.: "Fechamento do mês está na hora — criar?") — vira sugestão no Q1 (5.1) com ação "Criar processo"
- **Contador da aba Processos = portas de aprovação pendentes + processos parados (🟡/🔴)**

---

### 3.3 Aba Fluxo

> Conceito: o dinheiro que entra e sai — duas áreas na mesma visão: **Contas a pagar** (faturas/boletos por cartão com status) e **Histórico** (transações categorizadas).

### 3.3.1 Cabeçalho da visão
- **Elemento:** `CabecalhoVisaoFluxo`
- **Conteúdo (informações):** título "Fluxo" + subtítulo ("2 faturas abertas · 48 transações no período")
- **Opções (filtros/período):** pills discretas Hoje / 7 dias / 30 dias / Tudo (persiste por sessão) · Conta · Categoria · busca por texto
- **Ações:** filtros combináveis; "Limpar filtros" quando ativo
- **Estados:** filtro ativo (badge) / inativo
- **Visibilidade:** sempre na aba Fluxo

### 3.3.2 Contas a pagar (faturas)
- **Elemento:** `ListaFaturas` — `FaturaCard` por cartão/banco
- **Propósito:** o dono vê o que vence, o que está atrasado e quanto falta — sem abrir a fatura
- **Conteúdo (informações):**
  - Nome do cartão/banco (💳) + vencimento com semáforo ("vence hoje" / "3d atrasada" / "em 12d")
  - Valor total (mono) + mínimo quando aplicável ("mín. R$ 120")
  - Parcialmente pago: "✓ R$ 500 pago · restante R$ 740"
  - Ciclos anteriores em aberto: "⚠ +2 ciclos anteriores · R$ 1.900"
  - Conciliação: "💚 conciliada: R$ 1.240 em 12/08" (quando transação casa com a fatura — UF9)
  - Botão "Pagar agora" (cria aprovação → aba Decisões)
- **Opções (menu "..."):** Ver transações da fatura · Adiar · Dispensar
- **Ações:** clique → painel Modo Fatura; "Pagar agora" → cria decisão e mostra "✓ Enviado" (desabilita)
- **Estados:** loading / vazio ("Nenhuma fatura neste período") / sem contas (CTA "Conectar banco")
- **Visibilidade:** sempre na aba Fluxo; faturas **deduplicadas por ciclo** (só a mais recente de cada cartão na lista; ciclos anteriores somados no rodapé do card — UF7)

### 3.3.3 Histórico de transações
- **Elemento:** `ListaTransacoes` — `LinhaTransacao`
- **Propósito:** o dono vê o extrato e corrige a categoria quando o agente erra
- **Conteúdo (informações) por linha:**
  - Ícone (serviço 🎬🎵🍕🚗 / banco 🏛🟣 / categoria 🏥💳 / fallback ↑↓) + logo do merchant quando houver
  - Nome (merchant/pix/descrição) + categoria (chip)
  - Data (dd/mm) + valor (+/- mono; crédito verde; pendente cinza)
- **Ações:** clique na linha → painel Modo Transação; clique na categoria → seletor abre no lugar (mesma lista de categorias atual + sugestão do agente); busca/filtros do cabeçalho
- **Estados:** loading (esqueleto) / vazio ("Nenhuma transação neste período") / sem contas (CTA)
- **Visibilidade:** sempre na aba Fluxo (abaixo de Contas a pagar)

---

### 3.4 Aba Contas

> Conceito: as contas conectadas (Open Finance) — o dono vê o caixa e o crédito num lugar só e gerencia conexões.

### 3.4.1 Saldo consolidado
- **Elemento:** `SaldoConsolidado`
- **Propósito:** a resposta imediata para "quanto tenho"
- **Conteúdo (informações):** caixa consolidado (soma das contas tipo banco, mono, destaque) + crédito em uso (soma dos limites usados) quando houver
- **Estados:** sem contas → estado vazio com CTA "Conectar banco"
- **Visibilidade:** topo da aba Contas

### 3.4.2 Lista de contas
- **Elemento:** `ListaContas` — `ContaCard`
- **Conteúdo (informações):**
  - Tipo (🏦 conta / 💳 cartão) + nome + apelido/número
  - Saldo (mono; negativo vermelho) · status de sincronização (↑ sincronizado · ⚠ erro · desconectado)
  - Cartão: barra de uso do limite (R$ X de R$ Y usados; barra >80% vermelha)
- **Opções (menu "..."):** Atualizar · Renomear apelido · Desconectar (confirmação dupla)
- **Ações:** clique → painel Modo Conta; "Conectar banco" abre o fluxo de Open Finance (chat/overlay)
- **Estados:** loading / vazio ("Nenhuma conta conectada" + CTA) / erro de sync (alerta no card)
- **Visibilidade:** sempre na aba Contas

---

### 3.5 Aba Rotinas

> Conceito: o que o agente faz sozinho no financeiro — reusa a Rotina API (catálogo built-in + builder chat + gatilhos + feed).

### 3.5.1 Cabeçalho + catálogo + lista + feed
- **Elemento:** `CabecalhoVisaoRotinas` + `CatalogoRotinas` + `RotinaCard` + `FeedExecucoes` + `BuilderRotina` (mesmos padrões de Clientes — 3D.1–3D.5)
- **Propósito:** adicionar automações prontas do financeiro, acompanhar as configuradas e ver o que o agente fez
- **Catálogo built-in (proposta — validar funções no backend):**
  - **Cobrança de inadimplentes** — lista inadimplentes e prepara follow-up (schedule)
  - **Revisão de gastos** — análise mensal por categoria com comparações (schedule mensal)
  - **Conciliação automática** — cruza faturas × transações e marca 💚 (schedule diário) — ver decisão em aberto 3
  - **Resumo financeiro mensal** — relatório com comparações (schedule mensal)
  - **Alerta de saldo baixo / limite próximo** — notifica quando cruza a faixa (event/numeric)
  - **Disparo de processos** — ex.: "criar missão de fechamento mensal no dia 28" (schedule)
- **Conteúdo (informações) do RotinaCard:** nome, gatilho legível, status ativa/pausada, última execução + resultado
- **Ações:** Rodar agora · Pausar/Retomar · Editar com IA (builder) · Ver execuções · Excluir (confirmação)
- **Estados:** ativa / pausada / executando (spinner) / erro na última execução (alerta)
- **Visibilidade:** sempre na aba Rotinas

---

## 4. Região C — Painel direito (faixa vertical, contextual)

> Painel lateral fixo (~380px). **Conceito:** o painel é a **lupa da sala** — mostra o detalhe do item selecionado e muda de **modo** conforme a aba ativa e o que foi clicado. Cada aba tem o seu modo; navegar para dentro de um item **empilha** na trilha (breadcrumb).

```
┌──────────────────────────────────────┐
│ C · PAINEL CONTEXTUAL (fixo ~380px)  │
│   Trilha: Fechamento › Relatório ›   │
│           Preview                    │
├──────────────────────────────────────┤
│ Modo muda conforme ABA + seleção:    │
│  · Decisões   → Modo Decisão         │
│  · Processos  → Modo Processo        │
│  · Fluxo      → Modo Fatura / Trans. │
│  · Contas     → Modo Conta           │
│  · Rotinas    → Modo Rotina          │
│  · (qualquer) → Modo Preview (doc)   │
└──────────────────────────────────────┘
```

### 4.0 Contêiner e modos
- **Elemento:** `PainelContextual`
- **Modos:** Decisão (4.3) · Processo (4.4) · Fatura (4.5) · Transação (4.6) · Conta (4.7) · Rotina (4.8) · Preview (4.9)
- **Regra de troca (U24):** clicar num item de outra aba **substitui** o modo; navegar para dentro (ex.: ver relatório) **empilha** na trilha
- **Estados:** aberto (item selecionado) / fechado (X ou Esc limpa a trilha) / loading / erro
- **Visibilidade:** sempre à direita; sem item selecionado mostra "Selecione um item para ver o detalhe" (padrão Clientes — em aberto 6)

### 4.1 Cabeçalho do painel
- **Elemento:** `CabecalhoPainel` (contextual)
- **Conteúdo (informações):** ícone do modo + identidade do item (nome + semáforo + valor) + menu "..." com ações do modo
- **Opções (menu por modo):** Decisão — adiar/rejeitar · Processo — gerar relatório/arquivar · Fatura — pagar/adiar · Conta — atualizar/desconectar · Rotina — rodar/pausar/excluir · Preview — baixar/enviar
- **Ações:** fechar (X); **"Ver no fluxo"** (disponível em Decisão/Fatura/Transação — troca para a aba Fluxo e abre o item)
- **Visibilidade:** sempre que o painel está aberto

### 4.2 Trilha de navegação
- **Elemento:** `TrilhaNavegacao`
- **Conteúdo (informações):** breadcrumb da pilha (ex.: "Fechamento mensal › Relatório › Preview")
- **Ações:** clique em nível anterior desempilha; X fecha
- **Visibilidade:** 2+ níveis de pilha

---

### Modo Decisão (aba Decisões)

### 4.3 Decisão em foco
- **Elemento:** `PainelDecisao`
- **Propósito:** o dono resolve a decisão com contexto — o quê, quanto, até quando e por que o agente pediu
- **Conteúdo (informações):** tipo + título; **valor em destaque** (mono grande); vencimento/recência; origem (banco/cartão/fatura); o que o agente propôs e por quê (1–2 linhas); decisões relacionadas do mesmo processo/fatura se houver
- **Ações:** **Agendar/Aprovar** (só quem tem permissão de aprovar) · **Adiar** (1/3/7d ou data — snooze) · **Rejeitar** (motivo opcional) · "Ver no fluxo" (empilha a transação/fatura correspondente)
- **Estados:** pendente / aprovado (registra no Histórico) / rejeitado / disabled (sem permissão — com dica)
- **Feedback:** toast (""Pagamento agendado"", ""Rejeitado — Blu anotou"")
- **Visibilidade:** sempre no Modo Decisão

---

### Modo Processo (aba Processos)

### 4.4 Processo em foco
- **Elemento:** `PainelProcesso`
- **Propósito:** o dono vê o passo a passo do processo, quem aprova cada porta e os artefatos — e destrava as etapas sem sair do painel
- **Conteúdo (informações):**
  - Identidade: missão + período + semáforo + responsável
  - **Passo a passo das etapas** (Coleta → Dados → Relatório → Final): check nas concluídas, **porta de aprovação atual em destaque** (badge "Aguardando aprovação" + quem aprova)
  - Artefatos por etapa (dados brutos, relatório, versão final) — visualizar empilha Modo Preview
  - **Relatório final com comparações** (vs mês passado · vs mesmo mês do ano anterior · vs média do ano · vs 6 meses — D4/D6)
- **Ações:** **Aprovar etapa** (só quem tem permissão — aprovar dados / aprovar relatório) · **Rejeitar** (motivo opcional — volta uma etapa) · **Adiar** · **Gerar relatório** (dispara o agente; aparece como artefato na etapa) · ver histórico do processo
- **Estados:** etapa concluída / porta pendente (destaque) / rejeitado (volta) / atrasado (semáforo) / disabled
- **Feedback:** toast (""Relatório aprovado — processo finalizado"", ""Rejeitado — voltou para Coleta"")
- **Visibilidade:** sempre no Modo Processo

---

### Modo Fatura / Transação (aba Fluxo)

### 4.5 Fatura em foco
- **Elemento:** `PainelFatura`
- **Propósito:** o dono entende a fatura inteira — vencimento, pagamentos, parcelamento, conciliação — e paga sem sair
- **Conteúdo (informações):** cartão/banco; vencimento + semáforo; valor total + mínimo; pagamentos parciais (lista: quando, quanto); parcelável; **ciclos anteriores em aberto** (lista com valores); **conciliação** (quais transações casam — data/valor)
- **Ações:** **Pagar agora** (cria aprovação → aba Decisões) · ver transações da fatura (lista no painel ou empilha) · adiar
- **Estados:** vencida / vence hoje / em dia / paga (resolvida)
- **Feedback:** toast (""Aprovação criada — Fatura X aguarda confirmação"")
- **Visibilidade:** sempre no Modo Fatura

### 4.6 Transação em foco
- **Elemento:** `PainelTransacao`
- **Propósito:** o dono confere e corrige uma transação — categoria, conciliação — sem caçar no extrato
- **Conteúdo (informações):** nome/logo; data; valor; conta; categoria atual (trocar direto — seletor com sugestão do agente); status (pendente/confirmada); conciliação com fatura quando houver (💚 + link para a fatura)
- **Ações:** trocar categoria · "Ver no fluxo" (mostra a lista filtrada na conta/período) · ver fatura conciliada
- **Estados:** loading / erro
- **Visibilidade:** sempre no Modo Transação

---

### Modo Conta (aba Contas)

### 4.7 Conta em foco
- **Elemento:** `PainelConta`
- **Propósito:** o dono vê a conta inteira — saldo, limite, saúde do sync, extrato resumido — e gerencia
- **Conteúdo (informações):** tipo + nome + apelido; saldo (mono); cartão: limite, uso, barra; status de sync (última atualização); **extrato resumido** (últimas transações, clique empilha Modo Transação)
- **Ações:** Atualizar (força sync) · Renomear apelido · Desconectar (confirmação dupla)
- **Estados:** sincronizado / erro (alerta + "Tentar novamente") / desconectado
- **Visibilidade:** sempre no Modo Conta

---

### Modo Rotina (aba Rotinas)

### 4.8 Configuração da rotina
- **Elemento:** `PainelRotina` (mesmo padrão Clientes — D17/U27)
- **Conteúdo (informações):** nome + descrição; gatilho/frequência legível; ação; filtro; canal; status ativa/pausada; última execução + resultado
- **Ações:** editar campos direto (salva na hora) · **Editar com IA** (builder chat preenchido) · Rodar agora · Pausar/Retomar · Ver execuções · Excluir (confirmação)
- **Visibilidade:** sempre no Modo Rotina

---

### Modo Preview (documento / relatório)

### 4.9 Preview do documento/relatório
- **Elemento:** `PainelPreview` (mesmo padrão Clientes — D15/U26)
- **Propósito:** conferir boleto, fatura ou relatório antes de enviar/finalizar — dentro do painel, sem perder o contexto
- **Conteúdo (informações):** renderização do documento (template + dados) + tipo/nome + status (rascunho/gerado/enviado/aprovado)
- **Ações:** **Baixar PDF** · **Enviar** · **Aprovar/Finalizar** (se for porta de aprovação) · **Abrir documento completo** (quando o preview em 380px não bastar) · Voltar (desempilha)
- **Estados:** loading (gerando) / erro de geração / sem template
- **Visibilidade:** sempre que um documento é visualizado

---

## 5. Região D — Quadrinhos (no plano)

> Decisão 11/08: os quadrinhos ficam no plano. As métricas da sala **moram aqui** (nunca numa strip horizontal no topo).

### 5.1 Q1 — Insights do agente financeiro
- **Elemento:** `InsightsSala`
- **Propósito:** sugestões proativas da IA sobre o dinheiro do negócio
- **Conteúdo (informações):** 2–3 cards de sugestão (ex.: "Fatura Nubank vence em 2 dias — pagar agora?", "Gastos com restaurantes +30% vs mês passado", "Fechamento do mês está na hora — criar missão?", "3 boletos sem conciliação")
- **Opções por card:** Abrir decisão · Criar processo · Ver no fluxo · Dispensar
- **Estados:** vazio ("Sem insights agora") / loading
- **Visibilidade:** sempre

### 5.2 Q2 — Métricas da sala (com comparações)
- **Elemento:** `MetricasSala`
- **Propósito:** os indicadores da dimensão em um quadrinho compacto — no lugar da antiga strip do topo
- **Conteúdo (informações):** período 30d/90d/1y; métricas: Faturamento · Despesas · Margem · Fluxo 30d · Caixa consolidado · Burn rate · Runway · DSO · DPO · CCC (as disponíveis no indicadores/context — em aberto 4)
- **Comparações (Q2b/D6):** cada métrica mostra **só as pills que fazem sentido**: vs mês passado (MoM) · vs mesmo mês do ano anterior (YoY) · vs média do ano anterior · vs média dos últimos 6 meses (ex.: DSO/DPO/CCC sem "média do ano")
- **Ações:** clique numa métrica → Estratégia ou lista filtrada; pills de comparação trocam o contexto exibido
- **Estados:** loading / sem dados ("Conecte suas contas ou importe")
- **Visibilidade:** sempre

### 5.3 Q2c — Mapa de contexto do negócio
- **Elemento:** `MapaContexto` (comportamento/vinculação)
- **Propósito:** as comparações alimentam o contexto do agente (`contextMetrics`, dimensão finance) — as métricas não vivem isoladas na sala; o mesmo mapa vira pauta em Estratégia e base das sugestões do Q1
- **Visibilidade:** transversal (não é um quadrinho visual separado — é a regra que alimenta Q1/Q2/Estratégia)

### 5.4 Q3 — Contas rápido
- **Elemento:** `ContasRapido`
- **Propósito:** ver o saldo das contas sem trocar de aba
- **Conteúdo (informações):** contas conectadas com saldo (mono) + atalho para a aba Contas; sem contas → CTA "Conectar banco"
- **Visibilidade:** sempre

---

## 6. Overlays (Região E)

### 6.1 Overlay "Nova missão" (chat)
- **Elemento:** `OverlayBuilderMissao`
- **Campos:** chat com o agente ("Descreva a missão…" — ex.: "fechamento mensal de julho") → proposta estruturada: tipo de processo (Fechamento mensal · Balanço anual · Nota Fiscal · Relatório de fluxo de caixa · outro) · período · etapas (padrão 4, ajustável) · responsável · prazo
- **Ações:** Confirmar (cria o processo na etapa Coleta) · Refinar no chat · Cancelar
- **Feedback:** toast "Missão criada — Fechamento mensal entrou na etapa Coleta"

### 6.2 Overlay "Conectar banco" (Open Finance)
- **Ações:** fluxo de conexão via chat/agente (Polp) — selecionar banco, autorizar; conta entra na aba Contas
- **Feedback:** toast de sucesso/erro; erro → estado "erro de sync" no ContaCard

### 6.3 Overlay "Rejeitar" (motivo)
- **Ações:** motivo opcional + confirmar; rejeitar decisão registra no Histórico; rejeitar etapa do processo **volta o card uma etapa**

### 6.4 Confirmações
- Desconectar conta / excluir processo / excluir rotina → confirmação (desconectar e excluir em lote: confirmação dupla)

---

## 7. Biblioteca de elementos (novo conceito — para o design system)

> Elementos puros, sem herança do design atual. Nome + região + propósito; o desenho vem depois.

| Elemento | Região | Propósito |
|---|---|---|
| `NavegacaoAbas` | A | abas discretas sem faixa horizontal, com contador |
| `CampoBusca` | A | busca no financeiro com resultados agrupados |
| `Filtros` | A | restringir a visão ativa por atributos combináveis |
| `BotaoPrimario` | A | criar missão/processo |
| `CabecalhoVisaoDecisoes` | B (Decisões) | título + subtítulo + filtros da fila |
| `FilaDecisoes` | B (Decisões) | fila de decisões ordenada por semáforo |
| `CartaoDecisao` | B (Decisões) | decisão: tipo, semáforo, valor, ação sugerida |
| `BarraAcoesLote` | B | agendar/adiar/rejeitar em massa |
| `QuadroProcessos` | B (Processos) | kanban 4 etapas dos processos financeiros |
| `ColunaEtapa` | B (Processos) | etapa com contador, cor, dropzone |
| `CartaoProcesso` | B (Processos) | missão: etapa, badge, semáforo, responsável, aprovador |
| `CabecalhoVisaoFluxo` | B (Fluxo) | período + filtros do fluxo |
| `ListaFaturas` / `FaturaCard` | B (Fluxo) | contas a pagar: vencimento, mínimo, parcial, conciliação |
| `ListaTransacoes` / `LinhaTransacao` | B (Fluxo) | extrato: ícone, nome, categoria, valor |
| `SaldoConsolidado` | B (Contas) | caixa + crédito em uso |
| `ListaContas` / `ContaCard` | B (Contas) | contas conectadas: saldo, limite, sync |
| `CabecalhoVisaoRotinas` | B (Rotinas) | resumo de automações + nova rotina |
| `CatalogoRotinas` | B (Rotinas) | sugestões prontas do financeiro |
| `RotinaCard` | B (Rotinas) | rotina configurada com gatilho, status, última execução |
| `BuilderRotina` | B/E | criar/editar rotina por chat |
| `FeedExecucoes` | B (Rotinas) | execuções recentes com resultado |
| `PainelContextual` | C | contêiner do detalhe que troca de modo por aba + trilha |
| `TrilhaNavegacao` | C | breadcrumb da pilha |
| `PainelDecisao` | C (Decisões) | decisão em foco + aprovar/adiar/rejeitar |
| `PainelProcesso` | C (Processos) | passo a passo das etapas + portas + artefatos + comparações |
| `PainelFatura` | C (Fluxo) | fatura: pagamentos, parcelas, ciclos, conciliação |
| `PainelTransacao` | C (Fluxo) | transação: categoria, status, conciliação |
| `PainelConta` | C (Contas) | conta: saldo, limite, sync, extrato resumido |
| `PainelRotina` | C (Rotinas) | configuração da rotina + status + ações |
| `PainelPreview` | C | preview de boleto/fatura/relatório no painel |
| `InsightsSala` | D | sugestões proativas do agente |
| `MetricasSala` | D | métricas com comparações (MoM/YoY/média ano/6m) |
| `ContasRapido` | D | contas com saldo + atalho |
| `OverlayBuilderMissao` | E | criar missão/processo por chat |
| `OverlayConectarBanco` | E | conexão Open Finance |
| `OverlayMotivo` | E | motivo de rejeição |

---

## 8. Regras de negócio de UI (resumo)

| # | Regra |
|---|---|
| U1 | Aba padrão = Decisões; última aba persiste por sessão |
| U2 | Colunas do QuadroProcessos são as 4 etapas base (D2) — renomear/remover só por configuração do tipo de processo |
| U3 | Pendência aparece com contador na aba Decisões/Processos e na Home |
| U4 | Toda ação relevante (aprovar, rejeitar, mover, pagar, criar processo, executar rotina) registra no Histórico |
| U5 | Pular etapa do processo exige confirmação |
| U6 | Papéis: sem permissão de aprovar/mover → botões desabilitados com dica (permissões por sala no Admin — D3) |
| U7 | Sem permissão de criar → "Nova missão" desabilitado |
| U8 | Ações em lote só com 2+ selecionados; excluir em lote exige confirmação dupla |
| U9 | **Nunca há strip de métricas** no topo — métricas ficam no quadrinho D (Q2) |
| U10 | Contador aba Decisões = decisões ativas; aba Processos = portas pendentes + parados |
| U11 | Rejeitar etapa do processo volta o card uma etapa (com motivo registrado) |
| U12 | "Pagar agora" cria uma aprovação — a decisão cai na aba Decisões (UF8) |
| U13 | Faturas na lista são deduplicadas por ciclo (só a mais recente por cartão; anteriores somadas no card) (UF7) |
| U14 | Conciliação automática marca 💚 quando transação casa com fatura (mesmo cartão, ±7d do vencimento, valor ≈ total ou mínimo) (UF9) |
| U15 | Rotinas reusam a Rotina API existente; gatilhos manual/schedule/event/numeric/cron (U16 de Clientes) |
| U16 | "Rodar agora" dispara imediatamente e registra no feed + Histórico |
| U17 | Erro/parcial na execução de rotina vira alerta visual no card e entra na Home |
| U18 | "Dispensar" em decisão/insight é permanente; só volta se nascer de novo |
| U19 | **Painel direito é contextual**: Decisão (Decisões) · Processo (Processos) · Fatura/Transação (Fluxo) · Conta (Contas) · Rotina (Rotinas) · Preview (qualquer) |
| U20 | Clicar item de outra aba substitui o modo; navegar para dentro empilha na trilha; X/Esc limpa |
| U21 | Preview de documento/relatório acontece dentro do painel (Modo Preview) |
| U22 | Configuração de rotina vive no Modo Rotina (edição direta); builder fica para criação/edição guiada |
| U23 | **Comparações por métrica** — cada métrica declara quais pills se aplicam (D6: DSO/DPO/CCC sem "média do ano") |
| U24 | **Comparações alimentam o contexto do agente** (`contextMetrics`, dimensão finance) — mapa de contexto do negócio (D4) |
| U25 | **Relatório final do processo inclui as comparações** (D4) |
| U26 | Sem dados fabricados: nenhum gráfico/valor com dados fixos inventados (gráfico fake do Financeiro atual é removido) |
| U27 | Etapas base 4 (D2); tipos de processo podem ajustar etapas depois (decisão em aberto 2) |

---

## 9. Cenários de teste (UI)

### Decisões
- [ ] Fila ordena 🔴 → 🟡 → 🟢; badge da aba bate com o total
- [ ] Aprovar decisão → toast + some da fila + contador aba/Home atualizam
- [ ] Adiar (1/3/7d ou data) → some e volta no snooze
- [ ] Rejeitar → motivo opcional → registra no Histórico
- [ ] Selecionar 3 → barra de lote → Agendar selecionadas → "2 pagamentos agendados"
- [ ] Sem permissão de aprovar → botões disabled com dica
- [ ] Nenhuma decisão → estado vazio "Nenhuma decisão pendente ✓"

### Processos
- [ ] Nova missão via chat → processo nasce na etapa Coleta + toast
- [ ] Card move Coleta → Aprovação dos dados (com permissão) → badge "Aguardando aprovação"
- [ ] Aprovar dados → agente gera relatório → card vai para "Aprovação do relatório"
- [ ] Aprovar relatório → processo termina na "Relatório final" + relatório com comparações
- [ ] Rejeitar → motivo → card volta uma etapa
- [ ] Pular etapa (Coleta → Relatório) → confirmação exigida
- [ ] Sem permissão de mover/aprovar → drag desabilitado + botões disabled
- [ ] Selecionar coluna inteira → Aprovar etapa em lote → toast com contagem
- [ ] Processo atrasado → semáforo 🔴 + entra na Home
- [ ] Nenhum processo → estado vazio com CTA "Nova missão"
- [ ] Agente propõe processo no Q1 → "Criar processo" cria na Coleta

### Fluxo
- [ ] Faturas deduplicadas por cartão; ciclos anteriores somados no rodapé do card
- [ ] "Pagar agora" → cria decisão na aba Decisões + botão vira "✓ Enviado"
- [ ] Fatura parcialmente paga → "✓ X pago · restante Y"
- [ ] Transação casa com fatura → 💚 conciliada (data/valor)
- [ ] Categorizar na linha → seletor abre no lugar → salva e reusa em transações iguais
- [ ] Filtros período (Hoje/7d/30d/Tudo) + conta + categoria combinados
- [ ] Sem contas conectadas → CTA "Conectar banco"

### Contas
- [ ] Saldo consolidado = soma das contas banco; cartão mostra uso do limite com barra
- [ ] Sync com erro → ⚠ erro + "Tentar novamente"; desconectar exige confirmação dupla
- [ ] Nenhuma conta → estado vazio + CTA

### Rotinas
- [ ] Adicionar do catálogo → entra na lista ativa; "Rodar agora" → feed + Histórico + toast
- [ ] Pausar mantém config; retomar volta
- [ ] Erro/parcial na execução → alerta no card + Home
- [ ] Builder chat → proposta estruturada → confirmar → rotina criada

### Painel contextual
- [ ] Aba Decisões → clique → Modo Decisão; trocar para Processos e clicar processo → Modo Processo **substitui**
- [ ] Trilha: Fechamento › Relatório › Preview — voltar desempilha; breadcrumb só com 2+
- [ ] Modo Preview: visualizar relatório no painel com Baixar/Enviar; sem template → estado "sem preview"
- [ ] "Ver no fluxo" em Decisão/Fatura/Transação → aba Fluxo + item aberto

### Quadrinhos
- [ ] Q2 mostra período 30d/90d/1y; cada métrica só com as comparações que fazem sentido (DSO sem "média do ano")
- [ ] Comparação ↑/↓ com cor (verde/vermelho); clique na métrica → Estratégia/lista filtrada
- [ ] Q1 insight "Criar processo" → cria missão na Coleta
- [ ] Q3 contas com saldo; sem contas → CTA
- [ ] Nenhum valor fabricado — gráfico fake não existe (U26)

---

## 10. Decisões

### Tomadas (12/08)

| # | Decisão |
|---|---|
| D1 | Aba **Processos (Missões)** entra na sala — processos financeiros em etapas com portas de aprovação; não são só fiscais (inclui relatórios gerenciais) |
| D2 | **Etapas base:** Coleta de dados → Aprovação dos dados → Aprovação do relatório → Relatório final; ajustes por tipo de processo depois |
| D3 | **Quem move o card = quem tem autorização** — permissões por sala configuradas no Admin (owner): quem aprova, quem move, quem conecta conta, quem cria missão |
| D4 | **Comparações em métricas e relatórios** — vs mês passado (MoM) · vs mesmo mês do ano anterior (YoY) · vs média do ano anterior · vs média dos últimos 6 meses; alimentam o mapa de contexto do negócio (context metrics) |
| D5 | **Primeiros processos (v1):** Fechamento mensal (DRE) · Balanço anual · Nota Fiscal · Relatório de fluxo de caixa |
| D6 | **Comparações só quando fazem sentido por métrica** (ex.: DSO/DPO/CCC sem "média do ano") |

### Em aberto

1. **Abas:** Decisões · Processos · Fluxo · Contas · Rotinas (proposta) vs outra combinação? (Config some — proposta)
2. **Etapas custom por processo:** quem define a etapa extra quando surgir exceção — agente propõe e dono aprova, ou dono configura?
3. **Conciliação automática** como rotina built-in — entra no catálogo? (validar função no backend)
4. **Quadrinho Q2 — quais métricas** de cara? (proposta: Faturamento · Despesas · Margem · Fluxo 30d · Caixa consolidado · Burn rate · Runway · DSO · DPO · CCC)
5. **"Nova Missão":** manter no topo como entrada do chat (proposta) vs esconder atrás das ações diretas?
6. **Painel sem seleção:** estado vazio "Selecione um item" (padrão Clientes) vs recolhido?
7. **Próximas salas:** depois de Financeiro → Compras (spec parcial) — confirmar ordem e o que é a "Saúde" citada (sala nova ou outro projeto?)
