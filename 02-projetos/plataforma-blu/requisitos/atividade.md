# 🔔 Atividade — Requisitos Blue V3

> Última atualização: 2026-07-30
> Status: 🟡 Em andamento
> Fonte: `apps/blu_web/src/pages/app/AtividadeScreen.tsx` (204 linhas)

---

## 1. Visão Geral

**Objetivo:** Feed de log em tempo real de todos os agentes. Centro de monitoramento de atividades, decisões e saúde do sistema.

**Contexto:** Central de controle onde o usuário vê tudo que acontece: sessões, ingestões, decisões pendentes, alertas.

**Relação com outras páginas:**
- **Home:** mesmos dados em formato compacto
- **Admin:** alertas de sistema podem exigir ação administrativa
- **Páginas de agente:** link rápido pelo painel "Agentes ativos"

---

## 2. Estrutura de Elementos (Front-End)

### 2.1 Header da página
- **Tipo:** barra de título
- **Conteúdo/Dados:** 🔔 + "Atividade" + "Log em tempo real de todos os agentes" + botão "← Início"

### 2.2 Feed de Atividades (Principal)
- **Tipo:** lista cronológica
- **Posição:** coluna esquerda (~70%)
- **Conteúdo/Dados:** cada linha = timestamp + dot colorido (kind) + título + badge severidade
  - Kinds: agent_session (azul), ingestion (teal), rfq (amarelo), upload (rosa)
  - Severidades: error (Urgente), warning (Atenção), info (Info)
- **Estados visuais:** loading, vazio "Nenhuma atividade registrada"

### 2.3 Painel "Agentes Ativos"
- **Tipo:** lista de cards de agente
- **Posição:** coluna direita (superior)
- **Conteúdo/Dados:** 6 agentes: 🛒 Compras, 📊 Financeiro, 📅 Agenda, ✍️ Documentos, 🎯 Estratégia, 👥 Clientes — cada um com contagem de pendências
- **Interações:** clique → navega para a página do agente

### 2.4 Painel "Resumo do Dia"
- **Tipo:** cards de métricas
- **Posição:** coluna direita (inferior)
- **Conteúdo/Dados:** Decisões pendentes, Aprovadas hoje, Ações do agente, NPS (colorido)
- **Interações:** somente leitura

### 2.5 Barra Inferior (Bottom Strip)
- **Tipo:** chips de status
- **Posição:** inferior da página
- **Conteúdo/Dados:** indicador urgência (🔴/🟢), alertas sistema (⚠️/💡), decisões pendentes (🟡), concluídas (🟢), chip numérico "🔔 Hoje"

---

## 3. Fluxos de Processo

```
Usuário acessa Atividade → vê feed em tempo real
  ├─ Identifica alertas (error/warning)
  ├─ Vê pendências por agente
  ├─ Clica em agente → navega para página específica
  └─ Acompanha resumo do dia
```

---

## 4. Regras de Negócio

| # | Regra |
|---|---|
| R1 | Decisões urgentes +2h são destacadas na barra inferior |
| R2 | Agentes com 0 pendências mostram "Nada urgente" |
| R3 | NPS colorido: verde ≥50, amarelo ≥0, vermelho <0 |

---

## 5. Integrações

| Integração | Tipo | Descrição |
|---|---|---|
| useRecentActivity | Query | Feed de atividades (últimos 20) |
| useDayStats | Query | Estatísticas do dia |
| usePendingApprovals | Query | Aprovações pendentes |
| useAgentRunsToday | Query | Execuções de agentes hoje |
| useNpsScore | Query | NPS do cliente |
| usePendencias | Query | Pendências do sistema |

---

## 6. Cenários de Teste

### Happy Path
- [ ] Ver feed com múltiplos tipos de atividade
- [ ] Clicar em agente → navegar
- [ ] Ver resumo do dia com métricas

### Edge Cases
- [ ] Feed vazio
- [ ] Múltiplas decisões urgentes
- [ ] NPS negativo
