# Estrutura de Documentos — Proposta v2 (revisada com o fundador)

**Profile:** design-writer
**Data:** 2026-08-18 (v2 — após discussão)
**Tipo:** spec de organização

---

## 1. Princípio revisado

- **Monorepo = tudo que é reutilizável em código.** Design systems (todos),
  telas (screens + wireframes), componentes, identidade visual. Importável de
  qualquer app; o usuário/produto escolhe o DS. É a fonte que constrói.
- **Projetos = tudo que comunica ou referencia.** Textos (copy library),
  apresentações, referências de design, documentação de negócio. Quem usa mais
  são os agentes (consultar, escrever proposta, preparar reunião) e podem ser
  reutilizados por outros agentes que trabalham em projetos/planejamento.

## 2. Monorepo — estrutura de design

```
monorepo/design/
├── design-systems/              ← TODOS os DS, importáveis por qualquer app
│   ├── README.md                ← catálogo: qual usar quando
│   ├── blu-novo/                ← DS do novo front Blu (multi-tema)
│   │   ├── DESIGN.md            ← tokens formais (lintado)
│   │   └── themes/              ← dark · azul · mono · warm
│   ├── formly/                  ← DS do Formly
│   ├── blu-original/            ← DS legado (glass roxo) — histórico
│   └── brand-hub/               ← identidade visual da empresa (tokens)
├── telas/                       ← telas + wireframes por produto
│   ├── blu/                     ← clientes, financeiro, mobile, estratégia…
│   ├── brain/                   ← memory_api: página do dono
│   └── formly/
└── componentes/                 ← tipos de componentes (UI kit por DS)
    ├── button/ pill/ card/ kanban…  (ex: pill → .pill por tema)
```

- Cada DS é um pacote importável (a pasta `libs/` do monorepo é o lugar natural
  se virar package; senão `design/design-systems/<nome>` com tokens publicados).
- Apps (`apps/blu_web`, `produtos/formly/frontend`, …) importam o DS — o usuário
  escolhe o tema (ex: dark/azul/mono/warm do Blu novo).
- Telas ficam junto do código porque o wireframe vira tela; o par
  wireframe + tela implementada mora no mesmo repo.
- Implementação segue a regra existente do monorepo: branch própria para design
  (ex: `docs/design-f3`), nunca em branch de fase em andamento.

## 3. Projetos — estrutura de comunicação e referência

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
│   ├── design-systems/          ← sistemas reais de referência (ex: opendesign,
│   │                              popular-web-designs — o que inspirar)
│   └── marcas/                  ← MESA.do, Zerezes e outras que o Lucas citou
├── apresentacoes/               ← PADRÃO de decks (negócio, reutilizável)
│   └── deck-empresa/            ← build_deck.py + roteiro + pptx/pdf
├── deepblue/                    ← materiais operacionais (posts, instagram, assets)
└── design/                      ← pasta ATUAL — migra (ver §5)
```

- **Textos**: cada produto/capability/serviço com 4 camadas (one-liner →
  parágrafo curto → parágrafo completo → bullets). Proposta, deck, site e posts
  puxam daqui; nunca reescrevem do zero. Voz = `deep-blue-voice`.
- **Referências**: coleção curada do que usar de inspiração (design systems
  reais, marcas de referência, templates opendesign). É o "acervo" que alimenta
  o design-writer quando o Lucas pede "me inspira nisso".
- **Apresentações**: todo deck nasce do gerador padrão (deck-empresa v3 = base).

## 4. Quem usa o quê

| Artefato | Quem usa | Onde |
|---|---|---|
| Design system (tokens, temas) | Código — apps importam | monorepo `design/design-systems/` |
| Telas / wireframes | Dev e design (viram tela) | monorepo `design/telas/` |
| Componentes | Código — apps importam | monorepo `design/componentes/` |
| Identidade visual (tokens) | Código + comunicação | monorepo `design/design-systems/brand-hub/` |
| Textos (descrições, capabilities) | Agentes (propostas, decks, posts) | projetos `textos/` |
| Apresentações | Agentes + Lucas (reuniões) | projetos `apresentacoes/` |
| Referências de design | Agentes (inspiração) | projetos `referencias/` |
| Materiais operacionais (posts) | Agentes + Lucas | projetos `deepblue/materiais/` |

## 5. O que acontece com a pasta atual `projetos-repo/design/`

| Pasta atual | Destino |
|---|---|
| `blu-novo-front/` (wireframes clientes/financeiro/mobile) | → monorepo `design/telas/blu/` |
| `blu-design-system/` (DS legado) | → monorepo `design/design-systems/blu-original/` |
| `blu-memory-api/` (página do dono) | → monorepo `design/telas/brain/` |
| `brand-hub/` (landing deepblue.company) | tokens/identidade → monorepo `design/design-systems/brand-hub/`; o SITE continua em projetos/Cloud Run (deploy não muda) |

**Migração em fases** (sem quebrar previews da 8899):
1. Fase 1 — criar `textos/` + `referencias/` no projetos (seed com o que já foi
   aprovado) e o README-mapa nos dois repos. Nada move.
2. Fase 2 — mover `apresentacoes/` (deck) para o lugar definitivo em projetos.
3. Fase 3 — criar `monorepo/design/` (branch própria) e migrar wireframes
   (`git mv` preserva histórico); atualizar symlinks do preview.
4. Fase 4 — formalizar DS `blu-novo` como pacote importável (tokens + temas) e
   apps passam a importar.

## 6. Decisões em aberto

1. O site **brand-hub** (deepblue.company): fica em projetos (deploy atual) com
   só os tokens no monorepo — ok? Ou ele também migra pro monorepo?
2. DS como **pacote importável**: formato `design/design-systems/<nome>` já
   serve, ou quer virar package em `libs/` (ex: `@deepblue/ds-blu-novo`)?
3. **Wireframes HTML** atuais entram no monorepo como `design/telas/` na Fase 3
   — confirma? (preview 8899 passa a apontar pro monorepo)
4. `deepblue/materiais/` (posts, instagram) continua como está — ok?
