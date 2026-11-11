"""Generate the oae-metadata skill's reference files from the LinkML schema.

    python scripts/gen_skill_references.py [--out skills/oae-metadata]

Writes references/class-index.md (every concrete class), references/vocabularies.md (what each
enum value means, which the JSON Schema does not carry), and a copy of the JSON Schema in assets/.
"""

import argparse
import shutil
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_YAML = ROOT / "src" / "oae_data_protocol" / "schema" / "oae_data_protocol.yaml"
JSON_SCHEMA = ROOT / "project" / "jsonschema" / "oae_data_protocol.schema.json"
# Vocabulary enums hold bare URIs; their labels come from the fetched vocabularies.
VOCABULARIES = [ROOT / "ontologies" / "sea_names.ttl", ROOT / "ontologies" / "platform_types.ttl"]

# class-index.md groups, by the root class each class descends from.
GROUPS = [
    ("Project", ["Project", "Container"]),
    ("Experiments", ["Experiment"]),
    ("Datasets", ["Dataset"]),
    ("Variables", ["Variable"]),
    ("Instruments and calibrations", ["AnalyzingInstrument", "SamplingInstrument", "Calibration", "StandardGas"]),
]
OTHER_GROUP = "Supporting"

INDEX_INTRO = """\
# Classes

Every class a metadata file can use. Each is defined in `assets/oae_data_protocol.schema.json` under
`$defs`, with its fields (`properties`), which are `required`, and its conditional rules (`if`/`then`).
"""

VOCABULARY_INTRO = """\
# Vocabularies

What each value means, for the enums whose values need explaining. The JSON Schema lists the allowed
values of every enum under `$defs.<EnumName>`; it does not carry these meanings. Find an enum here by
the name its field references. An enum that is not here has self-explanatory values.
"""


def one_line(text):
    return " ".join((text or "").split()).replace("|", "\\|")


def first_sentence(text):
    text = one_line(text)
    end = text.find(". ")
    return text if end < 0 else text[: end + 1]


def vocabulary_labels():
    """URI -> English skos:prefLabel, from the vocabulary files in ontologies/."""
    from rdflib import Graph
    from rdflib.namespace import SKOS

    labels = {}
    for path in VOCABULARIES:
        graph = Graph().parse(path, format="turtle")
        for subject, _, label in graph.triples((None, SKOS.prefLabel, None)):
            if getattr(label, "language", None) in (None, "en"):
                labels[str(subject)] = str(label)
    return labels


class References:
    def __init__(self, schema_yaml=SCHEMA_YAML):
        self.sv = SchemaView(str(schema_yaml))
        self.classes = self.sv.all_classes()
        self.enums = self.sv.all_enums()
        self.labels = vocabulary_labels()

    def is_concrete(self, name):
        cls = self.classes[name]
        return not cls.abstract and not cls.mixin and cls.class_uri != "linkml:Any"

    def concrete_classes(self):
        return sorted(name for name in self.classes if self.is_concrete(name))

    def group_of(self, name):
        ancestors = set(self.sv.class_ancestors(name, reflexive=True))
        for title, roots in GROUPS:
            if ancestors & set(roots):
                return title
        return OTHER_GROUP

    def index_page(self):
        lines = [INDEX_INTRO]
        by_group = {}
        for name in self.concrete_classes():
            by_group.setdefault(self.group_of(name), []).append(name)
        for title in [g for g, _ in GROUPS] + [OTHER_GROUP]:
            if title not in by_group:
                continue
            lines += [f"## {title}", "", "| Class | Parent | What it is |", "|---|---|---|"]
            for name in by_group[title]:
                cls = self.classes[name]
                lines.append(f"| {name} | {cls.is_a or ''} | {first_sentence(cls.description)} |")
            lines.append("")
        return "\n".join(lines).rstrip("\n") + "\n"

    def meaning(self, value, pv):
        return one_line(pv.description or pv.title or self.labels.get(value))

    def explained_enums(self):
        """Enums with a meaning for at least one value, from the schema or a fetched vocabulary."""
        return sorted(
            name
            for name, enum in self.enums.items()
            if any(self.meaning(value, pv) for value, pv in enum.permissible_values.items())
        )

    def vocabularies_page(self):
        lines = [VOCABULARY_INTRO]
        for name in self.explained_enums():
            enum = self.enums[name]
            lines += [f"## {name}", ""]
            if enum.description:
                lines += [one_line(enum.description), ""]
            rows = [(self.meaning(value, pv), value) for value, pv in enum.permissible_values.items()]
            if all(value.startswith("http") for _, value in rows):
                rows.sort()
            lines += [f"- `{value}`: {meaning}" if meaning else f"- `{value}`" for meaning, value in rows]
            lines.append("")
        return "\n".join(lines).rstrip("\n") + "\n"

    def write(self, out):
        refs = out / "references"
        refs.mkdir(parents=True, exist_ok=True)
        (refs / "class-index.md").write_text(self.index_page())
        (refs / "vocabularies.md").write_text(self.vocabularies_page())
        (out / "assets").mkdir(exist_ok=True)
        shutil.copyfile(JSON_SCHEMA, out / "assets" / JSON_SCHEMA.name)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--out", default=str(ROOT / "skills" / "oae-metadata"))
    args = parser.parse_args()
    References().write(Path(args.out))


if __name__ == "__main__":
    main()
