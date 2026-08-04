# Status — Formly

> Última atualização: 2026-08-04
> **Produto:** SaaS próprio (Deep Blue)
> **Fase:** Fase 0 — Protótipo funcional (realinhado ao protótipo canônico)
> **Responsável:** Lucas Cid

## 🩺 Saúde geral

🟢 **Protótipo funcional** — 5 telas implementadas e realinhadas ao design system wine/pine/paper, 12 tipos de pergunta no backend, fluxo landing → auth → builder → send → analytics operante. Gateway estável após limpeza de disco.

## 📊 Resumo executivo

| Item | Status |
|---|---|
| Escopo macro definido | 🟢 Google Doc criado (2026-07-30) |
| Protótipo HTML canônico (5 telas) | 🟢 `site/` no hub (index, auth, builder, send, analytics) |
| Design system wine/pine/paper | 🟢 `global.css` reescrito fiel ao protótipo (R1) |
| Backend 12 tipos de pergunta | 🟢 enum expandido: nps, ranking, matrix, datetime, number, dyn_list (R2) |
| Landing + Auth (sem JWT manual) | 🟢 Landing enxuta + Auth "Só mais uma coisa" + dev login (R3, R7) |
| Builder cards empilhados | 🟢 coluna 560px, + Pergunta / Enviar →, 12 tipos (R4) |
| Survey 12 tipos wine/pine/paper | 🟢 modo etapas/scroll, abertura/conclusão (R5) |
| Send (contatos + CSV) | 🟢 seleção, busca, CSV, mensagem (R6) |
| Analytics (KPIs + barras) | 🟢 3 KPIs, barras por pergunta, export CSV (R6) |
| Quebra de linha em textos longos | 🟢 overflow-wrap + textarea auto-resize (R8) |
| Fluxo de áudio completo | 🟢 gravação livre, timer, limite 2min, transcrição editável, e-mail (R9) |
| Repo de código | 🟢 https://github.com/CidLucas/formly — realinhamento + correções commitados (5 commits, 2026-08-04) |
| Transcrição real | 🟢 `POST /api/transcribe` — Groq Whisper |
| Envio de e-mail real (Resend) | 🟢 `/distribute` + RESEND_API_KEY configurada — template HTML com identidade visual, remetente = nome/e-mail do Google, envio validado |
| Ranking reordenável (mobile) | 🟢 botões ↑/↓ + drag com setData (R10) |
| Botão enviar no rodapé do builder | 🟢 `.submit-sticky` fixo no rodapé (R11) |
| Preview antes de enviar | 🟢 `/preview/:id` — form como o respondente vê (R11) |
| Stats por pergunta no Dashboard | 🟢 fix serialize_survey (backend) — barras por pergunta funcionando |
| Auth produção (Supabase OAuth) | 🟡 placeholder dev login; comentário onde plugar Supabase |
| Supabase/RLS em produção | 🟡 dev usa PostgreSQL Docker local + JWT dev |
| Observabilidade | 🔴 não iniciada |

## 🔑 Decisões recentes

| # | Decisão | Data |
|---|---|---|
| 1 | Realinhar TODO o app ao protótipo aprovado (design wine/pine/paper + 12 tipos + 5 telas) | 2026-08-01 |
| 2 | Remover entrada manual de JWT do fluxo — auth silenciosa via dev login (protótipo não tem token bar) | 2026-08-01 |
| 3 | Gravação de áudio: limite de 2 minutos, timer visível, transcrição editável, e-mail antes de prosseguir | 2026-08-04 |
| 4 | Modelo OpenCode: `deepseek-v4-flash-free` (New); conta Zen sem saldo para modelos pagos | 2026-08-04 |
| 5 | Stack efetiva: Vite + React 18 + FastAPI + PostgreSQL (Docker dev) — não Next.js | 2026-08-04 |
| 6 | Ranking com botões ↑/↓ (não só drag) — respondentes mobile não têm drag | 2026-08-04 |
| 7 | Preview obrigatório antes de enviar (builder → preview → send) | 2026-08-04 |
| 8 | Envio de e-mail via Resend; free só envia p/ e-mail verificado da conta | 2026-08-04 |
| 9 | E-mail com identidade visual (wine/pine/paper) + remetente = nome/e-mail do Google | 2026-08-04 |
| 10 | Send simplificado: só e-mail manual + CSV (sem lista de contatos) | 2026-08-04 |

## 🎯 Próximas ações

- [ ] **Hermes** — conectar Supabase Auth real (Google OAuth + magic link) no `/auth`
- [ ] **Hermes** — verificar domínio no Resend (`onboarding@resend.dev` → `envio@seudominio.com`) para enviar a respondentes reais
- [ ] **Lucas** — validar fluxo completo no navegador (criar → preview → enviar → responder → dashboard)
- [ ] **Hermes** — deploy do protótipo (frontend + backend) para acesso externo

## 📅 Histórico de atualizações

| Data | Atualização |
|---|---|
| 2026-07-30 | Bootstrap do projeto no hub. Google Doc importado. Requisitos iniciados. |
| 2026-08-01 | Protótipo HTML canônico no hub (`site/`). Specs R1–R9 escritos. |
| 2026-08-01 | Realinhamento R1–R7 executados (design system, 12 tipos, 5 telas, sem JWT, text wrap). |
| 2026-08-04 | R8/R9 concluídos (text wrap + fluxo de áudio com limite 2min). Commit + push do realinhamento. Doc do hub atualizada. |
| 2026-08-04 | Correções pós-teste: fix serialize_survey (stats por pergunta), ranking mobile (R10), sticky + preview (R11), envio Resend real (R12). Commit + push. |
| 2026-08-04 | E-mail final: template HTML wine/pine/paper, remetente = nome do Google (Lucas Cid), sem mensagem do usuário no corpo. Send simplificado (manual + CSV). Auth preparado p/ Supabase OAuth. |
