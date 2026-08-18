# Estrutura de Documentos — Proposta v3 (FINAL)

**Profile:** design-writer
**Data:** 2026-08-18 (v3 — decisões fechadas com o fundador)
**Tipo:** spec de organização

---

## 1. Princípio

- **Monorepo = tudo que é reutilizável em código.** Design systems (todos),
  telas (screens + wireframes), componentes, identidade visual. Importável de
  qualquer app; o usuário/produto escolhe o DS. É a fonte que constrói.
- **Projetos = tudo que comunica ou referencia.** Textos (copy library),
  apresentações, referências de design, documentação de negócio. Usado pelos
  agentes ao produzir propostas, decks e posts; reutilizável por outros agentes
  de planejamento.

## 2. Monorepo — design reutilizável

```
monorepo/design/
├── design-systems/              ← TODOS os DS, importáveis (formato: pasta por DS)
│   ├── README.md                ← catálogo: qual usar quando
│   ├── blu-novo/                ← DS do novo front Blu (multi-tema)
│   │   ├── DESIGN.md            ← tokens formais (lintado)
│   │   └── themes/              ← dark · azul · mono · warm
│   ├── formly/                  ← DS do Formly
│   ├── blu-original/            ← DS legado (glass roxo) — histórico
│   └── brand-hub/               ← identidade da empresa — tokens do site
│                                  (candidato: tema claro do Blu — ver §6.1)
├── telas/                       ← telas + wireframes por produto
│   ├── blu/                     ← clientes, financeiro, mobile, estratégia…
│   ├── brain/                   ← memory_api: página do dono
│   └── formly/
└── componentes/                 ← tipos de componentes (UI kit por DS)
```

- Site canônico da empresa: `monorepo/apps/brand-hub` (deploy já existe:
  `scripts/local/deploy-brand-hub.sh`). O **design system brand-hub** nasce dos
  tokens desse site.
- Apps importam os DS da pasta `design/design-systems/<nome>` (pacote
  `libs/` desnecessário — formato de pasta aprovado).

## 3. Projetos — comunicação e referência

```
projetos-repo/
├── textos/                      ← COPY LIBRARY (linguagem da casa)
│   ├── README.md                ← como usar (camadas + voz)
│   ├── produtos/                ← blu.md, formly.md, brain-mcp.md (4 camadas)
│   ├── capabilities/            ← plataforma.md, fluxos-de-agentes.md,
│   │                              assistente-diario.md, consultoria.md
│   ├── servicos/                ← ai-readiness.md, pilot-program.md, roadmap.md
│   ├── exemplos/                ← textos do Lucas (padrão ouro)
│   └── apresentacao/            ← estrutura padrão do deck (12 slides)
├── referencias/                 ← REFERÊNCIAS DE DESIGN p/ criar
│   ├── README.md                ← índice
│   ├── design-systems/          ← opendesign, sistemas reais, o que inspirar
│   └── marcas/                  ← MESA.do, Zerezes e outras citadas
├── apresentacoes/               ← PADRÃO de decks (negócio, reutilizável)
│   └── deck-empresa/            ← build_deck.py + roteiro + pptx/pdf
├── deepblue/materiais/          ← operacional (posts, instagram)
│   └── assets/                  ← subpastas por tipo: logo/ icons/ fonts/ social/
└── design/                      ← pasta ATUAL — migra para o monorepo (ver §5)
```

## 4. Quem usa o quê

| Artefato | Quem usa | Onde |
|---|---|---|
| Design system (tokens, temas) | Código — apps importam | monorepo `design/design-systems/` |
| Telas / wireframes | Dev e design (viram tela) | monorepo `design/telas/` |
| Componentes | Código — apps importam | monorepo `design/componentes/` |
| Identidade visual (tokens) | Código + comunicação | monorepo `design/design-systems/brand-hub/` |
| Site da empresa | Deploy (já existe) | monorepo `apps/brand-hub` |
| Textos (descrições, capabilities) | Agentes (propostas, decks, posts) | projetos `textos/` |
| Apresentações | Agentes + Lucas (reuniões) | projetos `apresentacoes/` |
| Referências de design | Agentes (inspiração) | projetos `referencias/` |
| Materiais operacionais (posts) | Agentes + Lucas | projetos `deepblue/materiais/` |

## 5. Destino da pasta atual `projetos-repo/design/`

| Pasta atual | Destino |
|---|---|
| `blu-novo-front/` (wireframes clientes/financeiro/mobile) | → monorepo `design/telas/blu/` ✅ |
| `blu-design-system/` (DS legado) | → monorepo `design/design-systems/blu-original/` |
| `blu-memory-api/` (página do dono) | → monorepo `design/telas/brain/` |
| `brand-hub/` (protótipo) | site canônico já é `monorepo/apps/brand-hub`; tokens → `design-systems/brand-hub/` |

**Migração em fases** (sem quebrar previews da 8899):
1. Fase 1 (feita) — `textos/` + `referencias/` criados no projetos (seed); mapa nos repos.
2. Fase 2 — mover `apresentacoes/` (deck) para o lugar definitivo em projetos.
3. Fase 3 — criar `monorepo/design/` (branch própria) e migrar wireframes
   (`git mv` preserva histórico); atualizar symlinks do preview. ✅ aprovado
4. Fase 4 — formalizar DS `blu-novo` + `brand-hub` (tokens lintados) e apps
   passam a importar.

## 6. Decisões fechadas (18/08)

1. **Brand-hub:** o site já vive no monorepo (`apps/brand-hub`); os tokens
   viram um design system também — candidato: **tema claro do Blu**.
2. **Formato DS:** pasta `design/design-systems/<nome>` — ✅ (sem pacote `libs/`).
3. **Wireframes HTML:** entram no monorepo como `design/telas/` na Fase 3 — ✅.
4. **`deepblue/materiais/`:** mantém; `assets/` ganha subpastas por tipo
   (`logo/`, `icons/`, `fonts/`, `social/`) — ✅.

### 6.1 Em aberto (decisão leve, pode ser na Fase 4)

- Os tokens do site (identidade clara `#F2F2F0`/`#1D4ED8`) viram um DS próprio
  `brand-hub/` ou o **5º tema** do `blu-novo/` ("claro")? Caminho sugerido:
  começar como `design-systems/brand-hub/` (identidade da empresa) e, se o app
  Blu adotar, promover a tema do blu-novo.
