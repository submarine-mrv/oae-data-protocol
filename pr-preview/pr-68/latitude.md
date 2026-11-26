

# Slot: Latitude (latitude)


_Latitude in decimal degrees of a location. For example 37.42242 (WGS 84)._





URI: [schema:latitude](http://schema.org/latitude)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeoCoordinates](GeoCoordinates.md) | A geographic coordinate in decimal degrees |  no  |







## Properties

* Range: [Float](Float.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:latitude |
| native | oae:latitude |




## LinkML Source

<details>
```yaml
name: latitude
description: Latitude in decimal degrees of a location. For example 37.42242 (WGS
  84).
title: Latitude
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
slot_uri: schema:latitude
alias: latitude
owner: GeoCoordinates
domain_of:
- GeoCoordinates
range: float
required: true

```
</details>