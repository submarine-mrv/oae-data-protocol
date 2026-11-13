

# Slot: Method to calculate reported values from raw data (raw_data_calculation_method)


_The method used to calculate reported values from raw sensor data._





URI: [oae:raw_data_calculation_method](https://schema.oaedata.org/raw_data_calculation_method)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContinuousPhysiologicalVariable](ContinuousPhysiologicalVariable.md) | Physiological response variable from continuous autonomous field sensors (e |  no  |
| [ContinuousPHVariable](ContinuousPHVariable.md) | pH measured variable from continuous autonomous sensor |  no  |
| [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md) | A variable measured in-situ by a continuous autonomous sensor (e |  no  |
| [ContinuousTAVariable](ContinuousTAVariable.md) | Total Alkalinity (TA) measured variable from continuous autonomous sensor |  no  |
| [ContinuousCO2Variable](ContinuousCO2Variable.md) | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2) |  no  |
| [ContinuousSedimentVariable](ContinuousSedimentVariable.md) | Measured sediment variable collected from continuous autonomous sensor |  no  |
| [ContinuousDICVariable](ContinuousDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:raw_data_calculation_method |
| native | oae:raw_data_calculation_method |




## LinkML Source

<details>
```yaml
name: raw_data_calculation_method
description: The method used to calculate reported values from raw sensor data.
title: Method to calculate reported values from raw data
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: raw_data_calculation_method
owner: ContinuousMeasuredVariable
domain_of:
- ContinuousMeasuredVariable
range: string
required: true

```
</details>