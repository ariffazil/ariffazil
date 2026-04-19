# arifOS Workspace — Copilot Instructions

> **Ditempa Bukan Diberi** — *Forged, Not Given* [ΔΩΨ | ARIF]

This repository is the **workspace shell** for the arifOS ecosystem. Most software work happens in **`arifOS/`**; start there unless the task explicitly targets another project.

## Workspace focus

| Path | Purpose |
|------|---------|
| `arifOS/` | Primary codebase: canonical Python governance kernel, MCP runtime, manifests, and tests |
| `A-FORGE/` | TypeScript execution/runtime companion |
| `GEOX/` | Geoscience MCP and data tools |
| `WEALTH/` | Capital and valuation organs |
| `arif-sites/` | Public web surfaces |

All commands below assume `cd arifOS`.

## Build, test, lint

```bash
# Install dependencies
uv sync --all-extras

# Full test suite
uv run pytest tests/ -v

# Single test file
uv run pytest tests/test_constitutional.py -v

# Single test case
uv run pytest tests/core/test_vault_integrity.py::test_verify_vault_record_accepts_canonical_entry -v

# Spec-level contract checks
uv run pytest tests/specs/test_specs.py -v

# Integration marker
uv run pytest -m integration

# Force physics enforcement when needed
ARIFOS_PHYSICS_DISABLED=0 uv run pytest tests/

# Lint / format / type-check
uv run ruff check .
uv run black . --line-length 100
uv run mypy .

# Pre-commit
uv run pre-commit run --all-files

# Local runtime entrypoints
uv run python server.py
uv run python -m arifosmcp.runtime

# Local status helpers
make status
make health
```

`pytest` is configured in `pyproject.toml` with `asyncio_mode = "auto"` and markers including `constitutional`, `slow`, `integration`, and `e3e`.

## High-level architecture

- **Source of truth split:** the workspace root is a hub, but `arifOS/` is the canonical source repo for doctrine, manifests, tool contracts, and tests.
- **Runtime entrypoint:** `arifOS/server.py` is the universal FastMCP/FastAPI entrypoint. It loads environment state, initializes VAULT999 session logging, adds middleware, and wraps tool handlers with hardened dispatch.
- **Canonical runtime layer:** `arifOS/arifosmcp/runtime/` contains the active runtime contract and orchestration code: `tool_specs.py`, `tools.py`, `kernel_core.py`, `kernel_router.py`, `resources.py`, `rest_routes.py`, and `__main__.py`.
- **Public MCP contract:** the public `arifos_*` surface is intentionally fixed at **11 tools**. `arifosmcp/runtime/tool_specs.py` defines the public/internal split, while `arifosmcp/fastmcp.json`, `arifosmcp/mcp.json`, and `arifosmcp/tool_registry.json` are the exported manifests. `tests/test_floors_ci.py` is the drift gate for that contract.
- **Canonical resources:** `arifosmcp/specs/resource_specs.py` defines the **5 canonical resources**: `arifos://doctrine`, `arifos://vitals`, `arifos://schema`, `arifos://session/{session_id}`, and `arifos://forge`.
- **Kernel vs runtime:** `arifosmcp/` is the main runtime package, but `core/` is still live kernel code rather than dead archive. The runtime imports `core.governance_kernel`, and stricter mypy rules apply to `core.governance_kernel`, `core.judgment`, `core.pipeline`, `core.organs.*`, and `core.shared.*`.
- **Stateful infrastructure:** the runtime is wired around Postgres + Redis for VAULT999 and session state, Qdrant for memory retrieval, and FastAPI/FastMCP as the transport surface.

## Key conventions

- Use **`arifosmcp`** as the canonical Python package/import name.
- Treat **tool specs and manifests as contracts**. If you change `tool_specs.py`, registry files, or MCP manifests, run the manifest/spec tests before assuming the surface is valid.
- Prefer **adding modes or internal handlers** over inventing new public `arifos_*` tool names. The public surface is deliberately compressed, and router naming still has a compatibility split between `arifos_route` and `arifos_kernel`, so check the current manifests and runtime handlers together before renaming anything.
- Keep the **5 canonical resources** stable. New context surfaces should usually be folded into existing resource/tool contracts rather than added as new top-level URIs.
- `ruff` excludes `tests/**` and `archive/**`, so a clean lint run mostly validates production code, not tests.
- Formatting and typing conventions come from `pyproject.toml`: **100-char lines**, **double quotes**, Python **3.12** target, and **selective mypy strictness** focused on kernel modules.
- Async tests use `pytest-asyncio` **auto mode**; do **not** add `@pytest.mark.asyncio`.
- Execution is **double-gated**: `arifos_forge` is an execution bridge, but real mutations are guarded by judge/vault flow and human approval constraints.
- When docs conflict, prefer `arifOS/` repo files for doctrine and the generated manifests/runtime endpoints for the live MCP contract.

*Authority: grounded from `README.md`, `GEMINI.md`, `arifOS/AGENTS.md`, `arifOS/docs/CONTRIBUTING.md`, `arifOS/pyproject.toml`, `arifOS/server.py`, and runtime manifest/tests.*
