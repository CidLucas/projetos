# Operações de domínios — Deep Blue (18/08/2026)

Mapa da presença online + instruções de DNS e e-mail corporativo.

## 1. Domínios

| Domínio | Registrar | Produto | Infra de destino |
|---|---|---|---|
| `deepblue.company` | Cloudflare | Hub (brand-hub) | Cloud Run `brand-hub` (blu-control-panel) |
| `bluapp.ink` | Namecheap | Blu | S3+CloudFront (deploy-web) |
| `formly.ink` | Namecheap | Formly | Cloud Run `formly-web` |
| `mcp-brain.com` | Cloudflare | Brain MCP | Cloud Run `auth-service` |

## 2. E-mail corporativo — Zoho Mail (Forever Free: 5 caixas, 5GB)

Configurar em **um domínio** (recomendado: `deepblue.company`); os demais entram
como domínios adicionais/aliases na mesma organização Zoho.

### 2.1 Passos no Zoho (https://mail.zoho.com / zoho.com/mail)

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

### 2.2 Registros DNS a criar no Cloudflare (`deepblue.company`)

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

### 2.3 Domínios secundários (formly.ink, mcp-brain.com, bluapp.ink)

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

- [ ] Deploy do hub (`make brand-hub-deploy`) + domain mapping `deepblue.company`
- [ ] E-mail Zoho (verificação + MX/SPF/DKIM) e criação das caixas
- [ ] Custom domain Formly (`formly.ink`) e Brain (`mcp-brain.com` + `app.*`)
- [ ] Domínio do Blu (`bluapp.ink`) via CloudFront + ACM
- [ ] V2: separar views do hub em páginas reais por domínio
