

# Slot: Location (location)


_Location of the sensor._





URI: [oae:location](https://schema.oaedata.org/location)



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
| self | oae:location |
| native | oae:location |




## LinkML Source

<details>
```yaml
name: location
description: Location of the sensor.
title: Location
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: location
owner: GenericSensor
domain_of:
- GenericSensor
range: string

```
</details>