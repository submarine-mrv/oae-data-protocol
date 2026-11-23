

# Slot: Funding Info (funding)


_Include the name of the funder, funder country, project title, project ID, and the project start and end dates. If there is no funding source (e.g., in the case of commercial projects), leave this field empty._





URI: [schema:funding](http://schema.org/funding)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Project](Project.md) | A project conducting OAE field trials or modeling |  no  |







## Properties

* Range: [MonetaryGrant](MonetaryGrant.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:funding |
| native | oae:funding |




## LinkML Source

<details>
```yaml
name: funding
description: Include the name of the funder, funder country, project title, project
  ID, and the project start and end dates. If there is no funding source (e.g., in
  the case of commercial projects), leave this field empty.
title: Funding Info
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
slot_uri: schema:funding
alias: funding
owner: Project
domain_of:
- Project
range: MonetaryGrant
multivalued: true

```
</details>