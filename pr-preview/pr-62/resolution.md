

# Slot: Resolution (resolution)


_Resolution of the CO2 sensor._





URI: [oae:resolution](https://schema.oaedata.org/resolution)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CO2GasDetector](CO2GasDetector.md) | CO2 gas detector with standard gas calibration |  no  |
| [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector for continuous measurements, with measurement frequency |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:resolution |
| native | oae:resolution |




## LinkML Source

<details>
```yaml
name: resolution
description: Resolution of the CO2 sensor.
title: Resolution
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: resolution
owner: CO2GasDetector
domain_of:
- CO2GasDetector
range: string

```
</details>