

# Slot: Longitude (longitude)


_Longitude in decimal degrees of a location. For example -122.08585 (WGS 84)._





URI: [schema:longitude](http://schema.org/longitude)



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
| self | schema:longitude |
| native | oae:longitude |




## LinkML Source

<details>
```yaml
name: longitude
description: Longitude in decimal degrees of a location. For example -122.08585 (WGS
  84).
title: Longitude
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
slot_uri: schema:longitude
alias: longitude
owner: GeoCoordinates
domain_of:
- GeoCoordinates
range: float
required: true

```
</details>