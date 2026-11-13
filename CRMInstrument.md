

# Class: CRMInstrument


_Instrument calibrated with Certified Reference Materials, used for DIC and TA measurements._





URI: [oae:CRMInstrument](https://schema.oaedata.org/CRMInstrument)






```mermaid
 classDiagram
    class CRMInstrument
    click CRMInstrument href "../CRMInstrument"
      AnalyzingInstrument <|-- CRMInstrument
        click AnalyzingInstrument href "../AnalyzingInstrument"
      
      CRMInstrument : accuracy
        
      CRMInstrument : calibration
        
          
    
    
    CRMInstrument --> "1" CRMCalibration : calibration
    click CRMCalibration href "../CRMCalibration"

        
      CRMInstrument : instrument_type
        
          
    
    
    CRMInstrument --> "1" AnalyzingInstrumentType : instrument_type
    click AnalyzingInstrumentType href "../AnalyzingInstrumentType"

        
      CRMInstrument : instrument_type_custom
        
      CRMInstrument : manufacturer
        
      CRMInstrument : model
        
      CRMInstrument : precision
        
      CRMInstrument : serial_number
        
      
```





## Inheritance
* [AnalyzingInstrument](AnalyzingInstrument.md)
    * **CRMInstrument**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [calibration](calibration.md) | 1 <br/> [CRMCalibration](CRMCalibration.md) | CRM calibration information for this instrument | direct |
| [manufacturer](manufacturer.md) | 0..1 <br/> [String](String.md) | Manufacturer name of the instrument | [AnalyzingInstrument](AnalyzingInstrument.md) |
| [model](model.md) | 0..1 <br/> [String](String.md) | Model number or name of the instrument | [AnalyzingInstrument](AnalyzingInstrument.md) |
| [instrument_type](instrument_type.md) | 1 <br/> [AnalyzingInstrumentType](AnalyzingInstrumentType.md) | Type of instrument used to analyze samples or measure continuously | [AnalyzingInstrument](AnalyzingInstrument.md) |
| [instrument_type_custom](instrument_type_custom.md) | 0..1 <br/> [String](String.md) |  | [AnalyzingInstrument](AnalyzingInstrument.md) |
| [serial_number](serial_number.md) | 0..1 <br/> [String](String.md) | Serial number of the instrument | [AnalyzingInstrument](AnalyzingInstrument.md) |
| [precision](precision.md) | 0..1 <br/> [String](String.md) | Precision of the instrument measurements | [AnalyzingInstrument](AnalyzingInstrument.md) |
| [accuracy](accuracy.md) | 1 <br/> [String](String.md) | Accuracy of the instrument measurements | [AnalyzingInstrument](AnalyzingInstrument.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DiscreteTAVariable](DiscreteTAVariable.md) | [analyzing_instrument](analyzing_instrument.md) | range | [CRMInstrument](CRMInstrument.md) |
| [DiscreteDICVariable](DiscreteDICVariable.md) | [analyzing_instrument](analyzing_instrument.md) | range | [CRMInstrument](CRMInstrument.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:CRMInstrument |
| native | oae:CRMInstrument |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CRMInstrument
description: Instrument calibrated with Certified Reference Materials, used for DIC
  and TA measurements.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: AnalyzingInstrument
attributes:
  calibration:
    name: calibration
    description: CRM calibration information for this instrument.
    title: Calibration
    from_schema: Instrument
    domain_of:
    - AnalyzingInstrument
    - PHInstrument
    - CRMInstrument
    - CO2GasDetector
    - ContinuousCO2GasDetector
    - GenericSensor
    range: CRMCalibration
    required: true

```
</details>

### Induced

<details>
```yaml
name: CRMInstrument
description: Instrument calibrated with Certified Reference Materials, used for DIC
  and TA measurements.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: AnalyzingInstrument
attributes:
  calibration:
    name: calibration
    description: CRM calibration information for this instrument.
    title: Calibration
    from_schema: Instrument
    alias: calibration
    owner: CRMInstrument
    domain_of:
    - AnalyzingInstrument
    - PHInstrument
    - CRMInstrument
    - CO2GasDetector
    - ContinuousCO2GasDetector
    - GenericSensor
    range: CRMCalibration
    required: true
  manufacturer:
    name: manufacturer
    description: Manufacturer name of the instrument.
    title: Manufacturer
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: manufacturer
    owner: CRMInstrument
    domain_of:
    - StandardGas
    - AnalyzingInstrument
    - GenericSensor
    range: string
  model:
    name: model
    description: Model number or name of the instrument.
    title: Model
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: model
    owner: CRMInstrument
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
    owner: CRMInstrument
    domain_of:
    - AnalyzingInstrument
    range: AnalyzingInstrumentType
    required: true
  instrument_type_custom:
    name: instrument_type_custom
    title: Instrument type (custom)
    from_schema: Instrument
    rank: 1000
    alias: instrument_type_custom
    owner: CRMInstrument
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
    owner: CRMInstrument
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
    owner: CRMInstrument
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
    owner: CRMInstrument
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: string
    required: true

```
</details>