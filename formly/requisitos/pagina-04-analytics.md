# 📊 Página 04 — Analytics

> **Status:** ✅ Implementado no site (`analytics.html`) como protótipo estático
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Dashboard de resultados com KPIs, gráfico de barras por pergunta e exportação CSV. Dados simulados para "Pesquisa de Clima 2026".

### Layout

```
┌──────────────────────────────────────────┐
│  ← Voltar                                │
│                                          │
│  Pesquisa de Clima 2026   [Exportar CSV] │
│                                          │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐    │
│  │   12    │ │   80%   │ │  4min   │    │
│  │Respostas│ │Taxa de  │ │ Tempo   │    │
│  │de 15    │ │resposta │ │ médio   │    │
│  └─────────┘ └─────────┘ └─────────┘    │
│                                          │
│  Respostas por pergunta                  │
│                                          │
│  Satisfação geral  ██████████████  88%   │
│  Comunicação       ████████████    72%   │
│  Ferramentas       ██████████      65%   │
│  Carga de trab.    ████████        52%   │
└──────────────────────────────────────────┘
```

---

## 2. Elementos de UI

### 2.1 Header

| Elemento | Tipo | Detalhes |
|---|---|---|
| ← Voltar | button link | `--muted`, hover: `--wine` |
| Título | heading | "Pesquisa de Clima 2026", `--display`, 1.1rem |
| Exportar CSV | button outline | `--card` bg, `--wine` text, hover: `--wine-soft` |

### 2.2 KPIs (`.kpi-grid`)

Grid de 3 colunas (2 em mobile):

| KPI | Valor | Label | Sub |
|---|---|---|---|
| Respostas | 12 | RESPOSTAS | de 15 enviados |
| Taxa | 80% | TAXA DE RESPOSTA | — |
| Tempo | 4min | TEMPO MÉDIO | por resposta |

### 2.3 Gráfico de Barras (`.bar-list`)

| Pergunta | % |
|---|---|
| Satisfação geral | 88% |
| Comunicação | 72% |
| Ferramentas | 65% |
| Carga de trabalho | 52% |

Componentes de cada barra:

| Elemento | Descrição |
|---|---|
| `.bar-label` | Nome da pergunta, 120px, right-aligned |
| `.bar-track` | Fundo `--paper2`, 24px height |
| `.bar-fill` | Fundo `--wine`, anima width no load |
| `.bar-val` | Percentual, `--mono`, 36px |

### 2.4 Animações

- Barras iniciam com `width: 0` e animam para `data-w` no load (100ms delay, 600ms ease)

---

## 3. Fluxos

```
1. Página carrega → barras animam do zero ao valor real
2. Usuário visualiza KPIs e gráfico
3. "Exportar CSV" → alert() simulado
4. "← Voltar" → send.html
```

---

## 4. Regras

- Dados 100% simulados (hardcoded no HTML)
- Sem filtro por período (fixo)
- Sem filtro por pergunta
- Sem player de áudio
- Exportação simulada (alert)
- KPIs não são calculados — são valores fixos

---

## 5. Integrações

| Integração | Status |
|---|---|
| GET responses/stats API | 🔴 Não implementado |
| Exportação CSV real | 🔴 Não implementado (alert) |
| Player de áudio | 🔴 Não implementado |
| Filtros por período | 🔴 Não implementado |

---

## 6. Cenários de Teste

- [ ] 3 KPIs renderizados com valores corretos
- [ ] Barras animam no load (width 0 → data-w)
- [ ] 4 perguntas no gráfico com % corretos
- [ ] "Exportar CSV" → alert()
- [ ] "← Voltar" → send.html
- [ ] Responsivo (2 colunas KPI em mobile)
- [ ] Tema vinho/papel aplicado

---

> **Fonte:** `/tmp/projetos/formly/site/analytics.html` (commit mais recente no GitHub)
