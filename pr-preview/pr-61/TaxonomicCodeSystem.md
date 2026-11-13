# Enum: TaxonomicCodeSystem




_Taxonomic code system used for species identification._



URI: [TaxonomicCodeSystem](TaxonomicCodeSystem.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| itis | None | Integrated Taxonomic Information System |
| worms | None | World Register of Marine Species |
| col | None | Catalogue of Life |
| pbdb | None | Paleobiology Database |




## Slots

| Name | Description |
| ---  | --- |
| [taxonomic_code_system](taxonomic_code_system.md) | Which taxonomic code system the identification code refers to |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: TaxonomicCodeSystem
description: Taxonomic code system used for species identification.
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  itis:
    text: itis
    description: Integrated Taxonomic Information System
  worms:
    text: worms
    description: World Register of Marine Species
  col:
    text: col
    description: Catalogue of Life
  pbdb:
    text: pbdb
    description: Paleobiology Database

```
</details>
