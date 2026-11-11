

# Slot: Titration type (titration_type)


_Type of the titration used to determine alkalinity._





URI: [oae:titration_type](https://schema.oaedata.org/titration_type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiscreteTAVariable](DiscreteTAVariable.md) | Total Alkalinity (TA) measured variable from discrete bottle samples |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:titration_type |
| native | oae:titration_type |




## LinkML Source

<details>
```yaml
name: titration_type
description: Type of the titration used to determine alkalinity.
title: Titration type
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: titration_type
owner: DiscreteTAVariable
domain_of:
- DiscreteTAVariable
range: string
required: true

```
</details>