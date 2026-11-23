

# Class: PHInstrument


_pH measurement instrument with dye-based calibration._





URI: [oae:PHInstrument](https://schema.oaedata.org/PHInstrument)






```mermaid
 classDiagram
    class PHInstrument
    click PHInstrument href "../PHInstrument"
      AnalyzingInstrument <|-- PHInstrument
        click AnalyzingInstrument href "../AnalyzingInstrument"
      
      PHInstrument : accuracy
        
      PHInstrument : calibration
        
          
    
    
    PHInstrument --> "1" Any : calibration
    click Any href "../Any"

        
      PHInstrument : instrument_type
        
          
    
    
    PHInstrument --> "1" AnalyzingInstrumentType : instrument_type
    click AnalyzingInstrumentType href "../AnalyzingInstrumentType"

        
      PHInstrument : instrument_type_custom
        
      PHInstrument : manufacturer
        
      PHInstrument : model
        
      PHInstrument : precision
        
      PHInstrument : serial_number
        
      
```





## Inheritance
* [AnalyzingInstrument](AnalyzingInstrument.md)
    * **PHInstrument**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [calibration](calibration.md) | 1 <br/> [Any](Any.md)&nbsp;or&nbsp;<br />[DyeCalibration](DyeCalibration.md)&nbsp;or&nbsp;<br />[PHCalibration](PHCalibration.md) | pH calibration information for this instrument | direct |
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
| [DiscretePHVariable](DiscretePHVariable.md) | [analyzing_instrument](analyzing_instrument.md) | range | [PHInstrument](PHInstrument.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:PHInstrument |
| native | oae:PHInstrument |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PHInstrument
description: pH measurement instrument with dye-based calibration.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: AnalyzingInstrument
attributes:
  calibration:
    name: calibration
    description: pH calibration information for this instrument.
    title: Calibration
    from_schema: Instrument
    domain_of:
    - AnalyzingInstrument
    - PHInstrument
    - CRMInstrument
    - CO2GasDetector
    - ContinuousCO2GasDetector
    - GenericSensor
    range: Any
    required: true
    any_of:
    - range: DyeCalibration
    - range: PHCalibration

```
</details>

### Induced

<details>
```yaml
name: PHInstrument
description: pH measurement instrument with dye-based calibration.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: AnalyzingInstrument
attributes:
  calibration:
    name: calibration
    description: pH calibration information for this instrument.
    title: Calibration
    from_schema: Instrument
    alias: calibration
    owner: PHInstrument
    domain_of:
    - AnalyzingInstrument
    - PHInstrument
    - CRMInstrument
    - CO2GasDetector
    - ContinuousCO2GasDetector
    - GenericSensor
    range: Any
    required: true
    any_of:
    - range: DyeCalibration
    - range: PHCalibration
  manufacturer:
    name: manufacturer
    description: Manufacturer name of the instrument.
    title: Manufacturer
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: manufacturer
    owner: PHInstrument
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
    owner: PHInstrument
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
    owner: PHInstrument
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
    owner: PHInstrument
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
    owner: PHInstrument
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
    owner: PHInstrument
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
    owner: PHInstrument
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: string
    required: true

```
</details>