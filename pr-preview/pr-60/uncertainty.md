

# Slot: Uncertainty (uncertainty)


_It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset._

_If uncertainty is provided as a variable, please list the column header name here._





URI: [oae:uncertainty](https://schema.oaedata.org/uncertainty)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md) | A variable measured in-situ by a continuous autonomous sensor (e |  no  |
| [DiscreteDICVariable](DiscreteDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle sampl... |  no  |
| [DiscreteCO2Variable](DiscreteCO2Variable.md) | CO2 discrete (bottle) measured variable (pCO2/fCO2) |  no  |
| [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector for continuous measurements, with measurement frequency |  no  |
| [ContinuousPhysiologicalVariable](ContinuousPhysiologicalVariable.md) | Physiological response variable from continuous autonomous field sensors (e |  no  |
| [ContinuousSedimentVariable](ContinuousSedimentVariable.md) | Measured sediment variable collected from continuous autonomous sensor |  no  |
| [ContinuousTAVariable](ContinuousTAVariable.md) | Total Alkalinity (TA) measured variable from continuous autonomous sensor |  no  |
| [MeasuredVariable](MeasuredVariable.md) | Variable that is directly measured in-situ using instruments |  yes  |
| [DiscretePHVariable](DiscretePHVariable.md) | pH measured variable with dye-based spectrophotometric measurement |  no  |
| [DiscreteSedimentVariable](DiscreteSedimentVariable.md) | Measured sediment variable collected from discrete bottle samples |  no  |
| [DiscreteMeasuredVariable](DiscreteMeasuredVariable.md) | A variable measured in-situ from discrete water samples (e |  no  |
| [ContinuousDICVariable](ContinuousDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous... |  no  |
| [ContinuousStandardGas](ContinuousStandardGas.md) | Standard gas used for continuous CO2 calibration, with additional traceabilit... |  no  |
| [DiscretePhysiologicalVariable](DiscretePhysiologicalVariable.md) | Physiological response variable from discrete field samples (e |  no  |
| [QCFields](QCFields.md) | Quality control fields applicable to measured and calculated variables |  no  |
| [CO2GasDetector](CO2GasDetector.md) | CO2 gas detector with standard gas calibration |  no  |
| [ContinuousCO2Variable](ContinuousCO2Variable.md) | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2) |  no  |
| [StandardGas](StandardGas.md) | Standard gas used for CO2 calibration |  no  |
| [DiscreteTAVariable](DiscreteTAVariable.md) | Total Alkalinity (TA) measured variable from discrete bottle samples |  no  |
| [CalculatedVariable](CalculatedVariable.md) | A variable that is calculated or derived from other measured variables rather... |  no  |
| [HPLCVariable](HPLCVariable.md) | HPLC (High-Performance Liquid Chromatography) measured variable for pigment a... |  no  |
| [ContinuousPHVariable](ContinuousPHVariable.md) | pH measured variable from continuous autonomous sensor |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:uncertainty |
| native | oae:uncertainty |




## LinkML Source

<details>
```yaml
name: uncertainty
description: 'It is recommended to provide uncertainty for each data point in the
  data file. Else provide a single value representative of the dataset.

  If uncertainty is provided as a variable, please list the column header name here.'
title: Uncertainty
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: uncertainty
domain_of:
- StandardGas
- CO2GasDetector
- QCFields
range: string

```
</details>