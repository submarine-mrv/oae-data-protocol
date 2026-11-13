# The report

Write the report as markdown beside the JSON. A researcher reads it with the Builder open, so order it by what they have to do. Keep it short: one line per item, no prose padding.

```markdown
# Metadata draft report: <project or dataset name>

Drafted <date> against OAE Data Protocol <version>.
<the update notice, if `--check-update` printed one>

## What was drafted
- Project: yes | no (existing project <project_id>)
- Experiments: <n> (<experiment_id>: <class>, ...)
- Datasets: <n> (<name>: <n> variables)

## Validation
<one of>
- Validated: no structural errors. <n> required fields are missing (listed under Gaps).
- Not clean: <n> structural errors remain after three rounds (listed below).
- Not run: <why>. The Builder will show errors after import.

## Gaps
Required fields with no supporting source. Grouped where the same field is missing on many items.
- `<item>.<field>`: <what is missing, and where you looked>

## Uncertain values
Values you filled from an inference or a partial statement.
- `<item>.<field>` = <value>: <why uncertain> (<source file>, <section, page, column or element>)

## Conflicts between sources
- `<item>.<field>`: <source A says X> / <source B says Y>. Draft uses <X or nothing>.

## Not used
Source content that fits no field, and columns with no variable.

## Sources
| File | Used for |
|---|---|
(for an OAPMetadata XML file, add its version, e.g. `a0.2.2`)

## Next steps
<the import steps from builder-handoff.md, adapted to new or existing project>
```

Rules:

- Every gap the validator lists goes under Gaps. Do not fill a gap to make the list shorter.
- A value belongs under Uncertain when a careful colleague would want to check it: a class you chose between two candidates, a date with no time, a unit you converted, an identifier you coined.
- Say where each uncertain or conflicting value came from, precisely enough to find it again.
- Leave a section out when it would be empty, except Validation.
