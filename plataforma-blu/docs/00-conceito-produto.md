# Conceito de Produto — Blu e MCP Brain

**Profile:** design-writer
**Projeto:** plataforma-blu (raiz) · mcp-brain (memória)
**Data:** 2026-08-12 (v2 — revisão com o app atual, terceira iteração)
**Tipo:** conceito de produto — product review interno, referência futura
**Status:** vivo. Atualizar a cada decisão de produto.

---

## Objetivo

Referência única do conceito dos dois produtos: o que são, por que existem,
como se relacionam e como comunicar o valor. Documento interno de produto
(product review): uso em decisões de produto, roadmap, propostas e pitches.

Fontes desta versão: conversa do fundador em 2026-08-12, o app atual
(`monorepo/apps/blu_web`, terceira iteração do produto — referência de
versão final), o plano de produto do memory_api
(`docs/memory_api/plano-produto.md`) e a visão do MCP Brain
(`mcp-brain/docs/01-visao.md`).

## O problema

Empresa pequena de serviço roda a gestão inteira do mesmo jeito há anos:
lead no WhatsApp, proposta na planilha, contrato no Word, documento perdido
em pasta. O fluxo é sempre o mesmo — e o dono refaz ele do zero a cada
cliente, enquanto decide sozinho.

Do outro lado, o conhecimento da empresa está espalhado em arquivos e na
cabeça das pessoas. Qualquer ferramenta de IA que entra na empresa nasce
sem memória do negócio: pergunta sem contexto, resposta genérica.

## Blu — a suíte de gestão das pequenas empresas

### O que é

A Blu é uma suíte para pequenas empresas fazerem toda a gestão usando IA.
Um ambiente só para o fluxo inteiro: clientes, propostas, contratos,
documentos e finanças.

### Centralizar muda o jogo

Centralizar não é organização. Com a gestão inteira num lugar, a empresa
tem **contexto unificado** — todos os dados dela num só contexto. E com
contexto unificado a IA faz muito mais do que executar fluxo:

- **Estratégia** — leitura do negócio inteiro, não de uma planilha.
- **Captação e capacidade** — quanto o dono pode investir, quanto pode
  tomar de crédito, onde buscar capital, com base nos números reais dele.
- **Crescimento** — ideias de aquisição e expansão que aparecem quando os
  dados de clientes, financeiro e operação estão no mesmo lugar.
- **Documentos e apresentações** — proposta, contrato, relatório, deck:
  o contexto já está lá, a IA monta.
- **Skills e agentes** — habilidades de IA plugadas na operação: atendente,
  rotinas, agentes construídos sob medida.

O fluxo (lead → contrato) é a porta de entrada. O contexto unificado é o
produto.

### O produto hoje (referência: terceira iteração)

A versão de referência é o app atual — a terceira iteração do produto, no
caminho de versão final. Mapa de superfícies:

| Área | Superfícies |
| --- | --- |
| Gestão | Clientes, Agenda, Documentos, Financeiro, Compras |
| Conhecimento | Biblioteca com grafo de documentos, Memória de negócio (MCP Brain) |
| Estratégia | Estratégia, Insights, Analytics, Relatório de contexto |
| Agentes / skills | Agentes (construtor), Rotinas, Atendente, Chat |
| Governança | Aprovações (com regras), LGPD, Admin |

### Por que começar pelas empresas de serviço

Empresa de serviço tem fluxo uniforme. O passo a passo se repete em todas:

1. conversa com o lead;
2. fecha o serviço (ex.: treinamento);
3. gera os documentos;
4. escreve a proposta;
5. escreve o contrato.

Processo uniforme é processo padronizável. Padronizado, a IA automatiza o
que é repetitivo e o dono decide o que é dele.

### Exemplos de aplicação

- **R&M** — primeira campanha, vertical de serviços. Primeiro caso real do fluxo.
- **Financeiro** — próximo exemplo. A mesma lógica de padronização aplicada
  à gestão financeira da PME.

### Como comunicar

**Uma frase:**
"Blu é a suíte de gestão para pequenas empresas de serviço. Centraliza o
fluxo inteiro — do lead ao contrato — e usa o contexto unificado para fazer
muito mais com IA: estratégia, captação, documentos, apresentações."

**Elevator pitch:**
"Empresa de serviço vive de repetir o mesmo fluxo: conversa com o lead,
fecha o serviço, monta a proposta, escreve o contrato. A Blu centraliza
esse fluxo e usa IA no trabalho repetitivo. A pessoa decide; a IA executa.
Com os dados centralizados, o contexto unificado destrava o resto: quanto
o dono pode investir, quanto pode captar, onde a operação ganha e perde,
documentos e apresentações prontos. Começamos por serviços porque o
processo é uniforme; o financeiro é o próximo."

**Mensagens-chave:**
- "Um fluxo só, do lead ao contrato."
- "Decisão é do dono. O repetitivo é da IA."
- "Os dados centralizados viram contexto — e o contexto vira estratégia."
- "Quanto pode investir, quanto pode captar: a resposta está nos dados dele."
- "Gestão inteira num lugar: clientes, propostas, contratos, documentos, financeiro."

**CTA:** "Começar com sua operação" · "Agendar um diagnóstico gratuito"

## MCP Brain — a memória do Blu

### O que é

O MCP Brain é a memória da Blu. O Blu usa ele para saber o que a empresa
sabe. E ele é produto próprio, vendável para fora — qualquer empresa que
rode agentes de IA.

### O valor

- **Memória compartilhada e corporativa.** O que a empresa sabe fica na
  empresa: políticas, procedimentos, processos, decisões. Um corpus curado,
  com o que está vigente e com histórico.
- **Organizada em grafo de conhecimento.** Entidades e relações extraídas
  dos documentos, navegáveis. Busca em arquivo devolve documento; o grafo
  devolve relação: quem, o quê, como se conecta.
- **Bancos de memória.** A memória viva de cada pessoa — o dono (acionista)
  e o time —, cada um com o seu banco, com recência, autoria e
  compartilhamento explícito. O que é do time fica no time; o que é da
  pessoa fica da pessoa.

### Como funciona (uma frase cada)

- **Corpus curado:** documentos vigentes, aprovados pelo dono antes de
  virar conhecimento corporativo. Um por empresa.
- **Memória viva:** registro contínuo por pessoa; o dono e cada um do time
  têm o seu banco.
- **URL MCP:** a empresa conecta uma URL e qualquer agente compatível
  (Claude, Cursor, agentes próprios) consulta via MCP.
- **Página do dono:** o dono administra o corpus — aprova, resolve
  contradições, vê insights. (Ver `docs/memory_api/design-pagina-do-dono.md`)

### Como comunicar

**Uma frase:**
"A memória da sua empresa, organizada em conhecimento, disponível para
qualquer agente de IA."

**Elevator pitch:**
"A empresa guarda o que sabe em documentos espalhados e na cabeça das
pessoas. O MCP Brain junta isso: um corpus curado com o que está vigente,
uma memória viva por pessoa, bancos de memória do dono e do time, tudo
organizado em grafo. Qualquer agente de IA consulta por uma URL MCP — o
conhecimento sai do documento e vira resposta com fonte."

**Mensagens-chave:**
- "O que a empresa sabe fica na empresa."
- "Conhecimento organizado, com relação entre fatos — não busca solta em arquivo."
- "O dono e cada pessoa têm o seu banco de memória."
- "Uma URL MCP. Qualquer agente responde com base no que a empresa sabe."

**CTA:** "Conectar minha empresa"

## A relação Blu ↔ MCP Brain

- O Blu usa o MCP Brain como memória: o Blu é o primeiro cliente da própria
  memória (dogfooding).
- O MCP Brain é produto independente: vende para qualquer empresa que rode
  agentes de IA.
- A separação é explícita (decisão D-12 do memory_api): auth e control plane
  próprios; o Blu vira um tenant como outro qualquer.
- A página do dono é a porta do MCP Brain para o dono da empresa — dentro
  do Blu e fora dele.

## Como falamos disso — tabela de comunicação

| | Blu | MCP Brain |
|---|---|---|
| Uma frase | Suíte de gestão para pequenas empresas de serviço; centraliza o fluxo do lead ao contrato e usa o contexto unificado para estratégia, captação, documentos e apresentações | A memória da empresa, organizada em conhecimento, disponível para qualquer agente de IA |
| Elevator | Fluxo repetido a cada cliente: lead → serviço → proposta → contrato. A Blu centraliza e automatiza o repetitivo; o contexto unificado destrava estratégia e capacidade | Documentos espalhados + cabeça das pessoas viram corpus curado, memória viva e bancos do dono e do time; qualquer agente consulta via MCP |
| Mensagens | Um fluxo só · Decisão é do dono · Dados viram contexto, contexto vira estratégia · Capacidade de investir e captar nos dados dele | O que a empresa sabe fica na empresa · Grafo, não busca solta · Banco do dono e de cada pessoa · URL MCP |
| CTA | Começar com sua operação | Conectar minha empresa |
| Cliente herói | O dono da empresa de serviço | O dono e o time que usam IA |
| Papel da IA | Ferramenta que executa o repetitivo e destrava o contexto | Camada de memória que dá contexto |

## O que NÃO dizemos

- "Chat com seus PDFs" — reduz o MCP Brain a busca em arquivo.
- "IA que transforma sua empresa" — hype sem entregável.
- "Memória infinita" — vago; não diz o que o dono ganha.
- "Escritório virtual" como abertura — vago demais; a abertura é o fluxo
  do lead ao contrato.
- Reduzir a Blu a "CRM" ou a "fluxo de proposta" — ela é a gestão inteira
  e o contexto que ela destrava.
- Qualquer frase em que a IA é o herói da história.

## Glossário (termos com significado fixo)

- **Corpus:** conjunto curado de documentos vigentes (políticas, procedimentos,
  processos). Um por empresa.
- **Memória viva:** registro contínuo por pessoa; o que cada um aprende, decide
  e compartilha.
- **Banco de memória:** unidade da memória viva; um por escopo (pessoal,
  compartilhado, corpus).
- **Grafo de conhecimento:** entidades e relações extraídas dos documentos,
  navegáveis.
- **MCP:** Model Context Protocol — padrão aberto de conexão entre agentes de
  IA e ferramentas.
- **Contexto unificado:** todos os dados da gestão num só lugar; a base de
  qualquer resposta, estratégia ou documento gerado pela IA.
- **Curadoria:** aprovação do dono antes de um documento virar conhecimento
  corporativo vigente.
- **Vigência:** o que vale agora, com histórico do que valeu antes.
- **Contradição:** dois autores dizem coisas diferentes; detecção automática,
  resolução humana.
- **Tenant:** uma empresa cliente do produto, com os seus dados isolados.

## Perguntas em aberto

- [ ] Registrar o case R&M como referência da vertical de serviços (nome
      completo, fluxo, resultados).
- [ ] Definir o modelo de cobrança do MCP Brain (por usuário, por GB, por chamada).
- [ ] Confirmar se o grafo de conhecimento é núcleo do produto ou feature
      opcional da V1.
- [ ] Fixar a persona primária do MCP Brain (dono da empresa × time de tecnologia).
- [ ] Consolidar a nomenclatura oficial da terceira iteração ("Blueprint 3").

## Próximos passos

- [ ] Aprovar este conceito e linkar nos READMEs de plataforma-blu e mcp-brain.
- [ ] Usar a seção "Como comunicar" como base da landing de cada produto.
- [ ] Manter o mapa de superfícies sincronizado com o app (a cada iteração).
- [ ] Atualizar este documento a cada decisão de produto.
