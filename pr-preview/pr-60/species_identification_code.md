

# Slot: Species Identification Code (species_identification_code)


_Species reference code from a taxonomic database (e.g., WoRMS AphiaID 140656, ITIS TSN 79861)._





URI: [oae:species_identification_code](https://schema.oaedata.org/species_identification_code)



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
| self | oae:species_identification_code |
| native | oae:species_identification_code |




## LinkML Source

<details>
```yaml
name: species_identification_code
description: Species reference code from a taxonomic database (e.g., WoRMS AphiaID
  140656, ITIS TSN 79861).
title: Species Identification Code
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: species_identification_code
owner: MeasuredPhysiologicalFields
domain_of:
- MeasuredPhysiologicalFields
range: string

```
</details>