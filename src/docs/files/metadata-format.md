# Metadata File Format

OAE metadata is stored as **JSON**. Each metadata file is one **[Container](Container.md)**: a project,
its experiments and its datasets in a single document.

To create a file, use the **[OAE Metadata Builder](https://metadata.oaedata.org)**. It exports files
that validate against the schema. The [Excel templates](https://www.carbontosea.org/oae-data-protocol#metadata-and-templates)
on the protocol website are still available, but they aren't checked against the schema, so you have
to get vocabulary values and field formats right by hand.

## The Container

A Container is the top-level object in every metadata file. It wraps project metadata, experiment metadata, and dataset metadata into a single document:

```json
{
  "@context": "https://schema.oaedata.org/context.jsonld",
  "version": "0.5.0",
  "protocol_git_hash": "abc123...",
  "project": { ... },
  "experiments": [ ... ],
  "datasets": [ ... ]
}
```

| Field | Description |
|-------|-------------|
| `@context` | JSON-LD context URL — makes the file interpretable as linked data |
| `version` | Protocol schema version |
| `protocol_git_hash` | Git hash of the schema used to generate this file |
| `project` | A single [Project](Project.md) object |
| `experiments` | Array of [Experiment](Experiment.md) objects |
| `datasets` | Array of [Dataset](FieldDataset.md) objects |

!!! tip "Linked Data"
    The `@context` field is optional but recommended. It makes OAE metadata files valid [JSON-LD](https://json-ld.org/) documents, meaning they can be interpreted by linked data tools and semantic web infrastructure without any conversion. Standard JSON tools ignore the `@context` field, so it doesn't affect non JSON-LD workflows.

## How the Pieces Relate

- The **project** describes the overall field trial or modeling effort: who, where, when and why.
- Each **experiment** is one activity within the project, such as baseline monitoring, an alkalinity
  intervention, a tracer study or a model simulation. It carries the project's `project_id`.
- Each **dataset** describes data files produced by one experiment, and names it with `experiment_id`.
- Each dataset lists its **[variables](Variables/index.md)**: metadata for each column or measurement
  in its files.

## Example

A minimal file that validates against the schema:

<!-- validate: Container -->
```json
{
  "@context": "https://schema.oaedata.org/context.jsonld",
  "version": "0.5.0",
  "protocol_git_hash": "50d3904c...",
  "project": {
    "project_id": "EXAMPLE-001",
    "research_project": "North Atlantic OAE pilot",
    "description": "A pilot OAE field trial in the North Atlantic",
    "mcdr_pathway": "ocean_alkalinity_enhancement",
    "sea_names": ["http://vocab.nerc.ac.uk/collection/C16/current/23/"],
    "spatial_coverage": { "geo": { "box": "40.0 -70.0 45.0 -65.0" } },
    "temporal_coverage": "2025-01-01/2025-12-31",
    "project_leads": [{ "name": "Ada Lovelace", "email": "ada@example.org" }]
  },
  "experiments": [
    {
      "project_id": "EXAMPLE-001",
      "experiment_id": "EXAMPLE-001-BASELINE",
      "name": "Baseline monitoring",
      "experiment_types": ["baseline"],
      "description": "Baseline water chemistry before the intervention",
      "spatial_coverage": { "geo": { "box": "40.0 -70.0 45.0 -65.0" } },
      "start_datetime": "2025-01-01T00:00:00Z",
      "end_datetime": "2025-06-30T23:59:59Z",
      "experiment_leads": [{ "name": "Ada Lovelace", "email": "ada@example.org" }]
    }
  ],
  "datasets": [
    {
      "project_id": "EXAMPLE-001",
      "experiment_id": "EXAMPLE-001-BASELINE",
      "name": "Baseline CTD profiles",
      "description": "CTD casts from baseline monitoring",
      "dataset_type": "cast",
      "data_product_type": "originally_collected_dataset",
      "temporal_coverage": "2025-01-15/2025-06-15",
      "filenames": ["baseline_ctd_profiles.csv"],
      "platform_info": { "platform_type": "http://vocab.nerc.ac.uk/collection/L06/current/31/" },
      "data_submitter": { "name": "Ada Lovelace", "email": "ada@example.org" },
      "data_accessibility": "open_access",
      "data_access_link": "https://doi.org/10.25921/example",
      "variables": [
        {
          "schema_class": "NonMeasuredVariable",
          "variable_type": "non_measured",
          "dataset_variable_name": "station",
          "long_name": "Station ID"
        }
      ]
    }
  ]
}
```

## Validating a File

Validate against the [validation JSON Schema](https://github.com/submarine-mrv/oae-data-protocol/blob/main/project/jsonschema/oae_data_protocol.validation.schema.json),
for example with `ajv-cli`:

```bash
npx ajv-cli validate \
  -s oae_data_protocol.validation.schema.json \
  -d your-metadata.json \
  --spec=draft2019 --strict=false
```

## JSON-LD

The schema publishes a [JSON-LD context](https://schema.oaedata.org/context.jsonld). Adding it to a
metadata file lets linked data tools read the file as JSON-LD: field names resolve to URIs in the
`https://schema.oaedata.org/` namespace, and vocabulary references (NERC, QUDT) resolve to their
canonical URIs.

```json
{
  "@context": "https://schema.oaedata.org/context.jsonld",
  "project": { ... }
}
```

The JSON Schema describes the plain JSON form and doesn't allow `@context`, so remove it before
validating.
