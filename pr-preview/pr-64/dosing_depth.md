

# Slot: Dosing Depth (dosing_depth)


_Depth in meters. If this is variable, please include the schedule of depth changes and depths, or as a vector in meters with the data._





URI: [oae:dosing_depth](https://schema.oaedata.org/dosing_depth)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [DosingDetails](DosingDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:dosing_depth |
| native | oae:dosing_depth |




## LinkML Source

<details>
```yaml
name: dosing_depth
description: Depth in meters. If this is variable, please include the schedule of
  depth changes and depths, or as a vector in meters with the data.
title: Dosing Depth
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: dosing_depth
owner: DosingDetails
domain_of:
- DosingDetails
range: string
required: true

```
</details>