

# Slot: identifier


_A unique identifier for the thing_





URI: [schema:identifier](http://schema.org/identifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.md) |  |  yes  |
| [MonetaryGrant](MonetaryGrant.md) |  |  yes  |
| [Person](Person.md) | Information about a researcher or investigator involved in the experiment |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:identifier |
| native | oae:identifier |




## LinkML Source

<details>
```yaml
name: identifier
description: A unique identifier for the thing
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
slot_uri: schema:identifier
alias: identifier
domain_of:
- Organization
- MonetaryGrant
- Person
range: string

```
</details>