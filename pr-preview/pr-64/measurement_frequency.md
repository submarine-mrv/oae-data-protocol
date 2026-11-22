

# Slot: Measurement frequency (measurement_frequency)


_How often measurements are taken, e.g., every 140 seconds except during calibration._





URI: [oae:measurement_frequency](https://schema.oaedata.org/measurement_frequency)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector for continuous measurements, with measurement frequency |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:measurement_frequency |
| native | oae:measurement_frequency |




## LinkML Source

<details>
```yaml
name: measurement_frequency
description: How often measurements are taken, e.g., every 140 seconds except during
  calibration.
title: Measurement frequency
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: measurement_frequency
owner: ContinuousCO2GasDetector
domain_of:
- ContinuousCO2GasDetector
range: string

```
</details>