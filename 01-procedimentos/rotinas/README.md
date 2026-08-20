# 🔁 Rotinas — Deep Blue

> **Rotinas = o que acontece de forma recorrente** (crons, checkpoints diários,
> cadências de conteúdo). Diferente de **procedimentos** (como fazer algo), a
> rotina define **quando/qual frequência** algo roda.
>
> Cada área tem sua pasta de rotinas — e o [inventário de crons](./inventario-crons.md)
> registra o que está automatizado, onde usamos LLM e onde o script basta.

| Área | Rotinas | Inventário |
|---|---|---|
| **Operações diárias** | [rotinas-diarias.md](./rotinas-diarias.md) — resumo da manhã, proposta da noite, monitoramento | — |
| **Produção de código** | pipeline (crons de fila, watchdog, verificação) | [inventario-crons.md](./inventario-crons.md) |
| **Conteúdo** | cadência editorial (pesquisa → aprovação → publicação) | [rotinas-conteudo.md](./rotinas-conteudo.md) |
| **Manutenção** | limpeza de disco, memória, health-checks | [inventario-crons.md](./inventario-crons.md) |

## Princípio (decisão 2026-08-20)

**Crons = script-first.** LLM só onde há julgamento (resumir, propor, revisar).
Tudo determinístico vira script `no_agent`. O inventário registra, por cron:
o que faz, quando roda, se usa LLM, e se é script.

## Forma de trabalho diária (proposta — a validar com o dono)

| Horário | Rotina | Tipo |
|---|---|---|
| **09:00** | Resumo do que foi feito durante a noite + proposta do dia (dono analisa) | LLM (julgamento) |
| **18:00/noturno** | Análise do worktree + proposta de tarefas para a noite | LLM (julgamento) |
| Contínuo | Pipeline de código (fila, watchdog) | Script |
| Contínuo | Guards (memória, disco, gateway) | Script |

*(detalhes em [rotinas-diarias.md](./rotinas-diarias.md))*
