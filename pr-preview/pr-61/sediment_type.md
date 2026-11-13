

# Slot: Sediment Type (sediment_type)


_e.g., mud, sand, etc._





URI: [oae:sediment_type](https://schema.oaedata.org/sediment_type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MeasuredSedimentFields](MeasuredSedimentFields.md) | Fields applied to all measured sediment variable types (discrete and continuo... |  no  |
| [DiscreteSedimentVariable](DiscreteSedimentVariable.md) | Measured sediment variable collected from discrete bottle samples |  no  |
| [ContinuousSedimentVariable](ContinuousSedimentVariable.md) | Measured sediment variable collected from continuous autonomous sensor |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:sediment_type |
| native | oae:sediment_type |




## LinkML Source

<details>
```yaml
name: sediment_type
description: e.g., mud, sand, etc.
title: Sediment Type
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: sediment_type
owner: MeasuredSedimentFields
domain_of:
- MeasuredSedimentFields
range: string
required: true

```
</details>