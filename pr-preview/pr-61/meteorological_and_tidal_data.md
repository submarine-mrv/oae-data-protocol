

# Slot: Meteorological and Tidal Data (meteorological_and_tidal_data)


_Include links to relevant open datasets if referenced in the experiment but not provided in the submission._





URI: [oae:meteorological_and_tidal_data](https://schema.oaedata.org/meteorological_and_tidal_data)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc |  no  |







## Properties

* Range: [NamedLink](NamedLink.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:meteorological_and_tidal_data |
| native | oae:meteorological_and_tidal_data |




## LinkML Source

<details>
```yaml
name: meteorological_and_tidal_data
description: Include links to relevant open datasets if referenced in the experiment
  but not provided in the submission.
title: Meteorological and Tidal Data
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: meteorological_and_tidal_data
owner: InSituExperiment
domain_of:
- InSituExperiment
range: NamedLink
multivalued: true
inlined: true
inlined_as_list: true

```
</details>