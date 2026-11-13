

# Slot: Variable Type (variable_type)


_High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use._





URI: [oae:variable_type](https://schema.oaedata.org/variable_type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MeasuredVariable](MeasuredVariable.md) | Variable that is directly measured in-situ using instruments |  no  |
| [FieldVariable](FieldVariable.md) | Abstract root for every variable that can appear in a FieldDataset — measured... |  yes  |
| [ContinuousPHVariable](ContinuousPHVariable.md) | pH measured variable from continuous autonomous sensor |  yes  |
| [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md) | A variable measured in-situ by a continuous autonomous sensor (e |  no  |
| [DiscretePhysiologicalVariable](DiscretePhysiologicalVariable.md) | Physiological response variable from discrete field samples (e |  yes  |
| [ContinuousDICVariable](ContinuousDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous... |  yes  |
| [CalculatedVariable](CalculatedVariable.md) | A variable that is calculated or derived from other measured variables rather... |  no  |
| [Variable](Variable.md) | Abstract root for all variable types (including non-measured) |  yes  |
| [InSituVariable](InSituVariable.md) | Base class for project-acquired variables (measured or calculated in-situ) |  no  |
| [DiscreteMeasuredVariable](DiscreteMeasuredVariable.md) | A variable measured in-situ from discrete water samples (e |  no  |
| [ModelOutputVariable](ModelOutputVariable.md) | A variable output by a model simulation (e |  yes  |
| [HPLCVariable](HPLCVariable.md) | HPLC (High-Performance Liquid Chromatography) measured variable for pigment a... |  yes  |
| [DiscreteSedimentVariable](DiscreteSedimentVariable.md) | Measured sediment variable collected from discrete bottle samples |  yes  |
| [ContinuousCO2Variable](ContinuousCO2Variable.md) | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2) |  yes  |
| [ContinuousPhysiologicalVariable](ContinuousPhysiologicalVariable.md) | Physiological response variable from continuous autonomous field sensors (e |  yes  |
| [DiscreteTAVariable](DiscreteTAVariable.md) | Total Alkalinity (TA) measured variable from discrete bottle samples |  yes  |
| [NonMeasuredVariable](NonMeasuredVariable.md) | A contextual or ancillary variable that is NOT directly measured or calculate... |  yes  |
| [DiscreteDICVariable](DiscreteDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle sampl... |  yes  |
| [ContinuousTAVariable](ContinuousTAVariable.md) | Total Alkalinity (TA) measured variable from continuous autonomous sensor |  yes  |
| [ContinuousSedimentVariable](ContinuousSedimentVariable.md) | Measured sediment variable collected from continuous autonomous sensor |  yes  |
| [DiscretePHVariable](DiscretePHVariable.md) | pH measured variable with dye-based spectrophotometric measurement |  yes  |
| [SocioeconomicVariable](SocioeconomicVariable.md) | Socioeconomic variable for social and economic data such as survey responses,... |  yes  |
| [DiscreteCO2Variable](DiscreteCO2Variable.md) | CO2 discrete (bottle) measured variable (pCO2/fCO2) |  yes  |







## Properties

* Range: [VariableType](VariableType.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:variable_type |
| native | oae:variable_type |




## LinkML Source

<details>
```yaml
name: variable_type
description: High-level classification of the variable. Determines which standard
  identifiers are available and, combined with genesis and sampling, which schema
  class to use.
title: Variable Type
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: variable_type
domain_of:
- Variable
range: VariableType

```
</details>