# Enum: EquilibrationStatus




_Equilibration status of the alkalinity feedstock_



URI: [EquilibrationStatus](EquilibrationStatus.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| pre_equilibrated | None | Pre-equilibrated with atmosphere before dosing |
| unequilibrated | None | Not pre-equilibrated before dosing |




## Slots

| Name | Description |
| ---  | --- |
| [equilibration](equilibration.md) | Whether the feedstock was pre-equilibrated or unequilibrated |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: EquilibrationStatus
description: Equilibration status of the alkalinity feedstock
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  pre_equilibrated:
    text: pre_equilibrated
    description: Pre-equilibrated with atmosphere before dosing
    title: Pre-equilibrated
  unequilibrated:
    text: unequilibrated
    description: Not pre-equilibrated before dosing

```
</details>
