

# Slot: Standard Gas Concentration (concentration)


_Concentrations of the CO2 standard gases that are used to calibrate the CO2 sensor, e.g., 260, 350, 510ppm._





URI: [oae:concentration](https://schema.oaedata.org/concentration)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StandardGas](StandardGas.md) | Standard gas used for CO2 calibration |  no  |
| [ContinuousStandardGas](ContinuousStandardGas.md) | Standard gas used for continuous CO2 calibration, with additional traceabilit... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:concentration |
| native | oae:concentration |




## LinkML Source

<details>
```yaml
name: concentration
description: Concentrations of the CO2 standard gases that are used to calibrate the
  CO2 sensor, e.g., 260, 350, 510ppm.
title: Standard Gas Concentration
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: concentration
owner: StandardGas
domain_of:
- StandardGas
range: string

```
</details>