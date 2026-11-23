

# Slot: Tracer Details (tracer_details)


_state the kind of tracer used (e.g. rhodamine, or a specific gas)_





URI: [oae:tracer_details](https://schema.oaedata.org/tracer_details)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [TracerDetails](TracerDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:tracer_details |
| native | oae:tracer_details |




## LinkML Source

<details>
```yaml
name: tracer_details
description: state the kind of tracer used (e.g. rhodamine, or a specific gas)
title: Tracer Details
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: tracer_details
owner: TracerDetails
domain_of:
- TracerDetails
range: string
required: true

```
</details>