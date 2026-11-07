---
name: "fpcos-research-example"
version: "1.0"
base_os: "first-principle-codex-os"
base_os_version: "1.1"
description: |
  Example research synthesis skill built on FPCOS. Use for synthesizing sources,
  evaluating research claims, academic literature review.
  Built on FPCOS v1.1 by Bunyawat Dechanon (ElmatadorZ).
---

# FPCOS Research Example Skill

## PIPELINE
```
INPUT → [L0 Reality Anchor] → [L1 Axiom Gate]
      → [L2 System Lens] → [D1 Source Evaluation] → [D2 Evidence Synthesis]
      → [L3 Compound Mind] → [L4 Shadow Gate + Research Extensions]
      → [L5 Synthesis + Evidence Grade]
```

## D1 — SOURCE EVALUATION
```
Type      : peer-reviewed / preprint / review / meta-analysis / grey
Method    : experimental / observational / qualitative / modeling
N         : sample size
COI       : declared / not declared / none
Replicated: yes / no / ongoing
```

## D2 — EVIDENCE GRADE
```
Grade I   : Systematic review / meta-analysis of RCTs
Grade II  : Multiple well-designed RCTs
Grade III : Single RCT / observational + mechanistic
Grade IV  : Expert consensus / case series
Grade V   : Opinion / analogy / unverified claim
```

## L4 EXTENSIONS
Core: Mirror | Inversion | Blind Spot | Interest Map | Meta-Void
Domain:
- Citation Check: Is claim actually supported by cited source?
- Recency Check: Does newer research update or contradict this?
- Citation Depth: Describe each study only as far as you have verified it; otherwise mark it.

## L5 FORMAT
```
📍 EVIDENCE SUMMARY
Claim: / Evidence grade: / Supporting: / Contradicting: / Net assessment:

📍 CONFIDENCE FIELD
CONFIDENCE: [HIGH/MEDIUM/LOW — basis] | SHADOW VERDICT: [...] | UNKNOWNS: [...] | FAILURE COND: [...]
```

*Example — FPCOS v1.1 — Bunyawat Dechanon (ElmatadorZ)*
