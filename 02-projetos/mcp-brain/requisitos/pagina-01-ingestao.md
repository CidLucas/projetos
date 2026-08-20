# 📤 Página 01 — Ingestão de Documentos

> **Arquivo no código:** `Context-MCP.dc.html` → `showIngestion`
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Tela principal de entrada de documentos no MCP Brain Lite. O usuário faz upload de arquivos corporativos, adiciona metadados opcionais, e acompanha o pipeline de processamento (Parse → Embed → Extract → Grafo → Concluído).

### Layout

```
┌─────────────────────────────────────────────────────────┐
│  [Drop zone: arraste arquivos]    │ [Metadados opcionais]│
│  ☁️ Arraste arquivos aqui        │ chave = valor        │
│  PDF · DOCX · CSV · XLSX · TXT   │ + Adicionar campo    │
│  [📂 Selecionar arquivos]        │ [📨 Enviar documentos]│
├─────────────────────────────────────────────────────────┤
│  📄 Documentos · 3                   Atualizado agora    │
├─────────────────────────────────────────────────────────┤
│  🔴 Contrato_Silva_2024.pdf  Concluído                  │
│    245 KB · 15/01/2024 · 18 chunks · 12 fatos           │
│    [✓ Parse] → [✓ Embed] → [✓ Extract] → [✓ Grafo] → [✓ Concluído] │
│    [👁] [🔄] [🗑]                                        │
├─────────────────────────────────────────────────────────┤
│  🟢 Balancete_Q4_2024.xlsx  Processando                 │
│    85 KB · 20/01/2024 · 8 chunks · 4 fatos              │
│    [✓ Parse] → [◌ Embed] → [○ Extract] → [○ Grafo] → [○ Concluído] │
│    [👁] [🔄] [🗑]                                        │
├─────────────────────────────────────────────────────────┤
│  🔵 Proposta_Comercial_Fornec.docx  Erro                 │
│    1.5 MB · 21/01/2024 · 0 chunks · 0 fatos             │
│    [✓ Parse] → [✗ Embed] → [○ Extract] → [○ Grafo] → [○ Concluído] │
│    ⚠️ Falha ao gerar embeddings: excede limite de 100k tokens │
│    [👁] [🔄] [🗑]                                        │
└─────────────────────────────────────────────────────────┘
```

---

## 2. Estrutura de Elementos

### 2.1 Drop Zone

- **Tipo:** área drag & drop
- **Posição:** coluna esquerda (flex: 1) do grid superior
- **Conteúdo/Dados:** ícone ☁️ (44px, cinza), texto "Arraste arquivos aqui", formatos aceitos, botão "Selecionar arquivos"
- **Interações:**
  - `dragOver` → borda fica roxa (`var(--ac)`), fundo roxo claro (`var(--adim)`)
  - `dragLeave` → volta ao estado normal (borda cinza `var(--gb)`)
  - `drop` → borda volta ao normal, toast "Arquivo recebido"
  - Clique no botão → abre file picker nativo com filtro `accept=".pdf,.docx,.csv,.xlsx,.txt,.md"`
- **Estados visuais:**
  - Normal: borda dashed cinza, fundo glass
  - Hover (drag): borda dashed roxa, fundo roxo claro
- **Condições de visibilidade:** sempre visível na tab Ingestão

### 2.2 Botão "Selecionar arquivos"

- **Tipo:** label estilizado como botão primário
- **Posição:** dentro da drop zone, abaixo do texto de formatos
- **Conteúdo/Dados:** ícone 📂 + "Selecionar arquivos"
- **Interações:** clique → abre file picker do SO com filtro de extensões. O input file real está hidden.
- **Estados visuais:** normal (roxo com sombra), hover (mais escuro)
- **Condições de visibilidade:** sempre visível

### 2.3 Painel de Metadados

- **Tipo:** card lateral
- **Posição:** coluna direita (310px fixo) do grid superior
- **Conteúdo/Dados:**
  - Título "Metadados opcionais" (uppercase, 9.5px, cinza)
  - Lista dinâmica de pares key=value
  - Botão "+ Adicionar campo"
  - Botão "Enviar documentos"
- **Interações:**
  - Digitar key/value → atualiza estado local
  - Clicar × → remove aquele par key=value
  - "+ Adicionar campo" → adiciona linha vazia `{key: '', val: ''}`
  - "Enviar documentos" → simula upload (2s loading), gera doc fake com metadados preenchidos
- **Estados visuais:**
  - Normal: inputs com borda cinza
  - Uploading: botão com opacidade 0.7, cursor wait, spinner
- **Condições de visibilidade:** sempre visível na tab Ingestão

### 2.4 Lista de Documentos

- **Tipo:** tabela/cards em container com borda
- **Posição:** abaixo do grid superior, largura total (max 1100px)
- **Conteúdo/Dados:**
  - Header: 📄 ícone + "Documentos · N" + "Atualizado agora"
  - Cards individuais por documento
- **Estados visuais:**
  - Com documentos: lista normal
  - Vazio (empty state): ícone 📄 grande opaco 50%, "Nenhum documento enviado ainda." + dica

### 2.5 Document Card

Para cada documento na lista:

| Sub-elemento | Tipo | Detalhes |
|---|---|---|
| Ícone de tipo | badge 38×38px | cor por MIME: PDF=#EF4444, XLSX/CSV=#10B981, DOCX=#3B82F6 |
| Nome do arquivo | texto bold 13.5px | truncado com ellipsis (max 340px) |
| Status badge | pill | Concluído=verde, Processando=roxo, Erro=vermelho, Enviado=cinza |
| Tamanho | texto 11.5px | formatado: B / KB / MB |
| Data | texto 11.5px | dd/mm/aaaa |
| Chunks | texto (condicional) | "N chunks" quando > 0 |
| Fatos extraídos | texto verde (condicional) | "N fatos extraídos" quando > 0 |
| Pipeline stages | pills inline | 5 estágios: Parse → Embed → Extract → Grafo → Concluído |
| Error message | alerta inline | fundo vermelho, ⚠️ ícone, texto do erro |
| Warning message | alerta inline | fundo laranja, ⚠️ ícone, texto do warning |
| Botão Ver detalhes | btn ghost 👁 | abre modal |
| Botão Reprocessar | btn ghost 🔄 | reseta pipeline |
| Botão Excluir | btn ghost 🗑 | remove documento |

### 2.6 Pipeline Stages (pills)

Cada pill representa um estágio do processamento:

| Ícone | Estado | Estilo | Quando |
|---|---|---|---|
| ✓ check-circle | done | verde (`var(--ok)`), fundo verde claro | estágio concluído |
| ◌ circle-notch + animação spin | active | roxo (`var(--ac)`), fundo roxo claro | estágio em processamento |
| ✗ x-circle | error | vermelho (`var(--urg)`), fundo vermelho claro | estágio com falha |
| ○ circle | pending | cinza (`var(--mu)`), fundo glass | estágio aguardando |

Cálculo de estado por estágio:
- `doc.status === 'done'` → todos done
- `doc.status === 'processing'` → anteriores done, atual active, posteriores pending
- `doc.status === 'error'` → anteriores done, atual error, posteriores pending

### 2.7 Modal de Detalhes

- **Tipo:** modal com overlay
- **Posição:** centro da tela (fixed, z-index 200)
- **Conteúdo/Dados:** todos os campos do documento:
  - Nome do arquivo (grid 2 colunas, nome ocupa linha inteira)
  - Status (badge)
  - Tipo MIME
  - Tamanho (mono)
  - Data de envio (mono)
  - Chunks gerados (número grande verde)
  - Fatos extraídos (número grande roxo)
  - Metadados (JSON formatado em `<pre>`)
- **Interações:**
  - Clicar ✕ → fecha
  - Clicar fora (overlay) → fecha
  - `stopPropagation` no container interno evita fechar ao clicar dentro
- **Estados visuais:** animação fade-in (0.15s), backdrop blur 5px + preto 55%

### 2.8 Toast

- **Tipo:** notificação fixa
- **Posição:** canto inferior direito (fixed, z-index 300)
- **Conteúdo/Dados:** ✓ ícone + mensagem de texto
- **Interações:** auto-dismiss em 3.2 segundos
- **Estados visuais:** fundo verde (`var(--ok)`), animação fade-in 0.16s

---

## 3. Fluxos de Processo

### 3.1 Upload de documento

```
1. Usuário arrasta arquivo(s) na drop zone
   → borda fica roxa (feedback visual)
   → toast: "Arquivo recebido. Clique em 'Enviar documentos' para iniciar."
   
   OU

1. Usuário clica "Selecionar arquivos"
   → file picker nativo abre
   → usuário seleciona arquivo(s)
   → toast: "X arquivo(s) selecionado(s). Clique em 'Enviar documentos'."

2. Usuário opcionalmente adiciona metadados (key=value)

3. Usuário clica "Enviar documentos"
   → botão entra em loading (spinner + opacidade + cursor wait)
   → após 2s: documento aparece no topo da lista como "Processando" no estágio Parse
   → metadados são resetados para 1 campo vazio (departamento)
   → toast: "Documento enviado e em processamento."
```

### 3.2 Pipeline de processamento

```
1. Documento entra com status: 'processing', stage: 'parse'
   → pills: [active Parse] [pending Embed] [pending Extract] [pending Grafo] [pending Concluído]

2. (Mock) Após 3s no reprocessar, status muda para 'done'
   → pills: [done Parse] [done Embed] [done Extract] [done Grafo] [done Concluído]
   → chunks e fatos são preenchidos com valores aleatórios (6-25 chunks, 3-17 fatos)

3. Se erro: status fica 'error' no estágio onde falhou
   → erro message aparece abaixo dos pills
```

### 3.3 Reprocessar documento

```
1. Usuário clica 🔄 em um documento
   → status muda para 'processing', stage: 'parse'
   → chunks e fatos zeram
   → erro limpo
   → toast: "Documento enviado para reprocessamento."

2. Após 3s (mock):
   → status muda para 'done'
   → novos valores aleatórios de chunks/fatos
   → toast: "Reprocessamento concluído."
```

### 3.4 Excluir documento

```
1. Usuário clica 🗑 em um documento
   → documento é removido da lista (filter)
   → toast: "Documento excluído."
```

### 3.5 Visualizar detalhes

```
1. Usuário clica 👁 em um documento
   → modal overlay + card central com todos os campos
   → JSON de metadados formatado com 2 espaços

2. Usuário clica ✕ ou fora
   → modal fecha
```

---

## 4. Regras de Negócio

### Formatos aceitos

- PDF (application/pdf)
- DOCX (application/vnd.openxmlformats-officedocument.wordprocessingml.document)
- XLSX (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)
- CSV (text/csv)
- TXT (text/plain)
- MD (text/markdown)

### Limite de tokens

- Documentos > 100k tokens → erro no estágio Embed
- Mensagem: "Falha ao gerar embeddings: documento excede o limite de tokens (máx. 100k). Divida em partes menores e reenvie."

### Metadados

- Formato: pares key=value livres
- Pelo menos 1 campo sempre visível (inicia com `{key: 'departamento', val: ''}`)
- Campos com key vazia são ignorados no envio
- Após envio, metadados voltam ao estado inicial (1 campo departamento vazio)

### Ícones por tipo MIME

| MIME contém | Ícone Phosphor | Cor |
|---|---|---|
| `pdf` | `ph-file-pdf` | #EF4444 |
| `sheet` / `csv` / `excel` | `ph-file-xls` | #10B981 |
| `word` / `doc` | `ph-file-doc` | #3B82F6 |
| outros | `ph-file-text` | #94a3b8 |

### Estados do documento

| Status | Label | Badge |
|---|---|---|
| `uploaded` | Enviado | cinza |
| `processing` | Processando | roxo |
| `done` | Concluído | verde |
| `error` | Erro | vermelho |

---

## 5. Integrações

| Elemento | Integração | Status |
|---|---|---|
| Upload real | POST /api/documents (multipart) | ❌ Mockado |
| Pipeline status | GET /api/documents/:id/status (polling) | ❌ Mockado |
| Reprocessar | POST /api/documents/:id/reprocess | ❌ Mockado |
| Excluir | DELETE /api/documents/:id | ❌ Mockado |
| Detalhes | GET /api/documents/:id | ❌ Mockado |
| Phosphor Icons | unpkg CDN | ✅ |
| Blu Design System | tokens CSS locais | ✅ |

---

## 6. Cenários de Teste

### Upload
- [ ] Drag & drop de 1 arquivo PDF → feedback visual + toast
- [ ] Drag & drop de múltiplos arquivos → toast genérico
- [ ] File picker filtra corretamente as extensões (pdf,docx,csv,xlsx,txt,md)
- [ ] "Enviar documentos" sem arquivos → ?
- [ ] "Enviar documentos" com 3 metadados preenchidos → doc gerado com os 3 pares
- [ ] Campo de metadado com key="" é ignorado no envio
- [ ] Upload simulado gera doc com status "processing", stage "parse"

### Pipeline visual
- [ ] Doc processing: Parse=active, Embed+Extract+Grafo+Concluído=pending
- [ ] Doc done: todos os estágios=done
- [ ] Doc error: Parse=done, Embed=error, Extract+Grafo+Concluído=pending
- [ ] Erro mostra mensagem abaixo dos pills

### Ações
- [ ] 🔄 Reprocessar → status reseta, chunks/fatos zeram, erro limpa
- [ ] 🗑 Excluir → doc some da lista, toast confirma
- [ ] 👁 Ver detalhes → modal com todos os campos + JSON metadados
- [ ] Fechar modal pelo ✕
- [ ] Fechar modal clicando fora

### Edge cases
- [ ] Lista vazia → empty state
- [ ] Documento com warnings (não erro) → alerta laranja abaixo dos pills
- [ ] Documento com 0 chunks e 0 fatos → contadores não aparecem
- [ ] Nome de arquivo muito longo → truncado com ellipsis
