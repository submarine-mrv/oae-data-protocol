

# Slot: Model (model)


_Model number or name of the instrument._





URI: [oae:model](https://schema.oaedata.org/model)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PHInstrument](PHInstrument.md) | pH measurement instrument with dye-based calibration |  no  |
| [CRMInstrument](CRMInstrument.md) | Instrument calibrated with Certified Reference Materials, used for DIC and TA... |  no  |
| [TemperatureSensor](TemperatureSensor.md) | Temperature sensor used in continuous CO2 measurements |  no  |
| [PressureSensor](PressureSensor.md) | Pressure sensor used in continuous CO2 measurements |  no  |
| [GenericSensor](GenericSensor.md) | Generic sensor base class used in continuous CO2 measurements |  no  |
| [AnalyzingInstrument](AnalyzingInstrument.md) | Base class for scientific instruments used in analyzing samples for measureme... |  no  |
| [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector for continuous measurements, with measurement frequency |  no  |
| [CO2GasDetector](CO2GasDetector.md) | CO2 gas detector with standard gas calibration |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:model |
| native | oae:model |




## LinkML Source

<details>
```yaml
name: model
description: Model number or name of the instrument.
title: Model
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: model
domain_of:
- AnalyzingInstrument
- GenericSensor
range: string

```
</details>