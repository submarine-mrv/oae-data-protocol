

# Slot: Dosing Description (dosing_description)


_Please be descriptive. Information about the dosing mechanism must be included (outflow from pipe, diffuser, doser, manual placement)_

_E.g., outflow from existing facility pipe directly to ocean, manual riverine introduction, coastal distribution at three separate 30 meter long sections, pier-based diffuser to intercoastal bay, distributed from stationary barge 10 miles offshore._





URI: [oae:dosing_description](https://schema.oaedata.org/dosing_description)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [DosingDetails](DosingDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:dosing_description |
| native | oae:dosing_description |




## LinkML Source

<details>
```yaml
name: dosing_description
description: 'Please be descriptive. Information about the dosing mechanism must be
  included (outflow from pipe, diffuser, doser, manual placement)

  E.g., outflow from existing facility pipe directly to ocean, manual riverine introduction,
  coastal distribution at three separate 30 meter long sections, pier-based diffuser
  to intercoastal bay, distributed from stationary barge 10 miles offshore.'
title: Dosing Description
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: dosing_description
owner: DosingDetails
domain_of:
- DosingDetails
range: string
required: true

```
</details>