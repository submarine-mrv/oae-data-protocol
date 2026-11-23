# Enum: HydrologicLocation




_Hydrologic location types for dosing_



URI: [HydrologicLocation](HydrologicLocation.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| coastal_surface | None | Surface waters in coastal areas |
| offshore_surface | None | Surface waters in offshore areas |
| river | None | River systems |
| wetland | None | Wetland areas |
| seafloor | None | Seafloor or benthic zone |




## Slots

| Name | Description |
| ---  | --- |
| [dosing_dispersal_hydrologic_location](dosing_dispersal_hydrologic_location.md) | Descriptive dosing location |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: HydrologicLocation
description: Hydrologic location types for dosing
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  coastal_surface:
    text: coastal_surface
    description: Surface waters in coastal areas
    title: Coastal Surface
  offshore_surface:
    text: offshore_surface
    description: Surface waters in offshore areas
    title: Offshore Surface
  river:
    text: river
    description: River systems
  wetland:
    text: wetland
    description: Wetland areas
  seafloor:
    text: seafloor
    description: Seafloor or benthic zone

```
</details>
