# 🚀 Plano — Versão estável e atualizada (Deep Blue)

> **Status:** FECHADO (2026-08-20, aprovação do dono)
> **Objetivo:** 1 instância por serviço, deploy verificável, E2E como gate.

---

## Diagnóstico que motivou

| Serviço | Deploy | Main | Status |
|---|---|---|---|
| memory_api (VM) | sha-d8ab2c6 | a1234d0 | ❌ 1-2 commits atrás (#312, #316) |
| auth_service/brain-web | sha-67742e1 | a1234d0 | 🔴 4 commits atrás (#294×2, #296, #315) |
| backend_api | sha-ddc03988 | a1234d0 | 🔴 13 commits atrás (parsers #25, LGPD #316) |
| formly-api | sha-0acf36d0 | a1234d0 | ⚠️ 1 atrás (#299) |
| formly-web **-ue** (us-east1) | sha-6377d11 | a1234d0 | 🔴 **298 commits atrás** (instância duplicada!) |
| tool_pool_api / agents_api | sha-ddc03988 | a1234d0 | ⚠️ 1-2 atrás |

**Causa raiz da duplicação (-rj / -ue):** Cloud Run só aceita domain mapping
(domínio custom) em `us-east1` → criou-se cópia do serviço lá. O `make deploy`
atualiza o BR, o domínio serve o `-ue` velho. **Correção D-24 (18/08):**
Cloudflare na frente + 1 instância (BR) + remover o `-ue`.

## Fases

### Fase A — Instrumentar versão ✅ (em implementação)
- [x] `GIT_SHA` no health do formly-api (`/health` → `{sha}`)
- [x] `sha` no healthz da memory_api
- [x] `/api/health` com SHA no brain-web (auth_service)
- [x] `scripts/check-versions.sh` (compara deploy vs main)
- [ ] Deploy.sh injeta `GIT_SHA` (build-time) nos 3 serviços

### Fase B — 1 instância por serviço (Cloudflare + remover -ue)
- [ ] CF proxy (proxied=True) para formly.ink → serviço BR
- [ ] Origin Rule no CF (Host header → run.app BR)
- [ ] Remover serviços `-ue`: formly-web-ue, brand-hub-ue
- [ ] Repetir para o domínio do brain (app.mcp-brain.com) se aplicável

### Fase C — Deploy + E2E (dono roda no Mac)
- [ ] E2E baseline (antes): e2e-fatos-ricos.sh, e2e-308.sh, smoke formly/brain
- [ ] `make deploy` (formly, backend, auth_service, etc.)
- [ ] E2E pós-deploy (mesma bateria)
- [ ] `check-versions.sh` → "✅ todos alinhados"

### Fase D — Release estável
- [ ] Tag `v2026.08.1` na main
- [ ] Procedimento de deploy em `01-procedimentos/deploy/`
- [ ] Rotina semanal no inventário de crons (6ª: check + E2E)

## Comandos (dono, Mac)

```bash
# 1. E2E memory_api (antes do deploy)
cd ~/Documents/GitHub/monorepo && ./scripts/e2e-308.sh && ./e2e-fatos-ricos.sh

# 2. Deploy (após merge das branches de instrumentação)
make deploy SERVICOS="formly_api formly_web agents_api backend_api routines_api tool_pool_api auth_service"

# 3. Verificar alinhamento
./scripts/check-versions.sh
```
