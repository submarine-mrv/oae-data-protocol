

# Slot: Vertical Coverage (vertical_coverage)


_Minimum and maximum depths of observation in meters._





URI: [oae:vertical_coverage](https://schema.oaedata.org/vertical_coverage)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc |  yes  |







## Properties

* Range: [VerticalExtent](VerticalExtent.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:vertical_coverage |
| native | oae:vertical_coverage |




## LinkML Source

<details>
```yaml
name: vertical_coverage
description: Minimum and maximum depths of observation in meters.
title: Vertical Coverage
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: vertical_coverage
domain_of:
- InSituExperiment
range: VerticalExtent

```
</details>