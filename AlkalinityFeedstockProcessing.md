# Enum: AlkalinityFeedstockProcessing




_Methods used to process alkalinity feedstock_



URI: [AlkalinityFeedstockProcessing](AlkalinityFeedstockProcessing.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| electrochemistry | None | Alkalinity generated via electrochemical processes (e |
| synthetically_derived | None | Intentionally industrially manufactured chemical compounds (e |
| mineral_mining | None | Mined geological material, including purified mineral or natural rock |
| blended | None | A mix of multiple sources |
| other | None | Unclassified or novel; include a description in Experiment Description |




## Slots

| Name | Description |
| ---  | --- |
| [alkalinity_feedstock_processing](alkalinity_feedstock_processing.md) | Method(s) used to process the alkalinity feedstock |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: AlkalinityFeedstockProcessing
description: Methods used to process alkalinity feedstock
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  electrochemistry:
    text: electrochemistry
    description: Alkalinity generated via electrochemical processes (e.g., seawater
      electrolysis).
  synthetically_derived:
    text: synthetically_derived
    description: Intentionally industrially manufactured chemical compounds (e.g.,
      Ca(OH)2 via lime kilns).
  mineral_mining:
    text: mineral_mining
    description: Mined geological material, including purified mineral or natural
      rock.
  blended:
    text: blended
    description: A mix of multiple sources.
  other:
    text: other
    description: Unclassified or novel; include a description in Experiment Description.

```
</details>
