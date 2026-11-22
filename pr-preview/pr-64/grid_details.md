

# Slot: Grid Details (grid_details)


_Details about the model grid(s). Use multiple entries for nested grid configurations._





URI: [oae:grid_details](https://schema.oaedata.org/grid_details)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Model](Model.md) | A computational model experiment related to OAE |  no  |







## Properties

* Range: [ModelGrid](ModelGrid.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:grid_details |
| native | oae:grid_details |




## LinkML Source

<details>
```yaml
name: grid_details
description: Details about the model grid(s). Use multiple entries for nested grid
  configurations.
title: Grid Details
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: grid_details
owner: Model
domain_of:
- Model
range: ModelGrid
multivalued: true
inlined: true
inlined_as_list: true

```
</details>