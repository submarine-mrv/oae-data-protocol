

# Slot: Initial Conditions (initial_conditions)


_Initial condition data source(s)._





URI: [oae:initial_conditions](https://schema.oaedata.org/initial_conditions)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelInputDetails](ModelInputDetails.md) | Details about input data sources used to drive the model |  no  |







## Properties

* Range: [NamedLink](NamedLink.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:initial_conditions |
| native | oae:initial_conditions |




## LinkML Source

<details>
```yaml
name: initial_conditions
description: Initial condition data source(s).
title: Initial Conditions
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: initial_conditions
owner: ModelInputDetails
domain_of:
- ModelInputDetails
range: NamedLink
multivalued: true
inlined: true
inlined_as_list: true

```
</details>