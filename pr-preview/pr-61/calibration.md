

# Slot: calibration



URI: [oae:calibration](https://schema.oaedata.org/calibration)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PressureSensor](PressureSensor.md) | Pressure sensor used in continuous CO2 measurements |  no  |
| [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector for continuous measurements, with measurement frequency |  no  |
| [CRMInstrument](CRMInstrument.md) | Instrument calibrated with Certified Reference Materials, used for DIC and TA... |  no  |
| [CO2GasDetector](CO2GasDetector.md) | CO2 gas detector with standard gas calibration |  no  |
| [TemperatureSensor](TemperatureSensor.md) | Temperature sensor used in continuous CO2 measurements |  no  |
| [GenericSensor](GenericSensor.md) | Generic sensor base class used in continuous CO2 measurements |  no  |
| [AnalyzingInstrument](AnalyzingInstrument.md) | Base class for scientific instruments used in analyzing samples for measureme... |  no  |
| [PHInstrument](PHInstrument.md) | pH measurement instrument with dye-based calibration |  no  |







## Properties

* Range: NONE





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:calibration |
| native | oae:calibration |




## LinkML Source

<details>
```yaml
name: calibration
alias: calibration
domain_of:
- AnalyzingInstrument
- PHInstrument
- CRMInstrument
- CO2GasDetector
- ContinuousCO2GasDetector
- GenericSensor

```
</details>