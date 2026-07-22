# 04 — Log de Reuniões e Decisões — CNAC

> Formato: 1 entrada por conversa/reunião relevante. Cronológico inverso (mais recente em cima).

---

## 2026-07-22 — Criação do projeto

**Participantes:** Lucas + Hermes
**Canal:** Telegram (DM)

**Resumo:**
- Lucas descreveu o projeto: agente que consulta base vetorial de diários de classe e gera relatórios personalizados por aluno. Permite Q&A sobre o corpus de relatórios.
- Cliente: CNAC (instituição de ensino).
- Fase: descoberta — sem requisitos detalhados ainda.
- Estrutura padrão de documentação criada no repo `CidLucas/projetos`.

**Próximos passos:**
- Lucas detalhar requisitos com CNAC (formato do diário, periodicidade, quem consome).
- Hermes propor arquitetura inicial.

**Decisões tomadas:**
- Documentação versionada no GitHub (não Google Drive) por enquanto.
- Estrutura padrão: `README + STATUS + docs/{01-visao,02-arquitetura,03-roadmap,04-reunioes} + decisions/ + assets/`.
- Stack provisória: Agno + FastAPI + vector DB (sujeito a revisão).

**Perguntas registradas:** ver `STATUS.md` (5 perguntas em aberto).
