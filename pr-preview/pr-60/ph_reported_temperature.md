

# Slot: Temperature at which pH was reported (ph_reported_temperature)


_The input could be a constant temperature value, or something like, in-situ temperature, temperature of analysis, etc._





URI: [oae:ph_reported_temperature](https://schema.oaedata.org/ph_reported_temperature)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiscretePHVariable](DiscretePHVariable.md) | pH measured variable with dye-based spectrophotometric measurement |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:ph_reported_temperature |
| native | oae:ph_reported_temperature |




## LinkML Source

<details>
```yaml
name: ph_reported_temperature
description: The input could be a constant temperature value, or something like, in-situ
  temperature, temperature of analysis, etc.
title: Temperature at which pH was reported
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: ph_reported_temperature
owner: DiscretePHVariable
domain_of:
- DiscretePHVariable
range: string
required: true

```
</details>