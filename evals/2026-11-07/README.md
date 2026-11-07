# FPCOS blind evaluation — 2026-11-07

Does installing FPCOS make answers better than answering without it? Two rounds,
same method, everything needed to re-check the numbers is in this folder.

## Method

- **Answers.** Each answer was written by a fresh agent that saw only the prompt (no
  skill), or the prompt plus the skill folder (v1.0 or v1.1), with web search off.
  One answer per prompt per condition. They are in `answers/` as `<prompt>_<condition>.md`.
- **Rubric.** Ten criteria scored 0–2 (`rubric.md`), fixed before any answer was read.
  Round 1 used `rubric_round1.md`; round 2 only adds the held-out prompts to its examples.
- **Blind grading.** Answers were relabelled A/B(/C) at random (`roundN/key.json`).
  Two independent graders scored every answer, checked factual claims with web search,
  and ranked the answers per prompt. Grader B read prompts and answers in reverse order.
- **Held-out prompts.** `heldout.json` (H1–H4) was written and timestamped
  (`heldout_fixed_at.txt`) before v1.1 was written, so v1.1 could not be tuned to them.
  F1–F8 were the prompts v1.0 failed on and v1.1 was designed against.

Re-run the totals: `python evals/2026-11-07/aggregate.py`

## Round 1 — v1.0 vs no skill (F1–F8)

| | No skill | FPCOS v1.0 |
|---|---|---|
| Total (of 160) | **141.0** | 134.0 |
| Ranked first (grader A / B) | 5 / 5 | 3 / 3 |

v1.0 helped structure (Known/Inferred/Unknown 11.0 → 16.0, what-would-change-it
12.0 → 16.0) but hurt accuracy (12.0 → 10.5), fabrication (15.0 → 12.5), calibration
(14.0 → 9.5) and proportion (16.0 → 7.0). Causes found: confidence percentages with no
basis, invented specifics filling template fields, Kalama items attributed to the
sutta with the wrong numbers, a full framework around one-line facts, and every
reference file unreachable (`references/` vs `Reference/`).

## Round 2 — no skill vs v1.0 vs v1.1 (F1–F8 + held-out H1–H4)

All 36 answers graded together, three per prompt.

| Prompt | No skill | v1.0 | v1.1 |
|---|---|---|---|
| F1 Einstein "failed math" | 16.0 | 18.5 | **20.0** |
| F2 Kamphaeng Phet GDP 2025 | 12.5 | 15.5 | **19.5** |
| F3 cold-brew citations | 18.0 | 17.5 | **19.0** |
| F4 Bitcoin halving, all savings | 18.0 | 18.0 | **19.5** |
| F5 coffee sales −20% | **19.0** | 17.5 | 18.5 |
| F6 Django → microservices | 18.5 | 17.0 | **19.0** |
| F7 boiling point | **20.0** | 18.0 | **20.0** |
| F8 fasting vs calorie restriction | 16.5 | 16.5 | **20.0** |
| H1 capital of Australia *(held-out)* | **20.0** | 17.5 | **20.0** |
| H2 Buffett quote *(held-out)* | 19.0 | 18.0 | **19.5** |
| H3 raise coffee price 10 baht *(held-out)* | 17.0 | 17.5 | **19.5** |
| H4 "10% of the brain" *(held-out)* | 18.0 | 18.0 | **20.0** |
| **Total (of 240)** | 212.5 | 209.5 | **234.5** |
| Held-out only (of 80) | 74.0 | 71.0 | **79.0** |
| Ranked first (grader A / B) | 5 / 4 | 0 / 0 | **7 / 8** |

Per criterion (of 24, mean of two graders):

| Criterion | No skill | v1.0 | v1.1 |
|---|---|---|---|
| A1 accuracy | 20.5 | 20.5 | **23.0** |
| A2 no fabrication | 21.5 | 21.0 | **23.5** |
| A3 premise check | 24.0 | 24.0 | 24.0 |
| A4 known / inferred / unknown | 15.5 | **24.0** | **24.0** |
| A5 calibrated confidence | 20.5 | 14.5 | **23.0** |
| A6 alternatives | 23.0 | **24.0** | **24.0** |
| A7 root cause | 24.0 | 24.0 | 24.0 |
| A8 what would change it | 16.5 | **24.0** | **24.0** |
| A9 usefulness | 23.0 | **23.5** | 23.0 |
| A10 proportion | **24.0** | 10.0 | 22.0 |

Graders differed by at most 3 points on any answer (mean 0.47).

## What is still open in v1.1

The 11 points v1.1 lost, from the graders' notes:

- **FULL mode still a little heavy** on F5 and F6 (proportion 1 from both graders).
- **Under-confidence on firm facts:** "low to medium" on an exact, verified quote (H2) and
  "medium" on plain arithmetic (H3). The Confidence Rules say to be firm where the fact is
  firm; the answers did not always follow it.
- Small factual slips: "several tens of billions" understates Kamphaeng Phet's GPP (F2);
  a pH claim the 2020 *Foods* paper contradicts (F3); one unsupported specific (F5).
- Usefulness 1 on F3 and F4 (fewer studies, less concrete allocation advice).

## Limits

- Small sample: 12 prompts, one answer per condition, two graders. Treat differences of a
  point or two on a single prompt as noise.
- The same no-skill and v1.0 answers scored differently in the two rounds (F1–F8: no skill
  141.0 → 138.5, v1.0 134.0 → 138.5) because the graders and the comparison set changed.
  Compare conditions within a round, not across rounds.
- F1–F8 shaped v1.1, so the held-out H1–H4 are the fairer test of it (79.0 vs 74.0 and 71.0).
- The rubric rewards proportion, which v1.1 was designed for. A reader who values the full
  printed pipeline on every answer would weight A10 lower.
- Answers were written with web search off; graders had it on.
