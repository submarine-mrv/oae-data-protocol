#!/usr/bin/env python3
"""Validate an OAE metadata draft against the OAE Data Protocol JSON Schema.

    python3 validate.py draft.json [--schema PATH] [--json]

Standard library only. Exit 0: no structural errors (gaps allowed). Exit 1:
structural errors. Exit 2: the file is missing, not JSON, or not a JSON object.

A gap is a required field that is absent. Everything else is a structural
error: an unknown field, a wrong type, a value outside its vocabulary.
"""

import argparse
import copy
import json
import re
import sys
from collections import namedtuple
from pathlib import Path

DEFAULT_SCHEMA = Path(__file__).resolve().parent.parent / "assets" / "oae_data_protocol.schema.json"

SUPPORTED_KEYWORDS = {
    "$ref", "$defs", "type", "properties", "required", "additionalProperties", "const", "enum",
    "items", "contains", "if", "then", "anyOf", "allOf", "pattern", "minItems", "minimum", "maximum",
}  # fmt: skip
# format is an annotation in Draft 2019-09 unless a validator opts in.
IGNORED_KEYWORDS = {"description", "title", "$schema", "$id", "metamodel_version", "version", "format"}

TOP_LEVEL_LISTS = ("experiments", "datasets")

Error = namedtuple("Error", "path kind message")
Finding = namedtuple("Finding", "item path message")
Result = namedtuple("Result", "structural gaps notes")


class UnknownBranch(Exception):
    """A union whose selector field is missing or names no allowed class."""


# ---------- JSON Schema subset ----------

_TYPES = {
    "object": lambda x: isinstance(x, dict),
    "array": lambda x: isinstance(x, list),
    "string": lambda x: isinstance(x, str),
    "boolean": lambda x: isinstance(x, bool),
    "null": lambda x: x is None,
    "number": lambda x: isinstance(x, (int, float)) and not isinstance(x, bool),
    "integer": lambda x: (isinstance(x, int) and not isinstance(x, bool)) or (isinstance(x, float) and x.is_integer()),
}


def _type_name(value):
    for name in ("null", "boolean", "integer", "number", "string", "array", "object"):
        if _TYPES[name](value):
            return name
    return type(value).__name__


def _same(a, b):
    """JSON equality: true is not 1."""
    if isinstance(a, bool) != isinstance(b, bool):
        return False
    return a == b


def _ref_name(schema):
    return schema.get("$ref", "").rsplit("/", 1)[-1]


def _join(path, key):
    if isinstance(key, int):
        return f"{path}[{key}]"
    return f"{path}.{key}" if path else key


def errors(instance, schema, defs, path="", route=None):
    """Errors for instance against schema. `route` picks one branch of a class union."""
    out = []
    if schema is True or not schema:
        return out

    if "$ref" in schema:
        out += errors(instance, defs[_ref_name(schema)], defs, path, route)

    if "type" in schema:
        allowed = [schema["type"]] if isinstance(schema["type"], str) else schema["type"]
        if not any(_TYPES[t](instance) for t in allowed):
            out.append(Error(path, "type", f"expected {' or '.join(allowed)}, got {_type_name(instance)}"))
            return out

    if "const" in schema and not _same(instance, schema["const"]):
        out.append(Error(path, "const", f"must be {json.dumps(schema['const'])}"))
    if "enum" in schema and not any(_same(instance, option) for option in schema["enum"]):
        shown = ", ".join(json.dumps(o) for o in schema["enum"][:12])
        more = f", and {len(schema['enum']) - 12} more" if len(schema["enum"]) > 12 else ""
        out.append(Error(path, "enum", f"{json.dumps(instance)} is not an allowed value ({shown}{more})"))

    if isinstance(instance, str) and "pattern" in schema and not re.search(schema["pattern"], instance):
        out.append(Error(path, "pattern", f"does not match the pattern {schema['pattern']}"))

    if _TYPES["number"](instance):
        if "minimum" in schema and instance < schema["minimum"]:
            out.append(Error(path, "minimum", f"must be at least {schema['minimum']}"))
        if "maximum" in schema and instance > schema["maximum"]:
            out.append(Error(path, "maximum", f"must be at most {schema['maximum']}"))

    if isinstance(instance, dict):
        properties = schema.get("properties", {})
        for name in schema.get("required", []):
            if name not in instance:
                out.append(Error(path, "required", f"missing required field '{name}'"))
        for name, value in instance.items():
            if name in properties:
                out += errors(value, properties[name], defs, _join(path, name), route)
            elif schema.get("additionalProperties") is False:
                out.append(Error(path, "additionalProperties", f"unknown field '{name}'"))
            elif isinstance(schema.get("additionalProperties"), dict):
                out += errors(value, schema["additionalProperties"], defs, _join(path, name), route)

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            out.append(Error(path, "minItems", f"needs at least {schema['minItems']} item(s)"))
        if "items" in schema:
            for i, item in enumerate(instance):
                out += errors(item, schema["items"], defs, _join(path, i), route)
        if "contains" in schema and not any(not errors(item, schema["contains"], defs) for item in instance):
            out.append(Error(path, "contains", "has no item of the required form"))

    for part in schema.get("allOf", []):
        out += errors(instance, part, defs, path, route)

    if "if" in schema and not errors(instance, schema["if"], defs, path):
        out += errors(instance, schema.get("then", {}), defs, path, route)

    if "anyOf" in schema:
        out += _any_of(instance, schema["anyOf"], defs, path, route)

    return out


def _any_of(instance, branches, defs, path, route):
    if route:
        try:
            chosen = route(instance, branches, defs)
        except UnknownBranch as problem:
            return [Error(path, "anyOf", str(problem))]
        if chosen is not None:
            return errors(instance, chosen, defs, f"{path}<{_ref_name(chosen)}>", route)

    results = [errors(instance, branch, defs, path, route) for branch in branches]
    if any(not result for result in results):
        return []
    names = [_ref_name(b) or "an inline form" for b in branches]
    best = min(range(len(branches)), key=lambda i: len(results[i]))
    out = [Error(path, "anyOf", f"matches none of the allowed forms ({', '.join(names)}); closest is {names[best]}")]
    return out + results[best]


def is_valid(instance, schema, defs):
    """Plain JSON Schema validity, with no routing."""
    return not errors(instance, schema, defs)


# ---------- OAE routing ----------


def experiment_class(experiment):
    """Mirrors the Metadata Builder's getExperimentSchemaType."""
    types = experiment.get("experiment_types")
    types = types if isinstance(types, list) else []
    if "model" in types:
        return "Model"
    if "intervention" in types and "tracer_study" in types:
        return "InterventionWithTracer"
    if "intervention" in types:
        return "Intervention"
    if "tracer_study" in types:
        return "Tracer"
    return "InSituExperiment"


def dataset_class(dataset):
    return "ModelOutputDataset" if dataset.get("dataset_type") == "model_output" else "FieldDataset"


def route_union(instance, branches, defs):
    """Pick the branch of a class union the way the Metadata Builder does, or None to try them all."""
    names = [_ref_name(b) for b in branches]
    if not all(names) or not isinstance(instance, dict):
        return None
    by_name = dict(zip(names, branches))

    if all("schema_class" in defs[n].get("properties", {}) for n in names):
        value = instance.get("schema_class")
        if value is None:
            raise UnknownBranch("missing 'schema_class', which says what kind of variable this is")
        if value not in by_name:
            raise UnknownBranch(f"schema_class {json.dumps(value)} is not one of: {', '.join(sorted(names))}")
        return by_name[value]

    if set(names) == {"DyeCalibration", "PHCalibration"}:
        return by_name["DyeCalibration" if instance.get("standard_used") == "dye" else "PHCalibration"]

    return None


def patched(schema):
    """LinkML drops the condition on this rule (oae-data-protocol issue #25), which would make
    mcdr_forcing_description required on every model dataset. The Metadata Builder applies the same fix."""
    schema = copy.deepcopy(schema)
    dataset = schema["$defs"].get("ModelOutputDataset", {})
    for part in [dataset] + list(dataset.get("allOf", [])):
        condition = part.get("if", {}).get("properties", {})
        if "simulation_type" in condition:
            condition["simulation_type"] = {"type": "array", "contains": {"const": "perturbation"}}
    return schema


# ---------- bounding boxes ----------
# JSON Schema sees a box as a plain string. These are the Metadata Builder's rules (validateSpatialBounds).


def check_box(box):
    """(error or None, plain-words reading or None) for a "south west north east" box string."""
    parts = box.split()
    if len(parts) != 4:
        return "a box needs four numbers separated by spaces: south west north east (minLat minLon maxLat maxLon)", None
    try:
        south, west, north, east = (float(p) for p in parts)
    except ValueError:
        return "every box value must be a number: south west north east", None
    if not all(-90 <= lat <= 90 for lat in (south, north)):
        return "the 1st and 3rd box values are latitudes and must be between -90 and 90; the order is south west north east", None
    if not all(-180 <= lon <= 180 for lon in (west, east)):
        return "the 2nd and 4th box values are longitudes and must be between -180 and 180", None
    if north <= south:
        return "north must be greater than south; the order is south west north east", None
    south_s, west_s, north_s, east_s = parts
    reading = (
        f"{south_s.lstrip('-')}°{'S' if south < 0 else 'N'} to {north_s.lstrip('-')}°{'S' if north < 0 else 'N'}, "
        f"{west_s.lstrip('-')}°{'W' if west < 0 else 'E'} to {east_s.lstrip('-')}°{'W' if east < 0 else 'E'}"
    )
    if west > east:
        reading += " (crosses the antimeridian)"
    return None, reading


def boxes(node, path=""):
    """Every (path, box string) in the document."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "box" and isinstance(value, str):
                yield _join(path, key), value
            else:
                yield from boxes(value, _join(path, key))
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from boxes(item, _join(path, i))


# ---------- findings ----------


def _check(item, class_name, schema, label):
    found = errors(item, {"$ref": f"#/$defs/{class_name}"}, schema["$defs"], "", route_union)
    return [(Finding(label, e.path, e.message), e.kind) for e in found]


def check_item(item, class_name, schema, label=None):
    """Findings for one object validated as class_name."""
    return [finding for finding, _ in _check(item, class_name, schema, label or class_name)]


def _label(collection, index, item, class_name):
    name = item.get("name") if isinstance(item, dict) else None
    shown = f' "{name}"' if isinstance(name, str) and name else ""
    return f"{collection}[{index}]{shown} ({class_name})"


def validate(doc, schema):
    schema = patched(schema)
    structural, gaps = [], []
    notes = [
        "Applied the Metadata Builder's fix for the simulation_type rule: "
        "mcdr_forcing_description is required only when simulation_type contains 'perturbation'."
    ]

    def add(item, class_name, label):
        for finding, kind in _check(item, class_name, schema, label):
            (gaps if kind == "required" else structural).append(finding)

    allowed = set(schema.get("properties", {}))
    for key in doc:
        if key not in allowed:
            structural.append(Finding("file", "", f"unknown top-level field '{key}' (allowed: {', '.join(sorted(allowed))})"))

    if "project" in doc:
        if isinstance(doc["project"], dict):
            add(doc["project"], "Project", "project")
        else:
            structural.append(Finding("project", "", f"expected object, got {_type_name(doc['project'])}"))

    for collection, pick in (("experiments", experiment_class), ("datasets", dataset_class)):
        if collection not in doc:
            continue
        if not isinstance(doc[collection], list):
            structural.append(Finding(collection, "", f"expected array, got {_type_name(doc[collection])}; use [] for none"))
            continue
        for index, item in enumerate(doc[collection]):
            if not isinstance(item, dict):
                structural.append(Finding(f"{collection}[{index}]", "", f"expected object, got {_type_name(item)}"))
                continue
            class_name = pick(item)
            add(item, class_name, _label(collection, index, item, class_name))

    for key in ("version", "protocol_git_hash", "metadata_builder_git_hash"):
        if key in doc and not isinstance(doc[key], str):
            structural.append(Finding("file", key, f"expected string, got {_type_name(doc[key])}"))

    for path, box in boxes(doc):
        problem, reading = check_box(box)
        if problem:
            structural.append(Finding("file", path, problem))
        else:
            notes.append(f'{path} "{box}" reads as {reading}. Check this against the source.')

    if isinstance(doc.get("version"), str) and schema.get("version") and doc["version"] != schema["version"]:
        notes.append(f"The file says version {doc['version']}; this schema is {schema['version']}.")

    return Result(structural, gaps, notes)


# ---------- command line ----------


def _count(n, word):
    return f"{n} {word}{'' if n == 1 else 's'}"


def status_line(result):
    if result.structural:
        return f"Status: {_count(len(result.structural), 'structural error')}, {_count(len(result.gaps), 'gap')}"
    return f"Status: validated, no structural errors ({_count(len(result.gaps), 'gap')})"


def render(result):
    lines = [status_line(result)]
    for title, findings in (("Structural errors (fix these)", result.structural), ("Gaps (report these; do not guess)", result.gaps)):
        if not findings:
            continue
        lines += ["", title]
        current = None
        for finding in findings:
            if finding.item != current:
                current = finding.item
                lines.append(f"  {current}")
            where = f"{finding.path}: " if finding.path else ""
            lines.append(f"    - {where}{finding.message}")
    if result.notes:
        lines += ["", "Notes"] + [f"  - {note}" for note in result.notes]
    return "\n".join(lines)


def fail(message):
    print(message, file=sys.stderr)
    return 2


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate an OAE metadata draft.")
    parser.add_argument("file")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    parser.add_argument("--json", action="store_true", help="print findings as JSON")
    args = parser.parse_args(argv)

    try:
        doc = json.loads(Path(args.file).read_text(encoding="utf-8"))
    except OSError as problem:
        return fail(f"Cannot read {args.file}: {problem.strerror or problem}")
    except ValueError as problem:
        return fail(f"{args.file} is not valid JSON: {problem}")
    if not isinstance(doc, dict):
        return fail(f"{args.file} must hold a JSON object with project, experiments and/or datasets; got {_type_name(doc)}")
    try:
        schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))
    except (OSError, ValueError) as problem:
        return fail(f"Cannot load the schema at {args.schema}: {problem}")

    result = validate(doc, schema)
    if args.json:
        as_dicts = lambda findings: [f._asdict() for f in findings]  # noqa: E731
        print(json.dumps({"status": status_line(result), "structural": as_dicts(result.structural), "gaps": as_dicts(result.gaps), "notes": result.notes}, indent=2))
    else:
        print(render(result))
    return 1 if result.structural else 0


if __name__ == "__main__":
    sys.exit(main())
