"""project_id and experiment_id share one pattern wherever they appear."""

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCHEMA = json.loads((ROOT / "project" / "jsonschema" / "oae_data_protocol.schema.json").read_text())
ID_SLOTS = ("project_id", "experiment_id")


def id_properties():
    for cls, body in SCHEMA["$defs"].items():
        for slot in ID_SLOTS:
            if slot in body.get("properties", {}):
                yield cls, slot, body["properties"][slot]


def test_every_id_property_has_the_pattern():
    patterns = {(cls, slot): prop.get("pattern") for cls, slot, prop in id_properties()}
    assert patterns
    assert set(patterns.values()) == {"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$"}


PATTERN = re.compile(next(id_properties())[2]["pattern"])


@pytest.mark.parametrize(
    "value",
    ["E1", "EbbCarbon_20241010_PortAngelesWA", "planetary_tuftscove_intervention_tc26.1", "A" * 64],
)
def test_accepts(value):
    assert PATTERN.search(value)


@pytest.mark.parametrize("value", ["", "has space", "slash/id", "-leading", "é", "A" * 65])
def test_rejects(value):
    assert not PATTERN.search(value)
