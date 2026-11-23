

# Class: CalculatedVariable


_A variable that is calculated or derived from other measured variables rather than directly measured by an instrument (e.g., carbonate system parameters computed via CO2SYS). Set genesis to "calculated". The variable_type should reflect the quantity being calculated (e.g., "pH", "ta", "dic", "co2", or "other")._





URI: [oae:CalculatedVariable](https://schema.oaedata.org/CalculatedVariable)






```mermaid
 classDiagram
    class CalculatedVariable
    click CalculatedVariable href "../CalculatedVariable"
      QCFields <|-- CalculatedVariable
        click QCFields href "../QCFields"
      InSituVariable <|-- CalculatedVariable
        click InSituVariable href "../InSituVariable"
      
      CalculatedVariable : calculation_method_and_parameters
        
      CalculatedVariable : dataset_variable_name
        
      CalculatedVariable : dataset_variable_name_qc_flag
        
      CalculatedVariable : dataset_variable_name_raw
        
      CalculatedVariable : genesis
        
      CalculatedVariable : long_name
        
      CalculatedVariable : measurement_researcher
        
          
    
    
    CalculatedVariable --> "0..1" Person : measurement_researcher
    click Person href "../Person"

        
      CalculatedVariable : method_reference
        
      CalculatedVariable : missing_value_indicators
        
      CalculatedVariable : other_detailed_information
        
      CalculatedVariable : qc_researcher
        
      CalculatedVariable : qc_researcher_institution
        
      CalculatedVariable : qc_steps_taken
        
      CalculatedVariable : schema_class
        
      CalculatedVariable : standard_identifier
        
          
    
    
    CalculatedVariable --> "0..1" VocabularyItemReference : standard_identifier
    click VocabularyItemReference href "../VocabularyItemReference"

        
      CalculatedVariable : uncertainty
        
      CalculatedVariable : uncertainty_definition
        
      CalculatedVariable : units
        
      CalculatedVariable : variable_type
        
          
    
    
    CalculatedVariable --> "1" VariableType : variable_type
    click VariableType href "../VariableType"

        
      
```





## Inheritance
* [Variable](Variable.md)
    * [FieldVariable](FieldVariable.md)
        * [InSituVariable](InSituVariable.md)
            * **CalculatedVariable** [ [QCFields](QCFields.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [calculation_method_and_parameters](calculation_method_and_parameters.md) | 1 <br/> [String](String.md) | Information about how the variable was calculated and the parameters used in ... | direct |
| [qc_steps_taken](qc_steps_taken.md) | 0..1 <br/> [String](String.md) | Describe what QC steps have been taken to improve the quality of the data (e | [QCFields](QCFields.md) |
| [uncertainty](uncertainty.md) | 0..1 <br/> [String](String.md) | It is recommended to provide uncertainty for each data point in the data file | [QCFields](QCFields.md) |
| [uncertainty_definition](uncertainty_definition.md) | 0..1 <br/> [String](String.md) | A description of the uncertainties involved in this method | [QCFields](QCFields.md) |
| [missing_value_indicators](missing_value_indicators.md) | 0..1 <br/> [String](String.md) | The indicator used to represent missing values in the data file, e | [QCFields](QCFields.md) |
| [qc_researcher](qc_researcher.md) | 0..1 <br/> [String](String.md) | The name of the PI whose research team QCed this parameter | [QCFields](QCFields.md) |
| [qc_researcher_institution](qc_researcher_institution.md) | 0..1 <br/> [String](String.md) | The institution of the PI whose research team QCed this parameter | [QCFields](QCFields.md) |
| [genesis](genesis.md) | 1 <br/> [String](String.md) |  | [InSituVariable](InSituVariable.md) |
| [dataset_variable_name_qc_flag](dataset_variable_name_qc_flag.md) | 0..1 <br/> [String](String.md) | If applicable, the column header name used for the quality control flag corre... | [InSituVariable](InSituVariable.md) |
| [dataset_variable_name_raw](dataset_variable_name_raw.md) | 0..1 <br/> [String](String.md) | If applicable, the column header name used for the raw data corresponding to ... | [InSituVariable](InSituVariable.md) |
| [other_detailed_information](other_detailed_information.md) | 0..1 <br/> [String](String.md) | Any additional information about this variable | [InSituVariable](InSituVariable.md) |
| [method_reference](method_reference.md) | 0..1 <br/> [String](String.md) | Citation for the method used | [InSituVariable](InSituVariable.md) |
| [measurement_researcher](measurement_researcher.md) | 0..1 <br/> [Person](Person.md) | The name of the PI whose research team measured or derived this parameter | [InSituVariable](InSituVariable.md) |
| [units](units.md) | 1 <br/> [String](String.md) | Unit of measurement for this variable | [Variable](Variable.md) |
| [variable_type](variable_type.md) | 1 <br/> [VariableType](VariableType.md) | High-level classification of the variable | [Variable](Variable.md) |
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
| self | oae:CalculatedVariable |
| native | oae:CalculatedVariable |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CalculatedVariable
description: A variable that is calculated or derived from other measured variables
  rather than directly measured by an instrument (e.g., carbonate system parameters
  computed via CO2SYS). Set genesis to "calculated". The variable_type should reflect
  the quantity being calculated (e.g., "pH", "ta", "dic", "co2", or "other").
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: InSituVariable
mixins:
- QCFields
slot_usage:
  genesis:
    name: genesis
    range: string
    equals_string: calculated
attributes:
  calculation_method_and_parameters:
    name: calculation_method_and_parameters
    description: 'Information about how the variable was calculated and the parameters
      used in calculation, e.g.: Calculation software = CO2SYSv1 (MATLAB) Input variables
      =  pH and DIC (column header names ''ph_t_insitu'' and ''dic'' in associated
      dataset file) Additional information = the dissociation constants of Lueker
      et al., 2000 for carbonic acid, etc.'
    title: Calculated Method And Parameters
    from_schema: Variable
    rank: 1000
    domain_of:
    - CalculatedVariable
    range: string
    required: true

```
</details>

### Induced

<details>
```yaml
name: CalculatedVariable
description: A variable that is calculated or derived from other measured variables
  rather than directly measured by an instrument (e.g., carbonate system parameters
  computed via CO2SYS). Set genesis to "calculated". The variable_type should reflect
  the quantity being calculated (e.g., "pH", "ta", "dic", "co2", or "other").
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: InSituVariable
mixins:
- QCFields
slot_usage:
  genesis:
    name: genesis
    range: string
    equals_string: calculated
attributes:
  calculation_method_and_parameters:
    name: calculation_method_and_parameters
    description: 'Information about how the variable was calculated and the parameters
      used in calculation, e.g.: Calculation software = CO2SYSv1 (MATLAB) Input variables
      =  pH and DIC (column header names ''ph_t_insitu'' and ''dic'' in associated
      dataset file) Additional information = the dissociation constants of Lueker
      et al., 2000 for carbonic acid, etc.'
    title: Calculated Method And Parameters
    from_schema: Variable
    rank: 1000
    alias: calculation_method_and_parameters
    owner: CalculatedVariable
    domain_of:
    - CalculatedVariable
    range: string
    required: true
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
    owner: CalculatedVariable
    domain_of:
    - QCFields
    range: string
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
    owner: CalculatedVariable
    domain_of:
    - StandardGas
    - CO2GasDetector
    - QCFields
    range: string
  uncertainty_definition:
    name: uncertainty_definition
    description: A description of the uncertainties involved in this method.
    title: How was the uncertainty defined
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: uncertainty_definition
    owner: CalculatedVariable
    domain_of:
    - QCFields
    range: string
  missing_value_indicators:
    name: missing_value_indicators
    description: The indicator used to represent missing values in the data file,
      e.g., -999, NaN, etc.
    title: Missing value indicators
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: missing_value_indicators
    owner: CalculatedVariable
    domain_of:
    - QCFields
    range: string
  qc_researcher:
    name: qc_researcher
    description: The name of the PI whose research team QCed this parameter.
    title: Researcher who QCed this variable
    from_schema: Variable
    rank: 1000
    alias: qc_researcher
    owner: CalculatedVariable
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
    owner: CalculatedVariable
    domain_of:
    - QCFields
    range: string
  genesis:
    name: genesis
    from_schema: Variable
    rank: 1000
    alias: genesis
    owner: CalculatedVariable
    domain_of:
    - InSituVariable
    range: string
    required: true
    equals_string: calculated
  dataset_variable_name_qc_flag:
    name: dataset_variable_name_qc_flag
    description: If applicable, the column header name used for the quality control
      flag corresponding to this variable.
    title: Dataset variable name (Quality Flag)
    from_schema: Variable
    rank: 1000
    alias: dataset_variable_name_qc_flag
    owner: CalculatedVariable
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
    owner: CalculatedVariable
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
    owner: CalculatedVariable
    domain_of:
    - InSituVariable
    range: string
  method_reference:
    name: method_reference
    description: Citation for the method used.
    title: Method Reference
    from_schema: Variable
    alias: method_reference
    owner: CalculatedVariable
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
    owner: CalculatedVariable
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
    owner: CalculatedVariable
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
    owner: CalculatedVariable
    domain_of:
    - Variable
    range: VariableType
    required: true
  schema_class:
    name: schema_class
    description: The schema class name for this variable (e.g., "DiscretePHVariable").
      Auto-populated by the metadata builder.
    from_schema: Variable
    rank: 1000
    designates_type: true
    alias: schema_class
    owner: CalculatedVariable
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
    owner: CalculatedVariable
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
    owner: CalculatedVariable
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
    owner: CalculatedVariable
    domain_of:
    - Variable
    range: string
    required: true

```
</details>