# 04 — Log de Reuniões e Decisões — SENAC

> Formato: 1 entrada por conversa/reunião relevante. Cronológico inverso (mais recente em cima).

---

## 2026-07-22 (2ª conversa) — Recebimento do escopo contratual

**Participantes:** Lucas + Hermes
**Canal:** Telegram (DM)

**Resumo:**
- Lucas enviou o **escopo formal do contrato Templo × SENAC** (Relatórios de Diário de Bordo com IA).
- Confirmações extraídas:
  - **Cliente:** SENAC (dados vêm do sistema **SAVE**)
  - **Contrato:** 24 semanas máx, com entregas em 12 sem e discovery em 4 sem
  - **Pagamento:** R$ 18.200 ao final, após Templo receber do cliente
  - **Teto IA:** R$ 10k total (compartilhado com Cladtek) / R$ 3k/mês
  - **Rituais:** kickoff presencial, weekly, workshop, 10 entrevistas, showcase
  - **Stack confirmada:** **Agno** (ignorar N8N do escopo original — decisão Lucas)
  - **Escopo técnico:** agentes Agno, interface, base semântica, login, integração via MCP ou simples
- **Diferencial do produto:** cruzamento quantitativo + qualitativo por aluno, conforme matriz de competências; relatório no formato oficial (introdução + 5 capítulos), **editável**; dashboard agregado interativo; agent conversacional que fala com a base agregada.
- **TEMPLO** = empresa que contrata Lucas; titular da relação com cliente, GP, AI Officer, infra, custos IA, design system (se necessário).
- **Lucas** = responsável técnico ponta-a-ponta (front, back, AI).

**Entregas nesta conversa:**
- ✅ Criado `docs/PRD.md` (v0.1) com 12 seções
- ✅ Criado `docs/ROADMAP.md` (v0.1) com 5 fases + Gantt Mermaid (24 sem, marcos M0/M1/M2/M3)
- ✅ Atualizado STATUS.md com novas perguntas em aberto (10, categorizadas em críticas/importantes/produto)
- ✅ Renomeado repo `CidLucas/cnac` → `CidLucas/senac` e pasta `cnac/` → `senac/`

**Decisões registradas:**
- PRD + ROADMAP serão o **template mínimo padrão** pra replicar em Cladtek e MCP Brain depois
- Estrutura padrão confirmada: `README + STATUS + docs/{PRD, ROADMAP, 01-visao, 02-arquitetura, 03-roadmap-detalhado, 04-reunioes} + decisions/ + assets/`

**Próximos passos imediatos:**
- Lucas alinhar data do kickoff com Templo (D+0)
- Lucas solicitar credenciais OCI ao Templo
- Lucas solicitar acesso ao SAVE ao SENAC
- Hermes abrir issues F0 no repo `CidLucas/senac`

---

## 2026-07-22 (1ª conversa) — Criação do projeto

**Participantes:** Lucas + Hermes
**Canal:** Telegram (DM)

**Resumo:**
- Lucas descreveu (em voz) 3 projetos: CNAC, Coclade Tech, MCP Brain.
- Estrutura padrão de documentação criada no repo `CidLucas/projetos`.
- Pastas locais e repos criados.
- Identificado que `CidLucas/mcp_brain` já existia (servidor MCP real), evitando duplicação.

**Decisões iniciais:**
- Plano B de organização: 1 repo `projetos` (docs) + N repos de código
- Documentação versionada no GitHub (não Google Drive)
- Stack provisória: Agno + FastAPI + vector DB
