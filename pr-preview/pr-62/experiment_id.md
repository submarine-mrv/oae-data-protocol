

# Slot: Experiment ID (experiment_id)


_The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:_

_Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01_

_Letters, numbers, hyphens (`-`) and underscores (`_`) only, starting with a letter or number, up to 64 characters._





URI: [oae:experiment_id](https://schema.oaedata.org/experiment_id)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [Experiment](Experiment.md) | Abstract base class for all experiment types |  yes  |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [Model](Model.md) | A computational model experiment related to OAE |  no  |
| [Dataset](Dataset.md) | Abstract base class for all dataset types |  yes  |
| [InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:experiment_id |
| native | oae:experiment_id |




## LinkML Source

<details>
```yaml
name: experiment_id
description: 'The experiment to which the data belong. Any naming convention that
  produces a unique ID is usable. The recommended naming convention is:

  Project ID + Experiment type + Optional numerical indicator to differentiate between
  various experiments of the same type for a project. A two digit consecutive number
  beginning with 01

  Letters, numbers, hyphens (`-`) and underscores (`_`) only, starting with a letter
  or number, up to 64 characters.'
title: Experiment ID
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: experiment_id
domain_of:
- Experiment
- Dataset
range: string
pattern: ^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$

```
</details>