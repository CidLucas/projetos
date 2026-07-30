# 📱 Requisitos de Aplicação — Context-MCP

> **Versão:** v0.1 — 2026-07-30
> **Baseado em:** `CidLucas/mcp_brain_lite` → `Context-MCP.dc.html`
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

**Context-MCP** é o painel de administração da memória corporativa do MCP Brain Lite. Serve para **ingestão de documentos** (upload + pipeline de processamento) e **consolidação de memória** (resolução de conflitos entre fatos extraídos de documentos diferentes).

### Objetivo da aplicação

Permitir que um administrador/usuário:
1. Faça upload de documentos corporativos (PDF, DOCX, XLSX, CSV, TXT, MD)
2. Acompanhe o pipeline de processamento (Parse → Embed → Extract → Grafo → Concluído)
3. Resolva conflitos de fatos (quando dois documentos afirmam valores diferentes para a mesma entidade/predicado)
4. Visualize a timeline de fatos de cada entidade

### Páginas

| Página | Arquivo | Descrição |
|---|---|---|
| **Ingestão de Documentos** | `pagina-01-ingestao.md` | Upload, metadados, acompanhamento de pipeline |
| **Consolidação de Memória** | `pagina-02-consolidacao.md` | Resolução de conflitos, timeline de entidades |

### Público-alvo

- Admin/IT da empresa que configurou o MCP Brain Lite
- Curador de conhecimento corporativo
- Usuário que precisa auditar/gerenciar a base de conhecimento

---

## 2. Elementos de UI (Shell)

Ver catálogo completo em [`ui-elements.md`](./ui-elements.md).

### Topbar

- **Logo:** 🧠 ícone brain em gradiente roxo + texto "Context-MCP"
- **Subtítulo:** "Memória corporativa" (uppercase, cinza, 9.5px)
- **Navegação:** 2 tabs centrais — "Ingestão de documentos" (📤) + "Consolidação de memória" (🔀)
- **Badge:** Na tab Consolidação, badge numérico laranja quando há conflitos pendentes
- **Toggle tema:** ☀️/🌙 canto direito, persiste preferência (prefers-color-scheme)

### Layout responsivo

- Desktop-first (max-width 1100px na ingestão, 860px na consolidação)
- Altura total da viewport (`100vh`), sem scroll da página externa
- Scroll interno por área (documentos, conflitos, painel de entidade)

### Design System

- Usa tokens do Blu Design System: `blu-design-system-1b37312d` (fonts, colors, typography, spacing, shadows, motion)
- Ícones: Phosphor Icons (`@phosphor-icons/web`)
- Variáveis CSS customizadas: `--bg`, `--surface`, `--glass`, `--fg`, `--mu`, `--ac`, `--ac-grad`, `--urg`, `--att`, `--ok`, `--gb`, `--r`, `--rl`, etc.
- Tema: dark (padrão) + light (detecta `prefers-color-scheme`)

---

## 3. Fluxos

### Fluxo principal: Ingestão → Pipeline → Consolidação

```
[Upload de documento]
        ↓
[Pipeline: Parse → Embed → Extract → Grafo]
        ↓
[Fatos extraídos gravados no banco]
        ↓
[Mnemosyne detecta conflitos entre fatos]
        ↓
[Conflitos aparecem na tela de Consolidação]
        ↓
[Usuário resolve: manter novo / antigo / ambos / editar]
        ↓
[Fatos consolidados disponíveis via MCP]
```

### Navegação

```
Topbar tabs: [Ingestão] [Consolidação]
                    ↓
         Troca instantânea entre telas
         (sem recarregar a página)
```

---

## 4. Regras de Negócio

### Pipeline de processamento

- Estágios: Parse → Embed → Extract → Grafo → Concluído
- Se um estágio falhar, os seguintes não executam (ficam como "pending")
- Status possíveis: `uploaded`, `processing`, `done`, `error`
- Documento pode ser reprocessado a qualquer momento (reseta para `processing` no estágio `parse`)

### Conflitos de fatos

- Um conflito surge quando **dois documentos diferentes** afirmam fatos com:
  - Mesma **entidade** (subject)
  - Mesmo **predicado** (ex: `salario_mensal`, `capital_social`)
  - **Valores diferentes** (ex: R$ 50.000 vs R$ 65.000)
- Tipos de entidade: Pessoa, Empresa, Contrato
- Predicados suportados (hardcoded): `salario_mensal`, `capital_social`, `prazo_vigencia`, `cnpj`, `endereco_sede`
- Cada fato tem: valid_from, valid_to (null = "em aberto"), confidence (0–1), source_filename

### Resolução de conflitos

- **Manter o novo:** encerra vigência do antigo, define novo como vigente
- **Manter o antigo:** rejeita entrante, mantém vigente intacto
- **Manter ambos:** define janelas de validade para coexistência temporal (ambos ficam vigentes em períodos diferentes)
- **Editar:** permite modificar valor, unidade, confiança e datas do entrante antes de confirmar

### Documentos

- Formatos aceitos: PDF, DOCX, CSV, XLSX, TXT, MD
- Metadados opcionais: pares key=value definidos pelo usuário no upload
- Limite de tokens: documentos que excedem 100k tokens geram erro no estágio Embed

### Temas

- Padrão: dark (respeita `prefers-color-scheme: dark`)
- Se o sistema está em light, inicia em light
- Alternância manual persiste na sessão (não persiste em localStorage no código atual)

---

## 5. Integrações

| Integração | Tipo | Status no código |
|---|---|---|
| **Backend MCP Brain Lite** | REST API | Não implementado — estado é mockado no `Component.state` |
| **Upload de arquivos** | Multipart POST | Mockado — `sendFiles()` gera documento fake após 2s |
| **Pipeline de processamento** | Async polling | Mockado — `reprocess()` usa `setTimeout` 3s |
| **Mnemosyne (detecção de conflitos)** | API interna | Dados mockados no `state.conflicts` |
| **Blu Design System** | CDN de tokens CSS | ✅ Carregado via `<helmet>` — `_ds/blu-design-system-...` |
| **Phosphor Icons** | CDN | ✅ unpkg.com/@phosphor-icons/web |
| **OAuth / Autenticação** | — | Não visível no front-end atual |

### Mock data (para desenvolvimento)

- **3 documentos** mock: Contrato_Silva_2024.pdf (done), Balancete_Q4_2024.xlsx (processing), Proposta_Comercial_Fornec.docx (error)
- **5 conflitos** mock: João Silva (salário), Silva & Associados (capital social + endereço), Contrato-001 (prazo), Fornecedor ABC (CNPJ)
- **Dados de timeline** hardcoded em `ENTITY_FACTS`: João Silva, Silva & Associados, Contrato-001, Fornecedor ABC

---

## 6. Cenários de Teste

### Upload de documento

- [ ] Arrastar arquivo PDF na drop zone → borda fica roxa, toast confirma
- [ ] Clicar "Selecionar arquivos" → file picker abre com filtro de extensões
- [ ] Selecionar arquivo → toast "X arquivo(s) selecionado(s)"
- [ ] Adicionar campo de metadado → novo par key=value aparece
- [ ] Remover campo de metadado → campo some
- [ ] Clicar "Enviar documentos" (sem arquivos selecionados) → ?
- [ ] Clicar "Enviar documentos" (com arquivos) → loading spinner, doc aparece na lista após 2s
- [ ] Upload de arquivo >100k tokens → erro "Falha ao gerar embeddings"

### Pipeline visual

- [ ] Documento processing mostra estágio atual como "active" (spinner)
- [ ] Documento done mostra todos os estágios "done" + "Concluído"
- [ ] Documento error mostra estágio do erro "error" + anteriores "done" + posteriores "pending"

### Conflitos

- [ ] Tab Consolidação mostra badge numérico = conflitos pendentes
- [ ] Stats bar atualiza com contagens corretas (pendentes, resolvidos hoje, total)
- [ ] Filtrar por entidade "Pessoa" → só mostra conflitos de Pessoa
- [ ] Filtrar por predicado "salário mensal" → só mostra conflitos desse predicado
- [ ] Buscar "Silva" → filtra por subject/entity/predicate/valores
- [ ] Empty state aparece quando filtros não encontram nada

### Resolução

- [ ] "Manter o novo" → conflito vai pra "Resolvido", toast confirma, badge atualiza
- [ ] "Manter o antigo" → mesmo fluxo
- [ ] "Manter ambos" → expande painel de datas → confirmar → resolvido
- [ ] "Editar" → expande formulário → alterar valor → confirmar → resolvido
- [ ] Cancelar resolução → volta ao estado pendente
- [ ] Cancelar edição → volta à barra de ações

### Painel de entidade

- [ ] Clicar "Contexto" → painel lateral abre com timeline da entidade
- [ ] Timeline mostra fatos em ordem com dots conectados
- [ ] Clicar ✕ → painel fecha

### Tema

- [ ] Clique no toggle → alterna dark/light
- [ ] Início com `prefers-color-scheme: light` → já abre em light

### Modal de detalhes

- [ ] Clicar 👁 → modal abre com todos os campos preenchidos
- [ ] Metadados JSON formatados corretamente
- [ ] Clicar ✕ ou fora → modal fecha
