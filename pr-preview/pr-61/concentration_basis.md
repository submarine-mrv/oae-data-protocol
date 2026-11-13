

# Slot: Per-volume vs per-mass based units (concentration_basis)


_Whether measurements are expressed per unit volume or per unit mass (for DIC, TA, etc.)_





URI: [oae:concentration_basis](https://schema.oaedata.org/concentration_basis)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiscreteDICVariable](DiscreteDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle sampl... |  no  |
| [MeasuredDICFields](MeasuredDICFields.md) | Fields applied to all measured DIC variable types (discrete and continuous) |  no  |
| [MeasuredTAFields](MeasuredTAFields.md) | Fields applied to all measured TA variable types (discrete and continuous) |  no  |
| [ContinuousTAVariable](ContinuousTAVariable.md) | Total Alkalinity (TA) measured variable from continuous autonomous sensor |  no  |
| [DiscreteTAVariable](DiscreteTAVariable.md) | Total Alkalinity (TA) measured variable from discrete bottle samples |  no  |
| [ContinuousDICVariable](ContinuousDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous... |  no  |







## Properties

* Range: [ConcentrationBasis](ConcentrationBasis.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:concentration_basis |
| native | oae:concentration_basis |




## LinkML Source

<details>
```yaml
name: concentration_basis
description: Whether measurements are expressed per unit volume or per unit mass (for
  DIC, TA, etc.)
title: Per-volume vs per-mass based units
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: concentration_basis
domain_of:
- MeasuredTAFields
- MeasuredDICFields
range: ConcentrationBasis
required: true

```
</details>