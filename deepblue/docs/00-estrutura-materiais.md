# Estrutura de Materiais da Deep Blue

**Profile:** design-writer
**Data:** 2026-08-18 (atualizado na Fase 2)
**Tipo:** spec de organização

---

## Objetivo

Definir onde cada material da empresa nasce, vive e é entregue. Um único
padrão para apresentações, posts e gráficos — sem arquivo perdido em pasta
de outro projeto.

## Mapa de armazenamento

| O que | Onde | Formato |
|---|---|---|
| Apresentações (padrão de decks) | `projetos-repo/apresentacoes/deck-empresa/` | pptx/pdf/md/py |
| Copy library (produtos, capabilities, serviços, exemplos) | `projetos-repo/textos/` | md (4 camadas) |
| Referências de design | `projetos-repo/referencias/` | md |
| Materiais operacionais (posts, instagram, assets) | `projetos-repo/deepblue/materiais/` | md/svg/png |
| Design reutilizável (DS, telas, componentes) | **monorepo** `design/` (migração Fase 3) | html/css/ts |
| Site corporativo (brand-hub) | **monorepo** `apps/brand-hub` | html |
| Propostas de cliente | `projetos-repo/<slug-do-cliente>/` | html→Google Docs |
| Rascunhos em iteração | `~/.hermes/profiles/design-writer/drafts/` (local) | html/py/md |
| Preview HTML na tailnet | `http://100.69.231.7:8899/<projeto>/` | html |

## Estrutura de materiais (pós Fase 2)

```
projetos-repo/
├── apresentacoes/                 ← PADRÃO de decks
│   ├── README.md                  ← como criar deck novo
│   └── deck-empresa/              ← build_deck.py + roteiro + pptx/pdf
├── textos/                        ← copy library (4 camadas)
│   ├── produtos/ capabilities/ servicos/ exemplos/ apresentacao/
├── referencias/                   ← acervo de inspiração (design-systems, marcas)
└── deepblue/
    ├── materiais/                 ← operacional
    │   ├── linkedin/              ← posts (01-titulo.md)
    │   ├── instagram/             ← posts gráficos (01-titulo.png/svg)
    │   └── assets/                ← logo/ icons/ fonts/ social/
    └── docs/                      ← specs e regras (00-, 01-…)
```

## Regras por tipo de material

### Apresentações (deck institucional, pitches, reuniões)

1. Nascem do gerador padrão (`apresentacoes/deck-empresa/build_deck.py`) —
   copia a pasta, edita roteiro, roda o gerador.
2. Roteiro em markdown com texto slide a slide + notas do apresentador.
3. Revisão de copy SEMPRE na Voz Deep Blue antes de fechar.
4. Fluxo: `drafts/presentations/` → aprovação do Lucas → `apresentacoes/`
   → commit → Google Slides (`Hermes - Entregáveis/Apresentações`).

### Posts LinkedIn

1. Arquivo markdown por post: `materiais/linkedin/01-titulo.md`.
2. Estrutura do post: gancho → dor → abordagem Deep Blue → CTA. Frases curtas,
   travessões com critério, dados reais quando houver.
3. Copy puxa de `textos/` (camada one-liner/curto), não reescreve do zero.

### Posts Instagram

1. Gráfico por post em `materiais/instagram/` (png/svg) + legenda em markdown.
2. Identidade: **landing clara** (`#F2F2F0` canvas, `#1D4ED8` accent, Plus
   Jakarta Sans + Instrument Serif, kickers JetBrains Mono). Um gráfico quieto
   por peça — sem poluição.

### Assets

1. Subpastas por tipo em `materiais/assets/`: `logo/`, `icons/`, `fonts/`,
   `social/`.
2. Logo (SVG círculos concêntricos + wordmark), paleta e ícones Phosphor.
3. Emoji é proibido em UI; ícones Phosphor.

## Fluxo de trabalho

1. Nasceu em `drafts/` → itera com o Lucas → vira artefato no repo.
2. Todo artefato commitado no repo central (versionado).
3. Texto novo de produto/capability entra em `textos/` ANTES de ser usado.

## Próximos passos

- [x] Fase 1 — textos/, referencias/, assets com subpastas
- [x] Fase 2 — apresentacoes/ no lugar definitivo
- [ ] Fase 3 — monorepo `design/` (DS, telas, componentes)
- [ ] Primeiros 3 posts LinkedIn (puxando da copy library)
- [ ] Primeiros 3 gráficos Instagram
