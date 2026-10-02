# Datasets

A **Dataset** describes one or more related data files produced by an experiment, and the variables in them.

!!! note "What is a dataset?"
    A dataset typically corresponds to a single data file (e.g., one CSV of CTD profiles), but it may include multiple files when they share the same platform, instruments, and data submitter. The key organizing principle is that a dataset represents data collected on a **single platform** using a **consistent set of instruments**, managed by a **single data submitter**. If data come from different platforms or instrument configurations, they should be separate datasets.

## Dataset Types

- **[FieldDataset](../FieldDataset.md)**: data collected during in-situ experiments, such as CTD casts,
  bottle samples and sensor deployments. It records the platform that collected the data, using the
  [NERC L06](https://vocab.nerc.ac.uk/collection/L06/current/) platform types (see
  [Platform](../Platform.md)).
- **[ModelOutputDataset](../ModelOutputDataset.md)**: output from a model experiment. How the output
  was produced is described here, through the simulation type, period, output frequency and hardware.

## Rules

These apply on top of each field's own requirements:

- **Data access** (both dataset types): `open_access` is for data you can reach today and requires
  `data_access_link`. Use `scheduled_access` for anything not openly available yet; it requires
  `data_access_date`, the date the data will open. `data_access_link` is optional for scheduled and
  conditional access.
- **Perturbation runs** (model output): `simulation_type` can list several values. If it includes
  `perturbation`, describe the forcing in `mcdr_forcing_description`.

## Linking Datasets to Experiments

Each dataset names the experiment it belongs to with `experiment_id`, so one experiment can have several
datasets, such as CTD profiles, bottle samples and sensor time series.

## Variables

Each dataset lists its `variables`, metadata for each measurement or column in its files. Field
datasets use the field variable classes, with specific classes for pH, total alkalinity, DIC, CO₂ and
other common measurements. Model output datasets use [ModelOutputVariable](../ModelOutputVariable.md).
See [Variables](../Variables/index.md) for how to choose a class.
