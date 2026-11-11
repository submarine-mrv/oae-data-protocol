

# Slot: Data Conflicts and Unreported Data (data_conflicts_and_unreported_data)


_If data exist that are or have been used by the project but are not provided due to conflicts (e.g., geopolitical or other), data availability (e.g., a dataset is no longer available), it may be noted here._





URI: [oae:data_conflicts_and_unreported_data](https://schema.oaedata.org/data_conflicts_and_unreported_data)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc |  no  |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:data_conflicts_and_unreported_data |
| native | oae:data_conflicts_and_unreported_data |




## LinkML Source

<details>
```yaml
name: data_conflicts_and_unreported_data
description: If data exist that are or have been used by the project but are not provided
  due to conflicts (e.g., geopolitical or other), data availability (e.g., a dataset
  is no longer available), it may be noted here.
title: Data Conflicts and Unreported Data
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: data_conflicts_and_unreported_data
owner: InSituExperiment
domain_of:
- InSituExperiment
range: string

```
</details>