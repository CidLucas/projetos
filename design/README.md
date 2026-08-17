# Design — índice geral

Todos os artefatos de design do Blu concentrados aqui. Cada subpasta tem seu
próprio README ou é autoexplicativa. Preview dos protótipos servido em
`http://100.69.231.7:8899/` (raiz = `~/.hermes/profiles/writer/drafts/proposals`,
com symlink para `design/blu-novo-front`).

## Conjuntos

| Pasta | Conteúdo | Fonte canônica |
|---|---|---|
| `blu-novo-front/` | Novo front (blu_web v2): DESIGN.md (tokens multi-tema), wireframe v3 (Cliente), sala Financeiro (referência de sala), opções de Clientes, **mobile.html** (casca mobile navegável) + README | **esta pasta** (movida de `drafts/blu-site`) |
| `blu-design-system/` | Design system do app: 10 HTML de referência (charts, tables, cards/kanban, chat, forms, navigation shell, docs financeiros, estratégia, v3) | snapshot de `monorepo/docs/design-system` |
| `blu-memory-api/` | Design da página do dono (Memory API / F3): `pagina-do-dono.html`, index, blu.css | snapshot de `monorepo/docs/memory_api/referencia` |
| `brand-hub/` | Hub de marca (Deep Blue → produtos): **SPEC.md** (spec de desenvolvimento) + `index.html` (protótipo navegável — empresa + Blu + Formly + Brain) | **esta pasta** |

## Novo front — atalhos

- Wireframe v3 (Cliente): `blu-novo-front/wireframe.html`
- Sala Financeiro (referência): `blu-novo-front/financeiro.html`
- Mobile (casca mobile, frame de telefone): `blu-novo-front/mobile.html`
  - Deep links: `#decisoes #salas #atividade #conta #sala #processos #fluxo #contas #rotinas #builder #rotina-r1 #d1`
  - Tema no hash: `#salas-warm`, `#rotinas-azul`, `#rotina-r4-warm`
- Spec/tokens: `blu-novo-front/DESIGN.md` · índice do conjunto: `blu-novo-front/README.md`

## Fluxo de trabalho

- Trabalho de design novo → editar aqui e commitar.
- Preview: `design/blu-novo-front` está espelhado via symlink em
  `drafts/proposals/blu-site` (servido na 8899).
- Screenshots de validação: `previews/blu-mobile/` (fora do repo, descartáveis).
