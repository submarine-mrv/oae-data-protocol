

# Slot: Permits (permits)


_Associated permit number(s)._





URI: [oae:permits](https://schema.oaedata.org/permits)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc |  no  |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |







## Properties

* Range: [Permit](Permit.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:permits |
| native | oae:permits |




## LinkML Source

<details>
```yaml
name: permits
description: Associated permit number(s).
title: Permits
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: permits
domain_of:
- InSituExperiment
range: Permit
multivalued: true
inlined: true
inlined_as_list: true

```
</details>