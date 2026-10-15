# RASA DERITA — Phase 1 Land (ZEN)

> **2026-07-29** · Branch `forge/rasa-derita-semantic-closure`  
> **Verdict:** `888_HOLD` — specification landed in-repo; **not** installed/enforced

## Commits

| SHA | Message |
|-----|---------|
| `d6ea3a72a` | Phase 1 — gate schemas + failing evaluator/e2e tests |
| `3f1d13df4` | Phase 1 zen — constitutional schema land + structural validation |

## Canonical artifact

```text
arifosmcp/schemas/constitutional/rasa-derita-schema.json
schema_hash: sha256:d74069f868d84e5306e1b3c32fd9e7b07c0b8bc8f304d1c26125cb8c42c7d966
status: 888_HOLD
enforcement_mode: NONE
```

## Structural tests

```text
ARIFOS_SKIP_PROTOCOL_SENTINEL=1 \
  pytest tests/constitutional/test_rasa_derita_schema.py
→ 17 passed
```

## Zen discipline applied

| Action | Done |
|--------|------|
| Land schema under arifOS tree | YES |
| Structural loader (no enforcement) | YES |
| Failing gate tests (prior commit) | YES |
| Eval fixtures frozen | YES |
| Restore accidental `core/laws.py` Phase-2 leak | YES |
| Restore accidental `forge_scar_consult.py` leak | YES |
| Exclude ABI adapters from Phase 1 | YES (left untracked) |
| New public MCP tools | **+0** |
| VAULT INSTALLED_ENFORCED | **NO** |

## Correct classification after Phase 1

```text
SPECIFIED:        YES
MACHINE-READABLE: YES
COMMITTED:        YES (feature branch)
LOADED (boot):    NO
ENFORCED:         NO
EVALS EXECUTED:   NO
DEPLOYED:         NO
ATTESTED:         NO
```

## Next (Phase 2 — not started)

Rewrite weak evaluators + scar fail-closed against failing tests.  
Still zero new public tools. PR only after green semantics + live refuse probes.

DITEMPA BUKAN DIBERI
