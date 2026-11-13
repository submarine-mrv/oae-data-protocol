

# Slot: Experiment ID (experiment_id)


_The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:_

_Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01_





URI: [oae:experiment_id](https://schema.oaedata.org/experiment_id)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [Model](Model.md) | A computational model experiment related to OAE |  no  |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc |  no  |
| [Dataset](Dataset.md) | Abstract base class for all dataset types |  yes  |
| [Experiment](Experiment.md) | Abstract base class for all experiment types |  yes  |







## Properties

* Range: [String](String.md)





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
  beginning with 01'
title: Experiment ID
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: experiment_id
domain_of:
- Experiment
- Dataset
range: string

```
</details>