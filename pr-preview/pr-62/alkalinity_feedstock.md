

# Slot: Alkalinity Feedstock (alkalinity_feedstock)


_Examples may include: olivine, potassium hydroxide, magnesium hydroxide, lime, portlandite, calcium carbonate, anorthite, dolomite, periclase, brucite, magnesite, forsterite, sodium hydroxide, natrite, nahcolite, akermanite, akermanite, alunoakermanite, etc._

_See Controlled Vocabularies section for selected examples (this list is not exhaustive, you may need to include your unique feedstock)._





URI: [oae:alkalinity_feedstock](https://schema.oaedata.org/alkalinity_feedstock)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [InterventionDetails](InterventionDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |







## Properties

* Range: [FeedstockType](FeedstockType.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:alkalinity_feedstock |
| native | oae:alkalinity_feedstock |




## LinkML Source

<details>
```yaml
name: alkalinity_feedstock
description: 'Examples may include: olivine, potassium hydroxide, magnesium hydroxide,
  lime, portlandite, calcium carbonate, anorthite, dolomite, periclase, brucite, magnesite,
  forsterite, sodium hydroxide, natrite, nahcolite, akermanite, akermanite, alunoakermanite,
  etc.

  See Controlled Vocabularies section for selected examples (this list is not exhaustive,
  you may need to include your unique feedstock).'
title: Alkalinity Feedstock
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: alkalinity_feedstock
owner: InterventionDetails
domain_of:
- InterventionDetails
range: FeedstockType
required: true

```
</details>