

# Slot: Magnitude of blank correction (blank_correction)


_Whether the reported variables were corrected for blank, and if so, how they were corrected._





URI: [oae:blank_correction](https://schema.oaedata.org/blank_correction)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiscreteDICVariable](DiscreteDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle sampl... |  no  |
| [DiscreteTAVariable](DiscreteTAVariable.md) | Total Alkalinity (TA) measured variable from discrete bottle samples |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:blank_correction |
| native | oae:blank_correction |




## LinkML Source

<details>
```yaml
name: blank_correction
description: Whether the reported variables were corrected for blank, and if so, how
  they were corrected.
title: Magnitude of blank correction
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: blank_correction
domain_of:
- DiscreteTAVariable
- DiscreteDICVariable
range: string
required: true

```
</details>