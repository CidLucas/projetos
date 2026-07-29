# PRD — Projeto Cladtek (Sistema Agêntico de Engenharia)

> **Documento vivo.** Última atualização: 2026-07-29
> **Status:** Rascunho v0.1 — criado a partir do escopo contratual formalizado pelo Templo

---

## 1. Contexto e problema

A Cladtek é uma empresa de tubos de petróleo com dois fluxos críticos de engenharia que hoje são **manuais, lentos e especialista-dependentes**:

### Fluxo 1 — Revisão de desenhos técnicos
Engenheiros revisam cada desenho técnico (SolidWorks/PDL/PDF) manualmente, verificando cotas, tolerâncias e notas técnicas contra os parâmetros internos da Cladtek. O processo é demorado, inconsistente entre revisores e gera documentação fragmentada para diferentes áreas.

### Fluxo 2 — Análise crítica de BID
Quando chega uma RFQ (Request for Quotation), engenheiros leem e interpretam o documento, cruzam com as capacidades e procedimentos internos da Cladtek, e geram um Technical Comment. Esse processo é intensivo em conhecimento tácito e difícil de escalar.

**O cliente unificou os dois casos em um único contrato, projeto e sistema integrado.**

## 2. Usuários

| Persona | Papel | Necessidade |
|---|---|---|
| **Engenheiro revisor** | Revisa desenhos e emite parecer | Acelerar checagem, focar em exceções |
| **Analista de BID** | Lê RFQs e gera Technical Comment | Cruzamento rápido com capacidades internas |
| **Coordenador de projetos** | Gerencia fila de aprovação/BID | SLA previsível, rastreabilidade, dashboard |
| **Gestão** | Consome relatórios agregados | Visão consolidada de desenhos aprovados/reprovados e BIDs respondidos |

~20 usuários no total.

## 3. Proposta de solução

Sistema agêntico **único e integrado** com:

### Caso 1 — Revisão e aprovação de desenhos técnicos
1. **Lê** desenhos técnicos (SolidWorks/PDL/PDF) e extrai dados estruturados
2. **Verifica** cotas, tolerâncias e notas técnicas contra parâmetros da Cladtek
3. **Gera** laudo de conformidade com evidências por item
4. **Encaminha** para revisão humana (palavra final é do engenheiro)
5. **Outputs:**
   - Relatórios em diferentes documentos para diferentes áreas
   - Bot consultor que fala com a base de desenhos
   - Dashboard agregado de gestão

### Caso 2 — Análise crítica de BID
1. **Lê e interpreta** RFQs
2. **Cruza** com capacidades e procedimentos internos da Cladtek
3. **Gera** Technical Comment com validação humana em sandbox
4. **Outputs:**
   - Relatórios em diferentes documentos para diferentes áreas
   - Bot consultor que fala com a base
   - Dashboard agregado de gestão

### Características comuns
- Interface própria com login
- Dashboard unificado
- Histórico e rastreabilidade
- Bot consultor que fala com a base (compartilhado entre os 2 casos)

## 4. Fora de escopo (V1)

- Integrações customizadas para sistemas internos da Cladtek (ERP, MES, etc.)
- Integração ao Orchestra — a cargo do Templo após este contrato ou negociada à parte
- Geração/edição de desenhos (sistema só lê e analisa, não edita)
- Certificação ISO / auditoria formal
- App mobile

## 5. Fora de escopo do LUCAS (delegado ao Templo)

- Infraestrutura e ambiente de produção
- Direção técnica (Chief AI Officer do Templo)
- Atendimento ao cliente e gestão de projeto (GP do Templo)
- Reembolso de transporte e alimentação em encontros presenciais
- Custos de IA (tokens, licenças) — Templo cobre até R$ 10k total, R$ 3k/mês
- Fornecimento de design system da interface

## 6. Stack proposta (a confirmar)

| Camada | Candidato | Nota |
|---|---|---|
| **Orquestrador de agentes** | **Agno** | Confirmado pelo Lucas (29/07). Padrão interno, mesmo do `agente-bloquo` e Plataforma Blu |
| **LLM** | A definir | Precisa de visão (desenhos) + texto (RFQs) |
| **RAG / base semântica** | A definir | Base de parâmetros Cladtek + capacidades internas |
| **API / Backend** | FastAPI (provável) | Padrão dos outros projetos |
| **Interface** | A definir (Templo fornece design system) | Conforme cláusula contratual |
| **Login / Auth** | A definir | ~20 usuários |
| **Storage** | A definir | Desenhos, RFQs, laudos, histórico |

## 7. Funcionalidades da V1

### 7.1 Caso 1 — Revisão de desenhos

- Upload ou ingestão de desenho (SolidWorks/PDL/PDF)
- Extração de dados estruturados (cotas, tolerâncias, notas)
- Comparação com parâmetros Cladtek
- Geração de laudo de conformidade (✅/⚠️/❌) com justificativas
- Interface de revisão humana (sandbox de validação)
- Histórico de revisões por desenho

### 7.2 Caso 2 — Análise de BID

- Upload ou ingestão de RFQ
- Extração e interpretação dos requisitos
- Cruzamento com base de capacidades/procedimentos Cladtek
- Geração de Technical Comment
- Interface de validação humana (sandbox)
- Histórico de BIDs analisados

### 7.3 Compartilhados

- Dashboard agregado (ambos os casos)
- Bot consultor (Q&A sobre a base)
- Export de relatórios por área/formato
- Login/autenticação (~20 usuários)
- Rastreabilidade (log de quem fez o quê)

## 8. Restrições e requisitos não-funcionais

- **Propriedade intelectual** — desenhos e RFQs são IP da Cladtek
- **Rastreabilidade** — toda decisão do sistema tem rastro auditável
- **Validação humana** — palavra final sempre é do engenheiro
- **Custo** — respeitar teto de IA (R$ 3k/mês, R$ 10k total nos 2 projetos)
- **LGPD** — dados potencialmente sensíveis da Cladtek

## 9. Critérios de sucesso

| Métrica | Meta |
|---|---|
| Tempo de revisão de desenho | Redução vs. processo manual atual |
| Tempo de análise de BID | Redução vs. processo manual atual |
| Precisão do laudo (vs. decisão humana) | ≥ 90% |
| Cobertura de parâmetros Cladtek | Todos os parâmetros documentados |
| NPS do engenheiro revisor | ≥ 8 |

_Valores exatos a definir no discovery com Cladtek._

## 10. Riscos e mitigações

| Risco | Impacto | Mitigação |
|---|---|---|
| **LLM não entende desenhos técnicos** | Alto | Testar com amostras reais no discovery; possível fallback: OCR + LLM multimodal |
| **Parâmetros Cladtek ambíguos** | Médio | Documentar e validar com engenharia nas entrevistas |
| **RFQs com formato variável** | Médio | Parser flexível + validação humana em sandbox |
| **Custo de IA estoura teto** | Médio | Cache, batch, modelo mais barato para consultas simples |
| **Engenheiro não confia no sistema** | Alto | Estratégia "sandbox" — humano sempre valida antes de publicar |
| **Dois casos de uso complexos em 24 semanas** | Alto | Priorizar 1 caso como MVP (provável caso 1 — desenhos) |

## 11. Dependências externas

- **Cladtek** — acesso a desenhos reais, RFQs, parâmetros internos, engenheiros para entrevistas
- **Templo** — design system, infra de produção, AI Officer, GP
- **Acesso a dados** — formato real dos desenhos (SolidWorks/PDL/PDF), base de parâmetros

## 12. Stakeholders

| Papel | Quem |
|---|---|
| Responsável técnico | Lucas Cid |
| Gestor de projeto (GP) | Templo (a definir nome) |
| Chief AI Officer | Templo (a definir nome) |
| Cliente (engenharia) | Cladtek (contato a definir) |
| Infraestrutura | Templo |

---

## 📝 Pendências para fechar este PRD

- [x] ~~Confirmar stack: N8N (contratual) vs Agno (padrão interno)~~ → **Agno confirmado (29/07)**
- [ ] Obter amostras reais de desenho + RFQ + parâmetros Cladtek
- [ ] Confirmar formato dos desenhos (SolidWorks/PDL/PDF) e método de extração
- [ ] Confirmar formato das RFQs e método de parsing
- [ ] Definir LLM (precisa de visão + texto)
- [ ] Definir base semântica (onde armazenar parâmetros e capacidades)
- [ ] Definir stack de auth (~20 usuários)
- [ ] Priorizar casos de uso: qual é o MVP da semana 12?
