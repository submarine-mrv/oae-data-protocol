# Drafting Metadata with an AI Assistant

The `oae-metadata` skill lets an AI assistant draft a [metadata file](metadata-format.md) from your
project documents and data files. You then import the draft into the
[Metadata Builder](metadata-builder.md), check it, fill what is missing and export the final file.

The assistant produces two files:

- a metadata JSON holding whichever of project, experiments and datasets your files support
- a short report listing required fields it could not find, values it was unsure of, and places
  where your sources disagree

It does not fill a required field it cannot find. Those are listed in the report for you to complete
in the Builder.

## What to give it

- Project design documents, monitoring or operations reports, methods descriptions (PDF or text)
- Data files (CSV or XLSX): one dataset per file, one variable per data column
- OAPMetadata XML, if you have submitted to OCADS

Say whether the project is new or already exists in the Metadata Builder. For an existing project,
give its project ID and, for each dataset, the ID of the experiment it belongs to.

## Using it

### Any assistant that can read web pages

Attach your files and ask:

> Follow the instructions at https://schema.oaedata.org/skill/SKILL.md to draft OAE metadata from
> these files. The other files it mentions are in the same folder.

### Claude Code

Download [oae-metadata.zip](https://schema.oaedata.org/oae-metadata.zip) and unzip it into
`~/.claude/skills/`, then ask Claude to draft OAE metadata from your files.

### Claude in the browser or desktop app

Upload the same zip under Customize → Skills.

Every page of this site is also published as markdown for assistants: add `.md` to a page's address
(for example [`/FieldDataset.md`](https://schema.oaedata.org/FieldDataset.md)), or start from
[`/llms.txt`](https://schema.oaedata.org/llms.txt).

## Checking the draft

The skill includes a validator that needs only Python 3:

```bash
curl -O https://schema.oaedata.org/skill/scripts/validate.py
curl -O https://schema.oaedata.org/skill/assets/oae_data_protocol.schema.json
python3 validate.py your-metadata.json --schema oae_data_protocol.schema.json
```

It reports structural errors (an unknown field, a value outside its vocabulary) separately from
gaps (a required field that is absent), and prints each bounding box in words so a swapped latitude
and longitude is easy to spot. An assistant that can run code will run it for you. One that cannot
will say so in the report, and the Builder will show the same errors after import.

## Limits

- The draft is a starting point. Review every value against its source before you publish.
- Maps and figures are not read. Locations shown only on a map are reported as missing.
- Importing a dataset twice creates two datasets. Delete the old one in the Builder first.
- NetCDF files are not supported yet.
