# Enum: DataProductType



URI: [DataProductType](DataProductType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| originally_collected_dataset | None | A dataset collected from a research cruise or laboratory experiment |
| data_compilation_product | None | (e |
| derived_product | None | (e |




## Slots

| Name | Description |
| ---  | --- |
| [data_product_type](data_product_type.md) | One of the three choices: (a) Originally collected dataset (e |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: DataProductType
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  originally_collected_dataset:
    text: originally_collected_dataset
    description: A dataset collected from a research cruise or laboratory experiment
  data_compilation_product:
    text: data_compilation_product
    description: (e.g., SOCAT, GLODAP)
  derived_product:
    text: derived_product
    description: (e.g. gridded products, or model output).

```
</details>
