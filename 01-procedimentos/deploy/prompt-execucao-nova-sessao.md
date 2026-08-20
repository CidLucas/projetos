# PROMPT DE EXECUÇÃO — Plano de Atualização e Finalização da Produção (Deep Blue)

> **Uso:** colar este prompt no início de uma NOVA sessão Hermes (profile default/PM).
> **Data:** 2026-08-20 · **Autor:** Lucas Cid (aprovado)
> **Contexto completo:** este prompt é autocontido — não depende de sessão anterior.

---

## Missão

Executar o plano de **atualização e finalização da produção** dos serviços da Deep
Blue: unificar para **1 instância por serviço** no GCP, atualizar todos os
deploys para a **main atual**, e validar com E2E. Plano documentado em:
`/home/ec2-user/projetos-repo/01-procedimentos/deploy/plano-versao-estavel.md`
(repo `CidLucas/deepBlue`, pasta `01-procedimentos/deploy/`).

## Antes de começar — ler (obrigatório)

1. Skill `gcp-cloud-run-deploy` (`skill_view(name='gcp-cloud-run-deploy')`) — tem TODOS os pitfalls validados (region mapping us-east1, deploy.sh, secrets, auth_service). **NÃO reinventar.**
2. Plano: `projetos-repo/01-procedimentos/deploy/plano-versao-estavel.md`
3. Inventário de crons (para não religar nada errado): `projetos-repo/01-procedimentos/rotinas/inventario-crons.md`

## Estado do pipeline (deixado pausado de propósito)

- **Fila assistente pessoal** (`~/.hermes/state/assistente_queue.json`): F0 completa
  (9/9), F1 completa ou quase (10 issues — a última #330 deploy). Cron
  `assistente-pessoal-fila` **PAUSADO no fim da F1** (gate `stop_after_phase: F1`).
  **NÃO religar** — o foco agora é produção. Se o dono pedir para retomar, ver o
  item "Retomar F2" no fim.
- PR **#356** (F0, lib blu_agno_runtime) aberto — dono pode querer mergear antes.

## O que já está na main (Fase A de instrumentação — NÃO refazer)

Commits na main: `2213d6e` (specs P2) + `1b8c174` (Fase A). Já implementado:
- `services/formly-api` → `/health` retorna `{status, service, sha}` (GIT_SHA env)
- `services/memory_api` → `/healthz` retorna `{..., sha}` (GIT_SHA env)
- `apps/auth_service` → nova rota `/api/health` retorna `{status, sha}`
- `scripts/check-versions.sh` — compara deploy vs main (rodar para ver o estado)

**Pendente que EU (sessão nova) devo fazer:**

## Fase A2 — deploy.sh injeta GIT_SHA (build-time)

1. No `scripts/local/deploy.sh` (e `deploy-auth.sh`), adicionar injeção de
   `GIT_SHA=$(git rev-parse origin/main)` como build ARG/env nos 3 serviços
   (formly_api, memory_api via Dockerfile, auth_service). Sem isso o health
   mostra "dev" em produção.

## Fase B — 1 instância por serviço (o ponto crítico)

**Problema:** `formly-web` e `brand-hub` têm DUAS instâncias no Cloud Run:
`-rj` (southamerica-east1, atualizada) e `-ue` (us-east1, ANTIGA — formly-web-ue
está 298 commits atrás). Causa: Cloud Run só aceita domain mapping em us-east1;
criou-se cópia lá. O domínio serve o `-ue` velho. Correção D-24:

1. **Cloudflare na frente** (formly.ink): DNS `proxied=True` + CNAME para o
   serviço BR (`formly-web-...-rj.a.run.app`) + **Origin Rule** reescrevendo
   Host header → run.app BR. Token em `~/.cloudflare/token`, zone formly.ink
   ativa (`144803591b8a4a559e074872614d2e09`). ⚠️ Origin Rule via API exige
   token com `Transform Rules:Edit` (senão 10405). Alternativa: Worker free.
2. **Verificar** que `https://formly.ink` serve a versão nova (ETag/HTML).
3. **Remover os serviços `-ue`**: `gcloud run services delete formly-web-ue`
   e `brand-hub-ue` (projeto `blu-control-panel`, região `us-east1`).
   ⚠️ gcloud roda no MAC do dono — gerar comandos prontos, um por linha.
4. Repetir para `app.mcp-brain.com` se tiver instância duplicada (verificar).

## Fase C — Atualizar deploys (dono roda no Mac)

Estado atual (do diagnóstico 2026-08-20): formly-api 1 atrás, memory_api 1-2
atrás (#312 extração LLM + #316 LGPD), auth_service 4 atrás (#294/#296/#315),
backend_api 13 atrás (parsers #25, LGPD #316). E2E existentes:
`scripts/e2e-308.sh` + `e2e-fatos-ricos.sh` (memory_api, rodam no Mac com SSM).

Sequência (dono roda no Terminal GUI do Mac, linha a linha — zsh mastiga blocos):
```bash
cd ~/Documents/GitHub/monorepo && git fetch origin && git checkout main && git pull
# E2E baseline (antes)
./scripts/e2e-308.sh && ./e2e-fatos-ricos.sh
# Deploy (após merge dos PRs pendentes)
make deploy SERVICOS="formly_api formly_web agents_api backend_api routines_api tool_pool_api auth_service"
# memory_api (VM EC2 — fluxo ECR+SSM separado, ver skill)
# Verificação
./scripts/check-versions.sh
```

## Fase D — Release + rotina

1. E2E pós-deploy (mesma bateria) → tag `v2026.08.1` na main
2. Procedimento de deploy completo em `01-procedimentos/deploy/`
3. Rotina semanal no inventário de crons (6ª: `check-versions.sh` + E2E)

## Regras de ouro (desta empresa)

- **gcloud/AWS deploy rodam no Mac do dono** — a EC2 do Hermes NÃO tem gcloud e
  a AWS CLI lá tem credenciais válidas (profile `default` = MantleApiKey-wy0kn5mp,
  conta 655177116015) mas deploy é do Mac. Dar comandos prontos linha a linha.
- **Nunca colar blocos com `#`, `; \` ou aspas aninhadas no chat pro dono** —
  zsh mastiga. Script `.sh` via write_file + `bash /tmp/x.sh`, ou um comando por
  mensagem.
- **Autorização explícita antes de deploy com secrets** — apresentar o comando
  completo e pedir OK.
- **Verificar produção pelo código da MAIN** (`git show origin/main:<path>`),
  nunca pelo working tree local.
- **`make deploy` NÃO cobre auth_service** — usar `make auth-service-deploy`.
- **Memory_api roda na VM EC2** (i-0919e237f715f19ec, só SSM) — não é Cloud Run.

## Retomar F2 (assistente pessoal) — SÓ se o dono pedir

Para religar o pipeline da F2: remover `stop_after_phase` do
`~/.hermes/state/assistente_queue.json` e `cronjob action=resume` no
`assistente-pessoal-fila` (ebf8c83441e4). Specs em
`/home/ec2-user/monorepo/scripts/prompts/issue-*.md`.

## Entregável da sessão

Ao final: relatório com (a) serviços unificados (1 instância), (b) todos os
deploys alinhados com a main (check-versions.sh ✅), (c) E2E verdes, (d) tag
criada, (e) procedimento documentado.
