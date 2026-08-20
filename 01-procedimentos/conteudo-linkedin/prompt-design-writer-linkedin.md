# PROMPT — Design Writer: integrar LinkedIn (OAuth oficial + MCP + skill própria)

> **Para:** profile `design-writer` (bot @falanego_bot)
> **De:** Lucas Cid (via PM)
> **Data:** 2026-08-20
> **Objetivo:** o design-writer passa a publicar/gerir conteúdo no LinkedIn da Deep
> Blue usando a **API oficial** (OAuth 2.0) — e cria uma **skill própria** dele.

---

## 1. Contexto

O dono criou um **app oficial do LinkedIn** (Developer Portal) para a Deep Blue.
As credenciais já estão validadas e o fluxo OAuth está montado. Você (design-writer)
será o perfil que usa o LinkedIn para publicar conteúdo (posts, cases, bastidores).

**⚠️ Credenciais (confidenciais — NÃO exponha em chat/logs):**
```
LINKEDIN_CLIENT_ID=<ver /home/ec2-user/linkedin-callback/.env>
LINKEDIN_CLIENT_SECRET=<ver /home/ec2-user/linkedin-callback/.env>
LINKEDIN_REDIRECT_URI=https://ip-172-31-41-24.tail2af056.ts.net/callback
```
Salvas em `/home/ec2-user/linkedin-callback/.env` (modo 600) no host do PM — leia de lá,
nunca transcreva em chat ou commit.

## 2. Infraestrutura já montada (pelo PM)

| Peça | Endereço | Status |
|---|---|---|
| App LinkedIn (Deep Blue) | Developer Portal | ✅ criado (Client ID/Secret acima) |
| Mini callback OAuth | `https://ip-172-31-41-24.tail2af056.ts.net/callback` (GET) | ✅ vivo (Funnel Tailscale) |
| Servidor callback | porta 8645 no host (`/home/ec2-user/linkedin-callback/server.py`) | ✅ rodando |
| Code capturado | `/tmp/linkedin_oauth_code.json` no host | ✅ code real já recebido |
| Access token | **ainda não trocado** (a troca code→token ficou pendente) | ⏳ você faz |

## 3. O que fazer (na ordem)

### Passo 1 — Completar a troca code→token

1. Leia o code: `curl http://127.0.0.1:8645/code` (ou `/home/ec2-user/linkedin-callback/.env`)
2. Troque pelo access token (POST form-urlencoded):
   ```
   POST https://www.linkedin.com/oauth/v2/accessToken
   grant_type=authorization_code&code=<CODE>&redirect_uri=<REDIRECT>&client_id=<ID>&client_secret=<SECRET>
   ```
3. Salve o token (e o refresh, se vier) em `/home/ec2-user/linkedin-callback/token.json` (modo 600)
4. Teste identidade: `GET https://api.linkedin.com/v2/userinfo` com `Authorization: Bearer <token>`

### Passo 2 — Descobrir as possibilidades da API

- **Microsoft Learn MCP** (a fonte canônica de docs da LinkedIn API): configure no
  VS Code o servidor MCP `https://learn.microsoft.com/api/mcp` e peça ao Copilot
  em agent mode: *"usando Microsoft Learn MCP, documente os endpoints para postar
  conteúdo (UGC posts), ler analytics de posts, e gerenciar a página da empresa"*.
- **Testar na mão** (curl): `POST /v2/ugcPosts` (publicar), `GET /v2/me`,
  `GET /v2/company/{id}/ugcPosts` — com o Bearer token do passo 1.
- Verificar scopes efetivos do token (o app pediu `w_member_social` + `openid profile email`).

### Passo 3 — Instalar/avaliar o MCP do LinkedIn

Dois candidatos (avalie qual serve ao SEU fluxo — você tem skills/tools próprias,
então pode preferir API direta via curl em vez de MCP):

1. **`stickerdaniel/linkedin-mcp-server`** (⭐3.2k, `uvx mcp-server-linkedin`):
   usa a SESSÃO do navegador logado (scraping) — lê perfis/empresas/jobs/inbox,
   MAS NÃO publica via API oficial. Bom para pesquisa de conteúdo.
   ⚠️ Scraping viola ToS do LinkedIn para automação — usar só leitura leve.
2. **API oficial via curl** (recomendado para PUBLICAR): `POST /v2/ugcPosts`
   com Bearer token. É o caminho que o dono quer para posts reais.

Decisão do dono: **publicar = API oficial. Pesquisar = pode usar o MCP de leitura
se quiser.** Se instalar o MCP no SEU profile, configurar em
`~/.hermes/profiles/design-writer/config.yaml` (seção `mcp_servers`).

### Passo 4 — Escrever sua SKILL PRÓPRIA

Crie uma skill sua (não copie a do PM): `skill_manage(action='create')` com nome
ex. `linkedin-content` (ou `linkedin-dw`), cobrindo:

- **Trigger**: quando o dono pedir post/conteúdo/case para o LinkedIn
- **Passos**: ler token (`/home/ec2-user/linkedin-callback/token.json`) → montar
  o payload UGC → `POST https://api.linkedin.com/v2/ugcPosts` → verificar
  `200 OK` + `id` → reportar URL do post
- **Pitfalls**: token expira (~60 dias? renovar via refresh ou reautorizar);
  scopes insuficientes → reautorizar; rate limits; texto com emoji/link exige
  `author:` URN correto; publicar na página vs perfil pessoal
- **Verificação**: o `id` do post + `GET /v2/ugcPosts/{id}` é a prova (nunca
  self-report)

Salve a skill e registre no seu SOUL.md / memória (Mnemosyne) o caminho do token
e o procedimento resumido.

## 4. Regras de segurança (obrigatórias)

- **NUNCA** colar o Client Secret ou o token no chat (redator mascara e corrompe)
- **NUNCA** usar `--verbose`/`-v` em comandos que passam o Bearer
- Token em arquivo modo 600; credenciais só em `/home/ec2-user/linkedin-callback/`
- Antes de QUALQUER publicação real: mostrar o texto ao dono e pedir OK (o dono
  aprova conteúdo — decisão explícita dele)
- Avisar o dono se o LinkedIn exigir re-autorização (token expirado)

## 5. Entregáveis

1. Access token salvo e validado (`GET /v2/userinfo` responde com o perfil)
2. Skill `linkedin-content` criada no seu profile (ou nome que preferir)
3. Teste de publicação em modo rascunho/privado (se a API permitir) OU publicação
   de 1 post de teste aprovado pelo dono
4. Relatório: o que a API permite, o que a skill cobre, e os pitfalls encontrados

## 6. Contato

Se o fluxo OAuth precisar de re-autorização (novo code), peça ao dono para abrir:
`https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=77k2dxvegi4vlk&redirect_uri=https%3A%2F%2Fip-172-31-41-24.tail2af056.ts.net%2Fcallback&scope=openid+profile+email+w_member_social&state=deepblue`
(a URL redireciona para o callback do PM, que salva o code novo).
