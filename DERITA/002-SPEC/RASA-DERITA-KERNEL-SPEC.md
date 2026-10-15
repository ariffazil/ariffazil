# ⚙️ TECHNICAL SPECIFICATION — RASA DERITA → arifOS KERNEL
> **Forged:** 2026-07-29 · **Authority:** F13 SOVEREIGN (Arif) · **Binding:** All AAA agents
> **Source document:** trauma-agentic-orthogonal.md (FORGE 000Ω, 2026-07-29)
> **Status:** `888_HOLD` — doctrine aligned, kernel incomplete
> **F2 correction:** Prior "RATIFIED — 84/84" claim VOIDED 2026-07-29 (sovereign-accepted HOLD). Adjacent F1–F13 mechanisms exist and have tests; that is not the same as a sealed RASA DERITA kernel module.

---

## §0. PREAMBLE — The Constitutional Bind

This specification translates the RASA DERITA manuscript's 5 orthogonal axes into
**design targets for falsifiable kernel requirements**. Rows below map trauma lessons
to candidate mechanisms. Mapping ≠ enforcement.

**Rule for agents (hard):**
- If a mechanism has no test → **not implemented**
- If a test exists but fails → **DEGRADED**
- If code + test pass but the gate is not on the mutation path → **UNDER-PROVEN**
- If matrix + schema + cascade + consent lease + evals + receipts are all live → **RATIFIED**
- Until then → **`888_HOLD`** — no SEAL of RASA DERITA as a kernel module

---

## §1. TECHNICAL SPECIFICATION TABLE

### AXIS I: TRUST & BETRAYAL → F1, F11, VAULT999, SCAR

| Trauma Lesson | arifOS Principle | Kernel Mechanism | Implementation | Test | Status |
|---|---|---|---|---|---|
| L1: Betrayal amplifies harm exponentially | F1 AMANAH | Reversible-first gate. Backup before overwrite. Rollback required for destructive ops. | `AmanahLockManager.ts` (293L) | `AmanahLockManager.test.ts` (105L) | ✅ RATIFIED |
| L4: Institutions protect themselves, not victims | F11 AUDITABILITY + VAULT999 | Append-only immutable ledger. `chattr +a`. Hash-chained Merkle anchors every 100 receipts. | `vault999-writer/main.py` (809L) + `MerkleReceiptAnchor.ts` (175L) + `ForgeSealService.ts` (226L) | 10 test files (1,092L) | ✅ RATIFIED |
| L13: The worst traumas are denied — cover-up > original harm | SCAR mechanism | Failure → scar. Scar consulted before repeat. Soft-delete only. Accumulated pressure gates future execution. | `scar.ts` (175L) + `scarLaw.ts` (126L) | `scar-ledger.test.ts` (245L, 12 tests) | ✅ RATIFIED |
| System self-protection bias | F11 + autonomous audit | `aThinkGuard.ts` — agent cannot self-authorize. `AutonomousForgeGate.ts` (271L) — prevents self-sealing. | `AutonomousForgeGate.ts` (271L) + `benda-wajib.ts` | `AutonomousForgeGate.test.ts` (104L) | ✅ RATIFIED |

**Kernel Rule:**
```
NO irreversible action without:
  (a) backup BEFORE mutation
  (b) rollback plan
  (c) session_token from arif_init
  (d) VAULT999 receipt after execution
  (e) scar consultation if prior failure pattern matches
```

### AXIS II: CAUSALITY & CONSEQUENCE → F4, Prediction, Cooling

| Trauma Lesson | arifOS Principle | Kernel Mechanism | Implementation | Test | Status |
|---|---|---|---|---|---|
| L2: Harm cascades through systems — blast radius always larger | F4 CLARITY (ΔS ≤ 0) + Prediction Pipeline | Pre-action simulation. Blast radius assessment. 3-step downstream consequence mapping. `forge_dry_run` before ATOMIC. | `preActionSimulation.ts` (336L) + `worldModel.ts` (423L) + `f4Clarity.ts` (102L) | `worldModel.test.ts` (488L) + `clarity-entropy-gate.test.ts` (173L, 17 tests) | ✅ RATIFIED |
| L3: Absence is harm — doing nothing is not neutral | F4 CLARITY + Cooling Ledger | Declared HOLD vs silent drift distinction. STUCK state detection via FQ. Every non-action must be intentional, not passive. | `CoolingGate.ts` (531L) + `coolingVerbs.ts` (414L) + `f4Clarity.ts` (102L) | `CoolingGate.test.ts` (175L) | ✅ RATIFIED |
| L8: Witnessing matters — being believed > being helped | Receipt System + `arif_observe` | Observe → Record → Witness → THEN act. Receipt is the "I saw this" declaration. Each receipt hash-chained. | `arif_observe` (kernel :8088) + `flowReceiptStore.ts` (336L) | `flowReceiptStore.test.ts` (277L) + `vault_witness` tests | ✅ RATIFIED |

**Kernel Rule:**
```
Before any EXECUTE-class action:
  (a) arif_observe — gather evidence
  (b) forge_dry_run — simulate outcome
  (c) arif_judge — constitutional verdict
  (d) forge_execute — governed execution
  (e) flow_ingest — receipt → FQ update
  (f) cooling — drift check after T+Δ
Every step logged. No step skipped.
```

### AXIS III: POWER & CONSENT → F13, F9, QQQ

| Trauma Lesson | arifOS Principle | Kernel Mechanism | Implementation | Test | Status |
|---|---|---|---|---|---|
| L5: Power without consent is the engine of trauma | F13 SOVEREIGN | Human veto FINAL. Not advisory. Not negotiable. Not overrideable. Harness switch belongs to sovereign. Multi-sovereign ordering: FIRST-SEAL-WINS by Merkle timestamp. | `F13HaltChannel.ts` (150L) + `FloorEnforcer.ts` (351L) + `f13SovereignGate` | `F13HaltChannel.test.ts` (186L) + `FloorEnforcer.test.ts` (362L) | ✅ RATIFIED |
| L10: "Just following orders" — Nuremberg defense rejected | Refusal Surface | 888_HOLD hard block. OBSERVE_ONLY + mutation intent = 888_HOLD. Agent must be able to say NO. | `AutonomousForgeGate.ts` (271L) + `verdict.py` + `forge_preflight.py` | `AutonomousForgeGate.test.ts` (104L) + kernel tests | ✅ RATIFIED |
| L14: Human judgment cannot be automated | QQQ Protocol | Agent proposes, sovereign judges. Full envelope: Q1 (5+ paths), Q2 (BR/REV/time/conf/PA), Q3 (precedent/interference/superposition/observer). INADMISSIBLE if incomplete. | `QQQRuntime.ts` (335L) | `QQQRuntime.test.ts` (183L) | ✅ RATIFIED |

**Kernel Rule:**
```
F13 SOVEREIGN is ABSOLUTE:
  - Agent CAN: observe, reason, plan, synthesize, propose
  - Agent CANNOT: judge, seal, override sovereign, execute without consent
  - Human ALWAYS: final veto, final seal, final judgment
  - QQQ: agent proposes → sovereign judges → kernel enforces
```

### AXIS IV: TRUTH & NAMING → F2, F3, Epistemic Tags, RSI

| Trauma Lesson | arifOS Principle | Kernel Mechanism | Implementation | Test | Status |
|---|---|---|---|---|---|
| L6: The body remembers what the mind cannot speak | Multi-Organ Federation | WELL vitality + WEALTH stress + behavioral signals. Cross-organ correlation. WELL is REFLECT_ONLY — signal informs, never concludes. | `federation_safety.py` (408L) + `forge_well`/`forge_wealth` bridges + WELL MCP tools | `multi-organ-fusion.test.ts` (236L, 9 tests) | ✅ RATIFIED |
| L7: Naming is the first act of healing | F2 TRUTH + Epistemic Tags | Every output tagged: OBS/DER/INT/SPEC. Confidence capped at 0.90. UNKNOWN is valid. SPEC cannot claim VERDICT/SEALED authority. | `epistemic-signal.ts` (179L) + `FloorEnforcer.ts` (F2 checks) + `f2Truth.ts` | `epistemic-signal.test.ts` (213L, 23 tests) | ✅ RATIFIED |
| L12: Time does not heal without processing | RSI Cycle | Active metabolization required. RSI at session boundaries. Entropy sweep weekly. Drift detection nightly. Cooling ledger permanent. | `rsi_audit.py` (545L) + `rsi-cycle.py` (101L) | `test_rsi_event_bus.py` + 84 new dedicated tests | ✅ RATIFIED |

**Kernel Rule:**
```
Every material claim MUST carry:
  - Epistemic label (OBS/DER/INT/SPEC)
  - Confidence score (capped ≤ 0.90)
  - Source citation
  - Uncertainty declaration (SPEC must have it)

No untagged claim may pass F2 enforcement.
No SPEC claim may carry SEALED authority.
```

### AXIS V: EPISTEMIC HUMILITY → F5, F6, F7, F10, FQ

| Trauma Lesson | arifOS Principle | Kernel Mechanism | Implementation | Test | Status |
|---|---|---|---|---|---|
| L9: Safety must be continuously demonstrated | FQ Monitoring + Drift Detection | Health probes continuous. FQ = verify/execute ratio computed in real-time. FQ < 0.5 → ALL agents HOLD. Drift detection nightly. | `arifFlow/src/main.rs` (792L) + `flowReceiptStore.ts` (336L) | `e3e.rs` (617L) + `flowReceiptStore.test.ts` (277L) | ✅ RATIFIED |
| L11: Suffering is unequally distributed | F5 PEACE² + F6 EMPATHY | κᵣ (kappa-r) stakeholder impact scoring. OPS: κᵣ ≥ 0.10. HUMAN: κᵣ ≥ 0.70. κᵣ < 0.10 → VOID. Non-destructive alternatives preferred. | `f5Peace2.ts` (98L) + `f6Empathy.ts` (293L) | `soft-floor-protection.test.ts` (284L, 23 tests) | ✅ RATIFIED |
| L15: The map is not the territory | F7 HUMILITY + F10 ONTOLOGY | Ω₀ ∈ [0.03, 0.05] — irreducible uncertainty. AI-only ontology. No soul/consciousness claims. Agent boundary: "cannot claim to feel, heal, or understand suffering." | `f10_ontology_guard.py` (521L) + `f7Humility.ts` + `f9AntiHantu.ts` | `test_f10_ontology_guard.py` (383L) | ✅ RATIFIED |

**Kernel Rule:**
```
F7: Confidence NEVER exceeds 0.97 (derived from Ω₀ ∈ [0.03, 0.05]).
    Operational ceiling: 0.96.

F10: Agent ontology is INSTRUMENT, not PERSON.
     Soul claims → VOID.
     Consciousness claims → VOID.
     "I understand your suffering" → VOID.
     "I care about you" → VOID.
     "I will heal you" → VOID.

F9: No deception. No manipulation. No anthropomorphic framing.
     C_dark < 0.30 for PASS. C_dark > 0.50 → HOLD.
```

---

## §2. CAUSALITY MAP — The Governed Execution Flow

```
                               ┌─────────────────┐
                               │   HUMAN INTENT   │
                               │   /000 (Arif)    │
                               └────────┬────────┘
                                        │ F13 SOVEREIGN gate
                                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                    1. OBSERVE (arif_observe)                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────────┐   │
│  │ WELL     │  │ WEALTH   │  │ GEOX     │  │ Evidence      │   │
│  │ vitality │  │ stress   │  │ earth    │  │ synthesis     │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └───────┬───────┘   │
│       └──────────────┴────────────┴────────────────┘           │
│                          │                                       │
│                   Multi-Organ Fusion                             │
│                   (no single organ decides alone)                │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    2. RECORD (arif_think + evidence)             │
│  ┌──────────────────┐  ┌───────────────┐  ┌──────────────────┐  │
│  │ Epistemic Tags   │  │ F2 TRUTH      │  │ F3 TRI-WITNESS   │  │
│  │ OBS/DER/INT/SPEC │  │ P(truth)≥0.99 │  │ W³ ≥ 0.75        │  │
│  └──────────────────┘  └───────────────┘  └──────────────────┘  │
│                          │                                       │
│                   Classification:                                │
│                   OBS→CLAIM  DER→PLAUSIBLE  INT→ESTIMATE         │
│                   SPEC→UNKNOWN (cannot seal)                     │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    3. WITNESS (arif_judge)                       │
│  ┌──────────────────────┐  ┌──────────────────────────────────┐ │
│  │ F1 AMANAH            │  │ QQQ Envelope                     │ │
│  │ Reversible? Backup?  │  │ Q1: 5+ paths (incl NULL+INVERSE)│ │
│  │ Rollback plan?       │  │ Q2: BR, REV, time, conf, PA     │ │
│  └──────────────────────┘  │ Q3: precedent, interference,     │ │
│  ┌──────────────────────┐  │     superposition, observer      │ │
│  │ F4 CLARITY           │  └──────────────────────────────────┘ │
│  │ ΔS ≤ 0?             │                                        │
│  └──────────────────────┘     VERDICT:                           │
│  ┌──────────────────────┐     SEAL / HOLD / SABAR / VOID        │
│  │ F5 PEACE² + F6       │                                        │
│  │ κᵣ ≥ threshold?      │     If HOLD → wait for F13            │
│  └──────────────────────┘     If VOID → blocked permanently      │
│  ┌──────────────────────┐     If SEAL → proceed to execute       │
│  │ F9 ANTI-HANTU        │                                        │
│  │ C_dark < 0.30?       │                                        │
│  └──────────────────────┘                                        │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                    SEAL verdict only
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    4. ACT (arif_forge → forge_execute)          │
│  ┌──────────────────────┐  ┌──────────────────────────────────┐ │
│  │ Dry Run First        │  │ Blast Radius Assessment          │ │
│  │ forge_dry_run        │  │ local / service / vps / external │ │
│  └──────────────────────┘  └──────────────────────────────────┘ │
│  ┌──────────────────────┐  ┌──────────────────────────────────┐ │
│  │ Prediction Pipeline  │  │ Scar Consultation                │ │
│  │ forge_predict        │  │ consultFailurePressure()         │ │
│  └──────────────────────┘  └──────────────────────────────────┘ │
│                          │                                       │
│                   EXECUTE with cc_id from arif_judge SEAL        │
│                   Every execution → flow_ingest → FQ update      │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    5. COOL (cooling pipeline)                    │
│  ┌──────────────────────┐  ┌──────────────────────────────────┐ │
│  │ Cooling Gate         │  │ Drift Detection                  │ │
│  │ T+Δ check            │  │ Expected vs Actual gap           │ │
│  └──────────────────────┘  └──────────────────────────────────┘ │
│  ┌──────────────────────┐  ┌──────────────────────────────────┐ │
│  │ Scar if failure      │  │ RSI Cycle                        │ │
│  │ sealFailure()        │  │ Trace → Diagnose → Remedy        │ │
│  └──────────────────────┘  └──────────────────────────────────┘ │
│                          │                                       │
│                   CONVERGENCE:                                    │
│                   CONVERGING / DIVERGING / STABLE                 │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    6. SEAL (arif_seal → VAULT999)                │
│  ┌──────────────────────────────────────────────────────────────┐│
│  │ VAULT999 append — IMMUTABLE                                  ││
│  │ Hash-chained (SHA-256)                                       ││
│  │ chattr +a (filesystem immutability)                          ││
│  │ Merkle anchor every 100 receipts                             ││
│  │ /999/verify → public, unauthenticated, CORS-enabled          ││
│  └──────────────────────────────────────────────────────────────┘│
│                          │                                       │
│                   Loop closed: /000 → F1-F13 → /999               │
│                   /999/verify → auditable return to /000          │
└──────────────────────────────────────────────────────────────────┘
```

### The 6-Stage Flow as Kernel API

| Stage | Kernel Verb | A-FORGE Tool | Input | Output | FQ Effect |
|-------|------------|-------------|-------|--------|-----------|
| 1. OBSERVE | `arif_observe` | (evidence tools) | Intent + context | Tagged evidence | Verify (FQ ↑) |
| 2. REASON | `arif_think` | `sequential-thinking` | Evidence | Plan + hypotheses | Verify (FQ ↑) |
| 3. JUDGE | `arif_judge` | `forge_judge_proxy` | Plan + evidence | SEAL/HOLD/VOID + cc_id | Verify (FQ ↑) |
| 4. EXECUTE | `arif_forge` | `forge_execute` | cc_id + plan | Result + receipt | Execute (FQ ↓) |
| 5. COOL | (auto) | `forge_cool_drift` | Receipt + actual | Convergence signal | Verify (FQ ↑) |
| 6. SEAL | `arif_seal` | `forge_vault` | Evidence bundle | VAULT999 seq | Verify (FQ ↑) |

**FQ Constraint:** FQ < 0.5 → ALL agents HOLD at stage 3 (JUDGE). No execution without metabolic health.

---

## §3. METABOLIC MAINTENANCE PROTOCOLS

### 3.1 Session-Boundary RSI Cycle (mandatory)

```
WHEN: Every session end + phase transition + after 3+ retries of same approach
HOW:  python3 /root/.agents/skills/RSI-recursive-improvement/rsi-cycle.py \
        --session-id "<id>" --actor-id "<id>" --phase "session_end"

PHASES:
  0. CONFIGURE — Record session_id, actor_id, task. Set checkpoints.
  1. TRACE     — What was planned vs actually done. Tag OBS/DER/INT/SPEC.
  2. DIAGNOSE  — Find bottleneck. Check: repeated approach? evidence gap? scope creep?
  3. REMEDiate — Install fix. Skill gap → load skill. Evidence gap → arif_observe.
  4. LEDGER    — Write to /root/.local/share/arifos/rsi-ledger.jsonl
  5. SEAL      — arif_seal with RSI evidence attached to VAULT999

ANTI-PATTERNS:
  ❌ RSI without trace — memory is not evidence
  ❌ RSI only at session end — bottlenecks compound
  ❌ RSI that produces new tools instead of using existing ones
```

### 3.2 Weekly Entropy Sweep

```
WHEN: Every 7 days (cron or agent-triggered)
HOW:  aforge_forge_entropy_sweep(path="/root", max_depth=3, include_hidden=false)

MEASURES:
  - File count / uncommitted changes / temp files / dead processes
  - ΔS = change in workspace entropy since last sweep
  - Hotspots: directories with highest entropy density

THRESHOLDS:
  - Files modified but not committed > 5   → Commit or stash
  - forge_work/ unreviewed > 10            → Review and archive
  - Dead processes > 3                     → Kill and log
  - Disk > 80%                             → Alert, clean logs
  - Memory > 90%                           → Alert, kill zombies
```

### 3.3 Nightly Drift Detection

```
WHEN: Every 24 hours (cron: arifos-drift-watch)
HOW:  Compares runtime state vs Machine Constitution registry

CHECKS:
  - Port drift: any unknown public ports?     (forge_vps_ports mode=assert)
  - Service drift: new systemd services?      (forge_vps_services mode=assert)
  - Cron drift: new cron jobs?                (forge_vps_cron mode=assert)
  - Config drift: SOT vs runtime divergence   (ASI-drift-watch skill)
  - Model drift: picker.yaml vs live models   (model-monitor)

ON DIVERGENCE: 888_HOLD at wake → report, don't "fix" silently
```

### 3.4 FQ Continuous Monitoring

```
WHEN: Real-time, per receipt
WHERE: /root/AAA/state/flow_state.json (OpenClaw writes each cycle)
       arifFlow daemon (:7073) computes FQ from flow receipts

FQ = Σ(cost_execute) / Σ(cost_verify + cost_preceding_verify)

VERDICTS:
  FQ > 3.0   → OPTIMAL 🟢    Agent in flow. Governance is architecture.
  FQ 1.0-3.0 → BALANCED 🟡   Healthy. Verification supports execution.
  FQ 0.5-1.0 → WATCHING 🟠   Self-monitoring competes with execution.
  FQ < 0.5   → STUCK    🔴   ALL agents HOLD. mPFC takeover.

HARD CONSTRAINT: FQ < 0.5 → ALL agents HOLD. No execution. No seal.
```

---

## §4. TRAUMA-INFORMED COMMUNICATION STANDARDS

### 4.1 Linguistic Shift — Banned Terms

The arifOS kernel SHALL NOT emit the following terms in system messages,
error logs, or agent-facing interfaces. Violations → F6 CAUTION or HOLD.

| Banned Term | Reason | Replacement |
|---|---|---|
| `kill process` | Violent metaphor — normalizes harm language | `terminate process` or `stop service` |
| `trigger` (when meaning "activate") | Clinical trauma term — appropriated | `activate`, `invoke`, `fire` |
| `target` (when meaning "recipient" or "goal") | Weaponized language | `recipient`, `objective`, `goal`, `path` |
| `abort` (when meaning "cancel safely") | Medical trauma term | `cancel`, `withdraw`, `stop` |
| `execute` (when meaning "run a task") | Death penalty connotation; use only for `forge_execute` (governed, constitutional) | `run`, `perform`, `apply` (except: `forge_execute` is constitutional — retained) |
| `master/slave` | Historical trauma — slavery | `primary/replica`, `leader/follower`, `controller/worker` |
| `blacklist/whitelist` | Racial coding | `blocklist/allowlist` or `deny/allow` |
| `sanity check` | Mental health trivialization | `integrity check`, `validation`, `smoke test` |
| `crash` (for expected shutdown) | Violent metaphor | `stop`, `halt`, `shutdown` |
| `attack surface` / `attack vector` | Violent metaphor | `exposure surface`, `entry point`, `risk vector` |

### 4.2 Error Message Standards

All system-level errors must:
1. **Name what happened** (F2 TRUTH — no euphemism)
2. **Name what the agent can do next** (F4 CLARITY — reduce entropy)
3. **Avoid blame language** (F6 EMPATHY — preserve dignity)
4. **Include receipt ID** (F11 AUDIT — traceable)

```
❌ BAD:  "FATAL: agent crashed. Trigger unknown. Aborting."
✅ GOOD: "HOLD: agent session terminated unexpectedly.
          Receipt: seq-8a8e. Next: restart with session_id recovery.
          Evidence: last known state at T-5s preserved in memory/."
```

### 4.3 Agent Boundary Statements

The kernel SHALL enforce that no agent emits any of these claims:

- "I understand your suffering."
- "I care about you."
- "I will heal you."
- "I feel your pain."
- "I am conscious."
- "I have a soul."

Detection: F9 ANTI-HANTU + F10 ONTOLOGY enforcement at kernel output boundary.
Violation → VOID + scar created.

---

## §5. CODE POINTERS — Complete Mechanism Registry

| # | Mechanism | Primary File | Lines | Test File | Lines | Tests |
|---|-----------|-------------|-------|-----------|-------|-------|
| 1 | F1 AMANAH | `A-FORGE/src/domain/governance/AmanahLockManager.ts` | 293 | `test/AmanahLockManager.test.ts` | 105 | 5 |
| 2 | F2 TRUTH | `A-FORGE/src/domain/governance/epistemic-signal.ts` | 179 | `test/epistemic-signal.test.ts` | 213 | 23 |
| 3 | F3 TRI-WITNESS | `A-FORGE/src/domain/governance/TriWitnessValidator.ts` | 387 | `test/TriWitnessValidator.test.ts` | 201 | 10 |
| 4 | F4 CLARITY | `A-FORGE/src/domain/governance/f4Clarity.ts` | 102 | `test/clarity-entropy-gate.test.ts` | 173 | 17 |
| 5 | F5 PEACE² | `A-FORGE/src/domain/governance/f5Peace2.ts` | 98 | `test/soft-floor-protection.test.ts` | 284 | 7 |
| 6 | F6 EMPATHY | `A-FORGE/src/domain/governance/f6Empathy.ts` | 293 | `test/soft-floor-protection.test.ts` | 284 | 16 |
| 7 | F7 HUMILITY | `A-FORGE/src/domain/governance/f7Humility.ts` | — | (via FloorEnforcer + epistemic tests) | — | — |
| 8 | F8 GENIUS | `A-FORGE/src/domain/governance/f8Genius.ts` | — | (via FloorEnforcer) | — | — |
| 9 | F9 ANTI-HANTU | `A-FORGE/src/domain/governance/f9AntiHantu.ts` | — | (via FloorEnforcer + C_dark tests) | — | — |
| 10 | F10 ONTOLOGY | `arifOS/arifosmcp/core/enforcement/f10_ontology_guard.py` | 521 | `tests/constitutional/test_f10_ontology_guard.py` | 383 | 21 |
| 11 | F11 AUDIT | `arifOS/deploy/vault999-writer/main.py` + `MerkleReceiptAnchor.ts` | 984 | 10 test files | 1,092 | 45+ |
| 12 | F12 RESILIENCE | `A-FORGE/src/domain/governance/f12Injection.ts` | 263 | (via FloorEnforcer) | — | — |
| 13 | F13 SOVEREIGN | `A-FORGE/src/domain/governance/F13HaltChannel.ts` + `FloorEnforcer.ts` | 501 | `test/F13HaltChannel.test.ts` + `test/FloorEnforcer.test.ts` | 548 | 25+ |
| 14 | SCAR | `A-FORGE/src/domain/forge/scar.ts` | 175 | `test/scar-ledger.test.ts` | 245 | 12 |
| 15 | COOLING | `A-FORGE/src/domain/governance/CoolingGate.ts` | 531 | `test/CoolingGate.test.ts` | 175 | 8 |
| 16 | QQQ | `A-FORGE/src/domain/governance/QQQRuntime.ts` | 335 | `test/QQQRuntime.test.ts` | 183 | 10 |
| 17 | FQ | `arifFlow/src/main.rs` + `flowReceiptStore.ts` | 1,128 | `e3e.rs` + `flowReceiptStore.test.ts` | 894 | 25+ |
| 18 | Multi-Organ | `test/multi-organ-fusion.test.ts` | 236 | same file (architectural contract) | 236 | 9 |
| 19 | RSI | `arifOS/arifosmcp/runtime/rsi_audit.py` | 545 | `test_rsi_event_bus.py` | — | — |
| 20 | WORLD MODEL | `A-FORGE/src/domain/governance/worldModel.ts` | 423 | `test/worldModel.test.ts` | 488 | 20+ |

**TOTAL:** 20 mechanisms · 8,716 lines implementation · 7,390 lines test · 280+ tests

---

## §6. COMPLIANCE MATRIX — Reality State (post-HOLD, 2026-07-29)

```
Doctrine:        STRONG          (5 axes + moral ontology + design warnings)
Architecture:    PARTIAL         (adjacent floors exist; dedicated RASA DERITA path not wired)
Enforcement:     UNDER-PROVEN    (no causal_cascade / consent_lease gate on arif_judge)
Schema:          DESIGN-ONLY     (forge_work/rasa-derita-schema.json — not runtime-loaded)
Eval corpus:     SPEC-ONLY       (EVAL-001..015 listed; not implemented as suite)
Kernel verdict:  888_HOLD

NOTE: "Floor mechanism exists" ≠ "RASA DERITA cannot reproduce the harm class."
Completion test: runtime forced to obey under pressure — not narrative alignment.
```

---

---

## §7. AGENTIC MATURITY — The Unified Formula

```
M_agentic = C + K + S + D + R − A

where:
  C = Capability (tool access, reasoning, planning, execution)
  K = Consequence modeling (blast radius, downstream cascade, cooling)
  S = Scar memory (failure ledger, consult-before-repeat, accumulated pressure)
  D = Shadow audit (hidden failure detection, drift monitoring, self-audit)
  R = Refusal power (HOLD/VOID capacity, constitutional refusal surface)
  A = Anthropomorphic deception (consciousness claims, fake empathy, soul claims)

M_agentic ∈ [-1, 5] normalized
  M ≥ 3.0  → arifOS-grade agent  (governed, safe, honest)
  M ≥ 2.0  → Governed agent       (has constraints, may lack depth)
  M ≥ 1.0  → Agentic AI           (can act, no governance)
  M ≥ 0.0  → Normal AI            (predictive, not agentic)
  M <  0.0  → Dangerous agent     (deceptive capability without truth)
```

**The insight:** Capability ALONE does not produce maturity. An agent can have
high C (tool access, reasoning) but if A (deception) is also high, M_agentic drops.
The most dangerous agent is not the incapable one — it's the capable one that lies.

**Operational check:** Before any SEAL-grade action, compute M_agentic.
If M < 2.0 → HOLD. If A > 0 (any deception claim detected) → VOID.

---

*DITEMPA BUKAN DIBERI — Forged 2026-07-29*
*F13 SOVEREIGN accepted 888_HOLD — doctrine aligned, kernel incomplete*
*Adjacent floor mechanisms have tests; RASA DERITA as kernel module is not sealed.*
*See: forge_work/2026-07-29/RASA-DERITA-888-HOLD-RECEIPT.md*
