# 02 — Arquitetura — Coclade Tech

> _A ser preenchido após definição de stack e validação da API Sol de URX._

## 🧱 Stack proposta (inicial)

| Camada | Tecnologia | Por quê |
|---|---|---|
| Ingestão de desenho | API Sol de URX (externa) | conforme requisito do cliente |
| Parser/Extrator | LLM + regras determinísticas | LLM pra entender linguagem natural da spec, regras pra checagens numéricas |
| Comparador | Engine de regras + LLM | regras pra "dimensão X ∈ [a,b]", LLM pra "atende norma Y?" |
| Orquestrador | _a definir_ (Agno?) | coordena etapas, agrega parecer |
| LLM | _a definir_ | _a definir_ |
| Storage (desenhos + pareceres) | _a definir_ | precisa reter histórico |
| API / Backend | FastAPI (provável) | padrão consistente |
| Frontend | _a definir_ | dashboard de aprovação / fila |
| Deploy | _a definir_ | _a definir_ |

## 🔄 Fluxo principal (alto nível)

```
[Desenho técnico] + [Especificação técnica]
            ↓                   ↓
    [API Sol de URX]      [Parser da spec]
            ↓                   ↓
   [Dados estruturados]  [Requisitos estruturados]
            ↓                   ↓
            └───→ [Comparador] ←───┘
                       ↓
                  [Parecer]
              (✅ / ⚠️ / ❌)
                  + justificativas
                       ↓
                 [Fila humana]
            (apenas ⚠️ e ❌)
                       ↓
                [Aprovação final]
```

## 🧩 Componentes

- **Adapter Sol de URX:** cliente HTTP/RPC para a API, com retry e cache.
- **Parser de especificação:** converte spec (PDF/doc) em lista de requisitos estruturados.
- **Comparador:** engine de regras (checagens numéricas/lógicas) + LLM (checagens semânticas).
- **Gerador de parecer:** monta documento com resultado, evidências e citações do desenho/spec.
- **Fila de revisão humana:** UI ou workflow pra engenheiro dar palavra final.
- **Módulo de calibração:** permite revisor marcar "concordo/discordo" do parecer automatizado → feedback loop.

## 🔌 Integrações externas

- **API Sol de URX** (crítico — credenciais e contrato ainda não conhecidos).
- Possível: sistema interno da Coclade para registro de aprovação.

## 🔐 Considerações de segurança

- Desenhos técnicos são **propriedade intelectual** da Coclade / cliente final.
- Credenciais da API Sol de URX em cofre (Bitwarden / env var).
- Logs: nunca persistir desenho bruto em log, só IDs e metadados.
- Acesso por papel: desenhista, revisor, coordenador.

## 📐 Decisões arquiteturais (resumo)

Ver [`../decisions/`](../decisions/) para ADRs completos.
_— nenhum registrado —_

## 🧪 Estratégia de testes

- _a definir_ — provavelmente: golden set de (desenho + spec + parecer humano esperado) para regressão.
- Avaliação de LLM: graded eval com critérios explícitos (acerto = bater decisão humana).
