

# Slot: QC Flag Scheme (qc_flag_scheme)


_Describe what the quality control flags stand for, e.g.,_

_  0 = interpolated or calculated data_

_  1 = not evaluated/quality unknown_

_  2 = acceptable_

_  3 = questionable_

_  4 = known bad_

_  6 = median of replicates_

_  9 = missing value"_





URI: [oae:qc_flag_scheme](https://schema.oaedata.org/qc_flag_scheme)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:qc_flag_scheme |
| native | oae:qc_flag_scheme |




## LinkML Source

<details>
```yaml
name: qc_flag_scheme
description: "Describe what the quality control flags stand for, e.g.,\n  0 = interpolated\
  \ or calculated data\n  1 = not evaluated/quality unknown\n  2 = acceptable\n  3\
  \ = questionable\n  4 = known bad\n  6 = median of replicates\n  9 = missing value\""
title: QC Flag Scheme
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: qc_flag_scheme
owner: FieldDataset
domain_of:
- FieldDataset
range: string

```
</details>