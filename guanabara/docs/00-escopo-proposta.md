# Guanabara — Escopo da Proposta de Serviço

> **Versão:** v0.1 — 2026-07-29
> **Cliente:** Supermercados Guanabara
> **Contrato:** Deep Blue → Guanabara (direto)
> **Investimento:** R$ 60.000 (Fase 0 isolada) ou R$ 200.000 (projeto completo, 12 meses)

---

## 1. Situação atual

O Guanabara opera uma rede com 30+ lojas. Os dados da operação existem, mas estão espalhados por múltiplos sistemas (TOTVS, RP, planilhas de fechamento) e pela memória dos gerentes. Não há um jeito sistemático de capturar e compartilhar o que funciona: o know-how da rede está fragmentado em 30 silos.

Três dores centrais:

| Dor | Sintoma |
|---|---|
| **Conhecimento fragmentado** | O que o gerente da loja 12 faz bem no controle de perecíveis não chega na loja 7. Não há captura nem compartilhamento sistemático de boas práticas. |
| **Visibilidade defasada** | Os números chegam no fechamento do mês e exigem dias de consolidação manual. Quando a diretoria enxerga um desvio, já se passaram semanas. A rede reage no ritmo da planilha, não do negócio. |
| **Diagnóstico sem prescrição** | O BI atual mostra o que aconteceu (queda de margem no setor X, aumento de perda na loja Y), mas não cruza causas com efeitos, não compara lojas equivalentes, e não sugere ações. |

---

## 2. O que propomos

Uma plataforma de inteligência sobre os dados da rede — da loja à decisão — que unifica, compara e prescreve, com a velocidade e granularidade que 30+ lojas exigem.

O projeto é estruturado em três fases:

### Fase 0 — Diagnóstico (Meses 1–3) · R$ 60.000

Mapear o terreno antes de construir. Entender profundamente os processos, identificar onde o resultado vaza e quais práticas diferenciam as lojas de melhor desempenho.

**Atividades:**
- Entrevistas exploratórias com diretoria e responsáveis de cada área para montar o mapa macro da operação
- Co-design de questionários por função (gerente, perecíveis, frente de caixa, manutenção, RH), cada um focado no que o colaborador vê no dia a dia
- Aplicação dos questionários em amostra de lojas, com refinamento iterativo conforme padrões emergem
- Cruzamento das respostas com indicadores operacionais existentes

**Entregáveis da Fase 0:**
- Mapa de processos da rede
- Matriz de maturidade comparando todas as lojas
- Relatório de diagnóstico com vazamentos priorizados
- Especificação técnica da plataforma (escopo detalhado para Fases 1 e 2)
- Proposta de investimento revisada para as fases seguintes

> ⚠️ A Fase 0 pode ser contratada como projeto isolado. O escopo e investimento das Fases 1 e 2 são definidos ao final do diagnóstico, com base nos achados reais.

### Fase 1 — Unificar e enxergar (Meses 4–7)

Juntar todos os dados da rede num lugar só e entregar visão comparável entre as 30+ lojas.

**Atividades:**
- Integração de TOTVS, RP e demais fontes (planilhas, CSVs) num data warehouse unificado (PostgreSQL)
- Pipeline de ingestão automatizado: sobe o arquivo, o sistema descobre colunas, mapeia schemas e mantém sincronizado
- Padronização de cadastros entre lojas (nomes de produtos, categorias, centros de custo)
- Painel de comparação entre lojas com métricas normalizadas por faturamento, porte e demais variáveis

**Entregáveis da Fase 1:**
- Banco de dados unificado e documentado
- Pipeline de ingestão automático em produção
- Painel com indicadores atuais + benchmarking entre lojas
- Documentação de padronização de cadastros

### Fase 2 — Entender e agir (Meses 8–12)

Ir além do "o que aconteceu" e chegar no "por que aconteceu e o que fazer a respeito".

**Atividades:**
- Análise de direcionadores de custo: cruzamento do custo operacional com atributos estruturais de cada loja (idade dos equipamentos, localização, perfil de consumo)
- Chat com dados em linguagem natural conectado ao banco unificado
- Relatórios automáticos com desvios destacados e ações sugeridas
- Motor de recomendações que aprende quais práticas estão associadas a melhores resultados
- Agentes de IA por domínio: análise financeira, CRM de fornecedores, compras e procurement, análise estratégica

**Entregáveis da Fase 2:**
- Modelo de direcionadores de custo (separa custo passivo do gerenciável)
- Interface de chat com dados em linguagem natural
- Sistema de relatórios automáticos (agendados e sob demanda)
- Motor de recomendações conectando práticas a resultados
- Agentes de IA por domínio em produção

---

## 3. Diferencial estratégico: Direcionadores de custo

A pergunta que toda rede se faz: *"Por que esta loja fatura X% mais que a outra e ainda assim dá menos lucro?"*

A plataforma cruza os dados operacionais de cada loja com seus atributos estruturais — idade dos equipamentos, localização, perfil de consumo de energia e água, e outras variáveis levantadas no diagnóstico. O resultado é um modelo que **separa o custo passivo** (loja mal localizada, equipamento antigo — estruturais, não corrigíveis no curto prazo) **do custo gerenciável** (decisões operacionais que podem ser ajustadas). A diretoria para de tratar todas as lojas como se fossem iguais e passa a agir onde realmente faz diferença.

---

## 4. O que NÃO está incluso

- Substituição ou migração do TOTVS ou RP existentes — a plataforma integra, não substitui
- Criação de conteúdo operacional (procedimentos, manuais) — podemos recomendar padrões, não escrever do zero
- Hardware ou infraestrutura de rede nas lojas
- Manutenção contínua pós-entrega (pode ser contratada à parte)
- Treinamento de equipe além do escopo de adoção da plataforma

---

## 5. Stack prevista

| Camada | Tecnologia |
|---|---|
| Banco de dados | PostgreSQL (data warehouse unificado) |
| Pipeline de ingestão | Automatizado — detecção de colunas, mapeamento de schemas |
| Backend | FastAPI + Python |
| IA / Agentes | Modelos LLM para chat, relatórios e recomendações |
| Frontend | Painel web + chat em linguagem natural |
| Autenticação | A definir (integração com AD/existente ou própria) |

---

## 6. Cronograma

**Duração total: 12 meses**

| Fase | Período | Descrição |
|---|---|---|
| Fase 0 — Diagnóstico | Meses 1–3 | Entrevistas, questionários, matriz de maturidade, especificação da plataforma |
| Gate | Final Mês 3 | Decisão sobre continuidade + escopo revisado das Fases 1 e 2 |
| Fase 1 — Unificar | Meses 4–7 | Integração de dados, pipeline automático, painel comparativo |
| Fase 2 — Agir | Meses 8–12 | Direcionadores, chat, relatórios automáticos, recomendações, agentes IA |

---

## 7. Investimento

| Opção | Valor | Prazo |
|---|---|---|
| **Fase 0 isolada** | R$ 60.000 | 3 meses |
| **Projeto completo** (Fases 0+1+2) | R$ 200.000 | 12 meses |

> 💡 As Fases 1 e 2 só têm investimento definido após o diagnóstico da Fase 0. Os valores do projeto completo são uma estimativa-base que será refinada com os achados reais.

---

## 8. Riscos e mitigação

| Risco | Nível | Mitigação |
|---|---|---|
| **Qualidade/consistência dos dados de origem** | Alto | Fase 0 mapeia fontes e avalia qualidade antes de qualquer integração |
| **Resistência dos gerentes aos questionários** | Médio | Questionários curtos, por função, com opção de áudio. Foco no que o colaborador já vê |
| **Dependência de acesso aos sistemas (TOTVS, RP)** | Alto | Alinhamento prévio com TI do Guanabara; a Fase 0 já levanta isso |
| **Escopo das Fases 1–2 muda radicalmente após diagnóstico** | Médio | Isso é esperado e desejável — o modelo prevê refinamento ao final da Fase 0 |
| **30+ lojas = volume e variabilidade alta** | Médio | Pipeline automatizado desde o início; a plataforma é desenhada para escala |

---

## 9. Próximos passos

- [ ] Lucas validar este documento de escopo
- [ ] Ajustar com base no alinhamento
- [ ] Apresentar proposta ao Guanabara
- [ ] Se aprovado: agendar kickoff da Fase 0
