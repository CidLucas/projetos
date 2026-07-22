# 01 — Visão do Projeto CNAC

## 🧩 Problema

_Descrever o problema que o CNAC quer resolver. Em coleta — vai ser refinado após conversa com o cliente._

**Hipótese inicial:** professores/coordenação gastam tempo significativo lendo diários de classe manualmente e escrevendo relatórios individualizados por aluno. O processo é repetitivo, sujeito a viés, e consome horas que poderiam ir pra interação direta com o aluno.

## 👥 Público-alvo

| Persona | Papel | Necessidade |
|---|---|---|
| Professor | Alimenta o diário de classe, lê relatório do aluno | Visão consolidada de evolução |
| Coordenação pedagógica | Consome relatórios agregados | Comparar alunos, identificar padrões |
| Família do aluno (opcional) | Lê o relatório | Acompanhar desenvolvimento |

_A ser validado com o cliente._

## 💡 Proposta de valor

- **Relatório personalizado por aluno** gerado a partir do histórico de diários.
- **Q&A em linguagem natural** sobre o corpo de relatórios: o professor/coordenador pergunta "como está a evolução do aluno X em matemática?" e o agente responde.
- **Economia de tempo** vs. redação manual.

## 🎯 Objetivos de sucesso (métricas)

- _a definir com o cliente_

Sugestões a discutir:
- Tempo médio de geração do relatório < 30s.
- Cobertura: 100% dos alunos com diário recebem relatório.
- Acurácia: avaliação qualitativa de professores (NPS interno).
- Adoção: % de coordenadores que usam o Q&A semanalmente.

## 🚫 Fora de escopo (versão inicial)

- _a definir_

Sugestões razoáveis de exclusão pra V1:
- Geração de relatórios em outros idiomas (PT-BR only).
- Integração com sistema acadêmico existente do CNAC (a menos que pedido).
- App mobile (começar com web).

## 📝 Notas / Premissas

- Agente que consulta base vetorial de diários de classe e gera relatórios personalizados por aluno.
- Permite perguntas em linguagem natural sobre o conjunto de relatórios gerados (Q&A sobre o corpus).
