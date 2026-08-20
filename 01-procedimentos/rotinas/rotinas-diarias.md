# 🕐 Rotinas Diárias — Deep Blue

> **Status:** proposta (2026-08-20, a validar com o dono)
> **Objetivo:** forma de trabalho recorrente entre o dono e os agentes.

## Manhã (09:00) — resumo + proposta

**O que:** o Hermes entrega um resumo do que foi feito durante a noite
(pipeline, crons, issues fechadas) e **propõe** o foco do dia.

**Quem:** profile PM (LLM — exige julgamento: priorizar, propor).

**Entregável:**
- Resumo noturno: issues concluídas, PRs abertos, falhas/alertas
- Proposta do dia: top 3 prioridades com rationale
- Dono analisa e aprova/ajusta

## Noite (18:00 ou horário de fim do dia) — análise do worktree + propostas

**O que:** o Hermes analisa o estado do trabalho (worktrees, branches, WIP) e
**propõe tarefas para a noite** (o que pode rodar autônomo enquanto o dono
dorme).

**Quem:** profile PM (LLM).

**Entregável:**
- Estado dos worktrees/branches (WIP visível, nada escondido)
- Proposta de tarefas noturnas: fila de issues para rodar com agentes
- Gate de segurança: o que NÃO rodar sem revisão

## Monitoramento contínuo (scripts)

- Pipeline de código: watchdog a cada 10min (script, silencioso quando ok)
- Guards: memória (5min), disco (60min), gateway (5min) — todos script
- Limpeza de disco: 4h com early-exit

## Validação pendente com o dono

- [ ] Horários exatos (09:00 / 18:00?)
- [ ] Canal (Telegram? dashboard?)
- [ ] Formato do resumo (compacto? tabelas?)
- [ ] Quais tarefas podem rodar à noite sem aprovação
