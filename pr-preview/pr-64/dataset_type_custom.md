

# Slot: Dataset Type (Custom) (dataset_type_custom)


_Custom "data type" when an appropriate value is not found in the controlled vocabulary list for mCDR Data Type and the corresponding `data_type` field is set to "other"._





URI: [oae:dataset_type_custom](https://schema.oaedata.org/dataset_type_custom)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Abstract base class for all dataset types |  no  |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:dataset_type_custom |
| native | oae:dataset_type_custom |




## LinkML Source

<details>
```yaml
name: dataset_type_custom
description: Custom "data type" when an appropriate value is not found in the controlled
  vocabulary list for mCDR Data Type and the corresponding `data_type` field is set
  to "other".
title: Dataset Type (Custom)
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: dataset_type_custom
owner: Dataset
domain_of:
- Dataset
range: string

```
</details>