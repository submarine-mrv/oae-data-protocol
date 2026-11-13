

# Slot: Biological Subject (biological_subject)


_Taxonomy (species, genus, or community) being studied (e.g., Crassostrea gigas, coral reef community)._





URI: [oae:biological_subject](https://schema.oaedata.org/biological_subject)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MeasuredPhysiologicalFields](MeasuredPhysiologicalFields.md) | Fields applied to all measured physiological variable types (discrete and con... |  no  |
| [DiscretePhysiologicalVariable](DiscretePhysiologicalVariable.md) | Physiological response variable from discrete field samples (e |  no  |
| [ContinuousPhysiologicalVariable](ContinuousPhysiologicalVariable.md) | Physiological response variable from continuous autonomous field sensors (e |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:biological_subject |
| native | oae:biological_subject |




## LinkML Source

<details>
```yaml
name: biological_subject
description: Taxonomy (species, genus, or community) being studied (e.g., Crassostrea
  gigas, coral reef community).
title: Biological Subject
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: biological_subject
owner: MeasuredPhysiologicalFields
domain_of:
- MeasuredPhysiologicalFields
range: string
required: true

```
</details>