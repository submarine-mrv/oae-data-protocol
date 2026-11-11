# Choosing classes and ids

Read `class-index.md` beside this file for the full list. This page holds only the choices the class files can't make for you.

## Experiments

`experiment_types` selects the class. The Builder applies these rules in order:

| `experiment_types` contains | Class |
|---|---|
| `model` | Model |
| `intervention` and `tracer_study` | InterventionWithTracer |
| `intervention` | Intervention |
| `tracer_study` | Tracer |
| anything else (`baseline`, `control`, `other`) | InSituExperiment |

Use InterventionWithTracer only when the alkalinity and the tracer were dosed through the same mechanism and schedule. Otherwise draft two experiments.

An experiment is a campaign the project itself treats as one unit: a named trial, deployment, crediting period, cruise or model study. Use the project's own names and boundaries.

- Keep a named campaign as one experiment even when the feedstock lot, dose rate or schedule changed inside it. Describe the phases in its fields.
- Separate campaigns (different names, or separated in time with their own reporting) are separate experiments.
- A model the sources configure in some detail (code, grid, forcing) is a Model experiment, even when the sources give no dates for a specific run. List the missing run details as gaps.
- A planned or earlier campaign that the sources describe in detail is an experiment too. Say in its description that it is planned or historical.
- Laboratory studies, permit applications and monitoring programmes are not experiments.

## Datasets

`dataset_type` selects the class: `model_output` is ModelOutputDataset, every other value is FieldDataset. One dataset per data file, or per set of files with the same columns.

## Variables

Three facts choose a field variable's class: how the value came to be (`genesis`), how it was sampled (`sampling`), and what it is (`variable_type`).

| The column holds | Class |
|---|---|
| A value measured on a discrete sample (bottle, grab, core) | `Discrete<Type>Variable` for pH, TA, DIC, CO2, sediment, physiological; HPLCVariable for pigments by HPLC; otherwise DiscreteMeasuredVariable |
| A value from a sensor recording continuously or at bottle trip | `Continuous<Type>Variable` for the same types; otherwise ContinuousMeasuredVariable |
| A value computed from other variables (salinity from conductivity, a carbonate-system output) | CalculatedVariable |
| Context the project did not measure or compute (station id, cast number, time, position, a flag) that is still worth describing | NonMeasuredVariable |
| Survey or economic data | SocioeconomicVariable |
| Output of a model, in a ModelOutputDataset | ModelOutputVariable |

The typed classes exist because they carry type-specific instrument and calibration fields. Use the generic class only when no typed class fits. A typed variable's `analyzing_instrument` must be the class its file names; a generic variable takes the base AnalyzingInstrument.

## Ids

- `project_id` and `experiment_id` are free text. If the sources give none, coin one from the names in the sources, following the convention in the field's description, and list it in the report as coined.
- A dataset's `experiment_id` must equal the `experiment_id` of the experiment it belongs to, character for character.
- Every experiment and dataset carries the same `project_id` as the project.

## File shape

```json
{
  "version": "<schema version>",
  "project": { "project_id": "...", "name": "..." },
  "experiments": [ { "experiment_id": "...", "project_id": "...", "experiment_types": ["intervention"] } ],
  "datasets": [
    {
      "name": "...",
      "project_id": "...",
      "experiment_id": "...",
      "dataset_type": "bottle",
      "variables": [ { "schema_class": "DiscreteTAVariable", "dataset_variable_name": "TA" } ]
    }
  ]
}
```

Variables go inside their dataset. Nothing else goes at the top level.
