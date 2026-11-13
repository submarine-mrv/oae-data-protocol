

# Class: ContinuousCO2GasDetector


_CO2 gas detector for continuous measurements, with measurement frequency._





URI: [oae:ContinuousCO2GasDetector](https://schema.oaedata.org/ContinuousCO2GasDetector)






```mermaid
 classDiagram
    class ContinuousCO2GasDetector
    click ContinuousCO2GasDetector href "../ContinuousCO2GasDetector"
      CO2GasDetector <|-- ContinuousCO2GasDetector
        click CO2GasDetector href "../CO2GasDetector"
      
      ContinuousCO2GasDetector : accuracy
        
      ContinuousCO2GasDetector : calibration
        
          
    
    
    ContinuousCO2GasDetector --> "1" ContinuousCO2Calibration : calibration
    click ContinuousCO2Calibration href "../ContinuousCO2Calibration"

        
      ContinuousCO2GasDetector : detector_type
        
      ContinuousCO2GasDetector : instrument_type
        
      ContinuousCO2GasDetector : instrument_type_custom
        
      ContinuousCO2GasDetector : manufacturer
        
      ContinuousCO2GasDetector : measurement_frequency
        
      ContinuousCO2GasDetector : model
        
      ContinuousCO2GasDetector : precision
        
      ContinuousCO2GasDetector : resolution
        
      ContinuousCO2GasDetector : serial_number
        
      ContinuousCO2GasDetector : uncertainty
        
      
```





## Inheritance
* [AnalyzingInstrument](AnalyzingInstrument.md)
    * [CO2GasDetector](CO2GasDetector.md)
        * **ContinuousCO2GasDetector**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [measurement_frequency](measurement_frequency.md) | 0..1 <br/> [String](String.md) | How often measurements are taken, e | direct |
| [calibration](calibration.md) | 1 <br/> [ContinuousCO2Calibration](ContinuousCO2Calibration.md) | CO2 calibration information for this continuous instrument | direct |
| [detector_type](detector_type.md) | 1 <br/> [String](String.md) | Type of the CO2 gas detector (E | [CO2GasDetector](CO2GasDetector.md) |
| [resolution](resolution.md) | 0..1 <br/> [String](String.md) | Resolution of the CO2 sensor | [CO2GasDetector](CO2GasDetector.md) |
| [uncertainty](uncertainty.md) | 0..1 <br/> [String](String.md) | Uncertainty of the CO2 sensor | [CO2GasDetector](CO2GasDetector.md) |
| [manufacturer](manufacturer.md) | 1 <br/> [String](String.md) | Manufacture of the CO2 sensor | [AnalyzingInstrument](AnalyzingInstrument.md) |
| [model](model.md) | 0..1 <br/> [String](String.md) | Model number of the CO2 sensor, e | [AnalyzingInstrument](AnalyzingInstrument.md) |
| [instrument_type](instrument_type.md) | 1 <br/> [String](String.md) | Type of instrument used to analyze samples or measure continuously | [AnalyzingInstrument](AnalyzingInstrument.md) |
| [instrument_type_custom](instrument_type_custom.md) | 0..1 <br/> [String](String.md) |  | [AnalyzingInstrument](AnalyzingInstrument.md) |
| [serial_number](serial_number.md) | 0..1 <br/> [String](String.md) | Serial number of the instrument | [AnalyzingInstrument](AnalyzingInstrument.md) |
| [precision](precision.md) | 0..1 <br/> [String](String.md) | Precision of the instrument measurements | [AnalyzingInstrument](AnalyzingInstrument.md) |
| [accuracy](accuracy.md) | 1 <br/> [String](String.md) | Accuracy of the instrument measurements | [AnalyzingInstrument](AnalyzingInstrument.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ContinuousCO2Variable](ContinuousCO2Variable.md) | [analyzing_instrument](analyzing_instrument.md) | range | [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:ContinuousCO2GasDetector |
| native | oae:ContinuousCO2GasDetector |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ContinuousCO2GasDetector
description: CO2 gas detector for continuous measurements, with measurement frequency.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: CO2GasDetector
attributes:
  measurement_frequency:
    name: measurement_frequency
    description: How often measurements are taken, e.g., every 140 seconds except
      during calibration.
    title: Measurement frequency
    from_schema: Instrument
    rank: 1000
    domain_of:
    - ContinuousCO2GasDetector
    range: string
  calibration:
    name: calibration
    description: CO2 calibration information for this continuous instrument.
    title: Calibration
    from_schema: Instrument
    domain_of:
    - AnalyzingInstrument
    - PHInstrument
    - CRMInstrument
    - CO2GasDetector
    - ContinuousCO2GasDetector
    - GenericSensor
    range: ContinuousCO2Calibration
    required: true

```
</details>

### Induced

<details>
```yaml
name: ContinuousCO2GasDetector
description: CO2 gas detector for continuous measurements, with measurement frequency.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: CO2GasDetector
attributes:
  measurement_frequency:
    name: measurement_frequency
    description: How often measurements are taken, e.g., every 140 seconds except
      during calibration.
    title: Measurement frequency
    from_schema: Instrument
    rank: 1000
    alias: measurement_frequency
    owner: ContinuousCO2GasDetector
    domain_of:
    - ContinuousCO2GasDetector
    range: string
  calibration:
    name: calibration
    description: CO2 calibration information for this continuous instrument.
    title: Calibration
    from_schema: Instrument
    alias: calibration
    owner: ContinuousCO2GasDetector
    domain_of:
    - AnalyzingInstrument
    - PHInstrument
    - CRMInstrument
    - CO2GasDetector
    - ContinuousCO2GasDetector
    - GenericSensor
    range: ContinuousCO2Calibration
    required: true
  detector_type:
    name: detector_type
    description: Type of the CO2 gas detector (E.g., Infrared)
    title: Detector Type
    from_schema: Instrument
    rank: 1000
    alias: detector_type
    owner: ContinuousCO2GasDetector
    domain_of:
    - CO2GasDetector
    range: string
    required: true
  resolution:
    name: resolution
    description: Resolution of the CO2 sensor.
    title: Resolution
    from_schema: Instrument
    rank: 1000
    alias: resolution
    owner: ContinuousCO2GasDetector
    domain_of:
    - CO2GasDetector
    range: string
  uncertainty:
    name: uncertainty
    description: Uncertainty of the CO2 sensor.
    title: Uncertainty
    from_schema: Instrument
    alias: uncertainty
    owner: ContinuousCO2GasDetector
    domain_of:
    - StandardGas
    - CO2GasDetector
    - QCFields
    range: string
  manufacturer:
    name: manufacturer
    description: Manufacture of the CO2 sensor
    title: Manufacturer
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: manufacturer
    owner: ContinuousCO2GasDetector
    domain_of:
    - StandardGas
    - AnalyzingInstrument
    - GenericSensor
    range: string
    required: true
  model:
    name: model
    description: Model number of the CO2 sensor, e.g., 6262
    title: Model
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: model
    owner: ContinuousCO2GasDetector
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: string
  instrument_type:
    name: instrument_type
    description: Type of instrument used to analyze samples or measure continuously.
    title: Instrument type
    from_schema: Instrument
    rank: 1000
    alias: instrument_type
    owner: ContinuousCO2GasDetector
    domain_of:
    - AnalyzingInstrument
    range: string
    required: true
    equals_string: gas_analyzer
  instrument_type_custom:
    name: instrument_type_custom
    title: Instrument type (custom)
    from_schema: Instrument
    rank: 1000
    alias: instrument_type_custom
    owner: ContinuousCO2GasDetector
    domain_of:
    - AnalyzingInstrument
    range: string
  serial_number:
    name: serial_number
    description: Serial number of the instrument.
    title: Serial number
    from_schema: Instrument
    rank: 1000
    alias: serial_number
    owner: ContinuousCO2GasDetector
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: string
  precision:
    name: precision
    description: Precision of the instrument measurements.
    title: Precision
    from_schema: Instrument
    rank: 1000
    alias: precision
    owner: ContinuousCO2GasDetector
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: string
  accuracy:
    name: accuracy
    description: Accuracy of the instrument measurements.
    title: Accuracy
    from_schema: Instrument
    rank: 1000
    alias: accuracy
    owner: ContinuousCO2GasDetector
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: string
    required: true

```
</details>