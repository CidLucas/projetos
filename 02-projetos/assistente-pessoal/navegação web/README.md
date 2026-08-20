# 🧭 Navegação Web — Assistente Pessoal

> **Área:** pesquisa para o assistente pessoal
> **Tema:** remote control (Playwright/Puppeteer/CDP) + simplified view (Markdown/Accessibility Tree) aplicados a um agente
> **Data da pesquisa:** 2026-08-20

---

## 📄 Conteúdo

| Arquivo | O que é |
|---|---|
| [dossie-pesquisa.md](./dossie-pesquisa.md) | **Documento principal** — síntese de tudo: conceitos, skill hub, ferramentas, papers, padrões de design, stack sugerida |
| [docs/01-chrome-devtools-mcp.md](./docs/01-chrome-devtools-mcp.md) | README do chrome-devtools-mcp (Google, oficial) — browser agent via MCP, substituto do CDP raw no Chrome 149+ |
| [docs/02-browser-use.md](./docs/02-browser-use.md) | README do browser-use — agente LLM que controla browser, loop completo, benchmark 87.4% Odysseys |
| [docs/03-stagehand.md](./docs/03-stagehand.md) | README do Stagehand (Browserbase) — SDK p/ browser agents, hybrid accessibility tree trimming |
| [docs/04-playwright-accessibility.md](./docs/04-playwright-accessibility.md) | Docs do Playwright — accessibility testing (axe-core; atenção: compliance ≠ observation de agente) |
| [docs/05-puppeteer-api.md](./docs/05-puppeteer-api.md) | API do Puppeteer — classe `Accessibility` (Blink AX tree), SerializedAXNode |
| [docs/06-skill-openai-playwright.md](./docs/06-skill-openai-playwright.md) | Skill oficial OpenAI `playwright` — loop snapshot→refs→click→re-snapshot |
| [docs/07-skill-safe-browser.md](./docs/07-skill-safe-browser.md) | Skill Browserbase `safe-browser` — allowlist de domínios via Fetch interception, segurança anti prompt-injection |

## 🗂 Arquivos brutos (referência intermediária)

Os JSONs de árvore de repositórios usados para localizar os paths das skills (openai-tree.json, bb-tree.json, pw-tree.json) ficam temporários — não são fontes duradouras.

## 🔗 Fontes originais

- Playwright: https://playwright.dev · Puppeteer: https://pptr.dev
- chrome-devtools-mcp: https://github.com/ChromeDevTools/chrome-devtools-mcp
- Stagehand: https://github.com/browserbase/stagehand · browser-use: https://github.com/browser-use/browser-use
- Papers: Mind2Web arXiv:2306.06070 · SeeAct arXiv:2401.01614 · Do GUI Agents Believe Their Eyes? arXiv:2607.04334 · Read More Think More arXiv:2604.01535 · ComponentBench arXiv:2608.18307 · MolmoWeb arXiv:2604.08516
