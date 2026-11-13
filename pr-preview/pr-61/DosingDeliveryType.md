# Enum: DosingDeliveryType




_Types of dosing delivery methods_



URI: [DosingDeliveryType](DosingDeliveryType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| static_point_source | None | A single dosing location that does not move, such as an outfall pipe from a s... |
| variable_point_source | None | A dosing location that moves: a single location at each time step, such as an... |
| static_distributed | None | A set location or locations of dosing that is not a point source, such as a d... |
| variable_distributed | None | A distributed dosing area that varies in time, such as manually placed alkali... |




## Slots

| Name | Description |
| ---  | --- |
| [dosing_delivery_type](dosing_delivery_type.md) | Type of dosing delivery method |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: DosingDeliveryType
description: Types of dosing delivery methods
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  static_point_source:
    text: static_point_source
    description: A single dosing location that does not move, such as an outfall pipe
      from a static platform. The dosing rate may change over time.
    title: Static Point Source
  variable_point_source:
    text: variable_point_source
    description: 'A dosing location that moves: a single location at each time step,
      such as an outflow from a mobile platform such as a ship or surface vessel.
      "Variable" refers to the location, not the dosing rate.'
    title: Variable Point Source
  static_distributed:
    text: static_distributed
    description: A set location or locations of dosing that is not a point source,
      such as a distributed area over the seafloor or a diffusor.
    title: Static Distributed
  variable_distributed:
    text: variable_distributed
    description: A distributed dosing area that varies in time, such as manually placed
      alkaline material over different areas at different times.
    title: Variable Distributed

```
</details>
