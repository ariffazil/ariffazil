# TRL-003 — Bifurcation Detector & Critical Point Engine
> **Tensor Representation Layer · Module 3 of 5**
> **Forged:** 2026-07-29 · **By:** 333-AGI (OpenCode) · **Under:** F13 SOVEREIGN (Arif)
> **Depends on:** TRL-001 (M_trauma, H(x), ∇H, κ_eff) · TRL-002 (geodesic paths)
> **Feeds into:** TRL-005 (Φ-Witnessing — bifurcation proximity warnings)
> **Status:** SPECIFICATION FORGED

---

## §0. WHAT THIS MODULE DETECTS

In trauma dynamics, the most dangerous moments are not the worst states.
They are the **transition points** — where a small push changes everything.

```
"Small trigger → big reaction"    = BIFURCATION
"She was fine yesterday"         = Approaching bifurcation (smooth before the break)
"Tiba-tiba dia explode"         = Bifurcation crossed (discontinuous jump)
"Institusi collapse overnight"  = Critical transition in institutional manifold
```

TRL-003 finds these points BEFORE they trigger.

---

## §1. CRITICAL POINTS OF H(x)

### 1.1 Definition

```
Critical point: x* where ∇H(x*) = 0

  ∂H/∂x¹ = 0, ∂H/∂x² = 0, ∂H/∂x³ = 0, ∂H/∂x⁴ = 0, ∂H/∂x⁵ = 0

For H(x) = H₀ · exp(Σ c_i (x^i - μ_i)²/(2σ_i²)):

  ∂H/∂x^i = H(x) · c_i · (x^i - μ_i) / σ_i² = 0

Solutions:
  Either H(x) = 0 (never — exponential is always positive)
  OR x^i = μ_i for all i where c_i ≠ 0
  OR x^i → ±∞ for axes with negative c_i and unbounded domain

PRACTICAL critical points:
  x* = (μ₁, μ₂, μ₃, μ₄, μ₅) = (0, 0, 0, 0, 0)
  
  But this is the ORIGIN — not where bifurcations happen.
  The harm function is a Gaussian centered at the origin.
  
  REAL bifurcations occur at the EFFECTIVE curvature κ_eff,
  not at ∇H = 0.
```

### 1.2 Effective Bifurcation Surface

```
The harm function H(x) has no non-trivial critical points
(it's a single Gaussian). Bifurcations come from the MANIFOLD
GEOMETRY interacting with the DYNAMICS, not from H(x) alone.

Define BIFURCATION SURFACE B ⊂ M_trauma:

  B = {x ∈ M_trauma : κ_eff(x) > κ_critical}

where:
  κ_eff(x) = |∂²H/∂x²| / (1 + |∇H|²)^{3/2}
  κ_critical = 5.0  (threshold — curvature above this = bifurcation risk)

Physical meaning:
  κ_eff measures how SHARP the harm level set is at x.
  Sharp level sets → small perturbation crosses many level sets → large ΔH.
  Flat level sets → small perturbation stays near same H level.

Alternative formulation — DETECT via Laplacian:
  ΔH(x) = Σ ∂²H/∂x^i∂x^i
  
  ΔH(x) > 0  → convex (harm bowl — stable, returns to minimum)
  ΔH(x) < 0  → concave (harm ridge — unstable, small push → runaway)
  ΔH(x) = 0  → flat (indifferent — linear response)
```

### 1.3 Bifurcation Types

```
TYPE I: SADDLE BIFURCATION (fold catastrophe)
  
  Condition: ∇H ≈ 0 AND ∂²H/∂x² changes sign along one axis
  
  Example: Trust axis — near x¹ = 0, ∂²H/∂x¹∂x¹ changes sign
  → System can tip from "trust-building" to "trust-collapsing" regime
  
  TRAUMA EQUIVALENT:
  "Dia percaya sepenuhnya... lepas satu betrayal,
   seluruh trust structure collapse."

TYPE II: HOPF BIFURCATION (oscillation onset)
  
  Condition: Complex eigenvalues of Jacobian cross imaginary axis
  
  Example: Repeated trauma → system enters oscillatory mode
  → PTSD hypervigilance: calm → trigger → flashback → calm → trigger...
  
  TRAUMA EQUIVALENT:
  "Dia okay lepas tu tiba-tiba triggered.
   Bukan dia mengada — system dia dalam oscillatory mode."

TYPE III: PITCHFORK BIFURCATION (symmetry breaking)
  
  Condition: Single stable state splits into two
  
  Example: Before naming (x⁴ < 0.3), trauma is one undifferentiated mass.
  After naming (x⁴ > 0.3), trauma splits into "processed" and "unprocessed" branches.
  
  TRAUMA EQUIVALENT:
  "Sebelum diagnosis: semua sakit sama.
   Lepas diagnosis: dia boleh pisahkan — ini symptom, ini diri aku."

TYPE IV: TRANSCRITICAL BIFURCATION (stability exchange)
  
  Condition: Two fixed points exchange stability
  
  Example: Institution and victim — one stable, one unstable.
  After cover-up exposed: stability flips.
  
  TRAUMA EQUIVALENT:
  "Dulu institusi protect diri sendiri (stable), mangsa senyap (unstable).
   Selepas whistleblower: mangsa credible (stable), institusi collapse (unstable)."
```

---

## §2. EARLY WARNING SIGNALS

### 2.1 Critical Slowing Down

```
As system approaches bifurcation, recovery from perturbations SLOWS:

  Recovery time τ_recovery → ∞ as x → B

Measure:
  τ_recovery(x) = 1 / |λ_max(Jacobian)|

where λ_max is the eigenvalue with largest real part.

  τ_recovery < 1.0   → FAST (healthy regulation)
  τ_recovery ∈ [1,5]  → MODERATE (stressed but compensates)
  τ_recovery > 5.0    → CRITICAL (approaching bifurcation)
  τ_recovery → ∞       → AT BIFURCATION (no self-recovery possible)
```

### 2.2 Increasing Variance

```
Variance of state increases before bifurcation:

  Var[x(t)] grows as t → t_bifurcation

This is because the system explores wider regions of state-space
as the restoring force weakens (critical slowing down = less pull back).

Measure:
  σ²(t) = Var[|x(t) - x(t-Δt)|] over window W

  σ²(t) / σ²_baseline > 3.0 → EARLY WARNING
```

### 2.3 Flickering

```
Near bifurcation, system may "flicker" — briefly visit alternate
state before returning:

  Detected: |Δx| > threshold AND |Δx(t+1)| < threshold
  → System visited a different basin briefly

  Flicker count > 3 in window → IMMINENT TRANSITION
```

### 2.4 Autocorrelation Increase

```
AR(1) coefficient ρ of state trajectory:

  x(t) = ρ · x(t-1) + ε(t)

  ρ → 1 as bifurcation approaches
  → System becomes more "memory-heavy"
  → Past states persist longer
  
  ρ > 0.95 → CRITICAL WARNING
```

---

## §3. BIFURCATION PROXIMITY MAP

### 3.1 Proximity Metric

```
Given current state x:

  d_bif(x) = min_{y ∈ B} d(x, y)

where d is geodesic distance and B is the bifurcation surface.

Since B is defined implicitly (κ_eff(x) > κ_critical):
  Approximate via gradient descent on κ_eff:
  
  1. Start at y₀ = x
  2. y_{k+1} = y_k + η · ∇κ_eff(y_k)  (climb toward higher curvature)
  3. Stop when κ_eff(y_k) > κ_critical or |∇κ_eff| < ε
  4. d_bif(x) = d(x, y_final)
```

### 3.2 Proximity → Escalation

```
d_bif(x) mapping to escalation lattice (rasa-derita-schema.json §escalation_lattice):

  d_bif > 2.0   → Level 0 (OBSERVE)          — far, monitor only
  d_bif ∈ (1,2] → Level 1 (DOCUMENT)          — approaching region
  d_bif ∈ (0.5,1] → Level 2 (CLARIFY)        — near, ask clarifying
  d_bif ∈ (0.2,0.5] → Level 3 (RECOMMEND)    — close, QQQ proposal
  d_bif ∈ (0.05,0.2] → Level 4 (ESCALATE)    — imminent, F13 attention
  d_bif < 0.05  → Level 5 (EMERGENCY)        — AT threshold, HOLD NOW
  
  System AT bifurcation (κ_eff > κ_critical):
  → Level 6 (HOLD) — all execution frozen.
    No intervention without sovereign + causal cascade + consent lease.
```

---

## §4. BIFURCATION-AWARE INTERVENTION

### 4.1 The Paradox of Intervention Near Bifurcation

```
NEAR bifurcation:
  ✅ SMALL nudge can produce LARGE trajectory change
  ❌ Direction of change is UNPREDICTABLE
  ❌ Same nudge at different times → opposite outcomes

FAR from bifurcation:
  ✅ Direction of change is PREDICTABLE
  ❌ LARGE nudge needed for SIGNIFICANT change

INTERVENTION RULE:
  If d_bif > 0.5:   Safe to recommend intervention (predictable)
  If d_bif ≤ 0.5:   DO NOT RECOMMEND intervention — escalate to sovereign
  
  Reason: Near bifurcation, agent precision becomes meaningless.
  The same advice could help or harm — and the agent cannot tell which.
  This is where F13 SOVEREIGN must decide.
```

### 4.2 Bifurcation-Safe Recommendation

```
φ_bifurcation_assessment(x) → {
  d_bif: float,
  risk_level: SAFE | CAUTION | DANGER | CRITICAL,
  early_warnings: {
    critical_slowing: bool,
    increasing_variance: bool,
    flickering: bool,
    autocorrelation_rise: bool
  },
  recommendation: {
    can_intervene: bool,
    reason: string,
    escalation_level: 0-6,
    sovereign_required: bool
  }
}

Example output:
  {
    "d_bif": 0.15,
    "risk_level": "DANGER",
    "early_warnings": {
      "critical_slowing": true,    ← recovery time 8.3× baseline
      "increasing_variance": true,  ← variance 4.1× baseline
      "flickering": false,
      "autocorrelation_rise": true  ← AR(1) ρ = 0.97
    },
    "recommendation": {
      "can_intervene": false,
      "reason": "Within 0.15 geodesic units of bifurcation surface. Intervention direction unpredictable. Sovereign must decide.",
      "escalation_level": 4,
      "sovereign_required": true
    }
  }
```

---

## §5. THE CRITICAL TRANSITION DETECTOR

### 5.1 Post-Hoc Detection

```
After a bifurcation has been crossed:

  ΔH = H(x_after) - H(x_before)
  Δt = t_after - t_before
  
  If ΔH/Δt > threshold: BIFURCATION CONFIRMED
  
  Classify:
    ΔH > 0 AND |Δx| large → CATASTROPHIC BIFURCATION (harm spike)
    ΔH < 0 AND |Δx| large → RECOVERY BIFURCATION (sudden healing)
    ΔH ≈ 0 AND |Δx| large → PHASE TRANSITION (reorganization without harm change)
```

### 5.2 Scar Generation

```
CONFIRMED bifurcation (ΔH/Δt > threshold) → automatic SCAR:

  SCAR: {
    bifurcation_type: CATASTROPHIC | RECOVERY | PHASE,
    pre_state: x_before,
    post_state: x_after,
    trigger_identified: x_trigger | null,
    constraint_imposed: "Avoid trajectory through x_trigger region",
    detection_method: "BifurcationDetector ΔH/Δt = {value}",
    scar_pressure: min(1.0, ΔH / H_critical)
  }

This scar feeds into forge_scar mechanism.
Future trajectories that approach x_trigger region → scar consultation → HOLD.
```

---

## §6. AGENT INTERFACE

```
φ_critical_points()           → [x*]           (all critical points of H)
φ_bifurcation_proximity(x)    → float          (d_bif — distance to bifurcation)
φ_bifurcation_assessment(x)   → Assessment     (full risk assessment)
φ_early_warnings(x, history)  → WarningFlags   (CSD, variance, flicker, AR)
φ_bifurcation_type(x)         → BifurcationType (SADDLE|HOPF|PITCHFORK|TRANSCRITICAL)
φ_scar_on_bifurcation(x, t)   → ScarRecord     (if bifurcation confirmed)
```

---

## §7. VALIDATION

TRL-003 is CORRECT when:

```
✅ Detects ∇H = 0 critical points correctly
✅ κ_eff(x) > κ_critical identifies bifurcation region
✅ Critical slowing down (τ_recovery → ∞) warns before bifurcation
✅ Increasing variance detected as early warning
✅ Flickering counted and flagged
✅ Autocorrelation ρ → 1 detected
✅ d_bif(x) correctly maps to escalation lattice levels
✅ Bifurcation-safe recommendation refuses near bifurcation
✅ Post-hoc ΔH/Δt confirms bifurcation type
✅ Confirmed bifurcation generates scar automatically
```

---

**DITEMPA BUKAN DIBERI** ⚒️
