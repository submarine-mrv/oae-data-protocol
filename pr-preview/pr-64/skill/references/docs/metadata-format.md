# Metadata File Format

OAE metadata is stored as **JSON**. Each metadata file is one **[Container](https://schema.oaedata.org/Container.md)**: a project,
its experiments and its datasets in a single document.

To create a file, use the **[OAE Metadata Builder](https://metadata.oaedata.org)**. It exports files
that validate against the schema. The [Excel templates](https://www.carbontosea.org/oae-data-protocol#metadata-and-templates)
on the protocol website are still available, but they won't be updated for future versions of the
protocol. The LinkML schema on [GitHub](https://github.com/submarine-mrv/oae-data-protocol) is now the
single source of truth for the protocol's metadata requirements.

## The Container

| Field | Contains |
|-------|----------|
| `project` | One [Project](https://schema.oaedata.org/Project.md) |
| `experiments` | The project's [experiments](https://schema.oaedata.org/projects-experiments/index.md#experiments) |
| `datasets` | The datasets those experiments produced, either [FieldDataset](https://schema.oaedata.org/FieldDataset.md) or [ModelOutputDataset](https://schema.oaedata.org/ModelOutputDataset.md) |
| `protocol_version`, `schema_version`, `metadata_builder_version` | See [Versioning](#versioning) |

### Versioning

A metadata file records three versions: which protocol the project follows, which schema the file
was validated against, and which tool wrote it.

- `protocol_version`: the version of the OAE Data Management Protocol the schema is based on, which
  protocol compliance is checked against
- `schema_version`: the version of the OAE Data Schema the file follows, such as `0.7.0`. It is
  numbered separately from `protocol_version` and changes more often; each version is a
  [release of the schema repository](https://github.com/submarine-mrv/oae-data-protocol/releases)
- `metadata_builder_version`: optional; the
  [Metadata Builder release](https://github.com/submarine-mrv/oae-metadata-builder/releases) that
  wrote the file

The protocol and the schema are versioned separately. Each protocol version is published on Zenodo
with its own DOI, and one protocol version can span many schema releases. The table shows which
schema versions are based on each protocol version.

| Protocol version | DOI | Schema versions |
|---|---|---|
| 1.0.0 | [10.5281/zenodo.17154989](https://doi.org/10.5281/zenodo.17154989) | 0.1.0 and later |

All versions of the protocol are at [10.5281/zenodo.17154988](https://doi.org/10.5281/zenodo.17154988).

## How the Pieces Relate

- The **project** describes the overall field trial or modeling effort: who, where, when and why.
- Each **experiment** is one activity within the project, such as baseline monitoring, an alkalinity
  intervention, a tracer study or a model simulation. It carries the project's `project_id`.
- Each **dataset** describes data files produced by one experiment, and names it with `experiment_id`.
- Each dataset lists its **[variables](https://schema.oaedata.org/Variables/index.md)**: metadata for each column or measurement
  in its files.

## Example

A minimal file that validates against the schema:

<!-- validate: Container -->
```json
{
  "protocol_version": "1.0.0",
  "schema_version": "0.7.0",
  "project": {
    "project_id": "EXAMPLE-001",
    "name": "North Atlantic OAE pilot",
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

Validate against the [JSON Schema](https://github.com/submarine-mrv/oae-data-protocol/blob/main/project/jsonschema/oae_data_protocol.schema.json),
for example with `ajv-cli`:

```bash
npx ajv-cli validate \
  -s oae_data_protocol.schema.json \
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
