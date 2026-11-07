"""Copy the canonical skill into the Claude Code plugin layout.

Run after editing SKILL.md or references/:  python tools/sync_plugin_skill.py

The plugin loads skills/<name>/SKILL.md, and SKILL.md loads references/*.md
relative to its own folder, so both are copied. tests/test_plugin_package.py
fails until the copy matches the root files byte for byte.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def skill_name() -> str:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    return re.search(r'^name:\s*"?([^"\n]+)"?', text, re.M).group(1).strip()


def main() -> None:
    dest = ROOT / "skills" / skill_name()
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    shutil.copyfile(ROOT / "SKILL.md", dest / "SKILL.md")
    shutil.copytree(ROOT / "references", dest / "references")
    print(f"synced SKILL.md + references/ -> {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
