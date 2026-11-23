

# Slot: Variable full name (long_name)


_Full descriptive name of the variable._





URI: [oae:long_name](https://schema.oaedata.org/long_name)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MeasuredVariable](MeasuredVariable.md) | Variable that is directly measured in-situ using instruments |  no  |
| [SocioeconomicVariable](SocioeconomicVariable.md) | Socioeconomic variable for social and economic data such as survey responses,... |  no  |
| [DiscreteSedimentVariable](DiscreteSedimentVariable.md) | Measured sediment variable collected from discrete bottle samples |  no  |
| [Variable](Variable.md) | Abstract root for all variable types (including non-measured) |  no  |
| [DiscreteTAVariable](DiscreteTAVariable.md) | Total Alkalinity (TA) measured variable from discrete bottle samples |  no  |
| [DiscreteDICVariable](DiscreteDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle sampl... |  no  |
| [ModelOutputVariable](ModelOutputVariable.md) | A variable output by a model simulation (e |  no  |
| [DiscretePHVariable](DiscretePHVariable.md) | pH measured variable with dye-based spectrophotometric measurement |  no  |
| [DiscreteMeasuredVariable](DiscreteMeasuredVariable.md) | A variable measured in-situ from discrete water samples (e |  no  |
| [DiscretePhysiologicalVariable](DiscretePhysiologicalVariable.md) | Physiological response variable from discrete field samples (e |  no  |
| [InSituVariable](InSituVariable.md) | Base class for project-acquired variables (measured or calculated in-situ) |  no  |
| [ContinuousPhysiologicalVariable](ContinuousPhysiologicalVariable.md) | Physiological response variable from continuous autonomous field sensors (e |  no  |
| [ContinuousPHVariable](ContinuousPHVariable.md) | pH measured variable from continuous autonomous sensor |  no  |
| [ContinuousCO2Variable](ContinuousCO2Variable.md) | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2) |  no  |
| [NonMeasuredVariable](NonMeasuredVariable.md) | A contextual or ancillary variable that is NOT directly measured or calculate... |  no  |
| [ContinuousSedimentVariable](ContinuousSedimentVariable.md) | Measured sediment variable collected from continuous autonomous sensor |  no  |
| [ContinuousTAVariable](ContinuousTAVariable.md) | Total Alkalinity (TA) measured variable from continuous autonomous sensor |  no  |
| [CalculatedVariable](CalculatedVariable.md) | A variable that is calculated or derived from other measured variables rather... |  no  |
| [HPLCVariable](HPLCVariable.md) | HPLC (High-Performance Liquid Chromatography) measured variable for pigment a... |  no  |
| [DiscreteCO2Variable](DiscreteCO2Variable.md) | CO2 discrete (bottle) measured variable (pCO2/fCO2) |  no  |
| [ContinuousDICVariable](ContinuousDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous... |  no  |
| [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md) | A variable measured in-situ by a continuous autonomous sensor (e |  no  |
| [FieldVariable](FieldVariable.md) | Abstract root for every variable that can appear in a FieldDataset — measured... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:long_name |
| native | oae:long_name |




## LinkML Source

<details>
```yaml
name: long_name
description: Full descriptive name of the variable.
title: Variable full name
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: long_name
owner: Variable
domain_of:
- Variable
range: string
required: true

```
</details>