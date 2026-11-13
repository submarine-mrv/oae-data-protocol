

# Slot: Tracer Concentration (tracer_concentration)


_Fixed concentration or provide link/source to tracer concentration separately in the dosing file. Please include whether concentration is directly measured or a derived value. If this is a variable included with your data, please note so here as 'tracer concentration provided as a variable' and use 'tracer_concentration' for your column header name._





URI: [oae:tracer_concentration](https://schema.oaedata.org/tracer_concentration)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [TracerDetails](TracerDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |







## Properties

* Range: [DosingConcentration](DosingConcentration.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:tracer_concentration |
| native | oae:tracer_concentration |




## LinkML Source

<details>
```yaml
name: tracer_concentration
description: Fixed concentration or provide link/source to tracer concentration separately
  in the dosing file. Please include whether concentration is directly measured or
  a derived value. If this is a variable included with your data, please note so here
  as 'tracer concentration provided as a variable' and use 'tracer_concentration'
  for your column header name.
title: Tracer Concentration
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: tracer_concentration
owner: TracerDetails
domain_of:
- TracerDetails
range: DosingConcentration
required: true

```
</details>