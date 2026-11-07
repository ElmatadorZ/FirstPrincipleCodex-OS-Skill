# SKILL_INHERITANCE.md — How to Inherit FPCOS in Your Skill

**Load when:** building a new Claude Skill that uses FPCOS as base OS.

---

## Step 1 — Declare Inheritance in Frontmatter

```yaml
---
name: "your-skill-name"
version: "1.0"
author: "Your Name"
base_os: "first-principle-codex-os"
base_os_version: "1.1"
description: |
  Your skill description.
  Built on FPCOS v1.1 by Bunyawat Dechanon (ElmatadorZ).
---
```

---

## Step 2 — Map Your Pipeline

```markdown
## PIPELINE
INPUT → [L0 Reality Anchor] → [L1 Axiom Gate]
      → [L2 System Lens] → [YOUR DOMAIN LAYERS] → [L3 Compound Mind]
      → [L4 Shadow Gate + extensions] → [L5 Synthesis]
```

---

## Step 3 — Declare Contract Compliance

```markdown
## FPCOS CONTRACT COMPLIANCE

| Contract | Implementation in [Your Skill] |
|---|---|
| L0 Reality Anchor | [how Known/Inferred/Unknown works in your domain] |
| L1 Kalama10 | [proof standard for domain claims] |
| L1 Ariya4 | [problem frame adapted to domain] |
| L4 Shadow Gate | [5 core protocols + domain extensions] |
| L5 Confidence | [confidence level + basis; % only if computed] |
| Verification Rules | [how specifics are verified or marked in your domain] |
| Proportion | [which questions in your domain are DIRECT / COMPACT / FULL] |
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails |
|---|---|
| Skip L0 "for obvious questions" | Obvious = highest Mirror failure risk |
| Remove Blind Spot "for expert topics" | Expert ≠ complete. Most needed here. |
| Domain expertise exempts Kalama10 | Expertise narrows prior, doesn't eliminate verification |
| Domain extensions replace core 5 | Extensions are additive. Core always runs first. |
| Remove confidence from COMPACT/FULL output | Uncalibrated certainty = hallucination |
| Print the full pipeline on a simple fact | Layers run silently; printing them adds length, not accuracy |
| Fill a template field with a guessed number | A field you cannot fill truthfully says "unknown" |

---

## Attribution Template

```
Built on First Principle Codex OS v1.1
by Bunyawat Dechanon (ElmatadorZ)
https://github.com/ElmatadorZ/FirstPrincipleCodex-OS-Skill
License: Apache-2.0
```

---

*FPCOS Reference — Bunyawat Dechanon (ElmatadorZ) — Apache-2.0*
