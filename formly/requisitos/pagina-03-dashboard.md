# 📊 Página 03 — Dashboard de Resultados

> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)

---

## 1. Visão Geral

Dashboard onde o criador visualiza as respostas coletadas. Exibe dados agregados por pergunta, permite filtrar e exportar. Na Fase 4, inclui relatórios de IA com insights automáticos.

### Layout

```
┌──────────────────────────────────────────────────────────┐
│ ← Meus Questionários    Pesquisa de Satisfação           │
│ 12 respostas · Publicado há 3 dias                       │
├──────────────────────────────────────────────────────────┤
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐ │
│ │ 12       │ │ 85%      │ │ 4.2/5    │ │ 3:42         │ │
│ │ Respostas│ │ Conclusão│ │ Nota média│ │ Tempo médio  │ │
│ └──────────┘ └──────────┘ └──────────┘ └──────────────┘ │
├──────────────────────────────────────────────────────────┤
│ Filtros: [Período ▾] [Pergunta ▾]   [Exportar CSV ▾]    │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  1. ⭐ Satisfação geral                                  │
│  ┌──────────────────────────────────────────────────┐    │
│  │ 5 ★★★★★   ████████████████████████  8 (67%)     │    │
│  │ 4 ★★★★    ████████                  3 (25%)     │    │
│  │ 3 ★★★     ██                        1 (8%)      │    │
│  │ 2 ★★      │                         0           │    │
│  │ 1 ★       │                         0           │    │
│  └──────────────────────────────────────────────────┘    │
│                                                          │
│  2. 📄 Sugestões de melhoria                             │
│  ┌──────────────────────────────────────────────────┐    │
│  │ "Mais opções de comida vegana" — 3 menções  🔗    │    │
│  │ "Ar condicionado muito forte" — 2 menções   🔗   │    │
│  │ "Excelente organização" — 1 menção           🔗   │    │
│  └──────────────────────────────────────────────────┘    │
│                                                          │
│  3. 🎤 Comentário livre (áudio)                          │
│  ┌──────────────────────────────────────────────────┐    │
│  │ 🎤 Transcrição 1 — 0:42                     ▶    │    │
│  │ "Achei o evento muito bem organizado..."          │    │
│  │ 🎤 Transcrição 2 — 1:15                     ▶    │    │
│  │ "Sugiro que na próxima tenham mais..."            │    │
│  └──────────────────────────────────────────────────┘    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## 2. Estrutura de Elementos

### 2.1 Header

| Elemento | Tipo | Detalhes |
|---|---|---|
| Breadcrumb | link | ← Meus Questionários |
| Título | texto | Nome da pesquisa |
| Meta | texto | "12 respostas · Publicado há 3 dias" |
| Status | badge | Ativo (verde) / Pausado (amarelo) / Encerrado (cinza) |
| Botão Editar | btn outline | Volta ao builder |
| Botão Pausar/Reabrir | btn | Pausa coleta de respostas |
| Botão Compartilhar | btn outline | Abre modal de link/QR code |

### 2.2 Cards de Métricas (KPI row)

| Card | Métrica | Cálculo |
|---|---|---|
| Respostas | Total | Contagem de submissões completas |
| Conclusão | % | Respostas completas / (completas + parciais) |
| Nota média | Número | Média das perguntas de escala (se houver) |
| Tempo médio | Minutos | Tempo mediano de resposta |

### 2.3 Filtros

| Elemento | Tipo | Detalhes |
|---|---|---|
| Período | date range picker | "Últimos 7 dias", "30 dias", "Tudo", personalizado |
| Pergunta | select | "Todas as perguntas" ou específica |
| Status da resposta | select | "Completas", "Parciais", "Todas" |
| Exportar | dropdown btn | CSV, PDF, Excel |

### 2.4 Visualizações por tipo de pergunta

**⭐ Escala (gráfico de barras horizontais):**
| Elemento | Tipo | Detalhes |
|---|---|---|
| Barra de distribuição | bar chart | Uma linha por valor da escala |
| Barra | div com width % | Cor gradiente (1=vermelho → 5=verde) |
| Contagem | número | Total de respostas por valor |
| Porcentagem | % | Ex: "8 (67%)" |

**☑️ Múltipla escolha (gráfico de barras):**
| Elemento | Tipo | Detalhes |
|---|---|---|
| Barra por opção | bar chart | Uma linha por opção |
| Barra | div com width % | Cor do tema |
| Contagem | número + % | Ex: "15 (63%)" |

**📝 Texto curto / 📄 Parágrafo (nuvem de temas):**
| Elemento | Tipo | Detalhes |
|---|---|---|
| Tema/tópico | chip/tag | Agrupamento automático (IA) |
| Contagem | badge | "3 menções" |
| Link | btn 🔗 | "Ver todas as respostas" → expande lista |
| Lista completa | expansível | Mostra todas as respostas individuais |

**🎤 Áudio (lista de transcrições):**
| Elemento | Tipo | Detalhes |
|---|---|---|
| Item da lista | card | Ícone 🎤 + duração + transcrição + player ▶ |
| Player de áudio | controle | Ouvir áudio original |
| Transcrição | texto | Texto completo da transcrição |
| Expandir | btn | Ver transcrição completa se truncada |

**📎 Upload (galeria de arquivos):**
| Elemento | Tipo | Detalhes |
|---|---|---|
| Grid de arquivos | miniaturas | Preview de imagens, ícones para PDF/DOCX |
| Nome do arquivo | texto | Nome original |
| Download | btn | Baixar arquivo original |

### 2.5 Visualização por respondente (linha do tempo)

| Elemento | Tipo | Detalhes |
|---|---|---|
| Lista de respondentes | tabela/lista | Um por linha |
| Row do respondente | expansível | ID anônimo + data/hora + duração |
| Expandir | painel | Mostra todas as respostas daquele respondente |

### 2.6 Exportação

| Elemento | Tipo | Detalhes |
|---|---|---|
| Dropdown Exportar | btn + menu | CSV, PDF, Excel |
| Modal de exportação | modal | Opções: incluir transcrições, incluir áudios, período |
| Download | btn | Gera e baixa arquivo |

---

## 3. Fluxos de Processo

### 3.1 Acessar dashboard

```
1. Criador acessa "Meus Questionários"
2. Clica na pesquisa → dashboard abre
3. Cards de métricas carregam
4. Visualizações por pergunta renderizam
```

### 3.2 Filtrar resultados

```
1. Criador seleciona período "Últimos 7 dias"
   → Todas as visualizações se atualizam
2. Criador seleciona pergunta específica
   → Dashboard mostra só aquela pergunta
3. Criador limpa filtros → volta ao padrão (tudo, 30 dias)
```

### 3.3 Exportar

```
1. Criador clica Exportar → CSV
2. Período selecionado é aplicado ao export
3. CSV gerado com:
   - Colunas: ID respondente, data, pergunta, tipo, resposta, transcrição
4. Download inicia
```

### 3.4 Pausar / Reabrir questionário

```
1. Criador clica "Pausar"
   → Link público mostra "Pesquisa encerrada"
   → Respostas já coletadas permanecem
2. Criador clica "Reabrir"
   → Link volta a funcionar
```

---

## 4. Regras de Negócio

### Métricas

- Respostas: só conta submissões completas (chegaram na tela de agradecimento)
- Conclusão: respostas completas / (completas + parciais)
- Nota média: calculada sobre perguntas de escala (soma dos valores / total de respostas)
- Tempo médio: mediana dos tempos de resposta (evita outliers de quem deixou aberto)
- Parciais: respondentes que começaram mas não enviaram (expira em 7 dias)

### Agregação de texto

- Fase 1: lista simples de respostas, agrupada manualmente
- Fase 4: IA categoriza e agrupa temas similares automaticamente

### Privacidade

- Respondentes são anônimos por padrão
- Criador vê "Respondente #1", "Respondente #2"
- Se criador adicionou pergunta de identificação (nome, e-mail), esses dados aparecem
- Dados não são compartilhados entre questionários

### Retenção

- Dados de respostas: retidos enquanto o questionário existir
- Áudios: armazenados no S3 com política de ciclo de vida (90 dias free, depois archive)
- Questionário excluído → todos os dados são deletados (GDPR/LGPD)

---

## 5. Integrações

| Elemento | Integração | Status |
|---|---|---|
| Carregar métricas | GET /api/surveys/:id/stats | A construir |
| Carregar respostas | GET /api/surveys/:id/responses?page=&filters= | A construir |
| Pausar/Reabrir | PATCH /api/surveys/:id/status | A construir |
| Exportar CSV | GET /api/surveys/:id/export?format=csv | A construir |
| Download áudios | S3 presigned GET URL | A construir |
| Análise IA | POST /api/surveys/:id/analyze (Fase 4) | Fase 4 |

---

## 6. Cenários de Teste

### Métricas
- [ ] 0 respostas → cards mostram 0, 0%, —, —
- [ ] 12 respostas → cards atualizados corretamente
- [ ] Resposta parcial → não conta em "Respostas", conta em "Conclusão"
- [ ] Pergunta de escala → nota média calculada corretamente

### Visualizações
- [ ] Escala: gráfico de barras com distribuição correta
- [ ] Múltipla escolha: cada opção com contagem e %
- [ ] Texto/parágrafo: lista de respostas individuais
- [ ] Áudio: transcrição visível + player funciona
- [ ] Upload: preview de imagem, download de PDF

### Filtros
- [ ] Período "Últimos 7 dias" → só mostra respostas dessa janela
- [ ] Período "30 dias" → amplia janela
- [ ] Filtrar por pergunta específica → só aquela pergunta aparece
- [ ] Limpar filtros → volta ao padrão

### Exportação
- [ ] CSV: colunas corretas, dados completos
- [ ] CSV: transcrições incluídas quando checkbox marcado
- [ ] Período selecionado afeta export

### Ações
- [ ] Pausar → link mostra "Pesquisa encerrada"
- [ ] Reabrir → link volta a funcionar
- [ ] Editar → volta ao builder com dados do questionário
