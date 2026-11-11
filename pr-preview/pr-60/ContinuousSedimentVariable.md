

# Class: ContinuousSedimentVariable


_Measured sediment variable collected from continuous autonomous sensor_





URI: [oae:ContinuousSedimentVariable](https://schema.oaedata.org/ContinuousSedimentVariable)






```mermaid
 classDiagram
    class ContinuousSedimentVariable
    click ContinuousSedimentVariable href "../ContinuousSedimentVariable"
      MeasuredSedimentFields <|-- ContinuousSedimentVariable
        click MeasuredSedimentFields href "../MeasuredSedimentFields"
      ContinuousMeasuredVariable <|-- ContinuousSedimentVariable
        click ContinuousMeasuredVariable href "../ContinuousMeasuredVariable"
      
      ContinuousSedimentVariable : analyzing_instrument
        
          
    
    
    ContinuousSedimentVariable --> "1" AnalyzingInstrument : analyzing_instrument
    click AnalyzingInstrument href "../AnalyzingInstrument"

        
      ContinuousSedimentVariable : analyzing_method
        
      ContinuousSedimentVariable : calculation_software_version
        
      ContinuousSedimentVariable : dataset_variable_name
        
      ContinuousSedimentVariable : dataset_variable_name_qc_flag
        
      ContinuousSedimentVariable : dataset_variable_name_raw
        
      ContinuousSedimentVariable : field_replicate_information
        
      ContinuousSedimentVariable : genesis
        
      ContinuousSedimentVariable : long_name
        
      ContinuousSedimentVariable : measurement_researcher
        
          
    
    
    ContinuousSedimentVariable --> "0..1" Person : measurement_researcher
    click Person href "../Person"

        
      ContinuousSedimentVariable : method_reference
        
      ContinuousSedimentVariable : missing_value_indicators
        
      ContinuousSedimentVariable : observation_type
        
          
    
    
    ContinuousSedimentVariable --> "1" ObservationType : observation_type
    click ObservationType href "../ObservationType"

        
      ContinuousSedimentVariable : other_detailed_information
        
      ContinuousSedimentVariable : qc_researcher
        
      ContinuousSedimentVariable : qc_researcher_institution
        
      ContinuousSedimentVariable : qc_steps_taken
        
      ContinuousSedimentVariable : raw_data_calculation_method
        
      ContinuousSedimentVariable : sampling
        
      ContinuousSedimentVariable : sampling_instrument_type
        
          
    
    
    ContinuousSedimentVariable --> "1" SamplingInstrumentType : sampling_instrument_type
    click SamplingInstrumentType href "../SamplingInstrumentType"

        
      ContinuousSedimentVariable : sampling_instrument_type_custom
        
      ContinuousSedimentVariable : sampling_method
        
      ContinuousSedimentVariable : schema_class
        
      ContinuousSedimentVariable : sediment_sampling_depth
        
      ContinuousSedimentVariable : sediment_sampling_water_depth
        
      ContinuousSedimentVariable : sediment_type
        
      ContinuousSedimentVariable : standard_identifier
        
          
    
    
    ContinuousSedimentVariable --> "0..1" VocabularyItemReference : standard_identifier
    click VocabularyItemReference href "../VocabularyItemReference"

        
      ContinuousSedimentVariable : uncertainty
        
      ContinuousSedimentVariable : uncertainty_definition
        
      ContinuousSedimentVariable : units
        
      ContinuousSedimentVariable : variable_type
        
      
```





## Inheritance
* [Variable](Variable.md)
    * [FieldVariable](FieldVariable.md)
        * [InSituVariable](InSituVariable.md)
            * [MeasuredVariable](MeasuredVariable.md) [ [QCFields](QCFields.md)]
                * [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md)
                    * **ContinuousSedimentVariable** [ [MeasuredSedimentFields](MeasuredSedimentFields.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [sediment_type](sediment_type.md) | 1 <br/> [String](String.md) | e | [MeasuredSedimentFields](MeasuredSedimentFields.md) |
| [sediment_sampling_depth](sediment_sampling_depth.md) | 1 <br/> [String](String.md) | Depth that sediment was collected below sediment surface | [MeasuredSedimentFields](MeasuredSedimentFields.md) |
| [sediment_sampling_water_depth](sediment_sampling_water_depth.md) | 1 <br/> [String](String.md) | Water depth where sediment was collected | [MeasuredSedimentFields](MeasuredSedimentFields.md) |
| [raw_data_calculation_method](raw_data_calculation_method.md) | 1 <br/> [String](String.md) | The method used to calculate reported values from raw sensor data | [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md) |
| [calculation_software_version](calculation_software_version.md) | 0..1 <br/> [String](String.md) | Version of the software used to calculate reported values from raw values | [ContinuousMeasuredVariable](ContinuousMeasuredVariable.md) |
| [analyzing_instrument](analyzing_instrument.md) | 1 <br/> [AnalyzingInstrument](AnalyzingInstrument.md) | Instrument used to analyze the water samples or measure the water body contin... | [MeasuredVariable](MeasuredVariable.md) |
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
| self | oae:ContinuousSedimentVariable |
| native | oae:ContinuousSedimentVariable |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ContinuousSedimentVariable
description: Measured sediment variable collected from continuous autonomous sensor
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: ContinuousMeasuredVariable
mixins:
- MeasuredSedimentFields
slot_usage:
  variable_type:
    name: variable_type
    range: string
    equals_string: sediment

```
</details>

### Induced

<details>
```yaml
name: ContinuousSedimentVariable
description: Measured sediment variable collected from continuous autonomous sensor
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: ContinuousMeasuredVariable
mixins:
- MeasuredSedimentFields
slot_usage:
  variable_type:
    name: variable_type
    range: string
    equals_string: sediment
attributes:
  sediment_type:
    name: sediment_type
    description: e.g., mud, sand, etc.
    title: Sediment Type
    from_schema: Variable
    rank: 1000
    alias: sediment_type
    owner: ContinuousSedimentVariable
    domain_of:
    - MeasuredSedimentFields
    range: string
    required: true
  sediment_sampling_depth:
    name: sediment_sampling_depth
    description: Depth that sediment was collected below sediment surface. If provided
      as a variable (recommended), please list the column header name here.
    title: Sediment Sampling Depth
    from_schema: Variable
    rank: 1000
    alias: sediment_sampling_depth
    owner: ContinuousSedimentVariable
    domain_of:
    - MeasuredSedimentFields
    range: string
    required: true
  sediment_sampling_water_depth:
    name: sediment_sampling_water_depth
    description: Water depth where sediment was collected. If provided as a variable
      (recommended), please list the column header name here.
    title: Sediment Sampling Water Depth
    from_schema: Variable
    rank: 1000
    alias: sediment_sampling_water_depth
    owner: ContinuousSedimentVariable
    domain_of:
    - MeasuredSedimentFields
    range: string
    required: true
  raw_data_calculation_method:
    name: raw_data_calculation_method
    description: The method used to calculate reported values from raw sensor data.
    title: Method to calculate reported values from raw data
    from_schema: Variable
    rank: 1000
    alias: raw_data_calculation_method
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
    domain_of:
    - ContinuousMeasuredVariable
    range: string
  analyzing_instrument:
    name: analyzing_instrument
    description: Instrument used to analyze the water samples or measure the water
      body continuously. Instrument includes calibration information.
    title: Analyzing instrument
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: analyzing_instrument
    owner: ContinuousSedimentVariable
    domain_of:
    - MeasuredVariable
    range: AnalyzingInstrument
    required: true
  sampling_method:
    name: sampling_method
    description: Method used to collect samples.
    title: Sampling Method
    from_schema: Variable
    rank: 1000
    alias: sampling_method
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
    domain_of:
    - MeasuredVariable
    range: ObservationType
    required: true
  sampling:
    name: sampling
    from_schema: Variable
    rank: 1000
    alias: sampling
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
    domain_of:
    - QCFields
    range: string
  genesis:
    name: genesis
    from_schema: Variable
    rank: 1000
    alias: genesis
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
    domain_of:
    - InSituVariable
    range: string
  method_reference:
    name: method_reference
    description: Citation for the method used.
    title: Method Reference
    from_schema: Variable
    alias: method_reference
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
    domain_of:
    - Variable
    range: string
    required: true
    equals_string: sediment
  schema_class:
    name: schema_class
    description: The schema class name for this variable (e.g., "DiscretePHVariable").
      Auto-populated by the metadata builder.
    from_schema: Variable
    rank: 1000
    designates_type: true
    alias: schema_class
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
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
    owner: ContinuousSedimentVariable
    domain_of:
    - Variable
    range: string
    required: true

```
</details>