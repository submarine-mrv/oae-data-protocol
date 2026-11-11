"""Generate the oae-metadata skill's reference files from the LinkML schema.

    python scripts/gen_skill_references.py [--out skills/oae-metadata]

Writes references/classes/<Class>.md for every concrete class, references/enums/<Enum>.md for
large enums, references/class-index.md, and a copy of the JSON Schema in assets/.
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

# Enums longer than this get their own file; shorter ones are listed in the class file.
INLINE_ENUM_MAX = 30

# class-index.md groups, by the root class each class descends from.
GROUPS = [
    ("Project", ["Project", "Container"]),
    ("Experiments", ["Experiment"]),
    ("Datasets", ["Dataset"]),
    ("Variables", ["Variable"]),
    ("Instruments and calibrations", ["AnalyzingInstrument", "SamplingInstrument", "Calibration", "StandardGas"]),
]
OTHER_GROUP = "Supporting"


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

    def large_enums(self):
        return sorted(name for name, enum in self.enums.items() if len(enum.permissible_values) > INLINE_ENUM_MAX)

    def class_links(self, name):
        """A class range as links: itself if concrete, else its concrete descendants."""
        if self.is_concrete(name):
            return [f"[{name}]({name}.md)"]
        names = [d for d in self.sv.class_descendants(name, reflexive=False) if self.is_concrete(d)]
        return [f"[{d}]({d}.md)" for d in sorted(names)]

    def range_text(self, slot, class_name=None):
        if slot.designates_type:
            return f"always `{class_name}`"
        if slot.equals_string is not None:
            return f"always `{slot.equals_string}`"
        if slot.equals_string_in:
            allowed = [f"`{value}`" for value in slot.equals_string_in]
            return f"always {allowed[0]}" if len(allowed) == 1 else "one of: " + ", ".join(allowed)
        narrowed = slot.range in self.classes and self.classes[slot.range].class_uri != "linkml:Any"
        if slot.any_of and not narrowed:
            links = [link for expr in slot.any_of if expr.range in self.classes for link in self.class_links(expr.range)]
            return "one of " + ", ".join(links)
        if slot.range in self.classes:
            links = self.class_links(slot.range)
            return links[0] if len(links) == 1 else "one of " + ", ".join(links)
        if slot.range in self.enums:
            values = list(self.enums[slot.range].permissible_values)
            if len(values) > INLINE_ENUM_MAX:
                return f"enum [{slot.range}](../enums/{slot.range}.md)"
            return "enum: " + ", ".join(f"`{v}`" for v in values)
        return slot.range or "string"

    def rules(self, name):
        lines = []
        for ancestor in reversed(self.sv.class_ancestors(name, reflexive=True)):
            for rule in self.classes[ancestor].rules or []:
                lines.append(f"- When {self.conditions(rule.preconditions)}, {self.requirements(rule.postconditions)}.")
        return lines

    @staticmethod
    def conditions(expression):
        parts = []
        for slot, cond in expression.slot_conditions.items():
            if cond.equals_string is not None:
                parts.append(f"`{slot}` is `{cond.equals_string}`")
            elif cond.has_member is not None and cond.has_member.equals_string is not None:
                parts.append(f"`{slot}` contains `{cond.has_member.equals_string}`")
            else:
                raise ValueError(f"Unsupported rule precondition on {slot}; teach gen_skill_references.py to render it")
        return " and ".join(parts)

    @staticmethod
    def requirements(expression):
        parts = []
        for slot, cond in expression.slot_conditions.items():
            if cond.required:
                parts.append(f"`{slot}` is required")
            else:
                raise ValueError(f"Unsupported rule postcondition on {slot}; teach gen_skill_references.py to render it")
        return " and ".join(parts)

    def class_page(self, name):
        cls = self.classes[name]
        slots = self.sv.class_induced_slots(name)
        slots = [s for s in slots if s.required] + [s for s in slots if not s.required]
        lines = [f"# {name}", ""]
        if cls.description:
            lines += [one_line(cls.description), ""]
        if cls.is_a:
            lines += [f"Parent: {cls.is_a}", ""]
        lines += ["| Field | Required | Many | Type | Description |", "|---|---|---|---|---|"]
        for slot in slots:
            lines.append(
                f"| {slot.name} | {'yes' if slot.required else 'no'} | {'yes' if slot.multivalued else 'no'} "
                f"| {self.range_text(slot, name)} | {one_line(slot.description)} |"
            )
        rules = self.rules(name)
        if rules:
            lines += ["", "## Rules", ""] + rules
        vocabularies = self.vocabularies(slots)
        if vocabularies:
            lines += ["", "## Vocabularies", "", "What each value means, for the fields above."] + vocabularies
        return "\n".join(lines) + "\n"

    def vocabularies(self, slots):
        """Value meanings for the inlined enums these slots use, where the schema gives any."""
        lines, seen = [], set()
        for slot in slots:
            enum = self.enums.get(slot.range)
            if enum is None or slot.equals_string is not None or slot.range in seen:
                continue
            values = enum.permissible_values
            if len(values) > INLINE_ENUM_MAX or not any(pv.description for pv in values.values()):
                continue
            seen.add(slot.range)
            fields = ", ".join(s.name for s in slots if s.range == slot.range)
            lines += ["", f"### {fields}", ""]
            lines += [f"- `{value}`: {one_line(pv.description)}" if pv.description else f"- `{value}`" for value, pv in values.items()]
        return lines

    def enum_page(self, name):
        enum = self.enums[name]
        lines = [f"# {name}", ""]
        if enum.description:
            lines += [one_line(enum.description), ""]
        lines += ["| Value | Label |", "|---|---|"]
        rows = [(one_line(pv.title or pv.description or self.labels.get(value)), value) for value, pv in enum.permissible_values.items()]
        for label, value in sorted(rows):
            lines.append(f"| `{value}` | {label} |")
        return "\n".join(lines) + "\n"

    def group_of(self, name):
        ancestors = set(self.sv.class_ancestors(name, reflexive=True))
        for title, roots in GROUPS:
            if ancestors & set(roots):
                return title
        return OTHER_GROUP

    def index_page(self):
        lines = ["# Classes", "", "One file per class in `classes/`. Open only the ones you are drafting.", ""]
        by_group = {}
        for name in self.concrete_classes():
            by_group.setdefault(self.group_of(name), []).append(name)
        for title in [g for g, _ in GROUPS] + [OTHER_GROUP]:
            if title not in by_group:
                continue
            lines += [f"## {title}", "", "| Class | Parent | What it is |", "|---|---|---|"]
            for name in by_group[title]:
                cls = self.classes[name]
                lines.append(f"| [{name}](classes/{name}.md) | {cls.is_a or ''} | {first_sentence(cls.description)} |")
            lines.append("")
        return "\n".join(lines).rstrip("\n") + "\n"

    def write(self, out):
        refs = out / "references"
        for folder in (refs / "classes", refs / "enums"):
            if folder.exists():
                shutil.rmtree(folder)
            folder.mkdir(parents=True)
        for name in self.concrete_classes():
            (refs / "classes" / f"{name}.md").write_text(self.class_page(name))
        for name in self.large_enums():
            (refs / "enums" / f"{name}.md").write_text(self.enum_page(name))
        (refs / "class-index.md").write_text(self.index_page())
        (out / "assets").mkdir(exist_ok=True)
        shutil.copyfile(JSON_SCHEMA, out / "assets" / JSON_SCHEMA.name)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--out", default=str(ROOT / "skills" / "oae-metadata"))
    args = parser.parse_args()
    References().write(Path(args.out))


if __name__ == "__main__":
    main()
