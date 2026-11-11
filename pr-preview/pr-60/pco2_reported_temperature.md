

# Slot: Temperature at which pCO2 was reported (pco2_reported_temperature)


_In Celsius. The input could be a constant temperature value, or something like, in-situ temperature, temperature of analysis, etc._





URI: [oae:pco2_reported_temperature](https://schema.oaedata.org/pco2_reported_temperature)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MeasuredCO2Fields](MeasuredCO2Fields.md) | Fields applied to all measured CO2 variable types (discrete and continuous) |  no  |
| [ContinuousCO2Variable](ContinuousCO2Variable.md) | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2) |  no  |
| [DiscreteCO2Variable](DiscreteCO2Variable.md) | CO2 discrete (bottle) measured variable (pCO2/fCO2) |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:pco2_reported_temperature |
| native | oae:pco2_reported_temperature |




## LinkML Source

<details>
```yaml
name: pco2_reported_temperature
description: In Celsius. The input could be a constant temperature value, or something
  like, in-situ temperature, temperature of analysis, etc.
title: Temperature at which pCO2 was reported
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: pco2_reported_temperature
owner: MeasuredCO2Fields
domain_of:
- MeasuredCO2Fields
range: string
required: true

```
</details>