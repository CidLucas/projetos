# 01 — Visão do Projeto Cladtek Tech

## 🧩 Problema

A Cladtek (empresa de tubos de petróleo) tem um **fluxo manual de aprovação de desenhos técnicos** que hoje depende de um engenheiro especialista revisando cada desenho contra a especificação do projeto. O processo é:

- **Lento** — pode levar dias por desenho.
- **Especialista-dependente** — gargalo se a pessoa sai de férias.
- **Inconsistente** — revisores diferentes aplicam critérios diferentes.
- **Caro** — horas de engenharia em verificação mecânica.

## 👥 Público-alvo

| Persona | Papel | Necessidade |
|---|---|---|
| Engenheiro revisor | Revisa cada desenho hoje | Acelerar checagem, focar em exceções |
| Coordenação de projetos | Gerencia fila de aprovação | SLA previsível, rastreabilidade |
| Cliente final (interno ou externo) | Espera aprovação | Receber retorno mais rápido |

## 💡 Proposta de valor

Pipeline automatizado que:

1. **Extrai** dados estruturados do desenho via **API Sol de URX** (dimensões, materiais, tolerâncias, simbologia).
2. **Compara** automaticamente esses dados com a **especificação técnica** do projeto.
3. **Emite um parecer** com: ✅ aprovado / ⚠️ aprovado com ressalvas / ❌ reprovado + justificativa por item.
4. **Encaminha pro humano** apenas os casos duvidosos (revisor continua sendo a palavra final).

**Resultado esperado:** reduzir tempo médio de aprovação e liberar o engenheiro pra focar em casos que realmente precisam de julgamento humano.

## 🎯 Objetivos de sucesso (métricas)

- _a definir com a Cladtek_

Sugestões:
- Tempo médio de aprovação cai de N dias para < 1 dia.
- % de desenhos que vão direto pro humano sem revisão automatizada < 30%.
- Precisão do parecer automatizado (vs. decisão final do engenheiro) > 90%.
- NPS interno do revisor humano.

## 🚫 Fora de escopo (versão inicial)

- _a definir_

Sugestões razoáveis de exclusão:
- Geração de desenho (o sistema só **lê e aprova**, não desenha).
- Integração com ERP/MES da Cladtek (a menos que pedido).
- Suporte a múltiplos idiomas (PT-BR only).
- Auditoria completa / certificação ISO (pode ser fase posterior).

## 📝 Notas / Premissas

- "Sol de URX" mencionado como API de extração — pode ser nome interno da Cladtek ou fornecedor externo. **A confirmar.**
- Foco em **agilizar**, não em **substituir** o humano.
- Desenhos técnicos industriais (tubos) — domínio bem específico, vocabulário controlado.
