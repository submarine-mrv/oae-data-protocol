

# Slot: Tracer Form (tracer_form)


_The form of tracer upon delivery to the ocean (e.g. gas or dye-release)_





URI: [oae:tracer_form](https://schema.oaedata.org/tracer_form)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [TracerDetails](TracerDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |







## Properties

* Range: [TracerForm](TracerForm.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:tracer_form |
| native | oae:tracer_form |




## LinkML Source

<details>
```yaml
name: tracer_form
description: The form of tracer upon delivery to the ocean (e.g. gas or dye-release)
title: Tracer Form
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: tracer_form
owner: TracerDetails
domain_of:
- TracerDetails
range: TracerForm
required: true

```
</details>