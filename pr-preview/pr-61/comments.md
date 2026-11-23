

# Slot: Comments (comments)


_Additional comments about the sensor._





URI: [oae:comments](https://schema.oaedata.org/comments)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PressureSensor](PressureSensor.md) | Pressure sensor used in continuous CO2 measurements |  no  |
| [GenericSensor](GenericSensor.md) | Generic sensor base class used in continuous CO2 measurements |  no  |
| [TemperatureSensor](TemperatureSensor.md) | Temperature sensor used in continuous CO2 measurements |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:comments |
| native | oae:comments |




## LinkML Source

<details>
```yaml
name: comments
description: Additional comments about the sensor.
title: Comments
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: comments
owner: GenericSensor
domain_of:
- GenericSensor
range: string

```
</details>