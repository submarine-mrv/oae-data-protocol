

# Slot: Spatial Coverage (spatial_coverage)


_Latitude/longitude bounds of project site (e.g., boundary domain of observations or relevant activities), expressed as a schema.org GeoShape bounding box._





URI: [schema:spatialCoverage](http://schema.org/spatialCoverage)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [ExternalProject](ExternalProject.md) | A research project that is not directly managed by the OAE project, but whose... |  no  |
| [ModelGrid](ModelGrid.md) | Details about a model grid |  no  |
| [Experiment](Experiment.md) | Abstract base class for all experiment types |  yes  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc |  no  |
| [Model](Model.md) | A computational model experiment related to OAE |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [Project](Project.md) | A project conducting OAE field trials or modeling |  yes  |







## Properties

* Range: [SpatialCoverage](SpatialCoverage.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:spatialCoverage |
| native | oae:spatial_coverage |




## LinkML Source

<details>
```yaml
name: spatial_coverage
description: Latitude/longitude bounds of project site (e.g., boundary domain of observations
  or relevant activities), expressed as a schema.org GeoShape bounding box.
title: Spatial Coverage
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
slot_uri: schema:spatialCoverage
alias: spatial_coverage
domain_of:
- Project
- ExternalProject
- Experiment
- ModelGrid
range: SpatialCoverage
required: true

```
</details>