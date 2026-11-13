# Enum: PHCalibrationStandard




_Standard used to calibrate a pH measurement._



URI: [PHCalibrationStandard](PHCalibrationStandard.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| dye | None | Indicator dye, e |
| tris | None | TRIS buffer in synthetic seawater |
| other | None | A standard not listed here |




## Slots

| Name | Description |
| ---  | --- |
| [standard_used](standard_used.md) | Type of standard used to calibrate the pH measurement |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: PHCalibrationStandard
description: Standard used to calibrate a pH measurement.
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  dye:
    text: dye
    description: Indicator dye, e.g., m-cresol purple.
    title: Dye
  tris:
    text: tris
    description: TRIS buffer in synthetic seawater.
    title: TRIS
  other:
    text: other
    description: A standard not listed here. Name it in the custom field.
    title: Other

```
</details>
