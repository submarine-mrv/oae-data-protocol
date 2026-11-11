

# Slot: Missing value indicators (missing_value_indicators)


_The indicator used to represent missing values in the data file, e.g., -999, NaN, etc._





URI: [oae:missing_value_indicators](https://schema.oaedata.org/missing_value_indicators)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md) | A variable measured in-situ by a continuous autonomous sensor (e |  no  |
| [DiscreteTAVariable](DiscreteTAVariable.md) | Total Alkalinity (TA) measured variable from discrete bottle samples |  no  |
| [DiscreteDICVariable](DiscreteDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle sampl... |  no  |
| [DiscretePHVariable](DiscretePHVariable.md) | pH measured variable with dye-based spectrophotometric measurement |  no  |
| [DiscreteCO2Variable](DiscreteCO2Variable.md) | CO2 discrete (bottle) measured variable (pCO2/fCO2) |  no  |
| [DiscreteSedimentVariable](DiscreteSedimentVariable.md) | Measured sediment variable collected from discrete bottle samples |  no  |
| [QCFields](QCFields.md) | Quality control fields applicable to measured and calculated variables |  no  |
| [DiscreteMeasuredVariable](DiscreteMeasuredVariable.md) | A variable measured in-situ from discrete water samples (e |  no  |
| [CalculatedVariable](CalculatedVariable.md) | A variable that is calculated or derived from other measured variables rather... |  no  |
| [HPLCVariable](HPLCVariable.md) | HPLC (High-Performance Liquid Chromatography) measured variable for pigment a... |  no  |
| [ContinuousCO2Variable](ContinuousCO2Variable.md) | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2) |  no  |
| [ContinuousDICVariable](ContinuousDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous... |  no  |
| [ContinuousPHVariable](ContinuousPHVariable.md) | pH measured variable from continuous autonomous sensor |  no  |
| [ContinuousTAVariable](ContinuousTAVariable.md) | Total Alkalinity (TA) measured variable from continuous autonomous sensor |  no  |
| [ContinuousSedimentVariable](ContinuousSedimentVariable.md) | Measured sediment variable collected from continuous autonomous sensor |  no  |
| [ContinuousPhysiologicalVariable](ContinuousPhysiologicalVariable.md) | Physiological response variable from continuous autonomous field sensors (e |  no  |
| [DiscretePhysiologicalVariable](DiscretePhysiologicalVariable.md) | Physiological response variable from discrete field samples (e |  no  |
| [MeasuredVariable](MeasuredVariable.md) | Variable that is directly measured in-situ using instruments |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:missing_value_indicators |
| native | oae:missing_value_indicators |




## LinkML Source

<details>
```yaml
name: missing_value_indicators
description: The indicator used to represent missing values in the data file, e.g.,
  -999, NaN, etc.
title: Missing value indicators
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: missing_value_indicators
domain_of:
- QCFields
range: string

```
</details>