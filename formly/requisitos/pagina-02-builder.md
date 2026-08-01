# 📝 Página 02 — Builder

> **Status:** ✅ Implementado no site (`builder.html`) como protótipo estático
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Tela de criação/edição de questionário. Exibe perguntas de amostra ("Pesquisa de Clima 2026") como **cards** com 6 tipos de pergunta demonstráveis. O layout é header + corpo de cards editáveis.

### Layout

```
┌──────────────────────────────────────────┐
│  Pesquisa de Clima 2026   [+ Pergunta]   │
│                            [Enviar →]    │
├──────────────────────────────────────────┤
│                                          │
│  ┌────────────────────────────────────┐  │
│  │ Qual foi a parte mais irritante?   │  │
│  │ TEXTO LONGO                        │  │
│  │ ┌────────────────────────────────┐ │  │
│  │ │ Conte do jeito que vier...     │ │  │
│  │ └────────────────────────────────┘ │  │
│  │ 0/400    ● Gravar áudio · 0:00    │  │
│  └────────────────────────────────────┘  │
│                                          │
│  ┌────────────────────────────────────┐  │
│  │ Seu trabalho é mais...  MÚLTIPLA  │  │
│  │ ○ Repetitivo e previsível          │  │
│  │ ● Um equilíbrio entre os dois      │  │
│  │ ○ Sempre diferente                 │  │
│  └────────────────────────────────────┘  │
│                                          │
│  ┌─── [✓✓] Onde a informação... ──────┐  │
│  └────────────────────────────────────┘  │
│                                          │
│  ┌─── ESCALA: A ferramenta facilitou ──┐  │
│  │  ○──○──●──○──○  neutro             │  │
│  └────────────────────────────────────┘  │
│                                          │
│  ┌─── NPS: Quanto recomendaria? ───────┐  │
│  │  0 1 2 3 4 5 6 7 8 9 10            │  │
│  └────────────────────────────────────┘  │
│                                          │
│  ┌─── RANKING: Ordene por prioridade ──┐  │
│  │  ⠿ ① Redução de custo              │  │
│  │  ⠿ ② Velocidade de entrega         │  │
│  │  ⠿ ③ Qualidade do output           │  │
│  │  ⠿ ④ Autonomia da equipe           │  │
│  └────────────────────────────────────┘  │
│                                          │
└──────────────────────────────────────────┘
```

---

## 2. Elementos de UI

### 2.1 Header

| Elemento | Tipo | Detalhes |
|---|---|---|
| Título | heading | "Pesquisa de Clima 2026", `--display`, 1.1rem |
| + Pergunta | button secondary | Adiciona nova pergunta com tipo aleatório |
| Enviar → | button primary | `--wine` bg, redireciona para send.html |

### 2.2 Card de Pergunta (`.q-card`)

| Elemento | Tipo | Descrição |
|---|---|---|
| `.q-header` | flex row | Título + badge do tipo |
| `.q-title` | heading | `--display`, 1rem, weight 600 |
| `.q-badge` | badge | `--mono`, uppercase, fundo `--wine-soft`, cor `--wine` |
| `.q-hint` | parágrafo | Itálico, `--muted`, opcional |
| Corpo | variável | Componente específico do tipo de pergunta |

### 2.3 Componentes por Tipo de Pergunta

O builder implementa **11 tipos** (7 com UI completa, 4 apenas no randomizador):

| # | Badge | Tipo | Componente | UI no protótipo |
|---|---|---|---|---|
| 1 | TEXTO CURTO | short_text | `<input class="input-short">` | ✅ placeholder |
| 2 | TEXTO LONGO | long_text | `<textarea>` + contador `0/400` + audio companion | ✅ completo |
| 3 | MÚLTIPLA [○] | single_choice | `.option-card` com `.radio-dot` (seleção exclusiva) | ✅ completo |
| 4 | [✓✓] | multiple_choice | `.option-card` com `.checkbox-dot` (seleção múltipla) | ✅ completo |
| 5 | ESCALA | likert_scale | `.likert-row` 5 dots + labels extremos + "neutro" | ✅ completo |
| 6 | NPS | nps | `.nps-row` 11 dots numerados 0-10 | ✅ completo |
| 7 | RANKING | ranking | `.rank-item` com grip `⠿` + `.rank-num` | ✅ completo |
| 8 | MATRIZ | matrix | — | ❌ só no random |
| 9 | ARQUIVO | file_upload | — | ❌ só no random |
| 10 | DATA | date | — | ❌ só no random |
| 11 | NÚMERO | number | — | ❌ só no random |

---

## 3. Fluxos

```
1. Página carrega → 6 perguntas de amostra renderizadas
2. "+ Pergunta" → card com tipo aleatório, título "Nova pergunta" (contenteditable)
3. "Enviar →" → send.html
4. Interações por tipo:
   - Radio: clique → seleção exclusiva
   - Checkbox: clique → toggle seleção
   - Likert: clique no dot → seleção exclusiva
   - NPS: clique no número → seleção exclusiva
   - Ranking: visual apenas (drag simulado)
```

---

## 4. Regras

- Títulos das perguntas são `contenteditable`
- Tipo aleatório no `addQuestion()` escolhe entre os 11 tipos
- Card novo rola para view com `scrollIntoView({behavior:'smooth'})`
- Nenhuma validação ou persistência no protótipo
- Nenhuma IA ou chat de refinamento (protótipo estático)
- Nenhum preview mobile

---

## 5. Integrações

| Integração | Status |
|---|---|
| Geração IA (prompt → questionário) | 🔴 Não implementado |
| Persistência (salvar questionário) | 🔴 Não implementado |
| Preview | 🔴 Não implementado |

---

## 6. Cenários de Teste

- [ ] 6 perguntas de amostra renderizadas corretamente
- [ ] Cada tipo de pergunta com UI interativa
- [ ] "+ Pergunta" adiciona card com scroll suave
- [ ] Radio buttons: seleção exclusiva funciona
- [ ] Checkboxes: seleção múltipla funciona
- [ ] Likert: seleção exclusiva com destaque visual
- [ ] NPS: seleção exclusiva com destaque visual
- [ ] "Enviar →" redireciona para send.html
- [ ] Responsivo (media query < 600px)
- [ ] Tema vinho/papel aplicado consistentemente

---

> **Fonte:** `/tmp/projetos/formly/site/builder.html` (commit mais recente no GitHub)
