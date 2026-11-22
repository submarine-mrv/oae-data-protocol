

# Class: InSituVariable


_Base class for project-acquired variables (measured or calculated in-situ). Reference: OAPMetadata XSD variables.xsd - insitu_variable_




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [oae:InSituVariable](https://schema.oaedata.org/InSituVariable)






```mermaid
 classDiagram
    class InSituVariable
    click InSituVariable href "../InSituVariable"
      FieldVariable <|-- InSituVariable
        click FieldVariable href "../FieldVariable"
      

      InSituVariable <|-- MeasuredVariable
        click MeasuredVariable href "../MeasuredVariable"
      InSituVariable <|-- CalculatedVariable
        click CalculatedVariable href "../CalculatedVariable"
      InSituVariable <|-- SocioeconomicVariable
        click SocioeconomicVariable href "../SocioeconomicVariable"
      
      
      InSituVariable : dataset_variable_name
        
      InSituVariable : dataset_variable_name_qc_flag
        
      InSituVariable : dataset_variable_name_raw
        
      InSituVariable : genesis
        
          
    
    
    InSituVariable --> "1" GenesisType : genesis
    click GenesisType href "../GenesisType"

        
      InSituVariable : long_name
        
      InSituVariable : measurement_researcher
        
          
    
    
    InSituVariable --> "0..1" Person : measurement_researcher
    click Person href "../Person"

        
      InSituVariable : method_reference
        
      InSituVariable : other_detailed_information
        
      InSituVariable : schema_class
        
      InSituVariable : standard_identifier
        
          
    
    
    InSituVariable --> "0..1" VocabularyItemReference : standard_identifier
    click VocabularyItemReference href "../VocabularyItemReference"

        
      InSituVariable : units
        
      InSituVariable : variable_type
        
          
    
    
    InSituVariable --> "1" VariableType : variable_type
    click VariableType href "../VariableType"

        
      
```





## Inheritance
* [Variable](Variable.md)
    * [FieldVariable](FieldVariable.md)
        * **InSituVariable**
            * [MeasuredVariable](MeasuredVariable.md) [ [QCFields](QCFields.md)]
            * [CalculatedVariable](CalculatedVariable.md) [ [QCFields](QCFields.md)]
            * [SocioeconomicVariable](SocioeconomicVariable.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [genesis](genesis.md) | 1 <br/> [GenesisType](GenesisType.md) |  | direct |
| [dataset_variable_name_qc_flag](dataset_variable_name_qc_flag.md) | 0..1 <br/> [String](String.md) | If applicable, the column header name used for the quality control flag corre... | direct |
| [dataset_variable_name_raw](dataset_variable_name_raw.md) | 0..1 <br/> [String](String.md) | If applicable, the column header name used for the raw data corresponding to ... | direct |
| [other_detailed_information](other_detailed_information.md) | 0..1 <br/> [String](String.md) | Any additional information about this variable | direct |
| [method_reference](method_reference.md) | 0..1 <br/> [String](String.md) | Citation for the method used | direct |
| [measurement_researcher](measurement_researcher.md) | 0..1 <br/> [Person](Person.md) | The name of the PI whose research team measured or derived this parameter | direct |
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
| self | oae:InSituVariable |
| native | oae:InSituVariable |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InSituVariable
description: 'Base class for project-acquired variables (measured or calculated in-situ).
  Reference: OAPMetadata XSD variables.xsd - insitu_variable'
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: FieldVariable
abstract: true
slot_usage:
  units:
    name: units
    required: true
attributes:
  genesis:
    name: genesis
    from_schema: Variable
    rank: 1000
    domain_of:
    - InSituVariable
    range: GenesisType
    required: true
  dataset_variable_name_qc_flag:
    name: dataset_variable_name_qc_flag
    description: If applicable, the column header name used for the quality control
      flag corresponding to this variable.
    title: Dataset variable name (Quality Flag)
    from_schema: Variable
    rank: 1000
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
    domain_of:
    - InSituVariable
    range: string
  other_detailed_information:
    name: other_detailed_information
    description: Any additional information about this variable.
    title: Other Detailed Information
    from_schema: Variable
    rank: 1000
    domain_of:
    - InSituVariable
    range: string
  method_reference:
    name: method_reference
    description: Citation for the method used.
    title: Method Reference
    from_schema: Variable
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
    domain_of:
    - InSituVariable
    range: Person

```
</details>

### Induced

<details>
```yaml
name: InSituVariable
description: 'Base class for project-acquired variables (measured or calculated in-situ).
  Reference: OAPMetadata XSD variables.xsd - insitu_variable'
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: FieldVariable
abstract: true
slot_usage:
  units:
    name: units
    required: true
attributes:
  genesis:
    name: genesis
    from_schema: Variable
    rank: 1000
    alias: genesis
    owner: InSituVariable
    domain_of:
    - InSituVariable
    range: GenesisType
    required: true
  dataset_variable_name_qc_flag:
    name: dataset_variable_name_qc_flag
    description: If applicable, the column header name used for the quality control
      flag corresponding to this variable.
    title: Dataset variable name (Quality Flag)
    from_schema: Variable
    rank: 1000
    alias: dataset_variable_name_qc_flag
    owner: InSituVariable
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
    owner: InSituVariable
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
    owner: InSituVariable
    domain_of:
    - InSituVariable
    range: string
  method_reference:
    name: method_reference
    description: Citation for the method used.
    title: Method Reference
    from_schema: Variable
    alias: method_reference
    owner: InSituVariable
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
    owner: InSituVariable
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
    owner: InSituVariable
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
    owner: InSituVariable
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
    owner: InSituVariable
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
    owner: InSituVariable
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
    owner: InSituVariable
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
    owner: InSituVariable
    domain_of:
    - Variable
    range: string
    required: true

```
</details>