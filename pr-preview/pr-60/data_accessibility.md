

# Slot: Data Accessibility (data_accessibility)


_Level of access to this dataset. Open Access data are freely available now, without restriction. Conditional Access data are available upon request, subject to review. Scheduled Access data will become openly available after a specified date; choose it for any data that are not openly available yet._





URI: [oae:data_accessibility](https://schema.oaedata.org/data_accessibility)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |
| [Dataset](Dataset.md) | Abstract base class for all dataset types |  no  |







## Properties

* Range: [DataAccessibility](DataAccessibility.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:data_accessibility |
| native | oae:data_accessibility |




## LinkML Source

<details>
```yaml
name: data_accessibility
description: Level of access to this dataset. Open Access data are freely available
  now, without restriction. Conditional Access data are available upon request, subject
  to review. Scheduled Access data will become openly available after a specified
  date; choose it for any data that are not openly available yet.
title: Data Accessibility
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: data_accessibility
owner: Dataset
domain_of:
- Dataset
range: DataAccessibility
required: true

```
</details>