

# Slot: Processing code (processing_code)


_If applicable, link to any code for processing of raw forcing and input data listed in the fields above._





URI: [oae:processing_code](https://schema.oaedata.org/processing_code)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelInputDetails](ModelInputDetails.md) | Details about input data sources used to drive the model |  no  |







## Properties

* Range: [NamedLink](NamedLink.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:processing_code |
| native | oae:processing_code |




## LinkML Source

<details>
```yaml
name: processing_code
description: If applicable, link to any code for processing of raw forcing and input
  data listed in the fields above.
title: Processing code
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: processing_code
owner: ModelInputDetails
domain_of:
- ModelInputDetails
range: NamedLink
multivalued: true
inlined: true
inlined_as_list: true

```
</details>