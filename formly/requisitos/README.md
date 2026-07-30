# 📋 Requisitos — Formly

> **Produto:** Formly — Fábrica de Questionários com Áudio e IA
> **Fase:** Descoberta → Especificação de requisitos
> **Código:** A construir (stack: Next.js/React + FastAPI + PostgreSQL + Groq)
> **Última atualização:** 2026-07-30

---

## 🗂 Índice

| Arquivo | O que cobre |
|---|---|
| [`requisitos-app.md`](./requisitos-app.md) | 📱 Requisitos de aplicação — shell, regras globais, fluxo macro, integrações |
| [`pagina-01-criador.md`](./pagina-01-criador.md) | ✏️ Página do Criador — builder híbrido (chat + editor), fluxo 4 passos, distribuição |
| [`pagina-02-respondente.md`](./pagina-02-respondente.md) | 📝 Página do Respondente — questionário público, tipos de resposta, follow-up |
| [`pagina-03-dashboard.md`](./pagina-03-dashboard.md) | 📊 Dashboard de Resultados — respostas agregadas, filtros, exportação |

---

## 🏗 Estrutura do App

```
Formly (3 áreas)
│
├── ✏️ Criador (Builder)
│   ├── Chat panel (conversa com IA)
│   ├── Canvas/Preview (questionário sendo montado)
│   ├── Fluxo 4 passos: Input → Refinamento → Geração → Ajuste
│   └── Distribuição (enviar link após publicar)
│
├── 📝 Respondente (página pública)
│   ├── Renderização dos componentes de pergunta
│   ├── Áudio (gravação + transcrição)
│   └── Agente de follow-up (aprofundamento de respostas)
│
└── 📊 Dashboard
    ├── Respostas agregadas
    ├── Filtros + exportação
    └── (Fase 4) Relatórios IA
```

---

## 🔄 Fluxo macro

```
CRIADOR                          RESPONDENTE                   DASHBOARD
────────                         ───────────                   ─────────
1. Input (voz/texto)             Acessa link público           Vê respostas
   ↓                                 ↓                         agrupadas
2. Refinamento (IA pergunta)     Responde perguntas
   ↓                             (texto / áudio)
3. Geração (IA monta esqueleto)     ↓                         Filtra + exporta
   ↓                             Follow-up (se incompleto)
4. Ajuste (conversa + edição)       ↓
   ↓                             Revisão final → Enviar
5. Publicar → Link gerado
   ↓
6. Distribuir (selecionar contatos → enviar link)
```

---

## ⚠️ Status atual

- 🟡 **Fase:** Descoberta / Especificação
- 🟢 **Escopo macro:** definido no [Google Doc](https://docs.google.com/document/d/1V539iHGWJq-4qMA30YS7FbRCo023rwYm7rwbMkfGhEw/edit)
- 🟡 **Requisitos de UI/UX:** em construção (estes arquivos)
- 🔴 **Código:** não iniciado
- 🔴 **Design System:** a definir (Blu DS ou novo?)
