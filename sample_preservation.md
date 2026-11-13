

# Slot: Sample preservation (sample_preservation)


_How the samples were preserved for analysis._





URI: [oae:sample_preservation](https://schema.oaedata.org/sample_preservation)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiscreteTAVariable](DiscreteTAVariable.md) | Total Alkalinity (TA) measured variable from discrete bottle samples |  no  |
| [DiscreteDICVariable](DiscreteDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle sampl... |  no  |







## Properties

* Range: [SamplePreservation](SamplePreservation.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:sample_preservation |
| native | oae:sample_preservation |




## LinkML Source

<details>
```yaml
name: sample_preservation
description: How the samples were preserved for analysis.
title: Sample preservation
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: sample_preservation
domain_of:
- DiscreteTAVariable
- DiscreteDICVariable
range: SamplePreservation
required: true

```
</details>