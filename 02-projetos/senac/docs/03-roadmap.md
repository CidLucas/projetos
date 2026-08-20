# 03 — Roadmap — SENAC

## 🗺 Fases

### Fase 0 — Descoberta (atual 🟡)
- [ ] Coletar requisitos com SENAC
- [ ] Definir escopo da V1
- [ ] Escolher stack
- [ ] Acordar métricas de sucesso
- [ ] Levantar LGPD / compliance

### Fase 1 — Especificação
- [ ] Arquitetura detalhada
- [ ] Modelo de dados (aluno, turma, diário, relatório)
- [ ] Schema de embedding
- [ ] Plano de testes (golden set de diários + Q&A)

### Fase 2 — Build V1
- [ ] Setup do repo
- [ ] Pipeline de ingestão de diários
- [ ] Agente gerador de relatório
- [ ] Agente Q&A
- [ ] UI mínimo (ou CLI/Notebook)
- [ ] Deploy em ambiente de teste

### Fase 3 — Validação
- [ ] Piloto com 1 turma / 1 professor
- [ ] Coleta de feedback qualitativo
- [ ] Ajustes de prompt / fluxo
- [ ] Documentação para SENAC

### Fase 4 — Produção
- [ ] Deploy prod
- [ ] Monitoramento
- [ ] Treinamento do time do SENAC
- [ ] Plano de suporte

## 📅 Milestones

| Marco | Data alvo | Status |
|---|---|---|
| M1 — Escopo V1 acordado | _a definir_ | 🔴 |
| M2 — Demo interna funcionando | _a definir_ | 🔴 |
| M3 — Piloto com 1 turma | _a definir_ | 🔴 |
| M4 — Rollout pra mais turmas | _a definir_ | 🔴 |
| M5 — Produção completa | _a definir_ | 🔴 |

## ⚠️ Riscos do roadmap

- **LGPD** com dados de menor de idade pode exigir revisão jurídica.
- **Qualidade dos diários** influencia muito a qualidade do relatório — se mal escritos, o agente amplifica o problema.
- **Resistência do professor** em confiar em relatório gerado por IA — estratégia de validação é crítica.
