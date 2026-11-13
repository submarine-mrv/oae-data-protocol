# Enum: ConcentrationBasis




_Whether concentration measurements are expressed per unit volume or per unit mass._



URI: [ConcentrationBasis](ConcentrationBasis.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| per_volume | None | Concentration expressed per unit volume (e |
| per_mass | None | Concentration expressed per unit mass (e |




## Slots

| Name | Description |
| ---  | --- |
| [concentration_basis](concentration_basis.md) | Whether measurements are expressed per unit volume or per unit mass (for DIC,... |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: ConcentrationBasis
description: Whether concentration measurements are expressed per unit volume or per
  unit mass.
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  per_volume:
    text: per_volume
    description: Concentration expressed per unit volume (e.g., μmol/L, mmol/L)
  per_mass:
    text: per_mass
    description: Concentration expressed per unit mass (e.g., μmol/kg-seawater)

```
</details>
