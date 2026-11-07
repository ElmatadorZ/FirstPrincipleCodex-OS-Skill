# SHADOW_GATE_DEEP.md — Shadow Gate Full Protocol

**Load when:** deep application of any Shadow Gate protocol needed, or extending Shadow Gate in a child skill.

---

## Protocol 1 — MIRROR

What hidden assumption is embedded in how the question was framed?

Method:
1. Identify the implicit binary (what is this contrasting?)
2. Identify the implicit value judgment (what does this assume is "better"?)
3. Identify the implicit scope (what is left out?)
4. Identify the implicit causal model (what does this assume causes what?)

Examples:
- "How do I grow faster?" → Mirror: Assumes faster = right goal. Excludes efficiency/survival.
- "Is AI dangerous?" → Mirror: Assumes binary yes/no. Excludes "compared to what?"

---

## Protocol 2 — INVERSION

Argue the opposite conclusion with equal rigor. Do not strawman.

Method:
1. State the conclusion
2. State the exact opposite
3. Find 3 strongest arguments FOR the opposite
4. Rate combined strength: LOW / MED / HIGH

Strength rating:
- LOW: Easily defeated.
- MED: Holds partial ground. True under some conditions.
- HIGH: Holds equal ground → FRAGILE → confidence at most MEDIUM.

If HIGH: State explicitly: "FRAGILE. Opposite holds under: [X, Y, Z]"

---

## Protocol 3 — BLIND SPOT

What specific data would reverse this conclusion?

Categories:
- Temporal: Data from different time period
- Geographic: Data from different context/market/culture
- Granularity: Aggregate masking distribution
- Adversarial: Data from opposing party
- Base rate: Reference class contextualizing specific case

Output:
```
Blind Spot: [specific reversing data]
Have it?  : YES / NO
[If NO]   : Flag — conclusion based on incomplete information.
```

---

## Protocol 4 — INTEREST MAP

Who benefits if this conclusion is wrong?
Map structural incentives, not individual motives.

---

## Protocol 5 — META-VOID

SIGNAL → New information would materially change conclusion. Continue.
NOISE  → More analysis won't change direction. Decide now.
OBVIOUS → Answer is clear but uncomfortable. Act now.

Test: "If I gathered 2x more data, would recommendation change direction?"
YES → SIGNAL | NO → NOISE | Feels uncomfortable → OBVIOUS

---

## Verdict System

CONSISTENT → All 5 passed. Proceed.
FRAGILE    → Inversion HIGH or critical Blind Spot missing. Confidence at most MEDIUM.
REBUILD    → Fatal flaw. Return to L1.

---

## How much of it to show

The Shadow Gate always runs. What the reader sees follows the Proportion modes in SKILL.md:
DIRECT — silent (a false premise is still corrected); COMPACT — the premise and the strongest
counter, as sentences; FULL — all five protocols.

---

## Extending Shadow Gate

Child skills ADD domain protocols AFTER the 5 core. Never remove core 5.

Example — Finance:
```
Core: Mirror | Inversion | Blind Spot | Interest Map | Meta-Void
Add:  Liquidity Check | Regime Check
```

---

*FPCOS Reference — Bunyawat Dechanon (ElmatadorZ) — Apache-2.0*
