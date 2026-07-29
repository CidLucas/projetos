# 01 — Visão do Projeto

## 🧩 Problema

A Rastro é uma agência-studio premium com +10 anos de mercado e clientes de peso (Nubank, HBO Max, Globo, iFood, Itaú, Unilever). O time de 5–10 pessoas já usa **Claude intensamente** no dia a dia e tem um pipeline de IA próprio — incluindo uma **wiki LLM de 60MB** com conhecimento acumulado da empresa.

**Mas eles têm dificuldade em vender projetos.** O fluxo de criação de propostas comerciais sofre de problemas típicos de agências que escalaram sem estruturar seus ativos de conhecimento:

### Dores identificadas (pré-diagnóstico)

| Dor | Sintoma | Impacto |
|---|---|---|
| **Conhecimento preso em pessoas** | Cada pessoa tem seu próprio modelo de proposta, seu jeito de montar orçamento, seus cases de referência | Se a pessoa sai ou está ocupada, o conhecimento some |
| **Documentos espalhados** | Templates, briefings, propostas passadas, orçamentos — cada um num canto (Drive, Desktop, Slack, e-mail) | Ninguém encontra nada quando precisa |
| **Falta de padrão** | Não existe um modelo canônico de proposta, briefing ou orçamento que todo mundo use | Propostas inconsistentes, retrabalho, qualidade variável |
| **Reuso zero** | Cases de sucesso, propostas vencedoras, argumentos que funcionaram — não são catalogados nem reutilizáveis | Toda venda começa do zero |
| **Claude subutilizado** | Usam Claude, mas cada um no seu contexto isolado. O Claude não "conhece" a empresa | O assistente mais poderoso deles está cego ao conhecimento corporativo |

### Raiz do problema

A Rastro já tem o conhecimento. Já tem as ferramentas (Claude). Já tem maturidade técnica (pipeline de IA próprio). O que falta é **uma camada de memória corporativa que conecte as pessoas, os documentos e os assistentes num espaço de conhecimento unificado**.

---

## 💡 Proposta de valor

> **Transformar o conhecimento fragmentado da Rastro numa memória corporativa acessível via Claude, reduzindo o atrito de criar propostas e aumentando a taxa de conversão comercial.**

### Pilares

1. **Fase A — Consultoria de fluxo:** revisar o processo atual, identificar gargalos, propor melhorias de processo e templates. Entregar um diagnóstico acionável.
2. **Fase B — Memória como serviço:** implantar o MCP Brain Lite como camada de memória central, ingerir o corpus documental, conectar todos os Claude Desktop do time ao mesmo espaço de conhecimento.
3. **Grafo de conhecimento automático:** Mnemosyne cria automaticamente entidades e relações entre documentos na ingestão — o time consulta o corpus como quem "pergunta pra empresa".
4. **Curadoria humana no caminho de escrita:** o corpus corporativo tem escrita controlada por curadores designados, garantindo qualidade do que entra na base.

---

## 👥 Público-alvo (dentro da Rastro)

| Persona | O que ganha |
|---|---|
| **Sócio(a)/Diretor(a) de criação** | Para de ser o gargalo de aprovação — as pessoas se viram com o corpus |
| **Atendimento/Planner** | Monta briefings e propostas consultando cases anteriores, templates e argumentos via Claude |
| **Redator(a)/Diretor(a) de arte** | Acessa referências, tom de voz e cases sem interromper ninguém |
| **Gerente de projeto** | Consulta orçamentos anteriores, modelos de cronograma, lições aprendidas |

---

## 📦 Escopo detalhado

### Fase A — Consultoria de Fluxo de Propostas (1–2 semanas)

**Objetivo:** diagnosticar o fluxo atual e entregar recomendações acionáveis.

**Atividades:**
1. **Mapeamento do fluxo atual** — entrevistas com 2–3 pessoas-chave, coleta de documentos reais usados no processo
2. **Inventário documental** — catalogar templates, modelos de proposta, briefings, orçamentos, cases
3. **Identificação de gargalos** — onde o processo quebra? Onde há retrabalho? Onde o conhecimento se perde?
4. **Recomendações de padronização** — templates canônicos, estrutura de pastas, convenções de nome
5. **Desenho do fluxo-alvo** — como o processo ideal funciona com o MCP Brain Lite no centro

**Entregáveis:**
- Relatório de diagnóstico (PDF)
- Inventário documental comentado
- Desenho do fluxo-alvo (diagrama)
- Recomendações priorizadas (quick wins + estruturais)

### Fase B — Implementação MCP Brain Lite (2–3 semanas)

**Objetivo:** implantar a memória corporativa e conectar o time.

**Atividades:**
1. **Preparação do corpus** — limpeza, deduplicação, categorização dos documentos (wiki LLM + propostas + briefings + orçamentos + cases)
2. **Deploy do MCP Brain Lite** — provisionar infra, configurar gateway, OAuth, escopos
3. **Ingestão do corpus** — upload dos documentos no escopo corporativo (curadoria)
4. **Configuração dos MCPs** — instalar e configurar o conector MCP em cada Claude Desktop do time (5–10 pessoas)
5. **Validação e ajuste fino** — testar consultas reais ("me mostra propostas parecidas com X", "qual o orçamento típico de Y")
6. **Treinamento** — sessão de 1h com o time: como consultar, como contribuir, boas práticas

**Entregáveis:**
- Gateway MCP Brain Lite rodando em produção
- Corpus documental ingerido e indexado (com grafo de conhecimento)
- 5–10 Claude Desktops conectados
- Sessão de treinamento realizada
- Documento de boas práticas e manutenção do corpus

---

## 🚫 Fora de escopo

- **Criação de conteúdo novo** — não vamos escrever propostas, briefings ou templates do zero. Vamos recomendar e padronizar o que já existe.
- **Integração com outros sistemas** (CRM, ERP, Slack) — V1 foca só no MCP Brain Lite + Claude Desktop.
- **Dashboard de analytics** — métricas de uso do corpus ficam para V2.
- **Escopo restrito (grant-based)** — V1 só usa pessoal + corporativo.
- **Customização do Mnemosyne** — usamos o motor padrão, sem forks ou features novas.
- **Manutenção contínua do corpus** pós-entrega — a Rastro assume a curadoria com as boas práticas documentadas.

---

## 🎯 Métricas de sucesso

| Métrica | Alvo |
|---|---|
| **Time conectado** | 100% dos Claude Desktops do time configurados com MCP |
| **Corpus ingerido** | Wiki LLM completa + propostas + briefings + orçamentos indexados |
| **Latência de consulta** | < 2s para queries típicas via MCP |
| **Adoção** | Pelo menos 3 pessoas usando ativamente na primeira semana pós-treinamento |
| **Satisfação** | NPS ≥ 7 na pesquisa pós-implantação |

---

## 📝 Premissas

- A Rastro tem acesso ao corpus documental e vai compartilhá-lo na Fase A (sob NDA se necessário)
- O time tem Claude Desktop instalado e funcionando (já usam)
- O MCP Brain Lite estará com as ferramentas MCP funcionais até o início da Fase B
- O deploy é em cloud (Hetzner ou OCI), não on-premise
- A Rastro designa 1–2 pessoas como "curadores" do corpus corporativo
- **Este é um projeto de consultoria + implementação, não um produto continuado.** Suporte pós-entrega não está incluso (pode ser contratado à parte)
