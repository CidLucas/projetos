# 📋 Requisitos Blue V3 — Índice de Páginas

> Documento vivo. Cada página do Blue V3 tem seu próprio arquivo de requisitos.
> Baseado no código atual em `CidLucas/monorepo` → `apps/blu_web/src/pages/`.
> Atualizado conforme as conversas com o fundador.

---

## 🗂 Páginas (baseado no código atual)

### Shell / Layout Global

| # | Componente | Arquivo | Status |
|---|---|---|---|
| — | AppShell (layout) | [shell.md](./shell.md) | 🟡 Em andamento |
| — | ChatPanel | [chat.md](./chat.md) | 🟡 Em andamento |

### Onboarding

| # | Página | Arquivo | Status |
|---|---|---|---|
| 00 | Landing Page | [landing.md](./landing.md) | 🔴 Pendente |
| 01 | Onboarding (5 steps) | [onboarding.md](./onboarding.md) | 🟡 Em andamento |

### App (pós-login)

| # | Screen | Rota | Arquivo | Status |
|---|---|---|---|---|
| 10 | Início (Home) | `home` | [home.md](./home.md) | 🟡 Em andamento |
| 20 | Compras | `compras` | [compras.md](./compras.md) | 🟡 Em andamento |
| 30 | Financeiro | `financeiro` | [financeiro.md](./financeiro.md) | 🟡 Em andamento |
| 40 | Agenda | `agenda` | [agenda.md](./agenda.md) | 🟡 Em andamento |
| 50 | Estratégia | `estrategia` | [estrategia.md](./estrategia.md) | 🟡 Em andamento |
| 60 | Clientes | `clientes` | [clientes.md](./clientes.md) | 🟡 Em andamento (tela esmiuçada p/ design) |
| 70 | Biblioteca | `biblioteca` | [biblioteca.md](./biblioteca.md) | 🟡 Em andamento |
| 80 | Atividade | `atividade` | [atividade.md](./atividade.md) | 🟡 Em andamento |
| 90 | Admin | `admin` | [admin.md](./admin.md) | 🟡 Em andamento |
| 100 | AgentOps | `blu_ops` | [agentops.md](./agentops.md) | 🟡 Em andamento |

---

### Kanbans (spec transversal)

| Documento | Arquivo | Status |
|---|---|---|
| Especificação dos Kanbans (Clientes + Compras detalhados, varredura demais salas) | [kanbans.md](./kanbans.md) | 🟡 Proposta para validação |

---

## 📐 Template de documento de página

Cada arquivo segue esta estrutura (6 seções):

| # | Seção | Descrição |
|---|---|---|
| **1** | Visão Geral | Objetivo, contexto, relação com outras páginas |
| **2** | Estrutura de Elementos | Um subtópico por elemento da UI (tipo, posição, dados, interações, estados) |
| **3** | Fluxos de Processo | Criação, edição, exclusão, transições de estado |
| **4** | Regras de Negócio | Validações, permissões, restrições |
| **5** | Integrações | APIs, eventos, websockets |
| **6** | Cenários de Teste | Happy path + edge cases |

### Subtemplate de elemento de UI

```
### 2.X [Nome do Elemento]
- **Tipo:** tab | botão | card | lista | modal | formulário | sidebar | barra inferior
- **Posição:** topo / lateral / conteúdo central / barra inferior
- **Conteúdo/Dados:** o que está representado e de onde vem
- **Interações:** clicar, arrastar, preencher, expandir...
- **Estados visuais:** loading, vazio, erro, desabilitado
- **Condições de visibilidade:** quando aparece/esconde
```

---

## 🔄 Como alimentar este documento

- O fundador descreve uma página → Hermes preenche as 6 seções
- O fundador detalha um elemento → Hermes adiciona na seção 2
- O fundador descreve um fluxo → Hermes adiciona na seção 3
- Sempre que uma regra de negócio surgir → Hermes registra na seção 4
