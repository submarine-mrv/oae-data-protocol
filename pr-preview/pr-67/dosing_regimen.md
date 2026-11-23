

# Slot: Dosing Regimen (dosing_regimen)


_A human readable summary description of the dosing regimen / frequency. Exact details must be provided in the corresponding dosing file with exact timestamps for dosing on/off schedule._





URI: [oae:dosing_regimen](https://schema.oaedata.org/dosing_regimen)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [DosingDetails](DosingDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |
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
| self | oae:dosing_regimen |
| native | oae:dosing_regimen |




## LinkML Source

<details>
```yaml
name: dosing_regimen
description: A human readable summary description of the dosing regimen / frequency.
  Exact details must be provided in the corresponding dosing file with exact timestamps
  for dosing on/off schedule.
title: Dosing Regimen
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: dosing_regimen
owner: DosingDetails
domain_of:
- DosingDetails
range: string
required: true

```
</details>