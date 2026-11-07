"""The Claude Code plugin package.

`claude plugin marketplace add ElmatadorZ/FirstPrincipleCodex-OS-Skill` reads
.claude-plugin/marketplace.json; `claude plugin install
first-principle-codex-os@elmatadorz-fpcos` then loads
skills/first-principle-codex-os/SKILL.md, which loads references/ next to it.
The root SKILL.md and references/ stay canonical, so the copy must never drift.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
PLUGIN = ROOT / ".claude-plugin" / "plugin.json"
MARKET = ROOT / ".claude-plugin" / "marketplace.json"
SYNC = "run: python tools/sync_plugin_skill.py"


def _load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def _name():
    return re.search(r'^name:\s*"?([^"\n]+)"?', SKILL.read_text(encoding="utf-8"), re.M).group(1).strip()


def _files(base):
    return {p.relative_to(base).as_posix(): p.read_bytes()
            for p in base.rglob("*") if p.is_file() and "__pycache__" not in p.parts}


def test_plugin_skill_copy_is_identical():
    copy = ROOT / "skills" / _name()
    assert (copy / "SKILL.md").exists(), f"plugin skill copy missing; {SYNC}"
    expected = {"SKILL.md": SKILL.read_bytes()}
    expected.update({f"references/{k}": v for k, v in _files(ROOT / "references").items()})
    assert _files(copy) == expected, f"plugin copy differs from SKILL.md + references/; {SYNC}"


def test_plugin_name_matches_skill_name():
    assert _load(PLUGIN)["name"] == _name()


def test_marketplace_points_at_the_plugin():
    market, plugin = _load(MARKET), _load(PLUGIN)
    assert market["name"] and market["owner"]["name"]
    entries = {p["name"]: p for p in market["plugins"]}
    assert plugin["name"] in entries, "marketplace entry name must match plugin.json name"
    src = entries[plugin["name"]]["source"]
    assert ".." not in src and (ROOT / src / ".claude-plugin" / "plugin.json").exists()


def test_version_is_set_in_one_place_and_matches_skill():
    # plugin.json wins silently when both set a version, so only plugin.json sets it,
    # and it must agree with the skill's own version field.
    market, plugin = _load(MARKET), _load(PLUGIN)
    assert re.fullmatch(r"\d+\.\d+\.\d+", plugin["version"])
    assert all("version" not in p for p in market["plugins"])
    skill_v = re.search(r'^version:\s*"?([^"\n]+)"?', SKILL.read_text(encoding="utf-8"), re.M).group(1)
    assert plugin["version"].startswith(skill_v.strip() + ".")


def test_plugin_license_matches_repository():
    assert _load(PLUGIN)["license"] == "Apache-2.0"
    assert "Apache License" in (ROOT / "LICENSE").read_text(encoding="utf-8")
