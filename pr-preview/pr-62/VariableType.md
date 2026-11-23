# Enum: VariableType




_High-level classification of the variable. Determines which schema class to use in combination with genesis (measured/calculated) and sampling (discrete/continuous)._



URI: [VariableType](VariableType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| pH | None | pH measurement — use with Discrete/ContinuousPHVariable or CalculatedVariable |
| ta | None | Total alkalinity — use with Discrete/ContinuousTAVariable or CalculatedVariab... |
| dic | None | Dissolved inorganic carbon — use with Discrete/ContinuousDICVariable or Calcu... |
| co2 | None | CO₂ variables (xCO₂, pCO₂, fCO₂) — use with DiscreteCO2Variable or Calculated... |
| sediment | None | Sediment variable — use with Discrete/ContinuousSedimentVariable or Calculate... |
| hplc | None | HPLC pigment analysis — use with HPLCVariable (always discrete, always measur... |
| physiological | None | Physiological response variable — organism response data from field experimen... |
| socioeconomic | None | Socioeconomic variable — social and economic data |
| other | None | Any directly measured or calculated variable that does not fall into a specif... |
| non_measured | None | Contextual or ancillary columns that are not directly measured or calculated ... |




## Slots

| Name | Description |
| ---  | --- |
| [variable_type](variable_type.md) | High-level classification of the variable |
| [variable_type](variable_type.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: VariableType
description: High-level classification of the variable. Determines which schema class
  to use in combination with genesis (measured/calculated) and sampling (discrete/continuous).
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  pH:
    text: pH
    description: pH measurement — use with Discrete/ContinuousPHVariable or CalculatedVariable
  ta:
    text: ta
    description: Total alkalinity — use with Discrete/ContinuousTAVariable or CalculatedVariable
  dic:
    text: dic
    description: Dissolved inorganic carbon — use with Discrete/ContinuousDICVariable
      or CalculatedVariable
  co2:
    text: co2
    description: CO₂ variables (xCO₂, pCO₂, fCO₂) — use with DiscreteCO2Variable or
      CalculatedVariable
  sediment:
    text: sediment
    description: Sediment variable — use with Discrete/ContinuousSedimentVariable
      or CalculatedVariable
  hplc:
    text: hplc
    description: HPLC pigment analysis — use with HPLCVariable (always discrete, always
      measured)
  physiological:
    text: physiological
    description: Physiological response variable — organism response data from field
      experiments. Use with Discrete/ContinuousPhysiologicalVariable or CalculatedVariable.
  socioeconomic:
    text: socioeconomic
    description: Socioeconomic variable — social and economic data. Use only with
      SocioeconomicVariable. Does not include QC fields.
  other:
    text: other
    description: Any directly measured or calculated variable that does not fall into
      a specific category above (e.g., temperature, salinity, conductivity, pressure,
      fluorescence). Use with DiscreteMeasuredVariable, ContinuousMeasuredVariable,
      or CalculatedVariable.
  non_measured:
    text: non_measured
    description: Contextual or ancillary columns that are not directly measured or
      calculated by the project — identifiers, timestamps, coordinates and external
      source data. QC flag columns should NOT be listed as separate variables; instead
      set dataset_variable_name_qc_flag on the parent variable. Use only with NonMeasuredVariable.

```
</details>
