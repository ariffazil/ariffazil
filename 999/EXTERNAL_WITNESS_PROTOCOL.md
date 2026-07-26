# External Witness Protocol — Gödel Lock

> **ARIFFAZIL /999 — No formal system can adjudicate itself.**
> **The witness must come from outside.**
> **DITEMPA BUKAN DIBERI — Forged, Not Given.**

---

## 0. The Gödel Lock

The arifOS kernel refuses to self-validate SEAL-bound claims.
This is the formal Gödel lock — enforced at `arifOS/arifosmcp/runtime/godel_lock_enforcement.py`.

**The Iron Rule:** SEAL-bound claims without external witness get `Φ_effective = Φ × 0.5`.
SEAL-bound + strong external witness (Φ_external ≥ 0.9) → full seal.
SEAL-bound + weak external witness (Φ_external < 0.5) → HOLD, even if internal reasoning is perfect.

---

## 1. Witness Roles (W³ = Human × AI × External)

| Channel | Owner | What it provides |
|---------|-------|------------------|
| **Human** | ARIF (F13 SOVEREIGN) | Final veto, Φ_human attestation via Telegram/Hermes |
| **AI** | arifOS kernel + agents | Internal reasoning, capability, judgment |
| **External** | Third-party (ChatGPT, Gemini, Claude) OR another organ not in the judgment chain | Φ_external attestation for irreversible actions |

---

## 2. When External Witness Is Required

- SEAL-grade constitutional changes
- CANON.md modifications
- PRINCIPAL_DOCTRINE.md modifications
- FLOOR_TABLE.json changes
- VAULT999 pointer updates
- Any change to the 000/ or 999/ directories

---

## 3. External Witness Agents

| Agent | Role |
|-------|------|
| **ChatGPT** | External witness via `chatgpt_external_witness` attestation |
| **Gemini** | External witness via `gemini_external_witness` attestation |
| **Claude** | External witness via `claude_external_witness` attestation |

---

## 4. Attestation Format

```
EXTERNAL_WITNESS: SEAL|HOLD|APPROVE
Witness: [agent-name]
Date: [ISO-8601]
Hash: [SHA-256 of attested content]
Summary: [what was reviewed]
Confidence: [0.0-1.0]
```

---

## 5. Anti-Calhoun Gate

Beautiful internal coherence without external witness is the Iblis trap.
The kernel refuses coherence theatre.

---

## 6. Receipt

Every external witness attestation is sealed to VAULT999 with:
- `kind: godel_witness`
- `witness_channel: [chatgpt|gemini|claude|hermes]`
- `attested_hash: sha256:...`

---

**DITEMPA BUKAN DIBERI ⚒️**
