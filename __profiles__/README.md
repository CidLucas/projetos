# 🧠 Perfis de Agentes (Profiles)

> Para que um agente Hermes possa ler entregáveis de outro perfil,
> cada profile documenta seus artefatos aqui.

## Estrutura

```
__profiles__/
├── README.md                     ← este arquivo
├── <profile-name>/
│   ├── README.md                 ← propósito e deliverables do profile
│   └── <data>/                   ← entregáveis por data
│       └── <tipo>-<desc>.md
```

## Profiles ativos

| Profile | Propósito | Última entrega |
|---------|-----------|----------------|
| `triage` | Classificação e roteamento de tarefas | — |
| `researcher` | Pesquisa técnica e de mercado | — |
| `writer` | Produção de conteúdo e documentação | — |
| `reviewer` | Revisão técnica e QA | — |

## Regras

1. Cada profile **escreve** no seu diretório dentro de `__profiles__/`
2. Nome do arquivo: `YYYY-MM-DD-tipo-desc.md`
3. Sempre referenciar o projeto destino (`plataforma-blu`, `agente-bloquo`, etc.)
4. Ao finalizar uma entrega, atualizar o `STATUS.md` do projeto correspondente
