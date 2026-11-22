

# Slot: CRM batch number (crm_batch_number)


_Batch number of the Certified Reference Material._





URI: [oae:crm_batch_number](https://schema.oaedata.org/crm_batch_number)



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
| self | oae:crm_batch_number |
| native | oae:crm_batch_number |




## LinkML Source

<details>
```yaml
name: crm_batch_number
description: Batch number of the Certified Reference Material.
title: CRM batch number
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: crm_batch_number
owner: CRMCalibration
domain_of:
- CRMCalibration
range: string
required: true

```
</details>