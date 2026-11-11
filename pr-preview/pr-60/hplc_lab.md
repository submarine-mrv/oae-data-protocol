

# Slot: HPLC Lab (hplc_lab)


_The name of the lab where the HPLC analysis was run (e.g., 'NASA_GSFC'_





URI: [oae:hplc_lab](https://schema.oaedata.org/hplc_lab)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HPLCVariable](HPLCVariable.md) | HPLC (High-Performance Liquid Chromatography) measured variable for pigment a... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:hplc_lab |
| native | oae:hplc_lab |




## LinkML Source

<details>
```yaml
name: hplc_lab
description: The name of the lab where the HPLC analysis was run (e.g., 'NASA_GSFC'
title: HPLC Lab
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: hplc_lab
owner: HPLCVariable
domain_of:
- HPLCVariable
range: string
required: true

```
</details>