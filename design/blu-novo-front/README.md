# Blu — Novo Front (blu_web v2) · Protótipos

> O novo front re-casca as mesmas funções do monorepo (`apps/blu_web`): rotinas
> com gatilhos, aprovações com semáforo, segmentos, analytics 30d/90d/1y.
> **A função não muda, a casca muda.** Multi-tema por design: Dark (canônico),
> Azul, Mono, Warm — mesma arquitetura de tokens, só os valores mudam.

## Artefatos

| Arquivo | O que é | Como ver |
|---|---|---|
| `DESIGN.md` | Tokens e regras do sistema (cores, tipografia, componentes, Do's & Don'ts, riscos de a11y) | — |
| `clientes-v2.html` | **Exploração visual 14/08** — sala Clientes com design enriquecido: ambient por tema, gradiente de marca (avatares/ícone da sala/sidebar ativa), kanban com hover lift + badge com dot, painel com sparklines quietos + timeline com dots, bottom strip com delta + 1 gráfico quieto, tabs com ícones. Comparar com `wireframe.html` | `/blu-site/clientes-v2.html` |
| `wireframe.html` | Wireframe v3 — protótipo interativo completo do novo front (Cliente · Pipeline, orçamentos, follow-up). 4 temas. Revisado 14/08: tabs sem underline (padrão A2.1 do Financeiro), dots de coluna por tema (`--col-*`), métricas do bottom strip mudam por aba, ação sugerida em Phosphor | `/blu-site/` (index via redirect) |
| `financeiro.html` | Sala Financeiro — referência de sala: 5 abas (Decisões · Processos · Fluxo · Contas · Rotinas), painel contextual 380px master-detail, permissões por sala (Aprovador/Criador/Visualizador). Regras em destaque: sem strip de métricas no topo (U9), permissões (D3/U6) | `/blu-site/financeiro.html` |
| `blu-clientes-opcoes.html` | ⚠️ LEGADO — semente `.dc.html` da ferramenta de prototipagem (runtime `support.js`/`_ds/` não versionado; **não renderiza no preview**). Conteúdo absorvido pelo `wireframe.html` | não serve |
| `mobile.html` | **Versão mobile do novo front** — conceito de casca mobile navegável em frame de telefone (no celular real, ocupa a tela toda). Bottom nav 5 destinos, decisão em bottom sheet (r20), detalhe master-detail em slide-in, salas em grid, pills de config em rotinas, 4 temas | `/blu-site/mobile.html` |

## Mobile — decisões de casca (mobile.html)

- **Sidebar → bottom nav fixa**: Início · Decisões (badge) · Salas · Atividade · Conta.
- **Salas em grid 2 col** com agent colors por tema (`--ag-*` tokens — Dark neon, Azul profundo, Mono grayscale, Warm terroso).
- **Decisão → bottom sheet** (raio 20px, `rounded.lg` da spec) com Aprovar / Adiar / Ver detalhes.
- **Painel contextual 380px → tela de detalhe slide-in** com voltar (breadcrumb vira navegação push).
- **Kanban → lista vertical por etapa** (arrastar no toque é frágil; a lista mantém a semântica do quadro).
- **Abas da sala → pills horizontais scrolláveis**.
- **Rotinas**: a tab mostra o configurado (freq · dias · hora · canal em pills); o detalhe edita a config com pills pré-preenchidas (Gatilho Manual/Agenda/Evento/Métrica, Frequência, Dias quando Semanal, Horário, Canal) + Salvar; builder "Nova rotina" com as mesmas pills.
- **Sem strip de métricas no topo** (U9 mantida) — KPIs só na Home (carrossel com snap).
- Touch ≥44px · safe-area (home indicator) · mono p/ números · sem emoji (Phosphor).

## Deep links do mobile

`#decisoes` · `#salas` · `#atividade` · `#conta` · `#sala` · `#processos` · `#fluxo` ·
`#contas` · `#rotinas` · `#builder` · `#rotina-r1` (detalhe de rotina) · `#d1` (sheet de decisão) ·
tema no hash: `#salas-warm`, `#rotinas-azul`, `#rotina-r4-warm`

## Preview

Servido em `http://100.69.231.7:8899/blu-site/` (root = `drafts/proposals` do
profile; `blu-site` é symlink para este diretório — editar aqui, commitar,
o preview reflete na hora). `/blu-site/` abre `wireframe.html` via `index.html`
(redirect). Screenshots mobile: `previews/blu-mobile/`.

## Regras da spec (resumo)

- Copy pt-BR, segunda pessoa "você", CTA com verbo.
- Phosphor icons regular — **emoji proibido em UI**.
- JetBrains Mono + tabular-nums para todo número/valor/timestamp.
- Superfície glass: `rgba(255,255,255,.065)` + blur(16px) + borda 1px.
- Raio `lg` (20px) só para bottom sheets mobile.
- Não introduzir cor fora das 4 paletas; não aninhar variantes de componente.
- Transições ease-out, snappy (0.10–0.20s). Sem sombra em cards em repouso (sombra é dos painéis).
