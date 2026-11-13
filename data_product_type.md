

# Slot: Data Product Type (data_product_type)


_One of the three choices: (a) Originally collected dataset (e.g., a dataset collected from a research cruise or laboratory experiment), (b) Data compilation product (e.g., SOCAT, GLODAP), or (c) Derived product (e.g., gridded products, or model output)._





URI: [oae:data_product_type](https://schema.oaedata.org/data_product_type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |







## Properties

* Range: [DataProductType](DataProductType.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:data_product_type |
| native | oae:data_product_type |




## LinkML Source

<details>
```yaml
name: data_product_type
description: 'One of the three choices: (a) Originally collected dataset (e.g., a
  dataset collected from a research cruise or laboratory experiment), (b) Data compilation
  product (e.g., SOCAT, GLODAP), or (c) Derived product (e.g., gridded products, or
  model output).'
title: Data Product Type
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: data_product_type
owner: FieldDataset
domain_of:
- FieldDataset
range: DataProductType
required: true

```
</details>