# 📋 Inventário de Crons — Deep Blue

> **Objetivo:** registrar todos os crons do ambiente: o que fazem, quando rodam,
> se usam **LLM** ou são **script puro**. Fonte para decidir onde otimizar
> (script-first) e onde o julgamento LLM é necessário.
>
> **Atualizado:** 2026-08-20

## Legenda

- **Tipo:** `script` (no_agent, zero LLM) | `agente` (LLM decide) | `híbrido`
- **Custo:** LLM por tick? (sim/não)

## Pipeline de código (assistente pessoal)

| Cron | O que faz | Frequência | Tipo | Custo LLM |
|---|---|---|---|---|
| `assistente-pessoal-fila` | Watchdog da fila F0→F3: 1 worker/vez, verificação, redispatch | 10min | script | ❌ nenhum |
| dispatch-opencode/claude | Lança worker da issue em worktree | sob demanda (via fila) | script | ❌ (o worker usa LLM, mas o dispatch não) |
| `opencode-db-purge-idle` | Purga opencode.db quando idle >6h | 5min | script | ❌ |
| `disk-cleanup-4h` | Limpeza de disco com early-exit | 4h | script | ❌ |
| `disk-guard-85` | Alerta quando disco >85% | 60min | script | ❌ |
| `memory-guard` | Vigia memória da instância | 5min | script | ❌ |
| `gateway-health-guard` | Watchdog de saúde do gateway | 5min | script | ❌ |

## Produtos (memory_api/Brain, formly, ops)

| Cron | O que faz | Frequência | Tipo | Custo LLM |
|---|---|---|---|---|
| `brain-pipeline-orquestrador` | Orquestra fila do Brain (board kanban) | 10min | **agente** | ✅ sim |
| `brain-pipeline-cleanup` | Limpeza entre fases | 10min | script | ❌ |
| `revisao-claude-f1f4` | Revisão de fases com Claude Code | 30min | **agente** | ✅ sim |
| `supervisor-opencode-5min` | Supervisa workers opencode (kanban) | 5min | **agente** | ✅ sim |
| `ops-centro-retention-diario` | Retenção de logs Turso | diário 04:17 | script | ❌ |
| `duckdns-ip-update` | Atualiza IP DuckDNS | 5min | script | ❌ |

## Manutenção geral

| Cron | O que faz | Frequência | Tipo | Custo LLM |
|---|---|---|---|---|
| `experiment-gate-poll` | Poll de gates (pausado) | 5min | script | ❌ |
| `factory-gate-poll` | Poll de gates factory (pausado) | 40min | script | ❌ |

## Oportunidades de otimização (script-first)

1. **`brain-pipeline-orquestrador`, `supervisor-opencode-5min`** — hoje são
   agentes LLM; o ciclo (pgrep → fila → dispatch) é determinístico → candidatos
   a virar script como o `assistente-pessoal-fila` (padrão já validado).
2. **`revisao-claude-f1f4`** — revisão exige julgamento, mantém LLM (correto).
3. **Rotinas novas propostas** (resumo 09:00, proposta noturna) — LLM por
   natureza (julgamento), mas com script de coleta de dados antes (issues,
   git status) para o LLM só resumir.

## Regra de ouro

> Se a decisão é determinística → script. Se exige julgamento → LLM.
> Todo cron novo entra neste inventário antes de subir.
