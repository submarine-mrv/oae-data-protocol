

# Slot: Manufacturer (manufacturer)


_Manufacturer name of the instrument._





URI: [oae:manufacturer](https://schema.oaedata.org/manufacturer)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericSensor](GenericSensor.md) | Generic sensor base class used in continuous CO2 measurements |  no  |
| [PressureSensor](PressureSensor.md) | Pressure sensor used in continuous CO2 measurements |  no  |
| [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector for continuous measurements, with measurement frequency |  no  |
| [CO2GasDetector](CO2GasDetector.md) | CO2 gas detector with standard gas calibration |  yes  |
| [StandardGas](StandardGas.md) | Standard gas used for CO2 calibration |  no  |
| [AnalyzingInstrument](AnalyzingInstrument.md) | Base class for scientific instruments used in analyzing samples for measureme... |  no  |
| [ContinuousStandardGas](ContinuousStandardGas.md) | Standard gas used for continuous CO2 calibration, with additional traceabilit... |  no  |
| [PHInstrument](PHInstrument.md) | pH measurement instrument with dye-based calibration |  no  |
| [CRMInstrument](CRMInstrument.md) | Instrument calibrated with Certified Reference Materials, used for DIC and TA... |  no  |
| [TemperatureSensor](TemperatureSensor.md) | Temperature sensor used in continuous CO2 measurements |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:manufacturer |
| native | oae:manufacturer |




## LinkML Source

<details>
```yaml
name: manufacturer
description: Manufacturer name of the instrument.
title: Manufacturer
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: manufacturer
domain_of:
- StandardGas
- AnalyzingInstrument
- GenericSensor
range: string

```
</details>