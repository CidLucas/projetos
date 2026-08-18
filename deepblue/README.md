# Deep Blue — Materiais da Empresa

**Profile:** design-writer
**Data:** 2026-08-18
**Tipo:** estrutura de materiais corporativos

---

## Objetivo

Lugar único e versionado para os materiais da própria Deep Blue:
apresentações, posts de redes sociais e assets gráficos. O texto/copy segue a
Voz Deep Blue (`deep-blue-voice`); o visual segue a identidade do site
(dark `#080C1A`, accent `#3B82F6`, Plus Jakarta Sans + Inter).

## Estrutura

```
deepblue/
├── README.md                        ← este arquivo
├── STATUS.md                        ← o que está pronto / em andamento
├── apresentacoes/
│   └── deck-empresa/                ← deck institucional (pptx + pdf + roteiro md)
├── materiais/
│   ├── linkedin/                    ← posts (markdown + imagem quando houver)
│   ├── instagram/                   ← posts gráficos (svg/png)
│   └── assets/                      ← logo, paleta, fontes, elementos
└── docs/
    └── 00-estrutura-materiais.md    ← regras e fluxo dos materiais
```

## Regras

1. **Repo central:** `CidLucas/projetos` → pasta `deepblue/` (este slug).
   Nunca criar repo separado para materiais da empresa.
2. **Rascunhos em iteração:** `~/.hermes/profiles/design-writer/drafts/`
   (ex: `drafts/presentations/deck-empresa/`). O que for aprovado vai para cá.
3. **Copy:** qualquer texto passa pela Voz Deep Blue (anti-hype, cliente como
   herói, IA como ferramenta, dados reais).
4. **Deck:** fonte geradora + pptx + pdf de preview + roteiro em markdown
   (texto slide a slide com notas do apresentador).
5. **Antes de editar:** `git fetch origin main` (repo tem clones paralelos;
   escopo muda sem aviso).
