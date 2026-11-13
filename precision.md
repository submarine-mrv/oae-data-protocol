

# Slot: precision



URI: [oae:precision](https://schema.oaedata.org/precision)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TemperatureSensor](TemperatureSensor.md) | Temperature sensor used in continuous CO2 measurements |  yes  |
| [PHInstrument](PHInstrument.md) | pH measurement instrument with dye-based calibration |  no  |
| [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector for continuous measurements, with measurement frequency |  no  |
| [CO2GasDetector](CO2GasDetector.md) | CO2 gas detector with standard gas calibration |  no  |
| [AnalyzingInstrument](AnalyzingInstrument.md) | Base class for scientific instruments used in analyzing samples for measureme... |  no  |
| [PressureSensor](PressureSensor.md) | Pressure sensor used in continuous CO2 measurements |  yes  |
| [GenericSensor](GenericSensor.md) | Generic sensor base class used in continuous CO2 measurements |  no  |
| [CRMInstrument](CRMInstrument.md) | Instrument calibrated with Certified Reference Materials, used for DIC and TA... |  no  |







## Properties

* Range: NONE





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:precision |
| native | oae:precision |




## LinkML Source

<details>
```yaml
name: precision
alias: precision
domain_of:
- AnalyzingInstrument
- GenericSensor

```
</details>