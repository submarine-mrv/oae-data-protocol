

# Slot: Calibration location (calibration_location)


_Factory calibration, lab calibration, or field calibration._





URI: [oae:calibration_location](https://schema.oaedata.org/calibration_location)



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

* Range: [CalibrationLocation](CalibrationLocation.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:calibration_location |
| native | oae:calibration_location |




## LinkML Source

<details>
```yaml
name: calibration_location
description: Factory calibration, lab calibration, or field calibration.
title: Calibration location
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: calibration_location
domain_of:
- Calibration
range: CalibrationLocation

```
</details>