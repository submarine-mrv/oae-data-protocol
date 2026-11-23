

# Class: DyeCalibration


_pH instrument calibration with an indicator dye standard._





URI: [oae:DyeCalibration](https://schema.oaedata.org/DyeCalibration)






```mermaid
 classDiagram
    class DyeCalibration
    click DyeCalibration href "../DyeCalibration"
      PHCalibration <|-- DyeCalibration
        click PHCalibration href "../PHCalibration"
      
      DyeCalibration : calibration_certificates
        
      DyeCalibration : calibration_location
        
          
    
    
    DyeCalibration --> "0..1" CalibrationLocation : calibration_location
    click CalibrationLocation href "../CalibrationLocation"

        
      DyeCalibration : calibration_temperature
        
      DyeCalibration : correction_for_unpurified_dye
        
      DyeCalibration : dye_correction_method
        
      DyeCalibration : dye_purified
        
      DyeCalibration : frequency
        
      DyeCalibration : last_calibration_date
        
      DyeCalibration : method_reference
        
      DyeCalibration : ph_of_standards
        
      DyeCalibration : standard_type_and_production
        
      DyeCalibration : standard_used
        
      DyeCalibration : standard_used_custom
        
      DyeCalibration : technique_description
        
      
```





## Inheritance
* [Calibration](Calibration.md)
    * [PHCalibration](PHCalibration.md)
        * **DyeCalibration**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [dye_purified](dye_purified.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether the dye has been purified | direct |
| [correction_for_unpurified_dye](correction_for_unpurified_dye.md) | 0..1 <br/> [String](String.md) | Correction method applied if dye was not purified | direct |
| [dye_correction_method](dye_correction_method.md) | 0..1 <br/> [String](String.md) | Method used to correct for dye effects | direct |
| [calibration_temperature](calibration_temperature.md) | 0..1 <br/> [String](String.md) | Temperature at which calibration was performed | [PHCalibration](PHCalibration.md) |
| [standard_used](standard_used.md) | 1 <br/> [String](String.md) | Type of standard used to calibrate the pH measurement | [PHCalibration](PHCalibration.md) |
| [standard_used_custom](standard_used_custom.md) | 0..1 <br/> [String](String.md) | Name of the standard used, when it is not in the list | [PHCalibration](PHCalibration.md) |
| [standard_type_and_production](standard_type_and_production.md) | 0..1 <br/> [String](String.md) | Details on the standard (e | [PHCalibration](PHCalibration.md) |
| [ph_of_standards](ph_of_standards.md) | 0..1 <br/> [String](String.md) | pH values of the calibration standards used | [PHCalibration](PHCalibration.md) |
| [calibration_location](calibration_location.md) | 0..1 <br/> [CalibrationLocation](CalibrationLocation.md) | Factory calibration, lab calibration, or field calibration | [Calibration](Calibration.md) |
| [technique_description](technique_description.md) | 1 <br/> [String](String.md) | Details of the calibration technique used | [Calibration](Calibration.md) |
| [method_reference](method_reference.md) | 0..1 <br/> [String](String.md) | Citation or reference for the calibration method | [Calibration](Calibration.md) |
| [frequency](frequency.md) | 0..1 <br/> [String](String.md) | How often the instrument was calibrated | [Calibration](Calibration.md) |
| [last_calibration_date](last_calibration_date.md) | 0..1 <br/> [Datetime](Datetime.md) | Date and time of most recent calibration in UTC | [Calibration](Calibration.md) |
| [calibration_certificates](calibration_certificates.md) | 0..1 <br/> [String](String.md) | Information about calibration certificates | [Calibration](Calibration.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PHInstrument](PHInstrument.md) | [calibration](calibration.md) | any_of[range] | [DyeCalibration](DyeCalibration.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:DyeCalibration |
| native | oae:DyeCalibration |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DyeCalibration
description: pH instrument calibration with an indicator dye standard.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: PHCalibration
slot_usage:
  standard_used:
    name: standard_used
    range: string
    equals_string_in:
    - dye
attributes:
  dye_purified:
    name: dye_purified
    description: Whether the dye has been purified.
    title: Dye purified
    from_schema: Calibration
    rank: 1000
    domain_of:
    - DyeCalibration
    range: boolean
  correction_for_unpurified_dye:
    name: correction_for_unpurified_dye
    description: Correction method applied if dye was not purified.
    title: Correction for unpurified dye
    from_schema: Calibration
    rank: 1000
    domain_of:
    - DyeCalibration
    range: string
  dye_correction_method:
    name: dye_correction_method
    description: Method used to correct for dye effects.
    title: Dye correction method
    from_schema: Calibration
    rank: 1000
    domain_of:
    - DyeCalibration
    range: string

```
</details>

### Induced

<details>
```yaml
name: DyeCalibration
description: pH instrument calibration with an indicator dye standard.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: PHCalibration
slot_usage:
  standard_used:
    name: standard_used
    range: string
    equals_string_in:
    - dye
attributes:
  dye_purified:
    name: dye_purified
    description: Whether the dye has been purified.
    title: Dye purified
    from_schema: Calibration
    rank: 1000
    alias: dye_purified
    owner: DyeCalibration
    domain_of:
    - DyeCalibration
    range: boolean
  correction_for_unpurified_dye:
    name: correction_for_unpurified_dye
    description: Correction method applied if dye was not purified.
    title: Correction for unpurified dye
    from_schema: Calibration
    rank: 1000
    alias: correction_for_unpurified_dye
    owner: DyeCalibration
    domain_of:
    - DyeCalibration
    range: string
  dye_correction_method:
    name: dye_correction_method
    description: Method used to correct for dye effects.
    title: Dye correction method
    from_schema: Calibration
    rank: 1000
    alias: dye_correction_method
    owner: DyeCalibration
    domain_of:
    - DyeCalibration
    range: string
  calibration_temperature:
    name: calibration_temperature
    description: Temperature at which calibration was performed.
    title: Calibration temperature
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: calibration_temperature
    owner: DyeCalibration
    domain_of:
    - PHCalibration
    - DiscreteCO2Calibration
    range: string
  standard_used:
    name: standard_used
    description: Type of standard used to calibrate the pH measurement.
    title: Standard used
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: standard_used
    owner: DyeCalibration
    domain_of:
    - PHCalibration
    range: string
    required: true
    equals_string_in:
    - dye
  standard_used_custom:
    name: standard_used_custom
    description: Name of the standard used, when it is not in the list.
    title: Standard used (custom)
    from_schema: Calibration
    rank: 1000
    alias: standard_used_custom
    owner: DyeCalibration
    domain_of:
    - PHCalibration
    range: string
  standard_type_and_production:
    name: standard_type_and_production
    description: Details on the standard (e.g., type of dye used) and how or where
      it was produced.
    title: Standard type and production
    from_schema: Calibration
    rank: 1000
    alias: standard_type_and_production
    owner: DyeCalibration
    domain_of:
    - PHCalibration
    range: string
  ph_of_standards:
    name: ph_of_standards
    description: pH values of the calibration standards used.
    title: pH of standards
    from_schema: Calibration
    rank: 1000
    alias: ph_of_standards
    owner: DyeCalibration
    domain_of:
    - PHCalibration
    range: string
  calibration_location:
    name: calibration_location
    description: Factory calibration, lab calibration, or field calibration.
    title: Calibration location
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: calibration_location
    owner: DyeCalibration
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
    owner: DyeCalibration
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
    owner: DyeCalibration
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
    owner: DyeCalibration
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
    owner: DyeCalibration
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
    owner: DyeCalibration
    domain_of:
    - Calibration
    range: string

```
</details>