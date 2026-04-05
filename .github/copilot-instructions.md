# arifOS Workspace — Copilot Instructions

> **Ditempa Bukan Diberi** — *Forged, Not Given* [ΔΩΨ | ARIF]

This workspace is a **Constitutional AI Governance System**. All AI agent actions are subject to the 13-floor constitutional pipeline and role-based access control.

---

## Workspace Layout

| Directory | Purpose |
|-----------|---------|
| `arifOS/` | Primary codebase — governance kernel, MCP server, Trinity engines, tests |
| `arif-site/` | Public web presence (Human Anchor / Soul) |
| `GEOX/` | Geoscientific data integration and MCP server |
| `arifosmcp/` | Symlink / staging mirror of `arifOS/arifosmcp` |

The main development target is **`arifOS/`**. All commands below assume `cd arifOS/` unless stated otherwise.

---

## Build, Test, Lint

```bash
# Dependencies
uv sync                          # sync all deps (preferred over pip)
pip install -e ".[dev]"          # alternative editable install

# Tests
pytest tests/ -v                 # full suite (450+ tests)
pytest tests/test_constitutional.py -v   # single test file
pytest tests/ -v -m "not slow"   # skip slow/integration tests
pytest tests/ --cov=core --cov-report=term-missing  # with coverage

# Linting & formatting (100-char line length)
ruff check .                     # lint (excludes archive/, tests/ by default)
ruff check . --fix               # auto-fix
black .                          # format
mypy --ignore-missing-imports .  # type check

# Pre-commit (runs all hooks above)
pre-commit run --all-files

# Run MCP server
python stdio_server.py           # stdio transport
python server.py                 # HTTP/SSE transport
```

**Async tests:** `asyncio_mode = "auto"` in `pyproject.toml` — do **not** add `@pytest.mark.asyncio` to test functions.

---

## Architecture

### Trinity ΔΩΨ

The governance pipeline routes every action through three organs:

| Organ | Symbol | File | Responsibility |
|-------|--------|------|----------------|
| AGI Mind | Δ | `core/organs/_1_agi.py` | Logic, truth, hallucination prevention (F2, F4, F7, F8) |
| ASI Heart | Ω | `core/organs/_2_asi.py` | Safety, empathy, impact simulation (F1, F5, F6, F9) |
| APEX Soul | Ψ | `core/organs/_3_apex.py` | Final judgment, sovereign override (F3, F11, F13) |

### Metabolic Pipeline (000→999)

```
000_INTAKE → 111_SENSE → 222_THINK → 333_ATLAS → 444_EVIDENCE
    → 555_EMPATHY → 666_ALIGN → 777_FORGE → 888_JUDGE → 999_SEAL
```

- **`core/governance_kernel.py`** — facade; canonical logic lives in `arifos_mcp/core/governance/`
- **`core/pipeline.py`** — execution pipeline
- **`arifos_mcp/core/`** — modular governance implementation (canonical)
- **`arifos_mcp/`** — FastAPI + FastMCP tool surface (11 mega-tools, 37 modes)

### VAULT999

Immutable audit ledger backed by PostgreSQL + Redis. All constitutional decisions are cryptographically logged here. Never bypass — write to vault via `core/organs/_4_vault.py`.

### Infrastructure (Docker Compose)

- **Redis** — session persistence
- **PostgreSQL** — VAULT999 ledger
- **Qdrant** — primary vector store
- **Ollama** — local LLM inference
- **Traefik** — reverse proxy

---

## Key Conventions

### Versioning
Format: `YYYY.MM.DD` in `pyproject.toml` and `CHANGELOG.md` (e.g., `2026.03.25`).

### Tool Decorators (MCP surface)
```python
@mcp.tool()                   # outer — exposes to MCP clients
@constitutional_floor()        # inner — enforces governance floors
async def my_tool(...):
    ...
```
Confirm the current tool list in `arifos_mcp/` before adding or editing tools — tool consolidation has happened multiple times.

### Imports
- Use `arifosmcp.transport` for local code; `mcp` is the external SDK — do not shadow it.
- Use lazy imports for optional deps: `try: import X except ImportError: X = None`.

### mypy Strictness
Strict type enforcement (`disallow_untyped_defs = true`) applies to:
- `core.governance_kernel`, `core.judgment`, `core.pipeline`
- `core.organs.*`, `core.shared.*`

Tests are exempt from strict typing.

### Code Style
- Line length: **100 chars** (Black + Ruff)
- Quote style: double quotes
- `ruff` selects: E, F, I (isort), UP (pyupgrade), N (pep8-naming), B (bugbear)

---

## Constitutional Floor Reference

| Floor | Name | Code-level concern |
|-------|------|--------------------|
| F1 | Amanah | Reversibility — pure functions, no hidden side effects |
| F2 | Truth | No fabricated data or fake metrics |
| F3 | Tri-Witness | Triple-verifiable execution, no contract mismatch |
| F4 | Clarity (ΔS≤0) | Named constants, no magic numbers |
| F5 | Omega0 | Safe defaults, preserve state |
| F6 | Empathy | Handle edge cases, clear error messages |
| F7 | RASA | Admit uncertainty, cap confidence scores |
| F8 | Ledger | Use established governance patterns, no bypasses |
| F9 | Anti-Hantu | Honest naming, transparent behavior (C_dark < 0.30) |
| F11 | Audit | All actions logged to VAULT999 |

---

## 888 HOLD — Mandatory Pause Conditions

Declare `888 HOLD — [trigger]` and await human approval when:
- Database destructive ops (`DROP`, `TRUNCATE`, `DELETE` without `WHERE`)
- Production deployments or mass file changes (>10 files)
- Credential/secret handling or git history modification
- User corrects a constitutional claim (**H-USER-CORRECTION**)
- Conflicting evidence across source tiers (**H-SOURCE-CONFLICT**)
- Proposing fixes based on <5 minutes audit (**H-RUSHED-FIX**)

---

## Agent Role Permissions

| Role | Read | Edit | Deploy | SEAL |
|------|------|------|--------|------|
| A-ARCHITECT | ✅ | ❌ | ❌ | ❌ |
| A-ENGINEER | ✅ | ✅ (approval) | ❌ | ❌ |
| A-AUDITOR | ✅ | ❌ | ❌ | ❌ |
| A-VALIDATOR | ✅ | ✅ | ✅ | ✅ |

**Human veto is absolute.** AI proposes; human decides.

---

## AAA Output Rules (binding)

1. **DRY_RUN:** If `dry_run=true` or `output_policy=SIMULATION_ONLY` → label as `"Estimate Only / Simulated"`.
2. **DOMAIN_GATE:** If `output_policy=CANNOT_COMPUTE` → respond exactly: `"Cannot Compute — required domain payload absent."` Do not substitute inference.
3. **VERDICT_SCOPE:** Only `DOMAIN_SEAL` authorises factual claims. `ROUTER_SEAL` ≠ domain truth.
4. **ANCHOR_VOID:** If `init_anchor` returns `void` or `session-rejected` → surface `"888_HOLD — anchor void. Re-init required."` and halt.

---

## Deployment (from `arifOS/`)

```bash
make fast-deploy    # code changes only (2-3 min, uses layer cache)
make reforge        # full rebuild (10-15 min, after Dockerfile/deps change)
make hot-restart    # config-only reload (instant)
make status         # container health
make health         # hit /health endpoint
make maintenance    # cleanup + image pruning
```

---

## Live Endpoints

| Service | URL |
|---------|-----|
| MCP endpoint | https://arifosmcp.arif-fazil.com/mcp |
| Health + capability map | https://arifosmcp.arif-fazil.com/health |
| Grafana | https://monitor.arifosmcp.arif-fazil.com |

---

*Authority: 888_JUDGE | Ditempa Bukan Diberi*
