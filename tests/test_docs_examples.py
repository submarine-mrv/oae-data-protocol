"""Validate the JSON examples in the hand-written docs against the validation schema.

Mark an example by putting `<!-- validate: ClassName -->` on the line before its ```json fence.
`Container` validates a whole metadata file; any other name validates against that class.
"""

import json
import re
from pathlib import Path

import pytest
from jsonschema import Draft201909Validator

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "src" / "docs" / "files"
SCHEMA = json.loads(
    (ROOT / "project" / "jsonschema" / "oae_data_protocol.validation.schema.json").read_text()
)

MARKED = re.compile(r"<!-- validate: (\w+) -->\s*```json\n(.*?)```", re.S)


def marked_examples():
    for page in sorted(DOCS.rglob("*.md")):
        for match in MARKED.finditer(page.read_text()):
            cls, body = match.groups()
            yield pytest.param(cls, body, id=f"{page.relative_to(DOCS)}:{cls}")


EXAMPLES = list(marked_examples())


def test_docs_have_marked_examples():
    assert EXAMPLES, "no <!-- validate: ... --> examples found in the docs"


def messages(errors, branch=""):
    """One line per error. anyOf failures (experiments, datasets, variables) are expanded into
    each candidate class's errors, so the real cause shows next to the class it belongs to."""
    for error in errors:
        path = "/".join(map(str, error.absolute_path)) or "(root)"
        if not error.context:
            yield f"{path}{branch}: {error.message}"
            continue
        for sub in error.context:
            ref = error.validator_value[sub.relative_schema_path[0]].get("$ref", "")
            yield from messages([sub], f" [as {ref.rsplit('/', 1)[-1]}]")


@pytest.mark.parametrize("cls,body", EXAMPLES)
def test_example_validates(cls, body):
    if cls == "Container":
        schema = SCHEMA
    else:
        assert cls in SCHEMA["$defs"], f"{cls} is not a class in the schema"
        schema = {"$ref": f"#/$defs/{cls}", "$defs": SCHEMA["$defs"]}
    errors = list(messages(Draft201909Validator(schema).iter_errors(json.loads(body))))
    assert not errors, "\n".join(errors)
