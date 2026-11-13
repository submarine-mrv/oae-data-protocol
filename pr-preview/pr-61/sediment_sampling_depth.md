

# Slot: Sediment Sampling Depth (sediment_sampling_depth)


_Depth that sediment was collected below sediment surface. If provided as a variable (recommended), please list the column header name here._





URI: [oae:sediment_sampling_depth](https://schema.oaedata.org/sediment_sampling_depth)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContinuousSedimentVariable](ContinuousSedimentVariable.md) | Measured sediment variable collected from continuous autonomous sensor |  no  |
| [DiscreteSedimentVariable](DiscreteSedimentVariable.md) | Measured sediment variable collected from discrete bottle samples |  no  |
| [MeasuredSedimentFields](MeasuredSedimentFields.md) | Fields applied to all measured sediment variable types (discrete and continuo... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:sediment_sampling_depth |
| native | oae:sediment_sampling_depth |




## LinkML Source

<details>
```yaml
name: sediment_sampling_depth
description: Depth that sediment was collected below sediment surface. If provided
  as a variable (recommended), please list the column header name here.
title: Sediment Sampling Depth
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: sediment_sampling_depth
owner: MeasuredSedimentFields
domain_of:
- MeasuredSedimentFields
range: string
required: true

```
</details>