# 🛒 Compras — Requisitos Blue V3

> Última atualização: 2026-07-30 | Status: 🟡 Em andamento
> Fonte: `apps/blu_web/src/pages/app/ComprasRoom.tsx` (391 linhas)

---

## 1. Visão Geral

**Objetivo:** Gestão de compras e fornecedores com IA — decisões de compra, tarefas, histórico e configuração.

**Contexto:** O agente Compras analisa cotações, fornecedores e histórico para sugerir decisões.

**Relação com outras páginas:** Home (supply indicators), Financeiro (compras aprovadas → transações).

---

## 2. Estrutura de Elementos (Front-End)

### 2.1 Tabs de navegação
- **Tipo:** tabs horizontais
- **Conteúdo/Dados:** 4 abas — Decisões, Tarefas, Histórico, Config

### 2.2 Tab: Decisões
- **Tipo:** lista de DecisionCards
- **Conteúdo/Dados:** aprovações de compra pendentes — fornecedor, valor, justificativa
- **Interações:** aprovar, rejeitar, adiar

### 2.3 Tab: Tarefas
- **Tipo:** RoutineExecutionFeed
- **Conteúdo/Dados:** tarefas executadas pelo agente compras

### 2.4 Tab: Histórico
- **Tipo:** lista cronológica de compras

### 2.5 Tab: Config
- **Tipo:** RoutineConfigSection + AnalyticsPanel (30d/90d/1y)

### 2.6 Lista de Fornecedores
- **Tipo:** tabela paginada
- **Conteúdo/Dados:** fornecedores — nome, rating (★☆☆☆☆), total comprado
- **Interações:** paginação (8 por página)

---

## 3. Fluxos de Processo

```
Agente analisa cotação → propõe compra
  → Decisão aparece na tab Decisões
  → Usuário aprova/rejeita/adia
```

---

## 4. Regras de Negócio

| # | Regra |
|---|---|
| R1 | Fornecedores com rating 1-5 estrelas |
| R2 | Fornecedores paginados (8 por página) |
| R3 | Decisões de compra exigem aprovação explícita |

---

## 5. Integrações

| Integração | Tipo | Descrição |
|---|---|---|
| fetchSuppliers | Query | Lista de fornecedores |
| fetchComprasHistory | Query | Histórico de compras |
| getSupplyIndicators | Query | Indicadores de supply |

---

## 6. Cenários de Teste

- [ ] Aprovar decisão de compra
- [ ] Ver fornecedores com rating
- [ ] Nenhum fornecedor → estado vazio
