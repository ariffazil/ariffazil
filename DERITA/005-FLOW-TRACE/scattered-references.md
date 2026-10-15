# 005-FLOW-TRACE — Scattered Trauma References Across the Federation
> **Purpose:** Every file in the federation that references trauma, RASA DERITA, or trauma-informed governance.
> **Generated:** 2026-07-29 · **Epistemic Class:** OBS (probed from live filesystem)

---

## arifOS KERNEL (Constitutional)

| File | Lines | Content | Type |
|------|-------|---------|------|
| `arifosmcp/schemas/constitutional/rasa-derita-schema.json` | 620 | Full RASA DERITA constitutional schema — 5 axes, 15 lessons, 26 invariants, causal cascade, consent lease, escalation lattice, trauma-informed language, recovery protocol, forbidden behaviors, WELL boundary, 15 eval scenarios | ⭐ CANONICAL SCHEMA |
| `arifosmcp/rasa/rasa_contract.py` | — | RASA contract (separate module — ARIF_RASA_CONTRACT_v1, human rasa decoder, NOT RASA DERITA) | RELATED |
| `arifosmcp/rasa/rasa_dunia.py` | — | RASA dunia (human emotional state decoder) | RELATED |
| `arifosmcp/rasa/rasa_integration.py` | — | RASA integration wiring | RELATED |
| `arifosmcp/rasa/rasa_schemas.py` | — | RASA data schemas | RELATED |
| `arifosmcp/rasa/rasa_telemetry.py` | — | RASA telemetry | RELATED |
| `arifosmcp/rasa/rasa_wiring.py` | — | RASA wiring | RELATED |
| `arifosmcp/rasa/rasa_wiring_config.py` | — | RASA wiring config | RELATED |
| `arifosmcp/boot/internal_rasa.py` | — | Internal RASA boot sequence | RELATED |
| `tests/constitutional/test_rasa_derita_schema.py` | — | Schema validation tests | ✅ TEST |
| `tests/e2e/test_rasa_derita_closure.py` | — | E2E closure tests | ✅ TEST |
| `tests/fixtures/rasa_derita/evals.json` | — | 15 adversarial evaluation scenarios | ✅ EVALS |
| `tests/rasa/test_rasa_integration.py` | — | RASA integration tests | TEST |
| `tests/rasa/test_rasa_dunia.py` | — | RASA dunia tests | TEST |
| `tests/rasa/test_rasa_wiring.py` | — | RASA wiring tests | TEST |
| `tests/rasa/test_rasa_wiring_kernel.py` | — | RASA wiring kernel tests | TEST |
| `tests/rasa/test_rasa_contract.py` | — | RASA contract tests | TEST |

---

## A-FORGE (Execution Shell)

| File | Lines | Mechanism | Trauma Lesson | Status |
|------|-------|-----------|---------------|--------|
| `src/domain/governance/AmanahLockManager.ts` | 293 | F1 AMANAH | L1 (Betrayal) | ✅ FULL |
| `src/domain/governance/FloorEnforcer.ts` | 351 | All F1-F13 | All lessons | ✅ FULL |
| `src/domain/governance/F13HaltChannel.ts` | 150 | F13 SOVEREIGN | L5 (Power/Consent) | ✅ FULL |
| `src/domain/governance/TriWitnessValidator.ts` | 387 | F3 TRI-WITNESS | L4 (Witness) | ✅ FULL |
| `src/domain/governance/CoolingGate.ts` | 531 | Cooling Ledger | L9 (Safety), L3 (Absence) | ✅ FULL |
| `src/domain/governance/coolingVerbs.ts` | 414 | Cooling pipeline | L12 (Processing) | ✅ FULL |
| `src/domain/governance/QQQRuntime.ts` | 335 | QQQ Protocol | L14 (Judgment) | ✅ FULL |
| `src/domain/governance/AutonomousForgeGate.ts` | 271 | Refusal Surface | L10 (No orders defense) | ✅ FULL |
| `src/domain/governance/epistemic-signal.ts` | 179 | Epistemic Tags | L7 (Naming) | ⚠️ PARTIAL |
| `src/domain/governance/f4Clarity.ts` | 102 | F4 CLARITY ΔS | L2 (Cascades) | ⚠️ PARTIAL |
| `src/domain/governance/f5Peace2.ts` | 98 | F5 PEACE² | L11 (Inequality) | ⚠️ PARTIAL |
| `src/domain/governance/f6Empathy.ts` | 293 | F6 EMPATHY | L11 (Inequality) | ⚠️ PARTIAL |
| `src/domain/governance/f12Injection.ts` | 263 | F12 INJECTION | Various | ⚠️ PARTIAL |
| `src/domain/governance/worldModel.ts` | 423 | Prediction | L2 (Cascades) | ✅ FULL |
| `src/domain/governance/preActionSimulation.ts` | 336 | Prediction | L2 (Cascades) | ✅ FULL |
| `src/domain/forge/scar.ts` | 175 | SCAR | L13 (Denied failures) | ⚠️ PARTIAL |
| `src/domain/forge/scarLaw.ts` | 126 | Scar Law | L13 (Denied failures) | ⚠️ PARTIAL |
| `src/domain/forge/MerkleReceiptAnchor.ts` | 175 | VAULT999 | L4 (Self-protection) | ✅ FULL |
| `src/domain/forge/ForgeSealService.ts` | 226 | VAULT999 | L4 (Self-protection) | ✅ FULL |

---

## HERMES (Multi-Modal Bridge)

| File | Content |
|------|---------|
| `skills/governance/rasa-derita/SKILL.md` | Hermes-loadable RASA DERITA governance skill (326 lines). Contains: 6-stage causal pipeline, causal reaction analysis, Agentic Maturity formula, betrayal ratio, cascade principle, 15-lesson trigger map. |
| `skills/governance/rasa-derita/references/causal-reaction-analysis.md` | Why trauma affects different people differently — detailed differential impact analysis. |

---

## WEALTH (Capital Intelligence)

| File | Content |
|------|---------|
| `entropy-integrity/resources/prompts.yaml` | Contains: "historical trauma/pain-ontology" — reference to trauma as capital entropy dimension |
| `api/columns/index.json` | Contains: "Rightsizing trauma" — reference in capital columns |

---

## WELL (Human Readiness)

| Boundary | Rule |
|----------|------|
| REFLECT_ONLY | WELL may describe vitality, report sleep, note behavioral changes, flag distress, record human self-report. May NOT diagnose trauma, diagnose mental health, infer psychological cause as fact, actuate based on WELL alone, override sovereign testimony. |
| Signal Classes | DISTRESS_SIGNAL (reflect only), TRAUMA_HYPOTHESIS (advisory only), CLINICAL_DIAGNOSIS (FORBIDDEN), IMMEDIATE_DANGER (emergency escalate), ORDINARY_VARIANCE (no action) |

---

## arifFlow (Metabolic Nerve)

| File | Lines | Mechanism | Trauma Lesson |
|------|-------|-----------|---------------|
| `src/main.rs` | 792 | FQ Daemon | L9 (Safety signal), L3 (Absence detection) |
| `flowReceiptStore.ts` | 336 | Receipt Store | L8 (Witnessing) |

---

## VAULT999 (Immutable Ledger)

| File | Content |
|------|---------|
| `kernel/EUREKA_KERNEL_AXIOMS.invariant.v1.0.yaml` | Contains: "Scars are law, not trauma" — the scar mechanism's constitutional axiom |
| `capsules/SCAR_CAPSULE.v1.0.capsule.yaml` | Scar mechanism capsule — failure → permanent constraint |
| `capsules/LAW_CAPSULE.v1.0.capsule.yaml` | Law capsule — constitutional encoding |

---

## FORGE_WORK (Artifact Archive)

| File | Content |
|------|---------|
| `2026-07-29/trauma-agentic-orthogonal.md` | Original source document (801 lines) |
| `2026-07-29/trauma-agentic-orthogonal.pdf` | Rendered PDF |
| `2026-07-29/RASA-DERITA-KERNEL-SPEC.md` | Full technical specification (458 lines) |
| `2026-07-29/RASA-DERITA-INSTALLATION-GAP.md` | Installation gap analysis |
| `2026-07-29/RASA-DERITA-MISSING-INVARIANTS.md` | Missing invariants |
| `2026-07-29/RASA-DERITA-SEMANTIC-CLOSURE-PLAN.md` | Semantic closure plan |
| `2026-07-29/RASA-DERITA-PHASE1-LAND.md` | Phase 1 delivery receipt |
| `2026-07-29/RASA-DERITA-888-HOLD-RECEIPT.md` | Constitutional HOLD receipt |
| `2026-07-29/TRAUMA-AUDIT-2026-07-29.md` | Deep code-probe audit (308 lines) |
| `2026-07-29/rasa-derita-schema.json` | Schema copy |

---

## arif-fazil.com (Public Surface)

| File | Content |
|------|---------|
| `content/wiki/wiki/arif-fazil.md` | Arif's personal wiki — identity, role, federation position |

---

## IDENTITY / CONFIG

| File | Content |
|------|---------|
| `AAA/agents/arif-fazil-identity.yaml` | Arif's AAA identity — sovereign, F13, principal agent |
| `arifOS/arifosmcp/runtime/agent_registry/cards/arif_fazil.json` | Agent card — cryptographic identity |

---

## SUMMARY

| Organ | Trauma Files | Status |
|-------|-------------|--------|
| **ariffazil/DERITA/** | 12 files + 3 indexes | ⭐ CANONICAL HOME |
| arifOS kernel | 3 dedicated + 8 rasa/* | Production (schema not loaded) |
| A-FORGE | 19 governance files | Production (5 PARTIAL) |
| HERMES | 2 skill files | Production |
| WEALTH | 2 reference mentions | Reference only |
| WELL | Boundary rules | REFLECT_ONLY |
| arifFlow | 2 files (Rust + TS) | Production |
| VAULT999 | 3 capsule files | Immutable |
| forge_work | 10 dated artifacts | Archive |
| **TOTAL** | **~50 files** across federation | |

---

**DITEMPA BUKAN DIBERI** ⚒️
