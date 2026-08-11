# 👥 Clientes — Tela de Requisitos de UI (Blue V3)

> Última atualização: 2026-08-11 | Status: 🟡 Em andamento (esmiuçando para design)
> Segue o padrão de [template-tela.md](./template-tela.md). Fluxo do kanban em [kanbans.md](./kanbans.md).
> Legenda: ✅ Reusar (existe no Blu DS/monorepo) · 🔶 Adaptar · 🟥 Construir (novo)

---

## 1. Layout macro da tela

```
┌──────────────────────────────────────────────────────────────────────┐
│ A · TOPO: título "Clientes" | busca | filtros | [+ Novo cliente]     │
├──────────────────────────────────────────────────────────────────────┤
│ B · ABAS:  [Kanban] [Follow-up] [Histórico] [Rotinas]                │
│ ┌────────────────────────────────────────────┐  ┌──────────────────┐ │
│ │ KANBAN — 5 colunas                         │  │ C · PAINEL DIREITO│ │
│ │ 💬Conversa │ 🧾Orçamento │ 📎Artefatos │    │  │ (card selecionado)│ │
│ │ ✅Fechado │ 🔁Recorrência                 │  │ │                  │ │
│ └────────────────────────────────────────────┘  └──────────────────┘ │
├──────────────────────────────────────────────────────────────────────┤
│ D · QUADRINHOS:  [Insights do agente] [Métricas] [Interlocutores]    │
└──────────────────────────────────────────────────────────────────────┘
```

Aba padrão: **Kanban**. O painel direito (C) abre quando um card é clicado.

---

## 2. Região A — Topo da sala

### 2.1 Título + contador
- **Componente:** `PageHeader` 🔶 Adaptar
- **Conteúdo/Dados:** "Clientes" + subtítulo com total de clientes ativos (ex.: "128 clientes")
- **Interações:** clique no subtítulo abre a aba Ativos/lista
- **Estados:** — | **Visibilidade:** sempre

### 2.2 Busca de cliente
- **Componente:** `SearchInput` ✅ Reusar
- **Propósito:** achar cliente rápido (nome, contato, segmento)
- **Opções:** busca simples; tecla Enter abre lista de resultados com atalho
- **Estados:** vazio (placeholder "Buscar cliente..."), loading, sem resultados ("Nenhum cliente encontrado")
- **Feedback:** resultados em dropdown

### 2.3 Filtros
- **Componente:** `Select` + `DropdownMenu` ✅ Reusar
- **Opções:** Segmento (todos / lista de segmentos), Responsável (todos / dono / membro X), Risco (todos / oportunidade / alerta / risco)
- **Interações:** múltiplos filtros ativos ao mesmo tempo; badge de limpar ("Limpar filtros")
- **Estados:** selecionado, disabled quando não há opções

### 2.4 Botão "Novo cliente"
- **Componente:** `Button` (variant primary, ícone +) ✅ Reusar
- **Ações:** abre modal de criação (Região E)
- **Estados:** default / hover / disabled (sem permissão de criar)

---

## 3. Região B — Abas do quadro principal

### 3.1 Tabs
- **Componente:** `Tabs` ✅ Reusar
- **Abas (ordem):** Kanban (padrão) → Follow-up → Histórico → Rotinas
- **Opções:** clique troca de aba; badge de contagem na aba Follow-up (ex.: "5")
- **Interações:** persistência da aba ativa por sessão (Zustand)
- **Estados:** ativa/inativa; badge de pendência

### 3.2 Aba Kanban — barra de ferramentas do quadro
- **Componente:** `Toolbar` 🔶 Adaptar
- **Conteúdo/Dados:** filtros rápidos do quadro (buscar no quadro, por coluna, ordenar)
- **Opções de ordenação:** valor potencial (maior→menor), prazo (mais urgente), recência de contato (mais antigo), manual (arrastar)
- **Interações:** alternar visualização Kanban ↔ Lista (opcional); recolher/expandir colunas; limpar filtros
- **Estados:** — | **Visibilidade:** sempre na aba Kanban

### 3.3 KanbanBoard
- **Componente:** `KanbanBoard` 🟥 Construir (peça central)
- **Conteúdo/Dados:** 5 colunas do fluxo de relacionamento (kanbans.md §3.2): Conversa, Orçamento, Artefatos, Fechado, Recorrência
- **Interações:** scroll horizontal no quadro; drag & drop de cards entre colunas; clique em card abre painel C; drop fora da coluna válida → card volta ao lugar
- **Estados:** loading (skeleton), vazio (empty state com CTA "Adicionar primeiro cliente"), erro (reload)
- **Feedback:** animação de mover; toast em erro de movimentação

### 3.4 KanbanColumn
- **Componente:** `KanbanColumn` 🟥 Construir
- **Conteúdo/Dados:** header com nome, contador de cards (ex.: "Conversa · 12"), cor da coluna; corpo com cards empilhados (scroll interno)
- **Opções (menu da coluna):** recolher coluna, mover todos?, configurar limite (WIP opcional), (não permite renomear/remover — etapas fixas da dimensão)
- **Interações:** dropzone de cards; recolher/expandir
- **Estados:** recolhida (mostra só header), vazia (dropzone visível), limite atingido (aviso)

### 3.5 KanbanCard
- **Componente:** `KanbanCard` 🟥 Construir
- **Conteúdo/Dados:** nome do cliente (título), badge de etapa interna (ex.: "Aguardando aprovação"), semáforo (borda esquerda 🟢/🟡/🔴), valor potencial (R$), prazo/recência ("há 2d"), responsável (avatar)
- **Ações rápidas (hover):** Aprovar (se há pendência), Gerar artefato, Mover → (menu de coluna destino), Comentar (nota interna)
- **Interações:** clique → abre painel C; arrastar → mover coluna; menu "..." (mais ações: duplicar, arquivar, excluir com confirmação)
- **Estados:** default / hover / dragging (elevado) / selecionado / semáforo por cor / disabled
- **Feedback:** confirmação antes de excluir

### 3.6 Estado vazio do quadro
- **Componente:** `EmptyState` ✅ Reusar
- **Conteúdo/Dados:** ilustração + "Nenhum cliente aqui ainda" + botão "Novo cliente"
- **Visibilidade:** zero cards em todas as colunas

### 3.7 Aba Follow-up
- **Componente:** lista de `DecisionCard`/`FollowUpCard` 🔶 Adaptar
- **Conteúdo/Dados:** clientes que precisam de ação (sugeridos pelo agente): nome, motivo ("parado há 5 dias", "orçamento sem resposta"), tempo relativo, nível
- **Opções por card:** Concluir, Adiar (snooze 1/3/7 dias), Ver no kanban (abre card)
- **Estados:** vazio ("Nada pendente 🎉"), loading

### 3.8 Aba Histórico
- **Componente:** `Timeline` ✅ Reusar
- **Conteúdo/Dados:** ações em clientes (mensagem enviada, orçamento aceito, artefato gerado, follow-up concluído), cronológicas, com filtro por cliente
- **Interações:** clique em item abre contexto (card/painel)
- **Estados:** vazio ("Sem histórico ainda")

### 3.9 Aba Rotinas
- **Componente:** `RoutineConfigSection` + `RoutineExecutionFeed` ✅ Reusar
- **Conteúdo/Dados:** rotinas da dimensão Clientes (follow-up de parados, revisão de propostas vencidas, análise de churn mensal) + feed de execuções
- **Opções:** criar rotina via builder chat, "Rodar agora", editar pausar/excluir
- **Estados:** sem rotinas (empty + CTA), feed vazio

---

## 4. Região C — Painel direito (detalhe do card)

> Drawer lateral fixo (~380px), abre ao clicar num card. Componente: `Drawer` 🔶 Adaptar (painel existente ou novo).

### 4.1 Header do painel
- **Conteúdo/Dados:** nome do cliente + semáforo + valor potencial; botão fechar (X)
- **Ações:** fechar painel; editar dados (abre modal E)
- **Estados:** — | **Visibilidade:** sempre que um card está selecionado

### 4.2 Conversa (thread de mensagens)
- **Componente:** `MessageThread` 🟥 Construir + `MessageBubble` 🟥 Construir
- **Conteúdo/Dados:** histórico da troca com o cliente — bubbles do cliente (cinza) e do agente (azul); status em cada mensagem do agente: Rascunho → Aguardando aprovação → Enviada → (Lida/Respondida quando houver canal)
- **Opções:** ver mensagem inteira (expandir), copiar, "Reenviar" (se falhou)
- **Estados:** bubble com status visual (pendente = contorno amarelo), thread vazia ("Nenhuma mensagem ainda"), loading
- **Feedback:** toast ao aprovar/enviar

### 4.3 Campo de resposta
- **Componente:** `TextArea` + `Button` ✅ Reusar + botão IA 🟥 Construir
- **Conteúdo/Dados:** caixa para o dono escrever resposta; botão "Gerar resposta (IA)" aciona o agente
- **Opções:** enviar direto (se permissão), ou gerar rascunho do agente → fica "Aguardando aprovação" (Aprovar / Editar / Rejeitar)
- **Ações:** Enter envia; Esc limpa; atalho de IA
- **Estados:** disabled enquanto envia, placeholder "Responder ao cliente..."
- **Feedback:** confirmação de envio; aviso "resposta gerada pela IA, revise antes de aprovar"

### 4.4 Aprovação inline
- **Componente:** `ApprovalInline` 🟥 Construir (padrão reaproveitado nas outras salas)
- **Conteúdo/Dados:** quando há resposta/artefato pendente: texto + botões Aprovar / Editar / Rejeitar (+ motivo opcional ao rejeitar)
- **Estados:** pendente / aprovado / rejeitado (feedback com motivo)
- **Visibilidade:** só quando existe pendência

### 4.5 Informações do cliente
- **Componente:** `InfoList` 🔶 Adaptar
- **Conteúdo/Dados:** contato (WhatsApp, e-mail), segmento, valor potencial, origem (canal), criado em
- **Ações:** botão Editar → modal de formulário (E)
- **Estados:** campos vazios (placeholder "—")

### 4.6 Etapa atual + mover
- **Componente:** `SegmentedControl`/`Select` 🔶 Adaptar
- **Conteúdo/Dados:** coluna atual (Conversa/Orçamento/Artefatos/Fechado/Recorrência) + aprovador da etapa
- **Opções:** dropdown "Mover para..." com as 5 colunas (não permite pular etapas sem aviso: confirmar se pular)
- **Interações:** mover = atualiza card e registra no Histórico
- **Feedback:** toast "Movido para Orçamento"

### 4.7 Artefatos
- **Componente:** `ArtifactList` 🟥 Construir + `DropdownMenu` ✅ Reusar
- **Conteúdo/Dados:** lista de artefatos gerados (NF, contrato, pedido de envio, orçamento) com status (gerado/enviado/assinado)
- **Opções do botão "Gerar artefato":** Nota fiscal · Contrato · Pedido de envio · Orçamento · Proposta
- **Ações:** gerar (usa template — api/documents), visualizar (modal/aba), baixar PDF, enviar ao cliente (via canal), assinar
- **Estados:** vazio ("Nenhum artefato"), gerando (skeleton), erro de geração
- **Feedback:** toast sucesso/erro; artefato aparece na lista e no Histórico

### 4.8 Integrações (atalhos)
- **Componente:** `IconButton` + `Tooltip` ✅ Reusar
- **Conteúdo/Dados:** atalhos do cliente: Abrir WhatsApp, Enviar e-mail, Agendar follow-up (Google Calendar), (Notion/Outlook se configurado)
- **Ações:** cada atalho abre o canal externo em nova aba / cria evento
- **Estados:** ícone disabled quando integração não configurada (tooltip explica)
- **Visibilidade:** sempre; tooltips ajudam

### 4.9 Interlocutores
- **Componente:** `AvatarStack` + `Tag` ✅ Reusar
- **Conteúdo/Dados:** quem está envolvido no card: responsável (dono/membro), agente IA, cliente
- **Ações:** clique em avatar mostra nome/papel/contato
- **Estados:** — | **Visibilidade:** sempre

---

## 5. Região D — Quadrinhos inferiores (2–3)

### 5.1 Q1 — Insights do agente
- **Componente:** cards de insight 🔶 Adaptar (padrão de insights existe)
- **Conteúdo/Dados:** sugestões proativas (ex.: "Cliente X parado há 5 dias — gerar follow-up?", "Orçamento de Y sem resposta há 3 dias")
- **Ações por card:** Ver no kanban (abre card), Aplicar (gera follow-up/rascunho), Dispensar
- **Estados:** vazio ("Sem insights agora"), loading
- **Visibilidade:** sempre; limite 3 cards

### 5.2 Q2 — Métricas da dimensão
- **Componente:** `AnalyticsPanel`/`KpiCard` 🔶 Adaptar (indicadores já existem)
- **Conteúdo/Dados:** Pipeline (R$), Win rate, Ticket médio, NRR, Total de clientes, Segmentos
- **Opções:** período 30d / 90d / 1y; clique em métrica abre a fonte (Estratégia/lista)
- **Estados:** loading; sem dados ("Conecte seu CRM/importe clientes")
- **Visibilidade:** sempre na aba Kanban

### 5.3 Q3 — Interlocutores / envolvidos
- **Componente:** `AvatarStack` + lista ✅ Reusar
- **Conteúdo/Dados:** pessoas envolvidas nos processos da sala (dono, membros, agente) — quem o dono procura para falar
- **Ações:** clique abre contato/chat interno
- **Estados:** vazio ("Sem membros — convide em Admin")
- **Visibilidade:** sempre

---

## 6. Overlays (Região E)

### 6.1 Modal "Novo cliente"
- **Componente:** `Modal` + formulário ✅ Reusar
- **Campos:** nome, contato (WhatsApp/e-mail), segmento, valor potencial, responsável, coluna inicial (padrão Conversa)
- **Ações:** Salvar (cria card + registra Histórico), Cancelar
- **Validação:** nome obrigatório; contato válido
- **Feedback:** toast "Cliente criado"; erro de duplicidade

### 6.2 Modal "Editar cliente" (mesmo formulário preenchido)

### 6.3 Modal "Visualizar artefato"
- **Componente:** `Modal`/navegador de doc ✅ Reusar (EditorOverlay existe)
- **Conteúdo/Dados:** preview do artefato + ações (Baixar, Enviar, Assinar)
- **Visibilidade:** ao clicar em artefato da lista

### 6.4 Confirmações
- Excluir card → confirm; Rejeitar resposta/artefato → pedir motivo (opcional); Mover pulando etapas → avisar.

---

## 7. Elementos do design system (biblioteca Blu DS)

### 🟥 Construir (novos — núcleo)
| Componente | Uso | Salas que reusam |
|---|---|---|
| `KanbanBoard` | quadro de colunas com drag & drop | todas com kanban |
| `KanbanColumn` | coluna com contador, cor, dropzone | todas com kanban |
| `KanbanCard` | card com semáforo, badge, ações rápidas | todas com kanban |
| `SemaphoreDot` | indicador 🟢🟡🔴 | Home, todas as salas |
| `MessageThread` | conversa com o cliente | Clientes, Compras (cotação) |
| `MessageBubble` | mensagem com status (rascunho/pendente/enviada) | Clientes, Compras |
| `ApprovalInline` | aprovar/editar/rejeitar inline | todas as salas |
| `ArtifactList` | lista de artefatos + gerar | Clientes, Documentos, Financeiro |
| `StepBadge` | badge de etapa interna do card | todas com kanban |

### 🔶 Adaptar (existe, ajustar)
`PageHeader`, `Toolbar`, `Drawer`, `InfoList`, `AnalyticsPanel`, `KpiCard`, `DecisionCard` → `FollowUpCard`, `SegmentedControl`, cards de insight, `RoutineConfigSection` (rotinas por sala).

### ✅ Reusar (sem mudança)
`Button`, `Input`, `SearchInput`, `Select`, `DropdownMenu`, `Tabs`, `Modal`, `Tooltip`, `Toast`, `Skeleton`, `EmptyState`, `Avatar`, `AvatarStack`, `Badge`, `Tag`, `IconButton`, `Timeline`, `RoutineExecutionFeed`, `EditorOverlay`.

---

## 8. Regras de negócio de UI (resumo)

| # | Regra |
|---|---|
| U1 | Aba padrão = Kanban; persiste a última aba por sessão |
| U2 | Colunas do kanban são fixas (etapas da dimensão) — não renomear/remover na UI |
| U3 | Resposta pendente aparece com badge na aba Follow-up e na Home |
| U4 | Todo movimento de card registra no Histórico |
| U5 | Pular etapas exige confirmação |
| U6 | Papel "aprovador" vê o botão Aprovar; "criador" vê o botão Gerar; "visualizador" só vê (papéis fixos da Fase 0) |
| U7 | Sem permissão de criar → botão "Novo cliente" disabled |

---

## 9. Cenários de teste (UI)

- [ ] Criar cliente → card aparece na Conversa + toast + Histórico
- [ ] Gerar resposta IA → fica "Aguardando aprovação" → Aprovar → bubble "Enviada"
- [ ] Rejeitar resposta → motivo pedido → rascunho volta para edição
- [ ] Arrastar card Conversa → Orçamento → confirmação de pular? (não pula) → Histórico atualizado
- [ ] Gerar artefato (cada tipo) → aparece na lista, abre preview, baixa PDF
- [ ] Filtros combinados (segmento + responsável + risco) → quadro filtra
- [ ] Nenhum cliente → empty state com CTA
- [ ] Mobile: kanban horizontal + painel C vira tela cheia? (decisão em aberto)
- [ ] Permissão visualizador → sem botões de ação

---

## 10. Decisões em aberto

1. **4 abas confirmadas?** Kanban / Follow-up / Histórico / Rotinas — ou "Config" entra como 5ª aba?
2. **Métricas embaixo (Q2)** vs. no topo da sala (Fase 0 dizia topo). Qual fica?
3. **Painel C:** drawer lateral fixo vs. modal central? (proposta: drawer)
4. **Visualização Lista** ao lado do Kanban: útil ou desnecessária?
5. **Limite WIP por coluna:** mostrar aviso ou não?
6. **WhatsApp como canal de mensagens:** confirma? (muda integração 4.8 e o envio)
7. **Comentários internos** no card (nota do dono, não vai ao cliente): entra?
