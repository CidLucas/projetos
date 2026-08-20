# 🖼️ Shell (Layout Global) — Requisitos Blue V3

> Última atualização: 2026-07-30 | Status: 🟡 Em andamento
> Fonte: `AppShell.tsx`, `Sidebar.tsx`, `Topbar.tsx`, `SpotlightSearch.tsx`

---

## 1. Visão Geral

**Objetivo:** Layout principal que envolve todas as páginas — topbar, sidebar, área de conteúdo, chat panel e overlays.

**Contexto:** Toda página pós-login é renderizada dentro do AppShell.

---

## 2. Estrutura de Elementos (Front-End)

### 2.1 Topbar
- **Tipo:** barra superior fixa
- **Conteúdo/Dados:** logo, toggle tema (dark/light), busca (atalho Ctrl+K)
- **Interações:** alternar tema, abrir SpotlightSearch

### 2.2 Sidebar (Desktop)
- **Tipo:** barra lateral fixa com ícones
- **Conteúdo/Dados:** 10 ícones:
  - 🏠 Início, 🛒 Compras, 📊 Financeiro, 📅 Agenda, 🎯 Estratégia, 👥 Clientes, 📚 Biblioteca, 🔔 Atividade, ⚙️ Admin (owner), 🖥️ AgentOps (ADMIN)
- **Interações:** clique → navega (lazy mount, preserva estado); badge de pendências
- **Condições de visibilidade:** Admin → owner; AgentOps → tier ADMIN

### 2.3 Seção Inferior da Sidebar
- **Conteúdo/Dados:** Atividade, Admin, AgentOps agrupados separadamente

### 2.4 Mobile Bottom Nav
- **Tipo:** barra inferior + menu hamburguer (mobile only)
- **Conteúdo/Dados:** grid de ícones + labels

### 2.5 Área de Conteúdo (Main)
- **Tipo:** container central
- **Conteúdo/Dados:** screen ativa (lazy mount — primeira visita monta, depois preserva)

### 2.6 ChatPanel
- **Tipo:** painel lateral de chat (ver chat.md)
- **Posição:** sobreposição direita

### 2.7 SpotlightSearch (Ctrl+K)
- **Tipo:** modal de busca global com overlay blur

### 2.8 FirstRunOverlay
- **Tipo:** overlay tutorial de primeiro acesso
- **Condições:** apenas quando `firstRun === true` e sem dados

### 2.9 ToastContainer
- **Tipo:** container de notificações toast (sucesso, erro, info)

### 2.10 EditorOverlay
- **Tipo:** overlay de editor de documento

---

## 3. Fluxos de Processo

### Navegação
```
Clique em ícone na Sidebar → store atualiza screen
  → Primeira visita: componente montado (lazy)
  → Visitas seguintes: componente já montado (preserva estado/scroll)
```

### Tema
```
Toggle tema → estado invertido → classe 'light' no body
  → Preferência salva em localStorage com escopo do clientId
```

---

## 4. Regras de Negócio

| # | Regra |
|---|---|
| R1 | AdminScreen: apenas `role === 'owner'` |
| R2 | AgentOpsRoom: apenas `tier === 'ADMIN'` |
| R3 | Screens montadas lazy e nunca desmontadas |
| R4 | Tema escopo por clientId (multi-tenant) |
| R5 | FirstRunOverlay só aparece sem dados ingeridos |

---

## 5. Integrações

| Integração | Tipo |
|---|---|
| useAppStore | Zustand (screen, firstRun, tema) |
| useAuth | Hook (clientId, tier) |
| useMyRole | Hook (owner, member) |
