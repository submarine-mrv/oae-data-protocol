

# Slot: Bathymetry (bathymetry)


_Bathymetry data source(s)._





URI: [oae:bathymetry](https://schema.oaedata.org/bathymetry)



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
| self | oae:bathymetry |
| native | oae:bathymetry |




## LinkML Source

<details>
```yaml
name: bathymetry
description: Bathymetry data source(s).
title: Bathymetry
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: bathymetry
owner: ModelInputDetails
domain_of:
- ModelInputDetails
range: NamedLink
multivalued: true
inlined: true
inlined_as_list: true

```
</details>