

# Slot: Previous or Ongoing Co-located Research (previous_or_ongoing_colocated_research)


_This field is required for co-located operations that potentially impact the project results. If previous or on-going mCDR field operations have occurred in the study domain by any project developer, they may be mentioned here either as a description, and/or if a reference to the study exists in the form of a data set, publication, etc, the DOI or other identifying information should be provided. Please provide direct links to data when available._





URI: [oae:previous_or_ongoing_colocated_research](https://schema.oaedata.org/previous_or_ongoing_colocated_research)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Project](Project.md) | A project conducting OAE field trials or modeling |  no  |







## Properties

* Range: [ExternalProject](ExternalProject.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:previous_or_ongoing_colocated_research |
| native | oae:previous_or_ongoing_colocated_research |




## LinkML Source

<details>
```yaml
name: previous_or_ongoing_colocated_research
description: This field is required for co-located operations that potentially impact
  the project results. If previous or on-going mCDR field operations have occurred
  in the study domain by any project developer, they may be mentioned here either
  as a description, and/or if a reference to the study exists in the form of a data
  set, publication, etc, the DOI or other identifying information should be provided.
  Please provide direct links to data when available.
title: Previous or Ongoing Co-located Research
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: previous_or_ongoing_colocated_research
owner: Project
domain_of:
- Project
range: ExternalProject
multivalued: true

```
</details>