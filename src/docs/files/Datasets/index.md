# Datasets

A **Dataset** describes one or more related data files submitted as part of an experiment. Each dataset is linked to exactly one experiment via `experiment_id` and contains metadata about the data files, the platform used to collect the data, and detailed variable-level metadata.

!!! note "What is a dataset?"
    A dataset typically corresponds to a single data file (e.g., one CSV of CTD profiles), but it may include multiple files when they share the same platform, instruments, and data submitter. The key organizing principle is that a dataset represents data collected on a **single platform** using a **consistent set of instruments**, managed by a **single data submitter**. If data come from different platforms or instrument configurations, they should be separate datasets.

## Dataset Types

There are two kinds of datasets:

### Field Dataset

For data collected during in-situ experiments — CTD casts, bottle samples, sensor deployments, etc.

**Key fields:**

| Field | Purpose |
|-------|---------|
| `dataset_type` | Classification (cast, bottle, flow-through, underway, mooring, etc.) |
| `data_product_type` | Raw sensor data, data compilation, etc. |
| `data_accessibility` | Access level: `open_access`, `conditional_access`, or `scheduled_access` |
| `platform_info` | Ship, buoy, or vehicle that collected the data |
| `filenames` | Names of the data file(s) in this dataset |
| `variables` | Array of variable metadata (see [Variables](../variables/)) |
| `data_submitter` | Person responsible for this submission |

→ [Full FieldDataset schema reference](../FieldDataset.md)

### Model Output Dataset

For simulation output from computational models.

**Key fields:**

| Field | Purpose |
|-------|---------|
| `simulation_type` | Control run or perturbation |
| `mcdr_forcing_description` | Description of the mCDR forcing applied |
| `variables` | Array of model output variable metadata (see [Variables](../variables/)) |
| `output_frequency` | Temporal resolution (e.g., daily, monthly) |
| `hardware_configuration` | Compute details |

→ [Full ModelOutputDataset schema reference](../ModelOutputDataset.md)

## Platform Information

Every field dataset includes platform metadata — the ship, buoy, autonomous vehicle, or other platform used for data collection.

```json
{
  "platform_info": {
    "name": "R/V Wecoma",
    "platform_type": "http://vocab.nerc.ac.uk/collection/L06/current/31/",
    "platform_id": "SHIP-001",
    "owner": "Oregon State University",
    "country": "US"
  }
}
```

Platform types use the [NERC L06 vocabulary](https://vocab.nerc.ac.uk/collection/L06/current/) for standardized classification.

## Linking Datasets to Experiments

Every dataset has an `experiment_id` field that links it to the experiment it belongs to. This allows multiple datasets (e.g., CTD profiles, bottle samples, sensor time series) to be associated with the same experiment.

```json
{
  "experiment_id": "EXAMPLE-001-BASELINE",
  "name": "Baseline CTD profiles",
  "filenames": ["baseline_ctd_casts.csv"]
}
```

## Variables

Each dataset contains an array of `variables` — detailed metadata describing each measurement or data column across the dataset's files. Variables are the most richly typed part of the schema, with specific subclasses for pH, total alkalinity, DIC, CO₂, and other common oceanographic measurements.

See [Variables](../variables/) for the complete variable hierarchy and type selection guide.
