

# Slot: Temporal Coverage (temporal_coverage)


_Start date and end date (if known) of the project in ISO-8601 interval format (YYYY-MM-DD/YYY-MM-DD). If the end date is not known, use open-ended format YYYY-MM-DD/.._





URI: [schema:temporalCoverage](http://schema.org/temporalCoverage)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExternalProject](ExternalProject.md) | A research project that is not directly managed by the OAE project, but whose... |  no  |
| [Project](Project.md) | A project conducting OAE field trials or modeling |  yes  |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |







## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^\d{4}-\d{2}-\d{2}/(\d{4}-\d{2}-\d{2}|\.\.)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:temporalCoverage |
| native | oae:temporal_coverage |




## LinkML Source

<details>
```yaml
name: temporal_coverage
description: Start date and end date (if known) of the project in ISO-8601 interval
  format (YYYY-MM-DD/YYY-MM-DD). If the end date is not known, use open-ended format
  YYYY-MM-DD/..
title: Temporal Coverage
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
slot_uri: schema:temporalCoverage
alias: temporal_coverage
domain_of:
- Project
- ExternalProject
- FieldDataset
range: string
required: true
pattern: ^\d{4}-\d{2}-\d{2}/(\d{4}-\d{2}-\d{2}|\.\.)$

```
</details>