# Enum: CalibrationLocation




_Where the calibration was performed._



URI: [CalibrationLocation](CalibrationLocation.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| factory | None | Factory calibration performed by manufacturer |
| lab | None | Laboratory calibration |
| field | None | Field calibration performed during deployment |




## Slots

| Name | Description |
| ---  | --- |
| [calibration_location](calibration_location.md) | Factory calibration, lab calibration, or field calibration |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: CalibrationLocation
description: Where the calibration was performed.
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  factory:
    text: factory
    description: Factory calibration performed by manufacturer.
  lab:
    text: lab
    description: Laboratory calibration.
  field:
    text: field
    description: Field calibration performed during deployment.

```
</details>
