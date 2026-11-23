

# Slot: Detector Type (detector_type)


_Type of the CO2 gas detector (E.g., Infrared)_





URI: [oae:detector_type](https://schema.oaedata.org/detector_type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CO2GasDetector](CO2GasDetector.md) | CO2 gas detector with standard gas calibration |  no  |
| [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector for continuous measurements, with measurement frequency |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:detector_type |
| native | oae:detector_type |




## LinkML Source

<details>
```yaml
name: detector_type
description: Type of the CO2 gas detector (E.g., Infrared)
title: Detector Type
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: detector_type
owner: CO2GasDetector
domain_of:
- CO2GasDetector
range: string
required: true

```
</details>