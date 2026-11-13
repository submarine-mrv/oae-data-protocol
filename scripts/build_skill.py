"""Assemble the distributable oae-metadata skill.

    python scripts/build_skill.py --out DIR          the whole skill folder, plus oae-metadata.zip beside it
    python scripts/build_skill.py --vocabulary-page FILE

The repo holds only what is specific to drafting (skills/oae-metadata). The build adds what the
assistant should read from the same sources people do: the JSON Schema, the hand-written docs pages
on choosing classes, and a page of enum value meanings generated from the schema.
"""

import argparse
import re
import shutil
import zipfile
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "oae-metadata"
DOCS = ROOT / "src" / "docs" / "files"
SCHEMA_YAML = ROOT / "src" / "oae_data_protocol" / "schema" / "oae_data_protocol.yaml"
JSON_SCHEMA = ROOT / "project" / "jsonschema" / "oae_data_protocol.schema.json"
SITE = "https://schema.oaedata.org/"
# Vocabulary enums hold bare URIs; their labels come from the fetched vocabularies.
VOCABULARIES = [ROOT / "ontologies" / "sea_names.ttl", ROOT / "ontologies" / "platform_types.ttl"]

# Hand-written docs pages the skill reads, and the name each gets in references/docs/.
DOC_PAGES = {
    "metadata-format.md": "metadata-format.md",
    "projects-experiments/index.md": "projects-experiments.md",
    "Datasets/index.md": "datasets.md",
    "Variables/index.md": "variables.md",
    "instruments-calibration/index.md": "instruments-calibration.md",
}
VOCABULARY_PAGE = "vocabulary-values.md"

VOCABULARY_INTRO = """\
# Vocabulary Values

What each value means, for the vocabularies whose values need explaining, and the names behind the
sea-name and platform-type URIs. Generated from the schema and the NERC vocabularies. A vocabulary
that is not listed has self-explanatory values; see its own page.
"""


def one_line(text):
    return " ".join((text or "").split())


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


def vocabulary_page(schema_yaml=SCHEMA_YAML):
    """Markdown listing every enum that has a meaning for at least one value."""
    enums = SchemaView(str(schema_yaml)).all_enums()
    labels = vocabulary_labels()

    def meaning(value, pv):
        return one_line(pv.description or pv.title or labels.get(value))

    lines = [VOCABULARY_INTRO]
    for name in sorted(enums):
        rows = [(meaning(value, pv), value) for value, pv in enums[name].permissible_values.items()]
        if not any(text for text, _ in rows):
            continue
        lines += [f"## {name}", ""]
        if enums[name].description:
            lines += [one_line(enums[name].description), ""]
        if all(value.startswith("http") for _, value in rows):
            rows.sort()
        lines += [f"- `{value}`: {text}" if text else f"- `{value}`" for text, value in rows]
        lines.append("")
    return "\n".join(lines).rstrip("\n") + "\n"


def absolute_links(text, page):
    """Point a docs page's relative links at the published site, so they work outside it."""
    folder = Path(page).parent

    def fix(match):
        target = match.group(2)
        if re.match(r"[a-z]+:|#|/", target):
            return match.group(0)
        path, _, anchor = target.partition("#")
        parts = []
        for part in (folder / path).parts:
            if part == "..":
                parts = parts[:-1]
            elif part != ".":
                parts.append(part)
        return f"{match.group(1)}({SITE}{'/'.join(parts)}{'#' + anchor if anchor else ''})"

    return re.sub(r"(\]|\]:\s*)\(([^)\s]+)\)", fix, text)


def build(out):
    """Write the complete skill folder to `out`, replacing it, and oae-metadata.zip beside it."""
    out = Path(out)
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(SKILL, out, ignore=shutil.ignore_patterns("__pycache__"))
    (out / "assets").mkdir()
    shutil.copyfile(JSON_SCHEMA, out / "assets" / JSON_SCHEMA.name)
    docs = out / "references" / "docs"
    docs.mkdir(parents=True)
    for source, name in DOC_PAGES.items():
        (docs / name).write_text(absolute_links((DOCS / source).read_text(), source))
    (docs / VOCABULARY_PAGE).write_text(vocabulary_page())
    # The zip's top folder carries the skill's name whatever `out` is called; hosts require that.
    with zipfile.ZipFile(out.parent / f"{SKILL.name}.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(p for p in out.rglob("*") if p.is_file()):
            archive.write(path, f"{SKILL.name}/{path.relative_to(out).as_posix()}")
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--out", help="directory to write the assembled skill to")
    group.add_argument("--vocabulary-page", help="write only the vocabulary values page to this file")
    args = parser.parse_args()
    if args.out:
        build(args.out)
    else:
        Path(args.vocabulary_page).write_text(vocabulary_page())


if __name__ == "__main__":
    main()
