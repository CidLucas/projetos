# Rastro — Escopo da Proposta de Trabalho

> **Versão:** v0.3 — 2026-07-29
> **Cliente:** Rastro ([rastro.cc](https://rastro.cc/))
> **Contrato:** Deep Blue → Rastro (direto)
> **Investimento:** R$ 25.000 (projeto completo, 2 meses)

---

## 1. Situação atual

A Rastro é uma agência-studio com 5–10 pessoas, clientes de peso (Nubank, HBO Max, Globo, iFood, Unilever) e maturidade técnica — já usam Claude intensamente e têm um pipeline de IA próprio.

O conhecimento da empresa já existe e está organizado no **[Rastro Mind](https://rastro-mind-25619.netlify.app/)** — uma wiki LLM com ~60MB de dados institucionais (propostas passadas, briefings, orçamentos, cases, conhecimento técnico).

**O problema:** o Rastro Mind é uma ilha. O time precisa abrir um site separado, fazer login, digitar a pergunta — enquanto o Claude Desktop, que eles já usam o dia todo, não tem acesso a nada disso. Cada pessoa usa o Claude no seu próprio contexto isolado, sem memória do que a empresa sabe.

**Consequência:** dificuldade em vender projetos. Toda proposta começa do zero. Conhecimento de propostas vencedoras, orçamentos típicos e cases de sucesso está preso em pessoas ou num site que ninguém consulta durante o fluxo de trabalho real.

---

## 2. O que propomos

**Conectar o conhecimento da Rastro ao Claude Desktop do time inteiro**, transformando o que já existe numa memória corporativa viva — a **Rastro Brain** — que responde dentro do assistente que eles já usam.

O projeto tem duas fases:

### Fase A — Consultoria de fluxo (~3 semanas)

Revisar como as propostas são criadas hoje, mapear gargalos, e desenhar o processo ideal com a memória corporativa no centro.

**Atividades:**
- Entrevistas com 2–3 pessoas-chave
- Inventário dos documentos usados no fluxo de proposta
- Mapeamento do fluxo atual (AS-IS) e desenho do fluxo-alvo (TO-BE)
- Recomendações de padronização de templates e documentos

**Entregáveis:**
- **Processo de propostas atualizado** — a partir do pipeline definido durante a consultoria
- **Relatório sobre o estado do corpus documental** — o que existe, qualidade, gaps, plano de curadoria

### Fase B — Implementação Rastro Brain (~5 semanas)

Implantar a **Rastro Brain** como ponte entre o conhecimento da empresa e os Claude Desktop do time.

**Atividades:**
- Preparar o corpus documental (limpeza, categorização, curadoria)
- Deploy do gateway MCP (servidor que serve o conhecimento)
- Ingestão do corpus com criação automática de grafo de conhecimento (Mnemosyne)
- Configurar o conector MCP em cada Claude Desktop do time (5–10 pessoas)
- Treinamento do time: como consultar a memória da empresa direto do Claude

**Critério de pronto:**
- ✅ Todo o time conectado via MCP
- ✅ Todo conteúdo curado e disponibilizado na nuvem ou servidor próprio da Rastro
- ✅ Conteúdo acessível via MCP por todos os usuários

---

## 3. O que NÃO está incluso

- Criação de conteúdo novo (templates, propostas) — vamos recomendar padrões, não escrever do zero
- Integração com outros sistemas (CRM, Slack, e-mail)
- Manutenção contínua pós-entrega (pode ser contratada à parte)
- Modificações no Rastro Mind existente

---

## 4. Produto utilizado: Rastro Brain

**Rastro Brain** é a instância do **MCP Brain Lite** configurada para a Rastro — gateway MCP que expõe documentos corporativos como ferramentas acessíveis por qualquer cliente MCP (Claude Desktop, Cursor, etc.). Usa Mnemosyne como motor de busca vetorial + grafo de conhecimento, com autenticação OAuth 2.1.

**Configuração para a Rastro:**
- **Escopos:** pessoal (cada pessoa tem seu banco privado) + corporativo (conhecimento curado da empresa)
- **Curadoria:** Fábio e Lucas Diárea (Rastro) — escrita no corpus corporativo é controlada
- **Deploy:** servidor próprio da Rastro (provável EC2)
- **Clientes:** 5–10 Claude Desktops

O MCP Brain Lite está em desenvolvimento ativo (repo: `CidLucas/mcp_brain_lite`), com a Fase 0 (fundação, OAuth, CI/CD) concluída. **As ferramentas MCP ainda não foram testadas em produção.** A Fase B inclui a primeira implantação real com um cliente, o que pode revelar necessidade de ajustes.

---

## 5. Cronograma

**Duração total: 2 meses (8 semanas)**

| Fase | Duração | Descrição |
|---|---|---|
| Fase A — Consultoria | ~3 semanas | Entrevistas, inventário documental, mapeamento AS-IS/TO-BE, diagnóstico, recomendações |
| Fase B — Implementação | ~5 semanas | Preparação do corpus, deploy do gateway, ingestão, configuração dos MCPs, validação, treinamento |
| **Total** | **8 semanas** | |

---

## 6. Pré-requisitos

- Acesso ao corpus documental da Rastro (conteúdo do Rastro Mind + documentos complementares)
- Time com Claude Desktop instalado (já têm)
- Fábio e Lucas Diárea como curadores do conhecimento corporativo
- Servidor para deploy (provável EC2)

---

## 7. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| **Brain Lite não testado em produção** | Fase A roda em paralelo com a finalização e teste das tools MCP. Plano B: conector MCP simples direto no Rastro Mind |
| **Corpus desorganizado ou desatualizado** | Fase A mapeia o que existe → já entramos na Fase B com o inventário pronto |
| **Time não adota** | Eles já usam Claude diariamente. A barreira é zero — é só adicionar um endpoint. Treinamento resolve |
| **Aprovação da Rastro entre fases** | Proposta já prevê as duas fases. Gate claro: diagnóstico aprovado → implementação |

---

## 8. Investimento

**R$ 25.000** pelo projeto completo (Fase A + Fase B):

| Parcela | Valor | Condição |
|---|---|---|
| 1ª parcela (50%) | R$ 12.500 | Na entrega da Fase A (processo atualizado + relatório do corpus) |
| 2ª parcela (50%) | R$ 12.500 | Na entrega da Fase B (time conectado + conteúdo curado e disponível via MCP) |

---

## 9. Próximos passos

1. ✅ Lucas validou este escopo (v0.3)
2. Apresentar proposta à Rastro
3. Se aprovado: agendar kickoff (D+0)
