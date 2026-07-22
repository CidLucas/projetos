# 04 — Log de Reuniões e Decisões — Coclade Tech

> Formato: 1 entrada por conversa/reunião relevante. Cronológico inverso (mais recente em cima).

---

## 2026-07-22 — Criação do projeto

**Participantes:** Lucas + Hermes
**Canal:** Telegram (DM)

**Resumo:**
- Lucas descreveu o projeto: pipeline de aprovação de desenhos técnicos para Coclade Tech (tubos de petróleo). Usa API "Sol de URX" para extrair info do desenho, compara com spec técnica, emite parecer pra agilizar revisão.
- Cliente: Coclade Tech.
- Fase: descoberta — sem requisitos detalhados ainda. Especificamente, **API Sol de URX ainda não acessada** (sem credenciais/docs).
- Estrutura padrão de documentação criada no repo `CidLucas/projetos`.

**Próximos passos:**
- Lucas obter acesso à API Sol de URX (credenciais + docs).
- Lucas coletar exemplos reais (desenho + spec + parecer humano atual).
- Hermes propor arquitetura inicial.

**Decisões tomadas:**
- Documentação versionada no GitHub (não Google Drive) por enquanto.
- Estrutura padrão: `README + STATUS + docs/{01-visao,02-arquitetura,03-roadmap,04-reunioes} + decisions/ + assets/`.
- Foco do produto: **acelerar** o fluxo, **não substituir** o humano. Palavra final continua sendo do engenheiro.

**Perguntas registradas:** ver `STATUS.md` (7 perguntas em aberto).
