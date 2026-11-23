

# Slot: Standard used (standard_used)


_Type of standard used to calibrate the pH measurement._





URI: [oae:standard_used](https://schema.oaedata.org/standard_used)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DyeCalibration](DyeCalibration.md) | pH instrument calibration with an indicator dye standard |  yes  |
| [PHCalibration](PHCalibration.md) | pH instrument calibration |  no  |







## Properties

* Range: [PHCalibrationStandard](PHCalibrationStandard.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:standard_used |
| native | oae:standard_used |




## LinkML Source

<details>
```yaml
name: standard_used
description: Type of standard used to calibrate the pH measurement.
title: Standard used
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: standard_used
domain_of:
- PHCalibration
range: PHCalibrationStandard
required: true

```
</details>