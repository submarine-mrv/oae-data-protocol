

# Slot: Life Stage (custom) (life_stage_custom)


_Custom life stage description when "other" is selected._





URI: [oae:life_stage_custom](https://schema.oaedata.org/life_stage_custom)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContinuousPhysiologicalVariable](ContinuousPhysiologicalVariable.md) | Physiological response variable from continuous autonomous field sensors (e |  no  |
| [DiscretePhysiologicalVariable](DiscretePhysiologicalVariable.md) | Physiological response variable from discrete field samples (e |  no  |
| [MeasuredPhysiologicalFields](MeasuredPhysiologicalFields.md) | Fields applied to all measured physiological variable types (discrete and con... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:life_stage_custom |
| native | oae:life_stage_custom |




## LinkML Source

<details>
```yaml
name: life_stage_custom
description: Custom life stage description when "other" is selected.
title: Life Stage (custom)
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: life_stage_custom
owner: MeasuredPhysiologicalFields
domain_of:
- MeasuredPhysiologicalFields
range: string

```
</details>