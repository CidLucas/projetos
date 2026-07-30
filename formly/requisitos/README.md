# 📋 Requisitos — Formly

> **Produto:** Formly — Fábrica de Questionários com Áudio + IA
> **Fase:** Descoberta (sem código ainda)
> **Última atualização:** 2026-07-30
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 🗂 Índice

| Arquivo | O que cobre |
|---|---|
| [`requisitos-app.md`](./requisitos-app.md) | 📱 Requisitos de aplicação — Shell, regras globais, fluxo principal, planos, integrações |
| [`pagina-01-criador.md`](./pagina-01-criador.md) | 📝 Página 1 — Criador de Questionário (3 modos: Canvas, Documento, Chat) |
| [`pagina-02-resposta.md`](./pagina-02-resposta.md) | 📋 Página 2 — Página de Resposta do respondente (texto + áudio) |
| [`pagina-03-dashboard.md`](./pagina-03-dashboard.md) | 📊 Página 3 — Dashboard de Resultados (gráficos, áudios, exportação) |

> ⚠️ Não há `ui-elements.md` porque o Formly **ainda não tem código**. Todos os requisitos são aspiracionais, baseados no Google Doc de escopo e nas conversas com o Lucas.

---

## 🏗 Estrutura do App

```
Formly (web app)
│
├── 🖼️ Shell
│   ├── Topbar (logo + nav + avatar/plano)
│   └── Layout responsivo
│
├── 📝 Página 1: Criador de Questionário
│   ├── Seletor de modo: Canvas | Documento | Chat
│   ├── Modo Canvas: drag & drop de caixinhas
│   ├── Modo Documento: importar texto + parsing automático
│   ├── Modo Chat: assistente IA conversacional
│   ├── Sidebar de tipos de pergunta
│   ├── Preview mobile em tempo real
│   └── Barra inferior: Personalizar, Preview, Salvar, Publicar
│
├── 📋 Página 2: Página de Resposta (pública)
│   ├── Exibição de perguntas (uma por vez ou scroll)
│   ├── Gravador de áudio + transcrição automática
│   ├── Validação de campos obrigatórios
│   └── Tela de encerramento
│
└── 📊 Página 3: Dashboard de Resultados
    ├── Cards de resumo (KPI)
    ├── Gráficos por pergunta
    ├── Player de áudio inline
    ├── Filtros por período
    └── Exportação CSV/PDF
```

---

## 🔄 Fluxo de dados

```
[Criador monta questionário] → Banco (PostgreSQL)
        ↓
[Link público gerado]
        ↓
[Respondente acessa e responde]
    → Texto: salvo direto no PostgreSQL
    → Áudio: upload S3 → transcrição Groq → texto + URL no PostgreSQL
        ↓
[Criador acessa Dashboard]
    → Agregação de respostas
    → Player de áudio (URL assinada S3)
    → Exportação CSV/PDF
```

---

## ⚠️ Status atual

- 🔴 **Código:** não existe
- 🟡 **Escopo macro:** definido no Google Doc
- 🟡 **Requisitos visuais:** primeira versão criada (este diretório)
- 🔴 **Stack:** preliminar (Next.js + FastAPI + PostgreSQL + Groq + OCI)
- 🔴 **Protótipo:** não iniciado

---

## 📝 Como usar estes arquivos

1. Comece pelo [`requisitos-app.md`](./requisitos-app.md) — visão geral da aplicação
2. Vá para a página que quer discutir (Criador, Resposta, ou Dashboard)
3. Comente no arquivo ou me fale o que ajustar
4. Quando houver código, criaremos o `ui-elements.md` extraído do código real
