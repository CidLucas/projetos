# 📄 Documentos — Requisitos Blue V3

> Última atualização: 2026-07-30
> Status: 🟡 Em preenchimento

---

## 1. Visão Geral

**Objetivo:** Centralizar a criação, edição, visualização e gestão de documentos gerados na plataforma. Os documentos são artefatos produzidos pelos agentes de IA (ex: relatórios, propostas, atas, análises) a partir de modelos predefinidos.

**Contexto:** O usuário acessa esta página pelo menu lateral/superior. É uma das áreas centrais do Blue V3 — todo output estruturado dos agentes cai aqui.

**Relação com outras páginas:**
- **Chat:** o usuário pode solicitar a criação de um documento via chat → o sistema oferece modelos ou criar novo modelo antes de iniciar
- **Estratégia:** documentos podem ser insumo para a sala de estratégia
- **Conhecimento:** modelos de documento são parte da base de conhecimento da empresa

---

## 2. Estrutura de Elementos (Front-End)

> A preencher: cada tab, sidebar, botão, card, modal, etc.

### 2.1 Tabs de navegação da página

- **Tipo:** tabs horizontais (topo da área de conteúdo)
- **Posição:** abaixo do header principal, dentro da página Documentos
- **Conteúdo/Dados:** abas que segmentam os documentos por tipo/estado (ex: "Todos", "Rascunhos", "Finalizados", "Modelos")
- **Interações:** clique para alternar entre abas; possível indicador de contagem por aba
- **Estados visuais:** tab ativa destacada, tabs com contador
- **Condições de visibilidade:** sempre visível

### 2.2 Lista de documentos

- **Tipo:** lista / grid de cards
- **Posição:** conteúdo central da página
- **Conteúdo/Dados:** cada card representa um documento — título, tipo/modelo usado, data de criação, status, agente que gerou
- **Interações:** clique para abrir; possível menu de contexto (⋮) com ações: editar, duplicar, arquivar, excluir, exportar
- **Estados visuais:** card normal, card selecionado, indicador de status (rascunho/finalizado)
- **Condições de visibilidade:** visível quando há pelo menos 1 documento; estado vazio com CTA quando não há documentos

### 2.3 Botão "Novo Documento"

- **Tipo:** botão primário (CTA)
- **Posição:** canto superior direito da área de conteúdo
- **Conteúdo/Dados:** label "Novo Documento" ou "+"
- **Interações:** clique → abre modal de seleção de modelo (ver fluxo 3.1)
- **Estados visuais:** normal, hover, focus
- **Condições de visibilidade:** sempre visível

### 2.4 Modal de seleção de modelo

- **Tipo:** modal / diálogo
- **Posição:** centro da tela (overlay)
- **Conteúdo/Dados:** lista de modelos disponíveis (nome, descrição curta, preview) + opção "Criar novo modelo"
- **Interações:** clique no modelo → inicia criação do documento com aquele modelo; clique em "Criar novo modelo" → redireciona para tela de criação de modelo
- **Estados visuais:** modelos como cards clicáveis, destaque no hover
- **Condições de visibilidade:** abre ao clicar em "Novo Documento" ou quando o chat dispara a ação "criar documento"

### 2.5 Sidebar / Filtros (se houver)

- **Tipo:** sidebar lateral ou barra de filtros
- **Posição:** lateral esquerda da área de conteúdo
- **Conteúdo/Dados:** filtros por tipo de documento, data, status, agente
- **Interações:** checkboxes, dropdowns, campo de busca
- **Estados visuais:** filtro ativo com indicador
- **Condições de visibilidade:** a confirmar se existe sidebar ou se os filtros ficam no topo

### 2.6 Barra inferior / Ações em lote

- **Tipo:** barra de ações
- **Posição:** inferior da página
- **Conteúdo/Dados:** ações em lote quando múltiplos documentos estão selecionados
- **Interações:** selecionar múltiplos → ações: exportar selecionados, arquivar em lote, mover para pasta
- **Estados visuais:** barra aparece/desaparece com seleção
- **Condições de visibilidade:** visível apenas quando há ≥1 documento selecionado

---

## 3. Fluxos de Processo

### 3.1 Criação de documento

**Regra fundamental:** Um documento **só pode ser criado a partir de um modelo existente** ou **criando um novo modelo primeiro.**

```
INÍCIO
  │
  ├─ Gatilho A: Usuário clica "Novo Documento" na página Documentos
  ├─ Gatilho B: Usuário diz no Chat "quero criar um documento" / "cria uma proposta" etc.
  │
  ▼
Sistema exibe modal com:
  • Lista de modelos disponíveis (nome + descrição curta)
  • Opção "Criar novo modelo"
  │
  ├─ Usuário escolhe um modelo
  │     │
  │     ▼
  │   Documento é instanciado a partir do modelo
  │   (metadados, estrutura, seções predefinidas)
  │     │
  │     ▼
  │   Usuário é levado ao editor do documento
  │   (ou agente inicia o preenchimento, se acionado via chat)
  │
  └─ Usuário escolhe "Criar novo modelo"
        │
        ▼
      Abre tela de criação de modelo
        • Nome do modelo
        • Descrição
        • Estrutura/seções
        • Prompt associado (o que o agente deve fazer com esse modelo)
        │
        ▼
      Após salvar o modelo, volta ao fluxo de criação
      (modal reabre com o novo modelo disponível)
```

**Pré-condições:**
- Usuário autenticado com permissão de criação
- Pelo menos 1 modelo cadastrado OU usuário disposto a criar um novo

**Pós-condições:**
- Documento criado com status "Rascunho"
- Associado ao modelo utilizado
- Visível na lista de documentos

**Tratamento de erros:**
- Se não houver modelos disponíveis: exibir mensagem orientando criar o primeiro modelo
- Se falhar ao instanciar modelo: toast de erro + log

### 3.2 Criação via Chat (comando de voz/texto)

```
Usuário diz: "Cria um relatório de diário de bordo"
  │
  ▼
Agente interpreta a intenção: criar_documento
  │
  ▼
Agente busca modelos compatíveis com a intenção
(ex: "relatório" → busca modelos do tipo relatório)
  │
  ▼
Agente responde no chat:
  "Tenho estes modelos que podem servir:
   1. Relatório de Diário de Bordo
   2. Relatório Mensal
   3. Relatório de Análise
   Ou quer criar um modelo novo?"
  │
  ├─ Usuário escolhe 1, 2 ou 3 → fluxo normal de instanciação
  └─ Usuário pede modelo novo → fluxo de criação de modelo
```

### 3.3 Edição de documento

_A preencher._

### 3.4 Exclusão / Arquivamento

_A preencher._

### 3.5 Exportação

_A preencher._

---

## 4. Regras de Negócio

| # | Regra | Motivo |
|---|---|---|
| R1 | Documento só pode ser criado a partir de um modelo existente (ou criando novo modelo antes) | Controlar a estrutura e qualidade dos outputs; evitar documentos "soltos" sem template |
| R2 | Modelos são reutilizáveis — um modelo gera N documentos | Eficiência: define uma vez, usa sempre |
| R3 | Cada modelo tem um prompt associado que guia o agente no preenchimento | O agente precisa saber o que preencher em cada seção |
| R4 | Modelos podem ser marcados como "padrão" para determinados tipos de solicitação | Para o chat sugerir o modelo certo automaticamente |
| R5 | _A preencher: permissões (quem pode criar modelos? quem pode editar?)_ |
| R6 | _A preencher: versionamento de modelos (se editar um modelo, o que acontece com docs já criados?)_

---

## 5. Integrações

| Integração | Tipo | Descrição | Status |
|---|---|---|---|
| API de Modelos | REST/GraphQL | CRUD de modelos de documento | 🔴 A definir |
| API de Documentos | REST/GraphQL | CRUD de documentos + instanciação a partir de modelo | 🔴 A definir |
| Chat → Documentos | Interno/Evento | Quando o agente detecta intenção `criar_documento`, dispara o modal de seleção de modelo no front | 🔴 A definir |
| Editor de Documento | Interno | Ao instanciar documento, redireciona para o editor (tiptap? blocknote? custom?) | 🔴 A definir |

---

## 6. Cenários de Teste

### Happy Path
- [ ] Usuário clica "Novo Documento" → vê modelos → seleciona um → documento é criado → vai para editor
- [ ] Usuário diz no chat "cria um relatório" → agente sugere modelos → usuário escolhe → documento criado
- [ ] Usuário sem modelos clica "Novo Documento" → vê opção "Criar novo modelo" → cria modelo → volta e seleciona

### Edge Cases
- [ ] Usuário tenta criar documento sem nenhum modelo cadastrado
- [ ] Usuário seleciona modelo que foi excluído por outro admin enquanto a modal estava aberta
- [ ] Usuário inicia criação via chat mas perde conexão antes de escolher modelo
- [ ] Nome de documento duplicado (permite? renomeia automaticamente?)

### Error States
- [ ] API de modelos fora do ar → mensagem amigável + opção de criar documento em branco? (não, pela R1)
- [ ] Instanciação do documento falha → toast de erro + tentar novamente
- [ ] Timeout ao buscar modelos → spinner + retry automático
