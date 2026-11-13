

# Slot: Calibration Files (required if providing sensor data) (calibration_files)


_A list of supplementary file names containing coefficients and techniques used to calibrate the instruments used in data collection. The named files can be found within the relevant documents folder accompanying the submitted data files._





URI: [oae:calibration_files](https://schema.oaedata.org/calibration_files)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:calibration_files |
| native | oae:calibration_files |




## LinkML Source

<details>
```yaml
name: calibration_files
description: A list of supplementary file names containing coefficients and techniques
  used to calibrate the instruments used in data collection. The named files can be
  found within the relevant documents folder accompanying the submitted data files.
title: Calibration Files (required if providing sensor data)
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: calibration_files
owner: FieldDataset
domain_of:
- FieldDataset
range: string
multivalued: true

```
</details>