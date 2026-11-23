# Enum: GridType




_Type of grid in a multi-grid or nested model configuration_



URI: [GridType](GridType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| inner_grid | None | Inner (nested, higher-resolution) grid |
| outer_grid | None | Outer (coarser-resolution) grid |
| single_grid | None | Single grid (no nesting) |




## Slots

| Name | Description |
| ---  | --- |
| [grid_type](grid_type.md) | Role of this grid in a nested or multi-grid configuration |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: GridType
description: Type of grid in a multi-grid or nested model configuration
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  inner_grid:
    text: inner_grid
    description: Inner (nested, higher-resolution) grid
  outer_grid:
    text: outer_grid
    description: Outer (coarser-resolution) grid
  single_grid:
    text: single_grid
    description: Single grid (no nesting)

```
</details>
