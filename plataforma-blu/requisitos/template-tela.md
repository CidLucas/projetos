# Template de Análise de Tela — Blue V3

> **Uso:** este é o molde para especificar QUALQUER tela da Blue V3 (Clientes, Compras, Financeiro, Documentos, Biblioteca...).
> Toda tela nova segue este documento. O exemplo preenchido está em [clientes.md](./clientes.md).

---

## 1. O que uma tela precisa especificar

| # | Pergunta guia | Onde entra |
|---|---|---|
| 1 | Qual o layout macro da tela? (regiões) | Diagrama ASCII no topo |
| 2 | Quais abas o quadro principal tem? | Região Abas |
| 3 | O que tem em cada região? (elemento por elemento) | Uma seção por região |
| 4 | Quais opções o usuário pode escolher em cada dropdown/menu? | Na ficha do elemento |
| 5 | Quais ações são possíveis e o que cada ação faz? | Na ficha do elemento (Interações) |
| 6 | Quais estados visuais cada elemento tem? | Na ficha do elemento (Estados) |
| 7 | Quais elementos viram componente no design system? | Lista final de biblioteca |

## 2. Regiões padrão de uma tela

| Região | Posição | Conteúdo típico |
|---|---|---|
| A | Topo | Título da sala, ações globais (criar, buscar, filtrar) |
| B | Centro | Abas + quadro principal (kanban, lista, grade, tabela) |
| C | Lateral direita | Painel de detalhe do item selecionado (drawer) |
| D | Base | 2–3 quadrinhos de apoio (insights, métricas, interlocutores, pendências) |
| E | Overlays | Modais, confirmações, formulários, toasts |

## 3. Ficha padrão de elemento de UI

Para CADA elemento da tela, preencher:

```
### 2.X [Nome do Elemento]
- **Componente Blu DS:** [nome do componente na biblioteca]
- **Região:** A / B / C / D / E
- **Propósito:** [o que resolve para o usuário]
- **Conteúdo/Dados:** [o que mostra e de onde vêm os dados]
- **Opções (dropdowns/menus):** [todas as escolhas possíveis, item por item]
- **Ações/Interações:** [clique, hover, drag, teclado — e o efeito de cada uma]
- **Estados visuais:** default / hover / active / disabled / loading / empty / error / selected
- **Condições de visibilidade:** [quando aparece/esconde]
- **Feedback:** [toast, confirmação, notificação]
```

## 4. Checklist antes de considerar uma tela especificada

- [ ] Diagrama ASCII do layout
- [ ] Abas definidas (nome, ordem, aba padrão)
- [ ] Cada região com seus elementos fichados
- [ ] Todos os dropdowns/menus com as opções explícitas
- [ ] Todos os botões/ações com efeito descrito
- [ ] Estados vazio/loading/erro de cada lista e quadro
- [ ] Elementos novos (não existentes no Blu DS) marcados como 🟥 Construir
- [ ] Elementos existentes marcados como ✅ Reusar / 🔶 Adaptar
- [ ] Lista de componentes do design system fechada
- [ ] Decisões em aberto listadas para o fundador validar
