

# Class: DiscreteCO2Calibration


_CO2 calibration for discrete measurements, with calibration temperature._





URI: [oae:DiscreteCO2Calibration](https://schema.oaedata.org/DiscreteCO2Calibration)






```mermaid
 classDiagram
    class DiscreteCO2Calibration
    click DiscreteCO2Calibration href "../DiscreteCO2Calibration"
      CO2Calibration <|-- DiscreteCO2Calibration
        click CO2Calibration href "../CO2Calibration"
      
      DiscreteCO2Calibration : calibration_certificates
        
      DiscreteCO2Calibration : calibration_location
        
          
    
    
    DiscreteCO2Calibration --> "0..1" CalibrationLocation : calibration_location
    click CalibrationLocation href "../CalibrationLocation"

        
      DiscreteCO2Calibration : calibration_temperature
        
      DiscreteCO2Calibration : frequency
        
      DiscreteCO2Calibration : last_calibration_date
        
      DiscreteCO2Calibration : method_reference
        
      DiscreteCO2Calibration : standard_gas_info
        
          
    
    
    DiscreteCO2Calibration --> "0..1" StandardGas : standard_gas_info
    click StandardGas href "../StandardGas"

        
      DiscreteCO2Calibration : technique_description
        
      
```





## Inheritance
* [Calibration](Calibration.md)
    * [CO2Calibration](CO2Calibration.md)
        * **DiscreteCO2Calibration**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [calibration_temperature](calibration_temperature.md) | 0..1 <br/> [String](String.md) | Temperature at which calibration was performed | direct |
| [standard_gas_info](standard_gas_info.md) | 0..1 <br/> [StandardGas](StandardGas.md) | Standard gases used for calibration | [CO2Calibration](CO2Calibration.md) |
| [calibration_location](calibration_location.md) | 0..1 <br/> [CalibrationLocation](CalibrationLocation.md) | Factory calibration, lab calibration, or field calibration | [Calibration](Calibration.md) |
| [technique_description](technique_description.md) | 1 <br/> [String](String.md) | Details of the calibration technique used | [Calibration](Calibration.md) |
| [method_reference](method_reference.md) | 0..1 <br/> [String](String.md) | Citation or reference for the calibration method | [Calibration](Calibration.md) |
| [frequency](frequency.md) | 0..1 <br/> [String](String.md) | How often the instrument was calibrated | [Calibration](Calibration.md) |
| [last_calibration_date](last_calibration_date.md) | 0..1 <br/> [Datetime](Datetime.md) | Date and time of most recent calibration in UTC | [Calibration](Calibration.md) |
| [calibration_certificates](calibration_certificates.md) | 0..1 <br/> [String](String.md) | Information about calibration certificates | [Calibration](Calibration.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CO2GasDetector](CO2GasDetector.md) | [calibration](calibration.md) | range | [DiscreteCO2Calibration](DiscreteCO2Calibration.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:DiscreteCO2Calibration |
| native | oae:DiscreteCO2Calibration |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DiscreteCO2Calibration
description: CO2 calibration for discrete measurements, with calibration temperature.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: CO2Calibration
slots:
- calibration_temperature

```
</details>

### Induced

<details>
```yaml
name: DiscreteCO2Calibration
description: CO2 calibration for discrete measurements, with calibration temperature.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: CO2Calibration
attributes:
  calibration_temperature:
    name: calibration_temperature
    description: Temperature at which calibration was performed.
    title: Calibration temperature
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: calibration_temperature
    owner: DiscreteCO2Calibration
    domain_of:
    - PHCalibration
    - DiscreteCO2Calibration
    range: string
  standard_gas_info:
    name: standard_gas_info
    description: Standard gases used for calibration.
    title: Standard gas information
    from_schema: Calibration
    rank: 1000
    alias: standard_gas_info
    owner: DiscreteCO2Calibration
    domain_of:
    - CO2Calibration
    - ContinuousCO2Calibration
    range: StandardGas
  calibration_location:
    name: calibration_location
    description: Factory calibration, lab calibration, or field calibration.
    title: Calibration location
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: calibration_location
    owner: DiscreteCO2Calibration
    domain_of:
    - Calibration
    range: CalibrationLocation
  technique_description:
    name: technique_description
    description: Details of the calibration technique used.
    title: Calibration technique description
    from_schema: Calibration
    rank: 1000
    alias: technique_description
    owner: DiscreteCO2Calibration
    domain_of:
    - Calibration
    range: string
    required: true
  method_reference:
    name: method_reference
    description: Citation or reference for the calibration method.
    title: Calibration method reference
    from_schema: Calibration
    rank: 1000
    alias: method_reference
    owner: DiscreteCO2Calibration
    domain_of:
    - Calibration
    - InSituVariable
    range: string
  frequency:
    name: frequency
    description: How often the instrument was calibrated.
    title: Frequency of calibration
    from_schema: Calibration
    rank: 1000
    alias: frequency
    owner: DiscreteCO2Calibration
    domain_of:
    - Calibration
    range: string
  last_calibration_date:
    name: last_calibration_date
    description: Date and time of most recent calibration in UTC.
    title: Last calibration date (UTC)
    from_schema: Calibration
    rank: 1000
    alias: last_calibration_date
    owner: DiscreteCO2Calibration
    domain_of:
    - Calibration
    range: datetime
  calibration_certificates:
    name: calibration_certificates
    description: Information about calibration certificates. Ideally, the certificate
      should be made available in a PDF file with filename listed here.
    title: Calibration certificate information
    from_schema: Calibration
    rank: 1000
    alias: calibration_certificates
    owner: DiscreteCO2Calibration
    domain_of:
    - Calibration
    range: string

```
</details>