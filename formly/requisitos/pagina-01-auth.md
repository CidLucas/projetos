# 🔐 Página 01 — Auth

> **Status:** ✅ Implementado no site (`auth.html`)
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Tela de autenticação com tom acolhedor. Duas opções: Google OAuth ou magic link por e-mail. Ambos levam ao Builder (simulado no protótipo).

### Layout

```
┌──────────────────────────┐
│         formly           │
│                          │
│    Só mais uma coisa     │
│                          │
│  Crie uma conta          │
│  rapidinho para salvar   │
│  seu questionário.       │
│                          │
│ ┌──────────────────────┐ │
│ │ [G] Continuar c/     │ │
│ │    Google            │ │
│ └──────────────────────┘ │
│                          │
│         ou               │
│                          │
│ ┌──────────────────────┐ │
│ │ seu@email.com        │ │
│ └──────────────────────┘ │
│ ┌──────────────────────┐ │
│ │  Entrar com e-mail   │ │
│ └──────────────────────┘ │
└──────────────────────────┘
```

---

## 2. Elementos de UI

| Elemento | Tipo | Detalhes |
|---|---|---|
| Logo | texto | "formly", `--display`, 1.6rem, `--wine` |
| Título | heading | "Só mais uma coisa", weight 600 |
| Subtítulo | parágrafo | `--body`, 0.88rem, `--muted`, max-width 280px |
| Botão Google | button | Ícone SVG Google inline + "Continuar com Google", fundo #fff |
| Divisor | linha | "ou" com linhas nos lados |
| Input e-mail | email input | Type email, placeholder "seu@email.com", required |
| Botão submit | button primary | "Entrar com e-mail", `--wine` bg, texto branco |

---

## 3. Fluxos

```
1. Usuário clica "Continuar com Google" → builder.html (simulado)
2. Usuário preenche e-mail → submit → builder.html (simulado)
```

---

## 4. Regras

- Input e-mail tem `required` (HTML5)
- Ambos os métodos levam ao mesmo destino (builder)
- Sem validação de e-mail real no protótipo
- Sem integração com Supabase Auth no protótipo

---

## 5. Integrações

| Integração | Status |
|---|---|
| Google OAuth real | 🔴 Não implementado |
| Magic link e-mail (Resend) | 🔴 Não implementado |
| Redirecionamento | ✅ Simulado (href) |

---

## 6. Cenários de Teste

- [ ] Botão Google renderiza com ícone SVG
- [ ] Clique Google → builder.html
- [ ] Input e-mail aceita formato de e-mail
- [ ] Submit e-mail → builder.html
- [ ] Layout centrado e responsivo (max-width 360px)

---

> **Fonte:** `/tmp/projetos/formly/site/auth.html` (commit mais recente no GitHub)
