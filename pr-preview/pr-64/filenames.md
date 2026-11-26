

# Slot: Filenames (filenames)



URI: [oae:filenames](https://schema.oaedata.org/filenames)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  yes  |
| [Dataset](Dataset.md) | Abstract base class for all dataset types |  no  |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:filenames |
| native | oae:filenames |




## LinkML Source

<details>
```yaml
name: filenames
title: Filenames
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: filenames
domain_of:
- Dataset
range: string
required: true
multivalued: true
minimum_cardinality: 1

```
</details>