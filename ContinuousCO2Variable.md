

# Class: ContinuousCO2Variable


_CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2). Reference: OAPMetadata XSD variables.xsd - co2_continuous_





URI: [oae:ContinuousCO2Variable](https://schema.oaedata.org/ContinuousCO2Variable)






```mermaid
 classDiagram
    class ContinuousCO2Variable
    click ContinuousCO2Variable href "../ContinuousCO2Variable"
      MeasuredCO2Fields <|-- ContinuousCO2Variable
        click MeasuredCO2Fields href "../MeasuredCO2Fields"
      ContinuousMeasuredVariable <|-- ContinuousCO2Variable
        click ContinuousMeasuredVariable href "../ContinuousMeasuredVariable"
      
      ContinuousCO2Variable : analyzing_instrument
        
          
    
    
    ContinuousCO2Variable --> "1" ContinuousCO2GasDetector : analyzing_instrument
    click ContinuousCO2GasDetector href "../ContinuousCO2GasDetector"

        
      ContinuousCO2Variable : analyzing_method
        
      ContinuousCO2Variable : appropriate_use_quality
        
          
    
    
    ContinuousCO2Variable --> "0..1" AppropriateUseQuality : appropriate_use_quality
    click AppropriateUseQuality href "../AppropriateUseQuality"

        
      ContinuousCO2Variable : atmospheric_pressure_sensor
        
          
    
    
    ContinuousCO2Variable --> "0..1" PressureSensor : atmospheric_pressure_sensor
    click PressureSensor href "../PressureSensor"

        
      ContinuousCO2Variable : calculation_software_version
        
      ContinuousCO2Variable : dataset_variable_name
        
      ContinuousCO2Variable : dataset_variable_name_qc_flag
        
      ContinuousCO2Variable : dataset_variable_name_raw
        
      ContinuousCO2Variable : drying_method
        
      ContinuousCO2Variable : equilibrator
        
          
    
    
    ContinuousCO2Variable --> "0..1" CO2Equilibrator : equilibrator
    click CO2Equilibrator href "../CO2Equilibrator"

        
      ContinuousCO2Variable : equilibrator_pressure_sensor
        
          
    
    
    ContinuousCO2Variable --> "0..1" PressureSensor : equilibrator_pressure_sensor
    click PressureSensor href "../PressureSensor"

        
      ContinuousCO2Variable : equilibrator_temperature_sensor
        
          
    
    
    ContinuousCO2Variable --> "0..1" TemperatureSensor : equilibrator_temperature_sensor
    click TemperatureSensor href "../TemperatureSensor"

        
      ContinuousCO2Variable : field_replicate_information
        
      ContinuousCO2Variable : genesis
        
      ContinuousCO2Variable : long_name
        
      ContinuousCO2Variable : marine_air_measurement
        
          
    
    
    ContinuousCO2Variable --> "0..1" MarineAirMeasurement : marine_air_measurement
    click MarineAirMeasurement href "../MarineAirMeasurement"

        
      ContinuousCO2Variable : measurement_researcher
        
          
    
    
    ContinuousCO2Variable --> "0..1" Person : measurement_researcher
    click Person href "../Person"

        
      ContinuousCO2Variable : method_reference
        
      ContinuousCO2Variable : missing_value_indicators
        
      ContinuousCO2Variable : observation_type
        
          
    
    
    ContinuousCO2Variable --> "1" ObservationType : observation_type
    click ObservationType href "../ObservationType"

        
      ContinuousCO2Variable : other_detailed_information
        
      ContinuousCO2Variable : pco2_reported_temperature
        
      ContinuousCO2Variable : qc_researcher
        
      ContinuousCO2Variable : qc_researcher_institution
        
      ContinuousCO2Variable : qc_steps_taken
        
      ContinuousCO2Variable : raw_data_calculation_method
        
      ContinuousCO2Variable : sampling
        
      ContinuousCO2Variable : sampling_instrument_type
        
          
    
    
    ContinuousCO2Variable --> "1" SamplingInstrumentType : sampling_instrument_type
    click SamplingInstrumentType href "../SamplingInstrumentType"

        
      ContinuousCO2Variable : sampling_instrument_type_custom
        
      ContinuousCO2Variable : sampling_method
        
      ContinuousCO2Variable : schema_class
        
      ContinuousCO2Variable : seawater_intake_depth
        
      ContinuousCO2Variable : seawater_intake_location
        
      ContinuousCO2Variable : standard_identifier
        
          
    
    
    ContinuousCO2Variable --> "0..1" VocabularyItemReference : standard_identifier
    click VocabularyItemReference href "../VocabularyItemReference"

        
      ContinuousCO2Variable : temperature_correction_method
        
      ContinuousCO2Variable : uncertainty
        
      ContinuousCO2Variable : uncertainty_definition
        
      ContinuousCO2Variable : units
        
      ContinuousCO2Variable : variable_type
        
      ContinuousCO2Variable : water_vapor_correction_method
        
      
```





## Inheritance
* [Variable](Variable.md)
    * [FieldVariable](FieldVariable.md)
        * [InSituVariable](InSituVariable.md)
            * [MeasuredVariable](MeasuredVariable.md) [ [QCFields](QCFields.md)]
                * [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md)
                    * **ContinuousCO2Variable** [ [MeasuredCO2Fields](MeasuredCO2Fields.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [equilibrator](equilibrator.md) | 0..1 <br/> [CO2Equilibrator](CO2Equilibrator.md) | Equilibrator used for CO2 measurement | direct |
| [equilibrator_temperature_sensor](equilibrator_temperature_sensor.md) | 0..1 <br/> [TemperatureSensor](TemperatureSensor.md) | Temperature sensor for the equilibrator | direct |
| [equilibrator_pressure_sensor](equilibrator_pressure_sensor.md) | 0..1 <br/> [PressureSensor](PressureSensor.md) | Pressure sensor for the equilibrator | direct |
| [atmospheric_pressure_sensor](atmospheric_pressure_sensor.md) | 0..1 <br/> [PressureSensor](PressureSensor.md) | Atmospheric pressure sensor | direct |
| [seawater_intake_location](seawater_intake_location.md) | 1 <br/> [String](String.md) | Whereabouts of the seawater intake | direct |
| [seawater_intake_depth](seawater_intake_depth.md) | 1 <br/> [String](String.md) | Water depth of the seawater intake | direct |
| [drying_method](drying_method.md) | 0..1 <br/> [String](String.md) | The method used to dry the gas coming out of CO2 equilibrator, before it is p... | direct |
| [marine_air_measurement](marine_air_measurement.md) | 0..1 <br/> [MarineAirMeasurement](MarineAirMeasurement.md) | Information about CO2 measurements in marine air | direct |
| [appropriate_use_quality](appropriate_use_quality.md) | 0..1 <br/> [AppropriateUseQuality](AppropriateUseQuality.md) | Climate quality is defined as measurements of quality sufficient to assess lo... | [MeasuredCO2Fields](MeasuredCO2Fields.md) |
| [pco2_reported_temperature](pco2_reported_temperature.md) | 1 <br/> [String](String.md) | In Celsius | [MeasuredCO2Fields](MeasuredCO2Fields.md) |
| [water_vapor_correction_method](water_vapor_correction_method.md) | 0..1 <br/> [String](String.md) | How the water vapor pressure inside the equilibrator was determined | [MeasuredCO2Fields](MeasuredCO2Fields.md) |
| [temperature_correction_method](temperature_correction_method.md) | 0..1 <br/> [String](String.md) | How the temperature effect was corrected | [MeasuredCO2Fields](MeasuredCO2Fields.md) |
| [raw_data_calculation_method](raw_data_calculation_method.md) | 1 <br/> [String](String.md) | The method used to calculate reported values from raw sensor data | [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md) |
| [calculation_software_version](calculation_software_version.md) | 0..1 <br/> [String](String.md) | Version of the software used to calculate reported values from raw values | [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md) |
| [analyzing_instrument](analyzing_instrument.md) | 1 <br/> [ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector with standard gas calibration for continuous measurements | [MeasuredVariable](MeasuredVariable.md) |
| [sampling_method](sampling_method.md) | 1 <br/> [String](String.md) | Method used to collect samples | [MeasuredVariable](MeasuredVariable.md) |
| [field_replicate_information](field_replicate_information.md) | 0..1 <br/> [String](String.md) | Repetition of sample collection and measurement, e | [MeasuredVariable](MeasuredVariable.md) |
| [analyzing_method](analyzing_method.md) | 1 <br/> [String](String.md) | Additional information describing how the sample was analyzed | [MeasuredVariable](MeasuredVariable.md) |
| [observation_type](observation_type.md) | 1 <br/> [ObservationType](ObservationType.md) |  | [MeasuredVariable](MeasuredVariable.md) |
| [sampling](sampling.md) | 1 <br/> [String](String.md) |  | [MeasuredVariable](MeasuredVariable.md) |
| [sampling_instrument_type](sampling_instrument_type.md) | 1 <br/> [SamplingInstrumentType](SamplingInstrumentType.md) |  | [MeasuredVariable](MeasuredVariable.md) |
| [sampling_instrument_type_custom](sampling_instrument_type_custom.md) | 0..1 <br/> [String](String.md) |  | [MeasuredVariable](MeasuredVariable.md) |
| [qc_steps_taken](qc_steps_taken.md) | 1 <br/> [String](String.md) | Describe what QC steps have been taken to improve the quality of the data (e | [QCFields](QCFields.md) |
| [uncertainty](uncertainty.md) | 1 <br/> [String](String.md) | It is recommended to provide uncertainty for each data point in the data file | [QCFields](QCFields.md) |
| [uncertainty_definition](uncertainty_definition.md) | 1 <br/> [String](String.md) | A description of the uncertainties involved in this method | [QCFields](QCFields.md) |
| [missing_value_indicators](missing_value_indicators.md) | 1 <br/> [String](String.md) | The indicator used to represent missing values in the data file, e | [QCFields](QCFields.md) |
| [qc_researcher](qc_researcher.md) | 0..1 <br/> [String](String.md) | The name of the PI whose research team QCed this parameter | [QCFields](QCFields.md) |
| [qc_researcher_institution](qc_researcher_institution.md) | 0..1 <br/> [String](String.md) | The institution of the PI whose research team QCed this parameter | [QCFields](QCFields.md) |
| [genesis](genesis.md) | 1 <br/> [String](String.md) |  | [InSituVariable](InSituVariable.md) |
| [dataset_variable_name_qc_flag](dataset_variable_name_qc_flag.md) | 0..1 <br/> [String](String.md) | If applicable, the column header name used for the quality control flag corre... | [InSituVariable](InSituVariable.md) |
| [dataset_variable_name_raw](dataset_variable_name_raw.md) | 0..1 <br/> [String](String.md) | If applicable, the column header name used for the raw data corresponding to ... | [InSituVariable](InSituVariable.md) |
| [other_detailed_information](other_detailed_information.md) | 0..1 <br/> [String](String.md) | Any additional information about this variable | [InSituVariable](InSituVariable.md) |
| [method_reference](method_reference.md) | 0..1 <br/> [String](String.md) | Citation for the method used | [InSituVariable](InSituVariable.md) |
| [measurement_researcher](measurement_researcher.md) | 0..1 <br/> [Person](Person.md) | The name of the PI whose research team measured or derived this parameter | [InSituVariable](InSituVariable.md) |
| [units](units.md) | 1 <br/> [String](String.md) | Unit of measurement for this variable | [Variable](Variable.md) |
| [variable_type](variable_type.md) | 1 <br/> [String](String.md) | High-level classification of the variable | [Variable](Variable.md) |
| [schema_class](schema_class.md) | 1 <br/> [String](String.md) | The schema class name for this variable (e | [Variable](Variable.md) |
| [standard_identifier](standard_identifier.md) | 0..1 <br/> [VocabularyItemReference](VocabularyItemReference.md) | A term from a community vocabulary that identifies this variable | [Variable](Variable.md) |
| [dataset_variable_name](dataset_variable_name.md) | 1 <br/> [String](String.md) | The name for the variable as it is identified in the dataset data file | [Variable](Variable.md) |
| [long_name](long_name.md) | 1 <br/> [String](String.md) | Full descriptive name of the variable | [Variable](Variable.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:ContinuousCO2Variable |
| native | oae:ContinuousCO2Variable |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ContinuousCO2Variable
description: 'CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2). Reference:
  OAPMetadata XSD variables.xsd - co2_continuous'
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: ContinuousMeasuredVariable
mixins:
- MeasuredCO2Fields
slot_usage:
  variable_type:
    name: variable_type
    range: string
    equals_string: co2
  analyzing_instrument:
    name: analyzing_instrument
    description: CO2 gas detector with standard gas calibration for continuous measurements.
    range: ContinuousCO2GasDetector
attributes:
  equilibrator:
    name: equilibrator
    description: Equilibrator used for CO2 measurement.
    title: Equilibrator
    from_schema: Variable
    rank: 1000
    domain_of:
    - ContinuousCO2Variable
    range: CO2Equilibrator
  equilibrator_temperature_sensor:
    name: equilibrator_temperature_sensor
    description: Temperature sensor for the equilibrator.
    title: Equilibrator temperature sensor
    from_schema: Variable
    rank: 1000
    domain_of:
    - ContinuousCO2Variable
    range: TemperatureSensor
  equilibrator_pressure_sensor:
    name: equilibrator_pressure_sensor
    description: Pressure sensor for the equilibrator.
    title: Equilibrator pressure sensor
    from_schema: Variable
    rank: 1000
    domain_of:
    - ContinuousCO2Variable
    range: PressureSensor
  atmospheric_pressure_sensor:
    name: atmospheric_pressure_sensor
    description: Atmospheric pressure sensor.
    title: Atmospheric pressure sensor
    from_schema: Variable
    rank: 1000
    domain_of:
    - ContinuousCO2Variable
    range: PressureSensor
  seawater_intake_location:
    name: seawater_intake_location
    description: Whereabouts of the seawater intake.
    title: Location of seawater intake
    from_schema: Variable
    rank: 1000
    domain_of:
    - ContinuousCO2Variable
    range: string
    required: true
  seawater_intake_depth:
    name: seawater_intake_depth
    description: Water depth of the seawater intake.
    title: Depth of seawater intake
    from_schema: Variable
    rank: 1000
    domain_of:
    - ContinuousCO2Variable
    range: string
    required: true
  drying_method:
    name: drying_method
    description: The method used to dry the gas coming out of CO2 equilibrator, before
      it is pumped into the CO2 sensor.
    title: Drying method for CO2 gas
    from_schema: Variable
    domain_of:
    - MarineAirMeasurement
    - ContinuousCO2Variable
    range: string
  marine_air_measurement:
    name: marine_air_measurement
    description: Information about CO2 measurements in marine air.
    title: CO2 in marine air
    from_schema: Variable
    rank: 1000
    domain_of:
    - ContinuousCO2Variable
    range: MarineAirMeasurement

```
</details>

### Induced

<details>
```yaml
name: ContinuousCO2Variable
description: 'CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2). Reference:
  OAPMetadata XSD variables.xsd - co2_continuous'
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: ContinuousMeasuredVariable
mixins:
- MeasuredCO2Fields
slot_usage:
  variable_type:
    name: variable_type
    range: string
    equals_string: co2
  analyzing_instrument:
    name: analyzing_instrument
    description: CO2 gas detector with standard gas calibration for continuous measurements.
    range: ContinuousCO2GasDetector
attributes:
  equilibrator:
    name: equilibrator
    description: Equilibrator used for CO2 measurement.
    title: Equilibrator
    from_schema: Variable
    rank: 1000
    alias: equilibrator
    owner: ContinuousCO2Variable
    domain_of:
    - ContinuousCO2Variable
    range: CO2Equilibrator
  equilibrator_temperature_sensor:
    name: equilibrator_temperature_sensor
    description: Temperature sensor for the equilibrator.
    title: Equilibrator temperature sensor
    from_schema: Variable
    rank: 1000
    alias: equilibrator_temperature_sensor
    owner: ContinuousCO2Variable
    domain_of:
    - ContinuousCO2Variable
    range: TemperatureSensor
  equilibrator_pressure_sensor:
    name: equilibrator_pressure_sensor
    description: Pressure sensor for the equilibrator.
    title: Equilibrator pressure sensor
    from_schema: Variable
    rank: 1000
    alias: equilibrator_pressure_sensor
    owner: ContinuousCO2Variable
    domain_of:
    - ContinuousCO2Variable
    range: PressureSensor
  atmospheric_pressure_sensor:
    name: atmospheric_pressure_sensor
    description: Atmospheric pressure sensor.
    title: Atmospheric pressure sensor
    from_schema: Variable
    rank: 1000
    alias: atmospheric_pressure_sensor
    owner: ContinuousCO2Variable
    domain_of:
    - ContinuousCO2Variable
    range: PressureSensor
  seawater_intake_location:
    name: seawater_intake_location
    description: Whereabouts of the seawater intake.
    title: Location of seawater intake
    from_schema: Variable
    rank: 1000
    alias: seawater_intake_location
    owner: ContinuousCO2Variable
    domain_of:
    - ContinuousCO2Variable
    range: string
    required: true
  seawater_intake_depth:
    name: seawater_intake_depth
    description: Water depth of the seawater intake.
    title: Depth of seawater intake
    from_schema: Variable
    rank: 1000
    alias: seawater_intake_depth
    owner: ContinuousCO2Variable
    domain_of:
    - ContinuousCO2Variable
    range: string
    required: true
  drying_method:
    name: drying_method
    description: The method used to dry the gas coming out of CO2 equilibrator, before
      it is pumped into the CO2 sensor.
    title: Drying method for CO2 gas
    from_schema: Variable
    alias: drying_method
    owner: ContinuousCO2Variable
    domain_of:
    - MarineAirMeasurement
    - ContinuousCO2Variable
    range: string
  marine_air_measurement:
    name: marine_air_measurement
    description: Information about CO2 measurements in marine air.
    title: CO2 in marine air
    from_schema: Variable
    rank: 1000
    alias: marine_air_measurement
    owner: ContinuousCO2Variable
    domain_of:
    - ContinuousCO2Variable
    range: MarineAirMeasurement
  appropriate_use_quality:
    name: appropriate_use_quality
    description: 'Climate quality is defined as measurements of quality sufficient
      to assess long term trends with a defined level of confidence. Weather quality
      is defined as measurements of quality sufficient to identify relative spatial
      patterns and short term variation.

      For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson
      P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements
      and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.'
    title: Weather or climate quality
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: appropriate_use_quality
    owner: ContinuousCO2Variable
    domain_of:
    - MeasuredTAFields
    - MeasuredDICFields
    - MeasuredPHFields
    - MeasuredCO2Fields
    range: AppropriateUseQuality
  pco2_reported_temperature:
    name: pco2_reported_temperature
    description: In Celsius. The input could be a constant temperature value, or something
      like, in-situ temperature, temperature of analysis, etc.
    title: Temperature at which pCO2 was reported
    from_schema: Variable
    rank: 1000
    alias: pco2_reported_temperature
    owner: ContinuousCO2Variable
    domain_of:
    - MeasuredCO2Fields
    range: string
    required: true
  water_vapor_correction_method:
    name: water_vapor_correction_method
    description: How the water vapor pressure inside the equilibrator was determined.
    title: Water vapor correction method
    from_schema: Variable
    rank: 1000
    alias: water_vapor_correction_method
    owner: ContinuousCO2Variable
    domain_of:
    - MeasuredCO2Fields
    range: string
  temperature_correction_method:
    name: temperature_correction_method
    description: How the temperature effect was corrected.
    title: Temperature correction method
    from_schema: Variable
    alias: temperature_correction_method
    owner: ContinuousCO2Variable
    domain_of:
    - DiscretePHVariable
    - MeasuredCO2Fields
    range: string
  raw_data_calculation_method:
    name: raw_data_calculation_method
    description: The method used to calculate reported values from raw sensor data.
    title: Method to calculate reported values from raw data
    from_schema: Variable
    rank: 1000
    alias: raw_data_calculation_method
    owner: ContinuousCO2Variable
    domain_of:
    - ContinuousMeasuredVariable
    range: string
    required: true
  calculation_software_version:
    name: calculation_software_version
    description: Version of the software used to calculate reported values from raw
      values.
    title: Software version for the calculation
    from_schema: Variable
    rank: 1000
    alias: calculation_software_version
    owner: ContinuousCO2Variable
    domain_of:
    - ContinuousMeasuredVariable
    range: string
  analyzing_instrument:
    name: analyzing_instrument
    description: CO2 gas detector with standard gas calibration for continuous measurements.
    title: Analyzing instrument
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: analyzing_instrument
    owner: ContinuousCO2Variable
    domain_of:
    - MeasuredVariable
    range: ContinuousCO2GasDetector
    required: true
  sampling_method:
    name: sampling_method
    description: Method used to collect samples.
    title: Sampling Method
    from_schema: Variable
    rank: 1000
    alias: sampling_method
    owner: ContinuousCO2Variable
    domain_of:
    - MeasuredVariable
    range: string
    required: true
  field_replicate_information:
    name: field_replicate_information
    description: Repetition of sample collection and measurement, e.g., triplicate
      samples.
    title: Field replicate information
    from_schema: Variable
    rank: 1000
    alias: field_replicate_information
    owner: ContinuousCO2Variable
    domain_of:
    - MeasuredVariable
    range: string
  analyzing_method:
    name: analyzing_method
    description: Additional information describing how the sample was analyzed. DOIs
      provided as applicable.
    title: Analyzing Method
    from_schema: Variable
    rank: 1000
    alias: analyzing_method
    owner: ContinuousCO2Variable
    domain_of:
    - MeasuredVariable
    range: string
    required: true
  observation_type:
    name: observation_type
    title: Observation Type
    from_schema: Variable
    rank: 1000
    alias: observation_type
    owner: ContinuousCO2Variable
    domain_of:
    - MeasuredVariable
    range: ObservationType
    required: true
  sampling:
    name: sampling
    from_schema: Variable
    rank: 1000
    alias: sampling
    owner: ContinuousCO2Variable
    domain_of:
    - MeasuredVariable
    range: string
    required: true
    equals_string: continuous
  sampling_instrument_type:
    name: sampling_instrument_type
    title: Sampling instrument type
    from_schema: Variable
    rank: 1000
    alias: sampling_instrument_type
    owner: ContinuousCO2Variable
    domain_of:
    - MeasuredVariable
    range: SamplingInstrumentType
    required: true
  sampling_instrument_type_custom:
    name: sampling_instrument_type_custom
    title: Sampling instrument type (custom)
    from_schema: Variable
    rank: 1000
    alias: sampling_instrument_type_custom
    owner: ContinuousCO2Variable
    domain_of:
    - MeasuredVariable
    range: string
  qc_steps_taken:
    name: qc_steps_taken
    description: 'Describe what QC steps have been taken to improve the quality of
      the data (e.g., DOI, software and settings used, outlier removal, etc.).

      If quality control procedures are described in a separate document uploaded
      with the data, provide the name of the document here.'
    title: QC steps taken
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: qc_steps_taken
    owner: ContinuousCO2Variable
    domain_of:
    - QCFields
    range: string
    required: true
  uncertainty:
    name: uncertainty
    description: 'It is recommended to provide uncertainty for each data point in
      the data file. Else provide a single value representative of the dataset.

      If uncertainty is provided as a variable, please list the column header name
      here.'
    title: Uncertainty
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: uncertainty
    owner: ContinuousCO2Variable
    domain_of:
    - StandardGas
    - CO2GasDetector
    - QCFields
    range: string
    required: true
  uncertainty_definition:
    name: uncertainty_definition
    description: A description of the uncertainties involved in this method.
    title: How was the uncertainty defined
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: uncertainty_definition
    owner: ContinuousCO2Variable
    domain_of:
    - QCFields
    range: string
    required: true
  missing_value_indicators:
    name: missing_value_indicators
    description: The indicator used to represent missing values in the data file,
      e.g., -999, NaN, etc.
    title: Missing value indicators
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: missing_value_indicators
    owner: ContinuousCO2Variable
    domain_of:
    - QCFields
    range: string
    required: true
  qc_researcher:
    name: qc_researcher
    description: The name of the PI whose research team QCed this parameter.
    title: Researcher who QCed this variable
    from_schema: Variable
    rank: 1000
    alias: qc_researcher
    owner: ContinuousCO2Variable
    domain_of:
    - QCFields
    range: string
  qc_researcher_institution:
    name: qc_researcher_institution
    description: The institution of the PI whose research team QCed this parameter.
    title: QC Researcher Institution
    from_schema: Variable
    rank: 1000
    alias: qc_researcher_institution
    owner: ContinuousCO2Variable
    domain_of:
    - QCFields
    range: string
  genesis:
    name: genesis
    from_schema: Variable
    rank: 1000
    alias: genesis
    owner: ContinuousCO2Variable
    domain_of:
    - InSituVariable
    range: string
    required: true
    equals_string: measured
  dataset_variable_name_qc_flag:
    name: dataset_variable_name_qc_flag
    description: If applicable, the column header name used for the quality control
      flag corresponding to this variable.
    title: Dataset variable name (Quality Flag)
    from_schema: Variable
    rank: 1000
    alias: dataset_variable_name_qc_flag
    owner: ContinuousCO2Variable
    domain_of:
    - InSituVariable
    range: string
  dataset_variable_name_raw:
    name: dataset_variable_name_raw
    description: If applicable, the column header name used for the raw data corresponding
      to this variable.
    title: Dataset variable name (raw)
    from_schema: Variable
    rank: 1000
    alias: dataset_variable_name_raw
    owner: ContinuousCO2Variable
    domain_of:
    - InSituVariable
    range: string
  other_detailed_information:
    name: other_detailed_information
    description: Any additional information about this variable.
    title: Other Detailed Information
    from_schema: Variable
    rank: 1000
    alias: other_detailed_information
    owner: ContinuousCO2Variable
    domain_of:
    - InSituVariable
    range: string
  method_reference:
    name: method_reference
    description: Citation for the method used.
    title: Method Reference
    from_schema: Variable
    alias: method_reference
    owner: ContinuousCO2Variable
    domain_of:
    - Calibration
    - InSituVariable
    range: string
  measurement_researcher:
    name: measurement_researcher
    description: The name of the PI whose research team measured or derived this parameter.
    title: Researcher who measured the variable
    from_schema: Variable
    rank: 1000
    alias: measurement_researcher
    owner: ContinuousCO2Variable
    domain_of:
    - InSituVariable
    range: Person
  units:
    name: units
    description: Unit of measurement for this variable.
    title: Unit
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: units
    owner: ContinuousCO2Variable
    domain_of:
    - Variable
    range: string
    required: true
  variable_type:
    name: variable_type
    description: High-level classification of the variable. Determines which standard
      identifiers are available and, combined with genesis and sampling, which schema
      class to use.
    title: Variable Type
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: variable_type
    owner: ContinuousCO2Variable
    domain_of:
    - Variable
    range: string
    required: true
    equals_string: co2
  schema_class:
    name: schema_class
    description: The schema class name for this variable (e.g., "DiscretePHVariable").
      Auto-populated by the metadata builder.
    from_schema: Variable
    rank: 1000
    designates_type: true
    alias: schema_class
    owner: ContinuousCO2Variable
    domain_of:
    - Variable
    range: string
    required: true
  standard_identifier:
    name: standard_identifier
    description: A term from a community vocabulary that identifies this variable.
      CF standard names (NERC P07) are recommended.
    from_schema: Variable
    rank: 1000
    alias: standard_identifier
    owner: ContinuousCO2Variable
    domain_of:
    - Variable
    range: VocabularyItemReference
  dataset_variable_name:
    name: dataset_variable_name
    description: The name for the variable as it is identified in the dataset data
      file. This could be the column header in a CSV or the variable name in a NetCDF
      file. Standard common recommended column header names can be found in protocol
      documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).
    title: Dataset variable name
    from_schema: Variable
    rank: 1000
    alias: dataset_variable_name
    owner: ContinuousCO2Variable
    domain_of:
    - Variable
    range: string
    required: true
  long_name:
    name: long_name
    description: Full descriptive name of the variable.
    title: Variable full name
    from_schema: Variable
    rank: 1000
    alias: long_name
    owner: ContinuousCO2Variable
    domain_of:
    - Variable
    range: string
    required: true

```
</details>