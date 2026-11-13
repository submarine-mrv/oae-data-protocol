

# Slot: Calibration technique description (technique_description)


_Details of the calibration technique used._





URI: [oae:technique_description](https://schema.oaedata.org/technique_description)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PHCalibration](PHCalibration.md) | pH instrument calibration |  no  |
| [CRMCalibration](CRMCalibration.md) | Calibration using Certified Reference Materials, used for DIC and TA instrume... |  no  |
| [Calibration](Calibration.md) | Base calibration information for instruments |  no  |
| [ContinuousCO2Calibration](ContinuousCO2Calibration.md) | CO2 calibration for continuous measurements, with extended standard gas detai... |  no  |
| [DiscreteCO2Calibration](DiscreteCO2Calibration.md) | CO2 calibration for discrete measurements, with calibration temperature |  no  |
| [CO2Calibration](CO2Calibration.md) | Base CO2 gas detector calibration with standard gas information |  no  |
| [DyeCalibration](DyeCalibration.md) | pH instrument calibration with an indicator dye standard |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:technique_description |
| native | oae:technique_description |




## LinkML Source

<details>
```yaml
name: technique_description
description: Details of the calibration technique used.
title: Calibration technique description
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: technique_description
owner: Calibration
domain_of:
- Calibration
range: string
required: true

```
</details>