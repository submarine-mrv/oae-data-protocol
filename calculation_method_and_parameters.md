

# Slot: Calculated Method And Parameters (calculation_method_and_parameters)


_Information about how the variable was calculated and the parameters used in calculation, e.g.: Calculation software = CO2SYSv1 (MATLAB) Input variables =  pH and DIC (column header names 'ph_t_insitu' and 'dic' in associated dataset file) Additional information = the dissociation constants of Lueker et al., 2000 for carbonic acid, etc._





URI: [oae:calculation_method_and_parameters](https://schema.oaedata.org/calculation_method_and_parameters)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CalculatedVariable](CalculatedVariable.md) | A variable that is calculated or derived from other measured variables rather... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:calculation_method_and_parameters |
| native | oae:calculation_method_and_parameters |




## LinkML Source

<details>
```yaml
name: calculation_method_and_parameters
description: 'Information about how the variable was calculated and the parameters
  used in calculation, e.g.: Calculation software = CO2SYSv1 (MATLAB) Input variables
  =  pH and DIC (column header names ''ph_t_insitu'' and ''dic'' in associated dataset
  file) Additional information = the dissociation constants of Lueker et al., 2000
  for carbonic acid, etc.'
title: Calculated Method And Parameters
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: calculation_method_and_parameters
owner: CalculatedVariable
domain_of:
- CalculatedVariable
range: string
required: true

```
</details>