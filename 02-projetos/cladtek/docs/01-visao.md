# 01 — Visão do Projeto Cladtek

> Atualizado em 2026-07-29 com escopo contratual formalizado (Templo × Cladtek)

## 🧩 Problema

A Cladtek, empresa de óleo & gás, tem **dois fluxos críticos de engenharia** que hoje são manuais e dependentes de especialistas:

### Fluxo 1 — Revisão de desenhos técnicos
Engenheiros revisam desenhos (SolidWorks/PDL/PDF) manualmente — verificam cotas, tolerâncias e notas contra parâmetros internos. É lento, inconsistente e gera documentação fragmentada.

### Fluxo 2 — Análise crítica de BID
Quando chega uma RFQ, engenheiros leem, interpretam e cruzam com capacidades internas para gerar um Technical Comment. É intensivo em conhecimento tácito e difícil de escalar.

**O cliente unificou os dois casos em um único contrato, projeto e sistema.**

## 👥 Público-alvo

| Persona | Papel | Necessidade |
|---|---|---|
| Engenheiro revisor | Revisa desenhos e emite parecer | Acelerar checagem, focar em exceções |
| Analista de BID | Lê RFQs e gera Technical Comment | Cruzamento rápido com capacidades internas |
| Coordenação de projetos | Gerencia fila de aprovação/BID | SLA previsível, rastreabilidade |
| Gestão | Consome relatórios agregados | Visão consolidada por área |

~20 usuários.

## 💡 Proposta de valor

Sistema agêntico **único e integrado** (interface própria com login, dashboard, histórico e rastreabilidade) com:

### Caso 1 — Revisão de desenhos técnicos
1. **Lê** desenhos (SolidWorks/PDL/PDF) e extrai dados estruturados
2. **Verifica** cotas, tolerâncias e notas contra parâmetros Cladtek
3. **Gera** laudo de conformidade (✅/⚠️/❌) com justificativas
4. **Encaminha** para revisão humana (palavra final é do engenheiro)
5. **Outputs:** relatórios por área, bot consultor, dashboard agregado

### Caso 2 — Análise crítica de BID
1. **Lê e interpreta** RFQs
2. **Cruza** com capacidades e procedimentos internos da Cladtek
3. **Gera** Technical Comment com validação humana em sandbox
4. **Outputs:** relatórios por área, bot consultor, dashboard agregado

### Compartilhado
- **Bot consultor** que fala com a base (desenhos + BIDs)
- **Dashboard agregado** de gestão (ambos os casos)
- **Histórico e rastreabilidade** completos

**Resultado esperado:** reduzir tempo de revisão, liberar engenheiro para casos que realmente precisam de julgamento humano, e unificar a documentação em um só lugar.

## 🎯 Objetivos de sucesso (métricas)

- _A definir com a Cladtek no discovery._

Sugestões:
- Tempo médio de revisão de desenho: redução de X para Y dias
- Tempo médio de análise de BID: redução de X para Y horas/dias
- Precisão do parecer automatizado vs. decisão do engenheiro > 90%
- NPS interno do engenheiro ≥ 8

## 🚫 Fora de escopo (V1)

- Integrações customizadas para sistemas internos da Cladtek (ERP, MES)
- Integração ao Orchestra — **Templo fará após este contrato** ou negociará à parte
- Geração/edição de desenhos (sistema só lê e analisa)
- Certificação ISO / auditoria formal
- App mobile

## 📝 Notas / Premissas

- O contrato menciona **N8N** como orquestrador; internamente usamos **Agno**. Decisão a tomar no pré-kickoff.
- Fase 1 de setup — expectativa de virar contrato de recorrência integrado ao Orchestra (fora do escopo do Lucas).
- "Integração simples" de dados = APIs padrão, sem customização para sistemas internos da Cladtek.
- Foco em **agilizar**, não em **substituir** o humano. Palavra final sempre é do engenheiro.
