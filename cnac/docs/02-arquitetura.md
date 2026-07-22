# 02 — Arquitetura — CNAC

> _A ser preenchido após definição de stack. Esboço abaixo._

## 🧱 Stack proposta (inicial)

| Camada | Tecnologia | Por quê |
|---|---|---|
| Orquestrador de agentes | Agno (provável) | Padrão dos seus outros projetos (Blu, Bloquo) |
| LLM | _a definir_ | _a definir_ |
| Vector DB | _a definir_ | precisa buscar trechos relevantes por aluno/período |
| Banco relacional | _a definir_ | metadados de alunos, turmas, diários |
| API / Backend | FastAPI (provável) | padrão consistente |
| Frontend | _a definir_ | _a definir_ |
| Deploy | _a definir_ | _a definir_ |

**Hipótese:** Agno + FastAPI + vector DB + LLM com tool de retrieval.

## 🔄 Fluxo principal (alto nível)

### Geração de relatório
```
[Diário de classe] → [Ingestão + Embedding] → [Vector DB por aluno/turma]
                                                     ↓
[Pedido de relatório] → [Agente] → [Retrieval dos diários relevantes]
                                              ↓
                                    [LLM sintetiza relatório] → [Saída estruturada]
```

### Q&A sobre corpus de relatórios
```
[Pergunta do usuário] → [Agente] → [Retrieval nos relatórios já gerados]
                                            ↓
                                  [LLM responde com base no corpus] → [Resposta com citações]
```

## 🧩 Componentes

- **Ingestor de diários:** recebe novos diários (manual ou automático), normaliza, embute, indexa.
- **Gerador de relatório:** dado um aluno + período, recupera diários relevantes e gera texto estruturado.
- **Agente Q&A:** recebe pergunta, recupera relatórios/trechos, responde.
- **Camada de avaliação:** permite o professor/coordenador dar feedback (👍/👎) pra calibrar.

## 🔌 Integrações externas

- Nenhuma confirmada ainda. Possível: API do sistema acadêmico do CNAC se houver.

## 🔐 Considerações de segurança

- **LGPD:** dados de aluno — possivelmente menor de idade. Cuidado com armazenamento, retenção e compartilhamento.
- **Logs:** não persistir conteúdo bruto de diário em logs.
- **Isolamento por turma:** garantir que um professor só vê alunos da sua turma.

## 📐 Decisões arquiteturais (resumo)

Ver [`../decisions/`](../decisions/) para ADRs completos.
_— nenhum registrado —_

## 🧪 Estratégia de testes

- _a definir_ — provavelmente: golden set de diários + relatórios esperados, e suite de Q&A com perguntas canônicas.
