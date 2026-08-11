# Template de Análise de Tela — Blue V3

> **Uso:** este é o molde para especificar QUALQUER tela da Blue V3 (Clientes, Compras, Financeiro, Documentos, Biblioteca...).
> Toda tela nova segue este documento. O exemplo preenchido está em [clientes.md](./clientes.md).
> **Princípio:** especificar **elementos puros** — a informação e a ação, sem amarrar ao design/componentes atuais da Blu. O novo conceito visual nasce desta especificação.

---

## 1. O que uma tela precisa especificar

| # | Pergunta guia | Onde entra |
|---|---|---|
| 1 | Qual o layout macro da tela? (regiões) | Diagrama ASCII no topo |
| 2 | Quais abas a tela tem? (sem faixa horizontal — abas discretas) | Região de navegação |
| 3 | O que tem em cada região? (elemento por elemento) | Uma seção por região |
| 4 | Quais **informações** cada elemento mostra? | Na ficha do elemento (Conteúdo) |
| 5 | Quais **opções** o usuário pode escolher (dropdowns/menus)? | Na ficha do elemento (Opções) |
| 6 | Quais **ações** são possíveis e o efeito de cada uma? | Na ficha do elemento (Ações) |
| 7 | Quais estados visuais cada elemento tem? | Na ficha do elemento (Estados) |
| 8 | Quais elementos viram componente na biblioteca do novo conceito? | Lista final de biblioteca |

## 2. Regiões padrão de uma tela

| Região | Posição | Conteúdo típico |
|---|---|---|
| A | Topo | Nome da sala, ações globais (criar, buscar, filtrar) |
| B | Centro | O quadro principal (kanban, lista, grade, tabela) — abas discretas de navegação |
| C | Lateral direita | Painel de detalhe do item selecionado (faixa vertical) |
| D | Base | *Opcional* — quadrinhos de apoio (insights, métricas, interlocutores). Adiar por padrão; só incluir se provar valor. |
| E | Overlays | Modais, confirmações, toasts |

## 3. Ficha padrão de elemento de UI (elementos puros)

Para CADA elemento da tela, preencher:

```
### 2.X [Nome do Elemento]
- **Elemento (biblioteca):** [nome do componente no novo conceito — não é nome do Blu atual]
- **Região:** A / B / C / D / E
- **Propósito:** [o que resolve para o usuário]
- **Conteúdo (informações):** [o que mostra e de onde vêm os dados]
- **Opções (dropdowns/menus):** [todas as escolhas possíveis, item por item]
- **Ações/Interações:** [clique, seleção múltipla, drag, hover, teclado — e o efeito de cada uma]
- **Estados visuais:** default / hover / selected / multiple-selected / disabled / loading / empty / error
- **Condições de visibilidade:** [quando aparece/esconde]
- **Feedback:** [toast, confirmação, notificação]
```

## 4. Checklist antes de considerar uma tela especificada

- [ ] Diagrama ASCII do layout
- [ ] Navegação por abas discretas (sem faixa horizontal)
- [ ] Cada região com seus elementos fichados
- [ ] Todos os dropdowns/menus com as opções explícitas
- [ ] Todos os botões/ações com efeito descrito
- [ ] Seleção múltipla + ações em lote onde fizer sentido (quadros)
- [ ] Estados vazio/loading/erro de cada lista e quadro
- [ ] Cada elemento descrito como **puro** (informação + ação) — sem referência ao design atual
- [ ] Lista de componentes da biblioteca (novo conceito) fechada
- [ ] Decisões em aberto listadas para o fundador validar
