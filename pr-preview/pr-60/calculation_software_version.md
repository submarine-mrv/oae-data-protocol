

# Slot: Software version for the calculation (calculation_software_version)


_Version of the software used to calculate reported values from raw values._





URI: [oae:calculation_software_version](https://schema.oaedata.org/calculation_software_version)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContinuousCO2Variable](ContinuousCO2Variable.md) | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2) |  no  |
| [ContinuousPHVariable](ContinuousPHVariable.md) | pH measured variable from continuous autonomous sensor |  no  |
| [ContinuousPhysiologicalVariable](ContinuousPhysiologicalVariable.md) | Physiological response variable from continuous autonomous field sensors (e |  no  |
| [ContinuousTAVariable](ContinuousTAVariable.md) | Total Alkalinity (TA) measured variable from continuous autonomous sensor |  no  |
| [ContinuousSedimentVariable](ContinuousSedimentVariable.md) | Measured sediment variable collected from continuous autonomous sensor |  no  |
| [ContinuousDICVariable](ContinuousDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous... |  no  |
| [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md) | A variable measured in-situ by a continuous autonomous sensor (e |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:calculation_software_version |
| native | oae:calculation_software_version |




## LinkML Source

<details>
```yaml
name: calculation_software_version
description: Version of the software used to calculate reported values from raw values.
title: Software version for the calculation
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: calculation_software_version
owner: ContinuousMeasuredVariable
domain_of:
- ContinuousMeasuredVariable
range: string

```
</details>