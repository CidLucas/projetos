# 🖥️ AgentOps — Requisitos Blue V3

> Última atualização: 2026-07-30 | Status: 🟡 Em andamento
> Fonte: `apps/blu_web/src/pages/app/AgentOpsRoom.tsx` (489 linhas)
> Restrição: visível apenas para `tier === 'ADMIN'`

---

## 1. Visão Geral

**Objetivo:** Painel de operações para monitorar sessões de agentes, jobs de sincronização e credenciais. Uso interno — tier ADMIN.

**Contexto:** Ferramenta de debugging e monitoramento da infraestrutura de agentes.

**Relação com outras páginas:** Atividade (visão alto nível das mesmas sessões), Admin (credenciais).

---

## 2. Estrutura de Elementos (Front-End)

### 2.1 Lista de Sessões de Agentes
- **Tipo:** tabela expansível
- **Conteúdo/Dados:** cada sessão — ID curto (primeiro segmento UUID), status (completed/success/ready/pending/running/failed/error), duração, data
- **Interações:** expandir para ver mensagens
- **Estados visuais:** StatusPill colorida: verde (completed/success/active), amarelo (pending/running), vermelho (failed/error), cinza (inactive); ProgressBar (%)

### 2.2 Sync Jobs
- **Tipo:** lista de jobs com status e progresso
- **Interações:** retry job (mutation)

### 2.3 Credenciais
- **Tipo:** lista de credenciais de integração
- **Interações:** ativar/desativar (toggle)

---

## 3. Fluxos de Processo

### 3.1 Debugging
```
Admin acessa AgentOps → vê sessões com status
  → Expande sessão com erro → vê mensagens trocadas
  → Identifica problema → age no backend
```

---

## 4. Regras de Negócio

| # | Regra |
|---|---|
| R1 | Visível apenas para `tier === 'ADMIN'` |
| R2 | ID truncado (primeiro segmento UUID) |
| R3 | Duração: <60s → "Xs", ≥60s → "Xm Ys" |

---

## 5. Integrações

| Integração | Tipo | Descrição |
|---|---|---|
| fetchAgentSessions | Query | Sessões de agentes |
| fetchSessionMessages | Query | Mensagens de uma sessão |
| fetchSyncJobs | Query | Jobs de sincronização |
| retryJob | Mutation | Retentar job com erro |
| fetchCredentials / toggleCredential | Query/Mutation | Gestão de credenciais |

---

## 6. Cenários de Teste

- [ ] Ver sessões com status coloridos
- [ ] Expandir sessão e ver mensagens
- [ ] Retry job falho
- [ ] Nenhuma sessão → estado vazio
- [ ] Não-ADMIN → não vê a página
