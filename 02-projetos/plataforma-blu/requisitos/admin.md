# ⚙️ Admin — Requisitos Blue V3

> Última atualização: 2026-07-30 | Status: 🟡 Em andamento
> Fonte: `apps/blu_web/src/pages/app/AdminScreen.tsx` (1270 linhas)
> Restrição: visível apenas para `role === 'owner'`

---

## 1. Visão Geral

**Objetivo:** Painel de administração — integrações, usuários, auditoria, notificações, faturamento, LGPD e contexto.

**Relação com outras páginas:** Agenda (Google Calendar), Financeiro (Polp), Estratégia (Google Drive).

---

## 2. Estrutura de Elementos (Front-End)

### 2.1 Tabs de navegação
- **Tipo:** tabs horizontais
- **Conteúdo/Dados:** 7 abas — Integrações, Usuários, Auditoria, Notificações, Faturamento, LGPD, Contexto

### 2.2 Tab: Integrações
- **Tipo:** grid de cards organizado em lanes
- **Conteúdo/Dados:**
  - **ERPs & Gestão:** Conta Azul (NF-e e financeiro)
  - **Google:** Calendar, Drive
  - **Bancos (Polp):** Itaú, Bradesco, Santander, BB, Caixa, Nubank, Inter, PagBank, BTG, XP, C6, Sicoob, Sicredi, Stone + "Outro"
- **Interações:** conectar/desconectar (OAuth ou credenciais)
- **Estados visuais:** status conectado/desconectado

### 2.3 Tab: Usuários
- **Tipo:** lista de membros + formulário de convite
- **Conteúdo/Dados:** nome, email, role, status
- **Interações:** convidar, alterar permissões, remover

### 2.4 Tab: Auditoria
- **Tipo:** log de auditoria (timestamp, ação, usuário, detalhes)

### 2.5 Tab: Notificações
- **Tipo:** toggles de preferência por canal/agente

### 2.6 Tab: Faturamento
- **Tipo:** painel de plano atual, uso, histórico

### 2.7 Tab: LGPD
- **Tipo:** políticas de dados, consentimentos, exportação/exclusão

### 2.8 Tab: Contexto
- **Tipo:** informações estruturais da empresa usadas pelos agentes

---

## 3. Fluxos de Processo

### 3.1 Conectar Integração
```
Admin → Integrações → escolhe Google Calendar
  → OAuth → autoriza → integração "Conectado"
```

### 3.2 Convidar Usuário
```
Admin → Usuários → email + role
  → Convite enviado → usuário aceita → aparece na lista
```

---

## 4. Regras de Negócio

| # | Regra |
|---|---|
| R1 | Visível apenas para `role === 'owner'` |
| R2 | Desconectar remove tokens e interrompe sync |
| R3 | Bancos Polp: pessoa física e empresa (IDs separados) |

---

## 5. Integrações

| Integração | Tipo |
|---|---|
| useIntegrations | Query |
| useDisconnectIntegration | Mutation |
| useAuditLog | Query |
| useTeamMembers / useInviteUser / useUpdateUserPermissions | Query/Mutation |
| connectGoogleCalendar / connectGoogleDrive | Mutation (OAuth) |
| createCredential | Mutation |
| useNotificationPreferences | Query |

---

## 6. Cenários de Teste

- [ ] Conectar Google Calendar via OAuth
- [ ] Convidar novo membro
- [ ] OAuth cancelado → erro tratado
- [ ] Não-owner tenta acessar → não vê a página
