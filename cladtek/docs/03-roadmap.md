# 03 — Roadmap — Cladtek

## 🗺 Fases

### Fase 0 — Descoberta (atual 🟡)
- [ ] Obter credenciais e docs da **API Sol de URX**
- [ ] Coletar 2-3 exemplos reais de (desenho + spec + parecer humano)
- [ ] Definir escopo da V1
- [ ] Escolher stack
- [ ] Entender SLA atual e meta de melhoria

### Fase 1 — Especificação
- [ ] Contrato com a API Sol de URX mapeado
- [ ] Schema de "requisito estruturado" da spec
- [ ] Modelo do parecer
- [ ] Golden set montado (N desenhos anotados)

### Fase 2 — Build V1
- [ ] Setup do repo
- [ ] Adapter Sol de URX
- [ ] Parser de especificação
- [ ] Engine de comparação (regras + LLM)
- [ ] Geração de parecer
- [ ] CLI/script pra rodar fim-a-fim
- [ ] Deploy em ambiente de teste

### Fase 3 — Validação
- [ ] Comparação parecer automatizado vs. humano (golden set)
- [ ] Ajustes de prompt / regras
- [ ] Piloto com 1 projeto real
- [ ] Feedback do engenheiro revisor

### Fase 4 — Produção
- [ ] Deploy prod
- [ ] Integração com fluxo existente da Cladtek
- [ ] Monitoramento de SLA + acurácia
- [ ] Dashboard de métricas

## 📅 Milestones

| Marco | Data alvo | Status |
|---|---|---|
| M1 — Acesso à API Sol de URX | _a definir_ | 🔴 |
| M2 — Golden set + parser de spec | _a definir_ | 🔴 |
| M3 — Demo fim-a-fim | _a definir_ | 🔴 |
| M4 — Piloto com 1 projeto real | _a definir_ | 🔴 |
| M5 — Produção | _a definir_ | 🔴 |

## ⚠️ Riscos do roadmap

- **API Sol de URX desconhecida** — se for mal documentada, tempo de integração explode.
- **Especificações técnicas ambíguas** — o LLM pode "aprovar" interpretações diferentes das do humano.
- **Responsabilidade legal** — se um desenho aprovado pelo bot falhar em campo, quem responde? (decisão jurídica, não técnica).
- **Volume baixo de exemplos** — golden set pequeno pode dar falsa sensação de acurácia.
