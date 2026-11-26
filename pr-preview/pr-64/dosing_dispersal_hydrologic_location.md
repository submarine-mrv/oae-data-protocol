

# Slot: Dosing Dispersal Hydrologic Location (dosing_dispersal_hydrologic_location)


_Descriptive dosing location_





URI: [oae:dosing_dispersal_hydrologic_location](https://schema.oaedata.org/dosing_dispersal_hydrologic_location)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [DosingDetails](DosingDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |







## Properties

* Range: [HydrologicLocation](HydrologicLocation.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:dosing_dispersal_hydrologic_location |
| native | oae:dosing_dispersal_hydrologic_location |




## LinkML Source

<details>
```yaml
name: dosing_dispersal_hydrologic_location
description: Descriptive dosing location
title: Dosing Dispersal Hydrologic Location
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: dosing_dispersal_hydrologic_location
owner: DosingDetails
domain_of:
- DosingDetails
range: HydrologicLocation
required: true

```
</details>