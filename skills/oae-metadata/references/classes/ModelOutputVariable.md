# ModelOutputVariable

A variable output by a model simulation (e.g., air-sea CO2 flux, dissolved inorganic carbon, total alkalinity, pH, temperature, salinity from an OAE model run). Model outputs are produced by the simulation itself, so they carry none of the sampling, instrument, calibration or in-situ QC metadata that field-collected variables do — how the output was produced is described by the simulation configuration on the parent ModelOutputDataset.

Parent: Variable

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| units | yes | no | string | Unit of measurement for this variable. |
| variable_type | yes | no | enum: `air_sea_co2_flux`, `dissolved_inorganic_carbon`, `total_alkalinity`, `temperature`, `salinity`, `ph`, `biological_tracers`, `nutrients`, `zonal_velocity`, `meridional_velocity`, `vertical_velocity`, `co2`, `other` | Which model output quantity this variable holds. There is only one model variable class, so this classifies the variable rather than selecting a schema class. |
| schema_class | yes | no | always `ModelOutputVariable` | The schema class name for this variable (e.g., "DiscretePHVariable"). Auto-populated by the metadata builder. |
| dataset_variable_name | yes | no | string | The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name). |
| long_name | yes | no | string | Full descriptive name of the variable. |
| standard_identifier | no | no | [VocabularyItemReference](VocabularyItemReference.md) | A term from a community vocabulary that identifies this variable. CF standard names (NERC P07) are recommended. |

## Vocabularies

What each value means, for the fields above.

### variable_type

- `air_sea_co2_flux`: Air-sea CO₂ flux
- `dissolved_inorganic_carbon`: Dissolved inorganic carbon (DIC)
- `total_alkalinity`: Total alkalinity (TA)
- `temperature`: Temperature
- `salinity`: Salinity
- `ph`: pH of seawater
- `biological_tracers`: Biological tracers (e.g., chlorophyll, phytoplankton, zooplankton) — biomass or concentration
- `nutrients`: Nutrients (e.g., dissolved oxygen, NO₃⁻, NH₄⁺)
- `zonal_velocity`: Zonal velocity (u)
- `meridional_velocity`: Meridional velocity (v)
- `vertical_velocity`: Vertical velocity (w)
- `co2`: CO₂ variables (xCO₂, pCO₂, fCO₂)
- `other`: Any model output variable that does not fall into a specific category above.
