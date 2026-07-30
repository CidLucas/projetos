# 🧩 Elementos de UI — Context-MCP (catálogo visual)

> Extraído do código em `CidLucas/mcp_brain_lite` → `Context-MCP.dc.html`
> Aqui só tem **o que existe**. Sem opinião. Você comenta o que espera de cada um.

---

## 🖼️ Shell (Layout Global)

| Elemento | Tipo | Onde | Descrição no código |
|---|---|---|---|
| Topbar | barra fixa | topo (68px) | Logo 🧠 + "Context-MCP" + subtítulo "Memória corporativa" |
| Nav tabs | tabs centrais | topbar | 2 tabs: 📤 "Ingestão de documentos" + 🔀 "Consolidação de memória" |
| Badge de pendências | badge numérico | tab Consolidação | contador de conflitos pendentes (fundo laranja `var(--att)`) |
| Botão tema | btn circular | canto direito | ☀️/🌙 toggle dark/light mode |
| Área principal | container flex | abaixo do topbar | `flex:1; overflow:hidden` — troca entre as 2 telas |

---

## 📤 TELA 1 — Ingestão de Documentos

| Elemento | Tipo | Detalhes |
|---|---|---|
| **Drop zone** | área drag & drop | borda dashed 2px, hover roxo, ícone ☁️ + "Arraste arquivos aqui" |
| Formatos aceitos | texto guia | PDF · DOCX · CSV · XLSX · TXT · MD |
| Botão "Selecionar arquivos" | btn primário + input file | label estilizado, roxo com ícone 📂, input hidden |
| **Painel Metadados** | card lateral | coluna 310px à direita da drop zone |
| ↳ Título | label | "Metadados opcionais" (uppercase) |
| ↳ Campos key=value | pares input | chave + "=" + valor, dinâmicos, botão × remove |
| ↳ Botão "+ Adicionar campo" | btn texto | roxo, ícone ➕ |
| ↳ Botão "Enviar documentos" | btn primário | roxo full-width, 📨 ícone, estado loading com spinner |
| **Lista de Documentos** | tabela/cards | container com borda, header "Documentos · N" |
| ↳ Header | barra | 📄 ícone + contador + "Atualizado agora" |
| **Document Card** | card por doc | padding 14px, grid com ícone de tipo + info + ações |
| ↳ Ícone de tipo | badge colorido | PDF=🔴, XLSX/CSV=🟢, DOCX=🔵, outros=cinza (38px, fundo translúcido) |
| ↳ Nome do arquivo | texto bold | truncado com ellipsis (max 340px) |
| ↳ Status badge | pill | Concluído=verde, Processando=roxo, Erro=vermelho |
| ↳ Metadata row | linha | tamanho formatado (B/KB/MB), data (dd/mm/aaaa), chunks, fatos extraídos |
| ↳ Pipeline stages | pills horizontais | Parse → Embed → Extract → Grafo → Concluído (cada pill colorida por estado) |
| ↳ Pill done | pill verde | ✓ concluído |
| ↳ Pill active | pill roxa | spinner no stage atual |
| ↳ Pill error | pill vermelha | ✗ no stage com erro |
| ↳ Pill pending | pill cinza | ○ aguardando |
| ↳ Error message | alerta | fundo vermelho claro, ícone ⚠️, texto do erro |
| ↳ Warning message | alerta | fundo laranja claro, ícone ⚠️, texto de aviso |
| **Ações por documento** | 3 botões | 👁 Ver detalhes, 🔄 Reprocessar, 🗑 Excluir |
| ↳ Ver detalhes | btn ghost | abre modal de detalhes |
| ↳ Reprocessar | btn ghost | reseta pipeline, animação 3s de mock |
| ↳ Excluir | btn ghost vermelho | remove doc da lista |
| **Empty state** | placeholder | ícone 📄 grande opaco 50%, texto "Nenhum documento enviado ainda." + dica |
| **Toast** | notificação | canto inferior direito, verde, ✓ + mensagem, auto-dismiss 3.2s |

---

## 🔀 TELA 2 — Consolidação de Memória

| Elemento | Tipo | Detalhes |
|---|---|---|
| **Stats bar** | 3 cards lado a lado | Pendentes (laranja), Resolvidos hoje (verde), Total (cinza) |
| ↳ Card Pendentes | card | número grande laranja + label "Pendentes" |
| ↳ Card Resolvidos hoje | card | número grande verde + label "Resolvidos hoje" |
| ↳ Card Total | card | número grande cinza + label "Total" |
| **Filtros** | barra de busca + 2 dropdowns | alinhados à direita |
| ↳ Busca textual | input com ícone 🔍 | filtra por subject + entity + predicate + valores |
| ↳ Filtro Entidade | select | "Todas as entidades", Pessoa, Empresa, Contrato |
| ↳ Filtro Predicado | select | "Todos os predicados", Salário mensal, Capital social, Prazo de vigência, CNPJ, Endereço sede |
| **Conflict Card** | card expansível | borda esquerda colorida: laranja=pendente, verde=resolvido |
| ↳ Card header | barra | badge entidade (Pessoa/Empresa/Contrato) + subject + → + predicado (itálico roxo) |
| ↳ Detectado em | texto | data relativa "Detectado dd/mm/aaaa" |
| ↳ Status badge | pill | Pendente=laranja, Resolvido=verde |
| ↳ Botão "Contexto" | btn ghost | abre painel lateral com timeline da entidade |
| **Comparação lado a lado** | grid 2 colunas | Vigente (esquerda) vs Entrante (direita) |
| ↳ Coluna Vigente | painel | ícone 🕐, valor grande (23px bold), fonte, confiança %, valid_from/to |
| ↳ Coluna Entrante | painel fundo roxo claro | ícone 📈, badge delta (+R$ X ou +Y%), valor, fonte, confiança %, valid_from/to |
| **Barra de ações (pendente)** | barra inferior | fundo escurecido, label "Resolução:" |
| ↳ "Manter o novo" | btn primário roxo | ✓ encerra vigência do antigo, define novo como vigente |
| ↳ "Manter o antigo" | btn outline | ✗ rejeita entrante, mantém vigente |
| ↳ "Manter ambos" | btn outline | 📋 abre painel de janelas de validade |
| ↳ "Editar" | btn outline | ✏️ abre formulário de edição do entrante |
| **Painel "Manter ambos"** | expansão inline | fundo roxo claro, formulário de datas |
| ↳ Grid de datas | 2×2 inputs date | Vigente: De/Até + Entrante: De/Até |
| ↳ "Confirmar coexistência" | btn primário roxo | ✓ define janelas e resolve |
| ↳ "Cancelar" | btn outline | volta à barra de ações |
| ↳ Hint | texto | ℹ️ "Ambos coexistem nas janelas definidas." |
| **Painel "Editar"** | expansão inline | fundo azul claro, formulário editável |
| ↳ Campos editáveis | inputs | Valor, Unidade, Confiança (0–1), Válido desde, Válido até |
| ↳ "Confirmar edição" | btn primário azul | ✓ salva edição e resolve |
| ↳ "Cancelar" | btn outline | volta à barra de ações |
| **Estado resolvido** | barra inferior verde | ✓ "Resolvido:" + label da resolução + timestamp |
| **Painel de Entidade** | sidebar 280px | lado direito, timeline vertical |
| ↳ Header | barra | nome da entidade (15px bold) + tipo + botão ✕ fechar |
| ↳ Timeline | lista vertical | linha do tempo com dots roxos conectados por linha cinza |
| ↳ Fact na timeline | card pequeno | predicado (uppercase), valor (roxo bold), período (from→to mono), 📄 fonte |
| **Empty state (filtros)** | placeholder | ✓ verde "Nenhum conflito encontrado com esses filtros." |

---

## 🪟 Modal de Detalhes do Documento

| Elemento | Tipo | Detalhes |
|---|---|---|
| Overlay | backdrop | fundo preto 55% + blur 5px |
| Container | card central | 540px largura, max 80vh, scroll interno |
| Header | barra | "Detalhes do documento" (bold) + botão ✕ |
| Grid de informações | grid 2 colunas | Nome, Status, Tipo, Tamanho, Data, Chunks (verde grande), Fatos (roxo grande) |
| Metadados JSON | pre formatado | fundo glass, fonte mono, JSON pretty-print |
| Fechar | ✕ ou clique fora | fecha o modal |

---

## 🔔 Toast (notificações)

| Elemento | Tipo | Detalhes |
|---|---|---|
| Container | fixed | canto inferior direito, z-index 300 |
| Mensagem | card verde | ✓ ícone + texto, auto-dismiss 3.2s, animação fade-in |
