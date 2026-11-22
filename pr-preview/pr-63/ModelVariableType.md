# Enum: ModelVariableType




_Classification of a variable output by a model simulation. Used in place of VariableType on ModelOutputVariable. Model output covers a different set of quantities than field measurement (velocities and fluxes rather than sampling-based observations), so this enum is different than VariableType._



URI: [ModelVariableType](ModelVariableType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| air_sea_co2_flux | None | Air-sea CO₂ flux |
| dissolved_inorganic_carbon | None | Dissolved inorganic carbon (DIC) |
| total_alkalinity | None | Total alkalinity (TA) |
| temperature | None | Temperature |
| salinity | None | Salinity |
| ph | None | pH of seawater |
| biological_tracers | None | Biological tracers (e |
| nutrients | None | Nutrients (e |
| zonal_velocity | None | Zonal velocity (u) |
| meridional_velocity | None | Meridional velocity (v) |
| vertical_velocity | None | Vertical velocity (w) |
| co2 | None | CO₂ variables (xCO₂, pCO₂, fCO₂) |
| other | None | Any model output variable that does not fall into a specific category above |




## Slots

| Name | Description |
| ---  | --- |
| [variable_type](variable_type.md) | Which model output quantity this variable holds |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: ModelVariableType
description: Classification of a variable output by a model simulation. Used in place
  of VariableType on ModelOutputVariable. Model output covers a different set of quantities
  than field measurement (velocities and fluxes rather than sampling-based observations),
  so this enum is different than VariableType.
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  air_sea_co2_flux:
    text: air_sea_co2_flux
    description: Air-sea CO₂ flux
  dissolved_inorganic_carbon:
    text: dissolved_inorganic_carbon
    description: Dissolved inorganic carbon (DIC)
  total_alkalinity:
    text: total_alkalinity
    description: Total alkalinity (TA)
  temperature:
    text: temperature
    description: Temperature
  salinity:
    text: salinity
    description: Salinity
  ph:
    text: ph
    description: pH of seawater
  biological_tracers:
    text: biological_tracers
    description: Biological tracers (e.g., chlorophyll, phytoplankton, zooplankton)
      — biomass or concentration
  nutrients:
    text: nutrients
    description: Nutrients (e.g., dissolved oxygen, NO₃⁻, NH₄⁺)
  zonal_velocity:
    text: zonal_velocity
    description: Zonal velocity (u)
  meridional_velocity:
    text: meridional_velocity
    description: Meridional velocity (v)
  vertical_velocity:
    text: vertical_velocity
    description: Vertical velocity (w)
  co2:
    text: co2
    description: CO₂ variables (xCO₂, pCO₂, fCO₂)
  other:
    text: other
    description: Any model output variable that does not fall into a specific category
      above.

```
</details>
