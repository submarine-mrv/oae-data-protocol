

# Slot: Simulation Type (simulation_type)


_The type(s) of model simulation (e.g., counterfactual, perturbation, or both)._





URI: [oae:simulation_type](https://schema.oaedata.org/simulation_type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |







## Properties

* Range: [SimulationType](SimulationType.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:simulation_type |
| native | oae:simulation_type |




## LinkML Source

<details>
```yaml
name: simulation_type
description: The type(s) of model simulation (e.g., counterfactual, perturbation,
  or both).
title: Simulation Type
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: simulation_type
owner: ModelOutputDataset
domain_of:
- ModelOutputDataset
range: SimulationType
required: true
multivalued: true
minimum_cardinality: 1

```
</details>