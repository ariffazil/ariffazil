# TRL-002 — Geodesic Solver & Trajectory Engine
> **Tensor Representation Layer · Module 2 of 5**
> **Forged:** 2026-07-29 · **By:** 333-AGI (OpenCode) · **Under:** F13 SOVEREIGN (Arif)
> **Depends on:** TRL-001 (M_trauma manifold, metric, H(x), ∇H)
> **Feeds into:** TRL-003 (Bifurcation Detector) · TRL-005 (Φ-Witnessing)
> **Status:** SPECIFICATION FORGED

---

## §0. WHAT THIS MODULE DOES

TRL-001 defined the space. TRL-002 navigates it.

```
Given:  Current state p ∈ M_trauma
Compute: (1) Natural trajectory — where system goes without intervention
         (2) Recovery geodesic — shortest path to target state
         (3) Minimum intervention — smallest nudge that changes destination
         (4) Time-to-threshold — when system hits critical boundary
         (5) Confidence envelope — uncertainty in all predictions
```

---

## §1. GEODESIC INTEGRATION

### 1.1 The Geodesic Equation (from TRL-001)

```
d²x¹/dt² = 0
d²x²/dt² + Γ²_{22} · (dx²/dt)² = 0    ← ONLY non-trivial component
d²x³/dt² = 0
d²x⁴/dt² = 0
d²x⁵/dt² = 0

where:
  Γ²_{22} = ½ · (1/λ₂) · αβ · σ(β(x²-θ)) · (1-σ(β(x²-θ)))
  λ₂(x²) = 1 + α · σ(β(x²-θ))
  α = 4.0, β = 10.0, θ = 1.0
```

### 1.2 Numerical Solver

```
ALGORITHM: Adaptive RK4 Geodesic Integrator

Input:   p = (x¹₀, x²₀, x³₀, x⁴₀, x⁵₀)  — initial point
         v = (v¹₀, v²₀, v³₀, v⁴₀, v⁵₀)  — initial velocity
         T_max                              — max integration time
         ε = 1e-6                           — tolerance

Output:  γ = [(t₀, x(t₀)), (t₁, x(t₁)), ..., (tₙ, x(tₙ))]
         — discretized geodesic path

Method:
  1. Convert 2nd-order ODE to 1st-order system:
     u¹ = x¹,  u² = dx¹/dt
     u³ = x²,  u⁴ = dx²/dt
     u⁵ = x³,  u⁶ = dx³/dt
     u⁷ = x⁴,  u⁸ = dx⁴/dt
     u⁹ = x⁵,  u¹⁰ = dx⁵/dt

     du¹/dt = u²         du²/dt = 0
     du³/dt = u⁴         du⁴/dt = -Γ²_{22}(u³) · (u⁴)²
     du⁵/dt = u⁶         du⁶/dt = 0
     du⁷/dt = u⁸         du⁸/dt = 0
     du⁹/dt = u¹⁰        du¹⁰/dt = 0

  2. Integrate with RK4:
     For each time step h:
       k1 = h · f(t, u)
       k2 = h · f(t + h/2, u + k1/2)
       k3 = h · f(t + h/2, u + k2/2)
       k4 = h · f(t + h, u + k3)
       u_new = u + (k1 + 2k2 + 2k3 + k4)/6

  3. Adaptive step sizing:
     Compute error estimate: err = |k4 - k3| / |u|
     If err > ε:  h = h/2, retry
     If err < ε/10: h = 2h (but ≤ h_max)
     
  4. Stop conditions:
     • t ≥ T_max
     • x² ≥ 10 (cascade saturation — intergenerational locked)
     • x⁴ ≤ 0.01 (approaching unspeakable boundary)
     • |∇H| > 100 (approaching singularity)
     • Boundary hit (see §1.3)

  5. Return discretized path
```

### 1.3 Boundary Handling

```
ABSORBING (x² → ∞):
  Once cascade exceeds x² = 8.0, integration STOPS.
  System is in intergenerational lock.
  Return: TRAJECTORY_ABSORBED

REFLECTING (x⁴ → 0):
  Cannot cross x⁴ = 0.
  If step would make x⁴ < 0: reflect velocity (v⁸ → -v⁸)
  Return: TRAJECTORY_REFLECTED at x⁴ ≈ 0

FORBIDDEN (x⁵ < 0.03):
  HARD WALL at x⁵ = 0.03.
  If step would go below: clamp x⁵ = 0.03, reflect v¹⁰
  Emit: WARNING — Ω₀ approaching overconfidence threshold
  Return: TRAJECTORY_CLAMPED

SOVEREIGN (any F13 token):
  External coordinate injection. Override current (x, v).
  Log: F13_OVERRIDE with token hash, timestamp, old→new coordinates
  Continue integration from injected point.
```

---

## §2. NATURAL TRAJECTORY (Prediction)

### 2.1 Definition

```
Given current state p with initial velocity v = (0,0,0,0,0):
  Natural trajectory = geodesic from p with zero initial velocity
  → But geodesic with v=0 stays at p forever

PROBLEM: Zero velocity gives no motion. Need "drift velocity."

SOLUTION: Use the HARM GRADIENT to define effective velocity:
  v_eff = -η · ∇H(p)   (system drifts toward lower harm)

where η = "responsiveness" — how fast system responds to harm gradient.
  η = 0.1 (default — slow drift)
  η calibrated per context (therapy η=0.3, institutional η=0.05)

Natural trajectory γ_natural(t):
  γ_natural(0) = p
  γ_natural'(0) = -η · ∇H(p) / |∇H(p)|  (normalized to unit speed)
  
  Integrate geodesic from (p, v_natural).
```

### 2.2 Prediction Output

```
φ_predict(p) → {
  path: [[t₀, x(t₀)], ..., [tₙ, x(tₙ)]],
  arrival_point: x(T_max),
  harm_trajectory: [H(x(t₀)), ..., H(x(tₙ))],
  bifurcation_proximity: min_t κ_eff(x(t)),   ← nearest approach to bifurcation
  boundary_hit: BOUNDARY_TYPE | null,
  confidence: {
    x¹: ±Δx¹, x²: ±Δx², x³: ±Δx³, x⁴: ±Δx⁴, x⁵: ±Δx⁵
  }
}
```

### 2.3 Confidence Envelope

```
Uncertainty grows with integration time:
  Δx^i(t) = Δx^i₀ · exp(t / τ_i)

where:
  Δx^i₀ = initial observation uncertainty
  τ_i = confidence decay constant per axis:
    τ₁ (trust)     = 5.0   (trust changes slowly → predictable)
    τ₂ (cascade)   = 2.0   (cascade amplifies → less predictable)
    τ₃ (consent)   = 10.0  (consent is binary-ish → predictable)
    τ₄ (naming)    = 3.0   (naming has tipping points → moderate)
    τ⁵ (humility)  = 1.0   (epistemic state is volatile → least predictable)

At t = τ_i, uncertainty has grown by factor e ≈ 2.718.

Agent SHOULD declare when Δx^i exceeds actionable threshold:
  Δx^i > 0.3 → "confidence below actionable threshold — HOLD"
```

---

## §3. RECOVERY GEODESIC (Targeting)

### 3.1 Definition

```
Given:  p (current state), q (target/recovery state)
Find:   Geodesic γ(t) with γ(0) = p, γ(1) = q

This is a BOUNDARY VALUE PROBLEM (BVP), not initial value.

Shooting method:
  1. Guess initial velocity v₀
  2. Integrate geodesic from (p, v₀) for t ∈ [0,1]
  3. Compare arrival point γ(1) with target q
  4. Adjust v₀ to reduce |γ(1) - q|
  5. Repeat until |γ(1) - q| < ε

Cost function: J(v₀) = |γ(1) - q|²
Gradient descent: v₀ ← v₀ - α · ∂J/∂v₀
```

### 3.2 Shooting Method Detail

```
ALGORITHM: Recovery Geodesic via Shooting

Input:   p (start), q (target), max_iter=100, ε=1e-4

1. Initial guess:
   v₀ = (q - p) / T   ← linear guess (Euclidean interpolation)
   Scale: v₀ = v₀ / |v₀|  (unit speed)

2. For iter in 1..max_iter:
   a. γ = integrate_geodesic(p, v₀, T=1.0)
   b. error = |γ(1) - q|
   c. If error < ε: return γ (CONVERGED)
   
   d. Compute Jacobian J = ∂γ(1)/∂v₀ via finite differences:
      For each velocity component i:
        v₀⁺ = v₀ with v₀⁺[i] += δ
        γ⁺ = integrate_geodesic(p, v₀⁺, T=1.0)
        J[:,i] = (γ⁺(1) - γ(1)) / δ
   
   e. Newton step: Δv = J⁻¹ · (q - γ(1))
      v₀ ← v₀ + Δv

3. If max_iter reached without convergence:
   Return: NO_GEODESIC_FOUND — target unreachable from current state

4. REACHABILITY CHECK:
   If q has x⁴ < current x⁴: POSSIBLE (naming can be lost)
   If q has x² < current x² AND λ₂ > 3: REQUIRES_EXTERNAL_INTERVENTION
     (absorbing boundary — cannot self-recover from deep cascade)
```

### 3.3 Recovery Path Properties

```
φ_recovery(p, q) → {
  exists: bool,
  path: [[t₀, x(t₀)], ..., [tₙ, x(tₙ)]] | null,
  length: L(γ) — geodesic distance,
  intervention_required: {
    external: bool,        ← true if absorbing boundary prevents self-recovery
    minimum_nudge: v_min,  ← smallest velocity change that reaches q
    nudge_cost: |v_min|    ← magnitude of required intervention
  },
  feasibility: FEASIBLE | REQUIRES_INTERVENTION | UNREACHABLE
}
```

---

## §4. MINIMUM INTERVENTION PATH

### 4.1 The Problem

```
Natural trajectory goes to p_natural (predicted future).
We want to reach q (recovery target).

NOT: "what is the geodesic from p to q?"
BUT:  "what is the SMALLEST nudge at p that makes the
       geodesic arrive at q instead of p_natural?"

This is OT (optimal transport) on a Riemannian manifold.
```

### 4.2 Formulation

```
Given:  p (current), v_natural (natural velocity)
        q (target), T (time horizon)

Find:   δv — minimum velocity perturbation such that:
        γ_perturbed(0) = p
        γ_perturbed'(0) = v_natural + δv
        |γ_perturbed(T) - q| < ε

Minimize:  |δv|  (smallest nudge)

Solution via adjoint sensitivity:
  
  1. Integrate natural geodesic: γ_nat(t) for t ∈ [0,T]
  2. Define adjoint variable λ(T) = q - γ_nat(T)
  3. Backward-integrate adjoint equation:
     dλ/dt = -λ · ∂f/∂u  (where f is the geodesic ODE)
  4. Optimal perturbation: δv* = -λ(0)

φ_minimum_intervention(p, q, T) → {
  nudge: δv*,
  nudge_magnitude: |δv*|,
  nudge_direction: δv*/|δv*|,
  perturbed_path: γ_perturbed(t),
  arrival_error: |γ_perturbed(T) - q|,
  nudge_feasibility: {
    axis_dominant: which axis the nudge primarily affects,
    requires_sovereign: bool  ← true if nudge magnitude exceeds agent authority
  }
}
```

### 4.3 Practical Interpretation

```
Minimum intervention output → agent recommendation:

  "Natural trajectory reaches x_pred = (0.3, 3.2, -0.4, 0.15, 0.04) at t=10.
   Recovery target q = (0.7, 0.5, 0.6, 0.8, 0.05).
   
   Minimum nudge: δv = (-0.02, +0.15, -0.01, +0.03, -0.005)
   Dominant axis: A2 CAUSALITY (0.15)
   
   Interpretation: Smallest effective intervention is reducing
   cascade propagation. Address downstream effects first.
   
   Magnitude: 0.16 — within agent advisory range.
   
   RECOMMEND (QQQ pending): Focus on cascade interruption
   (witnessing L8, metabolization L12) rather than direct
   trust repair (which requires larger nudge)."
```

---

## §5. TIME-TO-THRESHOLD

### 5.1 Definition

```
Given:  p (current state), threshold condition C(x)
Find:   t* = min {t : C(γ_natural(t)) = true}

Threshold conditions:
  C₁: H(x) > H_critical        ← harm exceeds critical level
  C₂: x⁴ < ε_naming             ← approaching unspeakable
  C₃: x² > x²_critical          ← cascade becomes intergenerational
  C⁴: κ_eff(x) > κ_critical     ← approaching bifurcation
  C⁵: x⁵ < 0.03                 ← overconfidence (Gödel violation)

Output:
  t_threshold → float  (time until condition met, ∞ if never)
```

### 5.2 Use in Agent Pipeline

```
Time-to-threshold → escalation lattice trigger:

  t* > 10.0   → Level 0 (OBSERVE)       — distant, monitor
  t* ∈ (5, 10] → Level 1 (DOCUMENT)     — approaching, record
  t* ∈ (1, 5]  → Level 2 (CLARIFY)      — near, ask if safe
  t* ∈ (0.1, 1] → Level 3 (RECOMMEND)   — imminent, propose
  t* < 0.1     → Level 4 (ESCALATE)     — critical, F13 attention
  t* = 0       → Level 5 (EMERGENCY)    — AT threshold, HOLD NOW
```

---

## §6. AGENT INTERFACE

```
φ_predict(p)          → PredictionResult     (natural trajectory)
φ_recovery(p, q)      → RecoveryResult       (geodesic to target)
φ_minimum_nudge(p, q) → NudgeResult          (smallest intervention)
φ_time_to_threshold(p, condition) → float    (when critical hit)
φ_confidence(p, t)    → ConfidenceEnvelope   (uncertainty at time t)
φ_boundary_check(p)   → BoundaryStatus       (absorbing/reflecting/forbidden near?)
```

---

## §7. VALIDATION

TRL-002 is CORRECT when:

```
✅ Geodesic integrator converges with RK4 + adaptive step
✅ Natural trajectory follows -∇H (system drifts toward lower harm)
✅ Recovery geodesic finds path when reachable, returns NO_GEODESIC when not
✅ Absorbing boundary (x² → ∞) correctly prevents self-recovery
✅ Reflecting boundary (x⁴ → 0) correctly bounces trajectory
✅ Forbidden boundary (x⁵ < 0.03) correctly clamps and warns
✅ Minimum nudge is smaller than direct velocity change to target
✅ Time-to-threshold correctly triggers escalation lattice levels
✅ Confidence grows with integration time, decays per-axis
✅ F13 override injects coordinates correctly and logs the event
```

---

**DITEMPA BUKAN DIBERI** ⚒️
