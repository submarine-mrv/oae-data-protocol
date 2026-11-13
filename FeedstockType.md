# Enum: FeedstockType




_Types of materials used for alkalinity addition, as sourced from NCEI's OCADS controlled vocabulary: https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/vocabularies/alkalinization-types.html_



URI: [FeedstockType](FeedstockType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| lime | PUBCHEM:14778 | Lime (CaO) used as an alkalinity source |
| portlandite | PUBCHEM:Portlandite | Portlandite (Ca(OH)₂) used as an alkalinity source |
| calcium_carbonate | PUBCHEM:10112 | Calcium carbonate (CaCO₃) used as an alkalinity source |
| anorthite | PUBCHEM:56843091 | Anorthite (CaAl₂Si₂O₈) used as an alkalinity source |
| dolomite | PUBCHEM:61833 | Dolomite (CaMg(CO₃)₂) used as an alkalinity source |
| periclase | PUBCHEM:6850729 | Periclase (MgO) used as an alkalinity source |
| brucite | PUBCHEM:14791 | Brucite (Mg(OH)₂) used as an alkalinity source |
| magnesite | PUBCHEM:11029 | Magnesite (MgCO₃) used as an alkalinity source |
| forsterite | PUBCHEM:517737 | Forsterite (Mg₂SiO₄) used as an alkalinity source |
| mg_rich_olivine | PUBCHEM:71586774 | Magnesium-rich olivine used as an alkalinity source |
| sodium_hydroxide | PUBCHEM:14798 | NaOH used as an alkalinity source |
| natrite | PUBCHEM:10340 | Natrite (Na₂CO₃) used as an alkalinity source |
| nahcolite | PUBCHEM:516892 | Nahcolite (NaHCO₃) used as an alkalinity source |
| other | None | Enter a custom value in the field provided |




## Slots

| Name | Description |
| ---  | --- |
| [alkalinity_feedstock](alkalinity_feedstock.md) | Examples may include: olivine, potassium hydroxide, magnesium hydroxide, lime... |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: FeedstockType
description: 'Types of materials used for alkalinity addition, as sourced from NCEI''s
  OCADS controlled vocabulary: https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/vocabularies/alkalinization-types.html'
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  lime:
    text: lime
    description: Lime (CaO) used as an alkalinity source.
    meaning: PUBCHEM:14778
  portlandite:
    text: portlandite
    description: Portlandite (Ca(OH)₂) used as an alkalinity source.
    meaning: PUBCHEM:Portlandite
  calcium_carbonate:
    text: calcium_carbonate
    description: Calcium carbonate (CaCO₃) used as an alkalinity source.
    meaning: PUBCHEM:10112
  anorthite:
    text: anorthite
    description: Anorthite (CaAl₂Si₂O₈) used as an alkalinity source.
    meaning: PUBCHEM:56843091
  dolomite:
    text: dolomite
    description: Dolomite (CaMg(CO₃)₂) used as an alkalinity source.
    meaning: PUBCHEM:61833
  periclase:
    text: periclase
    description: Periclase (MgO) used as an alkalinity source.
    meaning: PUBCHEM:6850729
  brucite:
    text: brucite
    description: Brucite (Mg(OH)₂) used as an alkalinity source.
    meaning: PUBCHEM:14791
  magnesite:
    text: magnesite
    description: Magnesite (MgCO₃) used as an alkalinity source.
    meaning: PUBCHEM:11029
  forsterite:
    text: forsterite
    description: Forsterite (Mg₂SiO₄) used as an alkalinity source.
    meaning: PUBCHEM:517737
  mg_rich_olivine:
    text: mg_rich_olivine
    description: Magnesium-rich olivine used as an alkalinity source.
    meaning: PUBCHEM:71586774
  sodium_hydroxide:
    text: sodium_hydroxide
    description: NaOH used as an alkalinity source.
    meaning: PUBCHEM:14798
  natrite:
    text: natrite
    description: Natrite (Na₂CO₃) used as an alkalinity source.
    meaning: PUBCHEM:10340
  nahcolite:
    text: nahcolite
    description: Nahcolite (NaHCO₃) used as an alkalinity source.
    meaning: PUBCHEM:516892
  other:
    text: other
    description: Enter a custom value in the field provided

```
</details>
