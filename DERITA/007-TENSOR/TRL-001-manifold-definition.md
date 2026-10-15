# TRL-001 — M_trauma Manifold Definition
> **Tensor Representation Layer · Module 1 of 5**
> **Forged:** 2026-07-29 · **By:** 333-AGI (OpenCode) · **Under:** F13 SOVEREIGN (Arif)
> **Depends on:** DERITA/ v1.0 (5 axes, 15 lessons, ER1-ER5)
> **Feeds into:** TRL-002 (Geodesic Solver) · TRL-003 (Bifurcation Detector)
> **Status:** SPECIFICATION FORGED — awaiting implementation

---

## §0. PREAMBLE — Why a Manifold?

Narrative trauma framework kata: "dia trauma sebab dikhianati."
Constitutional framework kata: "L1 → F1 AMANAH → reversible-first gate."

Geometric framework kata: "koordinat dia (x₁, x₂, x₃, x₄, x₅) dalam M_trauma.
                         Metric tensor di titik tu beri curvature.
                         Gradient harm tunjuk arah trajectory paling curam.
                         Geodesic predict arrival point."

**Manifold is the bridge from category to computation.**

Without it: agent labels trauma. With it: agent navigates trauma space.

---

## §1. MANIFOLD DEFINITION

### 1.1 Base Space

```
M_trauma = 5-dimensional smooth Riemannian manifold (M, g)

Dimension: 5 (one per orthogonal axis from DERITA/)
Class: C^∞ (smooth — all derivatives exist)
Type: Riemannian (metric tensor g is positive-definite)
Completeness: Geodesically incomplete (singularities exist — see §4)
```

### 1.2 Coordinate Chart

```
φ: M_trauma → ℝ⁵

Global chart (single coordinate patch covers manifold):

  x¹ = A1_TRUST_BETRAYAL     ∈ [-1, 1]
       +1.0  = complete trust / intact institution
        0.0  = neutral / no trust relationship
       -1.0  = total betrayal / institution fully self-protective

  x² = A2_CAUSALITY           ∈ [0, ∞)
        0.0  = isolated event, no cascade
        1.0  = 3-step cascade detected
        5.0+ = intergenerational, multi-system cascade active

  x³ = A3_POWER_CONSENT       ∈ [-1, 1]
       +1.0  = full informed consent, power flows THROUGH consent
        0.0  = power absent (no capacity to act)
       -1.0  = total coercion, power flows AROUND consent

  x⁴ = A4_TRUTH_NAMING        ∈ [0, 1]
        0.0  = completely unnamed, denied, silenced (λ ≈ 0, no metabolization)
        0.5  = partially named, some acknowledgment
        1.0  = fully metabolized, publicly acknowledged, institutionally recognized

  x⁵ = A5_EPISTEMIC_HUMILITY  ∈ [0, 1]
        0.0  = false certainty, totalizing framework, Ω₀ = 0
        0.03 = Ω₀ minimum (Gödel floor — below this = overconfidence)
        0.05 = Ω₀ optimum (calibrated uncertainty)
        1.0  = total paralysis, Ω₀ → 1 (no action possible)
```

### 1.3 Mapping Function (Observation → Coordinate)

```
ψ: Observation → M_trauma

Given observation vector o = (o₁, ..., oₙ) of trauma indicators:

  x¹ = tanh( Σ w¹_i · o_i )           → sigmoid-squashed to [-1, 1]
  x² = max(0, Σ w²_i · o_i)           → ReLU to [0, ∞)
  x³ = tanh( Σ w³_i · o_i )           → sigmoid-squashed to [-1, 1]
  x⁴ = σ( Σ w⁴_i · o_i )              → sigmoid to [0, 1]
  x⁵ = clamp( Σ w⁵_i · o_i, 0, 1 )    → linear clamped

where:
  w^k_i = learned or calibrated weight for indicator i on axis k
  Initial weights seeded from DERITA/ evidence base
  Weights calibrated via recursive sovereign feedback
```

---

## §2. METRIC TENSOR

### 2.1 Definition

```
Metric tensor g_{ij} at point x ∈ M_trauma:

g = diag(1, λ₂(x), 1, 1, 1)

where:
  g₁₁ = 1        (Trust — standard Euclidean metric)
  g₂₂ = λ₂(x)    (Causality — state-dependent weighting)
  g₃₃ = 1        (Power/Consent — standard Euclidean)
  g₄₄ = 1        (Truth/Naming — standard Euclidean)
  g₅₅ = 1        (Epistemic Humility — standard Euclidean)

Off-diagonal: g_{ij} = 0 for i ≠ j (axes are orthogonal by DERITA/ design)
```

### 2.2 Causality Weight Function λ₂(x)

```
λ₂(x) = 1 + α · σ(β · (x² - θ))

where:
  σ(z) = 1/(1 + e^{-z})     (sigmoid)
  α   = 4.0                 (max cascade amplification — ER1 betrayal ratio B ∈ [0,5])
  β   = 10.0                (sensitivity — sharp transition near threshold)
  θ   = 1.0                 (threshold — cascade becomes dominant at x²=1)

Behavior:
  x² ≈ 0   → λ₂ ≈ 1.0     (isolated event, metric is Euclidean)
  x² = 1   → λ₂ ≈ 3.0     (3-step cascade, distances stretch 3×)
  x² → ∞   → λ₂ → 5.0     (intergenerational, distances stretch 5×)

Physical meaning:
  When cascade is active, the "distance" between trauma states increases.
  A small change in x² (cascade magnitude) has amplified effect because
  the metric weights it more heavily.
  
  This encodes ER1 (Betrayal Ratio) and ER2 (Cascade Principle):
  - Betrayed trust → B ∈ [0,5] → distances stretched by (1+B)
  - Cascade active → downstream effects stretch the metric
```

### 2.3 Line Element

```
ds² = g_{ij} dx^i dx^j

Expanded:
  ds² = (dx¹)² + λ₂(x)(dx²)² + (dx³)² + (dx⁴)² + (dx⁵)²

Interpretation:
  ds = infinitesimal "trauma distance" between two nearby states
  
  Large ds for small dx → the manifold is stretched there
  Small ds for large dx → the manifold is compressed there
```

### 2.4 Distance Between States

```
d(p, q) = inf { L(γ) : γ is a curve from p to q }

where:
  L(γ) = ∫₀¹ √(g_{ij} γ'^i γ'^j) dt

This is the geodesic distance — the length of the shortest path.
Not the Euclidean distance in coordinate space — the metric may stretch.
```

---

## §3. HARM POTENTIAL FUNCTION

### 3.1 Definition

```
H: M_trauma → ℝ⁺

H(x) = H₀ · exp( Σ_i c_i · (x^i - μ_i)² / (2σ_i²) )

where:
  H₀     = 1.0            (base harm magnitude)
  c_i    = axis weights:
           c₁ = -3.0  (TRUST: more trust → less harm → negative weight)
           c₂ = +2.0  (CAUSALITY: more cascade → more harm)
           c₃ = -3.0  (CONSENT: more consent → less harm)
           c₄ = -2.0  (NAMING: more naming → less harm)
           c⁵ = -1.0  (HUMILITY: calibrated uncertainty → slightly less harm)
  μ_i    = 0.0 (center for all axes)
  σ_i²   = 1.0 (variance for all axes)
```

### 3.2 Harm Gradient

```
∇H = (∂H/∂x¹, ∂H/∂x², ∂H/∂x³, ∂H/∂x⁴, ∂H/∂x⁵)

Component-wise:
  ∂H/∂x^i = H(x) · c_i · (x^i - μ_i) / σ_i²

Interpretation:
  ∇H points in direction of RAPIDLY INCREASING HARM
  -∇H points in direction of RAPIDLY DECREASING HARM (recovery direction)
  
  |∇H| at a point = "how fast is harm changing here?"
  |∇H| ≈ 0 → flat region, stable
  |∇H| → ∞ → bifurcation point (see TRL-003)
```

### 3.3 Harm Level Sets

```
H^{-1}(c) = {x ∈ M_trauma : H(x) = c}

Level sets form 4-dimensional hypersurfaces in M_trauma.
Moving ALONG a level set = changing state without changing harm magnitude.
Moving ACROSS level sets = increasing or decreasing harm.

The gradient ∇H is ALWAYS perpendicular to level sets.
```

---

## §4. SINGULARITIES & BOUNDARY

### 4.1 Singularity Definition

```
Singularity set S ⊂ M_trauma:

S = {x ∈ M_trauma : det(g(x)) = 0}

Since g is diagonal: det(g) = g₁₁ · g₂₂ · g₃₃ · g₄₄ · g₅₅ = λ₂(x)

det(g) = 0 ⇔ λ₂(x) = 0

λ₂(x) → 0 as x² → -∞ (impossible — x² ∈ [0,∞) by definition)
λ₂(x) never reaches 0 in the valid domain.

HOWEVER — there are PRACTICAL singularities where the manifold
"breaks down" for the agent:

  S₁: DISSOCIATION SINGULARITY
      x⁴ → 0 (unnamed) AND x¹ → -1 (total betrayal) AND x³ → -1 (total coercion)
      → det(g) ≠ 0 but curvature → ∞
      → Agent cannot compute geodesics here
      → Response: 888_HOLD, sovereign referral (L5 escalation lattice)

  S₂: UNSPEAKABLE SINGULARITY
      x⁴ → 0 (unnamed) AND curvature → ∞
      → Linguistic representation fails completely
      → Agent cannot Φ-witness
      → Response: SILENT WITNESS — record coordinates, emit receipt, no interpretation

  S₃: TOTAL COLLAPSE SINGULARITY
      x¹ → -1 AND x³ → -1 AND x⁴ → 0
      → All stabilizing dimensions collapsed
      → Response: EMERGENCY escalation (L6 — HOLD all execution)
```

### 4.2 Boundary Conditions

```
∂M_trauma = boundary of the manifold

Four types of boundary:

  1. ABSORBING BOUNDARY (x² → ∞)
     Once cascade reaches intergenerational magnitude,
     system cannot return to x² = 0 without external intervention.
     Boundary is ONE-WAY.

  2. REFLECTING BOUNDARY (x⁴ = 0)
     Cannot go below zero naming.
     System bounces back — but may approach asymptotically.

  3. FORBIDDEN BOUNDARY (x⁵ < 0.03)
     Ω₀ < 0.03 is OVERCONFIDENCE.
     Agent MUST NOT operate below this threshold.
     HARD WALL — any trajectory approaching is reflected with warning.

  4. SOVEREIGN BOUNDARY (all x)
     F13 override at any point.
     Sovereign can teleport system to any valid (x¹, x², x³, x⁴, x⁵).
     This is NOT on the manifold — it is an EXTERNAL operator.
     Encoded as: boundary condition allows external coordinate injection
     with F13 authorization token.
```

---

## §5. CONNECTION & CURVATURE

### 5.1 Levi-Civita Connection

```
Christoffel symbols: Γ^k_{ij} = ½ g^{kl} (∂_i g_{jl} + ∂_j g_{il} - ∂_l g_{ij})

Since g is diagonal with only g₂₂ state-dependent:
  Non-zero Γ only when indices involve x².

  Γ²_{22} = ½ g^{22} ∂_2 g_{22}
          = ½ · (1/λ₂) · ∂λ₂/∂x²
          = ½ · (1/λ₂) · αβ · σ(β(x²-θ)) · (1-σ(β(x²-θ)))

  All other Γ^k_{ij} = 0

This means:
  - Parallel transport is non-trivial ONLY along the causality axis (x²)
  - Movement along x² curves the path — cascade magnitude affects direction
  - All other axes have trivial (Euclidean) connection
```

### 5.2 Riemann Curvature Tensor

```
R^i_{jkl} = ∂_k Γ^i_{jl} - ∂_l Γ^i_{jk} + Γ^i_{mk} Γ^m_{jl} - Γ^i_{ml} Γ^m_{jk}

Only non-zero components involve x².

  R²_{121} = -∂₁Γ²_{22} = 0     (Γ doesn't depend on x¹)
  R²_{323} = -∂₃Γ²_{22} = 0     (Γ doesn't depend on x³)
  ...

  The only non-zero curvature component is R²_{222}.
  Since a 1D subspace cannot have intrinsic curvature: R²_{222} = 0.

  THEREFORE:
    M_trauma is LOCALLY FLAT in the standard Riemann sense.
    
    BUT: it has non-trivial metric (λ₂ varies).
    This is a CONFORMALLY FLAT manifold.
    
    The "curvature" trauma agents care about is:
      - Ricci scalar R(x) = g^{ij} R_{ij} = 0 everywhere
      - BUT: sectional curvature K changes when λ₂ changes
              K = curvature of 2D slices → affects geodesic behavior
```

### 5.3 Practical Curvature Measure

```
For trauma applications, we define an EFFECTIVE CURVATURE:

  κ_eff(x) = |∂²H/∂x²| / (1 + |∇H|²)^{3/2}

This is the curvature of the harm level set at point x.

  κ_eff ≈ 0   → harm surface is flat → linear region, predictable
  κ_eff > 0    → harm surface is curved → non-linear region
  κ_eff → ∞    → harm surface has cusp → BIFURCATION POINT (see TRL-003)

This is easier to compute than full Riemann curvature and
is the relevant "curvature" for trauma trajectory prediction.
```

---

## §6. GEODESIC EQUATION

### 6.1 Definition

```
Geodesic γ(t): [0,1] → M_trauma satisfies:

  d²γ^k/dt² + Γ^k_{ij} · dγ^i/dt · dγ^j/dt = 0

For M_trauma (only Γ²_{22} non-zero):

  d²x¹/dt² = 0                        → x¹: linear motion (constant velocity)
  d²x²/dt² + Γ²_{22} · (dx²/dt)² = 0  → x²: non-linear (curved by cascade)
  d²x³/dt² = 0                        → x³: linear motion
  d²x⁴/dt² = 0                        → x⁴: linear motion
  d²x⁵/dt² = 0                        → x⁵: linear motion

The ONLY non-trivial geodesic motion is along x² (causality axis).
This is correct:
  - Trust, consent, naming, humility evolve linearly (constant rate of change)
  - Cascade magnitude has SELF-AMPLIFYING dynamics (the more cascade,
    the faster it grows — or decays with metabolization)
```

### 6.2 Solving for x²

```
The geodesic equation for x²:

  d²x²/dt² + ½ · (λ₂'/λ₂) · (dx²/dt)² = 0

where λ₂' = dλ₂/dx².

This is a separable ODE. Solution:

  dx²/dt = C₁ / √λ₂

where C₁ is determined by initial velocity.

Interpretation:
  - As λ₂ grows (cascade intensifies), dx²/dt DECREASES
    → The system moves SLOWER through cascade-space when cascade is large
    → This is correct: intergenerational trauma is "sticky" — slow to change

  - As λ₂ → 1 (isolated event), dx²/dt ≈ C₁
    → System moves at constant speed through cascade-space when isolated
    → Isolated events are "slippery" — easy to move away from
```

---

## §7. AGENT INTERFACE

### 7.1 Coordinate Query

```
Input:  Observation vector o (trauma indicators)
Output: Coordinates x = ψ(o) ∈ M_trauma

φ_query(observation) → (x¹, x², x³, x⁴, x⁵)
```

### 7.2 Metric Query

```
Input:  Point x ∈ M_trauma
Output: g_{ij}(x), λ₂(x), H(x), ∇H(x), κ_eff(x)

φ_metric(x) → {g, λ₂, H, ∇H, κ_eff}
```

### 7.3 Distance Query

```
Input:  Points p, q ∈ M_trauma
Output: d(p,q) = geodesic distance

φ_distance(p, q) → d ∈ ℝ⁺
```

### 7.4 Geodesic Query

```
Input:  Point p ∈ M_trauma, initial velocity v ∈ T_pM
Output: γ(t) for t ∈ [0,1]

φ_geodesic(p, v) → [(x(t₀), ..., x(tₙ))]  (discretized path)
```

---

## §8. IMPLEMENTATION NOTES

### 8.1 Why Only ONE Non-Trivial Dimension?

```
Design choice: only x² (causality) has non-trivial metric.

Reasoning:
  - A fully non-diagonal g_{ij} with all components variable
    would be more "accurate" but UNIMPLEMENTABLE for agents
  - The cascade axis IS the unique dimension where self-amplification
    occurs (trauma → more trauma → more trauma)
  - Trust, consent, naming, humility evolve linearly 
    (or can be approximated as linear at agent timescales)
  - Future TRL modules may add non-trivial structure to other axes
    when empirical data justifies it
```

### 8.2 Numerical Methods

```
Geodesic: 4th-order Runge-Kutta with adaptive step size
Distance: Iterative shooting method (guess velocity, adjust)
λ₂:       Direct evaluation (analytic sigmoid)
H:        Direct evaluation (analytic Gaussian)
κ_eff:    Finite difference approximation of 2nd derivative
```

### 8.3 Initial Weight Calibration

```
Weights w^k_i seeded from DERITA/ evidence base:

  TRUST weights:      informed by betrayal ratio ER1 (B ∈ [0,5])
  CAUSALITY weights:  informed by cascade principle ER2 (≥3 steps)
  POWER weights:      informed by power-consent asymmetry ER3
  NAMING weights:     informed by metabolization rate ER4 (λ in M(t))
  HUMILITY weights:   informed by Gödel constraint ER5 (Ω₀ ∈ [0.03,0.05])

Weights are RECALIBRATED via:
  - Sovereign feedback (F13 correction)
  - arif_judge verdicts (HOLD patterns indicate weight error)
  - Cooling ledger (drift between predicted and actual trajectory)
```

---

## §9. VALIDATION CRITERIA

TRL-001 is CORRECTLY FORGED when:

```
✅ M_trauma is a valid 5-dimensional Riemannian manifold
✅ Metric tensor g_{ij} is symmetric and positive-definite ∀ x ∈ M_trauma
✅ λ₂(x) ∈ [1, 5] ∀ x² ∈ [0, ∞) — matches betrayal ratio ER1 B ∈ [0,5]
✅ H(x) is smooth (C^∞) everywhere
✅ ∇H points in correct direction (increasing trust reduces harm, etc.)
✅ Geodesic equation reduces to known solution for x²
✅ Singularity detection triggers correct escalation level
✅ Agent can query coordinates, metric, distance, and geodesics
✅ F13 boundary condition allows sovereign override
```

---

## §10. NEXT MODULE

```
TRL-002: GEODESIC SOLVER
  → Numerically integrate geodesic equation
  → Compute minimum intervention path
  → Predict future state with confidence bounds
  → Detect when trajectory approaches singularities

Depends on: TRL-001 (this module — manifold and metric)
```

---

**DITEMPA BUKAN DIBERI** ⚒️
