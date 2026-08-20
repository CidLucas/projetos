# 📋 Requisitos — Context-MCP

> **Produto:** MCP Brain Lite → Context-MCP (front-end)
> **Código fonte:** `CidLucas/mcp_brain_lite` → `Context-MCP.dc.html`
> **Última atualização:** 2026-07-30
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 🗂 Índice

| Arquivo | O que cobre |
|---|---|
| [`ui-elements.md`](./ui-elements.md) | 🧩 Catálogo visual de TODOS os elementos — extraído do código, sem opinião |
| [`requisitos-app.md`](./requisitos-app.md) | 📱 Requisitos de aplicação — Shell, regras globais, fluxo principal, integrações |
| [`pagina-01-ingestao.md`](./pagina-01-ingestao.md) | 📤 Página 1 — Ingestão de Documentos (upload, pipeline, lista de docs) |
| [`pagina-02-consolidacao.md`](./pagina-02-consolidacao.md) | 🔀 Página 2 — Consolidação de Memória (conflitos, resolução, timeline) |

---

## 🏗 Estrutura do App

```
Context-MCP (app single-page, 2 tabs)
│
├── 🖼️ Shell
│   ├── Topbar (logo + nav tabs + theme toggle)
│   └── Main (troca entre as 2 telas)
│
├── 📤 Tab 1: Ingestão de Documentos
│   ├── Drop zone (drag & drop)
│   ├── Painel de metadados
│   └── Lista de documentos (cards + pipeline pills)
│
└── 🔀 Tab 2: Consolidação de Memória
    ├── Stats bar (pendentes, resolvidos hoje, total)
    ├── Filtros (busca, entidade, predicado)
    ├── Conflict cards (comparação lado a lado)
    ├── Ações de resolução (4 opções)
    └── Painel de entidade (timeline lateral)
```

---

## 🔄 Fluxo de dados

```
[Upload doc] → Pipeline (Parse→Embed→Extract→Grafo) → Fatos no banco
                                                           ↓
                                            Mnemosyne detecta conflitos
                                                           ↓
                                            Conflitos aparecem na Tab 2
                                                           ↓
                                            Usuário resolve (humano no loop)
                                                           ↓
                                            Fatos consolidados → API MCP
```

---

## ⚠️ Status atual

- 🟡 **Front-end:** protótipo funcional com dados mockados
- 🔴 **Integrações:** todas as chamadas de API são simuladas (setTimeout/setState)
- 🟢 **Design System:** Blu DS + Phosphor Icons carregados corretamente
- 🟡 **Responsivo:** desktop-first, mobile não implementado

---

## 📝 Como usar estes arquivos

1. Comece pelo [`ui-elements.md`](./ui-elements.md) — veja o que já existe
2. Leia [`requisitos-app.md`](./requisitos-app.md) para entender a aplicação como um todo
3. Vá para a página específica que quer ajustar
4. Comente no arquivo ou me fale o que mudar
