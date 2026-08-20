# 📚 Biblioteca (Business Memory) — Requisitos Blue V3

> Última atualização: 2026-07-30
> Status: 🟡 Em andamento
> Fonte: `apps/blu_web/src/pages/app/BusinessMemoryPage.tsx` (397 linhas)

---

## 1. Visão Geral

**Objetivo:** Visualizar e auditar a memória de negócio (knowledge graph) construída pelos agentes ao longo do tempo.

**Contexto:** Todos os agentes produzem entidades armazenadas na Business Memory. Esta página permite auditar, buscar e entender o que a IA sabe sobre a empresa.

**Relação com outras páginas:**
- **Estratégia:** documentos da aba Conhecimento alimentam a memória
- **Home:** indicadores de confiança são visíveis aqui

---

## 2. Estrutura de Elementos (Front-End)

### 2.1 Header da página
- **Tipo:** barra de título
- **Conteúdo/Dados:** ícone + "Business Memory" + subtítulo

### 2.2 Filtros
- **Tipo:** dropdown de filtro
- **Conteúdo/Dados:** entity_type: Todos, Snapshot, Rotina, Skill, Resultado de Agente
- **Interações:** selecionar tipo filtra a lista

### 2.3 Lista de Records (expansível)
- **Tipo:** tabela expansível
- **Conteúdo/Dados:** cada record:
  - Entity Type (badge colorido: snapshot=roxo, routine=verde, skill=azul, agent_result=laranja)
  - Entity Name
  - Key (identificador único)
  - Confidence (0-100%: verde≥90%, amarelo≥70%, vermelho<70%)
  - Created/Updated At
  - Content preview (truncado)
- **Interações:** expandir para ver detalhes completos
- **Estados visuais:** linha expandida com grid 2 colunas (labels+valores)

---

## 3. Fluxos de Processo

### 3.1 Auditoria de Memória
```
Usuário acessa Biblioteca → vê lista de records
  │
  ├─ Filtra por tipo (ex: "Snapshot")
  ├─ Expande registro para ver conteúdo completo
  └─ Recolhe e continua navegando
```

---

## 4. Regras de Negócio

| # | Regra |
|---|---|
| R1 | Entity types: snapshot, routine, skill, agent_result |
| R2 | Confidence 0-1 exibido como % com cor semântica |
| R3 | Registros são imutáveis nesta tela (somente leitura) |
| R4 | Conteúdo truncado na lista (expandir para ver completo) |

---

## 5. Integrações

| Integração | Tipo | Descrição |
|---|---|---|
| useBusinessMemory | Hook/Query | Lista de records da Business Memory |

---

## 6. Cenários de Teste

### Happy Path
- [ ] Ver lista de records com badges coloridos por tipo
- [ ] Filtrar por entity type
- [ ] Expandir registro para ver conteúdo completo

### Edge Cases
- [ ] Nenhum registro → estado vazio
- [ ] Registro com conteúdo muito longo
- [ ] Confidence nulo (exibe "—")
