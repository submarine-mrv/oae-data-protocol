

# Slot: Boundary Conditions (boundary_conditions)


_Boundary condition data source(s)._





URI: [oae:boundary_conditions](https://schema.oaedata.org/boundary_conditions)



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
| self | oae:boundary_conditions |
| native | oae:boundary_conditions |




## LinkML Source

<details>
```yaml
name: boundary_conditions
description: Boundary condition data source(s).
title: Boundary Conditions
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: boundary_conditions
owner: ModelInputDetails
domain_of:
- ModelInputDetails
range: NamedLink
multivalued: true
inlined: true
inlined_as_list: true

```
</details>