

# Slot: Data Access Date (data_access_date)


_The date by when this dataset will be openly available on a public repository. Only used when data_accessibility is scheduled_access; leave empty otherwise._





URI: [oae:data_access_date](https://schema.oaedata.org/data_access_date)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Abstract base class for all dataset types |  no  |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |







## Properties

* Range: [Date](Date.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:data_access_date |
| native | oae:data_access_date |




## LinkML Source

<details>
```yaml
name: data_access_date
description: The date by when this dataset will be openly available on a public repository.
  Only used when data_accessibility is scheduled_access; leave empty otherwise.
title: Data Access Date
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: data_access_date
owner: Dataset
domain_of:
- Dataset
range: date

```
</details>