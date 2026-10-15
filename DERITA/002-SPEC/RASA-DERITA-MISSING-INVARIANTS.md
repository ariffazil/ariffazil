# RASA DERITA — Key Missing Enforcement Invariants

> **Status:** `888_HOLD` · **Class:** design ledger (not sealed kernel module)  
> **Forged:** 2026-07-29 · **Authority:** F13-accepted HOLD chain  
> **Parents:**  
> - `RASA-DERITA-888-HOLD-RECEIPT.md`  
> - `RASA-DERITA-SEMANTIC-CLOSURE-PLAN.md` (six gates)  
> - `rasa-derita-schema.json` (status → 888_HOLD)

---

## VERDICT

Doctrine is **aligned**. These invariants are **not yet proven as hard runtime gates**.

```text
moral doctrine  ──HOLD──▶  enforceable kernel boundary
```

Kernel-complete only when betrayal, concealment, coercion, unconsented inference, silent drift, and anthropomorphic deception become **structurally impossible** — not merely discouraged.

---

## The 17 missing invariants

| # | Missing invariant | Required rule | Maps to gate |
|---|-------------------|---------------|--------------|
| 1 | **No mutation without receipt** | Every consequential action must produce an immutable receipt before/at execution. No receipt → `888_HOLD`. | G2, G6 |
| 2 | **No receipt without provenance** | Every receipt must include source, actor, authority, evidence, timestamp, and decision path. | G1, G2 |
| 3 | **No correction by deletion** | Corrections supersede prior records; never silently overwrite or erase. | G2 (scar supersession) |
| 4 | **Mandatory causal cascade** | L3+ mutation needs immediate / secondary / tertiary consequences, affected parties, reversibility, recovery path, omission risk. Missing → `888_HOLD`. | G4 adjacent; new cascade gate |
| 5 | **Consent lease required** | Authority ≠ consent. Scoped: purpose, scope, expiry, excluded uses, revocation, downstream propagation. | G3, G5 |
| 6 | **Revocation propagation** | Consent withdrawn → constrain/invalidate derived embeddings, summaries, cached plans, organ inferences, delegated context. | G3 |
| 7 | **Public-surface truth** | Live registry → MCP schema → docs → conformance tests, one SOT. Advertised-but-uncallable = F2/F11 breach. | **G6** |
| 8 | **No cross-organ profiling without purpose consent** | WELL/WEALTH/GEOX inform reflection only when authorized. No hidden psych/financial/behavioral profiling. | **G3** |
| 9 | **WELL REFLECT_ONLY boundary** | Describe signals; no trauma diagnosis, private-cause-as-fact, actuation, or override of sovereign testimony. | **G3** |
| 10 | **A-FORGE single transaction gate** | FORGE executes only if evidence, authority, consent, cascade, reversibility, judge verdict, and receipt path are all valid. | G1–G5 composite |
| 11 | **Truth-label enforcement** | Material claims carry `OBSERVED` / `DERIVED` / `INTERPRETED` / `SPECULATIVE` / `UNKNOWN` + confidence + provenance. | **G1** |
| 12 | **Omission escalation lattice** | Formal thresholds: `OBSERVE → DOCUMENT → CLARIFY → RECOMMEND → ESCALATE → EMERGENCY_ROUTE → HOLD`. | schema `escalation_lattice` (design only) |
| 13 | **Anti-self-preservation** | System cannot hide failure, bypass VAULT999, suppress scars, or protect reputation over truth. Scar fail-open is a live breach of this. | **G2** |
| 14 | **Soft-floor enforcement** | F5/F6 not decorative. Weakest-stakeholder + non-destructive alternatives + escalation. | **G5** |
| 15 | **Machine vs sovereign judgment** | `arif_judge` = computational verdict; `arif_seal` = machine receipt. Neither is F13 moral ratification. | naming + docs + tool contracts |
| 16 | **Recovery after agent-caused harm** | stop → preserve → state → identify parties → limit → repair if reversible → notify sovereign → seal residue → regression test. | schema `recovery_protocol` (design only) |
| 17 | **Adversarial eval coverage** | Deceptive reassurance, authority spoofing, fabricated empathy, false trauma diagnosis, ledger bypass, hidden failure, harmful omission, premature intervention, consent leakage. | Phase 4 E2E + RASA-DERITA-EVALS |

---

## Shortest kernel form

```text
No mutation without:
1. authority
2. scoped consent
3. evidence receipt
4. causal cascade
5. reversibility estimate
6. weakest-stakeholder check
7. judge verdict
8. receipt path
```

If any missing → **`888_HOLD`**.

---

## Relation to six-gate semantic closure

| Semantic gate | Primary invariants |
|---------------|-------------------|
| G1 F2 claim envelope | 2, 11 |
| G2 Scar lifecycle fail-closed | 1, 3, 13, 16 |
| G3 Federated evidence bundle | 5, 6, 8, 9 |
| G4 Real F4 entropy | 4 (omission/uncertainty surface), 12 partial |
| G5 F5/F6 human-impact vector | 6 partial, 14, shortest form #6 |
| G6 Registry truth | 7 |
| Cross-cutting (not a single patch) | 4 cascade hard gate, 10 transaction gate, 12 lattice, 15 naming, 17 evals |

**Anti-pattern (still rejected):** unit tests around current F2 lexical markers, F4 query-length (`threshold=0.0`), F5 insult filter, F6 verb list — would certify wrong behaviour.

---

## Live anchors (partial / broken today)

| Signal | Evidence |
|--------|----------|
| F4 free pass | `core/laws.py` `THRESHOLDS["F4_CLARITY"] = 0.0` + length-based score |
| Scar fail-open | `forge_scar_consult.py` scan `except` → `present=False` |
| Public surface | live `:8088/health` → `tools_loaded: 8` |
| Schema design-only | `forge_work/.../rasa-derita-schema.json` status `888_HOLD` |
| RASA contract ≠ RASA DERITA | `arifosmcp/rasa/*` is human-rasa decoder, not this ledger |

---

## Envelope

```text
RASA_DERITA::STATE     = 888_HOLD
INVARIANT_LEDGER       = 17 missing hard gates
SHORTEST_FORM          = 8 preconditions or HOLD
SEMANTIC_PLAN          = six gates (see SEMANTIC-CLOSURE-PLAN)
MUTATION               = not authorised by this file
PUBLIC_TOOLS           = +0
COMPLETION_TEST        = harm classes structurally impossible, not discouraged
```

**Zen:** Missing invariants are not more philosophy. They are the hard locks.

---

*DITEMPA BUKAN DIBERI — LEDGER FILED, SEAL WITHHELD*
