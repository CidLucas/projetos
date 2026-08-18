# Operações de domínios — Deep Blue (18/08/2026)

Mapa da presença online + instruções de DNS e e-mail corporativo.

## 1. Domínios

| Domínio | Registrar | Produto | Infra de destino |
|---|---|---|---|
| `deepblue.company` | Cloudflare | Hub (brand-hub) | Cloud Run `brand-hub` (blu-control-panel) |
| `bluapp.ink` | Namecheap | Blu | S3+CloudFront (deploy-web) |
| `formly.ink` | Namecheap | Formly | Cloud Run `formly-web` |
| `mcp-brain.com` | Cloudflare | Brain MCP | Cloud Run `auth-service` |

## 2. E-mail corporativo

⚠️ **Correção 18/08:** o plano "Forever Free" do Zoho **não existe mais** para
novas organizações (verificado na página oficial BR). Preços atuais: Mail Lite
R$ 5/usuário/mês (anual, 5GB), Mail Premium R$ 20/usuário/mês (50GB), Workplace
desde R$ 12/usuário/mês. **A opção de custo zero é o Cloudflare Email Routing**
(seção 2.0); o Zoho (seção 2.1+) é a opção paga com caixa real.

### 2.0 Custo zero — Cloudflare Email Routing (+ Gmail "Enviar como")

**Recebe** em `@deepblue.company` → encaminha para o Gmail existente (grátis,
aliases ilimitados: contato@, lucas@, suporte@). **Envia** com o domínio via
Gmail → Configurações → Contas → "Enviar como". Requer DNS no Cloudflare
(deepblue.company e mcp-brain.com já estão; formly.ink/bluapp.ink: mover DNS
para o Cloudflare é grátis e opcional).

1. Cloudflare → domínio → **Email** → Email Routing → Enable → criar rotas
   (`contato@` → gmail pessoal etc.).
2. O Cloudflare adiciona automaticamente: MX `route1.mx.cloudflare.net` (10/20/30)
   + TXT `v=spf1 include:_spf.mx.cloudflare.net ~all`.
3. Gmail → Configurações → Contas e importação → **Enviar como** →
   `lucas@deepblue.company` (verifica via código; SMTP do próprio Gmail).
4. Opcional DKIM no Cloudflare (região/domínio → Email Routing → DKIM) para
   melhor entregabilidade.

**Estado 18/08 (feito via API):** MX route1/2/3 + SPF + DKIM criados
automaticamente; rotas `contato@` e `lucas@` → `cid.lucas@gmail.com` criadas e
ativas. SPF atualizado para `v=spf1 include:_spf.mx.cloudflare.net
include:_spf.google.com ~all` (cobre o envio pelo Gmail "Enviar como").
Catch-all (endereços não listados) continua **drop** — para encaminhar tudo,
ativar no painel: Email Routing → Routing rules → Catch-all → Send to
`cid.lucas@gmail.com` (a API exige permissão de settings que o token atual não tem).

**Limitação honesta:** não há caixa separada com login próprio — é
encaminhamento; as respostas saem do Gmail com o remetente corporativo. Suficiente
para 1–3 pessoas; quando precisar de caixas reais (times, IMAP, retenção), migrar
para Zoho Mail Lite (R$ 5/usuário/mês).

### 2.1 Opção paga — Zoho Mail (caixa real)

Configurar em **um domínio** (recomendado: `deepblue.company`); os demais entram
como domínios adicionais/aliases na mesma organização Zoho.

### 2.2 Passos no Zoho (https://mail.zoho.com / zoho.com/mail)

1. Criar conta Zoho Mail → "Add Organization" → nome: **Deep Blue**.
2. Adicionar domínio `deepblue.company` → escolher **Zoho Mail**.
3. O painel mostra um registro de **verificação TXT** (`zoho-verification=...`):
   adicionar no Cloudflare (aba DNS do domínio) → clicar "Verificar".
4. Após verificação, adicionar os **registros MX** (seção 2.2) e clicar
   "Continue" → o Zoho valida o e-mail de boas-vindas.
5. Criar caixas: `lucas@deepblue.company`, `contato@deepblue.company`.
6. **SPF**: adicionar o TXT da seção 2.2.
7. **DKIM**: no painel Zoho → Domínio → DKIM → gerar chave → copiar o TXT
   `v=DKIM1; k=rsa; p=...` (selector `zoho`) → adicionar no Cloudflare → clicar
   "Validate". (Opicional mas recomendado — melhora entregabilidade.)

### 2.3 Registros DNS a criar no Cloudflare (`deepblue.company`)

| Tipo | Nome | Valor | TTL |
|---|---|---|---|
| TXT | (raiz) | `zoho-verification=<gerado no painel>` | Auto |
| MX | (raiz) | `mx.zoho.com` (prioridade 10) | Auto |
| MX | (raiz) | `mx2.zoho.com` (prioridade 20) | Auto |
| MX | (raiz) | `mx3.zoho.com` (prioridade 30) | Auto |
| TXT | (raiz) | `v=spf1 include:zoho.com ~all` | Auto |
| TXT | `zoho._domainkey` | `v=DKIM1; k=rsa; p=<gerado no painel>` | Auto |

> ⚠️ Se existir TXT SPF antigo no domínio, substituir (só pode haver um).
> Observação: com Cloudflare, MX/TXT ficam em "DNS only" (cinza), nunca no proxy.

### 2.4 Domínios secundários (formly.ink, mcp-brain.com, bluapp.ink)

No Zoho: Domains → Add Domain → repetir verificação (TXT `zoho-verification`)
e MX. Para v1, aliases (`suporte@formly.ink` → `contato@deepblue.company`)
podem ser feitos com os mesmos MX + SPF `include:zoho.com`.

## 3. Custom domains no Cloud Run (Formly e Brain — rodar no Mac)

Cada serviço Cloud Run precisa de um domain mapping; o comando imprime os
registros DNS (CNAME → `ghs.googlehosted.com` + TXT `google-site-verification`)
para adicionar no registrar. TLS automático após validação.

### 3.1 Formly — `formly.ink` (DNS no Namecheap)

```bash
gcloud run domain-mappings create --service formly-web \
  --domain formly.ink --project blu-control-panel --region southamerica-east1
# opcional: app.formly.ink idem
```

Namecheap: Advanced DNS → adicionar CNAME (`formly.ink` → `ghs.googlehosted.com`)
+ TXT de verificação. Aguardar status `ACTIVE` e certificado.

### 3.2 Brain — `mcp-brain.com` (DNS no Cloudflare)

```bash
gcloud run domain-mappings create --service auth-service \
  --domain mcp-brain.com --project blu-control-panel --region southamerica-east1
# app.mcp-brain.com idem (usado nos CTAs do hub)
```

Cloudflare: DNS → CNAME `mcp-brain.com` → `ghs.googlehosted.com` (DNS only) +
TXT de verificação. Aguardar `ACTIVE`.

> Depois de mapeado, o hub aponta `https://app.mcp-brain.com` e
> `https://app.formly.ink` (quando criado) — atualizar CTAs se mudar o destino.

## 4. Blu — `bluapp.ink` (S3+CloudFront)

O `blu_web` já está em S3+CloudFront. Para o domínio:

1. `make deploy-web` (publica no bucket atual).
2. No terraform (`infra/terraform/environments/production`): adicionar
   `bluapp.ink` + `app.bluapp.ink` como alternate domains no CloudFront e
   certificado ACM em `us-east-1` (região obrigatória de certs p/ CloudFront).
3. DNS no Namecheap: CNAME `bluapp.ink` → `<cloudfront-domain>` + CNAME
   `app.bluapp.ink` → idem.
4. Atualizar `WEB_PUBLIC_URL` no `.env` (Mac) para o domínio final.

## 5. Pendências

- [x] Deploy do hub (`make brand-hub-deploy`) + domain mapping `deepblue.company` — **no ar 18/08**
- [x] Custom domain Formly — **`formly.ink` mapeado (Cloud Run), no ar 18/08**
- [x] Custom domain Brain — **`app.mcp-brain.com` mapeado, no ar 18/08**
- [ ] **Deploy da finalização do hub** (logo real, chips, drawers, áudio) — commitar `feat/brand-hub` → main → `make brand-hub-deploy`
- [ ] **Deploy do `brand-hub-voice`** (áudio → Groq Whisper): criar secrets `GROQ_API_KEY`, `SMTP_USER`, `SMTP_PASS` (senha de app do Gmail) e rodar `make brand-hub-voice-deploy`
- [ ] Domínio do Blu (`bluapp.ink`) via CloudFront + ACM — **`app.bluapp.ink` não resolve ainda (CTAs do hub apontam para ele)**
- [ ] E-mail Zoho (verificação + MX/SPF/DKIM) e criação das caixas — Cloudflare Email Routing já ativo (contato@ e lucas@ → Gmail)
- [ ] V2: separar views do hub em páginas reais por domínio
