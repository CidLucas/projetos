#!/bin/bash
# F0 — Copia o código existente para a lib blu_agno_runtime e ajusta interfaces.
# Estratégia (decisão 2026-08-20): NÃO reescrever padrões — copiar + editar imports.
# Fontes: memory_api (mesmo monorepo) + agente-bloquo (repo separado, puxado via git).
set -euo pipefail
cd /home/ec2-user/monorepo

SRC_AUTH=services/memory_api/src/memory_api/auth
SRC_CTRL=services/memory_api/src/memory_api/control
SRC_DB=services/memory_api/db
DST=libs/blu_agno_runtime/src/blu_agno_runtime

echo "==> Scaffold de diretórios"
mkdir -p "$DST"/{auth,mcp,storage,control} libs/blu_agno_runtime/{db/migrations,tests}

echo "==> 1. Auth (Principal, IdentityAdapter, AuthGate) — cópia direta da memory_api"
cp "$SRC_AUTH/principal.py"  "$DST/auth/principal.py"
cp "$SRC_AUTH/identity.py"   "$DST/auth/identity.py"
cp "$SRC_AUTH/middleware.py" "$DST/auth/middleware.py"
# __init__.py expõe Principal/IdentityAdapter/AuthGate/IdentityError
cat > "$DST/auth/__init__.py" <<'EOF'
from blu_agno_runtime.auth.identity import IdentityAdapter, IdentityError
from blu_agno_runtime.auth.middleware import AuthGate, get_principal
from blu_agno_runtime.auth.principal import Principal

__all__ = ["Principal", "IdentityAdapter", "IdentityError", "AuthGate", "get_principal"]
EOF

echo "==> 2. Control plane — cópia direta + rename de schema no SQL/código"
cp "$SRC_CTRL/plane.py"            "$DST/control/plane.py"
cp "$SRC_CTRL/identity_adapter.py" "$DST/control/identity_adapter.py"
touch "$DST/control/__init__.py"

echo "==> 3. Migrations — aplicador + SQL com schema agent_runtime"
cp "$SRC_DB/migrate.py" libs/blu_agno_runtime/db/migrate.py
touch libs/blu_agno_runtime/db/__init__.py

echo "==> 4. Edição de interfaces: memory_api.* → blu_agno_runtime.*"
find "$DST" -name "*.py" -not -name "__init__.py" -exec \
  sed -i 's/from memory_api\./from blu_agno_runtime./g; s/import memory_api/import blu_agno_runtime/g' {} +

echo "==> 5. Agente-bloquo (repo separado) — puxar via git"
git remote add agente-bloquo https://github.com/CidLucas/agente-bloquo.git 2>/dev/null || git remote set-url agente-bloquo https://github.com/CidLucas/agente-bloquo.git
git fetch agente-bloquo --depth 1 main 2>&1 | tail -1
# mcp_token_manager: cópia direta (não tem acoplamento Bloquo)
git checkout agente-bloquo/main -- src/auth/mcp_token_manager.py 2>/dev/null || true
if [ -f src/auth/mcp_token_manager.py ]; then
  mkdir -p "$DST/mcp"
  cp src/auth/mcp_token_manager.py "$DST/mcp/token_manager.py"
  rm -rf src/auth  # não commitar lixo do outro repo
  echo "  token_manager copiado (desacoplar provider Cognito→plugável é a edição pendente)"
else
  echo "  ⚠️ agente-bloquo fetch falhou — copiar manualmente de /tmp/agente-bloquo-inspect/src/auth/mcp_token_manager.py"
  cp /tmp/agente-bloquo-inspect/src/auth/mcp_token_manager.py "$DST/mcp/token_manager.py" 2>/dev/null || echo "  ⚠️ clone em /tmp ausente — baixar o arquivo manualmente"
fi

echo "==> 6. mcp/connection.py — EXTRAIR _mcp_connection do agent.py (não copiar cru)"
# O agent.py tem 490 linhas com 31 refs Bloquo/OCI. A extração é a ISSUE #323:
# manter streamablehttp_client + ClientSession + MCPTools(session=...) como
# MCPConnection (async context manager), sem VectorSearchTool/ScreenDetailTool.
echo "  (manual — issue #323) esqueleto esperado:"
cat > "$DST/mcp/connection.py" <<'EOF'
"""MCPConnection — conexão MCP via streamable HTTP para o Agno (padrão agente-bloquo).

Extraído de agente-bloquo/src/agent.py (_mcp_connection). O Agno MCPTools não
aceita URL HTTP nativa; abrimos streamablehttp_client + ClientSession e
injetamos session= no MCPTools. Conexão por request, teardown no mesmo task.
"""
from __future__ import annotations

import contextlib
from collections.abc import AsyncIterator

from agno.tools.mcp import MCPTools
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


@contextlib.asynccontextmanager
async def mcp_connection(
    url: str, token: str | None, exclude_tools: list[str] | None = None
) -> AsyncIterator[MCPTools | None]:
    """Abre conexão MCP para UM request; yield de MCPTools ou None."""
    if not token or not url:
        yield None
        return
    headers = {"Authorization": f"Bearer {token}"}
    async with streamablehttp_client(url, headers=headers) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            mcp_tools = MCPTools(session=session, exclude_tools=exclude_tools or [])
            await mcp_tools.connect()
            yield mcp_tools
EOF

echo "==> 7. Placeholder storage/tenant.py — subclasse TenantPostgresDb (issue #325)"
cat > "$DST/storage/tenant.py" <<'EOF'
"""TenantPostgresDb — PostgresDb do Agno com coluna tenant_id (issue #325).

O Agno PostgresDb não tem tenant_id nativo. Esta subclasse adiciona a coluna
na session_table e filtra TODA query por tenant_id.
"""
from __future__ import annotations

# TODO(#325): implementar — estender agno.db.postgres.PostgresDb
class TenantPostgresDb:  # placeholder até a issue #325
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("issue #325 — implementar TenantPostgresDb")
EOF
touch "$DST/storage/__init__.py"

echo "==> 8. pyproject.toml da lib"
cat > libs/blu_agno_runtime/pyproject.toml <<'EOF'
[project]
name = "blu-agno-runtime"
version = "0.1.0"
description = "Runtime Agno multi-tenant — auth, MCP HTTP, storage, control plane (assistente pessoal, ADR-001)"
requires-python = ">=3.12"
dependencies = ["agno>=2.6", "psycopg", "pydantic-settings", "httpx", "mcp"]

[tool.ruff]
line-length = 100
EOF

echo "==> DONE. Árvore:"
find "$DST" -name "*.py" | sort
echo "Próximos: ajustar docstrings/imports pendentes, escrever testes, submeter #319→#327."
