# Enum: DatasetType




_Type of dataset being submitted. This usually _



URI: [DatasetType](DatasetType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| dosing | None | Variables such as dosing_onoff, dosing_rate, and flow_rate should be included... |
| cast | None | Vertical profiles (e |
| bottle | None | Any other types of measurements from water samples collected at discrete dept... |
| flow_thru | None | Continuous data (e |
| pigment | None | For laboratory measured pigment data (e |
| marine_snow_catcher | None | For various types of marine snow catcher data |
| mooring | None | Moored and buoy data |
| drifter | None | Drifter and drogue data |
| airborne | None | Measurements made via an aircraft |
| diver | None | For measurements made by a diver |
| auv | None | Measurements made by an autonomous underwater vehicle |
| asv | None | Measurements made by an autonomous surface vehicle |
| experimental | None | Measurements that have a non-geospatial aspect (e |
| sediment_trap | None | Measurements from a sediment trap platform |
| taxonomy | None | Data whose purpose is the classification or annotation of phytoplankton, zoop... |
| sediment | None | Measurements from sediment samples (e |
| model_output | None | Data output from model experiments |
| socioeconomic | None | Information (quantitative or qualitative) from socioeconomic studies |
| net_tow | None | For measurements captured via net (e |
| underway | None | Data collected continuously from a moving platform (e |
| other | None | For data types not included in the controlled vocabulary |




## Slots

| Name | Description |
| ---  | --- |
| [dataset_type](dataset_type.md) | Selected controlled vocabularies for data types relevant to mCDR have been re... |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: DatasetType
description: 'Type of dataset being submitted. This usually '
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  dosing:
    text: dosing
    description: Variables such as dosing_onoff, dosing_rate, and flow_rate should
      be included here.
  cast:
    text: cast
    description: Vertical profiles (e.g., optical packages, CTD)
  bottle:
    text: bottle
    description: Any other types of measurements from water samples collected at discrete
      depths (e.g., nutrients)
  flow_thru:
    text: flow_thru
    description: Continuous data (e.g., shipboard, underway flow through system)
  pigment:
    text: pigment
    description: For laboratory measured pigment data (e.g. fluorometry, spectrophotometry,
      HPLC)
  marine_snow_catcher:
    text: marine_snow_catcher
    description: For various types of marine snow catcher data
  mooring:
    text: mooring
    description: Moored and buoy data
  drifter:
    text: drifter
    description: Drifter and drogue data
  airborne:
    text: airborne
    description: Measurements made via an aircraft
  diver:
    text: diver
    description: For measurements made by a diver
  auv:
    text: auv
    description: Measurements made by an autonomous underwater vehicle
  asv:
    text: asv
    description: Measurements made by an autonomous surface vehicle
  experimental:
    text: experimental
    description: Measurements that have a non-geospatial aspect (e.g., incubations
      or other laboratory measurements, etc.)
  sediment_trap:
    text: sediment_trap
    description: Measurements from a sediment trap platform
  taxonomy:
    text: taxonomy
    description: Data whose purpose is the classification or annotation of phytoplankton,
      zooplankton, or other marine groups.
  sediment:
    text: sediment
    description: Measurements from sediment samples (e.g., core samples, grab samples)
  model_output:
    text: model_output
    description: Data output from model experiments
  socioeconomic:
    text: socioeconomic
    description: Information (quantitative or qualitative) from socioeconomic studies
  net_tow:
    text: net_tow
    description: For measurements captured via net (e.g., zooplankton via MOCNESS)
  underway:
    text: underway
    description: Data collected continuously from a moving platform (e.g., ship underway
      system sampling surface seawater during transit).
  other:
    text: other
    description: For data types not included in the controlled vocabulary. Please
      fill in a the `dataset_type_custom` field with a more specific name for the
      custom mCDR data type.

```
</details>
