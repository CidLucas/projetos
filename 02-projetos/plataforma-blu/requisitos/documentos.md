# 📄 Documentos — Tela de Requisitos de UI (Blue V3)

> Última atualização: 2026-08-12 | Status: 🟡 Em andamento (spec v1 para design)
> Segue o padrão de [template-tela.md](./template-tela.md). Proposta análoga em [proposta-financeiro.md](./proposta-financeiro.md) — esta sala segue o **padrão de sala de fluxo + processos** estabelecido no Financeiro. Padrão do painel contextual em [clientes.md](./clientes.md).
> **Princípio:** elementos puros — informação + ação. Nenhum elemento é amarrado ao design atual da Blu; tudo nasce como novo conceito.
> **Fonte do comportamento atual:** a aba "documentos" de `apps/blu_web/src/pages/app/EstrategiaRoom.tsx` + tabelas `documents` / `doc_templates` + agente `documentos` (aprovações) + trigger `document_created` da routines_api — mas especificado como novo conceito, sem referência a componentes atuais.

---

## 1. Visão da sala (conceito)

> A sala **Documentos é a dimensão da formalização do negócio — e é um fluxo.** Um documento nasce de um fluxo da empresa (financeiro: relatório de fechamento; clientes: proposta, contrato; estratégia: plano) e, ao chegar na sala, **passa por etapas** — rascunho → revisão → aprovação → publicado. Cada documento carrega **metadados** (tipo, seções, cliente, produto, período, valor) que permitem **buscar e reencontrar** qualquer documento pelo que ele é, e **acessar o corpo** (o texto do documento) quando precisar usá-lo de novo.
> A base de tudo é o **modelo**: o dono cria modelos de documento (e de contrato), alimenta cada modelo com **exemplos** (ex.: 3 exemplos por tipo de contrato), e o agente usa o modelo + exemplos para gerar o corpo do documento. Modelo vira biblioteca reutilizável: "quero fazer um contrato de prestação de serviço" → busca por tipo → abre o modelo → gera o documento com o corpo do modelo.

---

## 2. Layout macro da tela

```
┌──────────────────────────────────────────────────────────────────────────┐
│ A · Topo:  [Documentos 3] [Processos 2] [Modelos] [Histórico] [Rotinas]  │
│            (abas discretas — sem faixa horizontal; sem strip de métricas)│
├───────────────────────────────────────────────────────┬──────────────────┤
│ B · VISÃO DA ABA ATIVA                                │ C · PAINEL       │
│   Documentos→ FilaDocumentos (tipo + status +         │   CONTEXTUAL     │
│              semáforo + metadados)                    │   (fixo ~380px)  │
│   Processos→ QuadroProcessos 4 colunas:               │   muda por ABA:  │
│              📝 Rascunho │ 👀 Revisão │ ✅ Aprovação │   Documentos→Doc.│
│              🚀 Publicado                             │   Processos→Proc.│
│   Modelos  → GradeModelos (sistema + próprios)        │   Modelos→Modelo │
│   Histórico→ TimelineDocumentos                       │   Histórico→Event│
│   Rotinas  → catálogo + configuradas + feed           │   Rotinas→Rotina │
│                                                       │   (qualquer)→Prev│
├───────────────────────────────────────────────────────┴──────────────────┤
│ D · QUADRINHOS:  [Insights do agente] [Métricas + comparações] [Modelos] │
└──────────────────────────────────────────────────────────────────────────┘
```

Layout do design inicial (padrão 12/08): **Topo (abas discretas) + Quadro + Painel direito fixo + Quadrinhos (D)**. **Não existe strip de métricas.** **O painel direito é contextual** — muda de modo conforme a aba ativa e o item selecionado (ver §4). **Dois mundos na sala:** o **fluxo de documentos** (fila com status e metadados) e os **processos de geração** (missões em etapas com portas de aprovação), sustentados pela **biblioteca de modelos** (com exemplos e metadados).

---

## 3. Região A — Topo

### 3.1 Navegação por abas (discretas, sem strip)
- **Elemento:** `NavegacaoAbas` (novo conceito)
- **Propósito:** trocar entre as 5 visões da sala **sem faixa horizontal** — abas como texto discreto com indicador de estado (cor + peso + contador), sem fundo, sem borda, sem barra sublinhada
- **Abas (ordem):** Documentos (padrão) · Processos · Modelos · Histórico · Rotinas
- **Conteúdo (informações):** nome da aba + contador de pendência quando houver (ex.: Documentos "3" · Processos "2")
- **Opções:** nenhuma além da própria troca de aba (abas fixas da dimensão)
- **Ações:** clique troca a visão; persiste a última aba por sessão (U1)
- **Estados:** ativa (destaque de cor) / inativa / com pendência (contador)
- **Visibilidade:** sempre
- **Feedback:** transição suave da visão

### 3.2 Busca
- **Elemento:** `CampoBusca`
- **Propósito:** achar documento, modelo ou processo por texto **e por metadado** (tipo, cliente, produto, período)
- **Conteúdo (informações):** placeholder "Buscar na sala de documentos..."; resultados em painel suspenso agrupados por aba (Documentos / Modelos / Processos), mostrando metadados do item encontrado (ex.: "Contrato de prestação — Cliente X · serviço de TI · 2026")
- **Ações:** digitar filtra (título + metadados); Enter confirma e abre o primeiro resultado no painel contextual
- **Estados:** vazio / digitando (sugestões) / sem resultados ("Nada encontrado") / loading
- **Visibilidade:** sempre no topo

### 3.3 Filtros da visão ativa
- **Elemento:** `Filtros`
- **Propósito:** restringir a visão da aba ativa por atributos
- **Opções (por aba):**
  - Documentos: Status (rascunho/revisão/aprovação/publicado/arquivado) · Tipo (relatório/proposta/contrato/ata/política/...) · Modelo · Cliente/Produto · Período · Semáforo
  - Processos: Etapa (todas/rascunho/revisão/aprovação/publicado) · Tipo de processo · Semáforo
  - Modelos: Categoria · Tipo (documento/contrato/...) · Origem (sistema/próprios) · Com exemplos (sim/não)
  - Histórico: Período · Tipo de evento · Agente · Documento
- **Ações:** múltiplos filtros combináveis; "Limpar filtros" aparece quando há filtro ativo
- **Estados:** ativo (badge com contagem de filtros) / inativo
- **Visibilidade:** sempre

### 3.4 Botão "Novo documento"
- **Elemento:** `BotaoPrimario` (ícone +)
- **Propósito:** criar um documento (rascunho) — caminho principal de entrada do fluxo
- **Ações:** abre o overlay de criação (Região E — 6.1); o documento nasce na etapa Rascunho do processo de geração (U2)
- **Estados:** default / hover / disabled (sem permissão de criar — Admin por sala)
- **Visibilidade:** sempre

---

## 4. Região B — Visão da aba ativa

### 4.1 Aba Documentos (a fila do fluxo)

> Conceito: **o fluxo do documento dentro da sala** — onde cada documento está (rascunho, em revisão, aguardando aprovação, publicado, arquivado), o que ele é (tipo, modelo, metadados) e o que precisa de atenção (semáforo). O dono entra para ver o que está andando e o que está parado — e busca por qualquer documento pelo tipo/metadado.

### 4.1.1 Cabeçalho da visão
- **Elemento:** `CabecalhoVisaoDocumentos`
- **Propósito:** resumir e filtrar a fila de documentos
- **Conteúdo (informações):** título "Documentos" + subtítulo ("3 em andamento · 1 aguardando aprovação")
- **Opções (filtros):** Status · Tipo · Modelo · Cliente/Produto · Período · Semáforo (3.3)
- **Ações:** filtros combináveis; "Limpar filtros" quando ativo; ordenar por (urgência/recência/título/tipo)
- **Estados:** filtro ativo (badge) / inativo
- **Visibilidade:** sempre na aba Documentos

### 4.1.2 Fila de documentos
- **Elemento:** `FilaDocumentos`
- **Propósito:** o dono vê todos os documentos da dimensão, onde cada um está no fluxo e o que precisa dele — sem caçar
- **Conteúdo (informações):** lista de `CartaoDocumento` (4.1.3) ordenada por semáforo (🔴→🟡→🟢) e recência
- **Ações:** scroll; clique → painel Modo Documento (4.4); seleção múltipla → barra de lote (4.1.4)
- **Estados:** loading (esqueleto) / vazio ("Nenhum documento ainda — crie o primeiro com um modelo" + CTA "Novo documento") / erro (recarregar)
- **Visibilidade:** sempre na aba Documentos

### 4.1.3 Card de documento
- **Elemento:** `CartaoDocumento`
- **Propósito:** o documento em uma linha — o dono entende o que é, de que fluxo veio, onde está e até quando
- **Conteúdo (informações):**
  - Tipo com ícone (Relatório 📊 · Proposta 📋 · Contrato 📜 · Ata 📝 · Política 🏛 · Invoice 🧾 · outro)
  - Título (ex.: "Contrato de prestação de serviço — Cliente X", "Fechamento mensal — Julho")
  - Status do fluxo (Rascunho · Em revisão · Aguardando aprovação · Publicado · Arquivado)
  - Semáforo 🟢/🟡/🔴 (borda esquerda) + badge ("Parado há 5d na revisão" · "Aprovação pendente" · "Publicado")
  - **Metadados-chave** (chips): modelo usado, cliente/produto, período, valor quando aplicável
  - Origem do fluxo (financeiro/clientes/estratégia/chat) + responsável/agente
- **Opções (menu "..."):** Abrir · Editar · Ver processo · Duplicar · Publicar · Arquivar · Exportar PDF · Excluir (confirmação)
- **Ações:** clique → painel Modo Documento; **ações rápidas no hover**: Editar · Publicar (com permissão) · Arquivar; checkbox de seleção (hover); sem permissão → desabilitado com dica
- **Estados:** default / hover / selecionado / urgente (destaque) / disabled (sem permissão)
- **Feedback:** toast ("Documento publicado", "Arquivado — você pode restaurar no Histórico")
- **Visibilidade:** sempre que há documentos

### 4.1.4 Barra de ações em lote (Documentos)
- **Elemento:** `BarraAcoesLote` (mesmo padrão Clientes/Financeiro)
- **Conteúdo (informações):** contador ("3 selecionados") + ações
- **Ações:** Publicar selecionados (com permissão) · Mover para revisão/aprovação · Duplicar · Arquivar · Excluir (confirmação dupla) · Limpar seleção (Esc)
- **Estados:** visível com 2+ selecionados; ações desabilitadas sem permissão
- **Feedback:** toast contando ("2 documentos publicados")
- **Visibilidade:** substitui o cabeçalho enquanto há seleção

---

### 4.2 Aba Processos (geração de documentos — missões em etapas)

> Conceito (padrão Financeiro, adaptado): todo **documento formal é gerado por um processo com etapas** — o agente prepara o rascunho a partir do modelo (e dos exemplos), o dono revisa, aprova e o documento é publicado/entregue. **Etapas base: Rascunho → Revisão → Aprovação → Publicado** (U3); cada tipo de documento pode ajustar depois (ex.: contrato pode ter etapa de assinatura — em aberto 4). **Quem move o card = quem tem autorização** (permissões por sala no Admin). O documento que nasce no "Novo documento" vira um processo aqui (U2); o processo também pode nascer do chat ("gera uma proposta para o Cliente X") ou de rotina/insight.

### 4.2.1 Quadro de processos
- **Elemento:** `QuadroProcessos` (reusa o padrão do novo conceito)
- **Propósito:** o dono vê o estágio de cada documento do começo ao fim e destrava as aprovações
- **Conteúdo (informações):** 4 colunas fixas: 📝 **Rascunho** → 👀 **Revisão** → ✅ **Aprovação** → 🚀 **Publicado**; cada coluna com contador
- **Ações:** scroll horizontal; arrastar cards (quem tem permissão); clicar card abre o painel; **seleção múltipla** (4.2.3)
- **Estados:** loading (esqueleto) / vazio (mensagem + CTA "Novo documento") / erro (recarregar)
- **Feedback:** animação ao mover; toast em falha
- **Visibilidade:** sempre na aba Processos

### 4.2.2 Card de processo (documento em geração)
- **Elemento:** `CartaoProcesso`
- **Propósito:** resumo do documento em geração — o dono vê o que está sendo gerado, com qual modelo e onde está travado
- **Conteúdo (informações):**
  - Nome do documento + tipo (ex.: "Proposta comercial — Cliente Y", "Contrato de serviço — Cliente X")
  - Badge de sub-estado: "Aguardando aprovação" · "Rascunho sendo gerado" · "Em revisão" · "Em atraso" · "Publicado"
  - Semáforo 🟢 no prazo / 🟡 parado há X dias / 🔴 atrasado (borda esquerda)
  - Modelo usado (chip) + responsável/agente que gera
  - Metadados-chave quando aplicável (cliente, valor)
- **Opções (menu "..."):** Abrir documento · Ver modelo · Aprovar etapa (com permissão) · Arquivar · Excluir (confirmação)
- **Ações:** clique → painel Modo Processo; arrastar → mover entre etapas (porta de aprovação: mover para frente exige permissão de aprovar OU mover — configurado no Admin; **pular etapa exige confirmação** U4); checkbox de seleção
- **Estados:** default / hover / arrastando / selecionado / semáforo por cor / disabled (sem permissão)
- **Feedback:** toast ("Rascunho aprovado — documento publicado", "Rejeitado — voltou para Revisão")
- **Visibilidade:** sempre que há processos

### 4.2.3 Seleção múltipla + ações em lote (Processos)
- **Elemento:** `SelecaoMultipla` + `BarraAcoesLote` (mesmos padrões)
- **Ações:** checkbox no hover; Shift/Ctrl para intervalos; selecionar tudo na coluna; com 2+ → barra de lote: **Aprovar etapa dos selecionados** · **Mover para…** (escolher etapa) · **Arquivar** · **Limpar seleção** (Esc)
- **Estados:** ações desabilitadas se o usuário não tem permissão para a ação em algum selecionado
- **Feedback:** toast contando ("2 rascunhos aprovados")
- **Visibilidade:** comportamento do quadro; barra com 2+

### 4.2.4 Origem dos processos
- **Elemento:** (comportamento)
- **Ações:** "Novo documento" (6.1) cria o processo na etapa Rascunho (U2); o chat gera processo ("cria um contrato de serviço para o Cliente X"); o agente **propõe processos** proativamente (ex.: "Fechamento do mês está na hora — gerar?") — vira sugestão no Q1 (5.1) com ação "Gerar documento"; rotinas disparam geração (5.5)
- **Contador da aba Processos = portas de aprovação pendentes + processos parados (🟡/🔴)**

---

### 4.3 Aba Modelos (a biblioteca de modelos de documento)

> Conceito (direção do fundador 12/08): **o modelo é o coração da sala.** O dono cria um **modelo de documento** (relatório, proposta, ata...) e um **modelo de contrato**; cada modelo define estrutura (seções), **metadados** (o que descreve o documento: tipo, cliente, produto, período, valores) e pode receber **exemplos** (ex.: 3 exemplos por tipo de modelo de contrato) que ensinam o agente a gerar o corpo. Na hora de fazer um contrato, o dono **busca pelo tipo/metadado** → abre o modelo → gera o documento com o corpo do modelo. Modelo é reutilizável: um modelo gera N documentos.

### 4.3.1 Cabeçalho da visão
- **Elemento:** `CabecalhoVisaoModelos`
- **Propósito:** resumir e filtrar a biblioteca de modelos
- **Conteúdo (informações):** título "Modelos" + subtítulo ("8 do sistema · 3 próprios")
- **Opções (filtros):** Categoria · Tipo (documento/contrato/...) · Origem (sistema/próprios) · Com exemplos (sim/não) · busca por nome
- **Ações:** filtros combináveis; "Limpar filtros" quando ativo; ordenar por (usados/recência/nome)
- **Estados:** filtro ativo (badge) / inativo
- **Visibilidade:** sempre na aba Modelos

### 4.3.2 Grade de modelos
- **Elemento:** `GradeModelos`
- **Propósito:** o dono vê todos os modelos disponíveis — do sistema e os próprios — e usa/edita na hora
- **Conteúdo (informações):** cards de `CartaoModelo` (4.3.3) em grade; agrupáveis por categoria
- **Ações:** clique → painel Modo Modelo; botão "Usar" direto no card (cria documento — 6.1); seleção múltipla → lote (4.3.4)
- **Estados:** loading (esqueleto) / vazio ("Nenhum modelo — crie o primeiro" + CTA) / erro (recarregar)
- **Visibilidade:** sempre na aba Modelos

### 4.3.3 Card de modelo
- **Elemento:** `CartaoModelo`
- **Propósito:** o modelo em um card — o dono entende o que ele gera e se está pronto para usar
- **Conteúdo (informações):**
  - Ícone + nome (ex.: "Contrato de prestação de serviço", "Proposta comercial", "Relatório de fechamento mensal", "Ata de reunião", "Política interna")
  - Tipo (Documento · Contrato · Relatório · Ata · Política) + categoria
  - Origem (⭐ Sistema · 🔵 Próprio)
  - Descrição curta + nº de seções
  - **Metadados definidos** (chips: tipo, cliente, produto, período, valor)
  - **Exemplos**: contador "2 exemplos" + badge "Sem exemplos" quando vazio
  - Nº de documentos gerados + últimos usos
- **Opções (menu "..."):** Usar (gera documento) · Editar · Duplicar · Gerenciar exemplos · Definir como padrão (para o chat sugerir) · Excluir (confirmação)
- **Ações:** clique → painel Modo Modelo; hover → botão "Usar" rápido
- **Estados:** default / hover / selecionado / sem exemplos (destaque suave) / disabled (sem permissão de usar — ver Admin)
- **Feedback:** toast ("Documento gerado a partir de Contrato de prestação")
- **Visibilidade:** sempre que há modelos

### 4.3.4 Seleção múltipla + ações em lote (Modelos)
- **Elemento:** `BarraAcoesLote`
- **Ações:** Duplicar selecionados · Excluir (confirmação dupla) · Limpar seleção (Esc)
- **Visibilidade:** comportamento da grade; barra com 2+

---

### 4.4 Aba Histórico

> Conceito: a timeline da dimensão — tudo que aconteceu com documentos e modelos (criação, edição, aprovação, publicação, arquivamento, execução de rotina de geração).

### 4.4.1 Timeline de eventos
- **Elemento:** `TimelineDocumentos`
- **Propósito:** o dono audita o que aconteceu com os documentos — quem fez o quê, quando
- **Conteúdo (informações):** eventos ordenados por data: tipo (Criado · Editado · Revisado · Aprovado · Rejeitado · Publicado · Arquivado · Restaurado · Gerado por rotina) + documento/modelo + agente ou usuário + data/hora; rejeições com motivo
- **Ações:** filtros (período · tipo de evento · agente · documento); clique no evento → abre o item no painel contextual
- **Estados:** loading / vazio ("Nenhum evento ainda") / erro
- **Visibilidade:** sempre na aba Histórico

---

### 4.5 Aba Rotinas

> Conceito: o que o agente faz sozinho na dimensão documentos — reusa a Rotina API (catálogo built-in + builder chat + gatilhos + feed). Trigger `document_created` já existe no backend.

### 4.5.1 Cabeçalho + catálogo + lista + feed
- **Elemento:** `CabecalhoVisaoRotinas` + `CatalogoRotinas` + `RotinaCard` + `FeedExecucoes` + `BuilderRotina` (mesmos padrões de Clientes/Financeiro)
- **Propósito:** adicionar automações prontas da dimensão, acompanhar as configuradas e ver o que o agente gerou
- **Catálogo built-in (proposta — validar funções no backend):**
  - **Gerar relatório de fechamento mensal** — cria o processo/documento todo dia 5 (schedule)
  - **Revisão de propostas paradas** — alerta propostas em revisão há X dias (schedule diário)
  - **Revisão de políticas/contratos** — revisão semestral dos modelos canônicos (schedule)
  - **Alerta de documentos parados** — notifica documentos em rascunho/revisão sem movimento (schedule)
  - **Disparo por evento** — "quando um documento for criado, notificar o aprovador" (event — trigger `document_created` já existe)
- **Conteúdo (informações) do RotinaCard:** nome, gatilho legível, status ativa/pausada, última execução + resultado
- **Ações:** Rodar agora · Pausar/Retomar · Editar com IA (builder) · Ver execuções · Excluir (confirmação)
- **Estados:** ativa / pausada / executando (spinner) / erro na última execução (alerta)
- **Visibilidade:** sempre na aba Rotinas

---

## 5. Região C — Painel direito (faixa vertical, contextual)

> Painel lateral fixo (~380px). **Conceito:** o painel é a **lupa da sala** — mostra o detalhe do item selecionado e muda de **modo** conforme a aba ativa e o que foi clicado. Cada aba tem o seu modo; navegar para dentro de um item **empilha** na trilha (breadcrumb). No Modo Preview, o dono **vê o corpo do documento** sem sair do painel.

```
┌──────────────────────────────────────┐
│ C · PAINEL CONTEXTUAL (fixo ~380px)  │
│   Trilha: Contrato › Modelo ›        │
│           Preview                    │
├──────────────────────────────────────┤
│ Modo muda conforme ABA + seleção:    │
│  · Documentos → Modo Documento       │
│  · Processos  → Modo Processo        │
│  · Modelos    → Modo Modelo          │
│  · Histórico  → Modo Evento          │
│  · Rotinas    → Modo Rotina          │
│  · (qualquer) → Modo Preview (corpo) │
└──────────────────────────────────────┘
```

### 5.0 Contêiner e modos
- **Elemento:** `PainelContextual`
- **Modos:** Documento (5.4) · Processo (5.5) · Modelo (5.6) · Evento (5.7) · Rotina (5.8) · Preview (5.9)
- **Regra de troca (U5):** clicar num item de outra aba **substitui** o modo; navegar para dentro (ex.: ver o corpo do documento) **empilha** na trilha
- **Estados:** aberto (item selecionado) / fechado (X ou Esc limpa a trilha) / loading / erro
- **Visibilidade:** sempre à direita; sem item selecionado mostra "Selecione um item para ver o detalhe" (em aberto 7)

### 5.1 Cabeçalho do painel
- **Elemento:** `CabecalhoPainel` (contextual)
- **Conteúdo (informações):** ícone do modo + identidade do item (nome + semáforo + status) + menu "..." com ações do modo
- **Opções (menu por modo):** Documento — editar/publicar/arquivar/duplicar · Processo — aprovar etapa/arquivar · Modelo — editar/duplicar/exemplos · Rotina — rodar/pausar/excluir · Preview — baixar/enviar
- **Ações:** fechar (X); **"Ver no fluxo"** (disponível em Documento/Processo — troca para a aba Documentos/Processos e abre o item)
- **Visibilidade:** sempre que o painel está aberto

### 5.2 Trilha de navegação
- **Elemento:** `TrilhaNavegacao`
- **Conteúdo (informações):** breadcrumb da pilha (ex.: "Contrato — Cliente X › Modelo › Preview")
- **Ações:** clique em nível anterior desempilha; X fecha
- **Visibilidade:** 2+ níveis de pilha

### 5.3 Busca global (atalho do painel)
- **Elemento:** (comportamento)
- **Ações:** Ctrl/Cmd+K abre a busca (3.2) de qualquer lugar da sala; resultados com metadados; Enter abre no painel

---

### Modo Documento (aba Documentos)

### 5.4 Documento em foco
- **Elemento:** `PainelDocumento`
- **Propósito:** o dono vê o documento inteiro — o que é, de onde veio, metadados, corpo — e toma as ações do fluxo sem sair do painel
- **Conteúdo (informações):**
  - Identidade: título + tipo + status do fluxo + semáforo + responsável
  - **Metadados** (editáveis): modelo usado · cliente · produto · período · valor · tags
  - Origem do fluxo (financeiro/clientes/estratégia/chat/rotina)
  - **Seções do documento** (resumo da estrutura: nome das seções + status de preenchimento — preenchida/pendente)
  - Aprovações: quem aprovou/rejeitou cada porta + datas (ou "aguardando aprovação de X")
  - **Corpo**: preview do documento (empilha Modo Preview ao clicar em "Ver corpo")
- **Ações:** **Editar** (abre o editor no Modo Preview) · **Publicar** (com permissão) · **Mover para revisão/aprovação** · **Duplicar** · **Arquivar** · **Exportar PDF** · "Ver processo" (empilha Modo Processo)
- **Estados:** rascunho / em revisão / aguardando aprovação / publicado / arquivado / disabled (sem permissão)
- **Feedback:** toast ("Documento publicado", "Salvo")
- **Visibilidade:** sempre no Modo Documento

---

### Modo Processo (aba Processos)

### 5.5 Processo em foco
- **Elemento:** `PainelProcesso`
- **Propósito:** o dono vê o passo a passo da geração do documento, quem aprova cada porta, o modelo usado e os artefatos — e destrava as etapas sem sair do painel
- **Conteúdo (informações):**
  - Identidade: documento + tipo + semáforo + responsável
  - **Passo a passo das etapas** (Rascunho → Revisão → Aprovação → Publicado): check nas concluídas, **porta de aprovação atual em destaque** (badge "Aguardando aprovação" + quem aprova)
  - **Modelo usado** (chip → clique empilha Modo Modelo)
  - Artefatos por etapa (rascunho, versões revisadas, versão final) — visualizar empilha Modo Preview
  - Registro: quem fez o quê em cada etapa
- **Ações:** **Aprovar etapa** (só quem tem permissão — aprovar revisão / aprovar publicação) · **Rejeitar** (motivo opcional — volta uma etapa) · **Editar rascunho** (empilha editor) · **Gerar novamente** (dispara o agente para refazer o rascunho a partir do modelo+exemplos) · ver histórico do processo
- **Estados:** etapa concluída / porta pendente (destaque) / rejeitado (volta) / atrasado (semáforo) / disabled
- **Feedback:** toast ("Rascunho aprovado — documento publicado", "Rejeitado — voltou para Revisão")
- **Visibilidade:** sempre no Modo Processo

---

### Modo Modelo (aba Modelos)

### 5.6 Modelo em foco
- **Elemento:** `PainelModelo`
- **Propósito:** o dono entende o modelo completo — estrutura, metadados, exemplos, prompt — e usa/edita
- **Conteúdo (informações):**
  - Identidade: nome + tipo + categoria + origem (sistema/próprio) + descrição
  - **Estrutura (seções)**: lista das seções do modelo (ex.: Contrato → Cláusulas, Partes, Objeto, Valores, Vigência...)
  - **Metadados definidos**: quais campos o modelo pede na geração (tipo, cliente, produto, período, valor...)
  - **Exemplos**: lista dos exemplos alimentados (ex.: "Exemplo 1 — Contrato de TI", "Exemplo 2 — Contrato de limpeza") com status (sem exemplos → aviso); clique abre o exemplo no Modo Preview
  - **Prompt associado**: o que o agente deve fazer com o modelo (legível)
  - Nº de documentos gerados + últimos usos
- **Ações:** **Usar** (gera documento — 6.1) · **Editar** (estrutura, metadados, prompt) · **Adicionar exemplo** (6.4) · **Duplicar** · **Definir como padrão** (chat sugere este modelo) · **Excluir** (confirmação)
- **Estados:** default / sem exemplos (aviso) / disabled (sem permissão)
- **Feedback:** toast ("Exemplo adicionado", "Modelo marcado como padrão")
- **Visibilidade:** sempre no Modo Modelo

---

### Modo Evento (aba Histórico)

### 5.7 Evento em foco
- **Elemento:** `PainelEvento`
- **Propósito:** o dono vê o detalhe de um evento do histórico
- **Conteúdo (informações):** tipo do evento + documento/modelo envolvido + quem fez + quando + contexto (ex.: motivo de rejeição, versão alterada) + link para o item
- **Ações:** "Abrir documento" / "Abrir modelo" (empilha no modo correspondente)
- **Visibilidade:** sempre no Modo Evento

---

### Modo Rotina (aba Rotinas)

### 5.8 Configuração da rotina
- **Elemento:** `PainelRotina` (mesmo padrão Clientes/Financeiro)
- **Conteúdo (informações):** nome + descrição; gatilho/frequência legível; ação (o que gera/notifica); filtro; canal; status ativa/pausada; última execução + resultado
- **Ações:** editar campos direto (salva na hora) · **Editar com IA** (builder chat preenchido) · Rodar agora · Pausar/Retomar · Ver execuções · Excluir (confirmação)
- **Visibilidade:** sempre no Modo Rotina

---

### Modo Preview (corpo do documento / exemplo / modelo)

### 5.9 Preview do documento
- **Elemento:** `PainelPreview` (mesmo padrão Clientes/Financeiro)
- **Propósito:** conferir o **corpo do documento** (gerado ou exemplo) antes de publicar/enviar — dentro do painel, sem perder o contexto
- **Conteúdo (informações):** renderização do documento (modelo + dados preenchidos) + tipo/nome + status (rascunho/em revisão/aprovado/publicado)
- **Ações:** **Editar** (quando é rascunho/em revisão) · **Baixar PDF** · **Enviar** · **Aprovar/Finalizar** (se for porta de aprovação) · **Abrir documento completo** (quando o preview em 380px não bastar — abre editor de largura cheia) · Voltar (desempilha)
- **Estados:** loading (gerando) / erro de geração / sem template
- **Visibilidade:** sempre que um documento ou exemplo é visualizado

---

## 6. Região D — Quadrinhos (no plano)

> Decisão 11/08: os quadrinhos ficam no plano. As métricas da sala **moram aqui** (nunca numa strip horizontal no topo).

### 6.1 Q1 — Insights do agente de documentos
- **Elemento:** `InsightsSala`
- **Propósito:** sugestões proativas da IA sobre os documentos do negócio
- **Conteúdo (informações):** 2–3 cards de sugestão (ex.: "Contrato — Cliente X parado em revisão há 5 dias", "Fechamento do mês está na hora — gerar?", "Modelo 'Contrato de serviço' sem exemplos — adicionar?", "3 rascunhos sem movimento há 10 dias")
- **Opções por card:** Abrir documento · Gerar processo · Ver modelo · Dispensar
- **Estados:** vazio ("Sem insights agora") / loading
- **Visibilidade:** sempre

### 6.2 Q2 — Métricas da sala (com comparações)
- **Elemento:** `MetricasSala`
- **Propósito:** os indicadores da dimensão em um quadrinho compacto — no lugar da antiga strip do topo
- **Conteúdo (informações):** período 30d/90d/1y; métricas propostas: Documentos criados · Publicados · Pendentes de aprovação · Por tipo · Tempo médio do fluxo (rascunho→publicado) · Modelos em uso
- **Comparações (Q2b/D6 Financeiro):** cada métrica mostra **só as pills que fazem sentido**: vs mês passado (MoM) · vs mesmo mês do ano anterior (YoY) · vs média do ano anterior · vs média dos últimos 6 meses
- **Ações:** clique numa métrica → aba Documentos/Histórico filtrada; pills de comparação trocam o contexto exibido
- **Estados:** loading / sem dados ("Crie um documento para começar")
- **Visibilidade:** sempre

### 6.3 Q3 — Modelos rápido
- **Elemento:** `ModelosRapido`
- **Propósito:** usar o modelo mais comum sem trocar de aba
- **Conteúdo (informações):** modelos mais usados (ícone + nome) + atalho "Novo modelo"; sem modelos → CTA "Criar modelo"
- **Ações:** clique no modelo → abre o overlay de criação de documento com ele selecionado (6.1)
- **Visibilidade:** sempre

---

## 7. Overlays (Região E)

### 7.1 Overlay "Novo documento" (escolha de modelo + chat)
- **Elemento:** `OverlayBuilderDocumento`
- **Campos:** duas entradas:
  - **Buscar modelo** — lista de modelos (nome + descrição + tipo) com busca por nome/categoria/metadado + opção "Criar em branco" (em aberto 2) + atalho "Criar novo modelo" (leva a 7.3)
  - **Chat com o agente** — "Descreva o documento…" (ex.: "contrato de prestação de serviço para o Cliente X") → o agente sugere o modelo compatível (ou pergunta os metadados que faltam: cliente, produto, período, valor) → gera o rascunho
- **Ações:** Confirmar (cria o documento na etapa Rascunho do processo — U2) · Refinar no chat · Cancelar
- **Feedback:** toast "Documento criado — Contrato entrou na etapa Rascunho"

### 7.2 Overlay "Novo modelo" (criar modelo de documento/contrato)
- **Elemento:** `OverlayBuilderModelo`
- **Campos:**
  - Nome + tipo (Documento · Contrato · Relatório · Ata · Política · outro) + categoria + descrição
  - **Estrutura (seções)** — editor de seções (adicionar/renomear/reordenar; cada seção com descrição do que o agente deve preencher)
  - **Metadados** — campos que o modelo pede na geração (tipo, cliente, produto, período, valor, tags — lista editável)
  - **Exemplos** — adicionar exemplos (3 por tipo de modelo na criação — em aberto 3): colar texto de exemplo ou gerar; cada exemplo com nome + tipo + conteúdo
  - **Prompt associado** — o que o agente deve fazer (opcional; padrão derivado de tipo + seções)
- **Ações:** Salvar modelo (entra na aba Modelos) · Salvar e usar (gera documento em seguida) · Cancelar
- **Feedback:** toast "Modelo criado — Contrato de prestação de serviço"

### 7.3 Overlay "Adicionar exemplo"
- **Elemento:** `OverlayExemplo`
- **Campos:** nome do exemplo (ex.: "Exemplo 1 — Contrato de TI") · tipo · conteúdo (editor markdown; colar texto existente ou gerar com IA)
- **Ações:** Salvar · Gerar com IA · Cancelar
- **Feedback:** toast "Exemplo adicionado — o agente vai usar como referência"

### 7.4 Overlay "Rejeitar" (motivo)
- **Elemento:** `OverlayMotivo`
- **Ações:** motivo opcional + confirmar; rejeitar etapa volta o card uma etapa e registra no Histórico

### 7.5 Confirmações
- Arquivar/excluir documento · excluir modelo (com aviso: documentos gerados permanecem) · excluir rotina → confirmação (excluir em lote: confirmação dupla)

---

## 8. Biblioteca de elementos (novo conceito — para o design system)

> Elementos puros, sem herança do design atual. Nome + região + propósito; o desenho vem depois.

| Elemento | Região | Propósito |
|---|---|---|
| `NavegacaoAbas` | A | abas discretas sem faixa horizontal, com contador |
| `CampoBusca` | A | busca na sala por título **e metadados**, resultados agrupados |
| `Filtros` | A | restringir a visão ativa por atributos combináveis |
| `BotaoPrimario` | A | novo documento |
| `CabecalhoVisaoDocumentos` | B (Documentos) | título + subtítulo + filtros da fila |
| `FilaDocumentos` | B (Documentos) | fluxo de documentos ordenado por semáforo |
| `CartaoDocumento` | B (Documentos) | documento: tipo, status, semáforo, metadados, origem |
| `BarraAcoesLote` | B | publicar/mover/duplicar/arquivar em massa |
| `QuadroProcessos` | B (Processos) | kanban 4 etapas da geração de documentos |
| `ColunaEtapa` | B (Processos) | etapa com contador, cor, dropzone |
| `CartaoProcesso` | B (Processos) | documento em geração: etapa, modelo, semáforo, aprovador |
| `CabecalhoVisaoModelos` | B (Modelos) | título + filtros da biblioteca |
| `GradeModelos` | B (Modelos) | grade de modelos do sistema + próprios |
| `CartaoModelo` | B (Modelos) | modelo: tipo, origem, seções, metadados, exemplos |
| `TimelineDocumentos` | B (Histórico) | eventos de documentos/modelos com filtros |
| `CabecalhoVisaoRotinas` | B (Rotinas) | resumo de automações + nova rotina |
| `CatalogoRotinas` | B (Rotinas) | sugestões prontas da dimensão |
| `RotinaCard` | B (Rotinas) | rotina configurada com gatilho, status, última execução |
| `BuilderRotina` | B/E | criar/editar rotina por chat |
| `FeedExecucoes` | B (Rotinas) | execuções recentes com resultado |
| `PainelContextual` | C | contêiner do detalhe que troca de modo por aba + trilha |
| `TrilhaNavegacao` | C | breadcrumb da pilha |
| `PainelDocumento` | C (Documentos) | documento: metadados editáveis, seções, aprovações, corpo |
| `PainelProcesso` | C (Processos) | passo a passo das etapas + portas + modelo + artefatos |
| `PainelModelo` | C (Modelos) | modelo: estrutura, metadados, exemplos, prompt |
| `PainelEvento` | C (Histórico) | detalhe de evento + link para o item |
| `PainelRotina` | C (Rotinas) | configuração da rotina + status + ações |
| `PainelPreview` | C | corpo do documento/exemplo renderizado no painel |
| `EditorDocumento` | C/E | edição do corpo (markdown) em largura cheia quando o painel não basta |
| `InsightsSala` | D | sugestões proativas do agente |
| `MetricasSala` | D | métricas com comparações (MoM/YoY/média ano/6m) |
| `ModelosRapido` | D | modelos mais usados + atalho |
| `OverlayBuilderDocumento` | E | criar documento: escolher modelo ou chat |
| `OverlayBuilderModelo` | E | criar modelo: nome, tipo, seções, metadados, exemplos, prompt |
| `OverlayExemplo` | E | adicionar exemplo de documento ao modelo |
| `OverlayMotivo` | E | motivo de rejeição |

---

## 9. Regras de negócio de UI (resumo)

| # | Regra |
|---|---|
| U1 | Aba padrão = Documentos; última aba persiste por sessão |
| U2 | **Todo documento criado vira um processo de geração** — nasce na etapa Rascunho (fluxo dentro da sala) |
| U3 | Colunas do QuadroProcessos são as 4 etapas base (Rascunho → Revisão → Aprovação → Publicado) — ajustes por tipo de documento depois (ex.: contrato com assinatura — em aberto 4) |
| U4 | Pular etapa do processo exige confirmação |
| U5 | Painel direito é contextual: Documento (Documentos) · Processo (Processos) · Modelo (Modelos) · Evento (Histórico) · Rotina (Rotinas) · Preview (qualquer) |
| U6 | Clicar item de outra aba substitui o modo; navegar para dentro empilha na trilha; X/Esc limpa |
| U7 | **Todo documento tem metadados** (tipo, modelo, cliente, produto, período, valor, tags) — definidos na criação/edição; busca cobre título + metadados |
| U8 | **Modelo define estrutura (seções) + metadados + prompt; exemplos ensinam o agente a gerar o corpo** — sem exemplos, o modelo avisa e o agente gera do prompt |
| U9 | Modelos são reutilizáveis — um modelo gera N documentos; modelo editado **não altera** documentos já gerados (versionamento de modelo — R6 antiga) |
| U10 | Modelos podem ser marcados como **padrão** para o chat sugerir automaticamente (R4 antiga) |
| U11 | Publicar documento formal/canônico exige aprovação (porta); rejeitar volta uma etapa com motivo registrado |
| U12 | Sem permissão de aprovar/mover/criar/publicar → botões desabilitados com dica (permissões por sala no Admin — D3 Financeiro) |
| U13 | Ações em lote só com 2+ selecionados; excluir em lote exige confirmação dupla |
| U14 | Pendência aparece com contador na aba Documentos/Processos e na Home |
| U15 | Toda ação relevante (criar, editar, aprovar, rejeitar, publicar, arquivar, executar rotina, usar modelo) registra no Histórico |
| U16 | **Nunca há strip de métricas** no topo — métricas ficam no quadrinho D (Q2) |
| U17 | Sem dados fabricados: nenhum exemplo/conteúdo de documento inventado como dado real |
| U18 | Rotinas reusam a Rotina API existente; gatilhos manual/schedule/event/numeric/cron; trigger `document_created` existe (event) |
| U19 | "Rodar agora" dispara imediatamente e registra no feed + Histórico |
| U20 | Erro/parcial na execução de rotina vira alerta visual no card e entra na Home |
| U21 | "Dispensar" em insight é permanente; só volta se nascer de novo |
| U22 | Preview do corpo do documento acontece dentro do painel (Modo Preview); editor de largura cheia só quando o usuário pedir "Abrir documento completo" |
| U23 | Comparações por métrica — cada métrica declara quais pills se aplicam (D6 Financeiro) |

---

## 10. Cenários de teste (UI)

### Documentos (fila do fluxo)
- [ ] Fila ordena 🔴 → 🟡 → 🟢; badge da aba bate com o total
- [ ] Criar documento → nasce na etapa Rascunho + aparece na fila e no quadro de Processos
- [ ] Buscar "contrato" → acha por título E por metadado (tipo=Contrato, cliente)
- [ ] Publicar documento → toast + some do quadro + contador aba/Home atualizam
- [ ] Arquivar → some da fila + aparece no Histórico com opção de restaurar
- [ ] Selecionar 3 → barra de lote → Publicar selecionados → toast com contagem
- [ ] Sem permissão de publicar → botões disabled com dica
- [ ] Nenhum documento → estado vazio com CTA "Novo documento"

### Processos
- [ ] Novo documento via chat ("contrato de prestação de serviço para o Cliente X") → agente sugere modelo → gera rascunho na etapa Rascunho
- [ ] Card move Rascunho → Revisão → Aprovação (com permissão) → badge "Aguardando aprovação"
- [ ] Aprovar → documento publicado + registra no Histórico
- [ ] Rejeitar → motivo → card volta uma etapa
- [ ] Pular etapa (Rascunho → Publicado) → confirmação exigida
- [ ] Sem permissão de mover/aprovar → drag desabilitado + botões disabled
- [ ] Processo atrasado → semáforo 🔴 + entra na Home
- [ ] Agente propõe no Q1 ("fechamento na hora") → "Gerar documento" cria processo na Rascunho

### Modelos
- [ ] Criar modelo de contrato → aparece na aba Modelos; sem exemplos mostra aviso
- [ ] Adicionar 3 exemplos → contador atualiza; badge "Sem exemplos" some
- [ ] Usar modelo → overlay de documento abre com o modelo selecionado → gera rascunho com estrutura do modelo
- [ ] Buscar modelo por tipo/categoria → resultados filtram
- [ ] Editar modelo (seções/metadados/prompt) → documentos já gerados NÃO mudam (U9)
- [ ] Marcar como padrão → chat sugere o modelo automaticamente na próxima "cria um contrato"
- [ ] Duplicar modelo → cópia independente com "Próprio"
- [ ] Excluir modelo → confirmação + aviso "documentos gerados permanecem"

### Histórico
- [ ] Eventos por tipo com filtros (período · evento · agente · documento)
- [ ] Rejeição mostra motivo; clique no evento abre o item no painel

### Rotinas
- [ ] Adicionar do catálogo → entra na lista ativa; "Rodar agora" → feed + Histórico + toast
- [ ] Rotina de geração (ex.: fechamento mensal) dispara → documento nasce na etapa Rascunho
- [ ] Trigger `document_created` → rotina reagindo ao evento funciona
- [ ] Pausar mantém config; retomar volta; erro na execução → alerta no card + Home

### Painel contextual
- [ ] Aba Documentos → clique → Modo Documento; trocar para Modelos e clicar modelo → Modo Modelo **substitui**
- [ ] Trilha: Contrato › Modelo › Preview — voltar desempilha; breadcrumb só com 2+
- [ ] Modo Preview: ver corpo do documento no painel com Baixar/Editar; sem template → estado "sem preview"
- [ ] "Ver no fluxo" em Documento/Processo → aba certa + item aberto

### Quadrinhos
- [ ] Q2 mostra período 30d/90d/1y; cada métrica só com as comparações que fazem sentido
- [ ] Q1 insight "Gerar documento" → cria processo na Rascunho
- [ ] Q3 modelos mais usados → clique abre overlay de documento com o modelo selecionado
- [ ] Nenhum valor fabricado (U17)

---

## 11. Decisões

### Tomadas (padrão estabelecido — 12/08)
| # | Decisão |
|---|---|
| D1 | Sala **Documentos é fluxo + processos + modelos** (não é só um kanban): fila de documentos com status/metadados (fluxo) + missões de geração em etapas com portas de aprovação (processos) + biblioteca de modelos com exemplos (base) |
| D2 | **Etapas base:** Rascunho → Revisão → Aprovação → Publicado; ajustes por tipo de documento depois |
| D3 | **Quem move o card = quem tem autorização** — permissões por sala configuradas no Admin (owner): quem cria, quem edita, quem aprova, quem publica, quem arquiva (herança D3 Financeiro) |
| D4 | **Todo documento tem metadados** (tipo, modelo, cliente, produto, período, valor, tags) — busca cobre título + metadados; na hora de fazer um tipo de documento, o acesso ao **corpo** é via modelo |
| D5 | **Modelos com exemplos** — criar modelo de documento/contrato; alimentar com exemplos (ex.: 3 por tipo) que o agente usa como referência para gerar o corpo; modelos de sistema + próprios |
| D6 | **Comparações só quando fazem sentido por métrica** (herança D6 Financeiro) |
| D7 | Painel contextual com modos por aba + trilha (herança Clientes/Financeiro) |
| D8 | Quadrinhos no plano (Q1 insights · Q2 métricas+comparações · Q3 modelos rápido); sem strip de métricas (herança 12/08) |

### Em aberto
1. **Abas:** Documentos · Processos · Modelos · Histórico · Rotinas (proposta) vs outra combinação? (ex.: separar "Modelos" numa visão de aba própria é o que sustenta a biblioteca de exemplos — confirma?)
2. **"Criar em branco":** manter como opção no overlay (rascunho livre sem modelo) ou todo documento nasce de modelo? (R1 antiga dizia "só a partir de modelo"; o código atual tem "criar em branco")
3. **Exemplos por modelo:** 3 por tipo fixo (como você disse) ou quantidade livre? O agente pode gerar o exemplo (com dados de exemplo, não reais — U17)?
4. **Etapa de assinatura:** contrato tem etapa de assinatura (eletrônica) no v1 ou só Publicado? (kanbans.md propôs Assinatura)
5. **Metadados padrão:** quais campos todo modelo/documento deve ter de cara? (proposta: tipo · modelo · cliente · produto · período · valor · tags — a definir a lista mínima)
6. **Modelos do sistema:** manter os 8 embutidos atuais (Fechamento Mensal, Fluxo de Caixa, Proposta Comercial, Plano Estratégico, OKR, Ata de Reunião, SWOT, Invoice) como modelo de sistema — e os modelos de contrato precisam nascer como sistema ou só próprios?
7. **Painel sem seleção:** estado vazio "Selecione um item" (padrão Clientes) vs recolhido?
8. **Quem cria modelo:** dono ou qualquer usuário com permissão na sala? (permissões por sala no Admin)
