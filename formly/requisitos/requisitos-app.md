# 📱 Requisitos de Aplicação — Formly

> **Versão:** v0.1 — 2026-07-30
> **Baseado em:** Google Doc de escopo + input do Lucas (2026-07-30)
> **Template:** 6 seções (visão geral, elementos UI, fluxos, regras, integrações, testes)
> **Status:** ⚠️ Sem código — requisitos aspiracionais baseados na visão do produto

---

## 1. Visão Geral

**Formly** é uma plataforma web para criação, coleta e análise de questionários. Diferencia-se dos concorrentes (Typeform, Google Forms, SurveyMonkey) por oferecer **áudio como canal de resposta nativo** com transcrição automática e **análise por IA** como camada de valor.

### Objetivo da aplicação

Permitir que um usuário:
1. **Crie questionários** de múltiplas formas: drag & drop, importação de texto, chat assistido
2. **Compartilhe** um link público para coleta de respostas
3. **Colete respostas** com suporte a texto + áudio (transcrito automaticamente)
4. **Visualize resultados** em dashboard com filtros e exportação
5. **(Futuro)** Receba análise por IA com insights automáticos

### Páginas

| Página | Arquivo | Descrição |
|---|---|---|
| **Criador de Questionário** | `pagina-01-criador.md` | Builder com 3 modos de interação (drag, texto, chat) |
| **Página de Resposta** | `pagina-02-resposta.md` | Link público para respondentes (digitar ou gravar áudio) |
| **Dashboard de Resultados** | `pagina-03-dashboard.md` | Visualização agregada, filtros, exportação |

### Público-alvo

- **Criador:** profissional que precisa aplicar pesquisas (RH, consultor, pesquisador, professor)
- **Respondente:** público final que acessa o link e responde
- **Analista:** mesmo criador, visualizando resultados

---

## 2. Elementos de UI (Shell)

### Topbar / Navegação

| Elemento | Tipo | Descrição |
|---|---|---|
| Logo | branding | "Formly" + ícone |
| Nav principal | links/tabs | Meus questionários, Criar novo, Templates |
| Avatar / Menu | dropdown | Conta, Configurações, Plano, Sair |
| Seletor de questionário | breadcrumb | Navegação contextual quando dentro de um form |

### Layout responsivo

- **Criador:** tela cheia, canvas central com sidebar de ferramentas
- **Resposta:** layout limpo, focado no respondente (estilo Typeform: uma pergunta por vez ou scroll)
- **Dashboard:** grid de cards e gráficos, responsivo

### Design System

- **Tema:** claro (padrão) com opção escura
- **Branding:** cores a definir (sugestão: paleta azul/verde — profissional e acolhedor)
- **Tipografia:** sans-serif moderna (Inter ou Geist)
- **Ícones:** Phosphor Icons ou Lucide

---

## 3. Fluxos

### Fluxo principal: Criar → Coletar → Analisar

```
[Criador monta questionário]
    → 3 modos: drag & drop / importar texto / chat
    → Personaliza (cores, logo, textos)
    → Publica
         ↓
[Link público gerado]
    → Criador compartilha (link, QR code, embed)
         ↓
[Respondente acessa o link]
    → Responde perguntas (texto ou áudio)
    → Áudio é transcrito automaticamente
         ↓
[Criador acessa Dashboard]
    → Vê respostas agregadas
    → Filtra por período, pergunta
    → Exporta (CSV, PDF)
    → (Futuro) Análise IA gera relatório
```

### Navegação entre páginas

```
Home (Meus questionários)
    │
    ├── [Criar novo] → Criador de Questionário
    │       └── [Publicar] → Confirmação + link
    │
    ├── [Ver resultados] → Dashboard
    │       └── [Exportar] → Download CSV/PDF
    │
    └── [Configurações] → Conta, plano, billing
```

---

## 4. Regras de Negócio

### Questionários

- **Tipos de pergunta (V1):** múltipla escolha, resposta curta, parágrafo, áudio
- **Personalização:** cores, logo, texto de abertura/encerramento
- **Publicação:** link público único por questionário
- **Limites por plano (premissa):**
  - Free: 3 ativos, 100 respostas/mês, sem áudio
  - Pro: ilimitados, áudio incluso, 1.000 respostas/mês
  - Business: ilimitado + análise IA

### Áudio

- **Gravação:** direto no navegador (MediaRecorder API)
- **Transcrição:** automática via Groq Whisper
- **Armazenamento:** S3/Blob storage, link associado à resposta
- **Fallback:** se transcrição falhar, áudio fica disponível para escuta manual

### Respostas

- **Anônimas por padrão** (sem coleta de e-mail, a menos que configurado)
- **Uma resposta por sessão** (evita duplicação acidental)
- **Rascunho automático:** resposta em andamento é salva localmente

### Planos e Cobrança

| Plano | Preço/mês | Questionários | Respostas/mês | Áudio | Exportação | IA |
|---|---|---|---|---|---|---|
| Free | R$ 0 | 3 ativos | 100 | ❌ | CSV | ❌ |
| Pro | R$ 49-79 | Ilimitados | 1.000 | ✅ | CSV+PDF | ❌ |
| Business | R$ 149-199 | Ilimitados | Ilimitadas | ✅ | CSV+PDF | ✅ (5/mês) |
| Add-on IA | R$ 29-49/pesquisa | — | — | — | — | ✅ avulso |

### Fora de escopo (V1)

- Skip logic / branching condicional
- White-label (domínio próprio)
- API pública
- Integrações nativas (CRM, planilhas)
- Coleta de vídeo
- App mobile nativo
- Multi-idioma (V1: PT-BR)

---

## 5. Integrações

| Integração | Tipo | Descrição |
|---|---|---|
| **Groq Whisper** | API STT | Transcrição de áudio das respostas |
| **S3 / Blob Storage** | Storage | Armazenamento dos arquivos de áudio |
| **Supabase Auth** | Autenticação | Login/cadastro de criadores |
| **Stripe** | Pagamento | Assinaturas e add-ons |
| **OCI GenAI** | API IA | (Futuro) Análise e geração de relatórios |
| **PostgreSQL** | Banco | Dados estruturados (questionários, respostas) |

---

## 6. Cenários de Teste

### Criação de questionário

- [ ] Criar questionário via drag & drop → perguntas aparecem no canvas
- [ ] Criar questionário importando documento de texto → parser extrai perguntas
- [ ] Criar questionário via chat → assistente gera estrutura após conversa
- [ ] Editar pergunta inline → alterações persistem
- [ ] Reordenar perguntas → drag no canvas
- [ ] Personalizar cores/logo → preview atualiza
- [ ] Publicar → link gerado e copiável

### Resposta

- [ ] Acessar link público → página de resposta carrega
- [ ] Responder pergunta de texto → validação (obrigatória/opcional)
- [ ] Gravar áudio → transcrição aparece após upload
- [ ] Submeter questionário completo → confirmação exibida

### Dashboard

- [ ] Ver respostas agregadas → gráficos e contagens
- [ ] Filtrar por período → dados atualizam
- [ ] Exportar CSV → arquivo gerado corretamente
- [ ] Questionário sem respostas → empty state amigável
