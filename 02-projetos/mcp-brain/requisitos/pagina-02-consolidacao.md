# 🔀 Página 02 — Consolidação de Memória

> **Arquivo no código:** `Context-MCP.dc.html` → `showConflicts`
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Tela de curadoria e resolução de conflitos do MCP Brain Lite. Quando dois documentos afirmam valores diferentes para o mesmo fato (mesma entidade + mesmo predicado), o sistema detecta o conflito e o apresenta aqui para decisão humana.

O usuário pode: manter o fato novo, manter o antigo, manter ambos com janelas de validade, ou editar o fato entrante antes de confirmar.

### Layout

```
┌──────────────────────────────────────────────────────────────────┐
│ ┌──────────┐ ┌───────────────┐ ┌────────┐  [🔍 Buscar...] [Entidade▾] [Predicado▾] │
│ │ 3        │ │ 1             │ │ 5      │                                    │
│ │ Pendentes│ │ Resolv. hoje  │ │ Total  │                                    │
│ └──────────┘ └───────────────┘ └────────┘                                    │
├──────────────────────────────────────────────────┬─────────────────────────────┤
│ ┌──────────────────────────────────────────────┐ │                             │
│ │ [Pessoa] João Silva → salário mensal         │ │ (painel de entidade         │
│ │ Detectado 21/01/2024       [Pendente] [Contexto]│  abre aqui quando          │
│ ├──────────────────┬───────────────────────────┤ │  clica "Contexto")          │
│ │ 🕐 Vigente       │ 📈 Entrante · novo        │ │                             │
│ │ R$ 50.000        │ R$ 65.000    +R$15.000    │ │                             │
│ │ Confiança: 92%   │ Confiança: 88%            │ │                             │
│ │ Fonte: Contrat.. │ Fonte: Contrato_Silva..   │ │                             │
│ │ De: 01/01/2023   │ De: 01/01/2024            │ │                             │
│ │ Até: em aberto   │ Até: em aberto            │ │                             │
│ ├──────────────────┴───────────────────────────┤ │                             │
│ │ Resolução: [✓ Manter o novo] [✗ Manter o antigo] [📋 Ambos] [✏️ Editar] │ │
│ └──────────────────────────────────────────────┘ │                             │
│                                                  │                             │
│ ┌──────────────────────────────────────────────┐ │                             │
│ │ [Empresa] Silva & Associados → capital social │                             │
│ │ ...                                          │ │                             │
│ └──────────────────────────────────────────────┘ │                             │
└──────────────────────────────────────────────────┴─────────────────────────────┘
```

---

## 2. Estrutura de Elementos

### 2.1 Stats Bar

- **Tipo:** 3 cards lado a lado
- **Posição:** topo da área de conflitos, acima dos filtros
- **Conteúdo/Dados:**
  - Card Pendentes: número grande laranja + label "Pendentes"
  - Card Resolvidos hoje: número grande verde + label "Resolvidos hoje"
  - Card Total: número grande cinza + label "Total"
- **Interações:** somente leitura (não clicável)
- **Estados visuais:** cards com fundo glass, borda, padding 12px 18px
- **Cálculo:**
  - Pendentes = `conflicts.filter(c => c.status === 'pending').length`
  - Resolvidos hoje = conflitos resolvidos com `resolved_at` no dia atual
  - Total = `conflicts.length`

### 2.2 Filtros

- **Tipo:** barra de busca + 2 dropdowns
- **Posição:** alinhados à direita, na mesma linha dos stats cards
- **Conteúdo/Dados:**

| Filtro | Tipo | Placeholder/Opções |
|---|---|---|
| Busca textual | input com 🔍 | "Buscar conflito..." — filtra por subject, entity, predicate, valores |
| Entidade | select (155px) | "Todas as entidades", Pessoa, Empresa, Contrato |
| Predicado | select (175px) | "Todos os predicados", Salário mensal, Capital social, Prazo de vigência, CNPJ, Endereço sede |

- **Interações:**
  - Digitar na busca → filtra em tempo real (match case-insensitive em subject + entity + predicate + currentValue + incomingValue)
  - Selecionar entidade → filtra por `c.entity === filterEntity`
  - Selecionar predicado → filtra por `c.predicate === filterPredicate`
- **Estados visuais:** inputs padrão com borda cinza, foco roxo
- **Condições de visibilidade:** sempre visível na tab Consolidação

### 2.3 Conflict Card

- **Tipo:** card expansível
- **Posição:** lista vertical com gap 12px, max-width 860px
- **Conteúdo/Dados:** um card por conflito (filtrado)

**Estrutura de cada card:**

| Seção | Conteúdo |
|---|---|
| **Header** | Badge entidade (Pessoa/Empresa/Contrato), subject (bold 13.5px), →, predicado (itálico roxo) |
| **Header direita** | "Detectado dd/mm/aaaa", status badge (Pendente/Resolvido), botão "Contexto" (se pendente) |
| **Comparação** | Grid 2 colunas: Vigente (esquerda) vs Entrante (direita) |
| **Coluna Vigente** | 🕐 "Vigente", valor grande (23px bold), confiança, fonte, valid_from, valid_to |
| **Coluna Entrante** | 📈 "Entrante · novo", badge delta (ex: +R$ 15.000), valor grande roxo, confiança, fonte, valid_from, valid_to |
| **Ações** | Barra inferior com 4 botões de resolução (se pendente) |
| **Expansão "Manter ambos"** | Grid 2×2 inputs date + confirmar/cancelar |
| **Expansão "Editar"** | Formulário com Valor, Unidade, Confiança, Válido desde/até + confirmar/cancelar |
| **Estado resolvido** | Barra verde com ✓ + label da resolução + timestamp |

### 2.4 Badge de Entidade

- **Tipo:** pill pequena
- **Posição:** início do header do card
- **Conteúdo/Dados:** texto da entidade (Pessoa, Empresa, Contrato)
- **Estados visuais:** fundo glass, borda cinza, uppercase 9.5px, cinza escuro

### 2.5 Status Badge

- **Tipo:** pill
- **Posição:** header direito do card
- **Conteúdo/Dados:**
  - Pendente: fundo laranja claro, texto laranja
  - Resolvido: fundo verde claro, texto verde
- **Estados visuais:** 10.5px, bold, padding 2px 8px, border-radius 99px

### 2.6 Badge Delta (Entrante)

- **Tipo:** pill posicionada absolutamente
- **Posição:** canto superior direito da coluna Entrante
- **Conteúdo/Dados:** diferença formatada — numérica: "+R$ 15.000 (+30.0%)", não-numérica: "≠ valor diferente"
- **Estados visuais:** fundo roxo, texto branco, 10px, bold

### 2.7 Barra de Ações (pendente)

- **Tipo:** barra horizontal
- **Posição:** abaixo da comparação, antes do estado resolvido
- **Conteúdo/Dados:**

| Botão | Ícone | Ação | Estilo |
|---|---|---|---|
| Manter o novo | ✓ | Encerra vigência do antigo, define novo como vigente | Primário roxo |
| Manter o antigo | ✗ | Rejeita entrante, mantém vigente intacto | Outline |
| Manter ambos | 📋 | Abre painel de janelas de validade | Outline |
| Editar | ✏️ | Abre formulário de edição do entrante | Outline |

- **Condições de visibilidade:** só aparece quando `isPending && !isResolving && !isEditing`

### 2.8 Painel "Manter ambos"

- **Tipo:** expansão inline
- **Posição:** entre a comparação e a barra de ações
- **Conteúdo/Dados:**
  - Título com 📅 "Defina as janelas de validade para coexistência temporal"
  - Grid 2×2: Vigente (De/Até) + Entrante (De/Até)
  - Inputs date com valores pré-preenchidos dos fatos atuais
  - Botão "Confirmar coexistência" (roxo) + "Cancelar"
  - Hint: ℹ️ "Ambos coexistem nas janelas definidas."
- **Interações:**
  - Alterar datas → atualiza estado `bothDates[id]`
  - Confirmar → resolve como `kept_both`, toast confirma
  - Cancelar → volta à barra de ações
- **Estados visuais:** fundo roxo claro (rgba(140,95,219,.05))
- **Condições de visibilidade:** `isResolving === true`

### 2.9 Painel "Editar"

- **Tipo:** expansão inline
- **Posição:** entre a comparação e a barra de ações
- **Conteúdo/Dados:**
  - Título com ✏️ "Editar fato entrante antes de confirmar"
  - Grid 3+2 colunas: Valor (text), Unidade (text), Confiança (number 0–1 step 0.01), Válido desde (date), Válido até (date)
  - Valores pré-preenchidos do fato entrante
  - Botão "Confirmar edição" (azul) + "Cancelar"
- **Interações:**
  - Alterar campos → atualiza estado `editValues[id]`
  - Confirmar → resolve como `edited`, atualiza entrante com valores editados
  - Cancelar → volta à barra de ações
- **Estados visuais:** fundo azul claro (rgba(59,130,246,.05))
- **Condições de visibilidade:** `isEditing === true`

### 2.10 Estado Resolvido

- **Tipo:** barra inferior
- **Posição:** abaixo de tudo, substitui a barra de ações
- **Conteúdo/Dados:**
  - ✓ ícone verde (16px)
  - "Resolvido:"
  - Label da resolução (ex: "Novo mantido, antigo encerrado")
  - Timestamp em formato mono
- **Estados visuais:** fundo verde claro, opacidade 0.7 no card
- **Labels de resolução:**
  - `kept_new`: "Novo mantido, antigo encerrado"
  - `kept_old`: "Antigo mantido, entrante rejeitado"
  - `kept_both`: "Ambos mantidos com janelas de validade"
  - `edited`: "Fato entrante editado e mantido"

### 2.11 Painel de Entidade (sidebar)

- **Tipo:** aside 280px
- **Posição:** coluna direita, abre quando clica "Contexto" em um conflito pendente
- **Conteúdo/Dados:**
  - Header: nome da entidade (15px bold) + tipo + botão ✕
  - "Linha do tempo de fatos" (título uppercase)
  - Lista vertical com timeline:
    - Dots roxos (8px) conectados por linha cinza vertical (1px)
    - Cada fato: predicado (uppercase, cinza), valor (13px bold roxo), período (mono, from → to), fonte (📄 + nome)
- **Interações:**
  - Clicar ✕ → fecha painel
- **Estados visuais:** fundo surface, borda esquerda, animação slide-in
- **Condições de visibilidade:** `entityPanelConflictId !== null`
- **Dados:** hardcoded em `ENTITY_FACTS` por subject:
  - João Silva: cargo, departamento, salário_mensal (2 fatos)
  - Silva & Associados: cnpj, capital_social (2 fatos), endereço_sede
  - Contrato-001: prazo_vigência (2 fatos), valor_contrato
  - Fornecedor ABC: cnpj (2 fatos)

### 2.12 Empty State (filtros)

- **Tipo:** placeholder centralizado
- **Posição:** no lugar da lista de conflitos
- **Conteúdo/Dados:** ✓ ícone verde grande + "Nenhum conflito encontrado com esses filtros."
- **Condições de visibilidade:** `filteredConflicts.length === 0`

---

## 3. Fluxos de Processo

### 3.1 Resolver conflito — "Manter o novo"

```
1. Usuário vê conflito pendente (borda laranja)
2. Clica "✓ Manter o novo"
   → conflito.status = 'resolved'
   → conflito.resolution = 'kept_new'
   → conflito.resolved_at = new Date()
   → card fica opaco 0.7, borda verde
   → barra de ações some, aparece estado resolvido
   → toast: "Novo fato mantido. Fato anterior encerrado."
   → stats atualizam (pendentes -1, resolvidos hoje +1)
```

### 3.2 Resolver conflito — "Manter o antigo"

```
1. Clica "✗ Manter o antigo"
   → conflito.status = 'resolved'
   → conflito.resolution = 'kept_old'
   → conflito.resolved_at = new Date()
   → toast: "Entrante rejeitado. Fato vigente mantido."
```

### 3.3 Resolver conflito — "Manter ambos"

```
1. Clica "📋 Manter ambos"
   → resolvingId = conflito.id
   → expande painel de datas (fundo roxo claro)
   → datas pré-preenchidas: Vigente(valid_from, valid_to), Entrante(valid_from, valid_to)

2. Usuário ajusta as datas
   → bothDates[id] atualiza em tempo real

3. Clica "Confirmar coexistência"
   → conflito.status = 'resolved'
   → conflito.resolution = 'kept_both'
   → conflito.resolved_at = new Date()
   → resolvingId = null
   → toast: "Ambos os fatos mantidos com janelas de validade definidas."

   OU

2. Clica "Cancelar"
   → resolvingId = null
   → volta à barra de ações
```

### 3.4 Resolver conflito — "Editar"

```
1. Clica "✏️ Editar"
   → editingId = conflito.id
   → expande formulário de edição (fundo azul claro)
   → campos pré-preenchidos com dados do fato entrante

2. Usuário modifica: Valor, Unidade, Confiança, Válido desde/até

3. Clica "Confirmar edição"
   → conflito.incoming atualizado com novos valores
   → valor numérico parseado (parseFloat) ou object_value
   → conflito.status = 'resolved'
   → conflito.resolution = 'edited'
   → conflito.resolved_at = new Date()
   → editingId = null
   → toast: "Fato editado e definido como vigente."

   OU

2. Clica "Cancelar"
   → editingId = null
   → volta à barra de ações
```

### 3.5 Visualizar contexto da entidade

```
1. Clica "Contexto" em um conflito pendente
   → entityPanelConflictId = conflito.id
   → painel lateral abre (280px, animação slide)
   → busca ENTITY_FACTS[subject] e renderiza timeline

2. Clica ✕ no painel
   → entityPanelConflictId = null
   → painel fecha
```

### 3.6 Filtrar conflitos

```
1. Usuário digita na busca
   → filterQuery atualiza
   → filteredConflicts() refiltra em tempo real
   → match em: subject + entity + predicate + currentValue + incomingValue (case-insensitive)

2. Usuário seleciona entidade "Empresa"
   → filterEntity = "Empresa"
   → só mostra conflitos com entity === "Empresa"

3. Usuário seleciona predicado "capital_social"
   → filterPredicate = "capital_social"
   → só mostra conflitos com predicate === "capital_social"

4. Filtros vazios (string "") = sem filtro
```

---

## 4. Regras de Negócio

### Estrutura de um conflito

```javascript
{
  id: string,
  subject: string,        // nome da entidade ("João Silva")
  entity: string,         // tipo ("Pessoa" | "Empresa" | "Contrato")
  predicate: string,      // ("salario_mensal" | "capital_social" | "prazo_vigencia" | "cnpj" | "endereco_sede")
  status: string,         // ("pending" | "resolved")
  detected_at: ISO string,
  resolution: string | null,  // ("kept_new" | "kept_old" | "kept_both" | "edited")
  resolved_at: ISO string | null,
  current: {              // fato vigente
    id, numeric_value, object_value, unit,
    valid_from, valid_to, confidence,
    source_filename, document_id
  },
  incoming: {             // fato entrante (conflitante)
    id, numeric_value, object_value, unit,
    valid_from, valid_to, confidence,
    source_filename, document_id
  }
}
```

### Formatação de valores

- **Numérico + unit="BRL":** `R$ 50.000` (toLocaleString pt-BR com espaço não-quebrável)
- **Numérico + outra unit:** `24 meses`
- **Não-numérico:** `object_value` direto (ex: "12.345.678/0001-90")
- **Nulo:** "—"

### Cálculo do delta

- Se ambos são numéricos: `incoming - current` → "+R$ 15.000 (+30.0%)"
- Se não: "≠ valor diferente"

### Confiança

- Label: `(confidence * 100).toFixed(0) + '%'`
- Exibida na linha de metadados do fato

### Predicados (labels)

| Predicado | Label |
|---|---|
| `salario_mensal` | salário mensal |
| `capital_social` | capital social |
| `prazo_vigencia` | prazo de vigência |
| `cnpj` | CNPJ |
| `endereco_sede` | endereço sede |
| outros | substitui `_` por espaço |

### Datas

- **Formato de exibição:** dd/mm/aaaa
- **Valor nulo:** "em aberto"

### Contadores dos stats

- Pendentes: `filter(c => c.status === 'pending').length` (do total, não dos filtrados)
- Resolvidos hoje: filtrados por `resolved_at.toDateString() === today.toDateString()`
- Total: `conflicts.length` (total, não filtrado)

---

## 5. Integrações

| Elemento | Integração | Status |
|---|---|---|
| Lista de conflitos | GET /api/conflicts | ❌ Mockado no `state.conflicts` |
| Resolver conflito | POST /api/conflicts/:id/resolve | ❌ Mockado (setState local) |
| Timeline da entidade | GET /api/entities/:name/facts | ❌ Mockado em `ENTITY_FACTS` |
| Filtros | Query params na API | ❌ Mockado (filter local) |

---

## 6. Cenários de Teste

### Stats
- [ ] Card Pendentes mostra contagem correta de conflitos com status "pending"
- [ ] Card Resolvidos hoje mostra 0 quando nenhum resolvido hoje
- [ ] Card Resolvidos hoje incrementa ao resolver um conflito
- [ ] Card Total mostra `conflicts.length`

### Filtros
- [ ] Buscar "Silva" → filtra conflitos de João Silva + Silva & Associados
- [ ] Buscar "50.000" → filtra conflito de salário (R$ 50.000)
- [ ] Filtrar entidade "Empresa" → só mostra Silva & Associados + Fornecedor ABC
- [ ] Filtrar predicado "capital_social" → só mostra conflito de capital social
- [ ] Combinar entidade + predicado → intersecção
- [ ] Limpar filtros → volta a mostrar todos
- [ ] Empty state quando filtros não encontram nada

### Resolução — Manter o novo
- [ ] Clicar "Manter o novo" → status muda para "resolved"
- [ ] Card fica opaco 0.7 com borda verde
- [ ] Barra de ações some, estado resolvido aparece
- [ ] Toast: "Novo fato mantido. Fato anterior encerrado."
- [ ] Stats atualizam

### Resolução — Manter o antigo
- [ ] Clicar "Manter o antigo" → status muda para "resolved"
- [ ] Toast: "Entrante rejeitado. Fato vigente mantido."

### Resolução — Manter ambos
- [ ] Clicar "Manter ambos" → expande painel de datas
- [ ] Datas pré-preenchidas com valid_from/valid_to dos fatos
- [ ] Alterar data → campo atualiza
- [ ] Confirmar → resolvido como "kept_both"
- [ ] Cancelar → volta à barra de ações
- [ ] Toast: "Ambos os fatos mantidos com janelas de validade definidas."

### Resolução — Editar
- [ ] Clicar "Editar" → expande formulário
- [ ] Campos pré-preenchidos com dados do entrante
- [ ] Alterar valor de 65000 para 70000 → confirma
- [ ] Valor editado aparece no estado resolvido
- [ ] Cancelar → volta à barra de ações
- [ ] Toast: "Fato editado e definido como vigente."

### Painel de entidade
- [ ] Clicar "Contexto" em conflito de João Silva → painel abre
- [ ] Timeline mostra 4 fatos de João Silva
- [ ] Dots conectados por linha vertical
- [ ] Cada fato mostra predicado, valor, período, fonte
- [ ] Clicar ✕ → painel fecha
- [ ] Clicar "Contexto" em outro conflito → painel atualiza para aquela entidade

### Edge cases
- [ ] Conflito já resolvido não mostra barra de ações nem botão "Contexto"
- [ ] Valor não-numérico (ex: CNPJ) → delta mostra "≠ valor diferente"
- [ ] Unidade não-BRL (ex: meses) → valor mostra "24 meses"
- [ ] valid_to null → mostra "em aberto"
- [ ] Múltiplos conflitos resolvidos hoje → contador incrementa
