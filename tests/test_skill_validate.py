"""Tests for the skill's validate script.

Fixtures start from the examples in the hand-written docs, which CI already validates.
"""

import copy
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft201909Validator

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "skills" / "oae-metadata" / "scripts" / "validate.py"
SCHEMA_PATH = ROOT / "project" / "jsonschema" / "oae_data_protocol.schema.json"
SCHEMA = json.loads(SCHEMA_PATH.read_text())
DOCS = ROOT / "src" / "docs" / "files"

spec = importlib.util.spec_from_file_location("skill_validate", SCRIPT)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def doc_example(page, cls):
    text = (DOCS / page).read_text()
    match = re.search(rf"<!-- validate: {cls} -->\s*```json\n(.*?)```", text, re.S)
    return json.loads(match.group(1))


@pytest.fixture
def container():
    return doc_example("metadata-format.md", "Container")


@pytest.fixture
def ph_instrument():
    return doc_example("instruments-calibration/index.md", "PHInstrument")


def messages(findings):
    return [f"{f.item} | {f.path} | {f.message}" for f in findings]


def run_cli(tmp_path, content, *args):
    path = tmp_path / "draft.json"
    path.write_text(content if isinstance(content, str) else json.dumps(content))
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(path), "--schema", str(SCHEMA_PATH), *args],
        capture_output=True,
        text=True,
    )


# --- whole files ---


def test_docs_example_has_no_findings(container):
    result = v.validate(container, SCHEMA)
    assert messages(result.structural) == []
    assert messages(result.gaps) == []


@pytest.mark.parametrize("keep", [["project"], ["datasets"], ["experiments"], []])
def test_partial_file_validates(container, keep):
    doc = {k: container[k] for k in keep}
    result = v.validate(doc, SCHEMA)
    assert messages(result.structural) == []
    assert messages(result.gaps) == []


def test_unknown_top_level_key_is_structural(container):
    container["notes"] = "x"
    result = v.validate(container, SCHEMA)
    assert any("notes" in m for m in messages(result.structural))


# --- gaps and structural errors ---


def test_missing_required_field_is_a_gap(container):
    del container["experiments"][0]["name"]
    result = v.validate(container, SCHEMA)
    assert messages(result.structural) == []
    assert len(result.gaps) == 1
    gap = result.gaps[0]
    assert "experiments[0]" in gap.item and "InSituExperiment" in gap.item
    assert "name" in gap.message


def test_unknown_field_is_structural_and_named(container):
    container["experiments"][0]["favourite_colour"] = "blue"
    result = v.validate(container, SCHEMA)
    assert messages(result.gaps) == []
    assert len(result.structural) == 1
    assert "favourite_colour" in result.structural[0].message


def test_value_outside_enum_is_structural(container):
    container["datasets"][0]["dataset_type"] = "not_a_type"
    result = v.validate(container, SCHEMA)
    assert any("dataset_type" in f.path for f in result.structural)


# --- routing ---


@pytest.mark.parametrize(
    "types,cls",
    [
        (["model"], "Model"),
        (["intervention", "tracer_study"], "InterventionWithTracer"),
        (["intervention"], "Intervention"),
        (["tracer_study"], "Tracer"),
        (["baseline"], "InSituExperiment"),
        (None, "InSituExperiment"),
    ],
)
def test_experiment_routing(types, cls):
    experiment = {} if types is None else {"experiment_types": types}
    assert v.experiment_class(experiment) == cls


@pytest.mark.parametrize("dataset_type,cls", [("model_output", "ModelOutputDataset"), ("bottle", "FieldDataset"), (None, "FieldDataset")])
def test_dataset_routing(dataset_type, cls):
    assert v.dataset_class({} if dataset_type is None else {"dataset_type": dataset_type}) == cls


def test_variable_errors_come_from_its_schema_class_only(container):
    variable = container["datasets"][0]["variables"][0]
    variable["made_up"] = 1
    result = v.validate(container, SCHEMA)
    assert len(result.structural) == 1
    finding = result.structural[0]
    assert "made_up" in finding.message
    assert variable["schema_class"] in finding.path


def test_unknown_schema_class_is_one_finding(container):
    container["datasets"][0]["variables"][0]["schema_class"] = "Nope"
    result = v.validate(container, SCHEMA)
    assert len(result.structural) == 1
    assert "Nope" in result.structural[0].message
    assert messages(result.gaps) == []


def test_missing_schema_class_is_one_finding(container):
    del container["datasets"][0]["variables"][0]["schema_class"]
    result = v.validate(container, SCHEMA)
    assert len(result.structural) == 1
    assert "schema_class" in result.structural[0].message


def test_dye_calibration_reports_dye_errors_only(ph_instrument):
    ph_instrument["calibration"] = {"standard_used": "dye", "made_up": 1}
    findings = v.check_item(ph_instrument, "PHInstrument", SCHEMA)
    paths = {f.path for f in findings}
    assert any("DyeCalibration" in p for p in paths)
    assert not any("PHCalibration" in p for p in paths)


# --- the simulation_type patch ---


def forcing_gaps(simulation_type):
    dataset = {"dataset_type": "model_output", "simulation_type": simulation_type}
    findings = v.check_item(dataset, "ModelOutputDataset", v.patched(SCHEMA))
    return [f for f in findings if "mcdr_forcing_description" in f.message]


def test_forcing_description_not_required_for_other_runs():
    assert forcing_gaps(["other"]) == []


def test_forcing_description_required_for_perturbation_runs():
    assert len(forcing_gaps(["perturbation"])) == 1


def test_result_notes_the_patch(container):
    assert any("simulation_type" in note for note in v.validate(container, SCHEMA).notes)


# --- agreement with jsonschema ---


def mutations(doc):
    """Yield copies of doc with one node dropped, retyped or given an unknown key."""

    def walk(node, path):
        if isinstance(node, dict):
            for key in list(node):
                yield path + [key]
                yield from walk(node[key], path + [key])
        elif isinstance(node, list):
            for i, item in enumerate(node):
                yield path + [i]
                yield from walk(item, path + [i])

    for path in walk(doc, []):
        for kind in ("drop", "retype", "extra"):
            mutated = copy.deepcopy(doc)
            parent = mutated
            for step in path[:-1]:
                parent = parent[step]
            last = path[-1]
            if kind == "drop":
                if isinstance(parent, dict):
                    del parent[last]
                else:
                    parent.pop(last)
            elif kind == "retype":
                parent[last] = 12345 if not isinstance(parent[last], (int, float)) else "text"
            elif isinstance(parent[last], dict):
                parent[last]["zz_unknown"] = True
            else:
                continue
            yield kind, path, mutated


@pytest.mark.parametrize("page,cls", [("metadata-format.md", "Container"), ("instruments-calibration/index.md", "PHInstrument")])
def test_verdicts_match_jsonschema(page, cls):
    doc = doc_example(page, cls)
    schema = SCHEMA if cls == "Container" else {"$ref": f"#/$defs/{cls}", "$defs": SCHEMA["$defs"]}
    oracle = Draft201909Validator(schema)
    checked = 0
    for kind, path, mutated in mutations(doc):
        expected = oracle.is_valid(mutated)
        actual = v.is_valid(mutated, schema, SCHEMA["$defs"])
        assert actual == expected, f"{kind} at {path}: jsonschema says {expected}"
        checked += 1
    assert checked >= 15


def test_schema_uses_only_supported_keywords():
    seen = set()

    def walk(node, is_name_map=False):
        if isinstance(node, dict):
            for key, value in node.items():
                if not is_name_map:
                    seen.add(key)
                walk(value, key in ("properties", "$defs"))
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(SCHEMA)
    assert seen - v.SUPPORTED_KEYWORDS - v.IGNORED_KEYWORDS == set()


# --- command line ---


def test_cli_ok(tmp_path, container):
    done = run_cli(tmp_path, container)
    assert done.returncode == 0
    assert done.stdout.startswith("Status: validated, no structural errors (0 gaps)")


def test_cli_reports_structural_errors(tmp_path, container):
    container["experiments"][0]["favourite_colour"] = "blue"
    del container["experiments"][0]["name"]
    done = run_cli(tmp_path, container)
    assert done.returncode == 1
    assert done.stdout.startswith("Status: 1 structural error, 1 gap")
    assert "favourite_colour" in done.stdout


def test_cli_gaps_alone_exit_zero(tmp_path, container):
    del container["experiments"][0]["name"]
    done = run_cli(tmp_path, container)
    assert done.returncode == 0
    assert "(1 gap)" in done.stdout


@pytest.mark.parametrize("content", ["{not json", "[1, 2]", '"text"'])
def test_cli_rejects_unreadable_input(tmp_path, content):
    done = run_cli(tmp_path, content)
    assert done.returncode == 2
    assert "Traceback" not in done.stderr
    assert done.stderr.strip()


def test_cli_missing_file(tmp_path):
    done = subprocess.run([sys.executable, str(SCRIPT), str(tmp_path / "nope.json")], capture_output=True, text=True)
    assert done.returncode == 2
    assert "Traceback" not in done.stderr


def test_cli_json_output(tmp_path, container):
    del container["experiments"][0]["name"]
    done = run_cli(tmp_path, container, "--json")
    out = json.loads(done.stdout)
    assert set(out) >= {"status", "structural", "gaps", "notes"}
    assert out["gaps"][0]["message"]


def test_script_imports_only_the_standard_library():
    source = SCRIPT.read_text()
    imported = set(re.findall(r"^(?:import|from) (\w+)", source, re.M))
    assert imported <= {"argparse", "json", "re", "sys", "pathlib", "collections", "copy"}
