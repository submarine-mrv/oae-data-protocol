

# Slot: Description of mCDR Forcing (mcdr_forcing_description)


_Description of the mCDR forcing applied in the simulation (e.g., the alkalinity perturbation). Required when simulation_type is "perturbation"._





URI: [oae:mcdr_forcing_description](https://schema.oaedata.org/mcdr_forcing_description)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:mcdr_forcing_description |
| native | oae:mcdr_forcing_description |




## LinkML Source

<details>
```yaml
name: mcdr_forcing_description
description: Description of the mCDR forcing applied in the simulation (e.g., the
  alkalinity perturbation). Required when simulation_type is "perturbation".
title: Description of mCDR Forcing
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: mcdr_forcing_description
owner: ModelOutputDataset
domain_of:
- ModelOutputDataset
range: string

```
</details>