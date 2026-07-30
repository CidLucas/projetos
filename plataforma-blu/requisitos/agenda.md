# 📅 Agenda — Requisitos Blue V3

> Última atualização: 2026-07-30 | Status: 🟡 Em andamento
> Fonte: `apps/blu_web/src/pages/app/AgendaRoom.tsx` (460 linhas)

---

## 1. Visão Geral

**Objetivo:** Gestão de agenda e tarefas com IA — Gantt mensal, tarefas do dia, pendências e Google Calendar.

**Contexto:** O agente Agenda organiza tarefas, compromissos e rotinas em linha do tempo.

**Relação com outras páginas:** Home (mini-calendário), Admin (conexão Google Calendar).

---

## 2. Estrutura de Elementos (Front-End)

### 2.1 Tabs de navegação
- **Tipo:** tabs horizontais
- **Conteúdo/Dados:** 6 abas — Decisões, Gantt, Hoje, Pendentes, Histórico, Config

### 2.2 Tab: Decisões
- **Tipo:** lista de aprovações do agente agenda
- **Interações:** aprovar, adiar (snooze)

### 2.3 Tab: Gantt (Principal)
- **Tipo:** gráfico de Gantt mensal (MonthlyGantt)
- **Conteúdo/Dados:** tarefas/eventos no mês — barras coloridas (approval=laranja, calendar=azul)
- **Interações:** scroll horizontal, clique em tarefa

### 2.4 Tab: Hoje
- **Tipo:** lista de tarefas do dia (UnifiedTask)
- **Interações:** expandir detalhes (toggle)

### 2.5 Tab: Pendentes
- **Tipo:** lista de tarefas não concluídas

### 2.6 Tab: Histórico
- **Tipo:** lista cronológica

### 2.7 Tab: Config
- **Tipo:** RoutineConfigSection + CollapsiblePanel + conectar Google Calendar

---

## 3. Fluxos de Processo

### 3.1 Google Calendar
```
Usuário conecta Google Calendar (OAuth)
  → Eventos externos sincronizados → visíveis no Gantt e tab Hoje
  → Agente Agenda pode criar eventos no Google Calendar
```

---

## 4. Regras de Negócio

| # | Regra |
|---|---|
| R1 | Gantt mostra mês atual com barras coloridas por tipo |
| R2 | Tarefas Google Calendar mescladas com tarefas internas |
| R3 | OAuth requer permissão explícita do usuário |

---

## 5. Integrações

| Integração | Tipo | Descrição |
|---|---|---|
| fetchTodaySchedule | Query | Tarefas de hoje |
| fetchUnifiedTasks | Query | Tarefas unificadas |
| fetchExternalAgendaEvents | Query | Eventos Google Calendar |
| connectGoogleCalendar | Mutation | OAuth Google Calendar |

---

## 6. Cenários de Teste

- [ ] Visualizar Gantt mensal
- [ ] Conectar Google Calendar
- [ ] Google Calendar não conectado → apenas tarefas internas
