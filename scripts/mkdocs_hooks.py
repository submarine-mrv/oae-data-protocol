"""MkDocs build hook: publish the docs for AI agents as well as people.

After the HTML build it adds, to the built site:

- every page's source markdown at the same path (`/FieldDataset.md` beside `/FieldDataset/`)
- the oae-metadata skill as plain files under `/skill/`
- `/llms.txt`, an index of both
"""

import shutil
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent / "skills" / "oae-metadata"

INTRO = """\
> Schema and documentation for Ocean Alkalinity Enhancement (OAE) metadata: projects, experiments,
> datasets and variables. Every page listed here is plain markdown.

## Drafting metadata

- [oae-metadata skill]({base}skill/SKILL.md): step-by-step instructions for drafting an OAE metadata
  file from project documents and data files. Its reference files and validator are in the same folder.
- [JSON Schema]({base}skill/assets/oae_data_protocol.schema.json): the schema a metadata file must follow.
- [Validator]({base}skill/scripts/validate.py): `python3 validate.py file.json`, standard library only.
"""


def nav_lines(items, base, depth=0):
    """Markdown list lines for a MkDocs nav: sections as headings, pages as links to their markdown."""
    lines = []
    for item in items:
        if isinstance(item, str):
            title, target = Path(item).parent.name or Path(item).stem, item
        else:
            (title, target), = item.items()
        if isinstance(target, list):
            lines += ["", f"## {title}", ""] if depth == 0 else []
            first = target[0] if target and isinstance(target[0], str) else None
            if first:
                lines.append(f"- [{title}]({base}{first})")
            lines += nav_lines(target[1:] if first else target, base, depth + 1)
        elif not target.startswith(("http://", "https://")):
            lines.append(f"- [{title}]({base}{target})")
    return lines


def on_post_build(config, **kwargs):
    docs, site = Path(config["docs_dir"]), Path(config["site_dir"])
    base = (config.get("site_url") or "").rstrip("/") + "/"

    for source in docs.rglob("*.md"):
        target = site / source.relative_to(docs)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)

    shutil.copytree(SKILL, site / "skill", dirs_exist_ok=True)

    lines = [f"# {config['site_name']}", "", INTRO.format(base=base).rstrip()]
    lines += ["", "## Documentation", ""] + nav_lines(config.get("nav") or [], base)
    (site / "llms.txt").write_text("\n".join(lines) + "\n")
