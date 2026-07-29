# Status — Rastro

> Última atualização: 2026-07-29
> **Contrato:** Deep Blue → Rastro (direto)
> **Lucas:** responsável técnico + consultor
> **Foco:** Pré-proposta — alinhamento de escopo e elaboração da proposta comercial

## 🩺 Saúde geral

🟡 **Pré-proposta** — Escopo definido em conversa inicial (2026-07-29). Documentação base criada. Próxima etapa crítica: **fechar escopo e valores com a Rastro** antes de iniciar a Fase A.

## 📊 Resumo executivo

| Item | Status |
|---|---|
| **Escopo Fase A (consultoria)** | 🟡 definido em alto nível — falta detalhar entregáveis |
| **Escopo Fase B (implementação)** | 🟡 definido em alto nível — falta detalhar configuração |
| **Produto-base (MCP Brain Lite)** | 🟢 repo ativo, CI/CD funcionando, Fase 1 em andamento |
| **Time da Rastro mapeado** | 🟢 5–10 pessoas |
| **Volume documental estimado** | 🟢 wiki LLM 60MB + propostas + briefings + orçamentos |
| **Acesso ao corpus atual** | 🔴 não — precisa solicitar na Fase A |
| **Proposta comercial** | 🔴 não iniciada |
| **Contrato** | 🔴 não iniciado |
| **Data de kickoff** | 🔴 a definir (provável semana de 03/08) |

## 🚧 Blockers / Riscos

- **Risco #1 (comercial, alto):** escopo e valor ainda não foram apresentados à Rastro. Se a proposta não for aceita, o projeto não avança.
- **Risco #2 (técnico, médio):** MCP Brain Lite está na Fase 1 — as ferramentas MCP ainda estão sendo implementadas. Se o cronograma da Rastro for agressivo, pode haver conflito com o desenvolvimento do produto.
- **Risco #3 (dados, médio):** o corpus de 60MB (wiki LLM) pode conter material sensível ou desatualizado. A Fase A precisa incluir auditoria de qualidade dos documentos antes da ingestão.
- **Risco #4 (adoção, baixo):** a Rastro já usa Claude intensamente → barreira de adoção do MCP deve ser baixa. Time tech-savvy.

## 🎯 Próximas ações (próximas 7 dias)

- [ ] **Lucas** — validar escopo da Fase A e Fase B (este documento é a base)
- [ ] **Lucas** — definir modelo de precificação (fixo? valor/hora? dividido por fase?)
- [ ] **Lucas** — agendar conversa com a Rastro para apresentar a proposta
- [ ] **Lucas** — verificar status atual do MCP Brain Lite (as tools MCP já estão funcionais?)
- [ ] **Hermes** — manter docs atualizados conforme o escopo evoluir

## ❓ Perguntas em aberto

### 🔴 Críticas (bloqueiam início)

1. **Modelo de precificação:** valor fixo por fase? Pacote fechado? Hora de consultoria?
2. **Entregáveis da Fase A:** relatório de diagnóstico em PDF? Apresentação? Documento de recomendações?
3. **Critério de "pronto" da Fase B:** o que define sucesso? Time todo conectado? Número X de documentos no corpus? Primeira proposta gerada com auxílio do MCP?
4. **Prazo da Rastro:** eles têm urgência? Qual a janela ideal para ter isso funcionando?

### 🟡 Importantes (definem execução)

5. **Acesso ao corpus:** a Rastro compartilha a wiki LLM + documentos na Fase A (durante consultoria) ou só na Fase B (durante implementação)?
6. **Infra de deploy:** onde o gateway do MCP Brain Lite vai rodar? Cloud da Deep Blue? Hetzner? OCI? On-premise na Rastro?
7. **Escopos:** pessoal + corporativo bastam? Ou precisamos do escopo restrito (grant-based)?
8. **Curadoria:** quem na Rastro vai ser o "curador" do corpus corporativo? (escrita só via curadoria no Brain Lite)

### 🟢 De produto

9. **Nome do projeto para a Rastro:** "Memória Central Rastro"? "Rastro Brain"? Manter "MCP Brain Lite" como nome técnico?
10. **Expansão futura:** a Rastro tem potencial de virar case/portfolio? Autorizam mencionar?

## 📅 Histórico de atualizações

| Data | Atualização |
|---|---|
| 2026-07-29 | Criação do projeto. Conversa inicial com Lucas definindo escopo Fase A + Fase B. Site da Rastro analisado. Docs base criados. |

---

## 🔜 Próxima conversa — quando você voltar

Sugestão de pauta (você ajusta):

1. **Revisar este STATUS.md** — alguma pergunta crítica já tem resposta?
2. **Fechar modelo de precificação** — valor fixo vs hora, divisão por fase
3. **Definir entregáveis concretos** de cada fase para a proposta comercial
4. **Verificar status do MCP Brain Lite** — as tools MCP já estão prontas pra uso?
5. **Preparar one-pager da proposta** para apresentar à Rastro
