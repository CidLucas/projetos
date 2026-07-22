# PRD — Projeto SENAC (Relatórios de Diário de Bordo com IA)

> **Documento vivo.** Última atualização: 2026-07-22
> **Status:** Rascunho v0.1 — para discussão

---

## 1. Contexto e problema

O SENAC mantém **diários de classe** dos cursos no sistema **SAVE** (exportação de dados). Hoje, a equipe pedagógica **escreve manualmente** os relatórios de cada aluno a partir desses diários, seguindo um formato oficial (introdução + 5 capítulos), cruzando dados quantitativos e qualitativos conforme a **matriz de competências** da turma.

Esse processo é:

- **Lento** — cada relatório consome horas de escrita por aluno
- **Repetitivo** — mesmos padrões se repetem entre alunos
- **Inconsistente** — qualidade varia entre pedagogos
- **Difícil de escalar** — turmas grandes viram gargalo

## 2. Usuários

| Persona | Papel | Necessidade |
|---|---|---|
| **Pedagogo / Coordenador** | Revisa e valida os relatórios | Relatório editado de aluno pronto, com base nos dados; só ajusta e aprova |
| **Professor** | Alimenta o diário de classe no SAVE | Não muda o fluxo dele — sistema lê do SAVE |
| **Gestão pedagógica** | Lê dashboard agregado | Visão consolidada por turma, eixo de competência, período |
| **Aluno** (futuro) | Lê o próprio relatório | Recebe versão editada do pedagogo |

## 3. Proposta de solução

Sistema agêntico que:

1. **Ingere** dados exportados do SAVE (diários de classe, notas, presenças, observações).
2. **Cruza** dados quantitativos + qualitativos por aluno conforme a **matriz de competências** da turma.
3. **Gera** rascunho de relatório individual no formato oficial (introdução + 5 capítulos), **editável** (doc/Word/Google Docs).
4. **Gera** dashboard agregado interativo (turma, período, eixo de competência).
5. **Permite Q&A** em linguagem natural sobre a base agregada (o "agent conversacional que fala com a base agregada" do escopo).

A equipe pedagógica **valida, ajusta e aprova** antes de qualquer uso externo. O sistema **não substitui** o pedagogo — **acelera** a primeira versão.

## 4. Fora de escopo (V1)

- Geração de relatório para o aluno final diretamente sem revisão do pedagogo
- Integração em tempo real com SAVE (vamos de export/CSV/upload)
- Customização da matriz de competências por turma via UI (V1 lê matriz fixa do SAVE)
- App mobile
- Multilíngue (PT-BR only)

## 5. Stack proposta

| Camada | Tecnologia | Justificativa |
|---|---|---|
| **Orquestrador de agentes** | **Agno** | Decisão confirmada pelo Lucas (substituindo N8N do escopo original); padrão já usado em `agente-bloquo` |
| **LLM** | OCI GenAI (Grok/Llama) — mesmo do `agente-bloquo` | Reaproveitar setup OCI, unificar billing |
| **RAG / base semântica** | OCI Vector Store — padrão `agente-bloquo` | Reaproveitar pipeline de ingestão; alternativa: Turso (avaliar) |
| **API / Backend** | FastAPI + Uvicorn | Padrão `agente-bloquo` |
| **Interface** | A definir — Templo fornecerá design system se necessário | Conforme cláusula contratual |
| **Login / Auth** | A definir (Cognito / Auth0 / Supabase) | Abreviar na Fase 1 |
| **Armazenamento de relatório editável** | Google Docs API (preferido) ou .docx | "mantendo o documento editável para a equipe pedagógica validar" |
| **Deploy** | A definir (infra Templo) | Conforme cláusula |

**Pontos a decidir (Fase 0):**
- LLM exato (Grok ou Llama) — definir benchmark de qualidade vs. custo
- Vector store: manter OCI (consistência) ou Turso (menor custo edge)?
- Interface: web app próprio ou Notion/Google Docs como frontend?

## 6. Funcionalidades da V1

### 6.1 Ingestão

- Upload manual de export do SAVE (CSV/XLSX)
- Processamento → embedding → indexação por aluno/turma/período
- Validação: relatório de "X alunos / Y diários processados" no fim do upload

### 6.2 Geração de relatório individual

- Input: aluno + período + turma
- Output: rascunho de relatório em formato oficial, editável
- Componentes: introdução + 5 capítulos
- Cruzamento automático: quantitativo (notas, presença) + qualitativo (observações do diário) conforme matriz de competências
- Cada afirmação do relatório tem **rastro** (qual diário/nota gerou)

### 6.3 Dashboard agregado

- Visualização por turma, período, eixo de competência
- Filtros interativos (aluno, período, competência)
- Export para PDF/PNG

### 6.4 Agent Q&A (conversacional)

- Pergunta em linguagem natural sobre a base agregada
- Resposta com citações (qual diário/dado fundamenta)
- Escopo: só dados do SAVE, sem opinião

## 7. Restrições e requisitos não-funcionais

- **LGPD** — dados de aluno. Consentimento do SENAC. Retenção configurável.
- **Rastreabilidade** — toda afirmação do relatório aponta pra fonte.
- **Auditabilidade** — log de quem editou, quando, o quê.
- **Performance** — geração de relatório < 60s.
- **Custo** — respeitar teto contratual de IA (R$ 3k/mês, R$ 10k total nos 2 projetos).
- **Editabilidade** — relatório tem que ser editável em ferramenta padrão (Word/Docs), não PDF trancado.

## 8. Critérios de sucesso

| Métrica | Meta |
|---|---|
| Tempo de geração de rascunho | < 60s por aluno |
| % de cobertura (alunos com diário geram relatório) | 100% |
| Taxa de aproveitamento do rascunho (pedagogo aprova com < 20% de edição) | ≥ 70% |
| NPS interno do pedagogo | ≥ 8 |
| Acurácia do Q&A (resposta bate com dado) | ≥ 90% (avaliação humana em golden set) |

## 9. Riscos e mitigações

| Risco | Impacto | Mitigação |
|---|---|---|
| **LLM alucina** números/observações que não existem no diário | Alto | Citação obrigatória por afirmação + validação humana antes de publicar |
| **SAVE muda formato** do export | Médio | Adapter isolado; testes de contrato com export real |
| **Custo de IA estoura teto** (R$ 3k/mês) | Médio | Cache de embeddings, batch de ingestão, escolha de modelo mais barato para Q&A |
| **Pedagogo não confia** no relatório | Alto | Estratégia de "rascunho editável" — sempre passa pela mão humana |
| **Matriz de competências ambígua** | Médio | Validar com pedagogia nas entrevistas de discovery |

## 10. Dependências externas

- Acesso ao **SAVE** — entender formato de export, periodicidade, dados disponíveis
- **Templo** — design system (se necessário), infra de produção, AI Officer
- **SENAC** — pedagogos para entrevistas de discovery, validação de formato de relatório
- **OCI** — cota de Grok/Llama, Vector Store provisionado

## 11. Fora de escopo do LUCAS (delegado ao Templo)

Conforme cláusula contratual:
- Infraestrutura e ambiente de produção
- Direção técnica (Chief AI Officer do Templo)
- Atendimento ao cliente e gestão de projeto (GP do Templo)
- Reembolso de transporte e alimentação em encontros presenciais
- Custos de IA (tokens, licenças)
- Fornecimento de design system (se necessário)

## 12. Stakeholders

| Papel | Quem |
|---|---|
| Responsável técnico | Lucas Cid |
| Gestor de projeto (GP) | Templo (a definir nome) |
| Chief AI Officer | Templo (a definir nome) |
| Cliente (pedagogia) | SENAC (contato a definir) |
| Infraestrutura | Templo |
| AI Officer / Curador de prompt | Templo |

---

## 📝 Pendências para fechar este PRD

- [ ] Confirmar com SENAC formato de export do SAVE (campos disponíveis)
- [ ] Confirmar com SENAC formato **exato** do relatório oficial (template Word/Docs?) — capítulo a capítulo
- [ ] Confirmar matriz de competências: vem no export? precisa de planilha separada?
- [ ] Definir LLM final (Grok ou Llama) com base em teste de qualidade em 5 relatórios reais
- [ ] Definir stack de auth
- [ ] Definir formato final do entregável editável (Google Docs, .docx, both?)
- [ ] Esclarecer com Templo: quem faz o login do pedagogo? Single sign-on do SENAC?
