# Status — SENAC

> Última atualização: 2026-07-22
> **Contrato:** Templo × SENAC, 24 semanas, R$ 18.200 (pagamento final)
> **Lucas:** responsável técnico
> **Templo:** GP + AI Officer + infra

> 🎯 **FOCO ATIVO:** Lucas definiu em 2026-07-22 que vamos trabalhar **100% no SENAC nos próximos dias**. Cladtek e MCP Brain ficam em standby (docs básicos mantidos, sem avanço).

## 🩺 Saúde geral

🟡 **Em descoberta** — coletando requisitos, definindo escopo e stack.

## 📊 Resumo executivo

| Item | Status |
|---|---|
| **Contrato assinado** | 🟡 pendente confirmação Templo |
| **Data de kickoff (D+0)** | 🔴 a definir com SENAC |
| **PRD v0.1** | 🟡 rascunho criado ([docs/PRD.md](./docs/PRD.md)) |
| **ROADMAP v0.1 (24 sem + Gantt)** | 🟡 rascunho criado ([docs/ROADMAP.md](./docs/ROADMAP.md)) |
| **Stack escolhida** | 🟡 Agno confirmado; resto em avaliação |
| **Acesso ao SAVE** | 🔴 não |
| **Repo de código** | 🟡 bootstrap criado ([CidLucas/senac](https://github.com/CidLucas/senac)) |

## 🚧 Blockers / Riscos

- _nenhum registrado_

## 🎯 Próximas ações (próximas 7 dias)

- [ ] **Lucas** — alinhar com Templo a **data do kickoff** (D+0) para fixar o Gantt
- [ ] **Lucas** — solicitar ao Templo **credenciais OCI GenAI + Vector Store** provisionadas
- [ ] **Lucas** — solicitar ao SENAC **acesso ao SAVE** (formato do export + amostras reais)
- [ ] **Hermes** — abrir issues de F0 no repo `CidLucas/senac` (setup, CI, estrutura)
- [ ] **Lucas** — revisar o [PRD v0.1](./docs/PRD.md) e marcar o que precisa de ajuste

## ❓ Perguntas em aberto

(Atualizadas pós-recebimento do escopo contratual — Templo × SENAC)

**Críticas (bloqueiam F1):**
1. Data do kickoff com SENAC? (D+0 define o Gantt inteiro)
2. Quem é o GP do Templo e o AI Officer? (contatos)
3. Quem será o ponto focal no SENAC (pedagogia + TI)?

**Importantes (definem arquitetura):**
4. SAVE: confirmar formato do export, periodicidade, campos disponíveis
5. Matriz de competências: vem no export ou é planilha separada?
6. Formato final do relatório editável: Google Docs API ou .docx?
7. Auth: SSO do SENAC ou independente?

**De produto:**
8. Turma-piloto: 1 turma acordada com o SENAC?
9. Métricas de sucesso: confirmadas (NPS, tempo, taxa de aproveitamento)?
10. SLA esperado (geração em < 60s é viável com o LLM escolhido)?

## 📅 Histórico de atualizações

| Data | Atualização |
|---|---|
| 2026-07-22 | Criação do projeto. Pasta + docs placeholder. |
| 2026-07-22 | Recebido escopo contratual (Templo × SENAC, 24 sem, R$ 18.200). |
| 2026-07-22 | Criado PRD v0.1 ([docs/PRD.md](./docs/PRD.md)). |
| 2026-07-22 | Criado ROADMAP v0.1 com Gantt Mermaid ([docs/ROADMAP.md](./docs/ROADMAP.md)). |
| 2026-07-22 | Renomeado: repo CidLucas/cnac → CidLucas/senac; pasta cnac/ → senac/. |
| 2026-07-22 | **Decisão: foco 100% no SENAC nos próximos dias.** Cladtek + MCP Brain em standby. |

---

## 🔜 Próxima conversa — quando você voltar

Sugestão de pauta (você ajusta):

1. **Data do kickoff (D+0)** — você já tem? Alinhamos o Gantt.
2. **Credenciais OCI** — Templo já provisionou? Precisamos de Grok/Llama + Vector Store.
3. **Acesso ao SAVE** — formato do export, periodicidade, campos?
4. **Revisão do PRD** — o que ajustar, o que está bom, o que falta?
5. **Revisão do ROADMAP** — fases, marcos, tarefas de alto nível.
6. **Próximos passos práticos** — abrir issues F0 no repo `CidLucas/senac`? setup local? benchmark Grok vs Llama em amostras reais?
