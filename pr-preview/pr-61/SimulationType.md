# Enum: SimulationType




_Type of model simulation dataset_



URI: [SimulationType](SimulationType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| counterfactual | None | Control/baseline simulation without alkalinity perturbation |
| perturbation | None | Simulation with alkalinity perturbation applied |
| other | None | Other simulation type not listed above |




## Slots

| Name | Description |
| ---  | --- |
| [simulation_type](simulation_type.md) | The type(s) of model simulation (e |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: SimulationType
description: Type of model simulation dataset
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  counterfactual:
    text: counterfactual
    description: Control/baseline simulation without alkalinity perturbation
  perturbation:
    text: perturbation
    description: Simulation with alkalinity perturbation applied
  other:
    text: other
    description: Other simulation type not listed above

```
</details>
