#!/usr/bin/env python3
"""
validate_skill.py — integrity checks for FPCOS.

READ-ONLY. This script never modifies SKILL.md; it only verifies that the file
still satisfies the contract that makes it installable and makes it FPCOS.

Two classes of check:

  INSTALLABILITY  — the frontmatter is well-formed YAML with the fields a skill
                    loader needs. If these fail, the skill will not install.

  INTEGRITY       — the non-removable layers (L0, L1, L4, L5) and the pipeline
                    are present. If these fail, the artifact may still install,
                    but it is no longer FPCOS (see NOTICE).

Run:  python tools/validate_skill.py
Exit: 0 all checks pass · 1 one or more failed
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
    OK, BAD = "PASS", "FAIL"
except Exception:  # pragma: no cover
    OK, BAD = "PASS", "FAIL"

try:
    import yaml
except ImportError:
    print("Missing dependency: pyyaml. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"

# The layers FPCOS declares non-removable. See NOTICE.
NON_REMOVABLE = ["L0", "L1", "L4", "L5"]
ALL_LAYERS = ["L0", "L1", "L2", "L3", "L4", "L5"]
REQUIRED_FRONTMATTER = ["name", "description", "license"]

results: list[tuple[str, bool, str]] = []

# Backticked repository paths, e.g. `references/CODEX_KALAMA.md`.
PATH_RE = re.compile(r"`((?:references|example|tools|tests)/[^`\s]+)`")


def referenced_paths(text: str) -> list[str]:
    return sorted(set(PATH_RE.findall(text)))


def exists_case_exact(rel: str) -> bool:
    """Path.exists() is case-insensitive on macOS and Windows, but skill loaders
    run on Linux, where `references/` and `Reference/` are different folders."""
    here = ROOT
    for part in Path(rel).parts:
        if not here.is_dir() or part not in {p.name for p in here.iterdir()}:
            return False
        here = here / part
    return True


def check(name: str, cond: bool, detail: str = "") -> None:
    results.append((name, bool(cond), detail))
    print(f"  {OK if cond else BAD}  {name}" + (f"  — {detail}" if detail and not cond else ""))


def main() -> int:
    if not SKILL.exists():
        print(f"FATAL: {SKILL.name} not found at {SKILL}")
        return 1

    text = SKILL.read_text(encoding="utf-8")

    print("\nINSTALLABILITY")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    check("frontmatter block present and delimited", m is not None)
    if not m:
        return 1

    try:
        fm = yaml.safe_load(m.group(1))
        parsed = isinstance(fm, dict)
    except yaml.YAMLError as e:
        fm, parsed = None, False
        check("frontmatter is valid YAML", False, str(e)[:80])
    if parsed:
        check("frontmatter is valid YAML", True)
        for field in REQUIRED_FRONTMATTER:
            check(f"frontmatter has '{field}'", field in fm)
        name = str(fm.get("name", ""))
        check("name is slug-safe (a-z0-9-)", bool(re.fullmatch(r"[a-z0-9][a-z0-9-]*", name)),
              f"got {name!r}")
        desc = str(fm.get("description", ""))
        check("description is non-empty", len(desc.strip()) > 0)
        check("license is declared", bool(str(fm.get("license", "")).strip()))
        check("description does not demand ALWAYS-trigger",
              not re.search(r"\bALWAYS trigger\b|do NOT skip", desc),
              "an always-trigger description collides with every other skill")

    print("\nINTEGRITY (what makes it FPCOS)")
    body = text[m.end():]
    for layer in ALL_LAYERS:
        present = re.search(rf"^#+.*\b{layer}\b", body, re.M) is not None
        must = layer in NON_REMOVABLE
        check(f"layer {layer} section present" + ("  [non-removable]" if must else ""), present)
    check("pipeline block declared", "PIPELINE" in body)
    check("Shadow Gate marked non-skippable",
          re.search(r"NON-?SKIPPABLE", body, re.I) is not None)
    for section in ("PROPORTION", "EPISTEMIC CORE", "VERIFICATION RULES", "CONFIDENCE RULES"):
        check(f"{section} section present", re.search(rf"^#+ {section}\b", body, re.M) is not None)

    print("\nREPOSITORY CONSISTENCY")
    check("LICENSE exists", (ROOT / "LICENSE").exists())
    check("NOTICE exists", (ROOT / "NOTICE").exists())
    lic = str(fm.get("license", "")) if parsed else ""
    lic_text = (ROOT / "LICENSE").read_text(encoding="utf-8") if (ROOT / "LICENSE").exists() else ""
    check("declared license matches LICENSE file",
          ("Apache" in lic and "Apache License" in lic_text) or (lic and lic in lic_text),
          f"frontmatter says {lic!r}")
    ref = ROOT / "references"
    check("references/ directory present", ref.is_dir() and any(ref.glob("*.md")))
    missing = [p for p in referenced_paths(body) if not exists_case_exact(p)]
    check("every file SKILL.md points to exists (case-exact)", not missing,
          ", ".join(missing))
    ex = ROOT / "example"
    check("example/ directory present", ex.is_dir() and any(ex.iterdir()))

    passed = sum(1 for _, ok, _ in results if ok)
    total = len(results)
    print(f"\n{'=' * 52}\nFPCOS VALIDATION: {passed}/{total} passed")
    if passed != total:
        print("FAILED:")
        for n, ok, d in results:
            if not ok:
                print(f"  - {n}" + (f" ({d})" if d else ""))
        return 1
    print("SKILL.md is installable and structurally intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
