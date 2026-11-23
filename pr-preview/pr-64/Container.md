

# Class: Container



URI: [oae:Container](https://schema.oaedata.org/Container)






```mermaid
 classDiagram
    class Container
    click Container href "../Container"
      Container : datasets
        
          
    
    
    Container --> "*" Any : datasets
    click Any href "../Any"

        
      Container : experiments
        
          
    
    
    Container --> "*" Any : experiments
    click Any href "../Any"

        
      Container : metadata_builder_version
        
      Container : project
        
          
    
    
    Container --> "0..1" Project : project
    click Project href "../Project"

        
      Container : protocol_version
        
      Container : schema_version
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [project](project.md) | 0..1 <br/> [Project](Project.md) |  | direct |
| [experiments](experiments.md) | * <br/> [Any](Any.md)&nbsp;or&nbsp;<br />[Experiment](Experiment.md)&nbsp;or&nbsp;<br />[InSituExperiment](InSituExperiment.md)&nbsp;or&nbsp;<br />[Model](Model.md)&nbsp;or&nbsp;<br />[Intervention](Intervention.md)&nbsp;or&nbsp;<br />[Tracer](Tracer.md)&nbsp;or&nbsp;<br />[InterventionWithTracer](InterventionWithTracer.md) |  | direct |
| [datasets](datasets.md) | * <br/> [Any](Any.md)&nbsp;or&nbsp;<br />[Dataset](Dataset.md)&nbsp;or&nbsp;<br />[FieldDataset](FieldDataset.md)&nbsp;or&nbsp;<br />[ModelOutputDataset](ModelOutputDataset.md) |  | direct |
| [protocol_version](protocol_version.md) | 0..1 <br/> [String](String.md) | Version of the OAE Data Management Protocol the schema is based on: 1 | direct |
| [schema_version](schema_version.md) | 0..1 <br/> [String](String.md) | Version of this schema the file follows, such as 0 | direct |
| [metadata_builder_version](metadata_builder_version.md) | 0..1 <br/> [String](String.md) | Version of the Metadata Builder that wrote the file, in the same form as sche... | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:Container |
| native | oae:Container |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Container
from_schema: https://schema.oaedata.org/OAEDataSchema
attributes:
  project:
    name: project
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    domain_of:
    - Container
    range: Project
  experiments:
    name: experiments
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    domain_of:
    - Container
    range: Any
    multivalued: true
    any_of:
    - range: Experiment
    - range: InSituExperiment
    - range: Model
    - range: Intervention
    - range: Tracer
    - range: InterventionWithTracer
  datasets:
    name: datasets
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    domain_of:
    - Container
    range: Any
    multivalued: true
    any_of:
    - range: Dataset
    - range: FieldDataset
    - range: ModelOutputDataset
  protocol_version:
    name: protocol_version
    description: 'Version of the OAE Data Management Protocol the schema is based
      on: 1.0.0, https://doi.org/10.5281/zenodo.17154989.'
    from_schema: https://schema.oaedata.org/OAEDataSchema
    see_also:
    - https://doi.org/10.5281/zenodo.17154989
    rank: 1000
    domain_of:
    - Container
    range: string
    required: false
    equals_string: 1.0.0
  schema_version:
    name: schema_version
    description: 'Version of this schema the file follows, such as 0.7.0. A file built
      from an unreleased commit reads 0.6.1+dev.3c014f73: the last release, then the
      commit.'
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    domain_of:
    - Container
    range: string
    required: false
  metadata_builder_version:
    name: metadata_builder_version
    description: Version of the Metadata Builder that wrote the file, in the same
      form as schema_version.
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    domain_of:
    - Container
    range: string
    required: false
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Container
from_schema: https://schema.oaedata.org/OAEDataSchema
attributes:
  project:
    name: project
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: project
    owner: Container
    domain_of:
    - Container
    range: Project
  experiments:
    name: experiments
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: experiments
    owner: Container
    domain_of:
    - Container
    range: Any
    multivalued: true
    any_of:
    - range: Experiment
    - range: InSituExperiment
    - range: Model
    - range: Intervention
    - range: Tracer
    - range: InterventionWithTracer
  datasets:
    name: datasets
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: datasets
    owner: Container
    domain_of:
    - Container
    range: Any
    multivalued: true
    any_of:
    - range: Dataset
    - range: FieldDataset
    - range: ModelOutputDataset
  protocol_version:
    name: protocol_version
    description: 'Version of the OAE Data Management Protocol the schema is based
      on: 1.0.0, https://doi.org/10.5281/zenodo.17154989.'
    from_schema: https://schema.oaedata.org/OAEDataSchema
    see_also:
    - https://doi.org/10.5281/zenodo.17154989
    rank: 1000
    alias: protocol_version
    owner: Container
    domain_of:
    - Container
    range: string
    required: false
    equals_string: 1.0.0
  schema_version:
    name: schema_version
    description: 'Version of this schema the file follows, such as 0.7.0. A file built
      from an unreleased commit reads 0.6.1+dev.3c014f73: the last release, then the
      commit.'
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: schema_version
    owner: Container
    domain_of:
    - Container
    range: string
    required: false
  metadata_builder_version:
    name: metadata_builder_version
    description: Version of the Metadata Builder that wrote the file, in the same
      form as schema_version.
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: metadata_builder_version
    owner: Container
    domain_of:
    - Container
    range: string
    required: false
tree_root: true

```
</details>