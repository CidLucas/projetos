# 👥 Clientes — Requisitos Blue V3

> Última atualização: 2026-07-30 | Status: 🟡 Em andamento
> Fonte: `apps/blu_web/src/pages/app/ClientesRoom.tsx` (561 linhas)

---

## 1. Visão Geral

**Objetivo:** Gestão de relacionamento com clientes com IA — segmentação, follow-ups, histórico e análises.

**Contexto:** O agente Clientes analisa CRM, identifica segmentos, sugere follow-ups e gera insights comerciais.

**Relação com outras páginas:** Home (KPIs comerciais), Estratégia (métricas de clientes).

---

## 2. Estrutura de Elementos (Front-End)

### 2.1 Tabs de navegação
- **Tipo:** tabs horizontais
- **Conteúdo/Dados:** 4 abas — Follow-up, Ativos, Histórico, Config

### 2.2 Tab: Follow-up
- **Tipo:** lista de cards
- **Conteúdo/Dados:** clientes que precisam de ação — último contato relativo (hoje, ontem, Xd atrás)
- **Interações:** expandir, marcar como concluído

### 2.3 Tab: Ativos
- **Tipo:** tabela paginada
- **Conteúdo/Dados:** top customers — nome, segmento, valor, recência
- **Interações:** paginação (8 por página)

### 2.4 Tab: Histórico
- **Tipo:** lista cronológica
- **Conteúdo/Dados:** histórico de interações com clientes

### 2.5 Tab: Config
- **Tipo:** painel de rotinas + AnalyticsPanel (30d/90d/1y)

### 2.6 Painel de Segmentos
- **Tipo:** cards de segmento identificados pela IA

---

## 3. Fluxos de Processo

```
Agente identifica cliente que precisa de follow-up
  → Sugestão aparece na tab Follow-up
  → Usuário revisa e conclui
```

---

## 4. Regras de Negócio

| # | Regra |
|---|---|
| R1 | Follow-ups exibidos com tempo relativo |
| R2 | Clientes paginados (8 por página) |
| R3 | Segmentos gerados automaticamente pela IA |

---

## 5. Integrações

| Integração | Tipo | Descrição |
|---|---|---|
| fetchCustomerSegments | Query | Segmentos de cliente |
| fetchTopCustomers | Query | Top clientes (paginado) |
| fetchClientesHistory | Query | Histórico |
| getCommercialIndicators | Query | KPIs comerciais |

---

## 6. Cenários de Teste

- [ ] Ver follow-ups pendentes
- [ ] Navegar entre páginas de clientes
- [ ] Nenhum cliente → estado vazio
