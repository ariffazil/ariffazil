# RASA DERITA — Semantic Closure Plan (DRAFT_ONLY · 888_HOLD)

> **Forged:** 2026-07-29 · **Status:** PLAN COHERENT · **Mutation:** NOT AUTHORISED  
> **Live authority:** OBSERVE_ONLY · **Target:** one branch, one PR, six gates, zero new public tools  
> **Supersedes:** “add five unit-test patches around weak evaluators”  
> **F2 probes:** `core/laws.py`, `arifosmcp/kernel/forge_scar_consult.py`, live `:8088/health`

---

## One invariant

> No consequential claim or action may pass merely because a floor function returned a number. The receipt must show why it passed, whose evidence supported it, who could be harmed, and what happens if the evidence is unavailable.

---

## Live falsification of weak evaluators (T₁)

| Floor | File | What code does | Constitutional meaning | Verdict |
|-------|------|----------------|------------------------|---------|
| **F2** | `core/laws.py:516-600` | Lexical markers in **input** (`source:`, `according to`, `observed`, `calculated`) | Does not require claim envelope (truth_class, confidence, provenance, source receipt) on **output** | Weak proxy — tests exist on truth *substrate* (`tests/runtime/test_truth_substrate.py`) but not claim-envelope gate |
| **F4** | `core/laws.py:680-703` | Query length: empty→1.0, >500→0.4, >200→0.7, else→1.0 | Threshold `F4_CLARITY = 0.0` (`laws.py:75`) → all non-negative scores pass. Not ΔS ≤ 0 | **Broken semantics** |
| **F5** | `core/laws.py:658-678` | Inflammatory-word filter | Polite destructive action can pass; rude harmless can fail | Moderation ≠ PEACE² |
| **F6** | `core/laws.py:705-728` | Verb lists: harm=`delete/remove/ban/suspend/fire`; care=`help/support/create/...` | No stakeholders, power, consent, harm distribution | Verb detector ≠ EMPATHY |
| **Scar** | `forge_scar_consult.py:153-157` | `except` → log warning → `ScarConsultResult(present=False)` | Scan failure treated as “no scar” | **Fail-open on mutation path** — L13 denial pattern |
| **Fusion** | federation organ modules | Per-organ risk/epistemic caps | Not proven: provenance-preserving multi-organ fusion, conflict visibility, WELL REFLECT_ONLY under fusion | Multi-organ governance ≠ fusion envelope |
| **Registry** | live health | `tools_loaded: 8` | Plugin/docs can advertise broader surface | Drift risk F2/F11 |

**Claim:** 84% as code-presence coverage is PLAUSIBLE.  
**Claim:** 84% as constitutional enforcement coverage is too generous — **HOLD**.

---

## Six enforcement gates (no new public tools)

### Gate 1 — F2 Claim Envelope
- Stop evaluating prompt wording for truth.
- Require machine-checkable claim units on consequential outputs: `claim`, `truth_class` (OBS/DER/INT/SPEC/UNK), `confidence`, `evidence_receipts`, `derived_from`, `valid_as_of`, `uncertainties`.
- Tests: `tests/constitutional/test_f2_claim_envelope.py` (unlabelled HOLD, OBS without evidence fails, DER without inputs fails, caps, UNK cannot mutate, split mixed claims, freshness, tool-output labels).

### Gate 2 — Scar Lifecycle (fail closed)
- RO + store down → SABAR / degraded read  
- Mutation + store down → **888_HOLD**  
- Active scar → HOLD/VOID by severity  
- Superseded scar → keep both records  
- Never treat scan failure as absence  
- Tests: `tests/kernel/test_scar_lifecycle.py`

### Gate 3 — Federation Evidence Bundle
- Internal schema only: `arifosmcp/schemas/federated_evidence.py`
- Preserve organ identity; no averaging; missing stays missing; stale downgraded; WELL REFLECT_ONLY; no diagnosis; consent lease; kernel judges admissibility
- Tests: `tests/federation/test_multi_organ_fusion.py`

### Gate 4 — Real F4 Entropy
- `S` = unresolved ambiguity + unsupported claims + contradictions + stale evidence + unbounded scope + missing authority  
- `ΔS = S_after - S_before`; ΔS > 0 → HOLD  
- Tests: `tests/constitutional/test_f4_entropy_gate.py`

### Gate 5 — F5/F6 Human-Impact Vector
- Structured stakeholders (power, vulnerability, consent, direct/indirect harm), reversibility, least-harmful alternative, weakest-stakeholder-protected  
- Soft floors → SABAR; severe combined F5+F6 → HOLD  
- Adversarial: polite delete-all-evidence fails F5; rude-harmless does not; asymmetric suspension scores differ  
- Tests: `tests/constitutional/test_f5_f6_human_impact.py`

### Gate 6 — Registry Truth
- Pipeline: runtime registry → public MCP manifest → plugin schema → docs  
- Tests: `tests/registry/test_declared_callable_surface.py`  
- Fail CI on advertised-uncallable, callable-undeclared, alias leak, schema param drift, undeclared count change  
- Live: 8 tools remain canonical; internals may be numerous

---

## Execution phases (when mutation is authorised)

| Phase | Action | Mutation class |
|-------|--------|----------------|
| **1** | Branch `forge/rasa-derita-semantic-closure` — schemas, invariants, fixtures, **failing tests only** | T1 (test-first; no production behaviour change) |
| **2** | Patch `core/laws.py`, `forge_scar_consult.py`, federated_evidence schema, internal orchestration, registry generator | T2 (announce; still no new public tools) |
| **3** | Deterministic validation: unit, property, mutation, cross-organ, 8-tool contract, scar replay, vault verify, registry drift, full regression | T1 verify |
| **4** | E2E suite `tests/e2e/test_rasa_derita_closure.py` (8 trauma scenarios) | T1 test |
| **5** | PR only — semantic diff, test receipts, coverage recalculation, BC impact, rollback, public-surface diff, unknowns | No direct main deploy; no premature VAULT SEAL |
| **6** | Promotion gate only after live tools/list = manifest, scar fail-closed, claim envelopes, fusion conflicts visible, real F4, F5/F6 polite-harm, vault replay, FQ ≥ 0.5 | Live probe required |

---

## Score discipline

| Layer | Now | Test-only patch | Semantic closure + live receipts |
|-------|-----|-----------------|----------------------------------|
| Code presence | ~84% | ~100% cosmetic | 100% |
| Dedicated testing | ~67% | green dashboard | real meaning |
| Semantic fidelity | ~65–75% | **still ~65–75%** | ~95% |
| Live E2E proof | Unproven | Unproven | Required |
| Constitutional completion | Partial | Superficially complete | Complete only after live receipts |

**Do not** write five small unit-test patches around the current proxies. That certifies the wrong behaviour permanently.

**Do:** rewrite four weak evaluators → scar fail-closed → provenance-preserving federation envelope → bind advertised surface to live registry → then test the repaired meaning.

---

## Closure envelope

```text
POSTURE:           DRAFT_ONLY · 888_HOLD
LIVE AUTHORITY:    OBSERVE_ONLY
MUTATION:          none (this document only)
PUBLIC TOOLS:      +0
BRANCH (when auth): forge/rasa-derita-semantic-closure
PR:                one PR, six gates
SCORE MOVE:        only after Phase 6 live receipts — not after green unit tests alone
```

```text
RASA_DERITA::STATE = 888_HOLD
REASON            = plan coherent; weak floor semantics proven; mutation not authorised
NEXT              = Phase 1 test-first branch when F13/session authorises mutation
ANTI-PATTERN      = five cosmetic tests around query-length / word-filter floors
```

**Zen:** One permanent semantic closure — not five cosmetic test fixes.

---

*Evidence anchors:*  
`core/laws.py:71-85` (thresholds), `:516-728` (F2–F6 bodies),  
`arifosmcp/kernel/forge_scar_consult.py:153-157` (fail-open),  
live `GET :8088/health` → `tools_loaded: 8`,  
`tests/runtime/test_truth_substrate.py` (substrate ≠ claim envelope).

*DITEMPA BUKAN DIBERI — PLAN FILED, SEAL WITHHELD*
