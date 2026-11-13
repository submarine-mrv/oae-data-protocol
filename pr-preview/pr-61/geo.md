

# Slot: geo


_Entities that have a somewhat fixed, physical extension. (imported from schema.org)_





URI: [oae:geo](https://schema.oaedata.org/geo)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpatialCoverage](SpatialCoverage.md) | A bounding box defined by latitude and longitude coordinates |  yes  |
| [Place](Place.md) | A geospatial area of interest, defined by a bounding box, polygon/line, or a ... |  no  |
| [DosingLocation](DosingLocation.md) | A specific location of dosing for an OAE intervention and/or tracer study |  no  |







## Properties

* Range: [Any](Any.md)&nbsp;or&nbsp;<br />[GeoShape](GeoShape.md)&nbsp;or&nbsp;<br />[GeoCoordinates](GeoCoordinates.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:geo |
| native | oae:geo |




## LinkML Source

<details>
```yaml
name: geo
description: Entities that have a somewhat fixed, physical extension. (imported from
  schema.org)
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: geo
domain_of:
- Place
range: Any
any_of:
- range: GeoShape
- range: GeoCoordinates

```
</details>