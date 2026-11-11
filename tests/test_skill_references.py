"""Tests for the generated skill reference files."""

import filecmp
import importlib.util
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SKILL = ROOT / "skills" / "oae-metadata"

spec = importlib.util.spec_from_file_location("gen_skill_references", ROOT / "scripts" / "gen_skill_references.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

REFS = gen.References()
GENERATED = ["references/classes", "references/enums", "references/class-index.md", "assets"]


@pytest.fixture(scope="module")
def out(tmp_path_factory):
    path = tmp_path_factory.mktemp("skill")
    REFS.write(path)
    return path


def page(out, name):
    return (out / "references" / "classes" / f"{name}.md").read_text()


def test_one_file_per_concrete_class(out):
    written = {p.stem for p in (out / "references" / "classes").glob("*.md")}
    expected = {
        name
        for name, cls in REFS.classes.items()
        if not cls.abstract and not cls.mixin and cls.class_uri != "linkml:Any"
    }
    assert written == expected


def test_class_page_lists_inherited_and_nested_fields(out):
    text = page(out, "FieldDataset")
    assert re.search(r"^\| name \| yes \|", text, re.M)
    assert re.search(r"^\| platform_info \|.*\[Platform\]\(Platform\.md\)", text, re.M)


def test_abstract_range_lists_its_concrete_classes(out):
    row = re.search(r"^\| variables \|.*$", page(out, "FieldDataset"), re.M).group(0)
    assert "[DiscretePHVariable](DiscretePHVariable.md)" in row
    assert "FieldVariable.md" not in row


def test_rules_render_including_inherited_ones(out):
    assert "When `data_accessibility` is `open_access`, `data_access_link` is required." in page(out, "FieldDataset")
    assert "When `simulation_type` contains `perturbation`, `mcdr_forcing_description` is required." in page(
        out, "ModelOutputDataset"
    )


def test_large_enum_gets_its_own_file(out):
    assert "(../enums/SeaNames.md)" in page(out, "Project")
    rows = re.findall(r"^\| `", (out / "references" / "enums" / "SeaNames.md").read_text(), re.M)
    assert len(rows) == len(REFS.enums["SeaNames"].permissible_values)


def test_vocabulary_enum_rows_have_labels(out):
    for name in ("SeaNames", "PlatformType"):
        text = (out / "references" / "enums" / f"{name}.md").read_text()
        assert not re.search(r"^\| `[^`]+` \|\s*\|$", text, re.M), f"{name} has a value with no label"


def test_small_enum_is_inlined(out):
    row = re.search(r"^\| experiment_types \|.*$", page(out, "InSituExperiment"), re.M).group(0)
    assert "`baseline`" in row


def test_pinned_values_are_shown(out):
    assert re.search(r"^\| schema_class \| yes \| no \| always `DiscretePHVariable` \|", page(out, "DiscretePHVariable"), re.M)
    assert re.search(r"^\| instrument_type \|.*always `gas_analyzer`", page(out, "CO2GasDetector"), re.M)


def test_enum_value_meanings_are_in_the_class_file(out):
    text = page(out, "Intervention")
    meaning = REFS.enums["DosingDeliveryType"].permissible_values["static_point_source"].description
    assert "## Vocabularies" in text
    assert f"- `static_point_source`: {' '.join(meaning.split())}" in text


def test_enums_without_meanings_get_no_vocabulary_entry(out):
    assert "### observation_type" not in page(out, "DiscretePHVariable")


def test_every_link_resolves(out):
    refs = out / "references"
    for path in [*refs.glob("classes/*.md"), refs / "class-index.md"]:
        for target in re.findall(r"\]\((?!https?:)([^)]+\.md)\)", path.read_text()):
            assert (path.parent / target).exists(), f"{path.name} links to missing {target}"


def test_schema_copy_matches_the_published_schema(out):
    assert filecmp.cmp(out / "assets" / gen.JSON_SCHEMA.name, gen.JSON_SCHEMA, shallow=False)


def test_unknown_rule_shape_raises():
    from linkml_runtime.linkml_model.meta import AnonymousClassExpression, SlotDefinition

    expression = AnonymousClassExpression(slot_conditions={"x": SlotDefinition(name="x", minimum_value=1)})
    with pytest.raises(ValueError, match="x"):
        REFS.conditions(expression)


def compare(left, right):
    if left.is_file():
        return filecmp.cmp(left, right, shallow=False)
    diff = filecmp.dircmp(left, right)
    return not (diff.left_only or diff.right_only or diff.diff_files)


@pytest.mark.parametrize("relative", GENERATED)
def test_committed_files_match_a_fresh_run(out, relative):
    assert (SKILL / relative).exists(), "run `just gen-all`"
    assert compare(out / relative, SKILL / relative), f"{relative} is stale; run `just gen-all`"
