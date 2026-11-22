

# Slot: Alkalinity Feedstock CO₂ Removal Potential (alkalinity_feedstock_co2_removal_potential)


_Maximum CO₂ removal potential of a feedstock material. We recommend using an adjusted version of the Steinour equation (Gunning et al., 2010), which uses bulk elemental oxide composition to estimate the maximum CO₂ removal potential of a feedstock material. The calculation output is in the form of kg of CO₂ per tonne of feedstock and represents the quantitative hypothetical potential of the material to capture CO₂ as bicarbonate or carbonate. See Isometric's CO2 removal potential module for details._





URI: [oae:alkalinity_feedstock_co2_removal_potential](https://schema.oaedata.org/alkalinity_feedstock_co2_removal_potential)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [InterventionDetails](InterventionDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |







## Properties

* Range: [Float](Float.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:alkalinity_feedstock_co2_removal_potential |
| native | oae:alkalinity_feedstock_co2_removal_potential |




## LinkML Source

<details>
```yaml
name: alkalinity_feedstock_co2_removal_potential
description: Maximum CO₂ removal potential of a feedstock material. We recommend using
  an adjusted version of the Steinour equation (Gunning et al., 2010), which uses
  bulk elemental oxide composition to estimate the maximum CO₂ removal potential of
  a feedstock material. The calculation output is in the form of kg of CO₂ per tonne
  of feedstock and represents the quantitative hypothetical potential of the material
  to capture CO₂ as bicarbonate or carbonate. See Isometric's CO2 removal potential
  module for details.
title: Alkalinity Feedstock CO₂ Removal Potential
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: alkalinity_feedstock_co2_removal_potential
owner: InterventionDetails
domain_of:
- InterventionDetails
range: float
required: true

```
</details>