

# Slot: Instrument type (instrument_type)


_Type of instrument used to analyze samples or measure continuously._





URI: [oae:instrument_type](https://schema.oaedata.org/instrument_type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector for continuous measurements, with measurement frequency |  no  |
| [CRMInstrument](CRMInstrument.md) | Instrument calibrated with Certified Reference Materials, used for DIC and TA... |  no  |
| [CO2GasDetector](CO2GasDetector.md) | CO2 gas detector with standard gas calibration |  yes  |
| [AnalyzingInstrument](AnalyzingInstrument.md) | Base class for scientific instruments used in analyzing samples for measureme... |  no  |
| [PHInstrument](PHInstrument.md) | pH measurement instrument with dye-based calibration |  no  |







## Properties

* Range: [AnalyzingInstrumentType](AnalyzingInstrumentType.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:instrument_type |
| native | oae:instrument_type |




## LinkML Source

<details>
```yaml
name: instrument_type
description: Type of instrument used to analyze samples or measure continuously.
title: Instrument type
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: instrument_type
owner: AnalyzingInstrument
domain_of:
- AnalyzingInstrument
range: AnalyzingInstrumentType
required: true

```
</details>