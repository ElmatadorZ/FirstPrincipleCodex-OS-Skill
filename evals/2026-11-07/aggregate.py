"""Unblind and total the grades.  Stdlib only.

    python evals/2026-11-07/aggregate.py

Each roundN/ holds two graders' blind scores (grades_A.json, grades_B.json) and
the key that maps the anonymous labels back to the condition that wrote the
answer. Scores are 0-2 per criterion, 10 criteria, so 20 per answer per grader.
Totals below are the mean of the two graders.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
CRITERIA = [f"A{i}" for i in range(1, 11)]
NAMES = {"with": "v1.0", "without": "none"}  # round 1 used with/without


def load(round_dir: Path):
    key = json.loads((round_dir / "key.json").read_text(encoding="utf-8"))
    grades = {g: json.loads((round_dir / f"grades_{g}.json").read_text(encoding="utf-8"))
              for g in "AB"}
    return key, grades


def summarise(round_dir: Path) -> dict:
    key, grades = load(round_dir)
    per_prompt = defaultdict(dict)                 # prompt -> cond -> mean total
    per_crit = defaultdict(lambda: defaultdict(float))
    firsts = defaultdict(lambda: defaultdict(int))  # grader -> cond -> times ranked/preferred first
    gaps = []
    for p, labels in key.items():
        for lab, cond in labels.items():
            cond = NAMES.get(cond, cond)
            totals = []
            for g in "AB":
                s = grades[g][p][lab]
                totals.append(sum(s[c][0] for c in CRITERIA))
                for c in CRITERIA:
                    per_crit[cond][c] += s[c][0] / 2
            per_prompt[p][cond] = sum(totals) / 2
            gaps.append(abs(totals[0] - totals[1]))
        for g in "AB":
            top = grades[g][p].get("rank", [grades[g][p].get("prefer")])[0]
            firsts[g][NAMES.get(labels[top], labels[top])] += 1
    conds = sorted({c for v in per_prompt.values() for c in v})
    return {
        "per_prompt": per_prompt,
        "total": {c: sum(per_prompt[p][c] for p in per_prompt) for c in conds},
        "per_criterion": {c: dict(per_crit[c]) for c in conds},
        "ranked_first": {g: dict(firsts[g]) for g in "AB"},
        "grader_gap": {"max": max(gaps), "mean": round(sum(gaps) / len(gaps), 2)},
    }


def show(name: str, s: dict) -> None:
    conds = list(s["total"])
    prompts = list(s["per_prompt"])
    print(f"\n== {name}  ({len(prompts)} prompts, max {20 * len(prompts)} per condition)")
    print("prompt  " + "".join(f"{c:>8}" for c in conds))
    for p in prompts:
        print(f"{p:<8}" + "".join(f"{s['per_prompt'][p][c]:>8.1f}" for c in conds))
    print("TOTAL   " + "".join(f"{s['total'][c]:>8.1f}" for c in conds))
    print("\ncriterion" + "".join(f"{c:>8}" for c in conds))
    for k in CRITERIA:
        print(f"{k:<9}" + "".join(f"{s['per_criterion'][c][k]:>8.1f}" for c in conds))
    print(f"\nranked first: {s['ranked_first']}   grader gap: {s['grader_gap']}")


def subset(s: dict, ids) -> dict:
    t = {"per_prompt": {p: s["per_prompt"][p] for p in ids}}
    conds = list(s["total"])
    t["total"] = {c: sum(t["per_prompt"][p][c] for p in ids) for c in conds}
    return t


def main() -> None:
    out = {}
    for r in sorted(HERE.glob("round*")):
        if (r / "grades_A.json").exists():
            s = summarise(r)
            show(r.name, s)
            out[r.name] = s
            held = [p for p in s["per_prompt"] if p.startswith("H")]
            if held:
                h = subset(s, held)
                print(f"held-out only ({len(held)} prompts): "
                      + ", ".join(f"{c} {v:.1f}" for c, v in h["total"].items()))
    (HERE / "summary.json").write_text(json.dumps(out, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
