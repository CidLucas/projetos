# 🎯 Estratégia — Requisitos Blue V3

> Última atualização: 2026-07-30
> Status: 🟡 Em andamento
> Fonte: `apps/blu_web/src/pages/app/EstrategiaRoom.tsx` (1316 linhas)

---

## 1. Visão Geral

**Objetivo:** Sala de estratégia com 4 abas: objetivos, documentos, conhecimento e configuração de rotinas. Onde o usuário gerencia o planejamento estratégico com IA.

**Contexto:** Central de inteligência combinando OKRs, documentos estruturados, base de conhecimento e rotinas automatizadas.

**Relação com outras páginas:**
- **Home:** insights da estratégia no dashboard
- **Chat:** análise de documentos pode ser acionada via chat
- **Biblioteca:** tipos de documento compartilhados

---

## 2. Estrutura de Elementos (Front-End)

### 2.1 Tabs de navegação
- **Tipo:** tabs horizontais
- **Posição:** topo da área de conteúdo
- **Conteúdo/Dados:** 4 abas — Objetivos, Documentos, Conhecimento, Config
- **Interações:** clique alterna entre abas
- **Condições de visibilidade:** sempre visível

### 2.2 Tab: Objetivos
- **Tipo:** painel de métricas + cards de objetivo
- **Conteúdo/Dados:** KPIs estratégicos (Sparkline), contexto histórico, aprovações pendentes do agente estratégia
- **Interações:** aprovar/rejeitar/adiar decisões, visualizar métricas

### 2.3 Tab: Documentos
- **Tipo:** editor + seletor de template + lista de recentes
- **Conteúdo/Dados:** 8 templates inline + documentos recentes do cliente + editor markdown
- **Interações:**
  - "Novo Documento" → modal de seleção de template
  - Selecionar template → instancia documento com conteúdo padrão
  - Editar → salvar → ver diff entre original e editado
- **Estados visuais:** modal de templates com ícones (📊💰📋🎯✅📝🔍🧾), editor com toolbar

### 2.4 Tab: Conhecimento
- **Tipo:** árvore de pastas + lista de documentos
- **Conteúdo/Dados:** estrutura: Todos, Estratégia→OKRs/Planejamento, Relatórios, Jurídico, Pesquisa
- **Interações:** navegar na árvore, clicar em documento para abrir

### 2.5 Tab: Config
- **Tipo:** painel de rotinas
- **Conteúdo/Dados:** RoutineConfigSection do agente estratégia
- **Interações:** ativar/desativar rotinas, configurar parâmetros

### 2.6 Painel lateral de métricas
- **Tipo:** painel colapsável com resize (CollapsiblePanel + RColResizeHandle)
- **Posição:** coluna direita redimensionável
- **Conteúdo/Dados:** métricas de contexto, relatórios de contexto, download

---

## 3. Fluxos de Processo

### 3.1 Criação de Documento (a partir de template)
```
Usuário na tab "Documentos" → clica "Novo Documento"
  │
  ▼
Modal com 8 templates:
  📊 Fechamento Mensal | 💰 Fluxo de Caixa | 📋 Proposta Comercial
  🎯 Plano Estratégico | ✅ OKR | 📝 Ata de Reunião | 🔍 SWOT | 🧾 Invoice
  │
  ▼
Seleciona template → documento instanciado com conteúdo padrão
  │
  ▼
Editor → edita → salva → documento na lista de recentes
```

### 3.2 Templates disponíveis
- `fechamento-mensal`: receitas, despesas, KPIs
- `fluxo-caixa`: DCF (operacional, investimento, financiamento)
- `proposta-comercial`: escopo, investimento, condições
- `plano-estrategico`: visão, missão, objetivos, KPIs
- `okr`: Objectives & Key Results
- `ata-reuniao`: pauta, discussões, ações
- `swot`: forças, fraquezas, oportunidades, ameaças
- `invoice`: fatura comercial

---

## 4. Regras de Negócio

| # | Regra |
|---|---|
| R1 | Documentos são criados a partir de templates (não há "documento em branco") |
| R2 | Cada template tem estrutura Markdown predefinida |
| R3 | Documentos salvos são associados a uma pasta (folder) |
| R4 | Diff entre versão original e editada é exibido antes de salvar |

---

## 5. Integrações

| Integração | Tipo | Descrição |
|---|---|---|
| fetchDocTemplates | Query | Templates disponíveis |
| fetchRecentDocuments | Query | Documentos recentes do cliente |
| createDocument | Mutation | Instanciar documento a partir de template |
| saveDocument | Mutation | Salvar alterações |
| fetchEstrategiaHistory | Query | Histórico da estratégia |
| fetchInsights | Query | Insights do agente estratégia |
| getContextMetrics | Query | Métricas de contexto |

---

## 6. Cenários de Teste

### Happy Path
- [ ] Criar documento a partir de template → editar → salvar
- [ ] Navegar entre as 4 tabs
- [ ] Visualizar diff entre original e editado

### Edge Cases
- [ ] Salvar documento sem alterações (diff vazio)
- [ ] Template com conteúdo muito longo
- [ ] Navegar na árvore de pastas com muitos documentos
