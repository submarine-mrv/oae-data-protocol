# Enum: AlkalinityFeedstockForm




_Physical form of the alkalinity feedstock upon ocean delivery_



URI: [AlkalinityFeedstockForm](AlkalinityFeedstockForm.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| solid | None | Involves adding alkaline minerals or particulate slurry (such as MgOH2, MgO, ... |
| aqueous | None | Aqueous alkalinity addition may use electrochemistry or fully dissolved miner... |
| slurry | None | Slurry alkalinity additions include a mix of solid and aqueous alkalinity for... |




## Slots

| Name | Description |
| ---  | --- |
| [alkalinity_feedstock_form](alkalinity_feedstock_form.md) | The phase upon delivery to the ocean |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: AlkalinityFeedstockForm
description: Physical form of the alkalinity feedstock upon ocean delivery
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  solid:
    text: solid
    description: Involves adding alkaline minerals or particulate slurry (such as
      MgOH2, MgO, or CaO) to seawater or river systems either directly, through coastal
      outfalls (such as wastewater), or at breaking shorelines to increase its alkalinity.
  aqueous:
    text: aqueous
    description: Aqueous alkalinity addition may use electrochemistry or fully dissolved
      mineral feedstock to increase seawater alkalinity.
  slurry:
    text: slurry
    description: Slurry alkalinity additions include a mix of solid and aqueous alkalinity
      forms, where the solid alkaline particulates are suspended in a solution.

```
</details>
