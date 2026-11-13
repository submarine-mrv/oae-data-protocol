

# Slot: Location of seawater intake (seawater_intake_location)


_Whereabouts of the seawater intake._





URI: [oae:seawater_intake_location](https://schema.oaedata.org/seawater_intake_location)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContinuousCO2Variable](ContinuousCO2Variable.md) | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2) |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:seawater_intake_location |
| native | oae:seawater_intake_location |




## LinkML Source

<details>
```yaml
name: seawater_intake_location
description: Whereabouts of the seawater intake.
title: Location of seawater intake
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: seawater_intake_location
owner: ContinuousCO2Variable
domain_of:
- ContinuousCO2Variable
range: string
required: true

```
</details>