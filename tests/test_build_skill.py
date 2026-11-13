"""Tests for assembling the distributable skill."""

import filecmp
import importlib.util
import json
import re
import zipfile
from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

ROOT = Path(__file__).parent.parent

spec = importlib.util.spec_from_file_location("build_skill", ROOT / "scripts" / "build_skill.py")
bs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bs)

ENUMS = SchemaView(str(bs.SCHEMA_YAML)).all_enums()


@pytest.fixture(scope="module")
def skill(tmp_path_factory):
    return bs.build(tmp_path_factory.mktemp("build") / "oae-metadata")


def vocabulary(skill, enum):
    text = (skill / "references" / "docs" / bs.VOCABULARY_PAGE).read_text()
    match = re.search(rf"^## {enum}\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return match.group(1) if match else None


def test_hand_written_skill_files_are_copied_unchanged(skill):
    for relative in ("SKILL.md", "scripts/validate.py", "references/builder-handoff.md"):
        assert filecmp.cmp(skill / relative, bs.SKILL / relative, shallow=False)


def test_schema_is_bundled_and_the_validator_finds_it(skill):
    assert filecmp.cmp(skill / "assets" / bs.JSON_SCHEMA.name, bs.JSON_SCHEMA, shallow=False)
    import subprocess
    import sys

    draft = skill.parent / "draft.json"
    draft.write_text(json.dumps({"project": {"name": "x"}}))
    done = subprocess.run([sys.executable, str(skill / "scripts" / "validate.py"), str(draft)], capture_output=True, text=True)
    assert done.stdout.startswith("Status:")


def test_every_file_skill_md_names_exists(skill):
    named = set(re.findall(r"`((?:references|scripts|assets)/[\w./-]+)`", (skill / "SKILL.md").read_text()))
    assert named, "SKILL.md names no files"
    missing = sorted(path for path in named if not (skill / path).exists())
    assert missing == []


def test_docs_pages_keep_their_content_with_links_made_absolute(skill):
    page = (skill / "references" / "docs" / "variables.md").read_text()
    assert "Selection → Schema Class Mapping" in page
    assert "(https://schema.oaedata.org/DiscretePHVariable.md)" in page
    assert "](../" not in page


def test_links_are_resolved_from_the_page_folder():
    text = "[a](../Project.md) [b](index.md#x) [c](https://e.org/y) [d](#here)"
    fixed = bs.absolute_links(text, "Variables/index.md")
    assert "(https://schema.oaedata.org/Project.md)" in fixed
    assert "(https://schema.oaedata.org/Variables/index.md#x)" in fixed
    assert "(https://e.org/y)" in fixed and "(#here)" in fixed


def test_enum_value_meanings_come_from_the_schema(skill):
    meaning = ENUMS["DosingDeliveryType"].permissible_values["static_point_source"].description
    assert f"- `static_point_source`: {' '.join(meaning.split())}" in vocabulary(skill, "DosingDeliveryType")


def test_vocabulary_uris_get_their_labels(skill):
    rows = re.findall(r"^- `(http[^`]+)`: (.+)$", vocabulary(skill, "SeaNames"), re.M)
    assert len(rows) == len(ENUMS["SeaNames"].permissible_values)
    assert ("http://vocab.nerc.ac.uk/collection/C16/current/23/", "North Atlantic Ocean") in rows


def test_enums_with_no_meanings_are_left_out(skill):
    assert vocabulary(skill, "ObservationType") is None


def test_zip_holds_the_skill_folder(skill):
    with zipfile.ZipFile(skill.parent / "oae-metadata.zip") as archive:
        names = archive.namelist()
    assert "oae-metadata/SKILL.md" in names
    assert "oae-metadata/assets/oae_data_protocol.schema.json" in names
