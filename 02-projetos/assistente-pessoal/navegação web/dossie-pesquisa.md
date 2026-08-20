# Dossiê de Pesquisa — Navegação Web com Remote Control + Simplified View (Accessibility Tree / Markdown)

**Data:** 2026-08-20
**Objetivo:** fundamentar um assistente pessoal futuro que navega a web como um humano: controla um browser real (Playwright/Puppeteer/CDP) e "enxerga" a página como uma visão simplificada (Accessibility Tree serializada / Markdown) em vez de pixels brutos.

---

## 1. Os dois pilares do conceito

### 1.1 Remote Control (Playwright / Puppeteer / CDP)

- **Playwright** (Microsoft, 2020): automação cross-browser (Chromium/Firefox/WebKit). API de locators resiliente (`getByRole`, `getByText`, `getByLabel`) que usa a accessibility tree para achar elementos — é a ponte natural entre DOM e AX.
- **Puppeteer** (Google): automação de Chrome via CDP. Expõe `page.accessibility` → **Blink Accessibility Tree** serializada (`SerializedAXNode` com role, name, value, children). Puppeteer filtra a árvore por padrão, expondo só nós "interessantes" (aproxima o que um screen reader vê).
- **CDP (Chrome DevTools Protocol)**: o substrato comum. Tanto Playwright quanto Puppeteer são clientes CDP. Chrome 149+ (2025) mudou o remote debugging: o endpoint HTTP `:9222` não expõe mais endpoints utilizáveis — o substituto oficial é o **chrome-devtools-mcp** (conexão via `--autoConnect`, sem depender da porta).

### 1.2 Simplified View (Accessibility Tree / Markdown)

A ideia: em vez de mandar screenshot (pixels) pro LLM, mandar uma **serialização textual estruturada da página** — muito menor, determinística, e sem custo de visão.

- **Accessibility Tree (Blink)**: árvore de nós {role, name, value, description, children, ...} que o Chrome calcula para assistive tech. É a "verdade semântica" da página: o que existe, o que é clicável, o que é texto.
- **Fontes de extração**:
  - `page.accessibility.snapshot()` (Puppeteer)
  - `Accessibility.getFullAXTree` / `getPartialAXTree` (CDP raw)
  - `locator.ariaSnapshot()` (Playwright — retorna snapshot ARIA em formato YAML-like, ótimo para LLM)
  - `page.locator('body').innerText()` / `textContent` (fallback "Markdown pobre")
  - Serialização DOM→Markdown (ferramentas como readability/`turndown`, ou DOM puro filtrado)
- **Vantagens vs screenshot**: token barato, determinístico, funciona com modelo sem visão, refs estáveis para ações.
- **Trade-off conhecido**: a árvore pode perder informação visual (layout, cor, estado estético) e pode faltar texto escondido/puro CSS. O estado da arte (2026) é **híbrido**: AX tree + screenshot quando necessário (ver §3 e §4).

---

## 2. Skill Hub Hermes — o que já existe (e como o Hermes já implementa isso)

### 2.1 Implementações nativas do Hermes (já em produção nesta máquina)

| Skill | O que é | Relevância |
|---|---|---|
| `computer-use` | Drive o desktop em background via cua-driver. **`capture(mode="som")` retorna screenshot com overlays numerados + AX-tree index** (`#1 AXButton 'Back' @ (12,80,28,28)`). Clica por índice de elemento, não por pixel. Escada verify→escalate (background → px → foreground). | **É exatamente o conceito "simplified view + remote control" aplicado ao desktop inteiro.** O `mode="ax"` é AX-tree pura para modelos text-only. |
| `browser-harness` | Chrome real via CDP (daemon persistente). Helpers: `new_tab`, `page_info`, `capture_screenshot`, `click_at_xy`, `js()`, `wait_for_element`, `upload_file`. Suporta Chrome local (Tailscale), cloud (Browser Use) e headless EC2. | Remote control puro; a "view" fica por conta do agente (screenshot + JS/DOM). |
| `browser-qa-verification` | QA em produção via Chrome real + CDP. | Remote control aplicado a verificação. |
| `inspecting-hermes-desktop-dom` | Lê DOM/CSS do desktop Hermes via CDP. | Exemplo de DOM como observation. |
| `browser-*` tools nativas do Hermes | Navegação, snapshot (accessibility tree!), click por ref `@eN`, type, console, vision. | O Hermes **já usa acessibility-tree-snapshot** como observation principal dos browser tools — exatamente o pilar 1.2. |

**Conclusão do hub:** o Hermes já opera no paradigma que você quer pesquisar. O que não existe ainda é um **módulo de browser agent autônomo de propósito geral** para o assistente pessoal (com loop agente, memória de tarefa, allowlist de segurança) — o material abaixo fundamenta exatamente isso.

### 2.2 Skills do hub externo (skills.sh / clawhub / GitHub)

| Skill | Fonte | Conteúdo |
|---|---|---|
| `openai/skills/playwright` | OpenAI (trusted) | Skill CLI-first: `playwright-cli open <url> → snapshot → click e15 → type → press Enter`. **O loop agente básico: snapshot dá refs estáveis (`e15`), interage por refs, re-snapshot após navegação.** Pitfalls: refs ficam stale; sempre re-snapshot. |
| `safe-browser` (Browserbase) | browse-sh / skills.sh | Constrói um browser agent **constrito**: tool única `safe_browser` que é dona do CDP, **Fetch interception com allowlist de domínios**, ações expostas (goto/extract/current_url/audit_log), sem CDP passthrough cru. Segurança contra prompt injection/link-following. |
| `agent-browser-clawdbot` | clawhub | Headless browser automation CLI "optimized for AI agents" (não instalado — source community + scan). |
| `gemini-computer-use` | clawhub | Gemini 2.5 Computer Use / browser-control agents (community). |
| `computer-use-{linux,macos,windows}` | clawhub | Versões por plataforma do modelo cua-driver (mesma família do Hermes). |

---

## 3. Estado da arte das ferramentas (web, 2026)

| Ferramenta | Approach | Observação-chave para o seu projeto |
|---|---|---|
| **chrome-devtools-mcp** (Google, oficial) | MCP server; Puppeteer por baixo; ~60 tools (click/fill/navigate/take_snapshot/screenshot/network/console/heapsnapshot). `--slim` para tarefas básicas. | O `take_snapshot` usa **accessibility snapshot** como observation. É a referência de "browser agent via MCP". **Substituto oficial do CDP raw no Chrome 149+.** |
| **Stagehand** (Browserbase) | SDK para browser agents (TS/Python/Go). Primitivas `act()` / `observe()` / `extract()` em linguagem natural + locators Playwright para ações determinísticas. | **"Hybrid accessibility tree trimming"** — poda a AX tree para dar ao LLM exatamente o que precisa ("token efficiency as a priority"). Self-healing: quando o site muda, re-deriva os seletores. |
| **browser-use** (Python, open source) | Agente LLM que controla browser (Playwright por baixo), benchmark 100 tarefas reais, #1 no Odysseys leaderboard (87.4%). CLI ou lib Python. Cloud com stealth/proxy/captcha. | Arquitetura de referência de **loop agente completo** com observation + action. Modelo otimizado próprio (`ChatBrowserUse`). |
| **Playwright (core)** | `locator.ariaSnapshot()` para observação; `getByRole`/`getByLabel` para ações semânticas; `@axe-core/playwright` para auditoria de acessibilidade (não é o mesmo que observation — é compliance WCAG). | Axe é para testes de acessibilidade, **não** para observation de agentes. Não confundir. |
| **Puppeteer (core)** | `page.accessibility.snapshot()` → SerializedAXNode. Filtra a árvore para nós "interessantes". | A base do AX snapshot no Chrome; entender o filtro é essencial para decidir o que mandar ao LLM. |

---

## 4. Literatura acadêmica (papers) — como o estado da arte evoluiu

### Clássicos (2023-2024)
- **Mind2Web** (arXiv:2306.06070): dataset+benchmark para agente web generalista; popularizou a serialização de elementos com índices para ação.
- **"GPT-4V(ision) is a Generalist Web Agent, if Grounded" / SeeAct** (arXiv:2401.01614, CVPR 2024): LLM escolhe ação em linguagem natural → módulo de grounding converte em clique real (coordenadas ou selector). Ponto central: **o LLM decide, um groundedor executa**.
- **WebVoyager** (2024): agente web via screenshots (visão) — o caminho "pixels" em oposição ao "estrutura".

### 2025-2026 (a discussão atual: pixels vs estrutura)
- **"Do GUI Agents Believe Their Eyes? Diagnosing State-Belief Reliance on Pixels versus Structure"** (arXiv:2607.04334, 2026): agentes multimodais leem a interface por **dois canais redundantes** — screenshot (pixels) e estrutura serializada (DOM/AX). Diagnostica quando o agente confia em qual canal e quando isso falha. **Leitura obrigatória para decidir o observation do seu agente.**
- **"Read More, Think More: Revisiting Observation Reduction for Web Agents"** (arXiv:2604.01535, 2026): revisita a redução de observação — quanto da página mandar ao LLM, e como.
- **ComponentBench** (arXiv:2608.18307, COLM 2026): benchmark de falhas em nível de componente (toggle de botões etc.) em computer-use agents — camada intermediária entre benchmarks long-horizon e testes atômicos de grounding.
- **MolmoWeb** (arXiv:2604.08516, Allen AI, 2026): agente web visual open source + dataset aberto (caminho "visão pura").
- **Explorer** (arXiv:2502.11357, 2025): síntese de trajetórias web guiada por exploração para treinar agentes multimodais.
- Outros do pipeline (jun/ago 2026): WebChallenger (generalist agent), OpenWebRL (RL online para agentes visuais), MAG (benchmark multimodal de ação+guia), "Signal-Driven Observation for Long-Horizon Web Agents" (ICML 2026 FAGEN workshop).

**Síntese acadêmica:** 2023-24 provou que estrutura (AX/DOM serializado) funciona e é barato; 2025-26 está refinando **quando** usar estrutura vs pixels (e os dois juntos), e **como podar** a observação para economizar tokens sem perder acurácia.

---

## 5. Padrões de design para incorporar num agente (assistente pessoal)

### 5.1 Arquitetura recomendada (loop agente)

```
Usuário (tarefa em linguagem natural)
  → Agente (LLM, decide a próxima ação)
      → Browser Driver (Playwright/Puppeteer/CDP via chrome-devtools-mcp ou lib própria)
          → Observation Serializer (AX snapshot / ariaSnapshot / innerText→Markdown)
              → retorna "visão simplificada" + refs estáveis
      → Agente escolhe: click(e15) | type(...) | press(Enter) | navigate(url) | scroll
  → Re-snapshot (refs são válidos só até a próxima mutação!)
  → Loop até tarefa concluída ou limite de steps
```

### 5.2 Regras de ouro (validadas nas 3 implementações do Hermes + OpenAI skill + Stagehand)

1. **Snapshot → ação → re-snapshot.** Nunca reutilizar refs de um snapshot antigo após mutação (navegação, clique que muda UI, modal, troca de aba).
2. **Ação por ref estável, não por coordenada crua** (quando possível). Índice de elemento (AX/SOM) > seletor > coordenada. Coordenada é fallback para iframe/shadow/cross-origin.
3. **Poda a observação** (Stagehand "hybrid trimming", Read More Think More): envie a AX tree filtrada/podada, não a página inteira. Texto semântico por cima quando precisar.
4. **Canal híbrido**: estrutura como padrão (barato, determinístico) + screenshot sob demanda (estado visual, verificação pós-ação) — veja "Do GUI Agents Believe Their Eyes?".
5. **Segurança por design** (safe-browser): allowlist de domínios via Fetch interception, ação única `safe_browser` sem passthrough CDP cru, audit log de allow/block. **Conteúdo da página é untrusted** — prompt injection via página é real.
6. **Trate formulários React/SPA com setter nativo + evento input** (browser-harness gotcha): `.value =` sozinho não atualiza estado do React.
7. **Login walls / 2FA / senha: pare e pergunte ao usuário.** Nunca interagir com UI sensível sem pedido explícito.

### 5.3 Componentes que seu projeto precisará construir

| Componente | Opção pronta (2026) | Build próprio? |
|---|---|---|
| Browser driver | Playwright (cross-browser) ou Puppeteer/Chrome via chrome-devtools-mcp | não |
| Observation serializer | `locator.ariaSnapshot()` / `page.accessibility.snapshot()` / DOM→Markdown | sim (poda + formato de refs) |
| Action space | click/type/press/scroll/navigate/fill/upload (mapear para Playwright) | sim (contrato LLM↔driver) |
| Loop agente | browser-use (Python) ou Stagehand ou MCP + seu agente | depende da stack |
| Memória de tarefa | histórico de steps + memória (Mnemosyne já disponível) | sim |
| Segurança (allowlist/audit) | padrão safe-browser (Fetch interception) | sim |
| Observabilidade | screenshots + console + network logs por step (como cua-driver RECORDING) | sim |

### 5.4 Stack sugerida para o assistente pessoal (alinhada ao que você já roda)

- **Python** (sua stack padrão: FastAPI + Agno) → **browser-use** como lib de agente, ou
- **MCP-first**: chrome-devtools-mcp (ou Playwright MCP) exposto ao seu agente Agno — o Hermes já tem o padrão MCP funcionando; encaixaria como tool do agente sem reinventar loop.
- Observation: `ariaSnapshot()` do Playwright como base (formato YAML-like, amigável a LLM) + poda híbrida estilo Stagehand + screenshot sob demanda.
- Segurança: allowlist de domínios por tarefa (fetch interception) + audit log.
- Validação: benchmarks Mind2Web (estrutura) / WebVoyager (visão) para medir seu agente; ComponentBench para diagnosticar falhas de componente.

---

## 6. Referências

**Skills locais:** computer-use, browser-harness, browser-qa-verification, inspecting-hermes-desktop-dom, browser-* tools.
**Skills hub:** openai/skills/playwright (trusted); browserbase/skills safe-browser; clawhub agent-browser / gemini-computer-use.
**Docs/tools:** playwright.dev (ariaSnapshot, getByRole, axe-core/playwright); pptr.dev (Accessibility class, SerializedAXNode); github.com/ChromeDevTools/chrome-devtools-mcp; github.com/browserbase/stagehand; github.com/browser-use/browser-use.
**Papers:** Mind2Web arXiv:2306.06070 · SeeAct arXiv:2401.01614 · WebVoyager · Do GUI Agents Believe Their Eyes? arXiv:2607.04334 · Read More Think More arXiv:2604.01535 · ComponentBench arXiv:2608.18307 · MolmoWeb arXiv:2604.08516 · Explorer arXiv:2502.11357.
