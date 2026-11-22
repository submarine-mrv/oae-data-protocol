

# Slot: Data Submitter (data_submitter)


_Information about the individual submitting the dataset(s), including contact information_





URI: [oae:data_submitter](https://schema.oaedata.org/data_submitter)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Abstract base class for all dataset types |  no  |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |







## Properties

* Range: [Person](Person.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:data_submitter |
| native | oae:data_submitter |




## LinkML Source

<details>
```yaml
name: data_submitter
description: Information about the individual submitting the dataset(s), including
  contact information
title: Data Submitter
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: data_submitter
owner: Dataset
domain_of:
- Dataset
range: Person
required: true

```
</details>