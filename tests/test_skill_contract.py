"""The FPCOS contract.

FPCOS is a single-file base layer that every domain skill inherits, so the
promise that matters is that the non-removable layers are actually present and
marked non-removable. These tests hold SKILL.md to that — they are the pytest
companion to tools/validate_skill.py, so a contributor sees the contract without
reading the validator.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"


def _split():
    text = SKILL.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "frontmatter must be present and delimited"
    return yaml.safe_load(m.group(1)), text[m.end():]


def test_canonical_filename_lowercase_extension():
    # Claude's skill loader is case-sensitive and expects exactly SKILL.md.
    # The file was SKILL.MD, which a case-sensitive loader would not find.
    assert SKILL.exists()
    assert SKILL.name == "SKILL.md"


def test_frontmatter_and_license():
    fm, _ = _split()
    for f in ("name", "description", "license", "version"):
        assert f in fm
    assert str(fm["license"]).lower().replace(" ", "-") == "apache-2.0"


def test_license_matches_license_file():
    fm, _ = _split()
    lic = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert "Apache License" in lic
    assert str(fm["license"]).lower().replace(" ", "-") == "apache-2.0"


def test_metadata_declares_base_layer_role():
    fm, _ = _split()
    meta = fm.get("metadata", {})
    assert meta.get("compatibility")
    assert meta.get("not_for")
    # FPCOS's whole identity is that it is a base layer, not an optional add-on.
    assert "base" in str(meta.get("role", "")).lower()


def test_non_removable_layers_present():
    _, body = _split()
    # L0 (Reality Anchor), L1 (Axiom Gate), L4 (Shadow Gate), L5 (Synthesis) are
    # the layers the OS declares can never be removed by an inheriting skill.
    for layer in ("L0", "L1", "L4", "L5"):
        assert layer in body, f"non-removable layer {layer} must be present"


def test_shadow_gate_is_non_skippable():
    _, body = _split()
    assert re.search(r"shadow gate", body, re.I)
    assert re.search(r"non.?skippable|always runs|❌ No", body, re.I)


def test_known_inferred_unknown_separation():
    _, body = _split()
    for word in ("Known", "Inferred", "Unknown"):
        assert word in body


def test_output_states_confidence_and_unknowns():
    _, body = _split()
    assert re.search(r"confidence", body, re.I)
    assert re.search(r"unknown", body, re.I)


def test_inheritance_contract_marks_layers_non_removable():
    _, body = _split()
    # The SKILL INTERFACE CONTRACT table marks the inherited rules "❌ No"
    # (may not be removed). At least the core ones must be there.
    assert "SKILL INTERFACE CONTRACT" in body
    assert body.count("❌ No") >= 4


# ---------------------------------------------------------------- v1.1
# A blind A/B test of v1.0 (evals/2026-11-07/) found the skill made answers
# worse on exactly what it promises: invented specifics to fill template fields,
# confidence percentages with no basis, misattributed Kalama numbering, and a
# full framework around one-line facts. These tests pin the fixes.

def _referenced_paths(text):
    return sorted(set(re.findall(r"`((?:references|example|tools|tests)/[^`\s]+)`", text)))


def _exists_case_exact(rel):
    here = ROOT
    for part in Path(rel).parts:
        if not here.is_dir() or part not in {p.name for p in here.iterdir()}:
            return False
        here = here / part
    return True


def test_every_referenced_file_exists_case_exact():
    # v1.0 pointed at references/*.md while the folder was Reference/: every
    # reference file was unreachable on Linux, where skills actually run.
    _, body = _split()
    paths = _referenced_paths(body)
    assert len(paths) >= 6
    missing = [p for p in paths if not _exists_case_exact(p)]
    assert not missing, missing


def test_description_does_not_demand_always_trigger():
    fm, _ = _split()
    assert not re.search(r"\bALWAYS trigger\b|do NOT skip", fm["description"])
    assert "Being skipped" not in fm["metadata"]["not_for"]


def test_proportion_modes_scale_output_not_thinking():
    _, body = _split()
    assert re.search(r"^## PROPORTION", body, re.M)
    for mode in ("DIRECT", "COMPACT", "FULL"):
        assert f"**{mode}**" in body
    assert re.search(r"false premise is corrected in the first sentence", body)


def test_epistemic_core_has_five_moves():
    _, body = _split()
    core = body.split("## EPISTEMIC CORE", 1)[1].split("\n## ", 1)[0]
    assert len(re.findall(r"^\d\. \*\*", core, re.M)) == 5


def test_shadow_gate_runs_in_every_mode():
    _, body = _split()
    gate = body.split("## L4", 1)[1].split("\n## ", 1)[0]
    assert re.search(r"runs on every task, DIRECT\s+included", gate)


def test_verification_rules_forbid_invented_specifics():
    _, body = _split()
    rules = body.split("## VERIFICATION RULES", 1)[1].split("\n## ", 1)[0]
    for phrase in ("verified or marked", "Unknown beats invented", "Quote exactly"):
        assert phrase in rules


def test_confidence_is_grounded_not_a_bare_percentage():
    _, body = _split()
    assert "Confidence explicitly stated as %" not in body
    conf = body.split("## CONFIDENCE RULES", 1)[1].split("\n## ", 1)[0]
    assert "HIGH / MEDIUM / LOW" in conf
    assert re.search(r"percentage only when it is computed", conf)
    assert "not assessable" in conf


def test_kalama10_is_marked_as_an_adaptation_with_the_canonical_list():
    _, body = _split()
    assert re.search(r"Kalama10 is FPCOS's own adaptation", body)
    ref = (ROOT / "references" / "CODEX_KALAMA.md").read_text(encoding="utf-8")
    # the sutta's own first and last grounds, so the canonical order is on hand
    assert "anussava" in ref and "samaṇo no garu" in ref


def test_contract_includes_verification_rules():
    _, body = _split()
    contract = body.split("## SKILL INTERFACE CONTRACT", 1)[1].split("\n## ", 1)[0]
    assert re.search(r"\| 06 \| Follow the Verification Rules", contract)
