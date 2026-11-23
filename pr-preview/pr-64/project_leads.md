

# Slot: Project Lead(s) (project_leads)


_Provide details for each project lead / principal investigator (PI) including: Name, institutional information (name, address), phone, email, ID type (e.g., ORCID, etc), researcher ID, and role._





URI: [oae:project_leads](https://schema.oaedata.org/project_leads)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Project](Project.md) | A project conducting OAE field trials or modeling |  no  |







## Properties

* Range: [Person](Person.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:project_leads |
| native | oae:project_leads |




## LinkML Source

<details>
```yaml
name: project_leads
description: 'Provide details for each project lead / principal investigator (PI)
  including: Name, institutional information (name, address), phone, email, ID type
  (e.g., ORCID, etc), researcher ID, and role.'
title: Project Lead(s)
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: project_leads
owner: Project
domain_of:
- Project
range: Person
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>