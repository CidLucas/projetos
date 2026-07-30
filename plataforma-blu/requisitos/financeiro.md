# 📊 Financeiro — Requisitos Blue V3

> Última atualização: 2026-07-30 | Status: 🟡 Em andamento
> Fonte: `apps/blu_web/src/pages/app/FinanceiroRoom.tsx` (934 linhas)

---

## 1. Visão Geral

**Objetivo:** Gestão financeira com IA — transações bancárias (Polp/Open Finance), decisões do agente financeiro, tarefas e rotinas.

**Contexto:** O agente Financeiro analisa transações, gera insights e propõe decisões (aprovações de pagamento, categorização, alertas de fluxo de caixa).

**Relação com outras páginas:** Home (KPIs), Admin (conexão bancos), Estratégia (métricas financeiras).

---

## 2. Estrutura de Elementos (Front-End)

### 2.1 Tabs de navegação
- **Tipo:** tabs horizontais
- **Conteúdo/Dados:** 4 abas — Decisões, Transações, Tarefas, Config

### 2.2 Tab: Decisões
- **Tipo:** lista de cards de aprovação
- **Conteúdo/Dados:** pagamentos a aprovar, alertas, sugestões
- **Interações:** aprovar, rejeitar, adiar (snooze)

### 2.3 Tab: Transações
- **Tipo:** tabela de transações
- **Conteúdo/Dados:** transações Polp — descrição, valor, categoria, data, banco
- **Interações:** filtrar, categorizar
- **Estados visuais:** ícones por serviço (🎬 Netflix, 🎵 Spotify, 🚗 Uber, 🍕 iFood, 📦 Amazon...) e banco (🟣 Itaú/Nubank, 🏛 Bradesco...)

### 2.4 Tab: Tarefas
- **Tipo:** RoutineExecutionFeed
- **Conteúdo/Dados:** tarefas executadas pelo agente financeiro

### 2.5 Tab: Config
- **Tipo:** painel de configuração
- **Conteúdo/Dados:** RoutineConfigSection + AnalyticsPanel (30d/90d/1y)
- **Interações:** configurar rotinas, selecionar período de análise

### 2.6 Painel de KPIs
- **Tipo:** métricas + sparklines
- **Conteúdo/Dados:** indicadores financeiros formatados (compacto BRL)

---

## 3. Fluxos de Processo

### 3.1 Categorização
```
Agente analisa transação → propõe categoria
  │
  ▼
Usuário aceita ou redefine → categoria salva
```

---

## 4. Regras de Negócio

| # | Regra |
|---|---|
| R1 | Conexão bancária via Polp (Open Finance) — múltiplos bancos |
| R2 | Ícone automático por serviço conhecido (regex match) |
| R3 | Métricas em formato compacto (K, M) |

---

## 5. Integrações

| Integração | Tipo | Descrição |
|---|---|---|
| fetchConnectedAccounts | Query | Contas bancárias |
| fetchPolpTransactions | Query | Transações financeiras |
| fetchPolpBills | Query | Boletos/contas |
| getFinanceIndicators | Query | KPIs financeiros |
| fetchApprovalsByAgent | Query | Decisões pendentes |
| createPaymentApproval | Mutation | Criar aprovação de pagamento |

---

## 6. Cenários de Teste

- [ ] Ver transações categorizadas com ícones
- [ ] Aprovar decisão de pagamento
- [ ] Nenhuma conta conectada → estado vazio
