# VAULT999 — Public Pointer

> **ARIFFAZIL /999 — This file points to the canonical vault. It IS NOT the vault.**
> **DITEMPA BUKAN DIBERI — Forged, Not Given.**

---

## Canonical Location

The VAULT999 operational ledger lives at:

```
VPS: /root/.local/share/arifos/vault999/seal_chain.jsonl
```

This is the **single source of truth**. All mirrors are query/backup only. Never canonical.

---

## What VAULT999 Is

| Layer | Where | Role |
|-------|-------|------|
| **Operational ledger** | VPS seal chain | Arrow of time. Canonical only. |
| **Code models** | A-FORGE `apa/core/` | Readers validate what they see |
| **Doctrine** | AAA (meaning) + arifOS (writer) | WHAT a seal is + how it is written |

| Actor | Verb |
|-------|------|
| **arifOS** | **Writes** seals |
| **A-FORGE** | **Reads** (+ holds typed models) |
| **AAA** | **Defines** seal semantics |
| **VPS root** | **Stores** the physical chain |

---

## What VAULT999 Is NOT

- ❌ A GitHub file
- ❌ A database with UPDATE permissions
- ❌ A human-readable journal
- ❌ Editable
- ❌ Rewritable
- ❌ Forgivable

---

## Verification

```
curl https://arif-fazil.com/999/verify
→ {"head":"sha256:...","verified":true,"chain_status":"verified"}
```

The hash chain is the arrow of time. Reversing the arrow means rewriting the Vault, which doctrine forbids.

---

## Public Surface

This `/999` directory on GitHub is the **public window** — summaries, pointers, protocol.
It is NOT the canonical ledger. The canonical ledger is off-GitHub, runtime-governed,
append-only, and hash-chained.

---

*DITEMPA BUKAN DIBERI ⚒️*
