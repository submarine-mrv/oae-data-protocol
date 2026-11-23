

# Slot: Alkalinity Feedstock Description (alkalinity_feedstock_description)


_Information such as feedstock source, characteristics, impurities, dilution prior to dosing, and concentration. For feedstock other than NaOH: trace metal composition and particulate grain size. Any variable information must be provided in the dosing data file, in this case include the data file and column header names here provided as variables. See [Intervention Data](https://www.carbontosea.org/oae-data-protocol/1-0-0/#intervention-data) for details._





URI: [oae:alkalinity_feedstock_description](https://schema.oaedata.org/alkalinity_feedstock_description)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionDetails](InterventionDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing t... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:alkalinity_feedstock_description |
| native | oae:alkalinity_feedstock_description |




## LinkML Source

<details>
```yaml
name: alkalinity_feedstock_description
description: 'Information such as feedstock source, characteristics, impurities, dilution
  prior to dosing, and concentration. For feedstock other than NaOH: trace metal composition
  and particulate grain size. Any variable information must be provided in the dosing
  data file, in this case include the data file and column header names here provided
  as variables. See [Intervention Data](https://www.carbontosea.org/oae-data-protocol/1-0-0/#intervention-data)
  for details.'
title: Alkalinity Feedstock Description
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: alkalinity_feedstock_description
owner: InterventionDetails
domain_of:
- InterventionDetails
range: string
required: true

```
</details>