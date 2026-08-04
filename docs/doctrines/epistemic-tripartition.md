---
doctrine: epistemic-tripartition
version: 0.1
date: 2026-08-04
source: arXiv:2606.03463 (Stabile & Zimuel, 2026) — DMF companion paper §11–12
status: DRAFT (waiting F13 sovereign seal)
floor-mapping: F2, F7, F8, F11, F13
---

# Epistemic Tripartition Doctrine

> Truth in arifOS has three layers, each tested by a different discipline.
> Each layer corresponds to a constitutional floor. Each floor is non-substitutable.

## The Three Layers

| Layer | Domain | Testing Discipline | Floor | Failure Mode |
|---|---|---|---|---|
| **Semantic** | Meaning, intent, interpretation | Qualitative — NLP proxies, thematic fidelity | **F2 TRUTH** | Drift, hallucination, misinterpretation |
| **Deterministic** | Reproducibility, math, decay | Quantitative — statistical rigor, exponential decay | **F7 CONFIDENCE CAP** + **F8 LAW** | Non-reproducibility, hidden state, opacity |
| **Witnessed** | Authority, sovereignty, sealing | Quantum-style — multiple observers, classical shadows | **F11 AUDIT** + **F13 SOVEREIGN** | Single-witness corruption, sealed-but-wrong |

## Source

From "Paradigms of Epistemology and Measurement: A Comparative Analysis of Qualitative, Quantitative, and Quantum Methodologies" (2026), companion paper to **DMF** (arXiv:2606.03463), section on *The Geometry of Error Paradigms*:

> "In qualitative research architectures, system errors stem primarily from human misinterpretation, cognitive bias, generative model drift, and a lack of thematic trustworthiness. In quantitative benchmarking and classical computation, errors arise strictly from flawed deterministic logic or localized statistical hardware noise. In complex quantum systems, errors are inescapable physical and environmental realities: rapid decoherence, incoherent systemic noise, and SPAM errors degrade the incredibly fragile superposition of the physical qubit itself."

## Why Three Layers (Not One)

A claim can be:

- **Semantically faithful** (interpreted correctly) but **deterministically corrupt** (computed from wrong axes — e.g., wall-clock decay instead of interaction-count)
- **Deterministically clean** (reproducible) but **semantically empty** (a correct calculation of a meaningless question)
- **Both faithful and clean** but **single-witnessed** (one observer, no triangulation)

Each failure is invisible to the other two layers. Hence: **non-compensatory.**

## Doctrine Rules

### Rule 1 — Every SEAL must carry all three layers

A F13 SEAL on any artifact MUST include:

1. **Semantic tag** — `[OBS]` / `[DER]` / `[INT]` / `[SPEC]` / `[UNKNOWN]` (F2)
2. **Deterministic attestation** — proof that the same input produces the same output (F7/F8)
3. **Tri-witness ledger** — three independent witnesses with W³ ≥ 0.70 (F11/F13)

Single-witness SEAL is **prohibited**.

### Rule 2 — Errors inherit from layer, not domain

| Error Symptom | Likely Layer |
|---|---|
| "I think the user meant X" (over-interpretation) | Semantic |
| "Same input, different output" (non-reproducibility) | Deterministic |
| "Three sources say the same thing — must be true" (herding) | Witnessed |

When debugging, identify layer first. Don't conflate.

### Rule 3 — Quantum metaphors are constitutional, not literal

The third layer uses **quantum-measurement metaphors** (Bell sampling, classical shadows, SPAM errors, GST) not because arifOS runs on quantum hardware, but because:

- **Quantum states cannot be directly read** — observation collapses them. **Audit changes context.** Same truth.
- **Bell sampling** produces classical shadows from **N identical copies** measured transversally — our **W³ tri-witness** is exactly this.
- **SPAM errors** (State Preparation And Measurement) — **noise in epistemic labeling** corrupts truth before measurement.
- **GST (Gate Set Tomography)** — **audit the audit method itself.** Apply W³ to `forge_witness` periodically.

## Cross-references

- `bell-sampling-as-tri-witness.md` — formal proof that W³ ≡ Bell sampling
- `survival-score-logistic-projection.md` — memory scoring layer (Quantitative)
- `recall-time-nlp.md` — semantic layer discipline
- `../skills/governance/spatial-intelligence-substrate/SKILL.md` — concrete skill using this doctrine
- `../skills/governance/observe-ground/SKILL.md` — F2 enforcement

## Provenance

- **Authored**: 2026-08-04 21:30 MYT, Hermes (arifOS edge bridge)
- **Source paper**: arXiv:2606.03463 §11–12 + Stabile & Zimuel 2026
- **Sovereign sign-off**: pending F13 (Arif)
- **Hash chain**: to be sealed to VAULT999 upon F13 acceptance