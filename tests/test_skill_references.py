"""Tests for the generated skill reference files."""

import filecmp
import importlib.util
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SKILL = ROOT / "skills" / "oae-metadata"

spec = importlib.util.spec_from_file_location("gen_skill_references", ROOT / "scripts" / "gen_skill_references.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

REFS = gen.References()
GENERATED = ["references/class-index.md", "references/vocabularies.md", "assets/oae_data_protocol.schema.json"]


@pytest.fixture(scope="module")
def out(tmp_path_factory):
    path = tmp_path_factory.mktemp("skill")
    REFS.write(path)
    return path


def indexed_classes(out):
    return set(re.findall(r"^\| (\w+) \|", (out / "references" / "class-index.md").read_text(), re.M)) - {"Class"}


def vocabulary(out, enum):
    text = (out / "references" / "vocabularies.md").read_text()
    match = re.search(rf"^## {enum}\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return match.group(1) if match else None


def test_index_lists_every_concrete_class_and_nothing_else(out):
    expected = {
        name
        for name, cls in REFS.classes.items()
        if not cls.abstract and not cls.mixin and cls.class_uri != "linkml:Any"
    }
    assert indexed_classes(out) == expected


def test_every_indexed_class_is_in_the_bundled_schema(out):
    defs = json.loads((out / "assets" / gen.JSON_SCHEMA.name).read_text())["$defs"]
    assert indexed_classes(out) <= set(defs)


def test_enum_value_meanings_come_from_the_schema(out):
    meaning = REFS.enums["DosingDeliveryType"].permissible_values["static_point_source"].description
    assert f"- `static_point_source`: {' '.join(meaning.split())}" in vocabulary(out, "DosingDeliveryType")


def test_vocabulary_uris_get_their_labels(out):
    rows = re.findall(r"^- `(http[^`]+)`: (.+)$", vocabulary(out, "SeaNames"), re.M)
    assert len(rows) == len(REFS.enums["SeaNames"].permissible_values)
    assert ("http://vocab.nerc.ac.uk/collection/C16/current/23/", "North Atlantic Ocean") in rows


def test_enums_with_no_meanings_are_left_out(out):
    assert vocabulary(out, "ObservationType") is None


def test_schema_copy_matches_the_published_schema(out):
    assert filecmp.cmp(out / "assets" / gen.JSON_SCHEMA.name, gen.JSON_SCHEMA, shallow=False)


@pytest.mark.parametrize("relative", GENERATED)
def test_committed_files_match_a_fresh_run(out, relative):
    assert (SKILL / relative).exists(), "run `just gen-all`"
    assert filecmp.cmp(out / relative, SKILL / relative, shallow=False), f"{relative} is stale; run `just gen-all`"
