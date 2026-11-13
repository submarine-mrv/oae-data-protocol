

# Slot: Email (email)


_Contact email address._





URI: [oae:email](https://schema.oaedata.org/email)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Information about a researcher or investigator involved in the experiment |  no  |







## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:email |
| native | oae:email |




## LinkML Source

<details>
```yaml
name: email
description: Contact email address.
title: Email
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: email
owner: Person
domain_of:
- Person
range: string
required: true
pattern: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

```
</details>