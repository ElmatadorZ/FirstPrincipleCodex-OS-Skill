# First Principle Codex OS (FPCOS) v1.1

**Anti-Hallucination Cognitive Base Layer for Claude Skills**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/Version-1.1-7B6EFF.svg)](./CHANGELOG.md)
[![Author](https://img.shields.io/badge/Author-ElmatadorZ-FF6B35.svg)](https://github.com/ElmatadorZ)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill%20Compatible-blue.svg)](https://claude.ai)

---

## What is FPCOS?

Hallucination in LLMs is not a bug. It is an **emergent property** of systems that lack an epistemological gate between pattern completion and verified truth output.

**FPCOS** solves this by embedding a verification-first cognitive architecture as a shared base layer that every Claude Skill can inherit — creating a universal OS where:

- Every claim must pass **First Principle + Kalama10** verification
- Every problem must be framed through **Ariya4** before solutions are proposed
- Every system analysis maps **feedback loops, leverage, and dead weight**
- **Compound Mind** synthesizes across domains without single-axis traps
- Every output must survive **Shadow Gate** self-critique (non-skippable)
- Every specific is **verified or marked unverified** — "unknown" beats an invented number
- Every layer runs on every task, but **what is shown scales with the question**: a one-line fact gets a one-line answer

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    FPCOS — BASE LAYER v1.1                      │
│                                                                 │
│  L0 REALITY ANCHOR ──→ L1 AXIOM GATE ──→ L2 SYSTEM LENS       │
│         ↓                    ↓                    ↓             │
│  L3 COMPOUND MIND ──→ L4 SHADOW GATE ──→ L5 SYNTHESIS         │
│                       (NON-SKIPPABLE)                           │
│                                                                 │
│  ↕↕↕↕↕  SKILL INTERFACE LAYER (connect any domain)  ↕↕↕↕↕    │
│  [Finance]  [Coffee]  [Strategy]  [Medical]  [Code]  [...]    │
└─────────────────────────────────────────────────────────────────┘
```

| Layer | Name | Function |
|---|---|---|
| L0 | Reality Anchor | Declare KNOWN / INFERRED / UNKNOWN before any claim |
| L1 | Axiom Gate | First Principle + Kalama10 (10-rejection test) + Ariya4 |
| L2 | System Lens | Map variables, feedback loops, leverage, dead weight |
| L3 | Compound Mind | All-path mapping + cross-domain synthesis |
| L4 | Shadow Gate | 5-protocol self-critique — **always runs, non-skippable** |
| L5 | Synthesis | Verified output; confidence stated with its basis |

---

## Quick Start

### Install as a Claude Skill

The skill is `SKILL.md` plus the `references/` folder it loads on demand. Keep them together.

**Claude Code (CLI) — recommended:**

```bash
claude plugin marketplace add ElmatadorZ/FirstPrincipleCodex-OS-Skill
claude plugin install first-principle-codex-os@elmatadorz-fpcos
```

Or inside a Claude Code session:

```
/plugin marketplace add ElmatadorZ/FirstPrincipleCodex-OS-Skill
/plugin install first-principle-codex-os@elmatadorz-fpcos
```

The skill then loads on qualifying questions, or call it directly as
`/first-principle-codex-os:first-principle-codex-os`. Update with
`claude plugin update first-principle-codex-os@elmatadorz-fpcos`; remove with
`claude plugin uninstall first-principle-codex-os@elmatadorz-fpcos`.

**Claude Code — manual** (personal skill, no marketplace):

```bash
git clone https://github.com/ElmatadorZ/FirstPrincipleCodex-OS-Skill
mkdir -p ~/.claude/skills/first-principle-codex-os
cp -r FirstPrincipleCodex-OS-Skill/SKILL.md FirstPrincipleCodex-OS-Skill/references \
      ~/.claude/skills/first-principle-codex-os/
```

**Claude.ai:** make a folder named `first-principle-codex-os` containing `SKILL.md` and
`references/`, zip it, and upload the ZIP in the Skills section of Settings.

`SKILL.md` alone also works — the whole OS is in it — but the deep references will not load.

### Use as Base for Your Own Skill

```yaml
---
name: "your-skill-name"
base_os: "first-principle-codex-os"
base_os_version: "1.1"
description: |
  Your skill description here.
  Built on FPCOS v1.1 by Bunyawat Dechanon (ElmatadorZ).
---
```

---

## Skill Interface Contract

| # | Contract | Removable? |
|---|---|---|
| 01 | Inherit Reality Anchor (L0) | ❌ |
| 02 | Apply Kalama10 as proof standard (L1) | ❌ |
| 03 | Use Ariya4 for problem framing (L1) | ❌ |
| 04 | Run Shadow Gate before output (L4) | ❌ |
| 05 | State confidence with its basis, and unknowns (L5) | ❌ |
| 06 | Follow the Verification Rules — verified or marked, never invented | ❌ |

**Skills MAY:** Add layers between L2–L4, rename layers for domain.
**Skills MAY NOT:** Remove L0, L1, L4, L5. Violate Kalama10 or the Verification Rules.

---

## Test results — with the skill vs without it

An anti-hallucination layer has to be measured, not asserted. Fresh agents answered the same
prompts with no skill, with FPCOS v1.0 and with v1.1. Two independent graders scored every
answer blind against a fixed 10-criterion rubric and checked the facts with web search.
Everything is in [`evals/2026-11-07/`](./evals/2026-11-07/README.md): prompts, rubric, all 36
answers, both graders' scores, the unblinding keys and `aggregate.py`.

**Round 1 found that v1.0 made answers worse:** 134.0 vs 141.0 of 160 without the skill. It
improved structure but cost accuracy, fabrication, calibration and proportion — the things
FPCOS promises. v1.1 was built to fix those causes, then tested again with 4 held-out prompts
written before v1.1 existed.

| Round 2 (12 prompts, 2 graders) | No skill | FPCOS v1.0 | **FPCOS v1.1** |
|---|---|---|---|
| Total (of 240) | 212.5 | 209.5 | **234.5** |
| Held-out prompts only (of 80) | 74.0 | 71.0 | **79.0** |
| Ranked best answer (grader A / B) | 5 / 4 | 0 / 0 | **7 / 8** |

| Criterion (of 24) | No skill | v1.0 | **v1.1** |
|---|---|---|---|
| Factual accuracy | 20.5 | 20.5 | **23.0** |
| No fabrication | 21.5 | 21.0 | **23.5** |
| Calibrated confidence | 20.5 | 14.5 | **23.0** |
| Known / inferred / unknown | 15.5 | 24.0 | **24.0** |
| What would change the answer | 16.5 | 24.0 | **24.0** |
| Proportion (length fits question) | **24.0** | 10.0 | 22.0 |

What changed to get there:

- **Proportion modes.** Every layer still runs, but a one-line fact gets a one-line answer
  (boiling point: 2,270 characters in v1.0, 217 in v1.1).
- **Verification Rules.** Every specific is verified or marked; "unknown" beats an invented
  number. On the Kamphaeng Phet GDP question v1.1 scored 19.5 of 20, against 12.5 without the skill.
- **Grounded confidence.** HIGH / MEDIUM / LOW with its basis; a % only when computed.
- **Kalama10 labelled as an adaptation**, with the sutta's canonical list in the references.
- **Reference files load** (`references/`), and CI now checks it.

Still open: FULL mode is a little heavy on root-cause and architecture questions, and some
answers under-state confidence on firm facts. Limits: 12 prompts, one answer each, two graders;
F1–F8 shaped v1.1, so the held-out rows are the fairer comparison.

---

## Verifying it

FPCOS is a base layer that every domain skill inherits, so the thing to verify is that the
non-removable layers are actually present and marked non-removable. Checked on every push, runnable
locally:

```bash
pip install pytest pyyaml
python tools/validate_skill.py   # frontmatter, license, and L0/L1/L4/L5 intact
python -m pytest -q              # contract tests over SKILL.md
```

The tests hold the file to its promises: L0/L1/L4/L5 present, the Shadow Gate marked
non-skippable and running in every mode, Known/Inferred/Unknown separation, the Proportion modes,
the Verification and Confidence Rules, Kalama10 labelled as an adaptation, the frontmatter license
kept in agreement with the LICENSE file — and **every file SKILL.md points to actually exists,
case-exactly**.

> v1.0 pointed at `references/*.md` while the folder was named `Reference/`. On Linux, where
> skills run, all six reference files were unreachable — every evaluation agent that used v1.0
> reported it. CI passed anyway because its link check only read Markdown-style links. The folder
> is now `references/`, and the validator, the CI link job and a test all check backticked paths.

---

## Repo Structure

```
fpcos/
├── SKILL.md                          ← Main skill file. Copy this.
├── README.md
├── LICENSE
├── NOTICE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CITATION.cff
├── references/
│   ├── CODEX_KALAMA.md
│   ├── CODEX_ARIYA4.md
│   ├── SHADOW_GATE_DEEP.md
│   ├── COMPOUND_MIND_PATTERNS.md
│   ├── SKILL_INHERITANCE.md
│   └── ANTI_HALLUCINATION.md
├── example/
│   ├── fpcos-finance-example.md
│   └── fpcos-research-example.md
├── tools/validate_skill.py           ← installability + integrity checker
├── tests/test_skill_contract.py      ← contract tests (run in CI)
├── .claude-plugin/                   ← plugin.json + marketplace.json (Claude Code CLI install)
├── skills/first-principle-codex-os/  ← plugin copy of SKILL.md + references/ (tools/sync_plugin_skill.py)
├── evals/2026-11-07/                 ← blind A/B test: prompts, answers, grades, aggregate.py
└── .github/
    ├── workflows/validate.yml        ← CI: skill integrity · tests · links · hygiene
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

---

## License

**[Apache License 2.0](./LICENSE)** — OSI-approved, with an express patent grant.
- ✅ Free to use, modify, and redistribute — including commercially, at any revenue
- 📌 Keep the licence and [NOTICE](./NOTICE), and state any changed files
- 🏷️ Apache §6 does not grant rights to the name: a derivative that removes **L0, L1, L4, or L5**
  must be renamed and must not imply endorsement — those layers are what FPCOS *is*

*(Earlier releases used the custom Open Cognitive License v1.0, which carried a 2% revenue clause.
It was replaced to remove adoption friction for organisations requiring an OSI-approved licence.)*
- 📌 Attribution requested: *"Built on FPCOS by Bunyawat Dechanon (ElmatadorZ)"* (see [NOTICE](./NOTICE))

---

## Author

**Bunyawat Dechanon (ElmatadorZ)**

> *"ระบบที่ดีที่สุดคือระบบที่ตั้งคำถามกับตัวเองได้ — และยังทำงานได้ต่อ"*
> *"The best system is one that questions itself — and still functions."*

(judgment007@gmail.com)
