

# Slot: Variables (variables)


_The variables in this dataset, each with its own metadata._





URI: [schema:variableMeasured](http://schema.org/variableMeasured)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  yes  |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  yes  |







## Properties

* Range: [Variable](Variable.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:variableMeasured |
| native | oae:variables |




## LinkML Source

<details>
```yaml
name: variables
description: The variables in this dataset, each with its own metadata.
title: Variables
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
slot_uri: schema:variableMeasured
alias: variables
domain_of:
- FieldDataset
- ModelOutputDataset
range: Variable
multivalued: true

```
</details>