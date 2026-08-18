# Estrutura de Materiais da Deep Blue

**Profile:** design-writer
**Data:** 2026-08-18
**Tipo:** spec de organização

---

## Objetivo

Definir onde cada material da empresa nasce, vive e é entregue. Um único
padrão para apresentações, posts e gráficos — sem arquivo perdido em pasta
de outro projeto.

## Mapa de armazenamento (como está hoje)

| O que | Onde | Formato |
|---|---|---|
| Materiais da empresa (deck, posts, assets) | `projetos-repo/deepblue/` (repo CidLucas/projetos) | pptx/pdf/md/svg |
| Rascunhos em iteração | `~/.hermes/profiles/design-writer/drafts/` (local, fora do git) | html/py/md |
| Propostas de cliente | `projetos-repo/<slug-do-cliente>/` | html→Google Docs |
| Design de produtos (Blu, Formly, Brain, brand-hub) | `projetos-repo/design/<projeto>/` | html/DESIGN.md |
| Site corporativo (brand-hub) | `projetos-repo/design/brand-hub/` (branch feat/brand-hub até aprovação) | html |
| Preview HTML na tailnet | `http://100.69.231.7:8081/<projeto>/` | html |

## Estrutura de materiais

```
projetos-repo/deepblue/
├── apresentacoes/
│   └── deck-empresa/
│       ├── deck-empresa-v1.pptx      ← deck editável
│       ├── deck-empresa-v1.pdf       ← preview fiel
│       └── deck-empresa-v1.md        ← roteiro: texto + notas por slide
├── materiais/
│   ├── linkedin/                     ← posts (01-titulo.md + imagem quando houver)
│   ├── instagram/                    ← posts gráficos (01-titulo.png/svg)
│   └── assets/                       ← logo, paleta, fontes, ícones
└── docs/                             ← specs e regras (numerados 00-, 01-…)
```

## Regras por tipo de material

### Apresentações (deck institucional, pitches, reuniões)

1. Fonte geradora fica no repo junto do pptx (ex: `build_deck.py`) — deck se
   regenera, não vira caixa-preta.
2. Roteiro em markdown com texto slide a slide + notas do apresentador.
3. Revisão de copy SEMPRE na Voz Deep Blue antes de fechar.
4. Fluxo: `drafts/presentations/` → aprovação do Lucas → `deepblue/apresentacoes/`
   → commit → (opcional) Google Slides/Drive para edição colaborativa.

### Posts LinkedIn

1. Arquivo markdown por post: `materiais/linkedin/01-titulo.md`.
2. Estrutura do post: gancho → dor → abordagem Deep Blue → CTA. Frases curtas,
   travessões com critério, dados reais quando houver.
3. Título do arquivo começa com número sequencial; pasta é o calendário.

### Posts Instagram

1. Gráfico por post em `materiais/instagram/` (png/svg) + legenda em markdown.
2. Identidade: dark `#080C1A`, accent `#3B82F6`, Plus Jakarta Sans + Inter,
   círculos concêntricos da marca. Um gráfico quieto por peça — sem poluição.

### Assets

1. Logo (SVG círculos concêntricos + two-tone wordmark), paleta, fontes e
   ícones (Phosphor) em `materiais/assets/`.
2. Emoji é proibido em UI; ícones Phosphor.

## Fluxo de trabalho

1. Nasceu em `drafts/` → itera com o Lucas → vira artefato em `deepblue/`.
2. Todo artefato commitado no repo central (versionado).
3. STATUS.md do slug sempre reflete o estado atual.

## Próximos passos

- [ ] Revisão do Lucas no deck v1
- [ ] Primeiros 3 posts LinkedIn
- [ ] Primeiros 3 gráficos Instagram
- [ ] Definir se deck vai para Google Slides (colaborativo) ou só pptx/pdf
