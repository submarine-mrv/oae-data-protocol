

# Slot: is_derived_value


_Indicates that the field in question is a derived value as opposed to one measured directly._





URI: [oae:is_derived_value](https://schema.oaedata.org/is_derived_value)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DosingConcentration](DosingConcentration.md) | Details of tracer concentration information |  no  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:is_derived_value |
| native | oae:is_derived_value |




## LinkML Source

<details>
```yaml
name: is_derived_value
description: Indicates that the field in question is a derived value as opposed to
  one measured directly.
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: is_derived_value
domain_of:
- DosingConcentration
range: boolean
required: true

```
</details>