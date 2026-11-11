# Skills

`oae-metadata/` is a skill that lets an AI assistant draft an OAE metadata file from a researcher's
documents and data files. Researchers find it through the docs site
([Drafting Metadata with an AI Assistant](https://schema.oaedata.org/ai-skill/)). This page is for
maintainers. It replaces the architecture proposal that used to sit in the skill folder.

## What the skill does

The assistant writes a metadata JSON and a short report of gaps, uncertain values and conflicts
between sources. The researcher imports the JSON into the Metadata Builder, finishes it there and
exports the final file. The skill never fills a required field its sources don't support; missing
values go in the report.

It asks one thing the files can't answer: whether the project is new or already exists in the
Builder. Everything else is drafted first and reported after. An interview mode was considered and
left for later.

## Layout

```
oae-metadata/
  SKILL.md                    workflow                                   hand-written
  references/
    overview.md               choosing classes and ids                   hand-written
    builder-handoff.md        import modes, what the Builder drops       hand-written
    report-format.md          report template                            hand-written
    oap-xml-mapping.md        OAPMetadata (OCADS) XML to OAE fields      hand-written
    class-index.md            every concrete class                       generated
    vocabularies.md           what each enum value means, URI labels     generated
  scripts/validate.py         validator, Python standard library only    hand-written
  assets/oae_data_protocol.schema.json                                   generated copy
```

`just gen-all` regenerates the generated files (`scripts/gen_skill_references.py`), and CI fails if
the committed copies are stale. The skill reads field definitions straight from the bundled JSON
Schema. A version with one generated markdown file per class did no better in evals, so only what
the JSON Schema lacks is generated: a one-line index of classes, and the meanings of enum values. Change `builder-handoff.md` when the Metadata Builder's import or
parsing rules change; it was written from `applyImport.ts`, `parseEntity.ts` and
`conditionalFields.ts` in `oae-metadata-builder`.

## The validator

`scripts/validate.py` checks a draft against the published JSON Schema and reports structural errors
separately from gaps (required fields that are absent). It:

- validates each experiment, dataset, variable and pH calibration against the one class the Metadata
  Builder would pick, so errors name the right class
- applies the Builder's fix for the `simulation_type` rule (issue #25)
- checks bounding boxes the way the Builder does, and prints each one in words
- uses only the standard library, because many researchers' machines and most sandboxes have no
  `jsonschema` package

`tests/test_skill_validate.py` compares its verdicts with `jsonschema` and fails if the schema starts
using a keyword it doesn't implement.

## Publishing

The docs build (`scripts/mkdocs_hooks.py`) publishes the skill folder as plain files at
`https://schema.oaedata.org/skill/`, each docs page as markdown beside its HTML, and an index at
`https://schema.oaedata.org/llms.txt`. An assistant that can read web pages needs only the URL of
`SKILL.md`. Claude Code users can copy the folder into `~/.claude/skills/`.

`.claude-plugin/plugin.json` makes the repo loadable as a Claude Code plugin. A marketplace listing,
OpenAI packaging and a ZIP download are not set up.

## Evaluation

Eval cases use third-party project documents and curated reference metadata, so they are kept
outside this repo. The method:

- Each case gives the assistant real source files and compares its draft with an answer key built
  from what those files support: expected facts, and fields the files cannot supply.
- Each case runs with the skill and with only the JSON Schema, which is what a researcher can do
  without the skill.
- Scoring counts structural errors, values filled in fields the sources cannot supply, and expected
  facts found.

With only the schema, drafts validated but filled required fields with invented values (coordinates,
removal potentials, QC steps) in every run. With the skill, they did not.

## Not done yet

- Results on models other than Claude Sonnet, and on other assistants. [Inspect AI](https://inspect.aisi.org.uk/)
  with `inspect_swe` can run the same cases against Claude Code and Codex with Python scorers; move
  the evals there when that comparison is needed.
- NetCDF input.
- Updating part of an existing experiment or dataset. The Builder's import replaces an experiment
  whole and always adds datasets.
- An interview mode that resolves gaps with the researcher before the draft is written.
