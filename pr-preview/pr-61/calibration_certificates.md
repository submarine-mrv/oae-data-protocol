

# Slot: Calibration certificate information (calibration_certificates)


_Information about calibration certificates. Ideally, the certificate should be made available in a PDF file with filename listed here._





URI: [oae:calibration_certificates](https://schema.oaedata.org/calibration_certificates)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRMCalibration](CRMCalibration.md) | Calibration using Certified Reference Materials, used for DIC and TA instrume... |  no  |
| [CO2Calibration](CO2Calibration.md) | Base CO2 gas detector calibration with standard gas information |  no  |
| [ContinuousCO2Calibration](ContinuousCO2Calibration.md) | CO2 calibration for continuous measurements, with extended standard gas detai... |  no  |
| [Calibration](Calibration.md) | Base calibration information for instruments |  no  |
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
| self | oae:calibration_certificates |
| native | oae:calibration_certificates |




## LinkML Source

<details>
```yaml
name: calibration_certificates
description: Information about calibration certificates. Ideally, the certificate
  should be made available in a PDF file with filename listed here.
title: Calibration certificate information
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: calibration_certificates
owner: Calibration
domain_of:
- Calibration
range: string

```
</details>