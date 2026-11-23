

# Slot: Dosing Delivery Type (dosing_delivery_type)


_Type of dosing delivery method. See Controlled Vocabularies for definitions._





URI: [oae:dosing_delivery_type](https://schema.oaedata.org/dosing_delivery_type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [DosingDetails](DosingDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |







## Properties

* Range: [DosingDeliveryType](DosingDeliveryType.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:dosing_delivery_type |
| native | oae:dosing_delivery_type |




## LinkML Source

<details>
```yaml
name: dosing_delivery_type
description: Type of dosing delivery method. See Controlled Vocabularies for definitions.
title: Dosing Delivery Type
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: dosing_delivery_type
owner: DosingDetails
domain_of:
- DosingDetails
range: DosingDeliveryType
required: true

```
</details>