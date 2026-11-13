

# Slot: Instrument type (custom) (instrument_type_custom)



URI: [oae:instrument_type_custom](https://schema.oaedata.org/instrument_type_custom)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PHInstrument](PHInstrument.md) | pH measurement instrument with dye-based calibration |  no  |
| [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector for continuous measurements, with measurement frequency |  no  |
| [CO2GasDetector](CO2GasDetector.md) | CO2 gas detector with standard gas calibration |  no  |
| [AnalyzingInstrument](AnalyzingInstrument.md) | Base class for scientific instruments used in analyzing samples for measureme... |  no  |
| [CRMInstrument](CRMInstrument.md) | Instrument calibrated with Certified Reference Materials, used for DIC and TA... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:instrument_type_custom |
| native | oae:instrument_type_custom |




## LinkML Source

<details>
```yaml
name: instrument_type_custom
title: Instrument type (custom)
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: instrument_type_custom
owner: AnalyzingInstrument
domain_of:
- AnalyzingInstrument
range: string

```
</details>