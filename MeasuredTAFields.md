

# Class: MeasuredTAFields


_Fields applied to all measured TA variable types (discrete and continuous)_





URI: [oae:MeasuredTAFields](https://schema.oaedata.org/MeasuredTAFields)






```mermaid
 classDiagram
    class MeasuredTAFields
    click MeasuredTAFields href "../MeasuredTAFields"
      MeasuredTAFields <|-- ContinuousTAVariable
        click ContinuousTAVariable href "../ContinuousTAVariable"
      MeasuredTAFields <|-- DiscreteTAVariable
        click DiscreteTAVariable href "../DiscreteTAVariable"
      
      MeasuredTAFields : appropriate_use_quality
        
          
    
    
    MeasuredTAFields --> "0..1" AppropriateUseQuality : appropriate_use_quality
    click AppropriateUseQuality href "../AppropriateUseQuality"

        
      MeasuredTAFields : concentration_basis
        
          
    
    
    MeasuredTAFields --> "1" ConcentrationBasis : concentration_basis
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
| [ContinuousTAVariable](ContinuousTAVariable.md) | Total Alkalinity (TA) measured variable from continuous autonomous sensor |
| [DiscreteTAVariable](DiscreteTAVariable.md) | Total Alkalinity (TA) measured variable from discrete bottle samples |








## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:MeasuredTAFields |
| native | oae:MeasuredTAFields |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MeasuredTAFields
description: Fields applied to all measured TA variable types (discrete and continuous)
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
name: MeasuredTAFields
description: Fields applied to all measured TA variable types (discrete and continuous)
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
    owner: MeasuredTAFields
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
    owner: MeasuredTAFields
    domain_of:
    - MeasuredTAFields
    - MeasuredDICFields
    range: ConcentrationBasis
    required: true

```
</details>