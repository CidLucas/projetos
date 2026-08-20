# 🔧 Pipeline de Produção de Código — Deep Blue

> **Procedimento:** como transformamos issues em código entregue e verificado.
> **Status:** vigente (validado 2026-08-20 na F0 do assistente pessoal).
> **Dono:** Lucas Cid · **Executor da orquestração:** Hermes (profile PM).

---

## 1. Visão geral

```
Issue (GitHub) → Spec (scripts/prompts/) → Dispatch (OpenCode/Claude Code)
     → Branch encadeada + commits → Push → Verificação empírica
     → Comentário na issue → PR por fase → Merge (dono)
```

Cada issue vira **uma sessão de agente de código** que entrega
`branch + commits + push`. A orquestração (watchdog/cron) garante **1 worker
por vez** e **verificação empírica antes de avançar**.

## 2. Pré-requisitos (antes de despachar)

1. **Issue no GitHub** com critérios de pronto claros (`gh issue view N`).
2. **Spec versionada na main**: `scripts/prompts/issue-<N>-<tool>.md` — commit
   `chore(scripts): specs ...` + push ANTES do dispatch (o worker lê a spec
   DENTRO do worktree).
3. **Roteamento por complexidade** (revisado a cada fase):
   - **Simples** (1-2 arquivos, port de código, config) → **OpenCode**
   - **Complexas** (multi-arquivo, código novo, infra, lógica intrincada) → **Claude Code**
   - Claude sem créditos → **fallback OpenCode** (não bloquear a fila).
4. **Branches encadeadas**: a branch da issue N+1 nasce da branch da N
   (`fix/f0-322` base `fix/f0-321`), nunca da main — preserva dependências.

## 3. Dispatch

```bash
# OpenCode (simples):
bash ~/.hermes/scripts/dispatch-opencode-wt.sh scripts/prompts/issue-N-opencode.md fix/f0-N fix/f0-<anterior>
# Claude Code (complexas):
bash ~/.hermes/scripts/dispatch-claude.sh scripts/prompts/issue-N-claude.md fix/f0-N fix/f0-<anterior>
```

- **Worktree dedicado** em `~/worktrees/wk-<N>` (disco real, não /tmp).
- **Instrução obrigatória ao worker**: "commits incrementais, commite cedo,
  push no final, rode só os testes dos arquivos tocados (nunca a suíte inteira
  com --cov), não invente dados".
- **Depois do push, encerrar a sessão imediatamente** (não explorar mais nada —
  decisão 2026-08-20, P2).

## 4. Verificação empírica (regra de ouro)

**Nunca confiar no self-report do agente.** Antes de marcar done:

1. **Push confirmado**: `git ls-remote --heads origin fix/f0-N` retorna o commit.
2. **Testes reais no worktree** (PYTHONPATH do worktree + venv do monorepo):
   ```bash
   cd ~/worktrees/wk-N
   LIBPATHS=$(ls -d /home/ec2-user/monorepo/libs/*/src | tr '\n' ':')
   PYTHONPATH="$PWD/libs/blu_agno_runtime/src:${LIBPATHS}" \
     /home/ec2-user/monorepo/.venv/bin/python -m pytest <testes_tocados> -q
   ```
3. **Diff revisado** (o que mudou, sem surpresas).
4. **Comentário na issue** com evidências (commits, testes, push).
5. Só então a fila avança para a próxima.

## 5. Recovery (quando o worker falha)

| Sintoma | Ação |
|---|---|
| Sessão esgotou sem commit (worktree limpo) | Redispatch da MESMA issue com instrução "commite cedo"; máx 2 tentativas |
| Worker morto COM push | Verificar empiricamente → done → avançar (não redespachar!) |
| Worker vivo após entregar (explorando) | **Matar o processo** — trabalho já commitado/pusheado (P2) |
| 2 tentativas sem push | Parar a fila, reportar para revisão manual |

## 6. PR e merge

- **1 PR por fase** (cadeia encadeada inteira) — ex.: `fix/f0-320 → main` cobre a F0.
- **Revisão com Claude Code antes do merge** (padrão do pipeline) quando o dono
  pedir; senão merge direto pelo dono.
- Issues fecham com `Closes #N` no merge.

## 7. Crons: script-first

**Princípio (decisão 2026-08-20): crons devem ser scripts ao máximo — LLM só
onde há julgamento.**

| Tarefa | Deve ser | Exemplo |
|---|---|---|
| Dispatch de issue já refinada (spec pronta) | **Script** (no_agent) | `dispatch-opencode-wt.sh` |
| Watchdog de fila (worker vivo? terminou?) | **Script** | `assistente-fila-watchdog.py` |
| Verificação mecânica (push? testes?) | **Script** | parte do watchdog |
| Decidir roteamento/prioridade/revisar qualidade | **LLM** (agente cron) | reavaliação por fase |

Regra: se a decisão é determinística (issue refinada + spec pronta + fila
ordenada), é script. O LLM entra só para o que exige julgamento.

## 8. Dívida técnica

- **Fila de dívida = GitHub com label `tech-debt`** (não documento).
- Dívida pré-existente encontrada por worker → **registrar como issue** na hora
  (política do monorepo), não consertar de carona.
- Revisão semanal da fila `tech-debt` (decisão 2026-08-20, P4).
