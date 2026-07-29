# 03 — Roadmap

## 🗺 Fases

**Duração total: 8 semanas (2 meses)**

### Fase A — Consultoria de Fluxo de Propostas (Semanas 1–3)

**Duração estimada:** ~3 semanas
**D+0:** a definir
**Pagamento:** 50% (R$ 12.500) na entrega do relatório

| # | Atividade | Quem | Duração |
|---|---|---|---|
| A1 | Kickoff com stakeholders da Rastro | Lucas + Rastro | 1h |
| A2 | Entrevistas com 2–3 pessoas-chave do time | Lucas | 2–3h |
| A3 | Coleta e inventário de documentos (templates, propostas, briefings, orçamentos, cases) | Lucas + Rastro | 3–4 dias |
| A4 | Mapeamento do fluxo atual (diagrama AS-IS) | Lucas | 2 dias |
| A5 | Identificação de gargalos e oportunidades | Lucas | 2 dias |
| A6 | Desenho do fluxo-alvo (TO-BE) com memória corporativa no centro | Lucas | 2 dias |
| A7 | Recomendações de padronização (templates, pastas, convenções) | Lucas | 2 dias |
| A8 | Entrega do relatório de diagnóstico + apresentação | Lucas → Rastro | 1h |

**Entregáveis Fase A:**
- Relatório de diagnóstico (PDF)
- Diagrama AS-IS / TO-BE
- Inventário documental comentado
- Recomendações priorizadas

**Gate A→B:** Rastro aprova diagnóstico e autoriza continuar para implementação.
**💰 Pagamento:** R$ 12.500 na entrega.

---

### Fase B — Implementação MCP Brain Lite (Semanas 4–8)

**Duração estimada:** ~5 semanas
**Pré-requisito:** Fase A aprovada + MCP Brain Lite com tools MCP validadas
**Pagamento:** 50% (R$ 12.500) na entrega final

| # | Atividade | Quem | Duração |
|---|---|---|---|
| B1 | Preparação do corpus: limpeza, deduplicação, categorização | Lucas (+ curador Rastro) | 3–4 dias |
| B2 | Deploy do MCP Brain Lite: provisionar VPS, configurar gateway, OAuth, escopos | Lucas | 1–2 dias |
| B3 | Configurar tenant "rastro" com escopos `corp` + `personal/` (5–10 usuários) | Lucas | 0.5 dia |
| B4 | Ingestão do corpus: upload dos documentos no escopo `corp` | Lucas + curador | 3–5 dias |
| B5 | Validação pós-ingestão: testar queries reais, ajustar chunking/embedding | Lucas | 2 dias |
| B6 | Configurar MCP nos Claude Desktop do time (5–10 pessoas) | Lucas | 1 dia |
| B7 | Treinamento do time: como consultar, como contribuir, boas práticas | Lucas → Rastro | 1h |
| B8 | Período de observação: suporte a dúvidas, ajustes finos | Lucas | 1 semana |
| B9 | Entrega final: documento de boas práticas + handoff | Lucas → Rastro | — |

**Entregáveis Fase B:**
- Gateway MCP Brain Lite em produção
- Corpus documental ingerido (grafo de conhecimento ativo)
- 5–10 Claude Desktops conectados
- Sessão de treinamento realizada
- Documento de boas práticas (manutenção do corpus, curadoria, onboarding)

**💰 Pagamento:** R$ 12.500 na entrega.

---

## 📅 Cronograma visual (Gantt)

```mermaid
gantt
    title Rastro — Roadmap 8 semanas (D+0 = kickoff)
    dateFormat  YYYY-MM-DD
    axisFormat  Semana %V

    section Fase A — Consultoria
    Kickoff + entrevistas           :a1, 2026-08-03, 4d
    Inventário documental           :a2, after a1, 4d
    Diagnóstico + fluxo AS-IS       :a3, after a2, 3d
    Desenho TO-BE + recomendações   :a4, after a3, 4d
    Entrega relatório + pagamento   :milestone, m1, after a4, 0d

    section Fase B — Implementação
    Preparação do corpus            :b1, after a4, 4d
    Deploy + config tenant          :b2, after b1, 2d
    Ingestão do corpus              :b3, after b2, 5d
    Validação + ajustes             :b4, after b3, 2d
    Config MCPs + treinamento       :b5, after b4, 2d
    Observação + suporte            :b6, after b5, 7d
    Entrega final + pagamento       :milestone, m2, after b6, 0d
```

---

## 🎯 Milestones

| Marco | O quê | Data alvo | Status |
|---|---|---|---|
| **M1** | Relatório de diagnóstico entregue e aprovado + pagamento Fase A | ~Semana 3 | 🔴 |
| **M2** | Time conectado + corpus vivo + treinamento + pagamento Fase B | ~Semana 8 | 🔴 |

---

## ⚠️ Riscos do roadmap

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| **Brain Lite não testado em produção** | Alta | Alto | Fase A roda em paralelo com testes. Plano B: conector MCP simples direto no Rastro Mind (sem Brain Lite) |
| **Corpus desorganizado/deduplicado** | Alta | Médio | Fase A inclui inventário → já saímos com mapa do que ingerir |
| **Atraso na aprovação da Rastro entre fases** | Média | Baixo | Gate A→B claro. Proposta já prevê as duas fases |
| **Time não adota** | Baixa | Alto | Já usam Claude → barreira zero. Treinamento + suporte na primeira semana |
| **Vazamento de dados sensíveis** | Baixa | Crítico | Escopo `corp` com curadoria humana. Sem ingestão automática |
