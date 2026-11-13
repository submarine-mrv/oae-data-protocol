# Enum: ModelComponentType




_Type of model component_



URI: [ModelComponentType](ModelComponentType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| physics | None | Physical model component (e |
| bgc_ecosystem | None | Biogeochemical or ecosystem model component |
| sea_ice | None | Sea Ice model component |
| atmosphere | None | Atmosphere model component |
| other | None | Other model component (e |




## Slots

| Name | Description |
| ---  | --- |
| [model_component_type](model_component_type.md) | The type of model component (physics, BGC/ecosystem, or other) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: ModelComponentType
description: Type of model component
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  physics:
    text: physics
    description: Physical model component (e.g., ocean circulation)
    title: Physics
  bgc_ecosystem:
    text: bgc_ecosystem
    description: Biogeochemical or ecosystem model component
    title: BGC / Ecosystem
  sea_ice:
    text: sea_ice
    description: Sea Ice model component
    title: Sea Ice
  atmosphere:
    text: atmosphere
    description: Atmosphere model component
    title: Atmosphere
  other:
    text: other
    description: Other model component (e.g., sea ice, sediment, atmosphere)

```
</details>
