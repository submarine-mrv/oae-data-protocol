

# Slot: Frequency of calibration (frequency)


_How often the instrument was calibrated._





URI: [oae:frequency](https://schema.oaedata.org/frequency)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DyeCalibration](DyeCalibration.md) | pH instrument calibration with an indicator dye standard |  no  |
| [CO2Calibration](CO2Calibration.md) | Base CO2 gas detector calibration with standard gas information |  no  |
| [CRMCalibration](CRMCalibration.md) | Calibration using Certified Reference Materials, used for DIC and TA instrume... |  no  |
| [Calibration](Calibration.md) | Base calibration information for instruments |  no  |
| [PHCalibration](PHCalibration.md) | pH instrument calibration |  no  |
| [ContinuousCO2Calibration](ContinuousCO2Calibration.md) | CO2 calibration for continuous measurements, with extended standard gas detai... |  no  |
| [DiscreteCO2Calibration](DiscreteCO2Calibration.md) | CO2 calibration for discrete measurements, with calibration temperature |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:frequency |
| native | oae:frequency |




## LinkML Source

<details>
```yaml
name: frequency
description: How often the instrument was calibrated.
title: Frequency of calibration
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: frequency
owner: Calibration
domain_of:
- Calibration
range: string

```
</details>