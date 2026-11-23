

# Slot: Dataset Type (dataset_type)


_Selected controlled vocabularies for data types relevant to mCDR have been referenced from NASA's SeaBASS metadata system and are provided below, for additional data types of optical characteristics see the [SeaBASS controlled definitions list](https://seabass.gsfc.nasa.gov/wiki/metadataheaders#data_type). Additional data types have been included to meet the needs of mCDR field projects._





URI: [oae:dataset_type](https://schema.oaedata.org/dataset_type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |
| [Dataset](Dataset.md) | Abstract base class for all dataset types |  no  |







## Properties

* Range: [DatasetType](DatasetType.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:dataset_type |
| native | oae:dataset_type |




## LinkML Source

<details>
```yaml
name: dataset_type
description: Selected controlled vocabularies for data types relevant to mCDR have
  been referenced from NASA's SeaBASS metadata system and are provided below, for
  additional data types of optical characteristics see the [SeaBASS controlled definitions
  list](https://seabass.gsfc.nasa.gov/wiki/metadataheaders#data_type). Additional
  data types have been included to meet the needs of mCDR field projects.
title: Dataset Type
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: dataset_type
owner: Dataset
domain_of:
- Dataset
range: DatasetType
required: true

```
</details>