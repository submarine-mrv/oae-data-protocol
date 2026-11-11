

# Slot: Storage method (storage_method)


_How the samples were stored before the measurement._





URI: [oae:storage_method](https://schema.oaedata.org/storage_method)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiscreteCO2Variable](DiscreteCO2Variable.md) | CO2 discrete (bottle) measured variable (pCO2/fCO2) |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:storage_method |
| native | oae:storage_method |




## LinkML Source

<details>
```yaml
name: storage_method
description: How the samples were stored before the measurement.
title: Storage method
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: storage_method
owner: DiscreteCO2Variable
domain_of:
- DiscreteCO2Variable
range: string
required: true

```
</details>