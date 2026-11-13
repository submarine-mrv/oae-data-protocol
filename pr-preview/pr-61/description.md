

# Slot: Description (description)


_A narrative description of the thing._





URI: [schema:description](http://schema.org/description)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [Model](Model.md) | A computational model experiment related to OAE |  no  |
| [PublicComment](PublicComment.md) | A public comment document associated with a consultation for this experiment |  yes  |
| [ExternalProject](ExternalProject.md) | A research project that is not directly managed by the OAE project, but whose... |  no  |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |
| [ModelComponent](ModelComponent.md) | A component of a model (e |  yes  |
| [Experiment](Experiment.md) | Abstract base class for all experiment types |  yes  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [VocabularyItemReference](VocabularyItemReference.md) |  |  no  |
| [Dataset](Dataset.md) | Abstract base class for all dataset types |  yes  |
| [InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [Project](Project.md) | A project conducting OAE field trials or modeling |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:description |
| native | oae:description |




## LinkML Source

<details>
```yaml
name: description
description: A narrative description of the thing.
title: Description
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
slot_uri: schema:description
alias: description
domain_of:
- Project
- ExternalProject
- Experiment
- PublicComment
- VocabularyItemReference
- Dataset
- ModelComponent
range: string

```
</details>