

# Class: Variable


_Abstract root for all variable types (including non-measured)_




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [oae:Variable](https://schema.oaedata.org/Variable)






```mermaid
 classDiagram
    class Variable
    click Variable href "../Variable"
      Variable <|-- FieldVariable
        click FieldVariable href "../FieldVariable"
      Variable <|-- ModelOutputVariable
        click ModelOutputVariable href "../ModelOutputVariable"
      
      Variable : dataset_variable_name
        
      Variable : long_name
        
      Variable : schema_class
        
      Variable : standard_identifier
        
          
    
    
    Variable --> "0..1" VocabularyItemReference : standard_identifier
    click VocabularyItemReference href "../VocabularyItemReference"

        
      Variable : units
        
      Variable : variable_type
        
          
    
    
    Variable --> "1" VariableType : variable_type
    click VariableType href "../VariableType"

        
      
```





## Inheritance
* **Variable**
    * [FieldVariable](FieldVariable.md)
    * [ModelOutputVariable](ModelOutputVariable.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [units](units.md) | 0..1 <br/> [String](String.md) | Unit of measurement for this variable | direct |
| [variable_type](variable_type.md) | 1 <br/> [VariableType](VariableType.md) | High-level classification of the variable | direct |
| [schema_class](schema_class.md) | 1 <br/> [String](String.md) | The schema class name for this variable (e | direct |
| [standard_identifier](standard_identifier.md) | 0..1 <br/> [VocabularyItemReference](VocabularyItemReference.md) | A term from a community vocabulary that identifies this variable | direct |
| [dataset_variable_name](dataset_variable_name.md) | 1 <br/> [String](String.md) | The name for the variable as it is identified in the dataset data file | direct |
| [long_name](long_name.md) | 1 <br/> [String](String.md) | Full descriptive name of the variable | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:Variable |
| native | oae:Variable |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Variable
description: Abstract root for all variable types (including non-measured)
from_schema: https://schema.oaedata.org/OAEDataSchema
abstract: true
slots:
- units
- variable_type
slot_usage:
  variable_type:
    name: variable_type
    required: true
attributes:
  schema_class:
    name: schema_class
    description: The schema class name for this variable (e.g., "DiscretePHVariable").
      Auto-populated by the metadata builder.
    from_schema: Variable
    rank: 1000
    designates_type: true
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
    domain_of:
    - Variable
    range: string
    required: true

```
</details>

### Induced

<details>
```yaml
name: Variable
description: Abstract root for all variable types (including non-measured)
from_schema: https://schema.oaedata.org/OAEDataSchema
abstract: true
slot_usage:
  variable_type:
    name: variable_type
    required: true
attributes:
  schema_class:
    name: schema_class
    description: The schema class name for this variable (e.g., "DiscretePHVariable").
      Auto-populated by the metadata builder.
    from_schema: Variable
    rank: 1000
    designates_type: true
    alias: schema_class
    owner: Variable
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
    owner: Variable
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
    owner: Variable
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
    owner: Variable
    domain_of:
    - Variable
    range: string
    required: true
  units:
    name: units
    description: Unit of measurement for this variable.
    title: Unit
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: units
    owner: Variable
    domain_of:
    - Variable
    range: string
  variable_type:
    name: variable_type
    description: High-level classification of the variable. Determines which standard
      identifiers are available and, combined with genesis and sampling, which schema
      class to use.
    title: Variable Type
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: variable_type
    owner: Variable
    domain_of:
    - Variable
    range: VariableType
    required: true

```
</details>