# Prompt — Agente de Design · Blue V3 (BlueClient) — Painel direito contextual + Follow-up 2 dimensões + barras

> Fonte: `~/projetos-repo/plataforma-blu/requisitos/clientes.md` (canônico) · Google Doc: https://docs.google.com/document/d/1w8GRPBgLWPiraxPIhq9WetRJehmohWGK9AIL5RHf8X8/edit
> Decisões 13/08: D14–D18 · Regras U23–U31.

---

## Contexto

Você vai atualizar o design da tela **Clientes (Blue V3)**. São **duas mudanças de spec** + **um ajuste visual global**. Leia o requisito completo em `requisitos/clientes.md` antes de começar; abaixo está o resumo executável do que precisa mudar no design.

Princípios que valem para tudo: elementos puros (informação + ação), abas discretas **sem faixa horizontal**, stack padrão Vite + React 18 + Blu DS (CSS tokens), **sem libs externas de UI** (Radix/shadcn), painel direito **fixo ~380px**.

---

## 1) Painel direito contextual (Região C)

O painel lateral direito **não é mais só o detalhe do card do kanban**. Ele é a "lupa da sala": muda de **modo** conforme a aba ativa e o item selecionado.

**Modos (um por aba):**
- **Kanban → Modo Cliente:** gestão completa do cliente (conversa com status de envio Rascunho → Aguardando aprovação → Enviada, campo de resposta com "Gerar resposta (IA)", aprovação inline, informações do cliente, etapa atual + mover, artefatos com gerar/visualizar, atalhos de canal WhatsApp/e-mail/direto, interlocutores).
- **Follow-up → Modo Pendência:** pendência em foco — motivo legível, nível/semáforo, valor potencial em jogo, ação sugerida pelo agente, ações Concluir / Adiar (1/3/7 dias) / Dispensar / Aprovar (só aprovador), botão "Ver conversa" (empilha o Modo Cliente do mesmo cliente).
- **Histórico → Modo Perfil:** relatório do cliente dentro do painel — identidade, artefatos por tipo com visualizar/baixar, linha do tempo **só do cliente**, exportar relatório (PDF). (Não é overlay: vive no painel.)
- **Rotinas → Modo Rotina:** configuração da rotina no painel — gatilho/frequência legível ("Toda segunda às 8h"), ação, filtro (quais clientes), canal, status ativa/pausada, última execução + resultado; ações: editar campos direto (salva na hora), "Editar com IA" (abre o builder chat preenchido), Rodar agora, Pausar/Retomar, Ver execuções, Excluir.
- **Qualquer aba → Modo Preview:** preview de documento/contrato/NF **dentro do painel** (Baixar PDF, Enviar, Assinar, Voltar). **Não usar overlay para preview de artefato.**

**Navegação interna do painel:**
- **Trilha/breadcrumb** quando o usuário navega para dentro de um item (ex.: `Cliente › Artefato › Preview`); voltar desempilha um nível; X fecha e limpa.
- Clicar item de outra aba **substitui** o modo (não acumula).
- **"Abrir no kanban"** disponível em qualquer modo (exceto o próprio Cliente) — leva o item ao kanban em Modo Cliente.
- Estados: aberto / fechado (X) / loading / erro / vazio ("Selecione um item para ver o detalhe").

**Elementos de biblioteca:** `PainelContextual`, `TrilhaNavegacao`, `CabecalhoPainel` (contextual), `PainelPendencia`, `AcaoSugeridaPendencia`, `PainelPerfilCliente`, `PainelRotina`, `UltimaExecucaoRotina`, `PainelPreview`.

---

## 2) Aba Follow-up em duas dimensões (threads → casos)

A aba Follow-up **não é mais uma lista granulada de pendências**. Ela tem duas dimensões:

**1ª dimensão — THREADS (visão padrão ao entrar):**
- Pendências **agrupadas por tipo de situação** (ex.: 5 threads: "Parados há 5+ dias", "Orçamentos sem resposta", "Recorrências atrasadas", "Aprovações", "Mensagens em revisão").
- Cada thread (`ThreadFollowUpCard`) mostra: nome, **contador de casos**, **status da thread** (ex.: "3 em revisão" / "2 em acompanhamento"), semáforo 🟢🟡🔴, **valor potencial somado** (R$) e **ação sugerida do thread** (ex.: "Relembrar 3 orçamentos", "Aprovar 2 mensagens").
- Ações da thread: **Ver casos** (2ª dimensão) · **Aplicar ação sugerida** (dispara para os casos) · **Dispensar thread** (permanente).
- Thread sem casos some da lista.

**2ª dimensão — DETALHE DA THREAD:**
- Ao clicar na thread, mostra os **casos específicos** daquela situação em **cards de síntese** (`CartaoCasoFollowUp`): cliente (avatar) + coluna atual, motivo legível ("Parado há 5 dias", "Orçamento #123 sem resposta há 3 dias"), nível/semáforo + tempo relativo, valor potencial, ação sugerida pelo agente.
- Opções por caso: Concluir · Adiar (1/3/7 dias) · Ver no kanban · Aprovar (só aprovador) · Gerar rascunho · Dispensar (permanente).
- Botão **"Voltar às threads"** retorna à 1ª dimensão. Clique no caso → painel direito em **Modo Pendência**.
- Filtros do cabeçalho seguem aplicados nas duas dimensões.

**Contadores e lote:**
- Badge da aba Follow-up = **soma dos casos** das threads; resolver caso (concluir/adiar) atualiza contador da thread, da aba e da Home; thread zera → some.
- Barra de ações em lote: na 2ª dimensão atua nos **casos da thread ativa** (Concluir/Adiar/Aprovar/Aplicar ação sugerida); na 1ª dimensão atua nas **threads selecionadas**.

**Elementos de biblioteca:** `ListaThreadsFollowUp`, `ThreadFollowUpCard`, `DetalheThreadFollowUp`, `CartaoCasoFollowUp`, `BarraAcoesLoteFollowUp`.

---

## 3) Ajuste visual global — barras

- A **topbar** e as **barras de navegação** (topo e navegação) estão com um **sombreado feio, meio esfumacado** (gradiente/blur/sombra suja).
- **Corrigir para cores sólidas e com contraste:** fundo sólido da barra (sem translucidez, sem blur/glassmorphism, sem sombra esfumada), separação nítida entre a barra e o conteúdo (borda/linha de 1px ou contraste claro), e contraste adequado entre superfícies (fundo da barra ≠ fundo do conteúdo; texto legível — AA).
- Aplicar em toda a tela Clientes e, se estiver no mesmo padrão, no shell (topbar/sidebar) — consistência.

---

## Critérios de aceite

- [ ] Painel direito com os 5 modos (Cliente/Pendência/Perfil/Rotina/Preview) trocando conforme a aba e o item selecionado
- [ ] Trilha/breadcrumb ao navegar para dentro; voltar desempilha; X fecha e limpa; "Abrir no kanban" em qualquer modo
- [ ] Preview de documento/contrato **dentro do painel** (sem overlay de artefato)
- [ ] Follow-up com 1ª dimensão (threads com contador/status/ação sugerida) e 2ª dimensão (casos em cards de síntese) navegáveis
- [ ] Contadores sincronizados (thread → aba → Home); thread sem casos some
- [ ] Barras (topo e navegação) com **cores sólidas e contraste**, sem sombreado esfumado
- [ ] Abas discretas sem faixa horizontal; stack padrão; sem libs externas de UI
