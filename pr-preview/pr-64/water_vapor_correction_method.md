

# Slot: Water vapor correction method (water_vapor_correction_method)


_How the water vapor pressure inside the equilibrator was determined._





URI: [oae:water_vapor_correction_method](https://schema.oaedata.org/water_vapor_correction_method)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MeasuredCO2Fields](MeasuredCO2Fields.md) | Fields applied to all measured CO2 variable types (discrete and continuous) |  no  |
| [DiscreteCO2Variable](DiscreteCO2Variable.md) | CO2 discrete (bottle) measured variable (pCO2/fCO2) |  no  |
| [ContinuousCO2Variable](ContinuousCO2Variable.md) | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2) |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:water_vapor_correction_method |
| native | oae:water_vapor_correction_method |




## LinkML Source

<details>
```yaml
name: water_vapor_correction_method
description: How the water vapor pressure inside the equilibrator was determined.
title: Water vapor correction method
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: water_vapor_correction_method
owner: MeasuredCO2Fields
domain_of:
- MeasuredCO2Fields
range: string

```
</details>