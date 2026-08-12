# 💰 Proposta — Sala Financeiro (Novo Front Blu)

> Última atualização: 2026-08-12 | Status: 🟡 Proposta para validar
> Base: wireframe do novo front (`/blu-site/` — sala Clientes) + Financeiro atual (`apps/blu_web/src/pages/app/FinanceiroRoom.tsx`, 934 linhas)
> Padrão: elementos puros · abas discretas · painel contextual · quadrinhos — mesmo conceito de [clientes.md](./clientes.md)

---

## 1. Visão

A sala Financeiro deixa de ser uma **mesa de ferramentas** (4 abas + painel lateral de contas + strip de KPIs + gráfico) e vira a **dimensão financeira do negócio**: o dono responde em segundos *"quanto tenho, quanto devo, o que precisa de mim agora"*.

O agente financeiro continua no centro — analisa transações, categoriza, concilia, propõe decisões — mas a sala se organiza em torno do que o **dono precisa decidir e ver**, não em torno das ferramentas do agente.

**Relação com outras salas:** Home (urgências financeiras), Estratégia (métricas aprofundadas), Admin (conexão Open Finance de primeira vez).

---

## 2. Princípios aplicados (do novo conceito)

| # | Princípio |
|---|---|
| P1 | **Abas discretas, sem faixa horizontal** — nada de strip de métricas no topo; contador de pendência na aba |
| P2 | **Painel direito contextual (~380px)** — cada aba tem seu modo; navegar para dentro de um item empilha trilha (breadcrumb) |
| P3 | **Quadrinhos no rodapé (D)** — insights do agente + métricas da sala; métricas nunca no topo |
| P4 | **Elementos puros** — novos nomes de biblioteca, informação + ação, sem referência ao design atual |
| P5 | **Semáforo 🟢🟡🔴** em tudo que tem prazo: vencimento, limite de crédito, saldo baixo, conciliação pendente |
| P6 | **Números em mono**, contraste AA, 4 temas (dark / azul / mono / warm) |
| P7 | **Papéis fixos por dimensão** — no Financeiro o dono é **aprovador**: só aprovador vê Agendar/Aprovar |
| P8 | **Sem kanban** — Financeiro é sala de **fila/fluxo** (decisões + dinheiro), não de pipeline de etapas |

---

## 3. Layout macro

```
┌──────────────────────────────────────────────────────────────────────────┐
│ A · Topo:  [Decisões 3] [Fluxo] [Contas] [Rotinas]   …  [+ Nova missão]  │
│            (abas discretas — sem faixa horizontal; sem strip de métricas) │
├───────────────────────────────────────────────────────┬──────────────────┤
│ B · VISÃO DA ABA ATIVA                                │ C · PAINEL       │
│   Decisões → fila de aprovações (semáforo + valor)    │   CONTEXTUAL     │
│   Fluxo    → contas a pagar + histórico de transações │   (fixo ~380px)  │
│   Contas   → contas conectadas + saldo consolidado    │   muda por ABA:  │
│   Rotinas  → catálogo + configuradas + feed           │   Decisões→Decis.│
│                                                       │   Fluxo→Fatura/  │
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

### 4.2 Fluxo

**Conceito:** o dinheiro que entra e sai, em duas áreas na mesma visão: **Contas a pagar** (faturas/boletos por cartão com status) e **Histórico** (transações categorizadas).

- **Contas a pagar —** `FaturaCard` por cartão/banco: nome do cartão, vencimento ("vence hoje", "3d atrasada" — semáforo), valor total + mínimo, parcialmente pago (✓ pago · restante), parcelável, ciclos anteriores em aberto (⚠ +2 ciclos · R$ X), conciliação detectada (💚 conciliada: R$ Y em 12/08), ação "Pagar agora" (cria aprovação — cai na aba Decisões)
- **Histórico —** `ListaTransacoes`: linha por transação — ícone (serviço 🎬🎵🍕 / banco 🏛🟣 / categoria 🏥💳 / fallback ↑↓), nome (logo do merchant quando houver), **categoria** (chip com sugestão do agente; clique reabre seletor — mesma lista de categorias atual), data, valor (+/- mono, crédito verde)
- **Ações:** filtro de período (Hoje / 7d / 30d / Tudo — pills discretas, mesmo padrão do wireframe) · busca por texto · categorizar direto na linha · clique na linha → painel Modo Transação
- **Estados:** sem contas conectadas → CTA "Conectar banco" (abre aba Contas) · sem transações no período · loading

### 4.3 Contas

**Conceito:** as contas conectadas (Open Finance / Polp) — o dono vê o caixa e o crédito num lugar só, e gerencia conexões.

- **Elemento:** `ListaContas` — `ContaCard` por conta: tipo (🏦 conta / 💳 cartão), nome + apelido, saldo (mono; negativo em vermelho), status de sincronização (↑ sincronizado · ⚠ erro · desconectado), barra de uso do limite (crédito: R$ X de R$ Y usados, barra com cor por faixa >80% vermelho)
- **Saldo consolidado** em destaque no topo da visão (Caixa + Crédito em uso)
- **Ações:** Conectar banco (chat/overlay de Open Finance) · clique na conta → painel Modo Conta · menu "..." (atualizar, desconectar, renomear apelido)
- **Estados:** nenhuma conta → estado vazio com CTA de conexão

### 4.4 Rotinas

**Conceito:** o que o agente faz sozinho no financeiro — mesmas regras de Clientes (catálogo built-in embasado em funções reais da Rotina API + builder por chat + feed).

- **Catálogo built-in (proposta — validar funções no backend):** Cobrança de inadimplentes (lista inadimplentes e prepara follow-up) · Revisão de gastos (análise mensal por categoria) · Conciliação automática (cruza faturas × transações e marca 💚) · Resumo financeiro mensal (relatório) · Alerta de saldo baixo / limite próximo
- **Configuradas:** `RotinaCard` — nome, gatilho legível ("Toda segunda às 8h"), status ativa/pausada, última execução + resultado; ações: Rodar agora · Pausar/Retomar · Editar com IA
- **Feed de execuções:** `FeedExecucoes` (mesmo padrão Clientes)

---

## 5. Painel contextual — modos por aba

| Aba | Modo | O que o painel mostra |
|---|---|---|
| Decisões | **Modo Decisão** | decisão em foco: tipo, valor (destaque mono), vencimento, origem, o que o agente propôs e por quê · ações: **Agendar/Aprovar** (só aprovador) · Adiar (1d/3d/7d/data) · Rejeitar (motivo opcional) · "Ver no fluxo" (leva à transação/fatura correspondente) |
| Fluxo | **Modo Fatura** | fatura em foco: vencimento, valor + mínimo, pagamentos parciais, parcelável, ciclos anteriores, conciliação (quais transações casam) · ações: Pagar agora (cria decisão) · ver transações da fatura |
| Fluxo | **Modo Transação** | transação em foco: nome/logo, data, valor, conta, categoria (trocar direto) · conciliação com fatura se houver · "Ver no fluxo" |
| Contas | **Modo Conta** | conta em foco: saldo, limite/uso, status de sync, extrato resumido (últimas transações) · ações: atualizar · desconectar (confirmação) · apelido |
| Rotinas | **Modo Rotina** | configuração da rotina: gatilho/frequência/ação/filtro/canal editáveis no lugar · Rodar agora · Pausar · Ver execuções · Editar com IA (builder) |
| qualquer | **Modo Preview** | boleto/fatura/documento financeiro renderizado dentro do painel (Baixar · Enviar · abrir completo) — mesmo padrão D15/U26 de Clientes |

**Trilha:** clicar num item de outra aba **substitui** o modo; navegar para dentro (ex.: decisão → fatura → preview) **empilha**; X/Esc limpa (U24).

---

## 6. Quadrinhos (D — no plano)

| Quadrinho | Conteúdo |
|---|---|
| Q1 **Insights do agente** | 2–3 cards de sugestão proativa (ex.: "Fatura Nubank vence em 2 dias — pagar agora?", "Gastos com restaurantes +30% vs mês passado", "3 boletos sem conciliação") · ações: Abrir decisão · Dispensar |
| Q2 **Métricas da sala** | período 30d/90d/1y: Faturamento · Despesas · Margem · Fluxo 30d · Caixa consolidado · Burn rate · Runway · DSO/DPO/CCC (as que existem no `getFinanceIndicators`/context metrics) · clique numa métrica → Estratégia ou lista filtrada |
| Q3 **Contas rápido** | contas conectadas com saldo, atalho para aba Contas; sem contas → CTA "Conectar banco" |

---

## 7. De → Para (o que muda vs Financeiro atual)

| Hoje (FinanceiroRoom.tsx) | Proposta |
|---|---|
| Tabs: Decisões · Transações · Tarefas · Config | Tabs: **Decisões · Fluxo · Contas · Rotinas** — Config some (conexão vira aba Contas; config de rotina vira Modo Rotina do painel) |
| Painel lateral colapsável (rcol): Contas + Próximos pagamentos | Aba **Contas** + quadrinho Q3; "Próximos pagamentos" vira parte do Fluxo e das Decisões |
| Strip inferior: insights + chips de KPI + **gráfico de receita com dados fixos** | Quadrinhos D (insights + métricas reais); gráfico fake **some** (sem dados inventados) |
| Transações = faturas e histórico misturados | Aba **Fluxo** com duas áreas claras (Contas a pagar + Histórico), faturas com semáforo e conciliação |
| Decisões = lista simples de aprovação | **FilaDecisoes** com semáforo, valor, ação sugerida, seleção em lote, contador na aba |
| "Nova Missão" abre chat genérico | Mantém, mas ações contextuais (pagar, categorizar, adiar) acontecem **direto no painel** |
| KPIs no rodapé/analytics panel | Métricas no **quadrinho Q2** — nada de strip no topo |

---

## 8. Papéis (multi-usuário)

- **Criador** — abre missões, conecta contas, propõe
- **Aprovador** (dono, padrão no Financeiro) — Agendar/Aprovar/Rejeitar decisões, autorizar pagamentos
- **Visualizador** — só vê salas/abas; sem botões de ação (U6)
- Papel varia por dimensão (usuário aprovador no Financeiro, visualizador em Clientes — direção 07/08)

---

## 9. Decisões em aberto (validar antes de especificar)

1. **Abas:** Decisões · Fluxo · Contas · Rotinas (proposta) vs manter Decisões · Transações · Tarefas · Config? (Config some — proposta)
2. **Sem kanban** no Financeiro (P8) — confirma? (Clientes/Compras têm kanban; Financeiro é fila + fluxo)
3. **Dentro do Fluxo:** manter "Contas a pagar" + "Histórico" na mesma visão (proposta) vs sub-abas? (Hoje é misturado na mesma aba)
4. **Conciliação automática** como rotina built-in (cruza fatura × transações, marca 💚) — entra no catálogo? (função existe no backend?)
5. **Quadrinho Q2 — quais métricas** entram de cara? (proposta: Faturamento · Despesas · Margem · Fluxo 30d · Caixa consolidado · Burn rate · Runway · DSO · DPO · CCC — as disponíveis no indicadores/context)
6. **"Nova Missão":** manter no topo como entrada do chat (proposta) vs esconder atrás das ações diretas?
7. **Próximas salas:** depois de Financeiro, seguimos para **Compras** (que já tem spec parcial) e depois **Saúde** (se houver) — confirmar a ordem das prioridades
8. **Painel sem seleção:** estado vazio "Selecione um item" (mesmo padrão Clientes — manter consistência)?

---

## Próximo passo

Após validar as decisões acima: expandir para a **spec completa** no padrão [template-tela.md](./template-tela.md) (elemento por elemento, opções, estados, biblioteca, regras U#, cenários de teste) e gerar o **wireframe da sala Financeiro** seguindo o `/blu-site/` — para o Claude Code construir.
