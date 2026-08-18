# Proposta — Estrutura de Documentos (Design + Textos)

**Profile:** design-writer
**Data:** 2026-08-18
**Tipo:** spec de organização (proposta para aprovação do fundador)

---

## 1. Contexto

Precisamos de uma estrutura única, versionada e separada por tipo de documento,
para design e texto da Deep Blue. Gatilhos:

- O deck institucional v3 foi aprovado como **padrão de apresentações** — a
  estrutura que o gerou (fonte geradora + roteiro + pptx/pdf) precisa virar
  padrão, não caso isolado.
- Temos 4+ design systems espalhados (Formly, Blu original, Blu novo multi-tema,
  identidade da landing/brand-hub) sem um catálogo que diga **qual usar quando**.
- Textos de capabilities, produtos e serviços estão espalhados em skills,
  propostas e docs — sem uma biblioteca única que alimente propostas, deck e posts.
- Não está formalizada a regra do que vive no **monorepo** (construção) vs
  **projetos** (referência/comunicação).

## 2. Princípios

1. **Fonte única, referência por link** — cada artefato tem UM canônico; o resto aponta.
2. **Monorepo = construção. Projetos = referência e comunicação.** Design que vira
   código de produção mora no monorepo; design que documenta, prototipa ou
   apresenta mora no `projetos-repo/design/`. Texto que comunica mora em `textos/`.
3. **Design system é catálogo, não pasta solta** — cada DS tem tokens + quando usar.
4. **Texto em camadas** — cada produto/capability/serviço tem o texto em 4 tamanhos
   (one-liner → parágrafo completo) para qualquer artefato puxar o tamanho certo.
5. **Apresentação é padrão, não evento** — todo deck nasce do mesmo gerador
   (`build_deck.py`), mesma identidade, mesmo roteiro.

## 3. Onde cada coisa mora

| Tipo | Lugar | Exemplo |
|---|---|---|
| Tokens/temas de produção (CSS vars, DESIGN.md lintado, themes) | **monorepo** `apps/*/src/styles`, `theme/`, branch `docs/design-f3` para docs | `apps/blu_web/src/styles/global.css` |
| Componentes implementados (código) | **monorepo** `apps/*/src/components` | `blu_web` AppShell, Sidebar |
| Wireframes e protótipos HTML (referência de produto) | **projetos-repo** `design/telas/` | sala Clientes, Financeiro, mobile |
| Design systems catalogados (tokens + quando usar) | **projetos-repo** `design/design-systems/` | Formly, Blu original, Blu novo |
| UI kits / componentes descartáveis (protótipo) | **projetos-repo** `design/componentes/` | pills, kanban, cards |
| Brand/hub da empresa (landing) | **projetos-repo** `design/brand-hub/` | deepblue.company |
| Apresentações (padrão) | **projetos-repo** `design/apresentacoes/` | deck-empresa |
| Copy library (capabilities, produtos, serviços, exemplos) | **projetos-repo** `textos/` | `textos/produtos/blu.md` |
| Materiais operacionais (posts, instagram, assets) | **projetos-repo** `deepblue/materiais/` | posts LinkedIn |
| Documentos ricos colaborativos | **Google Drive** `Hermes - Entregáveis/` | Slides, planilhas |

## 4. Estrutura alvo de `projetos-repo/design/`

```
design/
├── README.md                     ← mapa + regra monorepo × projetos
├── design-systems/               ← catálogo: QUAL USAR QUANDO
│   ├── README.md                 ← tabela de DS + regra de decisão
│   ├── formly/                   ← DS Formly (canônico: monorepo/produtos/formly)
│   ├── blu-original/             ← DS Blu legado (glass roxo #8C5FDB)
│   ├── blu-novo/                 ← DS Blu novo multi-tema (dark/azul/mono/warm)
│   │   ├── DESIGN.md             ← tokens formais (lintado)
│   │   └── themes/               ← dark, azul, mono, warm (blocos de tokens)
│   └── brand-hub/                ← identidade landing da empresa (#F2F2F0 claro)
├── telas/                        ← wireframes/protótipos por produto
│   ├── blu/                      ← clientes, financeiro, mobile, estratégia…
│   ├── brain/                    ← memory_api: página do dono
│   └── formly/                   ← telas do questionário
├── componentes/                  ← UI kits por DS (protótipo, descartável)
│   └── README.md                 ← índice: componente → DS → arquivo
├── apresentacoes/                ← PADRÃO de apresentações
│   └── deck-empresa/             ← build_deck.py + roteiro + pptx/pdf (v3 = base)
└── assets/                       ← logo, paleta, fontes da empresa
```

### Catálogo de design systems (estado atual → destino)

| DS | Hoje | Destino | Quando usar |
|---|---|---|---|
| Formly | skill `formly-design`; canônico `monorepo/produtos/formly/frontend` | `design-systems/formly/` (referência + link p/ canônico) | Produto Formly |
| Blu original | `design/blu-design-system/` (legado repo_platform) | `design-systems/blu-original/` | NADA novo — manter só como histórico |
| Blu novo | `design/blu-novo-front/` (wireframes); tokens em `monorepo/apps/blu_web` | `design-systems/blu-novo/` (DESIGN.md + themes) + `telas/blu/` (wireframes) | Todo o novo front Blu (4 temas) |
| Brand-hub / identidade empresa | `design/brand-hub/` | `design-systems/brand-hub/` | Landing, deck, materiais da empresa |

> **Nota:** "Warrami" = tema **warm** do Blu novo (fundo `#FBF1E7`, accent `#C2410C`).
> Fica catalogado como um dos 4 temas em `design-systems/blu-novo/themes/warm`.

## 5. Copy library — `projetos-repo/textos/`

```
textos/
├── README.md                     ← como usar (camadas, voz, atualização)
├── produtos/                     ← por produto: BLU, FORMly, BRAIN MCP
│   └── blu.md                    ← 4 camadas de texto (ver abaixo)
├── capabilities/                 ← o que a Deep Blue faz
│   ├── plataforma.md
│   ├── fluxos-de-agentes.md
│   ├── assistente-diario.md
│   └── consultoria.md
├── servicos/                     ← serviços prestados (Consulting)
│   ├── ai-readiness.md
│   ├── pilot-program.md
│   └── transformation-roadmap.md
├── exemplos/                     ← textos do Lucas (padrão ouro, para inspirar)
│   └── landing-empresa.md        ← copy do doc "Sua operação já funciona"
└── apresentacao/                 ← estrutura padrão do deck (12 slides) + roteiro
```

**Camadas de texto por arquivo (obrigatório):**
1. **One-liner** (~10 palavras) — hero, card, post.
2. **Parágrafo curto** (2–3 frases) — seção, proposta, site.
3. **Parágrafo completo** — drawer, página de produto, proposta detalhada.
4. **Bullets de features** — o que entrega, em lista.

Regra: todo texto novo de produto/capability entra aqui primeiro; proposta, deck,
site e posts **puxam** daqui (nunca reescrevem do zero). Voz = skill
`deep-blue-voice` (anti-hype, cliente como herói, dados reais).

## 6. Padrão de apresentações

- Canônico: `design/apresentacoes/deck-empresa/` → `build_deck.py` (gerador),
  `deck-empresa-v3.md` (roteiro slide a slide + notas), `*.pptx` + `*.pdf`.
- **Como criar um deck novo:** copiar a pasta `deck-empresa`, editar copy no
  roteiro, ajustar o gerador, rodar `build_deck.py`, renderizar, subir pro Drive
  (`Hermes - Entregáveis/Apresentações`).
- Identidade fixa: landing clara (`#F2F2F0`, `#1D4ED8`, Instrument Serif itálico
  no termo-chave, kickers JetBrains Mono).
- O `deepblue/apresentacoes/deck-empresa` (atual) migra para cá.

## 7. Migração (fases — sem quebrar previews)

1. **Fase 1 (agora):** criar `design/README.md` (mapa + regra) e o catálogo
   `design-systems/README.md` apontando para as pastas atuais — SEM mover arquivos.
   Criar `textos/` com os primeiros arquivos (seed a partir do que já foi aprovado:
   landing, deck, produtos.md).
2. **Fase 2:** mover `deck-empresa` para `design/apresentacoes/` e ajustar links
   (STATUS, symlinks do preview 8899).
3. **Fase 3:** renomear pastas atuais para o layout alvo (`blu-novo-front` →
   `telas/blu` + `design-systems/blu-novo`), mantendo `index.html`/`README` de
   transição. Renomeações com `git mv` (histórico preservado).
4. **Fase 4:** formalizar `design-systems/blu-novo/DESIGN.md` (lintado) no monorepo
   branch `docs/design-f3` — o canônico de tokens que alimenta o código.

> Previews: o symlink `drafts/proposals/blu-site` → `design/blu-novo-front` só
> muda na Fase 3; até lá nada quebra.

## 8. Decisões em aberto (preciso do seu ok)

1. Aprova a divisão **monorepo = construção / design = referência / textos = copy**?
2. Copy library em `projetos-repo/textos/` (top-level) ou dentro de `deepblue/`?
3. Renomear `design/blu-novo-front` → `telas/blu` + `design-systems/blu-novo` na
   Fase 3, ou manter o nome atual (menos churn, estrutura nova só p/ o que nasce
   daqui pra frente)?
4. O `deepblue/` fica só com materiais operacionais (posts, instagram, assets)?
