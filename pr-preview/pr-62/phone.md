

# Slot: Phone (phone)


_Contact phone number._





URI: [oae:phone](https://schema.oaedata.org/phone)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Information about a researcher or investigator involved in the experiment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\+?[0-9\s\-\(\)]+$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:phone |
| native | oae:phone |




## LinkML Source

<details>
```yaml
name: phone
description: Contact phone number.
title: Phone
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: phone
owner: Person
domain_of:
- Person
range: string
pattern: ^\+?[0-9\s\-\(\)]+$

```
</details>