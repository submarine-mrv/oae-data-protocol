

# Slot: accuracy



URI: [oae:accuracy](https://schema.oaedata.org/accuracy)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRMInstrument](CRMInstrument.md) | Instrument calibrated with Certified Reference Materials, used for DIC and TA... |  no  |
| [PressureSensor](PressureSensor.md) | Pressure sensor used in continuous CO2 measurements |  yes  |
| [TemperatureSensor](TemperatureSensor.md) | Temperature sensor used in continuous CO2 measurements |  yes  |
| [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector for continuous measurements, with measurement frequency |  no  |
| [PHInstrument](PHInstrument.md) | pH measurement instrument with dye-based calibration |  no  |
| [AnalyzingInstrument](AnalyzingInstrument.md) | Base class for scientific instruments used in analyzing samples for measureme... |  no  |
| [CO2GasDetector](CO2GasDetector.md) | CO2 gas detector with standard gas calibration |  no  |
| [GenericSensor](GenericSensor.md) | Generic sensor base class used in continuous CO2 measurements |  no  |







## Properties

* Range: NONE





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:accuracy |
| native | oae:accuracy |




## LinkML Source

<details>
```yaml
name: accuracy
alias: accuracy
domain_of:
- AnalyzingInstrument
- GenericSensor

```
</details>