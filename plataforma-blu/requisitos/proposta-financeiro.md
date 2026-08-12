# 💰 Proposta — Sala Financeiro (Novo Front Blu)

> Última atualização: 2026-08-12 | Status: 🟡 Proposta validada nas decisões-chave (v4 — D5 processos v1 + D6 comparações por métrica); spec completa em [financeiro.md](./financeiro.md)
> Base: wireframe do novo front (`/blu-site/` — sala Clientes) + Financeiro atual (`apps/blu_web/src/pages/app/FinanceiroRoom.tsx`, 934 linhas)
> Padrão: elementos puros · abas discretas · painel contextual · quadrinhos — mesmo conceito de [clientes.md](./clientes.md)

---

## 1. Visão

A sala Financeiro deixa de ser uma **mesa de ferramentas** (4 abas + painel lateral de contas + strip de KPIs + gráfico) e vira a **dimensão financeira do negócio**: o dono responde em segundos *"quanto tenho, quanto devo, o que está em andamento e o que precisa de mim agora"*.

O agente financeiro continua no centro — analisa transações, categoriza, concilia, propõe decisões — mas a sala se organiza em torno do que o **dono precisa decidir, ver e aprovar**, em três frentes: **decisões** (o que precisa de mim agora), **processos** (missões em etapas que alguém precisa destravar) e **dinheiro** (contas, fluxo e métricas).

**Relação com outras salas:** Home (urgências financeiras), Estratégia (métricas aprofundadas), Admin (conexão Open Finance de primeira vez).

---

## 2. Princípios aplicados (do novo conceito)

| # | Princípio |
|---|---|
| P1 | **Abas discretas, sem faixa horizontal** — nada de strip de métricas no topo; contador de pendência na aba |
| P2 | **Painel direito contextual (~380px)** — cada aba tem seu modo; navegar para dentro de um item empilha trilha (breadcrumb) |
| P3 | **Quadrinhos no rodapé (D)** — insights do agente + métricas da sala; métricas nunca no topo |
| P4 | **Elementos puros** — novos nomes de biblioteca, informação + ação, sem referência ao design atual |
| P5 | **Semáforo 🟢🟡🔴** em tudo que tem prazo: vencimento, limite de crédito, saldo baixo, processo parado, aprovação pendente |
| P6 | **Números em mono**, contraste AA, 4 temas (dark / azul / mono / warm) |
| P7 | **Papéis e permissões por sala, configuráveis no Admin** — no Financeiro o dono é aprovador por padrão; o owner configura quem tem permissão em cada sala (quem aprova, quem move card, quem conecta conta). Só quem tem permissão age |
| P8 | **Dois mundos no Financeiro:** dinheiro (fila/fluxo, sem kanban) **e processos** (missões em etapas, com kanban de aprovação) |

---

## 3. Layout macro

```
┌──────────────────────────────────────────────────────────────────────────┐
│ A · Topo:  [Decisões 3] [Processos 2] [Fluxo] [Contas] [Rotinas] …       │
│            [+ Nova missão]   (abas discretas — sem faixa horizontal)     │
├───────────────────────────────────────────────────────┬──────────────────┤
│ B · VISÃO DA ABA ATIVA                                │ C · PAINEL       │
│   Decisões → fila de aprovações (semáforo + valor)    │   CONTEXTUAL     │
│   Processos→ kanban de missões (etapas + portas de    │   (fixo ~380px)  │
│              aprovação)                               │   muda por ABA:  │
│   Fluxo    → contas a pagar + histórico de transações │   Decisões→Decis.│
│   Contas   → contas conectadas + saldo consolidado    │   Processos→Proc.│
│   Rotinas  → catálogo + configuradas + feed           │   Fluxo→Fatura/  │
│                                                       │    Transação     │
│                                                       │   Contas→Conta   │
│                                                       │   Rotinas→Rotina │
│                                                       │   (qualquer)→Prev│
├───────────────────────────────────────────────────────┴──────────────────┤
│ D · QUADRINHOS:  [Insights do agente] [Métricas da sala] [Contas rápido]  │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Abas da sala

### 4.1 Decisões — padrão (contador de pendências)

**Conceito:** o coração da sala. Junta **tudo que precisa do dono agora** — pagamentos a aprovar, faturas que vencem, alertas do agente (gasto anormal, limite próximo do teto, saldo baixo, boleto sem conciliação). O agente propõe; o dono decide.

- **Elemento:** `FilaDecisoes` — lista vertical de `CartaoDecisao`, ordenada por urgência (semáforo 🔴 → 🟡 → 🟢, depois recência)
- **CartaoDecisao (informações):** tipo de decisão (Pagar boleto · Pagar fatura · Categorizar · Conciliação · Alerta), título legível (ex.: "Fatura Nubank vence em 2 dias · R$ 1.240"), semáforo, valor (mono), vencimento/recência ("vence amanhã", "há 3d"), origem (banco/cartão), ação sugerida do agente ("Pagar agora", "Relembrar", "Revisar gastos")
- **Ações no card:** clique → abre painel Modo Decisão · ações rápidas no hover (Agendar · Depois · Rejeitar) · seleção múltipla (checkbox no hover) → barra de lote (Agendar selecionados · Adiar selecionados)
- **Estados:** vazio ("Nenhuma decisão pendente ✓") · loading · erro
- **Contador da aba = total de decisões ativas** — resolver atualiza a aba e a Home (mesmo padrão U11 de Clientes)

### 4.2 Processos (Missões) — fluxo de processos financeiros

**Conceito (nova direção do fundador):** todo **processo financeiro do negócio vira uma missão com etapas** — **não é só fiscal**: emissão de Nota Fiscal, Balanço anual, Fechamento mensal (DRE), Declaração de impostos, relatório de fluxo de caixa, relatórios gerenciais (custo-benefício, desempenho). A aba mostra **em que etapa cada processo está e o que falta fazer** — o fluxo do processo, não só o resultado. O agente coleta e prepara; quem tem permissão **destrava as portas de aprovação**; no fim sai o **relatório final**.

- **Elemento:** `QuadroProcessos` (kanban — reusa o `QuadroKanban` do novo conceito)
- **Etapas padrão (4 colunas — proposta):**
  1. **Coleta de dados** — os dados do processo entram (integrações, upload, agente importa)
  2. **Aprovação dos dados** — aprovador valida o que entrou (rejeitar volta para a coleta com motivo)
  3. **Aprovação do relatório** — aprovador valida o relatório gerado pelo agente
  4. **Relatório final** — fechado/entregue; documento final disponível
- **CartaoProcesso (informações):** nome da missão (ex.: "Nota Fiscal — Junho", "Balanço anual 2026"), etapa atual (coluna), badge de sub-estado ("Aguardando aprovação" · "Dados incompletos" · "Em atraso" · "Aprovado"), semáforo de prazo, responsável (avatar), período/valor quando aplicável
- **Ações:** clique → painel Modo Processo · **mover entre etapas — quem tem permissão de mover (configurada no Admin por sala); pular porta exige confirmação (U5)** · **Aprovar etapa** (aprovar dados / aprovar relatório — só quem tem permissão de aprovar) · **Rejeitar** (motivo opcional, volta uma etapa) · menu "..." (gerar relatório, ver histórico, arquivar)
- **Seleção múltipla** (checkbox no hover) → barra de lote (Aprovar etapa dos selecionados · Mover para… · Arquivar)
- **Origem das missões:** botão "+ Nova missão" (chat com o agente) cria o processo e ele já nasce na etapa Coleta; o agente também propõe processos (ex.: "Fechamento do mês está na hora — criar?")
- **Contador da aba = processos com porta de aprovação pendente ou parados (semáforo 🟡/🔴)**
- **Estados:** vazio ("Nenhum processo — crie uma missão") · loading · erro
- **Etapas:** as **4 etapas são a base** — cada tipo de processo pode ajustar depois (ex.: Nota Fiscal pode ganhar "Validação fiscal" antes do relatório) — ver decisão 2

### 4.3 Fluxo

**Conceito:** o dinheiro que entra e sai, em duas áreas na mesma visão: **Contas a pagar** (faturas/boletos por cartão com status) e **Histórico** (transações categorizadas).

- **Contas a pagar —** `FaturaCard` por cartão/banco: nome do cartão, vencimento ("vence hoje", "3d atrasada" — semáforo), valor total + mínimo, parcialmente pago (✓ pago · restante), parcelável, ciclos anteriores em aberto (⚠ +2 ciclos · R$ X), conciliação detectada (💚 conciliada: R$ Y em 12/08), ação "Pagar agora" (cria aprovação — cai na aba Decisões)
- **Histórico —** `ListaTransacoes`: linha por transação — ícone (serviço 🎬🎵🍕 / banco 🏛🟣 / categoria 🏥💳 / fallback ↑↓), nome (logo do merchant quando houver), **categoria** (chip com sugestão do agente; clique reabre seletor — mesma lista de categorias atual), data, valor (+/- mono, crédito verde)
- **Ações:** filtro de período (Hoje / 7d / 30d / Tudo — pills discretas, mesmo padrão do wireframe) · busca por texto · categorizar direto na linha · clique na linha → painel Modo Transação
- **Estados:** sem contas conectadas → CTA "Conectar banco" (abre aba Contas) · sem transações no período · loading

### 4.4 Contas

**Conceito:** as contas conectadas (Open Finance / Polp) — o dono vê o caixa e o crédito num lugar só, e gerencia conexões.

- **Elemento:** `ListaContas` — `ContaCard` por conta: tipo (🏦 conta / 💳 cartão), nome + apelido, saldo (mono; negativo em vermelho), status de sincronização (↑ sincronizado · ⚠ erro · desconectado), barra de uso do limite (crédito: R$ X de R$ Y usados, barra com cor por faixa >80% vermelho)
- **Saldo consolidado** em destaque no topo da visão (Caixa + Crédito em uso)
- **Ações:** Conectar banco (chat/overlay de Open Finance) · clique na conta → painel Modo Conta · menu "..." (atualizar, desconectar, renomear apelido)
- **Estados:** nenhuma conta → estado vazio com CTA de conexão

### 4.5 Rotinas

**Conceito:** o que o agente faz sozinho no financeiro — mesmas regras de Clientes (catálogo built-in embasado em funções reais da Rotina API + builder por chat + feed).

- **Catálogo built-in (proposta — validar funções no backend):** Cobrança de inadimplentes (lista inadimplentes e prepara follow-up) · Revisão de gastos (análise mensal por categoria) · Conciliação automática (cruza faturas × transações e marca 💚) · Resumo financeiro mensal (relatório) · Alerta de saldo baixo / limite próximo · **Disparo de processos** (ex.: "criar missão de fechamento mensal no dia 28")
- **Configuradas:** `RotinaCard` — nome, gatilho legível ("Toda segunda às 8h"), status ativa/pausada, última execução + resultado; ações: Rodar agora · Pausar/Retomar · Editar com IA
- **Feed de execuções:** `FeedExecucoes` (mesmo padrão Clientes)

---

## 5. Painel contextual — modos por aba

| Aba | Modo | O que o painel mostra |
|---|---|---|
| Decisões | **Modo Decisão** | decisão em foco: tipo, valor (destaque mono), vencimento, origem, o que o agente propôs e por quê · ações: **Agendar/Aprovar** (só aprovador) · Adiar (1d/3d/7d/data) · Rejeitar (motivo opcional) · "Ver no fluxo" (leva à transação/fatura correspondente) |
| Processos | **Modo Processo** | processo em foco: missão, etapa atual, **passo a passo das etapas** (Coleta → Dados → Relatório → Final, com check nas concluídas e a porta de aprovação em destaque) · quem aprova cada porta · artefatos por etapa (dados brutos, relatório, versão final) com preview · **relatório final com comparações (vs mês passado, vs mesmo mês do ano anterior, vs média do ano, vs 6 meses)** · ações: **Aprovar etapa** (só quem tem permissão) · Rejeitar (motivo, volta) · Adiar · Gerar relatório · ver histórico do processo |
| Fluxo | **Modo Fatura** | fatura em foco: vencimento, valor + mínimo, pagamentos parciais, parcelável, ciclos anteriores, conciliação (quais transações casam) · ações: Pagar agora (cria decisão) · ver transações da fatura |
| Fluxo | **Modo Transação** | transação em foco: nome/logo, data, valor, conta, categoria (trocar direto) · conciliação com fatura se houver · "Ver no fluxo" |
| Contas | **Modo Conta** | conta em foco: saldo, limite/uso, status de sync, extrato resumido (últimas transações) · ações: atualizar · desconectar (confirmação) · apelido |
| Rotinas | **Modo Rotina** | configuração da rotina: gatilho/frequência/ação/filtro/canal editáveis no lugar · Rodar agora · Pausar · Ver execuções · Editar com IA (builder) |
| qualquer | **Modo Preview** | boleto/fatura/relatório/documento financeiro renderizado dentro do painel (Baixar · Enviar · abrir completo) — mesmo padrão D15/U26 de Clientes |

**Trilha:** clicar num item de outra aba **substitui** o modo; navegar para dentro (ex.: processo → relatório → preview) **empilha**; X/Esc limpa (U24).

---

## 6. Quadrinhos (D — no plano)

| Quadrinho | Conteúdo |
|---|---|
| Q1 **Insights do agente** | 2–3 cards de sugestão proativa (ex.: "Fatura Nubank vence em 2 dias — pagar agora?", "Gastos com restaurantes +30% vs mês passado", "Fechamento do mês pendente — criar missão?", "3 boletos sem conciliação") · ações: Abrir decisão · Criar processo · Dispensar |
| Q2 **Métricas da sala** | período 30d/90d/1y: Faturamento · Despesas · Margem · Fluxo 30d · Caixa consolidado · Burn rate · Runway · DSO/DPO/CCC (as que existem no `getFinanceIndicators`/context metrics) · clique numa métrica → Estratégia ou lista filtrada |
| Q2b **Comparações (por métrica, só as relevantes)** | além do valor, a métrica mostra as comparações aplicáveis em pills — **vs mês passado (MoM) · vs mesmo mês do ano anterior (YoY) · vs média do ano anterior · vs média dos últimos 6 meses** (decisão D6: cada métrica declara quais se aplicam; ex.: DSO/DPO/CCC não têm "média do ano"). Ex.: "Faturamento · R$ 48K · ↑ 12% vs mês passado · ↑ 8% vs jul/25 · ↑ 5% vs média do ano". As mesmas comparações entram no **relatório final dos processos** (Modo Processo/Preview) |
| Q2c **Mapa de contexto do negócio** | as comparações alimentam o contexto do agente (`contextMetrics`, dimensão finance) — as métricas não vivem isoladas na sala: o mesmo mapa vira pauta em Estratégia e base das sugestões do Q1 |
| Q3 **Contas rápido** | contas conectadas com saldo, atalho para aba Contas; sem contas → CTA "Conectar banco" |

---

## 7. De → Para (o que muda vs Financeiro atual)

| Hoje (FinanceiroRoom.tsx) | Proposta |
|---|---|
| Tabs: Decisões · Transações · Tarefas · Config | Tabs: **Decisões · Processos · Fluxo · Contas · Rotinas** — Config some (conexão vira aba Contas; config de rotina vira Modo Rotina do painel) |
| "Nova Missão" abre chat genérico e a missão não é rastreável | Missão vira **processo com etapas** na aba Processos — o dono vê o fluxo e destrava as aprovações |
| Painel lateral colapsável (rcol): Contas + Próximos pagamentos | Aba **Contas** + quadrinho Q3; "Próximos pagamentos" vira parte do Fluxo e das Decisões |
| Strip inferior: insights + chips de KPI + **gráfico de receita com dados fixos** | Quadrinhos D (insights + métricas reais); gráfico fake **some** (sem dados inventados) |
| Transações = faturas e histórico misturados | Aba **Fluxo** com duas áreas claras (Contas a pagar + Histórico), faturas com semáforo e conciliação |
| Decisões = lista simples de aprovação | **FilaDecisoes** com semáforo, valor, ação sugerida, seleção em lote, contador na aba |
| KPIs no rodapé/analytics panel | Métricas no **quadrinho Q2** — nada de strip no topo |

---

## 8. Papéis e permissões (multi-usuário — configuração no Admin)

- **Perfil base por sala:** criador (abre missões, conecta contas, propõe) · aprovador (aprova/agenda/rejeita) · visualizador (só vê)
- **Admin (owner) configura por sala** quem tem cada permissão: quem aprova · quem move card entre etapas · quem conecta conta · quem cria missão. **Quem move o card = quem tem autorização de mover** (não é regra fixa por cargo)
- Papel varia por dimensão (usuário aprovador no Financeiro, visualizador em Clientes — direção 07/08)

---

## 9. Decisões em aberto (validar antes de especificar)

### Resolvidas nesta rodada (12/08)

| # | Decisão |
|---|---|
| D1 | **Processos não são só fiscais** — a aba Processos cobre Nota Fiscal, Balanço anual, Fechamento mensal (DRE), Declaração, fluxo de caixa **e relatórios gerenciais** (custo-benefício, desempenho) |
| D2 | **Etapas: as 4 são a base** — Coleta → Aprovação dos dados → Aprovação do relatório → Relatório final; cada tipo de processo ajusta depois (fundador: "serão uma boa parte, teremos que ajustar") |
| D3 | **Quem move o card = quem tem autorização de mover** — permissões por sala configuradas no Admin (owner), não regra fixa por cargo |
| D4 | **Comparações em toda métrica** — vs mês passado (MoM) · vs mesmo mês do ano anterior (YoY) · vs média do ano anterior · vs média dos últimos 6 meses; alimentam o **mapa de contexto do negócio** (context metrics) e entram no relatório final dos processos |
| D5 | **Primeiros processos (v1):** Fechamento mensal (DRE) · Balanço anual · Nota Fiscal · Relatório de fluxo de caixa — aprovado |
| D6 | **Comparações só quando fazem sentido por métrica** — a métrica declara quais comparações são aplicáveis (ex.: DSO/DPO/CCC não têm "média do ano"; receita tem as 4) |

### Em aberto

1. **Abas:** Decisões · Processos · Fluxo · Contas · Rotinas (proposta v2) vs outra combinação? (Config some — proposta)
2. **Etapas custom por processo:** quando surgir a primeira exceção (ex.: "Validação fiscal" na Nota Fiscal), quem define a etapa extra — agente propõe e dono aprova, ou dono configura?
3. **Conciliação automática** como rotina built-in (cruza fatura × transações, marca 💚) — entra no catálogo? (função existe no backend?)
4. **Quadrinho Q2 — quais métricas** entram de cara? (proposta: Faturamento · Despesas · Margem · Fluxo 30d · Caixa consolidado · Burn rate · Runway · DSO · DPO · CCC — as disponíveis no indicadores/context)
5. **"Nova Missão":** manter no topo como entrada do chat (proposta) vs esconder atrás das ações diretas?
6. **Painel sem seleção:** estado vazio "Selecione um item" (mesmo padrão Clientes — manter consistência)?
7. **Próximas salas:** depois de Financeiro, seguimos para **Compras** (já tem spec parcial) — confirmar a ordem das prioridades ("Saúde" citada é sala nova ou outro projeto?)

---

## Próximo passo

Após validar as decisões acima: expandir para a **spec completa** no padrão [template-tela.md](./template-tela.md) (elemento por elemento, opções, estados, biblioteca, regras U#, cenários de teste) e gerar o **wireframe da sala Financeiro** seguindo o `/blu-site/` — para o Claude Code construir.
