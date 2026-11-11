

# Class: MeasuredDICFields


_Fields applied to all measured DIC variable types (discrete and continuous)_





URI: [oae:MeasuredDICFields](https://schema.oaedata.org/MeasuredDICFields)






```mermaid
 classDiagram
    class MeasuredDICFields
    click MeasuredDICFields href "../MeasuredDICFields"
      MeasuredDICFields <|-- ContinuousDICVariable
        click ContinuousDICVariable href "../ContinuousDICVariable"
      MeasuredDICFields <|-- DiscreteDICVariable
        click DiscreteDICVariable href "../DiscreteDICVariable"
      
      MeasuredDICFields : appropriate_use_quality
        
          
    
    
    MeasuredDICFields --> "0..1" AppropriateUseQuality : appropriate_use_quality
    click AppropriateUseQuality href "../AppropriateUseQuality"

        
      MeasuredDICFields : concentration_basis
        
          
    
    
    MeasuredDICFields --> "1" ConcentrationBasis : concentration_basis
    click ConcentrationBasis href "../ConcentrationBasis"

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [appropriate_use_quality](appropriate_use_quality.md) | 0..1 <br/> [AppropriateUseQuality](AppropriateUseQuality.md) | Climate quality is defined as measurements of quality sufficient to assess lo... | direct |
| [concentration_basis](concentration_basis.md) | 1 <br/> [ConcentrationBasis](ConcentrationBasis.md) | Whether measurements are expressed per unit volume or per unit mass (for DIC,... | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [ContinuousDICVariable](ContinuousDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous... |
| [DiscreteDICVariable](DiscreteDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle sampl... |








## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:MeasuredDICFields |
| native | oae:MeasuredDICFields |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MeasuredDICFields
description: Fields applied to all measured DIC variable types (discrete and continuous)
from_schema: https://schema.oaedata.org/OAEDataSchema
mixin: true
slots:
- appropriate_use_quality
- concentration_basis

```
</details>

### Induced

<details>
```yaml
name: MeasuredDICFields
description: Fields applied to all measured DIC variable types (discrete and continuous)
from_schema: https://schema.oaedata.org/OAEDataSchema
mixin: true
attributes:
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
    owner: MeasuredDICFields
    domain_of:
    - MeasuredTAFields
    - MeasuredDICFields
    - MeasuredPHFields
    - MeasuredCO2Fields
    range: AppropriateUseQuality
  concentration_basis:
    name: concentration_basis
    description: Whether measurements are expressed per unit volume or per unit mass
      (for DIC, TA, etc.)
    title: Per-volume vs per-mass based units
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: concentration_basis
    owner: MeasuredDICFields
    domain_of:
    - MeasuredTAFields
    - MeasuredDICFields
    range: ConcentrationBasis
    required: true

```
</details>