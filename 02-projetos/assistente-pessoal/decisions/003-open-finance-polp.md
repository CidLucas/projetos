# ADR-003 — Open Finance (Polp) para controle financeiro e classificação de gastos

- **Data:** 2026-08-20
- **Status:** Aceita
- **Decisor:** Lucas Cid

## Contexto

O assistente pessoal precisa de controle financeiro: saldos, transações e
**classificação de gastos**. O monorepo **já tem** integração Open Finance via
Polp (compatível com Pluggy): `backend_api` faz connect/sync/webhook com
upserts em `polp_accounts`, `polp_transactions` (com `category` e `merchant`),
`polp_bills`, `polp_integrations`, `polp_webhook_events`; `routines_api` já tem
FIN-01 (cash position) e FIN-02 (gastos agregados por categoria); o tool_pool
tem o `polp_webhook_router`.

## Decisão

1. **Reusar a integração Polp existente** — o assistente **não cria cliente
   Polp novo**. Consome os dados já sincronizados via tools (MCP) no tool_pool
   ou via routines, com tenant_id como fronteira.
2. **Classificação de gastos** em duas camadas:
   - Categoria que o Polp já entrega (`polp_transactions.category`) como base;
   - **Reclassificação/refino por LLM** quando a categoria vier vazia/genérica
     ou o usuário pedir ("quanto gastei em restaurantes?"), rodando sobre as
     transações do tenant.
3. **Consultas financeiras como tools do agente**: saldo, transações por
   período/categoria, gastos agregados — mesma assinatura FIN-01/FIN-02 do
   routines, expostas ao assistente.
4. **LGPD aplicado**: dados financeiros são dados pessoais → leitura só com o
   tenant autenticado (regra F-20), nunca em logs, lib `blu_lgpd` no caminho.

## Alternativas consideradas

| Alternativa | Por que foi recusada |
|---|---|
| Integração Polp nova no assistente | Duplica connect/sync/webhook já prontos; dados já estão no banco |
| Agregador diferente (Pluggy direto, Belvo, Prometeo) | Polp já está integrado e em produção no Blu; migrar é custo sem ganho no MVP |
| Categoria só do Polp, sem LLM | `category` do Polp é genérica/ausente em muitas transações; classificação por LLM é o diferencial pedido |

## Consequências

- **Positivas:** zero trabalho de sync bancário; dados financeiros já fluem
  (webhook do Polp → banco); classificação por LLM roda sobre dados reais.
- **Negativas:** dependência do estado da integração Polp do Blu (se cair,
  dados não atualizam — mas o assistente lê o banco, não a API); qualidade da
  categorização depende do prompt/refino.

## Links

- Código-fonte: `services/backend_api/src/backend_api/api/integrations/polp.py`
  · `services/tool_pool_api/src/tool_pool_api/api/polp_webhook_router.py` ·
  `services/routines_api/src/routines_api/core/functions.py` (FIN-01/FIN-02)
- Tabelas: `polp_accounts`, `polp_transactions`, `polp_bills`,
  `polp_integrations`, `polp_webhook_events`
