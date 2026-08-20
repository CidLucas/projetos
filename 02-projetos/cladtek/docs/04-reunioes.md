# 04 — Log de Reuniões e Decisões — Cladtek

> Formato: 1 entrada por conversa/reunião relevante. Cronológico inverso (mais recente em cima).

---

## 2026-07-29 — Formalização do contrato (Templo)

**Participantes:** Templo (e-mail) + Lucas + Hermes
**Canal:** E-mail formal + Telegram (DM)

**Resumo:**
- Templo formalizou a contratação: **contrato único** com Cladtek (não são 2 contratos separados como inicialmente considerado).
- Sistema agêntico **único e integrado** com 2 casos de uso no mesmo workflow/sistema: (1) Revisão e aprovação de desenhos técnicos, (2) Análise crítica de BID.
- Valor: **R$ 61.300,00** em 3 parcelas, liberadas após Templo receber do cliente.
- Prazo: **24 semanas** (máx), entrega intermediária 12s, discovery 4s.
- Custos de IA por conta do Templo (teto R$ 10k total, R$ 3k/mês).
- **Fase 1 de setup** — expectativa de recorrência futura integrada ao Orchestra (fora do escopo do Lucas).
- Contrato com Cladtek ainda em discussão jurídica: expectativa de assinatura em **15-30 dias**.
- Contrato com Lucas só ativa após assinatura do cliente final.

**Próximos passos:**
- Aguardar assinatura do contrato Cladtek.
- Hermes criou PRD.md e ROADMAP.md com base no escopo formalizado.
- Decidir N8N (contratual) vs Agno (padrão interno) no pré-kickoff.

**Decisões tomadas:**
- Documentação atualizada: STATUS.md, PRD.md, ROADMAP.md, 01-visao.md, README.md.
- Stack N8N vs Agno: deixado como pergunta aberta para o pré-kickoff.

**Perguntas registradas:** ver `STATUS.md` (11 perguntas em aberto, categorizadas).

---

## 2026-07-22 — Criação do projeto

**Participantes:** Lucas + Hermes
**Canal:** Telegram (DM)

**Resumo:**
- Lucas descreveu o projeto: pipeline de aprovação de desenhos técnicos para Cladtek (tubos de petróleo, via Templo). Usa SolidWorks (API nativa) para extrair info do desenho, compara com spec técnica, emite parecer pra agilizar revisão.
- Cliente: Cladtek.
- Fase: descoberta — sem requisitos detalhados ainda. Especificamente, **SolidWorks (API nativa) ainda não acessada** (sem credenciais/docs).
- Estrutura padrão de documentação criada no repo `CidLucas/projetos`.

**Próximos passos:**
- Lucas obter acesso à SolidWorks (API nativa) (credenciais + docs).
- Lucas coletar exemplos reais (desenho + spec + parecer humano atual).
- Hermes propor arquitetura inicial.

**Decisões tomadas:**
- Documentação versionada no GitHub (não Google Drive) por enquanto.
- Estrutura padrão: `README + STATUS + docs/{01-visao,02-arquitetura,03-roadmap,04-reunioes} + decisions/ + assets/`.
- Foco do produto: **acelerar** o fluxo, **não substituir** o humano. Palavra final continua sendo do engenheiro.

**Perguntas registradas:** ver `STATUS.md` (7 perguntas em aberto).
