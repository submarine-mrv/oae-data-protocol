

# Slot: box


_A bounding box defined by two corner points — the southwest (lower-left) corner followed by the northeast (upper-right) corner. Per science-on-schema.org, each point is written as `<latitude> <longitude>` in decimal degrees (WGS 84), with all four values space-separated: `"<minLat> <minLon> <maxLat> <maxLon>"`. Example: `"39.3280 120.1633 40.445 123.7878"`. See https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md#spatial-coverage_





URI: [schema:box](http://schema.org/box)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeoShape](GeoShape.md) | The geographic shape of a place |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:box |
| native | oae:box |




## LinkML Source

<details>
```yaml
name: box
description: 'A bounding box defined by two corner points — the southwest (lower-left)
  corner followed by the northeast (upper-right) corner. Per science-on-schema.org,
  each point is written as `<latitude> <longitude>` in decimal degrees (WGS 84), with
  all four values space-separated: `"<minLat> <minLon> <maxLat> <maxLon>"`. Example:
  `"39.3280 120.1633 40.445 123.7878"`. See https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md#spatial-coverage'
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
slot_uri: schema:box
alias: box
owner: GeoShape
domain_of:
- GeoShape
range: string

```
</details>