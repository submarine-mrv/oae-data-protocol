

# Slot: CRM manufacturer (crm_manufacturer)


_Manufacturer of the Certified Reference Material (e.g., Scripps, JAMSTEC)._





URI: [oae:crm_manufacturer](https://schema.oaedata.org/crm_manufacturer)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRMCalibration](CRMCalibration.md) | Calibration using Certified Reference Materials, used for DIC and TA instrume... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:crm_manufacturer |
| native | oae:crm_manufacturer |




## LinkML Source

<details>
```yaml
name: crm_manufacturer
description: Manufacturer of the Certified Reference Material (e.g., Scripps, JAMSTEC).
title: CRM manufacturer
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: crm_manufacturer
owner: CRMCalibration
domain_of:
- CRMCalibration
range: string
required: true

```
</details>