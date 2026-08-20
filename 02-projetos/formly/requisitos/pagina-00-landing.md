# 🏠 Página 00 — Landing

> **Status:** ✅ Implementado no site (`index.html`)
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Página inicial minimalista. Única ação: usuário descreve o questionário que precisa (texto ou áudio) e é levado para autenticação.

### Layout

```
┌──────────────────────────────────────┐
│                                      │
│              formly                  │
│                                      │
│     Precisa de um questionário?      │
│                                      │
│  ┌──────────────────────────────────┐│
│  │ Me fala qual, ou grave um áudio..││
│  └──────────────────────────────────┘│
│                                      │
│                ou                    │
│                                      │
│        ( ● ) Gravar áudio            │
│                                      │
└──────────────────────────────────────┘
```

---

## 2. Elementos de UI

| Elemento | Tipo | Tokens |
|---|---|---|
| Logo | texto | `--display`, 2rem, weight 700, `--wine` |
| Pergunta | heading | `--display`, 1.4rem, weight 500 |
| Input | text input | `--body`, `--card` bg, `--line` border, `--rl` radius, 20px padding |
| Input focus | — | border `--wine`, box-shadow `--wine-soft` |
| Placeholder | — | `--muted`, italic |
| Divisor "ou" | texto | `--mono`, 0.7rem, uppercase, `--muted` |
| Botão Gravar | button pill | `--display`, `--card` bg, `--wine` border, 999px radius |

### Estados do botão de áudio

| Estado | Visual |
|---|---|
| Normal | Fundo `--card`, texto `--wine`, dot estático |
| Hover | Fundo `--wine-soft` |
| Gravando | Fundo `--wine`, texto branco, animação pulse-rec, dot piscando |

---

## 3. Fluxos

```
1. Usuário digita descrição → Enter → auth.html
2. Usuário clica "Gravar áudio" → gravação simulada (2s) → auth.html
```

---

## 4. Regras

- Input com `autofocus` ao carregar
- Placeholder: "Me fala qual, ou grave um áudio..."
- Gravação de áudio: 2 segundos simulados (protótipo)
- Sem validação de input vazio no protótipo

---

## 5. Integrações

| Integração | Status |
|---|---|
| Redirecionamento pós-input | ✅ Simulado (href) |
| Gravação de áudio real | 🔴 Não implementado (setTimeout 2s) |

---

## 6. Cenários de Teste

- [ ] Input visível com autofocus
- [ ] Enter com texto → redireciona para auth.html
- [ ] Botão gravar → animação de gravação → redireciona
- [ ] Layout centralizado e responsivo
- [ ] Tema vinho/papel aplicado corretamente

---

> **Fonte:** `/tmp/projetos/formly/site/index.html` (commit mais recente no GitHub)
