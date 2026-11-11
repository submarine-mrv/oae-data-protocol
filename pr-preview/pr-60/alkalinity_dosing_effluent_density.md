

# Slot: Alkalinity Dosing Effluent Density (alkalinity_dosing_effluent_density)


_Fixed density or provide link/source to effluent density data if applicable. Please include whether density is directly measured or a derived value. If this is a variable included with your data, please note so here as 'alkalinity dosing effluent density is provided as a variable' and use 'dosing_effluent_density' for your column header name._





URI: [oae:alkalinity_dosing_effluent_density](https://schema.oaedata.org/alkalinity_dosing_effluent_density)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterventionDetails](InterventionDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |







## Properties

* Range: [DosingConcentration](DosingConcentration.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:alkalinity_dosing_effluent_density |
| native | oae:alkalinity_dosing_effluent_density |




## LinkML Source

<details>
```yaml
name: alkalinity_dosing_effluent_density
description: Fixed density or provide link/source to effluent density data if applicable.
  Please include whether density is directly measured or a derived value. If this
  is a variable included with your data, please note so here as 'alkalinity dosing
  effluent density is provided as a variable' and use 'dosing_effluent_density' for
  your column header name.
title: Alkalinity Dosing Effluent Density
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: alkalinity_dosing_effluent_density
owner: InterventionDetails
domain_of:
- InterventionDetails
range: DosingConcentration
required: true

```
</details>