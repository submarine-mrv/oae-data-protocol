

# Slot: Dosing Location (dosing_location)


_Provide latitude and longitude in decimal degrees. Depending on your method of dispersal, this information may be provided as a point source, vector, or bounding box. If provided as a vector, the latitude and longitude values should be included in the dosing data file._





URI: [oae:dosing_location](https://schema.oaedata.org/dosing_location)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [DosingDetails](DosingDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |







## Properties

* Range: [DosingLocation](DosingLocation.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:dosing_location |
| native | oae:dosing_location |




## LinkML Source

<details>
```yaml
name: dosing_location
description: Provide latitude and longitude in decimal degrees. Depending on your
  method of dispersal, this information may be provided as a point source, vector,
  or bounding box. If provided as a vector, the latitude and longitude values should
  be included in the dosing data file.
title: Dosing Location
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: dosing_location
owner: DosingDetails
domain_of:
- DosingDetails
range: DosingLocation
required: true

```
</details>