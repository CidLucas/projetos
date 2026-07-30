# 🏠 Início (Home) — Requisitos Blue V3

> Última atualização: 2026-07-30
> Status: 🟡 Em andamento
> Fonte: `apps/blu_web/src/pages/app/HomePage.tsx` (594 linhas)

---

## 1. Visão Geral

**Objetivo:** Dashboard principal que agrega o status de todos os agentes e áreas da empresa em uma única tela. Ponto de entrada pós-login.

**Contexto:** Primeira tela que o usuário vê após onboarding. Centraliza decisões pendentes, KPIs, insights, rotinas e próximos eventos.

**Relação com outras páginas:** Cada card/seção linka para a página específica do agente (Compras, Financeiro, Agenda, Estratégia, Clientes, Documentos/Biblioteca).

---

## 2. Estrutura de Elementos (Front-End)

### 2.1 Header da página
- **Tipo:** barra de título
- **Posição:** topo da área de conteúdo
- **Conteúdo/Dados:** ícone da casa + título "Início" + subtítulo descritivo
- **Interações:** nenhuma direta (navegação é feita via Sidebar)

### 2.2 Cards de Decisões Pendentes (por agente)
- **Tipo:** cards empilhados verticalmente (DecisionCard)
- **Posição:** coluna esquerda do conteúdo
- **Conteúdo/Dados:** cada card representa uma aprovação pendente — slug do agente, título, descrição, timestamp, prioridade
- **Interações:** expandir (toggle detalhes), aprovar, rejeitar, adiar (snooze)
- **Estados visuais:** card normal, expandido (mostra detalhes), botões de ação (aprovar verde, rejeitar vermelho, adiar amarelo)
- **Condições de visibilidade:** sempre visível; estado vazio se não houver pendências

### 2.3 Painel de Insights
- **Tipo:** lista de cards com indicadores coloridos
- **Posição:** coluna central
- **Conteúdo/Dados:** insights gerados pelos agentes — título, observação, recomendação, KPI afetado, sala de origem
- **Interações:** clique abre popover com 3 ações: "Explique este insight", "Como agir?", "Analisar tendência" (dispara chat)
- **Estados visuais:** dot colorido por agente, popover com opções
- **Condições de visibilidade:** sempre visível; estado vazio se não houver insights

### 2.4 Seção de Rotinas
- **Tipo:** lista de cards de rotina
- **Posição:** coluna direita
- **Conteúdo/Dados:** rotinas ativas do cliente — nome, status (active/pending_approval/inactive), última execução
- **Interações:** ativar/desativar rotina, expandir detalhes
- **Estados visuais:** indicador colorido por status (teal = ativa, yellow = pendente, gray = inativa)
- **Condições de visibilidade:** sempre visível

### 2.5 Mini-Calendário / Próximos Dias
- **Tipo:** strip horizontal com dias da semana
- **Posição:** inferior do dashboard
- **Conteúdo/Dados:** próximos 5 dias úteis com eventos do Google Calendar (se conectado)
- **Interações:** clique no dia expande eventos
- **Estados visuais:** dia atual destacado, indicadores de evento
- **Condições de visibilidade:** sempre visível

### 2.6 KPIs Rápidos (métricas)
- **Tipo:** cards numéricos compactos
- **Posição:** espalhados entre as seções
- **Conteúdo/Dados:** indicadores financeiros, comerciais, de agenda — valores formatados (BRL, %)
- **Interações:** clique navega para a página do agente correspondente
- **Estados visuais:** loading (skeleton), valor formatado, tendência (↑↓)

---

## 3. Fluxos de Processo

### 3.1 Aprovar/Rejeitar Decisão
```
Usuário vê card de decisão pendente
  │
  ├─ Expande o card (toggle)
  │     Mostra detalhes: o que o agente propõe, dados de contexto
  │
  ├─ Clique em "Aprovar" → card some da lista
  ├─ Clique em "Rejeitar" → card some da lista
  └─ Clique em "Adiar" → modal de snooze (15min, 1h, 4h, amanhã) → card some temporariamente
```

### 3.2 Investigar Insight
```
Usuário clica em um insight → popover abre acima do card
  │
  ├─ "Explique este insight" → abre ChatPanel com prompt contextual
  ├─ "Como agir?" → abre ChatPanel com prompt de ação
  └─ "Analisar tendência" → abre ChatPanel com prompt de projeção
```

---

## 4. Regras de Negócio

| # | Regra |
|---|---|
| R1 | Decisões com prioridade "urgent" + mais de 2h são destacadas visualmente |
| R2 | O dashboard agrega dados de TODOS os agentes (Compras, Financeiro, Agenda, Estratégia, Clientes, Documentos) |
| R3 | Ao clicar em um KPI ou seção, navega para a página do agente correspondente |

---

## 5. Integrações

| Integração | Tipo | Descrição |
|---|---|---|
| fetchPendingApprovals | React Query | Lista de aprovações pendentes de todos os agentes |
| getFinanceIndicators | React Query | KPIs financeiros |
| getAgendaEvents | React Query | Eventos de agenda |
| getInsights | React Query | Insights gerados pelos agentes |
| getCommercialIndicators | React Query | KPIs comerciais |
| fetchRoutines | React Query | Rotinas ativas do cliente |
| Google Calendar | OAuth | Eventos do calendário Google |

---

## 6. Cenários de Teste

### Happy Path
- [ ] Usuário logado vê dashboard com decisões, insights, rotinas e KPIs
- [ ] Aprovar uma decisão → card desaparece
- [ ] Clicar em insight → popover → "Explicar" → chat abre

### Edge Cases
- [ ] Nenhuma decisão pendente → estado vazio amigável
- [ ] Nenhum insight → estado vazio
- [ ] Google Calendar não conectado → mini-calendário sem eventos externos
