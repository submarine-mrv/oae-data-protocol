# Enum: DataAccessibility




_Level of access to a dataset._



URI: [DataAccessibility](DataAccessibility.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| open_access | None | Data are freely available now, without restriction |
| conditional_access | None | Data are available upon request, subject to review |
| scheduled_access | None | Data will become openly available after a specified date |




## Slots

| Name | Description |
| ---  | --- |
| [data_accessibility](data_accessibility.md) | Level of access to this dataset |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: DataAccessibility
description: Level of access to a dataset.
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  open_access:
    text: open_access
    description: Data are freely available now, without restriction.
    title: Open Access
  conditional_access:
    text: conditional_access
    description: Data are available upon request, subject to review.
    title: Conditional Access
  scheduled_access:
    text: scheduled_access
    description: Data will become openly available after a specified date.
    title: Scheduled Access

```
</details>
