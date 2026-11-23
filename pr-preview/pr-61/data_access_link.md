

# Slot: Data Access Link (data_access_link)


_URL to access this dataset, if it is already archived or published elsewhere. DOIs are preferred if available (e.g., https://doi.org/10.25921/xxxx-xxx). Required for open access, optional otherwise._





URI: [oae:data_access_link](https://schema.oaedata.org/data_access_link)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |
| [Dataset](Dataset.md) | Abstract base class for all dataset types |  no  |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |







## Properties

* Range: [uri](uri.md)

* Regex pattern: `^https?://.+`





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:data_access_link |
| native | oae:data_access_link |




## LinkML Source

<details>
```yaml
name: data_access_link
description: URL to access this dataset, if it is already archived or published elsewhere.
  DOIs are preferred if available (e.g., https://doi.org/10.25921/xxxx-xxx). Required
  for open access, optional otherwise.
title: Data Access Link
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: data_access_link
owner: Dataset
domain_of:
- Dataset
range: uri
pattern: ^https?://.+

```
</details>