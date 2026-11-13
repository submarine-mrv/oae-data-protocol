

# Slot: Weather or climate quality (appropriate_use_quality)


_Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation._

_For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf._





URI: [oae:appropriate_use_quality](https://schema.oaedata.org/appropriate_use_quality)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContinuousTAVariable](ContinuousTAVariable.md) | Total Alkalinity (TA) measured variable from continuous autonomous sensor |  no  |
| [DiscreteTAVariable](DiscreteTAVariable.md) | Total Alkalinity (TA) measured variable from discrete bottle samples |  no  |
| [DiscreteDICVariable](DiscreteDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle sampl... |  no  |
| [ContinuousDICVariable](ContinuousDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous... |  no  |
| [MeasuredDICFields](MeasuredDICFields.md) | Fields applied to all measured DIC variable types (discrete and continuous) |  no  |
| [MeasuredPHFields](MeasuredPHFields.md) | Fields applied to all measured pH variable types (discrete and continuous) |  no  |
| [MeasuredCO2Fields](MeasuredCO2Fields.md) | Fields applied to all measured CO2 variable types (discrete and continuous) |  no  |
| [ContinuousPHVariable](ContinuousPHVariable.md) | pH measured variable from continuous autonomous sensor |  no  |
| [DiscreteCO2Variable](DiscreteCO2Variable.md) | CO2 discrete (bottle) measured variable (pCO2/fCO2) |  no  |
| [MeasuredTAFields](MeasuredTAFields.md) | Fields applied to all measured TA variable types (discrete and continuous) |  no  |
| [DiscretePHVariable](DiscretePHVariable.md) | pH measured variable with dye-based spectrophotometric measurement |  no  |
| [ContinuousCO2Variable](ContinuousCO2Variable.md) | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2) |  no  |







## Properties

* Range: [AppropriateUseQuality](AppropriateUseQuality.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:appropriate_use_quality |
| native | oae:appropriate_use_quality |




## LinkML Source

<details>
```yaml
name: appropriate_use_quality
description: 'Climate quality is defined as measurements of quality sufficient to
  assess long term trends with a defined level of confidence. Weather quality is defined
  as measurements of quality sufficient to identify relative spatial patterns and
  short term variation.

  For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P.
  & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and
  Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.'
title: Weather or climate quality
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: appropriate_use_quality
domain_of:
- MeasuredTAFields
- MeasuredDICFields
- MeasuredPHFields
- MeasuredCO2Fields
range: AppropriateUseQuality

```
</details>