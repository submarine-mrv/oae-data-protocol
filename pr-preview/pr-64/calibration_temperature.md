

# Slot: Calibration temperature (calibration_temperature)


_Temperature at which calibration was performed._





URI: [oae:calibration_temperature](https://schema.oaedata.org/calibration_temperature)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PHCalibration](PHCalibration.md) | pH instrument calibration |  no  |
| [DiscreteCO2Calibration](DiscreteCO2Calibration.md) | CO2 calibration for discrete measurements, with calibration temperature |  no  |
| [DyeCalibration](DyeCalibration.md) | pH instrument calibration with an indicator dye standard |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:calibration_temperature |
| native | oae:calibration_temperature |




## LinkML Source

<details>
```yaml
name: calibration_temperature
description: Temperature at which calibration was performed.
title: Calibration temperature
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: calibration_temperature
domain_of:
- PHCalibration
- DiscreteCO2Calibration
range: string

```
</details>