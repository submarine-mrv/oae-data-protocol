

# Class: GenericSensor


_Generic sensor base class used in continuous CO2 measurements. Subclasses (e.g., TemperatureSensor, PressureSensor) specialize accuracy and precision units via slot_usage._





URI: [oae:GenericSensor](https://schema.oaedata.org/GenericSensor)






```mermaid
 classDiagram
    class GenericSensor
    click GenericSensor href "../GenericSensor"
      GenericSensor <|-- TemperatureSensor
        click TemperatureSensor href "../TemperatureSensor"
      GenericSensor <|-- PressureSensor
        click PressureSensor href "../PressureSensor"
      
      GenericSensor : accuracy
        
      GenericSensor : calibration
        
      GenericSensor : comments
        
      GenericSensor : location
        
      GenericSensor : manufacturer
        
      GenericSensor : model
        
      GenericSensor : precision
        
      GenericSensor : serial_number
        
      
```





## Inheritance
* **GenericSensor**
    * [TemperatureSensor](TemperatureSensor.md)
    * [PressureSensor](PressureSensor.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [location](location.md) | 0..1 <br/> [String](String.md) | Location of the sensor | direct |
| [manufacturer](manufacturer.md) | 0..1 <br/> [String](String.md) | Manufacturer of the sensor | direct |
| [model](model.md) | 0..1 <br/> [String](String.md) | Model number of the sensor | direct |
| [serial_number](serial_number.md) | 0..1 <br/> [String](String.md) | Serial number of the sensor | direct |
| [accuracy](accuracy.md) | 0..1 <br/> [Float](Float.md) | Accuracy of the sensor | direct |
| [precision](precision.md) | 0..1 <br/> [Float](Float.md) | Precision of the sensor | direct |
| [calibration](calibration.md) | 0..1 <br/> [String](String.md) | Calibration information for the sensor | direct |
| [comments](comments.md) | 0..1 <br/> [String](String.md) | Additional comments about the sensor | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:GenericSensor |
| native | oae:GenericSensor |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GenericSensor
description: Generic sensor base class used in continuous CO2 measurements. Subclasses
  (e.g., TemperatureSensor, PressureSensor) specialize accuracy and precision units
  via slot_usage.
from_schema: https://schema.oaedata.org/OAEDataSchema
attributes:
  location:
    name: location
    description: Location of the sensor.
    title: Location
    from_schema: Instrument
    rank: 1000
    domain_of:
    - GenericSensor
    range: string
  manufacturer:
    name: manufacturer
    description: Manufacturer of the sensor.
    title: Manufacturer
    from_schema: Instrument
    domain_of:
    - StandardGas
    - AnalyzingInstrument
    - GenericSensor
    range: string
  model:
    name: model
    description: Model number of the sensor.
    title: Model
    from_schema: Instrument
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: string
  serial_number:
    name: serial_number
    description: Serial number of the sensor.
    title: Serial number
    from_schema: Instrument
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: string
  accuracy:
    name: accuracy
    description: Accuracy of the sensor.
    title: Accuracy
    from_schema: Instrument
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: float
  precision:
    name: precision
    description: Precision of the sensor.
    title: Precision
    from_schema: Instrument
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: float
  calibration:
    name: calibration
    description: Calibration information for the sensor.
    title: Calibration
    from_schema: Instrument
    domain_of:
    - AnalyzingInstrument
    - PHInstrument
    - CRMInstrument
    - CO2GasDetector
    - ContinuousCO2GasDetector
    - GenericSensor
    range: string
  comments:
    name: comments
    description: Additional comments about the sensor.
    title: Comments
    from_schema: Instrument
    rank: 1000
    domain_of:
    - GenericSensor
    range: string

```
</details>

### Induced

<details>
```yaml
name: GenericSensor
description: Generic sensor base class used in continuous CO2 measurements. Subclasses
  (e.g., TemperatureSensor, PressureSensor) specialize accuracy and precision units
  via slot_usage.
from_schema: https://schema.oaedata.org/OAEDataSchema
attributes:
  location:
    name: location
    description: Location of the sensor.
    title: Location
    from_schema: Instrument
    rank: 1000
    alias: location
    owner: GenericSensor
    domain_of:
    - GenericSensor
    range: string
  manufacturer:
    name: manufacturer
    description: Manufacturer of the sensor.
    title: Manufacturer
    from_schema: Instrument
    alias: manufacturer
    owner: GenericSensor
    domain_of:
    - StandardGas
    - AnalyzingInstrument
    - GenericSensor
    range: string
  model:
    name: model
    description: Model number of the sensor.
    title: Model
    from_schema: Instrument
    alias: model
    owner: GenericSensor
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: string
  serial_number:
    name: serial_number
    description: Serial number of the sensor.
    title: Serial number
    from_schema: Instrument
    alias: serial_number
    owner: GenericSensor
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: string
  accuracy:
    name: accuracy
    description: Accuracy of the sensor.
    title: Accuracy
    from_schema: Instrument
    alias: accuracy
    owner: GenericSensor
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: float
  precision:
    name: precision
    description: Precision of the sensor.
    title: Precision
    from_schema: Instrument
    alias: precision
    owner: GenericSensor
    domain_of:
    - AnalyzingInstrument
    - GenericSensor
    range: float
  calibration:
    name: calibration
    description: Calibration information for the sensor.
    title: Calibration
    from_schema: Instrument
    alias: calibration
    owner: GenericSensor
    domain_of:
    - AnalyzingInstrument
    - PHInstrument
    - CRMInstrument
    - CO2GasDetector
    - ContinuousCO2GasDetector
    - GenericSensor
    range: string
  comments:
    name: comments
    description: Additional comments about the sensor.
    title: Comments
    from_schema: Instrument
    rank: 1000
    alias: comments
    owner: GenericSensor
    domain_of:
    - GenericSensor
    range: string

```
</details>