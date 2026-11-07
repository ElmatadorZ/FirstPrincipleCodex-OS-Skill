# Changelog

All notable changes to First Principle Codex OS will be documented here.

---

## [1.1] — 2026-11-07 — Measured, then fixed

A blind A/B test of v1.0 (`evals/2026-11-07/`) found that answers written with the
skill scored **lower** than answers written without it (134.0 vs 141.0 of 160). The
skill improved structure but hurt what it promises most: accuracy, no fabrication and
calibrated confidence. v1.1 fixes the causes. L0, L1, L4 and L5 are unchanged in
substance and stay non-removable.

### Fixed
- **Reference files were unreachable.** SKILL.md pointed at `references/*.md` but the
  folder was `Reference/`. On Linux, where skills run, every reference failed to load.
  The folder is now `references/`.
- **CI could not see it.** The link check only read Markdown-style links. The validator,
  the CI link job and the tests now check backticked paths too, case-exactly.
- A compiled `__pycache__` folder under tests was committed; it is removed and ignored.

### Changed
- **Proportion modes** (DIRECT / COMPACT / FULL): every layer still runs on every task,
  but how much is shown scales with the question. A one-line fact gets a one-line answer.
- **Epistemic Core:** the five moves every COMPACT and FULL answer carries (premise,
  known/inferred/unknown, strongest counter, confidence with basis, what would change it).
- **Verification Rules:** every specific is verified or marked unverified; "unknown"
  beats an invented number; quotes exact or labelled; studies described only as deep as
  verified.
- **Confidence Rules:** HIGH / MEDIUM / LOW with its basis. A percentage only when it is
  computed from a stated base rate, model or data. FRAGILE caps confidence at MEDIUM
  (was ≤70%).
- **Kalama10** is labelled as FPCOS's adaptation of the Kalama Sutta (AN 3.65).
  `references/CODEX_KALAMA.md` adds the sutta's canonical ten grounds, in order.
- Skill Interface Contract 05 now asks for confidence **with its basis**; new contract 06
  makes the Verification Rules non-removable for inheriting skills.
- The description no longer says "ALWAYS trigger — do NOT skip", which collided with every
  other skill; when Genesis Protocol (the router skill) is installed, it decides when
  FPCOS runs.

### Added
- `evals/2026-11-07/`: prompts, rubric, every answer, both graders' scores and the
  unblinding keys, for v1.0 vs v1.1 vs no skill, plus 4 held-out prompts.
- Validator checks and contract tests for all of the above (18 tests, 27 validator checks).

---

## [1.0] — 2024 — Initial Release

### Added
- L0 Reality Anchor — Known/Inferred/Unknown classification protocol
- L1 Axiom Gate — First Principle Decomposition + Kalama10 + Ariya4
- L2 System Thinking Lens — Living system mapping with feedback loops
- L3 Compound Mind Engine — All-path synthesis + cross-domain reasoning
- L4 Shadow Gate — 5-protocol self-critique (Mirror, Inversion, Blind Spot, Interest Map, Meta-Void)
- L5 Synthesis — Mandatory confidence field with CONSISTENT/FRAGILE/REBUILD verdict
- Skill Interface Contract — 5 non-removable inheritance requirements
- Cross-domain synthesis architecture
- Anti-hallucination map (11 sources → 11 mechanisms)
- Apache-2.0
- Full reference library (6 reference files)
- Example skills for Finance, Research domains

### Design Principles
- Token pressure priority: L4 > L1 > L5 > L3 > L2 > L0
- Compound Genius Principle formalized
- Proof = Understanding axiom
- Absolutism detector integrated into L4

---

## Versioning Policy

- **Major (x.0)**: Breaking changes to layer contracts or Skill Interface Contract
- **Minor (1.x)**: New layers, protocols, references (backward compatible)
- **Patch (1.0.x)**: Documentation, clarity, typo fixes

Child skills pin to minor: `base_os_version: "1.0"`

---

## Planned (v1.1)

- [ ] Domain adapter templates (Finance, Medical, Legal, Engineering)
- [ ] FPCOS validation tool (checks child skill contract compliance)
- [ ] Token budget optimization guide
- [ ] Multi-agent council integration pattern
- [ ] Performance benchmarks vs. unguided reasoning
