

# Slot: genesis



URI: [oae:genesis](https://schema.oaedata.org/genesis)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InSituVariable](InSituVariable.md) | Base class for project-acquired variables (measured or calculated in-situ) |  no  |
| [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md) | A variable measured in-situ by a continuous autonomous sensor (e |  no  |
| [DiscreteDICVariable](DiscreteDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle sampl... |  no  |
| [DiscreteCO2Variable](DiscreteCO2Variable.md) | CO2 discrete (bottle) measured variable (pCO2/fCO2) |  no  |
| [ContinuousPhysiologicalVariable](ContinuousPhysiologicalVariable.md) | Physiological response variable from continuous autonomous field sensors (e |  no  |
| [ContinuousSedimentVariable](ContinuousSedimentVariable.md) | Measured sediment variable collected from continuous autonomous sensor |  no  |
| [ContinuousTAVariable](ContinuousTAVariable.md) | Total Alkalinity (TA) measured variable from continuous autonomous sensor |  no  |
| [MeasuredVariable](MeasuredVariable.md) | Variable that is directly measured in-situ using instruments |  yes  |
| [DiscretePHVariable](DiscretePHVariable.md) | pH measured variable with dye-based spectrophotometric measurement |  no  |
| [SocioeconomicVariable](SocioeconomicVariable.md) | Socioeconomic variable for social and economic data such as survey responses,... |  no  |
| [DiscreteSedimentVariable](DiscreteSedimentVariable.md) | Measured sediment variable collected from discrete bottle samples |  no  |
| [DiscreteMeasuredVariable](DiscreteMeasuredVariable.md) | A variable measured in-situ from discrete water samples (e |  no  |
| [ContinuousDICVariable](ContinuousDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous... |  no  |
| [DiscretePhysiologicalVariable](DiscretePhysiologicalVariable.md) | Physiological response variable from discrete field samples (e |  no  |
| [ContinuousCO2Variable](ContinuousCO2Variable.md) | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2) |  no  |
| [DiscreteTAVariable](DiscreteTAVariable.md) | Total Alkalinity (TA) measured variable from discrete bottle samples |  no  |
| [CalculatedVariable](CalculatedVariable.md) | A variable that is calculated or derived from other measured variables rather... |  yes  |
| [HPLCVariable](HPLCVariable.md) | HPLC (High-Performance Liquid Chromatography) measured variable for pigment a... |  no  |
| [ContinuousPHVariable](ContinuousPHVariable.md) | pH measured variable from continuous autonomous sensor |  no  |







## Properties

* Range: [GenesisType](GenesisType.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:genesis |
| native | oae:genesis |




## LinkML Source

<details>
```yaml
name: genesis
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: genesis
owner: InSituVariable
domain_of:
- InSituVariable
range: GenesisType
required: true

```
</details>