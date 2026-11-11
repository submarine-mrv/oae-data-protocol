

# Slot: mCDR Experiment Type(s) (experiment_types)


_The type(s) of mCDR experiment conducted. See Controlled Vocabularies section for definitions._





URI: [oae:experiment_types](https://schema.oaedata.org/experiment_types)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc |  no  |
| [Experiment](Experiment.md) | Abstract base class for all experiment types |  no  |
| [Model](Model.md) | A computational model experiment related to OAE |  no  |







## Properties

* Range: [ExperimentType](ExperimentType.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:experiment_types |
| native | oae:experiment_types |




## LinkML Source

<details>
```yaml
name: experiment_types
description: The type(s) of mCDR experiment conducted. See Controlled Vocabularies
  section for definitions.
title: mCDR Experiment Type(s)
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: experiment_types
owner: Experiment
domain_of:
- Experiment
range: ExperimentType
required: true
multivalued: true

```
</details>