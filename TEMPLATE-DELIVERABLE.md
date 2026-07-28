# 📦 Template de Entrega (Deliverable)

> Use este template para **todo artefato** que um profile Hermes produzir.
> Cada entrega deve ter pelo menos: canal, formato, e link.

## Metadados Obrigatórios

| Campo | Exemplo |
|-------|---------|
| **Profile** | `triage`, `writer`, `researcher`, `reviewer` |
| **Projeto** | `plataforma-blu`, `agente-bloquo` |
| **Tipo** | `doc`, `planilha`, `apresentacao`, `preview`, `codigo`, `relatorio` |
| **Data** | `2026-07-28` |
| **Status** | `rascunho` → `revisao` → `entregue` |

## Regras de Canal

| Tipo de Artefato | Canal Padrão | Formato | Exemplo |
|---|---|---|---|
| Documentação técnica, specs, ADRs, status | **GitHub** → `projetos/<projeto>/docs/` | Markdown | `docs/05-api.md` |
| Cronogramas, planilhas, orçamentos | **Google Drive** → `Hermes - Entregáveis/<projeto>/` | Sheets (.gsheet) | Link compartilhável |
| Apresentações para cliente | **Google Drive** → `Hermes - Entregáveis/Apresentações/` | Slides (.gslides) | Link compartilhável |
| HTML previews, dashboards, protótipos | **EC2 via Tailscale** → `http://100.69.231.7:8081/<projeto>/` | HTML | URL Tailscale |
| Código, migrações, scripts | **GitHub** → repo de código do projeto | Pull Request | PR link |
| Relatórios curtos, briefings | **Telegram** + commit no GitHub | Markdown | Mensagem + commit |

## Estrutura de Arquivo (Markdown)

```markdown
# [Título do Documento]

**Profile:** [nome]
**Projeto:** [slug]
**Data:** YYYY-MM-DD
**Tipo:** [doc / spec / relatorio / decision]

---

## Objetivo

[1 parágrafo do que é este documento]

## Conteúdo

[...]

## Próximos passos

- [ ] Ação 1
- [ ] Ação 2
```

## Checklist de Entrega

- [ ] Metadados preenchidos (profile, projeto, tipo, data)
- [ ] Canal correto (GitHub / Drive / EC2 / conversa)
- [ ] Link registrado no `STATUS.md` do projeto (se relevante)
- [ ] Versão final revisada
