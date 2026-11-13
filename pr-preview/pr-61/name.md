

# Slot: Name (name)


_A human-readable name for the thing._





URI: [schema:name](http://schema.org/name)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Information about a researcher or investigator involved in the experiment |  no  |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |
| [ExternalProject](ExternalProject.md) | A research project that is not directly managed by the OAE project, but whose... |  no  |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |
| [ModelComponent](ModelComponent.md) | A component of a model (e |  no  |
| [MonetaryGrant](MonetaryGrant.md) |  |  yes  |
| [NamedLink](NamedLink.md) | A link to a resource with a name and URL |  no  |
| [Organization](Organization.md) |  |  yes  |
| [Platform](Platform.md) |  |  yes  |
| [Experiment](Experiment.md) | Abstract base class for all experiment types |  yes  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc |  no  |
| [Dataset](Dataset.md) | Abstract base class for all dataset types |  yes  |
| [Model](Model.md) | A computational model experiment related to OAE |  no  |
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
| self | schema:name |
| native | oae:name |




## LinkML Source

<details>
```yaml
name: name
description: A human-readable name for the thing.
title: Name
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
slot_uri: schema:name
alias: name
domain_of:
- Organization
- Project
- NamedLink
- ExternalProject
- MonetaryGrant
- Experiment
- Person
- Dataset
- Platform
- ModelComponent
range: string

```
</details>