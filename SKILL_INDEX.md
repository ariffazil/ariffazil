# arifOS Skills Index

**Generated:** 2026-06-06 (regenerated from current state — was 2 months stale at 2026-04-18)
**Motto:** *DITEMPA BUKAN DIBERI* — Forged, Not Given
**Regeneration method:** Inventory of `/root/.opencode/skills/`, `/root/.hermes/skills/`, `/root/AAA/skills/`, `/root/arif-sites/.opencode/skills/`. (Audit-discovered via repo-contrast-2026-06-06 eureka.)

---

## Active Skills

### Core arifOS Skills (`/root/.opencode/skills/`)

The OpenCode user-skill library. 32 skills total.

| Skill | Purpose | Status |
|-------|---------|--------|
| `arifOS-federation` | Federation architecture + 7-organ contract | ✅ Active |
| `arifos-operator` | Operate arifOS MCP kernel (governed actions) | ✅ Active |
| `constitutional-advisor` | Floor enforcement guidance (F1-F13) | ✅ Active |
| `constitutional-reasoning` | Pre-action constitutional check framework | ✅ Active |
| `arifos-governance` | Floor enforcement recipes | ✅ Active |
| `arifos-mcp-federation` | Cross-MCP federation routing | ✅ Active |
| `arifos-recall` | Federation memory recall (L1-L6) | ✅ Active |
| `arifos-observability` | Federation telemetry + audit log | ✅ Active |
| `arifos-plan-dag` | Multi-step execution plans | ✅ Active |
| `arifos-recursive-audit` | Self-audit of skill portfolio | ✅ Active |
| `arifos-evals` | Benchmark + measurement framework | ✅ Active |
| `arif-federation-ops` | Federation restart / verify / rollback | ✅ Active |
| `aaa-workspace` | AAA workspace operations | ✅ Active |
| `mcp-unified` | Unified MCP workflow (FastMCP/arifOS/Kimi/OpenCode) | ✅ Active |
| `mcp-builder` | Build MCP servers (Python/Node) | ✅ Active |
| `fastmcp-deploy` | Deploy FastMCP servers to VPS | ✅ Active |
| `gitingest-recipe` | L1 gitingest wrapper for repo analysis | ✅ Active |
| `repo-eureka` | Governed repo intelligence orchestrator (L1-L5) | ✅ Active |
| `claude-code-ops` | Maintain Claude Code on this VPS | ✅ Active |
| `caddy-cloudflare` | Caddy v2 + Cloudflare Tunnel config | ✅ Active |
| `docker-security` | Docker hardening + F1 AMANAH | ✅ Active |
| `docker-thermodynamics` | Container lifecycle reasoning | ✅ Active |
| `database-tuning` | Postgres + Redis tuning | ✅ Active |
| `backup-dr` | Backup + disaster recovery | ✅ Active |
| `github-issues` | Monitor + triage GitHub issues | ✅ Active |
| `hermes-ops` | Hermes ASI agent operations | ✅ Active |
| `fff-sweep` | End-of-session Forge/Fix/Forget sweep | ✅ Active |
| `vault999-ops` | VAULT999 ledger operations | ✅ Active |
| `vault-integrity` | Merkle chain reasoning | ✅ Active |
| `secret-hygiene` | Secret rotation + least privilege | ✅ Active |
| `secret-rotation-guide` | Map of all secrets + rotation paths | ✅ Active |
| `vps-management` / `vps-audit` / `vps-docker` | VPS operations | ✅ Active |

### Hermes Skills (`/root/.hermes/skills/`)

68 skills (agentic templates, governance, devops, language integrations). See [AAA wiki: hermes-arifos-integration-spec](https://github.com/ariffazil/AAA/wiki) for the full list. Highlights:

- `arifos/`, `arifOS/`, `arif-rootkey/` — arifOS-specific
- `agentic/`, `agentic-foundations/`, `aaa-agentic-governance/` — agent framework
- `devops/arif-federation-ops/`, `devops/dynamic-state-truth/`, `devops/mcp-semantic-affordance-discipline/` — federation devops
- `mcp-server-forge/`, `python-tool-isolation/`, `gitingest-recipe/`, `repo-eureka/`, `mcp-unified/` — MCP forge stack
- `agent-email-a2a-protocol/`, `a2a-agentic-template/` — A2A integrations
- `breaking-news-policy/`, `creative/`, `data-science/`, `domain/`, `briefing-system/` — content/data

### AAA Skills (`/root/AAA/skills/`)

28 federation-level skills. See [AAA/skills/](https://github.com/ariffazil/AAA/tree/main/skills) for the full list. Highlights:

- `arifos-governance`, `arifos-mcp-federation`, `arifos-observability`, `arifos-plan-dag`, `arifos-recall`, `arifos-recursive-audit`, `arifos-evals`
- `aaa-agentic-governance`, `agent-onboarding`
- `constitutional-`, `cross-domain-`, `repo-eureka` style

### Site Skills (`/root/arif-sites/.opencode/skills/`)

32 site-level skills. Mostly for site rendering + Cloudflare Pages deployment.

---

## MCP Servers (live, verified 2026-06-05)

| Server | URL | Tools | Status |
|--------|-----|------:|--------|
| **arifOS** | `https://arifos.arif-fazil.com/mcp` | 13 | ✅ LIVE · 200 · Server Card + Origin gate + outputSchema + Tasks |
| **WEALTH** | `https://wealth.arif-fazil.com/mcp` | 19 | ✅ LIVE · 200 · Server Card + Origin gate + outputSchema + Tasks |
| **WELL** | `https://well.arif-fazil.com/mcp` | 14 | ✅ LIVE · 200 · Server Card + Origin gate + outputSchema + Tasks |
| **GEOX** | `https://geox.arif-fazil.com/mcp` | 31 | ✅ LIVE · 200 · Server Card + Origin gate + outputSchema + Tasks |
| **minimax-media** | `http://localhost:18090/sse` | 9 | ✅ LIVE (SSE) |
| **minimax-code** | `http://localhost:18091/sse` | 2 | ✅ LIVE (SSE) |
| **github-official** | per-agent launcher | 5 toolsets | ✅ READ-ONLY |
| **repomapper** | per-agent launcher | map JSON | ✅ OUTPUT-ONLY |
| **serena** | per-agent launcher | symbol L3 | ✅ `--mode no-memories` |

Total federation tool surface: **94 canonical MCP tools** + 4 MCP server cards + 7 agent-card outputs.

---

## llms.txt Coverage (NEW — closed 2026-06-06)

All 7 federation repos now have `llms.txt` drafts in `/root/audit/repo-contrast-2026-06-06/*-llms.txt` (MCP-spec compliance gap closed). Awaiting `git mv` to repo roots.

---

## Federated Agent Roster (live as of 2026-06-05)

8 coding agents: **Claude Code, Codex, Copilot, Kimi Code, OpenCode, Continue CLI, Aider, Gemini**. Plus 3 ops agents: **Hermes ASI (Telegram)**, **OpenClaw Gateway**, **APEX Prime (888 JUDGE)**. Plus **cn-organ** (Continue CLI organ gateway).

---

## Archived Skills (DO NOT USE)

| Path | Reason |
|------|--------|
| `/root/.opencode/skills/_archive/merged-2026-06-03/` | Replicate/MCP models merged into `replicate-*` skills |
| `arifOS/archive/*/skills/` | Old workspace snapshots |
| `WEALTH/docs/legacy/` (now empty post LAW-SEAL) | Legacy docs archived in `_archive/docs_legacy_pre_forge_2026-06-06/` |
| `arif-sites/.opencode/skills/_archive/` (if any) | Deprecated site skills |

---

## Deprecated Domains

| Domain | Status | Notes |
|--------|--------|-------|
| `arifOS.arif-fazil.com` | ❌ Deprecated | Use `arifos.arif-fazil.com` (canonical: `arifos`, lowercase) |

---

## Change Log

- **2026-06-06**: Regenerated (was 2 months stale). New skills added: `arifOS-federation`, `arifos-operator`, `mcp-unified`, `gitingest-recipe`, `repo-eureka`, `claude-code-ops`, `caddy-cloudflare`, `docker-security`, `docker-thermodynamics`, `database-tuning`, `backup-dr`, `github-issues`, `hermes-ops`, `fff-sweep`, `vault999-ops`, `vault-integrity`, `secret-hygiene`, `secret-rotation-guide`, `vps-management`, `vps-audit`, `vps-docker`, `mcp-builder`, `fastmcp-deploy`. MCP server table updated to 9 live servers (added minimax-media + minimax-code, 2026-06-05). `llms.txt coverage` section added. Fed roster updated to 8 coding agents + 3 ops + 1 gateway. Trigger: repo-contrast audit eureka.
- **2026-04-18**: Original 24-skill index generated. Stale by 2026-06-06.

---

*999 SEAL — Skills indexed 2026-06-06*
