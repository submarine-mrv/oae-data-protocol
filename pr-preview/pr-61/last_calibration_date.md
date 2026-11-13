

# Slot: Last calibration date (UTC) (last_calibration_date)


_Date and time of most recent calibration in UTC._





URI: [oae:last_calibration_date](https://schema.oaedata.org/last_calibration_date)



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

* Range: [Datetime](Datetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:last_calibration_date |
| native | oae:last_calibration_date |




## LinkML Source

<details>
```yaml
name: last_calibration_date
description: Date and time of most recent calibration in UTC.
title: Last calibration date (UTC)
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: last_calibration_date
owner: Calibration
domain_of:
- Calibration
range: datetime

```
</details>