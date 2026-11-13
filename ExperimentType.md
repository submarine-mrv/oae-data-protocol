# Enum: ExperimentType




_Types of mCDR experiments_



URI: [ExperimentType](ExperimentType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| baseline | None | Baseline measurements taken before any intervention |
| control | None | Control experiment without intervention for comparison |
| intervention | None | Experiment with active OAE intervention |
| tracer_study | None | Tracer study experiment (eg- dye or gas tracer study) |
| model | None | Model-based experiment or simulation |
| other | None | Other experiment type not covered by standard categories |




## Slots

| Name | Description |
| ---  | --- |
| [experiment_types](experiment_types.md) | The type(s) of mCDR experiment conducted |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: ExperimentType
description: Types of mCDR experiments
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  baseline:
    text: baseline
    description: Baseline measurements taken before any intervention
  control:
    text: control
    description: Control experiment without intervention for comparison
  intervention:
    text: intervention
    description: Experiment with active OAE intervention
  tracer_study:
    text: tracer_study
    description: Tracer study experiment (eg- dye or gas tracer study)
  model:
    text: model
    description: Model-based experiment or simulation
  other:
    text: other
    description: Other experiment type not covered by standard categories

```
</details>
