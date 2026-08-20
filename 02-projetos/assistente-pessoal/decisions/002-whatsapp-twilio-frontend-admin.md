# ADR-002 — Canal WhatsApp (Twilio) + frontend admin pequeno

- **Data:** 2026-08-20
- **Status:** Aceita
- **Decisor:** Lucas Cid

## Contexto

O assistente pessoal precisa de dois canais de interação:
1. **WhatsApp** como canal principal do usuário (chat natural).
2. **Frontend pequeno** para relatórios e gestão de admin.

O Blu também usa Twilio para WhatsApp. Decisão necessária: onde vive o cliente
Twilio e como o assistente consome WhatsApp.

## Decisão

1. **WhatsApp via Twilio, consumindo a lib `blu_twilio_client` (já existe no
   monorepo).** A lib é descentralizada no monorepo (`libs/blu_twilio_client`)
   e **já é consumida pelo Blu** (`tool_pool_api` — tools `send_whatsapp_message`
   e `send_whatsapp_batch`; `routines_api` — notificações). O assistente **não
   cria cliente Twilio próprio**: consome as tools de WhatsApp do `tool_pool_api`
   via MCP (mesmo caminho de Google/Notion). Nenhuma nova dependência Twilio no
   assistente.
2. **Frontend admin pequeno** — app React + TS + Vite em `apps/` (mesmo padrão
   do monorepo: blu-web, formly-web). Escopo mínimo: relatórios (sessões,
   uso de tools, custos, erros) e gestão (tenants, usuários, membros, grants).
   Sem chat no frontend — o chat é WhatsApp.
3. **Webhook de entrada WhatsApp** no `assistente_api` (Twilio webhook →
   mensagem → agente → resposta via tool_pool), reusando os helpers de webhook
   da `blu_twilio_client` (`webhook.py` — validação de assinatura).

## Alternativas consideradas

| Alternativa | Por que foi recusada |
|---|---|
| Cliente Twilio próprio no assistente | Duplica lib; a lib já existe e é compartilhada; divergência de config |
| Telegram em vez de WhatsApp | Dono decidiu WhatsApp; Twilio é o provedor que o Blu já usa |
| Frontend rico (chat + admin + relatórios) | Escopo grande; MVP pede "pequeno" — só relatórios + gestão |

## Consequências

- **Positivas:** zero código Twilio novo no assistente; config centralizada;
  webhook reusável; frontend segue padrão existente do monorepo.
- **Negativas:** acoplamento ao tool_pool (já é o contrato); dependência do
  webhook responder rápido (Twilio timeout) — precisa processamento assíncrono.

## Links

- Lib: `libs/blu_twilio_client` (client.py, webhook.py, config.py)
- Tools MCP: `tool_pool_api/.../tool_modules/whatsapp_client_module.py`
- Consumidores atuais do Blu: `routines_api/core/notifications.py`, `tool_pool_api/.../consumer_inbox_module.py`
