

# Slot: uri



URI: [oae:uri](https://schema.oaedata.org/uri)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VocabularyItemReference](VocabularyItemReference.md) |  |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Required: True

## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NamedLink](NamedLink.md) | [url](url.md) | range | [uri](uri.md) |
| [ExternalProject](ExternalProject.md) | [related_links](related_links.md) | range | [uri](uri.md) |
| [PublicComment](PublicComment.md) | [url](url.md) | range | [uri](uri.md) |
| [Dataset](Dataset.md) | [license](license.md) | range | [uri](uri.md) |
| [Dataset](Dataset.md) | [data_access_link](data_access_link.md) | range | [uri](uri.md) |
| [FieldDataset](FieldDataset.md) | [license](license.md) | range | [uri](uri.md) |
| [FieldDataset](FieldDataset.md) | [data_access_link](data_access_link.md) | range | [uri](uri.md) |
| [ModelOutputDataset](ModelOutputDataset.md) | [license](license.md) | range | [uri](uri.md) |
| [ModelOutputDataset](ModelOutputDataset.md) | [data_access_link](data_access_link.md) | range | [uri](uri.md) |
| [Model](Model.md) | [model_configuration](model_configuration.md) | range | [uri](uri.md) |
| [ModelComponent](ModelComponent.md) | [codebase](codebase.md) | range | [uri](uri.md) |
| [ModelComponent](ModelComponent.md) | [references](references.md) | range | [uri](uri.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:uri |
| native | oae:uri |




## LinkML Source

<details>
```yaml
name: uri
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: uri
owner: VocabularyItemReference
domain_of:
- VocabularyItemReference
range: uriorcurie
required: true

```
</details>