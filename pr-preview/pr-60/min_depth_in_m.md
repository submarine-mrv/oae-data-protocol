

# Slot: Minimum Depth (in meters) (min_depth_in_m)


_Minimum depth of observation in meters. Use negative numbers for depths below sea level._





URI: [oae:min_depth_in_m](https://schema.oaedata.org/min_depth_in_m)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VerticalExtent](VerticalExtent.md) | The vertical extent of a place or structure in meters |  no  |







## Properties

* Range: [Float](Float.md)

* Maximum Value: 0





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:min_depth_in_m |
| native | oae:min_depth_in_m |




## LinkML Source

<details>
```yaml
name: min_depth_in_m
description: Minimum depth of observation in meters. Use negative numbers for depths
  below sea level.
title: Minimum Depth (in meters)
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: min_depth_in_m
owner: VerticalExtent
domain_of:
- VerticalExtent
range: float
maximum_value: 0

```
</details>