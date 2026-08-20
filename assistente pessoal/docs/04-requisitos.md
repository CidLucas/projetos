# 📋 Requisitos e Funcionalidades — Assistente Pessoal (MVP)

> **Versão:** 1.0 (2026-08-20) · **Status:** Aprovado para planejamento
> **Base:** visão + ADR-001/002/003 · **Formato:** RF (funcional) / RNF (não-funcional)

---

## 1. Atores

| Ator | Descrição |
|---|---|
| **Usuário** | Dono do tenant; conversa via WhatsApp; vê relatórios no admin |
| **Admin** | Gerencia tenants, usuários, papéis e grants (pode ser o dono) |
| **Polp / Pluggy** | Agregador Open Finance — envia webhooks de dados bancários |
| **Twilio** | Provedor WhatsApp — envia/recebe mensagens |
| **Tool Pool API** | Hub MCP do monorepo — expõe Google, WhatsApp, (futuro) Notion |

---

## 2. Requisitos Funcionais

### RF-A · Conversa e sessão

| ID | Requisito | Prioridade | Fase |
|---|---|---|---|
| RF-A1 | Receber tarefas em linguagem natural via WhatsApp e via `POST /api/v1/chat` | Alta | F1 |
| RF-A2 | Manter histórico multi-turno persistente por (tenant, sessão) | Alta | F1 |
| RF-A3 | Multi-tenant: cada tenant só acessa as próprias sessões | Alta | F0/F1 |
| RF-A4 | Selecionar modelo LLM por tier (blu_llm_service) | Média | F0 |
| RF-A5 | Não narrar uso de ferramentas; entregar resposta pronta | Média | F0 |

### RF-B · Navegação web

| ID | Requisito | Prioridade | Fase |
|---|---|---|---|
| RF-B1 | Navegar para URL e executar ações (click, type, press, scroll, fill) via Playwright | Alta | F1 |
| RF-B2 | Observation por visão simplificada: AX tree/Markdown (ariaSnapshot) em vez de pixels | Alta | F1 |
| RF-B3 | Extrair conteúdo estruturado da página (título, texto, links, dados) | Alta | F1 |
| RF-B4 | Screenshot sob demanda (verificação visual quando necessário) | Média | F1 |
| RF-B5 | Allowlist de domínios por tarefa (Fetch interception — padrão safe-browser) | Alta | F1 |
| RF-B6 | Re-snapshot após mutação; refs nunca reutilizados após mudança de DOM | Alta | F1 |

### RF-C · Google Workspace

| ID | Requisito | Prioridade | Fase |
|---|---|---|---|
| RF-C1 | Google Docs: criar, ler, editar (append/replace), listar | Alta | F1 |
| RF-C2 | Google Agenda: consultar eventos (existe) + criar/atualizar | Alta | F1 |
| RF-C3 | Gmail: ler/buscar emails (existe) | Média | F1 |
| RF-C4 | Google Sheets: ler/escrever (existe) | Média | F1 |
| RF-C5 | Tokens OAuth por tenant (via blu_context_service) — sem secret em prompt | Alta | F1 |

### RF-D · Notion

| ID | Requisito | Prioridade | Fase |
|---|---|---|---|
| RF-D1 | Criar página/bloco no Notion | Média | F1 |
| RF-D2 | Buscar conteúdo no Notion | Média | F1 |
| RF-D3 | Atualizar página existente | Média | F1 |

### RF-E · WhatsApp (Twilio)

| ID | Requisito | Prioridade | Fase |
|---|---|---|---|
| RF-E1 | Enviar mensagem WhatsApp (via tool_pool `send_whatsapp_message` — lib compartilhada) | Alta | F1 |
| RF-E2 | Enviar em lote (máx 20 — `send_whatsapp_batch`) | Média | F1 |
| RF-E3 | Receber mensagens via webhook com validação HMAC (webhook.py da lib) | Alta | F1 |
| RF-E4 | Consultar status de entrega (`check_whatsapp_status`) | Média | F1 |
| RF-E5 | Responder na janela de 24h (free-form) ou via template aprovado (business-initiated) | Alta | F1 |
| RF-E6 | Reply imediato + processamento assíncrono (timeout Twilio ~5s) | Alta | F1 |

### RF-F · Open Finance (Polp)

| ID | Requisito | Prioridade | Fase |
|---|---|---|---|
| RF-F1 | Consultar saldo/cash position (reuso FIN-01 sobre `polp_accounts`) | Alta | F2 |
| RF-F2 | Consultar gastos por categoria/período (reuso FIN-02 sobre `polp_transactions`) | Alta | F2 |
| RF-F3 | **Classificar gastos por LLM** — refinar categoria quando ausente/genérica | Alta | F2 |
| RF-F4 | Responder perguntas financeiras ("quanto gastei em X este mês?") | Alta | F2 |
| RF-F5 | Notificação de transação nova via WhatsApp (webhook `transaction/created`) | Média | F2 |
| RF-F6 | Fronteira de dados: só transações do tenant autenticado (regra F-20) | Alta | F2 |

### RF-G · Frontend admin

| ID | Requisito | Prioridade | Fase |
|---|---|---|---|
| RF-G1 | Login via Supabase (blu_auth) | Alta | F2 |
| RF-G2 | Relatórios: sessões, uso de tools, custos LLM, erros | Alta | F2 |
| RF-G3 | Financeiro: saldos, gastos por categoria, classificação LLM | Alta | F2 |
| RF-G4 | Gestão: tenants, usuários, membros (papéis), grants de escopo | Alta | F2 |
| RF-G5 | Visão de integrações (status Polp, Google, WhatsApp) | Média | F2 |

---

## 3. Requisitos Não-Funcionais

| ID | Requisito | Métrica |
|---|---|---|
| RNF-1 | **Isolamento multi-tenant** — identidade só do token (regra F-20 da memory_api) | 2 tenants nunca cruzam dados; argumento de roteamento nem existe no schema das tools |
| RNF-2 | **Migrations imutáveis** com checksum | `make migrate` idempotente; alteração de arquivo aplicado é denunciada |
| RNF-3 | **Segurança de navegação** — conteúdo de página é untrusted | allowlist de domínios; nunca seguir instruções de páginas (prompt injection) |
| RNF-4 | **Webhook Twilio** | resposta < 5s (reply imediato + fila); validação HMAC |
| RNF-5 | **Latência** | cold start < 5s; resposta com tools < 30s |
| RNF-6 | **Observabilidade** | structlog estruturado; traces langfuse (custo/uso por tenant) |
| RNF-7 | **Quotas por tenant** (F3) | teto checado antes da escrita |
| RNF-8 | **LGPD** | dados financeiros = dados pessoais; lib blu_lgpd; nada de PII em logs |
| RNF-9 | **Credenciais** | tokens/segredos nunca no prompt; só em headers HTTP (MCP) |
| RNF-10 | **Deploy** | mesmo padrão do monorepo (Neon + Cloud Run); staging antes de prod |

---

## 4. User stories principais (aceite do MVP)

| # | Story | Critério de aceite |
|---|---|---|
| US-1 | "Leia este doc do Google e me resuma" | agente lê doc real via tool_pool, devolve resumo citando fonte |
| US-2 | "Agende uma reunião amanhã 14h" | cria evento real no Google Agenda do tenant |
| US-3 | "Quanto gastei em restaurantes este mês?" | responde com dados reais do Polp (transações do tenant, categoria LLM) |
| US-4 | "Crie uma página no Notion com os pontos da reunião" | página criada; link devolvido |
| US-5 | "Pesquise no site X o preço do produto Y" | navega com Playwright, extrai, responde com fonte |
| US-6 | Admin vê relatórios e gerencia usuário | CRUD real no control plane, dados reais |
| US-7 | Mensagem de transação bancária chega no WhatsApp | webhook Polp → resumo → Twilio → usuário |

---

## 5. Fora de escopo (explícito)

- Chat no frontend (chat é WhatsApp)
- Telegram
- Migração LangGraph→Agno agora (só validação F3)
- Browser worker separado no MVP (embutido; worker na F3)
- Novas integrações (Slack, Drive, Trello...) — via tool_pool sob demanda
- Modificação de dados financeiros via assistente (leitura e classificação apenas no MVP)
