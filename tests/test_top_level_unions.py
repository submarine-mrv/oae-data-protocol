"""The slots that hold experiments and datasets list every concrete class by hand.
These tests fail when a list and the class tree disagree."""

import json
from pathlib import Path

import pytest
from jsonschema import Draft201909Validator
from linkml_runtime.utils.schemaview import SchemaView

ROOT = Path(__file__).parent.parent
SV = SchemaView(str(ROOT / "src" / "oae_data_protocol" / "schema" / "oae_data_protocol.yaml"))
SCHEMA = json.loads((ROOT / "project" / "jsonschema" / "oae_data_protocol.schema.json").read_text())

UNION_SLOTS = [
    ("Container", "experiments", "Experiment"),
    ("Container", "datasets", "Dataset"),
]


def concrete_family(base):
    names = [base, *SV.class_descendants(base, reflexive=False)]
    return {n for n in names if not SV.get_class(n).abstract and not SV.get_class(n).mixin}


@pytest.mark.parametrize("cls,slot,base", UNION_SLOTS)
def test_union_lists_every_concrete_class(cls, slot, base):
    listed = {expr.range for expr in SV.induced_slot(slot, cls).any_of}
    assert listed == concrete_family(base)


@pytest.mark.parametrize("cls,slot,base", UNION_SLOTS)
def test_json_schema_has_the_union(cls, slot, base):
    items = SCHEMA["$defs"][cls]["properties"][slot]["items"]
    refs = {branch["$ref"].rsplit("/", 1)[-1] for branch in items["anyOf"]}
    assert refs == concrete_family(base)


@pytest.mark.parametrize("doc", [{}, {"experiments": [], "datasets": []}])
def test_empty_project_file_validates(doc):
    assert not list(Draft201909Validator(SCHEMA).iter_errors(doc))


@pytest.mark.parametrize("slot", ["experiments", "datasets"])
def test_null_collection_is_rejected(slot):
    """An empty project omits the key or uses []."""
    assert list(Draft201909Validator(SCHEMA).iter_errors({slot: None}))


def test_nested_slots_stay_strict():
    """A generic variable's instrument is the base class, not a union of subclasses."""
    prop = SCHEMA["$defs"]["DiscreteMeasuredVariable"]["properties"]["analyzing_instrument"]
    assert prop["$ref"] == "#/$defs/AnalyzingInstrument"
    assert "anyOf" not in prop


def test_project_does_not_nest_experiments():
    """Experiments live in the container and point back with project_id."""
    assert "experiments" not in SCHEMA["$defs"]["Project"]["properties"]


def test_no_validation_schema_file():
    assert not (ROOT / "project" / "jsonschema" / "oae_data_protocol.validation.schema.json").exists()
