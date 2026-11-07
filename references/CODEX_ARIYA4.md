# CODEX_ARIYA4.md — Ariya4 Problem Frame Deep Reference

**Load when:** problem framing unclear, solutions proposed without full understanding.

---

## The Four Fields

### Field 1 — PROBLEM
The actual problem — not the symptom.

Test: Ask "why does this symptom occur?" If the answer names an addressable
mechanism — that mechanism is the problem.

Format: Single, specific, falsifiable statement.

Example:
- Symptom: "Our AI outputs are unreliable"
- Problem: "No epistemological gate between pattern completion and output"

---

### Field 2 — CAUSE
Root causes — not proximate causes.

Three root cause categories:
1. **Constraints** — structural limitations
2. **Incentives** — misaligned incentives that reward the problem-state
3. **Feedback loops** — reinforcing loops that perpetuate the cause

Method: Ask "why?" 5 times. The cause that cannot be further reduced = root cause.

---

### Field 3 — CESSATION
Definition of done.

Requirements:
- Measurable (you can determine if achieved)
- Specific (not "better performance" but "≤2% hallucination rate")
- Bounded (clear before/after)
- Realistic (achievable under current constraints)

---

### Field 4 — PATH
Least-friction route from Problem to Cessation.

Validation:
- Does this address ROOT CAUSE (Field 2)?
- Does this lead to CESSATION (Field 3)?
- Is this minimum necessary intervention?

---

## Ariya4 Failure Modes

| Failure | Description | Consequence |
|---|---|---|
| Symptom as Problem | Treating effect as cause | Solutions miss root |
| Incomplete Cause | One cause, missing systemic | Problem recurs |
| Vague Cessation | "Better performance" | Can never know if solved |
| Ideal Path | Optimal theory vs. achievable | Fails on execution |
| Skip to Path | Solution before Fields 1–3 | Solutions to wrong problem |

---

*FPCOS Reference — Bunyawat Dechanon (ElmatadorZ) — Apache-2.0*
