# Blue V3 — Especificação dos Kanbans

> **Profile:** pm
> **Projeto:** plataforma-blu
> **Data:** 2026-08-11
> **Tipo:** spec (kanbans — etapas, fluxos, regras)
> **Status:** 🟡 Proposta para validação do fundador — antes do trabalho de design

---

## 1. Recapitulação (onde estamos)

Direção da Fase 0 já validada:

- **Home = urgências** — cartões mostram o que está parado/atrasado/aguardando aprovação e levam direto ao ponto na sala.
- **Toda sala = dimensão do negócio com kanban** — andamento, cores (semáforo verde/amarelo/vermelho), onde as coisas pararam, ações.
- **Aprovações explícitas** por etapa sensível; a Home cobra o aprovador.
- **Rotinas por dimensão** reusando a Rotina API existente (catálogo + builder chat + triggers manual/schedule/event/numeric/cron + "rodar agora" + feed).
- **Multi-usuário** — papéis fixos (visualizador/criador/aprovador por sala).
- **Reorganizar, não reconstruir** — o kanban é a única peça grande nova do front.

Estrutura final: Home + 6 salas (Clientes, Financeiro + Compras, Agenda, Estratégia, Documentos, Biblioteca).

**Este documento detalha as etapas de cada kanban** para sentir e decidir antes do design.

---

## 2. Modelo do card (base comum)

Cada card do kanban representa **uma unidade de trabalho da dimensão** (um cliente, uma compra, um fechamento, um documento). Todo card tem:

| Campo | Exemplo |
|---|---|
| Título | Nome do cliente / item de compra / documento |
| Etapa interna | Rascunho, aguardando aprovação, enviado... |
| Semáforo | 🟢 no prazo · 🟡 parado há X dias · 🔴 atrasado/urgente |
| Responsável | Quem está com a bola (dono, membro ou agente IA) |
| Aprovador | Quem precisa aprovar na etapa sensível |
| Prazo | Data limite (opcional) |
| Interlocutores | Com quem o dono fala sobre isso |
| Ações | Mover etapa, aprovar, gerar artefato, delegar, comentar |

> **Decisão de design proposta:** colunas = estágios grandes do fluxo; dentro do card, um **badge de etapa interna** (sub-estado). Assim o dono vê de longe em qual estágio cada item está, sem poluir o quadro com 15 colunas.

---

## 3. Sala CLIENTES — Kanban de relacionamento (CRM)

### 3.1 Fluxo narrado pelo fundador (recapitulação)

```
Mensagem do cliente entra
  → card nasce no estágio de CONVERSA
  → agente de IA elabora uma resposta (rascunho)
  → dono aprova a resposta (ou edita e aprova)
  → resposta enviada ao cliente
  → enquanto for só troca de mensagens, o card fica no estágio de CONVERSA

Fechou a compra
  → card move para o estágio de ORÇAMENTO / COTAÇÃO
  → agente monta o orçamento (itens, quantidades, preços)
  → dono aprova e envia ao cliente

Orçamento aceito
  → card move para o estágio de ARTEFATO
  → sistema gera: nota fiscal, pedido de envio, contrato para assinar, orçamento final
```

### 3.2 Colunas do kanban (proposta)

| # | Coluna | O que acontece | Quem age | Semáforo típico |
|---|---|---|---|---|
| C1 | 💬 Conversa | Mensagem entra; agente rascunha resposta; dono aprova; resposta sai; aguarda cliente | Agente rascunha → dono aprova | 🔴 se cliente esperando há tempo |
| C2 | 🧾 Orçamento | Fechou a compra; agente monta cotação/orçamento; dono aprova e envia; cliente responde | Agente monta → dono aprova | 🟡 se orçamento parado com o cliente |
| C3 | 📎 Artefatos | Gerar NF, pedido de envio, contrato (assinatura), orçamento final | Sistema gera → dono revisa | 🟡 se falta artefato para fechar |
| C4 | ✅ Fechado | Venda concluída, entregue | — | 🟢 |
| C5 | 🔁 Recorrência | Cliente ativo, recompra, follow-up agendado | Rotina de follow-up | 🟡 se parado sem contato |

> Evolução vs. Fase 0 (Contato → Proposta → Em andamento → Entregue → Recorrência): o novo desenho separa **conversa** (negociação ainda aberta) de **orçamento** (compra fechada) e adiciona **artefatos** (formalização). Fica mais fiel à operação real.

### 3.3 Sub-estados do card (etapa interna)

**C1 — Conversa:**
`Nova mensagem → Rascunho do agente → Aguardando aprovação → Enviada → Aguardando cliente → (volta ao início se cliente responde)`

**C2 — Orçamento:**
`Montando → Aguardando aprovação → Enviado ao cliente → Aguardando aceite → Aceito`

**C3 — Artefatos:**
`Gerando → Aguardando revisão → Enviado → Assinado/Confirmado`

### 3.4 Regras de negócio (candidatas)

| # | Regra | Motivo |
|---|---|---|
| R1 | Toda resposta do agente ao cliente passa por aprovação do dono antes do envio | Controle total do relacionamento |
| R2 | Movimento Conversa → Orçamento é **sugerido pelo agente, confirmado pelo dono** (detecta intenção de compra) | Não mover cliente sem querer |
| R3 | Orçamento aceito = gatilho para abrir o estágio de artefatos | Fluxo natural |
| R4 | Artefatos gerados a partir de templates (api/documents) — contrato, NF, pedido de envio | Reutilizar o que existe |
| R5 | Cliente sem interação há X dias (configurável) → semáforo amarelo e follow-up na Home | Não deixar cliente esfriar |

### 3.5 Mensagens — decisão (12/08)

- **Canais:** WhatsApp, e-mail ou mensagem direta — arquitetura extensível a outros canais (decisão D6 em clientes.md). A aprovação do dono acontece na plataforma; o envio acontece no canal do cliente.

---

## 4. Sala FINANCEIRO — Kanban de Compras

### 4.1 Fluxo narrado pelo fundador (recapitulação)

```
Rotina (ex.: "reposição de ingredientes", semanal)
  → gera/coleta uma LISTA DE COMPRAS (requests: materiais, ingredientes, insumos)
  → agente MANDA MENSAGENS (para fornecedores) cotando cada item
  → agente RECEBE as respostas (preços, prazos, disponibilidade)
  → consolida as cotações no card
  → dono aprova a compra
  → pedido sai, entrega chega, pagamento é feito
  → o card anda no kanban durante todo esse caminho
```

### 4.2 Colunas do kanban (proposta)

| # | Coluna | O que acontece | Quem age |
|---|---|---|---|
| P1 | 📥 Solicitação | Request entra (manual, rotina de reposição, estoque baixo, lista importada) | Dono ou rotina |
| P2 | 💬 Cotação | Agente dispara mensagens aos fornecedores, recebe respostas, consolida preços/prazos | Agente (mensageria) |
| P3 | ⚖️ Aprovação | Dono aprova/rejeita a compra com base nas cotações | Dono (aprovador) |
| P4 | 📦 Pedido enviado | Ordem de compra enviada ao fornecedor vencedor | Agente/dono |
| P5 | 🚚 Recebimento | Entrega recebida, conferida | Dono/membro |
| P6 | 💳 Pago | Conta a pagar/pagamento — integra o financeiro | Sistema |

### 4.3 Rotina de mensagens (detalhe)

```
1. Rotina dispara (schedule — ex.: toda segunda 8h)
2. Gera lista de compras: itens + quantidades estimadas
   (fonte: rotina de estoque, pedidos recorrentes, ou lista manual)
3. Para cada item (ou lote), agente prepara mensagem de cotação
4. Mensagens enviadas aos fornecedores (canais: e-mail / WhatsApp / formulário)
5. Respostas voltam → agente normaliza (preço, prazo, frete, disponibilidade)
6. Card passa de Cotação → Aprovação com resumo comparativo
7. Dono aprova → Pedido enviado
8. Acompanha entrega → marca Recebimento → integra Pago
```

### 4.4 Regras de negócio (candidatas)

| # | Regra | Motivo |
|---|---|---|
| R1 | Compra acima de R$ X (configurável) exige aprovação | Controle de gasto |
| R2 | Aprovação de compra gera transação/despesa no Financeiro (integração) | Um lugar só |
| R3 | Fornecedores têm rating; cotação nova considera rating + histórico | Decisão melhor |
| R4 | Pedido sem resposta do fornecedor em X dias → alerta na Home | Não deixar compra parada |
| R5 | Compras recorrentes podem virar rotina automática (ex.: reposição semanal) | Reduz trabalho do dono |

### 4.5 Onde fica na sala

Proposta: **aba "Compras" dentro do Financeiro** com o kanban próprio (solicitação → pago), mantendo o kanban do fechamento (coleta → balanço) na aba principal. As métricas de compras (fornecedores, RFQs, spend) já existem e sobem para o topo da sala.

---

## 5. Varredura — kanbans das demais salas

| Sala | Kanban | Colunas (proposta) | Status |
|---|---|---|---|
| 🏠 Home | Centro de urgências (não é kanban — agrega cards das salas) | — | 🟥 Construir |
| 📊 Financeiro | Fechamento | Coleta → Conciliação → DRE → Balanço → Aprovado | 🟥 Construir |
| 📊 Financeiro | Compras | Solicitação → Cotação → Aprovação → Pedido → Recebimento → Pago | 🟥 Construir |
| 👥 Clientes | Relacionamento | Conversa → Orçamento → Artefatos → Fechado → Recorrência | 🟥 Construir |
| 📄 Documentos | Geração de documentos | Rascunho → Revisão → Aprovação → Assinatura → Arquivado | 🟥 Construir |
| 🎯 Estratégia | Iniciativas/planos | Ideia → Analisada → Planejada → Em execução → Revisada (kanban leve; o resto da sala é mapa de processos, SWOT, RACI — não-kanban) | 🟥 Construir |
| 📚 Biblioteca | Documentação canônica | Minuta → Revisão → Aprovada → Publicada | 🟥 Construir |
| 📅 Agenda | — | Não-kanban (Gantt + agenda do dia + Google Calendar) | — |

> Padrão único percebido: **entrada → trabalho com aprovação → artefato/resultado → acompanhamento**. Clientes e Compras detalhados aqui; Documentos e Biblioteca seguem o mesmo esqueleto com menos sub-estados; Estratégia é o único kanban leve.

---

## 6. Decisões em aberto (validar antes do design)

1. **Canal de mensagens do cliente:** WhatsApp API, e-mail, formulário, chat interno? (define integração e o fluxo de aprovação/envio)
2. **Aprovação de resposta:** toda mensagem exige aprovação do dono, ou só a primeira / ou configurável por cliente?
3. **Quem move Conversa → Orçamento:** agente sugere e dono confirma, ou o dono move manualmente?
4. **Compras:** as colunas batem com a operação real (solicitação → cotação → aprovação → pedido → recebimento → pago)?
5. **Lista de compras:** de onde vem (rotina de estoque, lista manual, importação)? A rotina gera automaticamente ou só lembra o dono?
6. **Limite de aprovação:** compras acima de quanto exigem aprovação? (R$ 500? R$ 1.000? configurável)
7. **Cliente sem contato:** após quantos dias o card fica amarelo e vira follow-up?

---

## 7. Próximo passo

Após validação destas decisões → fechar a spec de UI de cada kanban (elementos, estados visuais, interações de arrastar/expandir/approve) e só então partir para o design.
