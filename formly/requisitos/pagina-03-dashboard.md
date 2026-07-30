# 📊 Página 03 — Dashboard de Resultados

> **Status:** ⚠️ Aspiracional — sem código ainda. Baseado no Google Doc + input do Lucas (2026-07-30)
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Tela onde o criador do questionário **visualiza as respostas agregadas**. Oferece cards de resumo, gráficos por pergunta, filtros por período, e exportação.

### Layout

```
┌──────────────────────────────────────────────────────────────┐
│  ← Voltar   |   Resultados: Satisfação Clínica               │
│             |   [7 dias ▾] [Filtrar] [📥 Exportar ▾]         │
├──────────────────────────────────────────────────────────────┤
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │ 243      │ │ 87%      │ │ 12       │ │ 4.2/5    │        │
│  │ Respostas│ │ Taxa de  │ │ Áudios   │ │ Satisfação│        │
│  │          │ │ conclusão│ │ gravados │ │ média     │        │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────────────────────┐ ┌──────────────────────┐│
│  │ 1. Como avalia o atendimento?  │ │ 2. Tempo de espera?  ││
│  │                                 │ │                      ││
│  │ ████████████░░░░ 65% Ótimo     │ │ ████████░░░░ 52% Sim ││
│  │ ██████░░░░░░░░░ 25% Bom        │ │ ██████░░░░░░ 35% Não ││
│  │ ██░░░░░░░░░░░░░ 8% Regular     │ │ ██░░░░░░░░░░ 13% Melh││
│  │ █░░░░░░░░░░░░░░ 2% Ruim        │ │                      ││
│  └─────────────────────────────────┘ └──────────────────────┘│
│                                                              │
│  ┌──────────────────────────────────────────────────────────┐│
│  │ 3. Depoimento em áudio (12 respostas)                    ││
│  │ ┌──────────────────────────────────────────────────────┐ ││
│  │ │ "Fui muito bem atendido..." — 15/07  [▶️ ouvir]     │ ││
│  │ │ "A recepcionista foi ótima..." — 15/07  [▶️ ouvir]  │ ││
│  │ │ "Demorou um pouco mas..."    — 14/07  [▶️ ouvir]    │ ││
│  │ └──────────────────────────────────────────────────────┘ ││
│  └──────────────────────────────────────────────────────────┘│
│                                                              │
│  ┌──────────────────────────────────────────────────────────┐│
│  │ 📥 Exportar                                              ││
│  │ [CSV] [PDF]                                              ││
│  └──────────────────────────────────────────────────────────┘│
└──────────────────────────────────────────────────────────────┘
```

---

## 2. Estrutura de Elementos

### 2.1 Header do Dashboard

| Elemento | Tipo | Descrição |
|---|---|---|
| Breadcrumb | link | "← Meus questionários" |
| Título | heading | nome do questionário |
| Status | badge | "Ativo" (verde), "Pausado" (amarelo), "Encerrado" (cinza) |
| Link público | cópia rápida | URL + botão copiar |
| Período | dropdown | "7 dias", "30 dias", "90 dias", "Tudo" |
| Exportar | dropdown btn | CSV, PDF |

### 2.2 Cards de Resumo (KPI)

- **Tipo:** 4 cards lado a lado
- **Posição:** topo, abaixo do header
- **Conteúdo/Dados:**

| Card | Métrica | Cálculo |
|---|---|---|
| Respostas | número total | count(responses) |
| Taxa de conclusão | % | completas / iniciadas × 100 |
| Áudios gravados | número | count(responses com áudio) |
| Nota média | X/Y | média da pergunta de escala (se houver) |

- **Interações:** clique no card → filtra ou expande detalhes
- **Estados visuais:** cards brancos com sombra sutil, número grande + label pequeno

### 2.3 Gráficos por Pergunta

Para cada pergunta do questionário, um card com visualização adequada ao tipo:

| Tipo de pergunta | Visualização |
|---|---|
| Múltipla escolha | **Barra horizontal** — barras coloridas com % e contagem |
| Texto curto | **Lista de respostas** — scroll com as respostas mais recentes |
| Texto longo | **Lista de respostas** — truncada com "Ver mais", expandível |
| Áudio | **Lista de cards** — transcrição + player de áudio |

#### Card de pergunta (múltipla escolha)

```
┌──────────────────────────────────────────┐
│ 1. Como avalia o atendimento?            │
│                                          │
│ Ótimo     ████████████████ 65%  (158)   │
│ Bom       ██████░░░░░░░░░░░ 25%  (61)   │
│ Regular   ██░░░░░░░░░░░░░░░ 8%   (19)   │
│ Ruim      █░░░░░░░░░░░░░░░░ 2%   (5)    │
│                                          │
│ Total: 243 respostas                     │
└──────────────────────────────────────────┘
```

#### Card de pergunta (áudio)

```
┌──────────────────────────────────────────┐
│ 3. Deixe um depoimento em áudio   (12)   │
│                                          │
│ ┌──────────────────────────────────────┐ │
│ │ "Fui muito bem atendido pela equipe" │ │
│ │ 15/07/2026 — 0:32  [▶️ ouvir]      │ │
│ └──────────────────────────────────────┘ │
│ ┌──────────────────────────────────────┐ │
│ │ "A recepcionista foi ótima..."       │ │
│ │ 15/07/2026 — 0:18  [▶️ ouvir]      │ │
│ └──────────────────────────────────────┘ │
│ ...                                      │
│                          [Ver todos →]   │
└──────────────────────────────────────────┘
```

### 2.4 Player de Áudio (inline)

| Elemento | Tipo | Descrição |
|---|---|---|
| Botão Play/Pause | ▶️/⏸️ | mini player inline |
| Timeline | barra de progresso | arrastável |
| Duração | texto | "0:32" |
| Transcrição | texto | abaixo do player, colapsável |

### 2.5 Exportação

| Elemento | Tipo | Descrição |
|---|---|---|
| Botão CSV | btn | download de todas as respostas em CSV |
| Botão PDF | btn | gera relatório resumido em PDF |
| Loading | spinner | "Gerando arquivo..." durante processamento |
| Sucesso | toast | "Download iniciado" |

---

## 3. Fluxos de Processo

### 3.1 Visualizar resultados

```
1. Criador clica em "Ver resultados" na lista de questionários
   → Dashboard carrega com período padrão "7 dias"

2. Vê cards de resumo no topo
   → 243 respostas, 87% conclusão, 12 áudios, 4.2/5

3. Scrolla para ver gráficos por pergunta
   → Cada pergunta tem seu card com visualização adequada

4. Clica no player de áudio ▶️
   → Áudio toca inline, transcrição visível abaixo

5. Altera período para "30 dias"
   → Todos os dados recalculam para o novo período
```

### 3.2 Exportar dados

```
1. Criador clica "📥 Exportar" → escolhe "CSV"
   → Spinner: "Gerando CSV..."
   → Download inicia automaticamente
   → Toast: "Download iniciado — 243 linhas"

2. Criador clica "PDF"
   → Spinner: "Gerando relatório..."
   → PDF com gráficos e resumo é baixado
```

### 3.3 Filtrar respostas

```
1. Criador clica "Filtrar"
   → Painel lateral ou modal abre com opções:
     - Data (de/até)
     - Status (completa/incompleta)
     - Tem áudio? (sim/não)

2. Aplica filtros
   → Dados recalculam
   → Badge "Filtros ativos: 2" aparece
   → Botão "Limpar filtros" disponível
```

---

## 4. Regras de Negócio

### Métricas

| Métrica | Fórmula | Atualização |
|---|---|---|
| Total de respostas | `count(responses)` | near real-time |
| Taxa de conclusão | `count(complete) / count(started) × 100` | near real-time |
| Áudios gravados | `count(responses where question.type == 'audio')` | near real-time |
| Nota média | `avg(value) where question.type == 'scale'` | near real-time |

### Período

- **Default:** 7 dias
- **Opções:** 7, 30, 90 dias, Todo o período
- **Filtro customizado:** datas livre (de/até)

### Gráficos

- **Múltipla escolha:** sempre mostrar % e contagem absoluta
- **Ordenação:** por contagem (maior → menor)
- **Cores:** paleta consistente por opção (ex: Ótimo=verde, Ruim=vermelho)
- **Sem respostas:** empty state "Nenhuma resposta ainda. Compartilhe o link para começar!"

### Áudios

- **Lista ordenada por:** data (mais recente primeiro)
- **Limite inicial:** 5 exibidos, "Ver todos" para expandir
- **Player:** não faz autoplay — sempre requer clique do usuário

### Exportação

- **CSV:** uma linha por resposta, colunas = perguntas, encoding UTF-8 BOM (compatível Excel)
- **PDF:** capa + cards de resumo + gráficos + tabela de respostas textuais
- **Limite:** máximo 10.000 linhas no PDF (oferecer CSV para volumes maiores)

### Privacidade

- **Dados individuais:** visíveis apenas para o criador (autenticado)
- **Dados agregados:** podem ser compartilhados (link de resultados públicos — futuro)
- **Áudios:** accesso restrito via URL assinada (expira em 24h)

---

## 5. Integrações

| Integração | Descrição | Status |
|---|---|---|
| **Backend Formly** | GET /api/questionnaires/:id/responses | 🔴 não implementado |
| **S3 / Blob** | URLs assinadas para download de áudio | 🔴 não implementado |
| **Gerador de PDF** | Puppeteer ou similar para relatório | 🔴 não implementado |

---

## 6. Cenários de Teste

### Visualização
- [ ] Dashboard carrega com período "7 dias"
- [ ] Cards de resumo mostram métricas corretas
- [ ] Gráfico de múltipla escolha: barras coloridas com % e contagem
- [ ] Lista de áudios: cards com transcrição + player funcional
- [ ] Mudar período → dados recalculam
- [ ] Questionário sem respostas → empty states em todos os cards

### Áudio
- [ ] Clicar ▶️ no card de áudio → áudio toca
- [ ] Player mostra duração e timeline interativa
- [ ] Transcrição visível e correta
- [ ] "Ver todos" expande lista de áudios

### Exportação
- [ ] Exportar CSV → arquivo baixado com encoding correto (acentos funcionam)
- [ ] CSV contém todas as perguntas como colunas
- [ ] Exportar PDF → relatório com capa + gráficos + respostas
- [ ] Spinner durante geração

### Filtros
- [ ] Filtrar por data → dados recalculam
- [ ] Filtrar por status "completa" → só mostra respostas finalizadas
- [ ] Limpar filtros → volta ao estado padrão
