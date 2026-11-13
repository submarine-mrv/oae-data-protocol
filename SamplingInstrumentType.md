# Enum: SamplingInstrumentType



URI: [SamplingInstrumentType](SamplingInstrumentType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ctd_rosette | None | A CTD rosette consists of a metal frame that houses a collection of sensors a... |
| niskin_bottle | SDN_L05:30 | A device that collects an in-situ discrete water sample from any depth and re... |
| flow_through_system | SDN_L05:31 | A device that continuously supplies a flow of water either to an analytical i... |
| flask_for_discrete_co2_measurement | None | Such flasks are typically made of glass and have a capacity of around one lit... |
| biological_trawl | SDN_L05:23 | A net towed through the water column designed to sample free-swimming nekton ... |
| phytoplankton_net | SDN_L05:22 | Phytoplankton net is used to collect and identify phytoplankton, which are mi... |
| zooplankton_net | SDN_L05:22 | Zooplankton net is used to collect and identify zooplankton, which are micros... |
| edna_sampler | None | Environmental DNA (eDNA) samplers: used to collect and analyze genetic materi... |
| autonomous_sensor | None | A device used in the measurement of a variety of oceanographic variables that... |
| other | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [sampling_instrument_type](sampling_instrument_type.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: SamplingInstrumentType
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  ctd_rosette:
    text: ctd_rosette
    description: A CTD rosette consists of a metal frame that houses a collection
      of sensors and water sampling bottles (e.g., Niskin)
  niskin_bottle:
    text: niskin_bottle
    description: A device that collects an in-situ discrete water sample from any
      depth and returns it to the surface without contamination by the waters through
      which it passes, such as a water bottle.
    meaning: SDN_L05:30
  flow_through_system:
    text: flow_through_system
    description: A device that continuously supplies a flow of water either to an
      analytical instrument, over a sensor or from which samples may be drawn.
    meaning: SDN_L05:31
  flask_for_discrete_co2_measurement:
    text: flask_for_discrete_co2_measurement
    description: Such flasks are typically made of glass and have a capacity of around
      one liter. Seawater samples are collected from a specific depth using a Niskin
      bottle or other sampling device and transferred to the flask without exposing
      them to the air. The flask is then sealed with a stopper and transported to
      the laboratory for analysis.
  biological_trawl:
    text: biological_trawl
    description: A net towed through the water column designed to sample free-swimming
      nekton or fish
    meaning: SDN_L05:23
  phytoplankton_net:
    text: phytoplankton_net
    description: Phytoplankton net is used to collect and identify phytoplankton,
      which are microscopic plants that form the base of the marine food web.
    meaning: SDN_L05:22
  zooplankton_net:
    text: zooplankton_net
    description: Zooplankton net is used to collect and identify zooplankton, which
      are microscopic animals that feed on phytoplankton and are important prey for
      many marine organisms.
    meaning: SDN_L05:22
  edna_sampler:
    text: edna_sampler
    description: 'Environmental DNA (eDNA) samplers: used to collect and analyze genetic
      material shed by marine organisms, which can provide information about their
      distribution, abundance, and diversity.'
  autonomous_sensor:
    text: autonomous_sensor
    description: A device used in the measurement of a variety of oceanographic variables
      that functions autonomously
  other:
    text: other

```
</details>
