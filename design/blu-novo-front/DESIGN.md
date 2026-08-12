---
version: alpha
name: Blu Design System
description: >-
  Blu é o escritório virtual com IA para PMEs brasileiras. Sistema multi-tema:
  4 paletas (Dark, Azul, Mono, Warm) sobre um shell consistente — topbar 68px,
  sidebar 90px, glassmorphism, semântica de status verde/amarelo/vermelho.
  Fonte canônica: monorepo apps/blu_web (src/styles/global.css).
colors:
  primary: "#03071C"
  secondary: "#DFE3EE"
  tertiary: "#8C5FDB"
  neutral: "#0F1222"
  on-primary: "#DFE3EE"
  on-tertiary: "#FFFFFF"
  success: "#10B981"
  warning: "#F59E0B"
  danger: "#EF4444"
typography:
  h1:
    fontFamily: Inter
    fontSize: 1.75rem
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  h2:
    fontFamily: Inter
    fontSize: 1.25rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  body-md:
    fontFamily: Inter
    fontSize: 0.8125rem
    lineHeight: 1.5
  label-caps:
    fontFamily: Inter
    fontSize: 0.625rem
    fontWeight: 700
    letterSpacing: "0.08em"
  mono:
    fontFamily: JetBrains Mono
    fontSize: 0.8125rem
    lineHeight: 1.5
rounded:
  sm: 8px
  md: 12px
  lg: 20px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-tertiary}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  button-secondary:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  panel:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    padding: 16px
  kanban-card:
    backgroundColor: "#0B0E1E"
    textColor: "{colors.secondary}"
    rounded: "{rounded.sm}"
    padding: 10px 11px
  pill:
    backgroundColor: "rgba(255,255,255,0.065)"
    textColor: "{colors.secondary}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  pill-on:
    backgroundColor: "rgba(140,95,219,0.15)"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  badge-success:
    backgroundColor: "rgba(16,185,129,0.13)"
    textColor: "{colors.success}"
    rounded: "{rounded.full}"
    padding: 2px 7px
  badge-warning:
    backgroundColor: "rgba(245,158,11,0.13)"
    textColor: "{colors.warning}"
    rounded: "{rounded.full}"
    padding: 2px 7px
  badge-danger:
    backgroundColor: "rgba(239,68,68,0.13)"
    textColor: "{colors.danger}"
    rounded: "{rounded.full}"
    padding: 2px 7px
---

## Overview

Blu é um bureau de agentes de IA que trabalha **para** o dono de PME — nunca
"faz por ele". O produto espera aprovação humana antes de agir. O design
comunica isso com calma e autoridade: superfícies de vidro (glassmorphism),
dados em mono com tabular-nums, semântica clara de status, e hierarquia que
coloca a decisão do humano no centro.

**A função não muda, a casca muda.** O novo front (blu_web v2) re-casca as
mesmas funções que já rodam no monorepo — rotinas com gatilhos (manual,
agenda, evento, métrica), pills de frequência (Diário/Semanal/Mensal) e dias,
aprovações com semáforo, segmentos de cliente, analytics por período
(30d/90d/1y). Este DESIGN.md formaliza os tokens e componentes para a nova
casca.

O sistema é **multi-tema por design**: 4 paletas equivalentes em função e
contraste — **Dark** (identidade canônica, rodando hoje), **Azul**, **Mono**
e **Warm** (direções light-first da nova casca). A arquitetura de tokens é
idêntica entre temas; só os valores mudam. Trocar de tema não muda layout,
tipografia, raios ou densidade.

Todo copy em português brasileiro, tom direto e empoderador, segunda pessoa
"você". Emojis são proibidos em UI — ícones são Phosphor (regular).

## Colors

### Tema Dark (canônico — produção, monorepo)

- **Primary (#03071C):** Fundo noturno profundo — "escritório à noite".
  Radiais suaves de glow azul/índigo nos cantos para dar profundidade.
- **Tertiary (#8C5FDB):** "Roxo Blu" — o acento de interação. Hover: `#a07ae8`
  (`--ac-hi`). Gradiente da marca `135deg #7E5CC8 → #3A80D4`.
- **Superfície (--glass):** `rgba(255,255,255,0.065)` + blur(16px) + borda
  `rgba(255,255,255,0.10)` — o vidro do sistema.
- **Semântica:** success `#10B981`, warning `#F59E0B`, danger `#EF4444`, cada
  uma com variante dim (`--odim/--adm2/--udim`) para fundos de destaque.
- **Acento de agentes/salas:** indigo `#818cf8`, pink `#f472b6`, teal
  `#2dd4bf`, orange `#fb923c`, violet `#a78bfa`, yellow `#fbbf24`.

### Tema Azul (light)

- Fundo `#F5F9FE`, superfície `rgba(255,255,255,.85)`, texto `#0F2A43`.
- Acento `#2563EB` (blue-600). Semântica: ok `#059669`, att `#C2760A`,
  urg `#DC2626`.
- Glows ambientes azuis suaves. Sombras azuladas com inset highlight branco.

### Tema Mono (light)

- Fundo `#FFFFFF`, superfície `rgba(255,255,255,.92)`, texto `#0A0A0A`.
- Acento `#111111` — o contraste é o design. Semântica deep: ok `#166534`,
  att `#92400E`, urg `#B91C1C`.
- Sem ambient, sem gradientes. Estética editorial (princípio Zerezes).

### Tema Warm (light)

- Fundo `#FBF1E7`, superfície `rgba(255,250,244,.85)`, texto `#3A2415` —
  "papel quente".
- Acento `#C2410C`. Semântica: ok `#65792B` (oliva), att `#B45309`,
  urg `#B91C1C`.
- Glows ambientes laranja/marrom suaves. Acolhedor, artesanal.

## Typography

**Inter** para tudo — hierarquia vem de peso e tamanho, não de famílias.
**JetBrains Mono** exclusivamente para números, timestamps, IDs e valores
monetários, sempre `font-variant-numeric: tabular-nums`. Base 13px,
line-height 1.5. Headlines com tracking negativo apertado (-1px a -2px),
peso 800. Labels de painel em caps 9.5-10px/700/.08em. Eyebrows
11px/700/uppercase/.1em na cor do acento.

## Layout

Shell fixo: topbar 68px (`--th`) + sidebar 90px (`--sw`), conteúdo à direita.
Sidebar: 10 salas com ícone Phosphor 22px regular (Início, Compras,
Financeiro, Agenda, Estratégia, Clientes, Biblioteca, Atividade, Admin,
AgentOps) + badge de pendências. Espaçamento baseline 4px: `sm` 8px gaps
intra-componente, `md` 16px inter-componente, `lg` 24px seções, `xl` 48px
quebras.

Padrão de sala (room): header (ícone + nome + descrição + ações) + grid com
painel principal (abas + conteúdo + analytics) + coluna direita 420px
(collapsible panels: segmentos, últimas ações) + bottom strip (insights do
agente + chips numéricos). Na nova casca, a coluna direita vira painel
contextual 380px master-detail com breadcrumb stack.

## Elevation & Depth

Três níveis, sempre drop + inset highlight (no dark):
- `--shadow-1`: 0 2px 14px rgba(0,0,0,.28) + inset 1px branco — painéis em repouso
- `--shadow-2`: 0 4px 22px rgba(0,0,0,.36) — hover
- `--shadow-3`: 0 12px 40px rgba(0,0,0,.6) — modais/popovers
Nos temas light, sombras trocam para tintas sutis com inset highlight branco
mais forte.

## Shapes

Raios modestos e consistentes: `sm` (8px) para botões, inputs, cards, pills;
`md` (12px) para painéis, chips, modais; `lg` (20px) apenas bottom sheets
mobile; `full` para avatares, badges pill e o seletor de tema.

## Components

- **Button** — primary (fundo acento, texto branco), secondary (superfície,
  texto fg), ghost (sem fundo, hover glass). `btn bp` / `btn bs` / `btn bg`.
- **Pill** — `.pill` 10.5px, padding 2px 8px, radius 8px, glass bg + borda;
  ativo = `--adim` bg + acento. Usada para frequência (Diário/Semanal/Mensal),
  dias da semana (Dom…Sáb), hora, períodos analytics (30d/90d/1y), gatilhos
  (Manual/Evento/Monitoramento), filtros (nível/tipo).
- **Badge** — `.bdg` tons semânticos: `bu` (urg/Risco), `bw` (warn/Alerta),
  `bo` (ok/Oportunidade), `bi` (info/executando), `tbdg` (contagem de aba).
- **Panel** — recipiente glass com header (`ph`, `ph-ttl`) e corpo scrollável.
- **KanbanCard** — checkbox, nome, badge semântico, valor mono, prazo mono,
  avatar do responsável, borda esquerda 2.5px na cor do semáforo.
- **ApprovalCard** (`.dc`) — decisão com dot do agente + nome, badge de
  prioridade, resumo, timestamp, expandir + ações (Aprovar / Depois / Ignorar).
  Modelo de decisão: IA prepara → humano aprova → agente executa.
- **KpiCell** — label caps + valor + delta (↑/↓ com cor semântica).
- **PanelContextual** — 380px, stack com breadcrumb: cliente (conversa,
  informações, etapa, artefatos, atalhos, interlocutores), pendência,
  perfil (métricas + timeline), rotina (gatilho/ação/filtro/canal), execução,
  preview de artefato.
- **Rotina** — card com nome + toggle, gatilho como pill (Manual/Agenda/
  Evento/Métrica), steps (Função/Agente IA/Saída), badge "Rascunho" e "✦ IA".
- **Avatar** — círculo com iniciais + gradiente.
- **EmptyState** — ícone + título + corpo + ação opcional.
- **Modal** — fundo escurecido 55%, painel `--bg2`, radius 14px, `--shadow-pop`.

## Do's and Don'ts

- **Do** usar token references (`{colors.tertiary}`) em vez de hex literal.
- **Do** usar Phosphor icons (regular) para toda iconografia — emoji é proibido.
- **Do** usar mono + tabular-nums para todo número, valor e timestamp.
- **Do** reusar a função existente do monorepo — a casca muda, o produto não.
- **Don't** introduzir cor fora das 4 paletas — estenda o sistema de temas.
- **Don't** misturar temas na mesma tela; o tema é global por sessão/usuário.
- **Don't** adicionar sombra em cards em repouso — sombra é dos painéis.
- **Don't** usar ease-in em transições — sempre ease-out, snappy (0.10-0.20s).
- **Don't** aninhar variantes de componente (`button-primary-hover` é sibling).

## Riscos conhecidos de acessibilidade

- **Botão primário (dark):** `#FFFFFF` sobre `#8C5FDB` = 4.40:1, marginalmente
  abaixo de AA (4.5:1). É o token canônico de produção — não alterar sem decisão
  explícita. Mitigações: texto do botão em peso 700 + tamanho ≥13px; hover usa
  `--ac-hi` (#a07ae8). Se o AA for exigência, usar `#7C3AED` (violet-700) só no
  botão primário dark.
- **Pills/badges (dark):** o linter reporta 1.0:1 porque calcula o texto sobre
  o `rgba()` translúcido isolado — falso positivo. Na tela, o texto compõe com
  o fundo `#03071C` e o contraste real supera AA. Validar visualmente em cada
  tema antes de ship.
- **Temas light:** acentos semânticos escurecem (ok `#059669`→`#047857`, att
  `#C2760A`→`#B45309`, urg `#DC2626`→`#B91C1C`) para manter contraste sobre
  fundos claros — nunca usar o hex dark do tema dark em tema light.
