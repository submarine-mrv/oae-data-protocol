# Controlled Vocabularies

The OAE Data Protocol uses controlled vocabularies to standardize categorical values across metadata submissions. Some are defined as part of the protocol, while others reference established community standards.

For detailed definitions of each vocabulary, see the [Controlled Vocabularies](https://www.carbontosea.org/oae-data-protocol/1-0-0/#controlled-vocabularies) section of the OAE Data Protocol website.

## Community Standard Vocabularies

The following vocabularies are sourced from established oceanographic & scientific community standards:

| Vocabulary | Source                                                                                                                                                                                     | Used For |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| **Sea Names** | NERC [SDN:C16](https://vocab.nerc.ac.uk/collection/C16/current/)                                                                                                                           | Project geographic classification |
| **[Platform Type](https://www.carbontosea.org/oae-data-protocol/1-0-0/#platform-type)** | NERC [SDN:L06](https://vocab.nerc.ac.uk/collection/L06/current/)                                                                                                                           | Dataset platform classification |
| **[Instrument Type](https://www.carbontosea.org/oae-data-protocol/1-0-0/#instrument-type)** | NERC [SDN:L05](https://vocab.nerc.ac.uk/collection/L05/current/), [SDN:L22](https://vocab.nerc.ac.uk/collection/L22/current/), [SDN:B75](https://vocab.nerc.ac.uk/collection/B75/current/) | Sampling and analyzing instruments |
| **Units** | [QUDT](https://qudt.org/vocab/unit/)                                                                                                                                                       | Dosing concentration units |

## OAE Data Protocol Vocabularies

These vocabularies are defined as part of the [OAE Data Protocol](https://www.carbontosea.org/oae-data-protocol/1-0-0/#controlled-vocabularies) and maintained in this schema.

### Classification

| Vocabulary | Values | Used By |
|-----------|--------|---------|
| [VariableType](elements/VariableType.md) | pH, ta, dic, co2, sediment, hplc, other, non_measured | All variables |
| [GenesisType](elements/GenesisType.md) | measured, calculated | In-situ variables |
| [SamplingType](elements/SamplingType.md) | discrete, continuous | Measured variables |
| [mCDR Experiment Type](elements/ExperimentType.md) | baseline, control, intervention, tracer_study, model, other | Experiments |
| [mCDR Data Type](elements/DatasetType.md) | cast, bottle, flow_thru, mooring, drifter, ... | Field datasets |
| [mCDR Pathways](elements/MCDRPathway.md) | ocean_alkalinity_enhancement, biomass_sinking, ... | Projects |

### Experiment & Intervention

| Vocabulary | Values | Used By |
|-----------|--------|---------|
| [Alkalinity Feedstock](elements/FeedstockType.md) | lime, olivine, magnesium_hydroxide, ... | Intervention experiments |
| [Alkalinity Feedstock Processing](elements/AlkalinityFeedstockProcessing.md) | electrochemistry, mineral_mining, ... | Intervention experiments |
| [Alkalinity Feedstock Form](elements/AlkalinityFeedstockForm.md) | powder,ite, solution, ... | Intervention experiments |
| [Equilibration Status](elements/EquilibrationStatus.md) | pre_equilibrated, not_equilibrated, ... | Intervention experiments |
| [Tracer Form](elements/TracerForm.md) | gas, dye, other | Tracer experiments |
| [Dosing Delivery Type](elements/DosingDeliveryType.md) | static_distributed, dynamic_ship_based, ... | Dosing details |
| [Hydrologic Location](elements/HydrologicLocation.md) | ocean, river, estuary, ... | Dosing details |

### Variable & Instrument

| Vocabulary | Values | Used By |
|-----------|--------|---------|
| [Observation Type](elements/ObservationType.md) | profile, surface_underway, time_series, ... | Measured variables |
| [Appropriate Use Quality](elements/AppropriateUseQuality.md) | climate, weather, other | Specific measured types |
| [Calibration Location](elements/CalibrationLocation.md) | factory, lab, field | Calibration records |
