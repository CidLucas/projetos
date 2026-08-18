# SPEC — Brand Hub (Deep Blue → Produtos)

**Profile:** design-writer
**Projeto:** brand-hub
**Data:** 2026-08-17
**Tipo:** spec de desenvolvimento
**Status:** v1.0 — aprovada a direção (hub navegável: empresa → produtos)

---

## 1. Objetivo

Um hub navegável que mostra **como um usuário vê a Deep Blue na internet**:
a landing da empresa com seus dois braços (Labs + Consulting) e, dentro do
Labs, os produtos reais (Blu, Formly, Brain MCP) — cada um com sua identidade
visual, sua landing e seu app.

**Decisão de produto (Lucas, 17/08/2026):** os produtos NÃO são vitrine de
venda no site da empresa. Eles vivem **dentro do braço Labs** e servem para
**gerar credibilidade** — prova de que a Deep Blue desenvolve produtos — o que
abre a porta para vender consultoria e os próprios produtos.

**Fluxo do usuário:**
```
Empresa (landing) → Labs (expandir) → Abrir produto → produto real (usar, entrar, comprar)
```

## 2. Estrutura de domínios (destinos reais)

| Produto | Domínio | Estado | Deploy real hoje |
|---|---|---|---|
| Deep Blue (empresa) | `deepblue.company` | ✅ comprado 18/08 (Cloudflare) | ✅ NO AR: `brand-hub-960100281317.southamerica-east1.run.app` (sha-05855ae) — falta domain mapping |
| Blu | `bluapp.ink` (+ `app.bluapp.ink`) | ✅ comprado 18/08 (Namecheap) | blu_web S3+CloudFront (sem domínio próprio ainda) |
| Formly | `formly.ink` (+ `app.formly.ink`) | ✅ comprado 18/08 (Namecheap) | `https://formly-web-xkndgpat3q-rj.a.run.app/` (Cloud Run) |
| Brain MCP | `mcp-brain.com` (+ `app.mcp-brain.com`) | ✅ comprado 18/08 (Cloudflare) | gateway memory_api (deploy próprio) |

Regra: **todo CTA de produto abre o produto real em nova aba** (`target="_blank"`),
nunca uma tela de demonstração interna.

## 3. Arquitetura da página

Um único HTML (`index.html`) com 4 **views** alternadas por JS (`show(id)`),
barra de navegação fixa no topo + rodapé com os 4 domínios.

| View | id | Conteúdo |
|---|---|---|
| Empresa | `view-empresa` | Hero + duas frentes (Labs/Consulting) + casos reais + consultoria |
| Blu | `view-blu` | Landing do produto Blu (dark navy + roxo) |
| Formly | `view-formly` | Landing do produto Formly (wine/pine/paper) |
| Brain | `view-brain` | Landing do produto Brain MCP + login |

### Navegação (hubbar)
- Sticky top, fundo `rgba(242,242,240,.92)` + blur, borda inferior hairline.
- Brand: `Deep <span class="ser">Blue</span>` (Instrument Serif itálico).
- Links: Empresa · Blu · Formly · Brain. Ativo = pill azul (`--db-ac`).
- Botões de view usam `onclick="show('id')"`, nunca âncora real.

## 4. View EMPRESA (landing da empresa — identidade Soft A)

Tokens Soft A (canônicos do site Deep Blue, v3-soft-a):
- Canvas `#F2F2F0` · Ink `#101828` · Muted `#5B6472` · Accent `#1D4ED8` · Accent2 `#60A5FA` · Line `#E2E4E0`
- Display: Plus Jakarta Sans · Display serif itálico: Instrument Serif
- Sem kickers de seção no site real (começa direto no título); no hub, kicker
  mono uppercase é aceito para navegação interna.

### 4.1 Hero
- `h1`: "Sua operação já funciona.<br>Nossas ferramentas de IA fazem ela <span class="soft">render mais.</span>"
  - `clamp(34px,3.9vw,50px)`, `max-width:26ch`, `<br>` explícito entre as 2 frases → 3 linhas.
  - `span.soft`: Instrument Serif itálico, `color:var(--db-ac)`.
- Sub: "A Deep Blue ajuda empresas a usar inteligência artificial como ferramenta de negócio. Entregamos sistemas que agregam valor, com resultado mensurável."
- CTAs: `Conhecer os produtos` (primário, → `show('blu')`) · `Ver o Brain MCP` (secundário → `show('brain')`).

### 4.2 Blocos alternados (zig-zag esquerda/direita)
Os blocos da landing alternam o alinhamento (`margin-left/right:auto` no `.in` de
cada `.blk`), criando um ritmo editorial:
- **Hero** → esquerda
- **Duas frentes** (Labs + Consulting) → **direita** (`blk r`)
- **Casos reais** (logos) → **esquerda** (`blk l`)
- **Consultoria** (CTA final) → **direita** (`blk r`)

Cada `.blk` tem `.in` com `max-width:640px`; o `.bento2` e a `.clients` esticam
até 720px dentro do bloco.

### 4.3 Duas frentes (seção central — a decisão de produto)
- Título: "Duas frentes, um objetivo." (com `em` serif itálico azul em "um objetivo").
- Sub: "Produtos em assinatura para quem quer começar rápido. Consultoria para quem precisa de diagnóstico e estratégia sob medida. Os produtos que desenvolvemos são a prova do que entregamos."
- **Card Labs** (claro, expansível):
  - Tag: `Labs · assinatura` · Título: Deep Blue Labs · Sub: "Ferramentas de IA prontas para usar. Desenvolvemos produtos completos — e eles estão aqui para você ver."
  - Expandir → lista de 3 produtos (`.prow`), cada um com ícone, nome, descrição 1 linha, CTA **"Abrir produto"** com `arrow-up-right`:
    - Blu (gradiente `#7E5CC8→#3A80D4`) → `show('blu')`
    - Formly (`#7A2E3F`) → `show('formly')`
    - Brain MCP (`#1D4ED8`) → `show('brain')`
- **Card Consulting** (escuro `#101828`, expansível):
  - Tag: `Consulting · escopo fechado` · Título: Deep Blue Consulting
  - Expandir → 3 itens (`.crow`): AI Assessment, Transformation Roadmap, Advisory Retainer (mesma copy do Soft A).
- Interação: `toggleSvc(el)` — cada card abre/fecha independente (`classList.toggle('open')`), "+" rotaciona 45°.

### 4.4 Casos reais (strip de logos — padrão antigo)
- Kicker: `Quem confia` · Título: "Casos reais."
- Sub: "Projetos que entregamos, com resultado mensurável. Cada logo abre a história do projeto."
- Label acima da strip: `Com quem já trabalhamos` (mono uppercase, como o Soft A).
- **Strip de logos** (`.client-badge`): SENAC (SVG wikimedia), Cladtek (site oficial), Bloqüo (logo-white.svg), Templo (logo_templo_header.png, abre o site externo), Rastro (webflow logo).
  - Regra visual: logo `grayscale(1)` + `opacity:.72`; hover → cor + opacidade 1 + borda azul + seta `arrow-up-right`.
  - Fallback: se a imagem não carrega, `onerror` troca por texto bold (`SENAC`, `CLADTEK`...).
  - **Clique**: placeholder "Em breve: página do projeto X" até existirem as páginas de projeto; depois, cada badge navega para a página do projeto correspondente.

### 4.5 Consultoria (CTA final)
- Kicker: `Consultoria` · Título: "Antes da tecnologia, o diagnóstico."
- Parágrafo da voz Deep Blue (começa com pessoas, IA como ferramenta do diagnóstico).
- CTA secundário: "Agendar um diagnóstico" (sem destino real — placeholder).

## 5. View BLU (produto — identidade Blu)

Tokens Blu (canônicos do app):
- Fundo `#03071C` · Texto `#eef0f8` · Accent `#8C5FDB` · Accent-hi `#a98be8` · Glass `rgba(255,255,255,.055)` + blur(16px) + borda `rgba(255,255,255,.10)`
- Inter + JetBrains Mono (números) · Phosphor · **emoji proibido** · pt-BR "você"

Seções:
- **Barra**: brand Blu + CTA primário "Entrar no app" → `https://app.bluapp.ink` (nova aba).
- **Hero 2 col** (`1.1fr .9fr`):
  - `h1`: "Seu escritório virtual,<br>com <span class="g">agentes de IA</span> trabalhando." (gradiente `#a98be8→#7ec3ff` no span).
  - Sub: modelo de decisão (IA prepara → humano aprova → agente executa).
  - CTAs: "Entrar no app" (→ app.bluapp.ink) · "Ver planos" (placeholder).
  - Mock glass à direita: 4 linhas (Clientes 128 · Decisões pendentes 7 · Rotinas ativas 12 · Receita mês R$ 154k) com dots de status.
- **Features** (3 cards glass): Salas com agentes · IA prepara, você aprova · Rotinas automáticas.

## 6. View FORMLY (produto — identidade Formly)

Tokens Formly (canônicos do app — NÃO é Blu):
- Paper `#E7E6E0` · Card `#FCFBF8` · Wine `#7A2E3F` · Wine-dark `#5C1E2C` · Pine `#3B5B52` · Muted `#6E6D66` · Line `#C9C7BE`
- Helvetica Neue (display) · Georgia (body) · SF Mono (labels)
- **Emoji permitido** (🎙️ é do DNA do Formly).

Seções:
- **Barra**: brand `formly.` + CTA "Abrir produto" → `https://formly-web-xkndgpat3q-rj.a.run.app/` (nova aba).
- **Hero central**: "Precisa de um questionário?" (wine itálico) + sub 1 frase.
- **Caixa de pergunta** (o clássico): input "Me fala qual, ou grave um áudio..." + botão microfone (🎙️) + botão "Criar" → abre o produto real.
- **3 cards**: Áudio nativo · IA gera · Análise (badges mono uppercase, copy do wireframe).

## 7. View BRAIN (produto — identidade Brain MCP)

Tokens: herda o dark navy do Blu + marca própria:
- Brand: `ph-brain` + "Brain MCP" + **by DeepBlue** (logo círculos concêntricos SVG, gradiente `#1D4ED8→#60A5FA`) na barra.
- 4 paletas disponíveis (dark canônico no hub; azul/mono/warm nos protótipos).

Seções:
- **Barra**: brand Brain MCP + by DeepBlue + CTA "Entrar no app" → `https://app.mcp-brain.com` (nova aba).
- **Hero 2 col**: "Sua empresa vira um <span class="g">conector MCP</span>." + sub (URL MCP, corpus curado + memória viva, com fontes e citações). CTA "Criar conta" → app real.
  - Mock glass à direita: POL-042 publicado · PRO-117 em aprovação · Q&A via Claude (com citações).
- **3 passos**: 01 Conecte a URL MCP · 02 Suba políticas e documentos (curadoria, extração depois da aprovação) · 03 O time pergunta no Claude.
- **Login** (card glass, `max-width:420px`): título "Entrar no Brain MCP" + Google (logo SVG) → app real + "ou" + input e-mail + "Entrar com e-mail" → app real.

## 8. Rodapé (todas as views)

- Brand Deep Blue + 4 links de domínio (Empresa→deepblue.company, Blu→bluapp.ink, Formly→formly.ink, Brain→mcp-brain.com) — no hub, os links de produto abrem a view correspondente.

## 9. Regras inegociáveis

1. **Emoji proibido no hub** (empresa, Blu, Brain) — Phosphor icons. Única exceção: view Formly (🎙️ é identidade do produto).
2. **CTA de produto abre o produto real** em nova aba — nunca tela de demo interna.
3. **Fontes**: Plus Jakarta Sans + Instrument Serif (empresa), Inter + JetBrains Mono (Blu/Brain), Helvetica Neue + Georgia + SF Mono (Formly). Nunca misturar.
4. **Mono** (`tabular-nums`) em todo número, ID, timestamp.
5. **pt-BR**, tom direto, "você", frases curtas, verbo primeiro.
6. Modelo de decisão do Blu: IA prepara → humano aprova → agente executa (copy do produto).
7. `h1` do hero da empresa: `clamp(34px,3.9vw,50px)` + `max-width:26ch` + `<br>` — medir `h1Lines` no QA (máx 3).
8. Contraste AA nos temas claros (não usar `--mu` <12px nos cards de texto).

## 10. Status de entrega (revisão #200, 17/08/2026 — atualizada 18/08 pós-finalização)

| Item da spec | Entregue | Status |
|---|---|---|
| Login embutido na landing do Brain (card glass: Google + e-mail) | ✅ card glass com links reais para `app.mcp-brain.com` (sem fakes) | ✅ finalizado |
| CTA "Entrar no app" → `app.mcp-brain.com` | ✅ | ✅ |
| Elementos gráficos Labs e Consulting uniformes | ✅ mesmo componente `.prow`/`.crow` | ✅ |
| Logo real Deep Blue (círculos + wordmark) na barra e rodapé | ✅ referência Soft A (SVG 28px + serif wordmark) | ✅ |
| Nav Empresa/Blu/Formly/Brain removida; chips das marcas Blu + Formly no canto superior direito | ✅ chips → `show('blu')`/`show('formly')` | ✅ |
| Chips Blu/Formly removidos da barra (decisão 18/08 pós-preview) | ✅ barra só com o logo | ✅ |
| Botão "Ver o Brain MCP" no hero removido (decisão 18/08) | ✅ só CTA primário "Conhecer os produtos" | ✅ |
| Cards Labs e Consulting com mesmo tamanho ao expandir | ✅ estrutura fixa (t-sub min-height + span line-clamp 2) | ✅ |
| Expansão INDEPENDENTE dos cards (clique num não expande o outro) | ✅ `align-items:start` — QA: clicar Labs → Labs 457, Consulting 154; ambos abertos → 457=457 | ✅ |
| Cladtek visível no strip | ✅ trocado para wordmark 2025 (o PNG 2022 era 100% transparente) + `brightness(0)` | ✅ |
| Drawers de caso (sem `alert()`) | ✅ portados do Soft A (pf1/pf2/pf4 + pf-rastro); Templo abre site externo | ✅ |
| Botão de áudio no diagnóstico (Groq Whisper) | ✅ frontend no hub + serviço `brand-hub-voice` no monorepo (PENDENTE deploy) | ⚠️ aguarda deploy |
| Quadro de mensagem "Me conta aqui, com as suas palavras" no diagnóstico | ✅ substitui áudio + e-mail: textarea + Enviar → `POST /api/message` (backend testado local: 200 ok, 400 vazio) | ✅ (backend aguarda deploy) |
| Marcadores de protótipo removidos (.note, título interno, alerts) | ✅ | ✅ |
| SEO: title/meta/OG/canonical/favicon/theme-color | ✅ | ✅ |
| CTAs reais: Formly → `formly.ink`, Brain → `app.mcp-brain.com`, email `contato@deepblue.company` | ✅ | ✅ |
| `app.bluapp.ink` resolvendo | ❌ DNS do Blu pendente (CNAME no Namecheap) | ⚠️ aguarda infra |

Regra da uniformidade: **Labs e Consulting usam o MESMO componente de linha**
(ícone em quadrado 40px + título bold + descrição 12px + borda + radius 14px).
A única diferença: Labs tem CTA "Abrir produto" (navega), Consulting não
(serviço, sem destino). Nunca desenhar um como card e outro como lista solta.

## 11. QA (checklist pós-edição)

```js
(() => { const r = {};
  r.hOverflow = document.documentElement.scrollWidth > window.innerWidth;
  r.h1Lines = Math.round(document.querySelector('#view-empresa h1').getBoundingClientRect().height / parseFloat(getComputedStyle(document.querySelector('#view-empresa h1')).lineHeight));
  r.phosphor = getComputedStyle(document.querySelector('.chip i')).fontFamily;
  ['blu','formly','brain'].forEach(v => { show(v); r[v] = document.getElementById('view-'+v).classList.contains('on'); });
  show('empresa');
  return JSON.stringify(r); })()
```
- [x] hOverflow false · h1Lines ≤ 3 · Phosphor carregado · 4 views alternam
- [x] Labs expande com 3 `.prow` ("Abrir produto") · Consulting expande com 3 `.crow` — **alturas iguais ao expandir** (desktop e mobile; medir via `getBoundingClientRect` com `.open` nos dois)
- [x] Todos os CTAs de produto têm `href` real (`app.bluapp.ink`, `formly.ink`, `app.mcp-brain.com`) e `target="_blank"` (quando saem do hub)
- [x] Logo real (SVG círculos + wordmark) na barra e rodapé; sem chips, sem nav Empresa/Blu/Formly/Brain
- [x] Drawers de caso abrem sem `alert()`; Cladtek usa wordmark 2025 + `brightness(0)` (o PNG 2022 é transparente)
- [x] Expansão independente: clicar num card não expande o outro (`align-items:start`); ambos abertos ficam iguais
- [x] Quadro de mensagem: textarea → POST `API_BASE/api/message` → estados enviando/ok/err
- [x] Preview: `http://100.69.231.7:8899/brand-hub/` (servidor local em projetos-repo/design/brand-hub)

## 11b. Serviço brand-hub-voice (mensagens/áudio do site)

- Local: `monorepo/produtos/brand-hub-voice/` (FastAPI + Dockerfile + README).
- Endpoints: `POST /api/message` {text} → e-mail (usado pelo hub); `POST /api/voice`
  → Groq Whisper (mantido, sem frontend por ora).
- Deploy: `make brand-hub-voice-deploy` (requer secrets `GROQ_API_KEY`, `SMTP_USER`,
  `SMTP_PASS` no Secret Manager; ver README do serviço).
- Frontend: constante `API_BASE` no `index.html` — atualizar se a URL do Cloud Run mudar.
- Testado local: `/health` ok, `/api/message` 200 ok + 400 vazio, `/api/voice` chega
  à Groq (falhou só na autenticação porque a chave na EC2 é placeholder).

## 12. Fora de escopo (v1)

- Páginas de planos/preços reais dos produtos (placeholder "Ver planos")
- Formulário de diagnóstico funcional (CTA placeholder)
- E-mail de contato, LGPD/termos, analytics, SEO
- Versão EN
- Separação em arquivos por domínio (v2: um HTML por produto, servido em cada domínio)

## 13. Próximos passos

1. ✅ Comprar domínios (18/08): `deepblue.company` + `mcp-brain.com` (Cloudflare), `formly.ink` (Namecheap)
2. Deploy do hub `deepblue.company` (Cloud Run estático — decidir Cloud Run vs S3+CloudFront)
3. Deploy do Formly no `formly.ink` (custom domain no Cloud Run)
4. Deploy do Brain no `mcp-brain.com` (custom domain no auth-service)
5. E-mail corporativo (Zoho grátis / Google Workspace / Cloudflare Routing)
6. ✅ Domínio do Blu comprado (18/08): `bluapp.ink` (Namecheap)
7. V2: separar as views em páginas reais por domínio
