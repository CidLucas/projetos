# 📋 Requisitos Blue V3 — Índice de Páginas

> Documento vivo. Cada página do Blue V3 tem seu próprio arquivo de requisitos.
> Atualizado conforme as conversas com o fundador.

---

## 🗂 Páginas

| # | Página | Arquivo | Status |
|---|---|---|---|
| 00 | Landing Page | [landing.md](./landing.md) | 🔴 Pendente |
| 01 | Onboarding — Step 1 | [onboarding-01.md](./onboarding-01.md) | 🔴 Pendente |
| 02 | Onboarding — Step 2 | [onboarding-02.md](./onboarding-02.md) | 🔴 Pendente |
| 03 | Onboarding — Step 3+ | [onboarding-03.md](./onboarding-03.md) | 🔴 Pendente |
| 10 | Chat (Agentes) | [chat.md](./chat.md) | 🔴 Pendente |
| 20 | Documentos | [documentos.md](./documentos.md) | 🟡 Em andamento |
| 30 | Estratégia | [estrategia.md](./estrategia.md) | 🔴 Pendente |
| 40 | Conhecimento | [conhecimento.md](./conhecimento.md) | 🔴 Pendente |
| 50 | Configurações | [configuracoes.md](./configuracoes.md) | 🔴 Pendente |

---

## 📐 Template de documento de página

Cada arquivo segue esta estrutura:

1. **Visão Geral** — objetivo, contexto, relação com outras páginas
2. **Estrutura de Elementos (Front-End)** — um subtópico por elemento da UI
3. **Fluxos de Processo** — criação, edição, exclusão, transições de estado
4. **Regras de Negócio** — validações, permissões, restrições
5. **Integrações** — APIs, eventos, websockets
6. **Cenários de Teste** — happy path + edge cases

### Subtemplate de elemento de UI

```
### 2.X [Nome do Elemento]
- **Tipo:** tab | botão | card | lista | modal | formulário | sidebar | barra inferior
- **Posição:** topo / lateral esquerda / conteúdo central / barra inferior
- **Conteúdo/Dados:** o que está representado e de onde vem
- **Interações:** clicar, arrastar, preencher, expandir...
- **Estados visuais:** loading, vazio, erro, desabilitado
- **Condições de visibilidade:** quando aparece/esconde
```

---

## 🔄 Como alimentar este documento

- O fundador descreve uma página → Hermes preenche as 6 seções
- O fundador detalha um elemento → Hermes adiciona na seção 2
- O fundador descreve um fluxo → Hermes adiciona na seção 3
- Sempre que uma regra de negócio surgir → Hermes registra na seção 4
