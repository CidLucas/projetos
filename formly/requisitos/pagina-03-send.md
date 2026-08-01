# 📤 Página 03 — Send

> **Status:** ✅ Implementado no site (`send.html`) como protótipo estático
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Tela de envio do questionário para contatos. Permite selecionar destinatários individualmente, importar CSV, adicionar mensagem opcional, e disparar o envio.

### Layout

```
┌──────────────────────────────────────────┐
│  ← Voltar                                │
│                                          │
│  Enviar: Pesquisa de Clima 2026          │
│                                          │
│  Para quem?                              │
│  ┌──────────────────────────────────────┐│
│  │ Buscar contatos...                   ││
│  └──────────────────────────────────────┘│
│  ☑ Todos (4)                             │
│  ☑ ana@empresa.com.br                    │
│  ☑ carlos@empresa.com.br                 │
│  ☐ julia@empresa.com.br                  │
│  ☑ marcos@empresa.com.br                 │
│                                          │
│                 ou                       │
│                                          │
│  ┌──────────────────────────────────────┐│
│  │     ☁                                ││
│  │  Subir arquivo com e-mails           ││
│  │  (um por linha)                      ││
│  └──────────────────────────────────────┘│
│                                          │
│  Mensagem opcional                       │
│  ┌──────────────────────────────────────┐│
│  │ Olá! Sua opinião é importante...     ││
│  └──────────────────────────────────────┘│
│                                          │
│  ┌──────────────────────────────────────┐│
│  │       Enviar questionário →          ││
│  └──────────────────────────────────────┘│
└──────────────────────────────────────────┘
```

---

## 2. Elementos de UI

### 2.1 Navegação

| Elemento | Tipo | Detalhes |
|---|---|---|
| ← Voltar | button link | `--display`, `--muted`, hover: `--wine` |
| Título | heading | "Enviar: Pesquisa de Clima 2026" |

### 2.2 Seleção de Contatos

| Elemento | Tipo | Detalhes |
|---|---|---|
| Buscar | search input | Placeholder "Buscar contatos...", `--card` bg |
| Selecionar todos | toggle | Checkbox + "Todos (N)" ou "Selecionados (N)" |
| Lista de contatos | lista scroll | Max-height 200px, 4 contatos hardcoded |
| Contato | row com checkbox | Hover: `--paper2`, selecionado: `--wine-soft` |
| Check do contato | quadrado 18px | Selecionado: `--wine` bg + ✓ branco |

### 2.3 CSV Upload

| Elemento | Tipo | Detalhes |
|---|---|---|
| CSV zone | área dashed | Borda `2px dashed --line`, padding `--l` |
| CSV zone hover | — | Borda `--wine`, fundo `--wine-soft` |
| CSV zone preenchido | — | Borda `--pine`, fundo `--pine-soft`, texto "📄 contatos.csv · 12 contatos detectados" |

### 2.4 Mensagem e Envio

| Elemento | Tipo | Detalhes |
|---|---|---|
| Mensagem | textarea | Placeholder "Olá! Sua opinião é importante...", min-height 70px |
| Botão Enviar | button primary | `--wine` bg, full width, "Enviar questionário →" |
| Botão disabled | — | Opacity .5, cursor not-allowed |
| Botão enviando | — | Texto "Enviando...", disabled, 1.5s → analytics.html |

---

## 3. Fluxos

```
1. Usuário seleciona contatos (individual ou "Todos")
2. (Opcional) Upload de CSV → zona muda para estado preenchido
3. (Opcional) Escreve mensagem personalizada
4. Clica "Enviar questionário →"
5. Botão mostra "Enviando..." (1.5s)
6. Redireciona para analytics.html
```

---

## 4. Regras

- Contatos hardcoded: ana, carlos, julia, marcos (@empresa.com.br)
- Toggle "Todos": seleciona/deseleciona todos
- CSV: simulação — ao clicar, mostra "12 contatos detectados"
- Sem validação de destinatários vazios no protótipo
- Sem integração com Resend no protótipo

---

## 5. Integrações

| Integração | Status |
|---|---|
| Lista de contatos real (Supabase) | 🔴 Não implementado |
| Google Contacts import | 🔴 Não implementado |
| CSV upload real | 🔴 Simulado |
| Envio de e-mail (Resend) | 🔴 Não implementado |

---

## 6. Cenários de Teste

- [ ] Lista de 4 contatos renderizada
- [ ] Toggle seleção individual funciona
- [ ] "Todos (4)" seleciona/deseleciona todos
- [ ] Contador atualiza: "Selecionados (2)"
- [ ] CSV zone: clique → estado preenchido com 12 contatos
- [ ] Mensagem opcional aceita texto
- [ ] "Enviar questionário →" → estado "Enviando..." → analytics.html
- [ ] Voltar → builder.html
- [ ] Responsivo

---

> **Fonte:** `/tmp/projetos/formly/site/send.html` (commit mais recente no GitHub)
