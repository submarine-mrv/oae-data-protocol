

# Slot: datasets



URI: [oae:datasets](https://schema.oaedata.org/datasets)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |







## Properties

* Range: [Any](Any.md)&nbsp;or&nbsp;<br />[Dataset](Dataset.md)&nbsp;or&nbsp;<br />[FieldDataset](FieldDataset.md)&nbsp;or&nbsp;<br />[ModelOutputDataset](ModelOutputDataset.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:datasets |
| native | oae:datasets |




## LinkML Source

<details>
```yaml
name: datasets
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: datasets
owner: Container
domain_of:
- Container
range: Any
multivalued: true
any_of:
- range: Dataset
- range: FieldDataset
- range: ModelOutputDataset

```
</details>