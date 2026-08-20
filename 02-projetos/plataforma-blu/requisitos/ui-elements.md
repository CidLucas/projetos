# 🧩 Elementos de UI — Blue V3 (catálogo visual)

> Extraído do código em `CidLucas/monorepo` → `apps/blu_web/src/pages/`
> Aqui só tem **o que existe**. Sem opinião. Você comenta o que espera de cada um.

---

## 🖼️ Shell (Layout Global)

| Elemento | Tipo | Onde | Descrição no código |
|---|---|---|---|
| Topbar | barra fixa | topo | logo + toggle tema (dark/light) + busca |
| Sidebar (desktop) | nav vertical | esquerda | 10 ícones: 🏠🛒📊📅🎯👥📚🔔⚙️🖥️ |
| Sidebar inferior | nav agrupada | esquerda (rodapé) | 🔔 Atividade, ⚙️ Admin (owner), 🖥️ AgentOps (ADMIN) |
| Mobile nav | barra inferior | mobile | botão hamburguer → overlay com grid |
| SpotlightSearch | modal | centro (Ctrl+K) | campo busca + resultados |
| ChatPanel | painel lateral | overlay direita | chat com agentes |
| FirstRunOverlay | overlay | tela cheia | tutorial primeiro acesso |
| ToastContainer | notificações | canto fixo | sucesso/erro/info |
| EditorOverlay | overlay | tela cheia | editor de documento |

---

## 🏠 Home

| Elemento | Tipo | Detalhes |
|---|---|---|
| Header | barra | 🏠 "Home" / "Visão geral do Blu" |
| Botão "+ Nova Missão" | btn primário | abre chat com prompt |
| Botão "← Início" | btn secundário | (redundante na home) |
| **Painel "Decidir Agora"** | cards | decisões pendentes de todos os agentes |
| ↳ DecisionCard | card expansível | aprovar / rejeitar / adiar (snooze) |
| ↳ Badge de prioridade | badge | "Urgente" / "Amanhã" |
| ↳ Estado vazio | empty | "Tudo em dia ✓" |
| **CollapsiblePanel "Plano de Hoje"** | painel colapsável | eventos de hoje |
| ↳ Evento | linha expansível | hora, dot colorido, título, ▶ expandir |
| ↳ Detalhe expandido | painel | título, 🕐 horário, 📍 local, 👥 participantes |
| ↳ Botão "📹 Entrar" | link externo | Google Meet (hangoutLink) |
| ↳ Botão "💬 Preparar pauta" | btn ghost | abre chat |
| ↳ Botão "Conectar Google Calendar" | btn primário | se não conectado |
| **CollapsiblePanel "Visão da Semana"** | painel colapsável | 5 dias úteis |
| ↳ Dia | linha expansível | Seg..Sex, descrição, contador eventos |
| ↳ Detalhe expandido | lista | eventos do dia com hora e dot |
| **Bottom Strip** | barra horizontal | |
| ↳ Insight chips | chips clicáveis | ⚠️/💡/📈 + tag (financeiro/compras/outros) + título |
| ↳ InsightPopover | popover fixed | 3 ações: Explicar, Como agir?, Analisar tendência |
| ↳ Números chip | chip | 📊 Faturamento (K), Margem (%), Clientes (nº) |
| ↳ Rotinas chip | chip | rotinas ativas do cliente |
| **Coluna direita** | painel redimensionável | RColResizeHandle + CollapsiblePanels |

---

## 🎯 Estratégia

| Elemento | Tipo | Detalhes |
|---|---|---|
| Header | barra | 🎯 "Estratégia" / "Análises, KPIs e planejamento" |
| Botão "+ Nova Análise" | btn primário | abre chat |
| **Tabs** | tabs horizontais | Objetivos, Documentos, Conhecimento, Config |
| ↳ Tab Objetivos | tab | badge com contagem de pendências |
| **Tab: Objetivos** | | |
| ↳ ApprovalCard | card | aprovações de objetivos (aprovar/rejeitar/adiar) |
| **Tab: Documentos** | | |
| ↳ Sidebar de docs | coluna 230px | lista de documentos recentes + botão |
| ↳ Botão "+ Novo Documento" | btn primário | abre modal de templates |
| ↳ Modal "Novo Documento" | modal | 8 templates em grid + "Em branco" |
| ↳ Templates | cards no modal | 📊 Fechamento Mensal, 💰 Fluxo de Caixa, 📋 Proposta Comercial, 🎯 Plano Estratégico, ✅ OKR, 📝 Ata de Reunião, 🔍 SWOT, 🧾 Invoice |
| ↳ Editor | contentEditable div | markdown renderizado como HTML |
| ↳ Botão "Salvar" | btn | salva documento |
| ↳ Diff viewer | painel | mostra alterações (original vs editado) |
| **Tab: Conhecimento** | | |
| ↳ Árvore de pastas | nav lateral | Todos, Estratégia→OKRs+Planejamento, Relatórios, Jurídico, Pesquisa |
| ↳ Lista de docs | cards | docs filtrados por pasta |
| **Tab: Config** | | |
| ↳ RoutineConfigSection | painel | rotinas do agente estratégia |
| **Painel lateral** | coluna direita | CollapsiblePanel com métricas de contexto + relatórios |

---

## 📊 Financeiro

| Elemento | Tipo | Detalhes |
|---|---|---|
| Header | barra | 📊 "Financeiro" / "Fluxo de caixa, pagamentos e relatórios" |
| Botão "+ Nova Missão" | btn primário | abre chat |
| **Tabs** | tabs | Decisões, Transações, Tarefas, Config |
| ↳ Tab Decisões | tab | badge com contagem |
| ↳ Tab Transações | tab | badge com contagem de faturas abertas |
| **Tab: Decisões** | | |
| ↳ ApprovalCard | card expansível | igual padrão (aprovar/rejeitar/adiar) |
| **Tab: Transações** | | |
| ↳ Filtro de período | btn group | Hoje, 7 dias, 30 dias, Tudo |
| ↳ BillRow | card | 💳 nome cartão, vencimento, valor, status |
| ↳ Status vencimento | texto colorido | "X dias", "vence hoje", "X dias atrasada" (urg) |
| ↳ Botão "Pagar fatura" | btn | cria aprovação de pagamento |
| ↳ Transação | linha | ícone (🎬🍕🚗...), descrição, valor, categoria |
| ↳ Editar categoria | inline | dropdown de categorias (Restaurante, Transporte, Saúde...) |
| **Tab: Tarefas** | | |
| ↳ RoutineExecutionFeed | feed | tarefas executadas pelo agente |
| **Tab: Config** | | |
| ↳ RoutineConfigSection | painel | rotinas financeiras |
| **Painel lateral** | coluna direita | CollapsiblePanel com KPIs + AnalyticsPanel (30d/90d/1y) |

---

## 👥 Clientes

| Elemento | Tipo | Detalhes |
|---|---|---|
| Header | barra | 👥 "Clientes" |
| **Tabs** | tabs | Follow-up, Ativos, Histórico, Config |
| **Tab: Follow-up** | cards | clientes que precisam de ação, tempo relativo |
| **Tab: Ativos** | tabela paginada | top customers (8/página) |
| **Tab: Histórico** | lista | interações passadas |
| **Tab: Config** | painel | rotinas + AnalyticsPanel (30d/90d/1y) |
| **Painel lateral** | coluna direita | CollapsiblePanel + segmentos |

---

## 🛒 Compras

| Elemento | Tipo | Detalhes |
|---|---|---|
| Header | barra | 🛒 "Compras" |
| **Tabs** | tabs | Decisões, Tarefas, Histórico, Config |
| **Tab: Decisões** | cards | DecisionCard padrão (aprovar/rejeitar/adiar) |
| **Tab: Tarefas** | feed | RoutineExecutionFeed |
| **Tab: Histórico** | lista | compras passadas |
| **Tab: Config** | painel | rotinas + AnalyticsPanel (30d/90d/1y) |
| **Fornecedores** | tabela paginada | nome, rating ★☆☆☆☆, total (8/página) |
| **Painel lateral** | coluna direita | CollapsiblePanel |

---

## 📅 Agenda

| Elemento | Tipo | Detalhes |
|---|---|---|
| Header | barra | 📅 "Agenda" / "Reuniões, rotinas e planejamento semanal" |
| Botão "+ Novo evento" | btn primário | abre chat |
| **Tabs** | tabs | Decisões, Visão Mensal, Hoje, Pendentes, Histórico, Config |
| ↳ Tab Decisões | tab | badge com contagem |
| ↳ Tab Pendentes | tab | badge com contagem |
| **Tab: Visão Mensal** | | |
| ↳ MonthlyGantt | gráfico Gantt | tarefas + eventos no mês, barras coloridas (approval=laranja, calendar=azul) |
| **Tab: Hoje** | | |
| ↳ Evento do dia | card expansível | hora, dot colorido, título, status "Pendente" |
| ↳ Detalhe expandido | painel | 📍 local, 👤 contato, 📝 observação |
| ↳ Botão "✓ Confirmar" | btn primário | abre chat |
| ↳ Botão "↻ Remarcar" | btn ghost | abre chat |
| ↳ EmptyState | vazio | "Nenhum evento hoje" |
| **Tab: Pendentes** | cards | aprovações pendentes (aprovar/depois) |
| **Tab: Histórico** | lista | ações passadas (aprovado/rejeitado) |
| **Tab: Config** | painel | RoutineConfigSection |
| **Painel lateral** | coluna direita | CollapsiblePanel |

---

## 📚 Biblioteca (Business Memory)

| Elemento | Tipo | Detalhes |
|---|---|---|
| Header | barra | 📚 "Business Memory" |
| **Filtro** | dropdown | Entity type: Todos, Snapshot, Rotina, Skill, Resultado de Agente |
| **Lista de records** | tabela expansível | |
| ↳ Linha | row | Entity Type (badge colorido), Entity Name, Key, Confidence (%), data |
| ↳ Detalhe expandido | grid 2 colunas | Entity Type, Entity Name, Key, Confidence, Created, Updated, Content |
| ↳ Badge tipo | badge | snapshot=roxo, routine=verde, skill=azul, agent_result=laranja |
| ↳ Confidence | texto colorido | ≥90% verde, ≥70% amarelo, <70% vermelho |

---

## 🔔 Atividade

| Elemento | Tipo | Detalhes |
|---|---|---|
| Header | barra | 🔔 "Atividade" / "Log em tempo real de todos os agentes" |
| Botão "← Início" | btn secundário | volta pra Home |
| **Feed de atividades** | lista (coluna esquerda) | |
| ↳ ActivityRow | linha | timestamp, dot colorido (kind), título, badge severidade |
| ↳ Badge severidade | badge | error=Urgente(vermelho), warning=Atenção(amarelo), info=Info(roxo) |
| ↳ Dot kind | indicador | agent_session=azul, ingestion=teal, rfq=amarelo, upload=rosa |
| **Painel "Agentes ativos"** | lista (coluna direita) | |
| ↳ Agente row | linha clicável | 🛒📊📅✍️🎯👥 + nome + status + badge contagem |
| **Painel "Resumo do dia"** | cards | Decisões pendentes, Aprovadas, Ações, NPS |
| **Bottom strip** | barra | chips: 🔴/🟢 urgência, ⚠️/💡 alertas, 🟡 pendentes, 🟢 concluídas, chip numérico |

---

## ⚙️ Admin

| Elemento | Tipo | Detalhes |
|---|---|---|
| Header | barra | ⚙️ "Admin" |
| **Tabs** | tabs | Integrações, Usuários, Auditoria, Notificações, Faturamento, LGPD, Contexto |
| **Tab: Integrações** | | |
| ↳ Lanes | seções | "ERPs & Gestão", "Google", "Bancos" |
| ↳ Card integração | card | nome, descrição, status (conectado/desconectado), botão conectar |
| ↳ Bancos Polp | lista | 27 instituições (Itaú, Bradesco, Santander, BB, Caixa, Nubank, Inter...) |
| **Tab: Usuários** | | |
| ↳ Lista membros | tabela | nome, email, role, ações |
| ↳ Formulário convite | form | input email + select role + btn "Convidar" |
| **Tab: Auditoria** | log | timestamp, ação, usuário, detalhes |
| **Tab: Notificações** | toggles | preferências por canal/agente |
| **Tab: Faturamento** | painel | plano, uso, histórico |
| **Tab: LGPD** | painel | políticas, consentimentos, exportação/exclusão |
| **Tab: Contexto** | painel | informações estruturais da empresa |

---

## 🖥️ AgentOps

| Elemento | Tipo | Detalhes |
|---|---|---|
| Header | barra | 🖥️ "AgentOps" |
| **Sessões** | tabela expansível | ID curto, StatusPill, duração, data |
| ↳ StatusPill | badge | verde(completed/success/active), amarelo(pending/running), vermelho(failed/error), cinza(inactive) |
| ↳ ProgressBar | barra | % preenchida quando pct != null |
| **Sync Jobs** | lista | tipo, status, progresso, botão retry |
| **Credenciais** | lista | nome, tipo, toggle ativar/desativar |

---

## 🚀 Onboarding

| Elemento | Tipo | Detalhes |
|---|---|---|
| **Step indicator** | steps | 5 steps: Conta → Empresa → Dados → Mapeamento → Lançamento |
| **Step 1: Conta** | formulário | login/cadastro |
| **Step 2: Empresa** | formulário | nome, vertical (8 opções), porte (4 opções) |
| ↳ Select vertical | dropdown | Comércio, Serviços, Indústria, Saúde, Educação, Agronegócio, Financeiro, Outro |
| ↳ Select porte | dropdown | Só eu, 2-10, 10-50, 50+ |
| **Step 3: Dados** | upload | CSV/Excel + Google Drive picker |
| ↳ Upload area | drag & drop | arrastar arquivo |
| ↳ Google Picker | modal externo | Google Picker API |
| ↳ Schema type | select | Notas Fiscais, Transações Financeiras, Clientes, Estoque |
| **Step 4: Mapeamento** | tabela | coluna do arquivo → campo canônico (dropdown) |
| ↳ Campos canônicos | dropdown | 22 campos: documento, data, valor, cliente_*, fornecedor_*, produto_* |
| **Step 5: Lançamento** | tela final | resumo + CTA "Começar" |

---

## 💬 Chat

| Elemento | Tipo | Detalhes |
|---|---|---|
| ChatPanel | painel lateral | sobreposição direita |
| Área de mensagens | scroll | bolhas user/agent, timestamp |
| SmartRenderer | renderizador | markdown, código, tabelas, componentes interativos |
| Input | campo texto | placeholder, Enter envia, Shift+Enter nova linha |
| Seletor de agente | dropdown/tabs | agentes disponíveis |
