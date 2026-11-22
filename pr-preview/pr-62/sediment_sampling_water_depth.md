

# Slot: Sediment Sampling Water Depth (sediment_sampling_water_depth)


_Water depth where sediment was collected. If provided as a variable (recommended), please list the column header name here._





URI: [oae:sediment_sampling_water_depth](https://schema.oaedata.org/sediment_sampling_water_depth)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContinuousSedimentVariable](ContinuousSedimentVariable.md) | Measured sediment variable collected from continuous autonomous sensor |  no  |
| [MeasuredSedimentFields](MeasuredSedimentFields.md) | Fields applied to all measured sediment variable types (discrete and continuo... |  no  |
| [DiscreteSedimentVariable](DiscreteSedimentVariable.md) | Measured sediment variable collected from discrete bottle samples |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:sediment_sampling_water_depth |
| native | oae:sediment_sampling_water_depth |




## LinkML Source

<details>
```yaml
name: sediment_sampling_water_depth
description: Water depth where sediment was collected. If provided as a variable (recommended),
  please list the column header name here.
title: Sediment Sampling Water Depth
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: sediment_sampling_water_depth
owner: MeasuredSedimentFields
domain_of:
- MeasuredSedimentFields
range: string
required: true

```
</details>