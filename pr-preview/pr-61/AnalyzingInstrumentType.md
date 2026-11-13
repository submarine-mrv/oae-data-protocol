# Enum: AnalyzingInstrumentType



URI: [AnalyzingInstrumentType](AnalyzingInstrumentType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ctd_sensor | SDN_L05:130 | A reusable instrument that always simultaneously measures conductivity and te... |
| flow_through_system | SDN_L05:31 | A device that continuously supplies a flow of water either to an analytical i... |
| thermosalinograph | SDN_L05:133 | Temperature and conductivity sensors mounted on a sea-surface platform contin... |
| salinometer_for_discrete_salinity_measurement | SDN_L05:LAB30 | Instruments that measure the salinity of a collected water sample based on it... |
| dic_analyzers_based_on_coulometers | None | DIC coulometers are widely used in oceanographic research to measure the conc... |
| dic_analyzers_based_on_co2_gas_detectors | None | DIC analyzers based on a CO2 gas detector including Non-dispersive infrared a... |
| autonomous_dic_sensor | SDN_L05:86 | Autonomous dissolved inorganic carbon (DIC) sensors are devices that can meas... |
| alkalinity_titrator | SDN_L05:LAB12 | An alkalinity titrator is a device used to measure the total alkalinity of a ... |
| autonomous_ta_sensor | None | Autonomous total alkalinity (TA) sensors are devices that can measure the con... |
| showerhead_equilibrator | SDN_L05:EQUIL | This type of equilibrator works by spraying seawater into a gas chamber, allo... |
| floating_air_water_equilibrator | SDN_L05:EQUIL | An "h"-shaped bubble equilibrator assembly commonly used in MAPCO2 systems on... |
| membrane_equilibrator | SDN_L05:EQUIL | While seawater is passed through a membrane, CO2 in the water diffuses across... |
| spectrophotometer | SDN_L05:LAB20 | Instruments measuring the relative absorption of electromagnetic radiation of... |
| handheld_ph_spectrophotometer | None | One example of a handheld pH spectrophotometer is the "pHyter" |
| ph_electrode | SDN_L05:355 | A pH electrode, sometimes referred to as a pH probe or pH sensor, is a glass ... |
| sea_bird_seafet_v1 | SDN_L22:TOOL1292 | A pH sensor |
| sea_bird_seafet_v2 | SDN_L22:TOOL1293 | A pH sensor |
| oxygen_titrator | SDN_L05:LAB12 | An oxygen titrator is a device used to measure the concentration of dissolved... |
| oxygen_sensor | SDN_L05:351 | An oxygen sensor or probe or sond, is an electronic device that measures the ... |
| sea_bird_seaphox | SDN_L22:TOOL1895 | Sea-Bird SeapHOx is a type of oceanographic instrument that measures both the... |
| ysi | SDN_B75:ORG00475 | YSI (Yellow Springs Instruments) is a company that produces a variety of wate... |
| nutrient_analyzer | SDN_L05:181 | Instrument that makes in-situ measurements of one or more of nitrate, nitrite... |
| fluorometers | SDN_L05:113 | Instrument that measures the amount of stimulated electromagnetic radiation p... |
| high_performance_liquid_chromatography | SDN_L05:LAB11 | Instruments that separate and analyse mixtures of substances by high pressure... |
| acoustic_doppler_current_profiler | SDN_L05:115 | Acoustic Doppler Current Profiler (ADCP), is a type of instrument used to mea... |
| mass_spectrometers | SDN_L05:LAB16 | Instruments used to measure the mass-to-charge ratio of ions most generally u... |
| isotope_ratio_mass_spectrometers | SDN_L05:LAB48 | Instruments that measure isotopic ratios using an electron ionisation source |
| barometric_pressure_sensor | SDN_L05:102 | Instrument that makes routine meteorological measurements on the atmosphere, ... |
| microscopes | SDN_L05:LAB05 | Instruments that generate enlarged images of samples using the phenomena of r... |
| scanning_electron_microscopes | SDN_L05:LAB07 | A scanning electron microscope (SEM) is a type of microscope that uses a focu... |
| flow_cytometers | SDN_L05:LAB37 | Instruments that suspend cells in a stream of fluid past detection sensors wh... |
| edna_sampler | None | Environmental DNA (eDNA) samplers: used to collect and analyze genetic materi... |
| gas_analyzer | None | TBD |
| other | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [instrument_type](instrument_type.md) | Type of instrument used to analyze samples or measure continuously |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema






## LinkML Source

<details>
```yaml
name: AnalyzingInstrumentType
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
permissible_values:
  ctd_sensor:
    text: ctd_sensor
    description: A reusable instrument that always simultaneously measures conductivity
      and temperature (for salinity) and pressure (for depth).
    meaning: SDN_L05:130
  flow_through_system:
    text: flow_through_system
    description: A device that continuously supplies a flow of water either to an
      analytical instrument, over a sensor or from which samples may be drawn.
    meaning: SDN_L05:31
  thermosalinograph:
    text: thermosalinograph
    description: Temperature and conductivity sensors mounted on a sea-surface platform
      continuously measuring a surface water supply.
    meaning: SDN_L05:133
  salinometer_for_discrete_salinity_measurement:
    text: salinometer_for_discrete_salinity_measurement
    description: Instruments that measure the salinity of a collected water sample
      based on its electrical conductivity or optical properties.
    meaning: SDN_L05:LAB30
  dic_analyzers_based_on_coulometers:
    text: dic_analyzers_based_on_coulometers
    description: DIC coulometers are widely used in oceanographic research to measure
      the concentration of dissolved inorganic carbon in seawater samples. They are
      often coupled with computer-controlled automated dynamic headspace analyzers
      that extracts total carbon dioxide from seawater using Single-Operator Multiparameter
      Metabolic Analyzers (SOMMAs).
  dic_analyzers_based_on_co2_gas_detectors:
    text: dic_analyzers_based_on_co2_gas_detectors
    description: DIC analyzers based on a CO2 gas detector including Non-dispersive
      infrared absorption (NDIR) (e.g., Licor LI-850), Cavity Enhanced Absorption
      Spectroscopy (e.g., Licor's LI-7815), and Cavity Ring-Down Spectroscopy (CRDS)
      (e.g., Picarro G2131i) detectors.
  autonomous_dic_sensor:
    text: autonomous_dic_sensor
    description: Autonomous dissolved inorganic carbon (DIC) sensors are devices that
      can measure the concentration of DIC in seawater or other natural waters in
      situ, without the need for manual sampling and laboratory analysis.
    meaning: SDN_L05:86
  alkalinity_titrator:
    text: alkalinity_titrator
    description: An alkalinity titrator is a device used to measure the total alkalinity
      of a seawater by titration.
    meaning: SDN_L05:LAB12
  autonomous_ta_sensor:
    text: autonomous_ta_sensor
    description: Autonomous total alkalinity (TA) sensors are devices that can measure
      the concentration of TA in seawater or other natural waters in situ, without
      the need for manual sampling and laboratory analysis.
  showerhead_equilibrator:
    text: showerhead_equilibrator
    description: This type of equilibrator works by spraying seawater into a gas chamber,
      allowing the CO2 in the water to equilibrate with a gas mixture in the chamber.
    meaning: SDN_L05:EQUIL
  floating_air_water_equilibrator:
    text: floating_air_water_equilibrator
    description: An "h"-shaped bubble equilibrator assembly commonly used in MAPCO2
      systems on moorings. For more information, refer to Friederich et al. (1995).
    meaning: SDN_L05:EQUIL
  membrane_equilibrator:
    text: membrane_equilibrator
    description: While seawater is passed through a membrane, CO2 in the water diffuses
      across the membrane and equilibrates with the gas mixture, which is then analyzed
      to determine the CO2 concentration.
    meaning: SDN_L05:EQUIL
  spectrophotometer:
    text: spectrophotometer
    description: Instruments measuring the relative absorption of electromagnetic
      radiation of different wavelengths in the near infra-red, visible and ultraviolet
      wavebands by samples.
    meaning: SDN_L05:LAB20
  handheld_ph_spectrophotometer:
    text: handheld_ph_spectrophotometer
    description: One example of a handheld pH spectrophotometer is the "pHyter". Refer
      to Pardis et al. (2022) for more details.
  ph_electrode:
    text: ph_electrode
    description: A pH electrode, sometimes referred to as a pH probe or pH sensor,
      is a glass device used to measure the pH of a solution.
    meaning: SDN_L05:355
  sea_bird_seafet_v1:
    text: sea_bird_seafet_v1
    description: A pH sensor. The sensor can be used for ocean acidification, research
      coral reef sensitivity analysis and environmental monitoring. The sensor measures
      pH with a range of 6.5 to 9.0. The sensing element is an ion sensitive field
      effect transistor. The pH sensor has an initial accuracy of +/-0.05 pH, precision
      of 0.001 pH and stability of 0.005 pH/month. It can operate in temperatures
      ranging from 0 deg C to 50 deg C and up to depths of 50 m.
    meaning: SDN_L22:TOOL1292
  sea_bird_seafet_v2:
    text: sea_bird_seafet_v2
    description: A pH sensor. The sensor can be used for ocean acidification, research
      coral reef sensitivity analysis and environmental monitoring. The sensor measures
      pH with a range of 6.5 to 9.0. The sensing element is an ion sensitive field
      effect transistor. V2 implements improvements to the original SeaFET's reliability,
      data quality, ease of operation, and deployment endurance, with significant
      changes to how users interface with the instrument. The pH sensor has an accuracy
      to +/-0.05 pH, precision of 0.004 pH and stability of 0.003 pH/month. It can
      operate in temperatures ranging from 0 deg C to 50 deg C and up to depths of
      50 m.
    meaning: SDN_L22:TOOL1293
  oxygen_titrator:
    text: oxygen_titrator
    description: An oxygen titrator is a device used to measure the concentration
      of dissolved oxygen in a water sample, as required for the Winkler method.
    meaning: SDN_L05:LAB12
  oxygen_sensor:
    text: oxygen_sensor
    description: An oxygen sensor or probe or sond, is an electronic device that measures
      the concentration of dissolved oxygen in the ocean.
    meaning: SDN_L05:351
  sea_bird_seaphox:
    text: sea_bird_seaphox
    description: Sea-Bird SeapHOx is a type of oceanographic instrument that measures
      both the pH and dissolved oxygen concentration of seawater in real-time.
    meaning: SDN_L22:TOOL1895
  ysi:
    text: ysi
    description: YSI (Yellow Springs Instruments) is a company that produces a variety
      of water quality monitoring instruments. The YSI sensors are designed to measure
      a wide range of parameters, including temperature, salinity, and dissolved oxygen.
    meaning: SDN_B75:ORG00475
  nutrient_analyzer:
    text: nutrient_analyzer
    description: Instrument that makes in-situ measurements of one or more of nitrate,
      nitrite, ammonium, urea, phosphate or silicate dissolved in the water column.
    meaning: SDN_L05:181
  fluorometers:
    text: fluorometers
    description: Instrument that measures the amount of stimulated electromagnetic
      radiation produced by pulses of electromagnetic radiation emitted into the water
      column.
    meaning: SDN_L05:113
  high_performance_liquid_chromatography:
    text: high_performance_liquid_chromatography
    description: Instruments that separate and analyse mixtures of substances by high
      pressure pumping the sample through a column packed with microspheres coated
      with the stationary phase.
    meaning: SDN_L05:LAB11
  acoustic_doppler_current_profiler:
    text: acoustic_doppler_current_profiler
    description: Acoustic Doppler Current Profiler (ADCP), is a type of instrument
      used to measure water currents in oceans, rivers, and other bodies of water.
    meaning: SDN_L05:115
  mass_spectrometers:
    text: mass_spectrometers
    description: Instruments used to measure the mass-to-charge ratio of ions most
      generally used to find the composition of a sample by generating a mass spectrum
      representing the masses of sample components.
    meaning: SDN_L05:LAB16
  isotope_ratio_mass_spectrometers:
    text: isotope_ratio_mass_spectrometers
    description: Instruments that measure isotopic ratios using an electron ionisation
      source. Atoms in purified samples are ionised using a beam of electrons under
      vacuum. Subsequently, ions are focused into a beam by an electromagnet and then
      separated into individual beams based on their mass/charge ratio
    meaning: SDN_L05:LAB48
  barometric_pressure_sensor:
    text: barometric_pressure_sensor
    description: Instrument that makes routine meteorological measurements on the
      atmosphere, typically air pressure, temperature and humidity
    meaning: SDN_L05:102
  microscopes:
    text: microscopes
    description: Instruments that generate enlarged images of samples using the phenomena
      of reflection and absorption of visible light. Includes conventional and inverted
      instruments
    meaning: SDN_L05:LAB05
  scanning_electron_microscopes:
    text: scanning_electron_microscopes
    description: A scanning electron microscope (SEM) is a type of microscope that
      uses a focused beam of electrons to create high-resolution images of the surface
      of a specimen.
    meaning: SDN_L05:LAB07
  flow_cytometers:
    text: flow_cytometers
    description: Instruments that suspend cells in a stream of fluid past detection
      sensors whilst illuminating them with laser light. Used for cell counting, sorting,
      biomarker detection and protein engineering.
    meaning: SDN_L05:LAB37
  edna_sampler:
    text: edna_sampler
    description: 'Environmental DNA (eDNA) samplers: used to collect and analyze genetic
      material shed by marine organisms, which can provide information about their
      distribution, abundance, and diversity.'
  gas_analyzer:
    text: gas_analyzer
    description: TBD
  other:
    text: other

```
</details>
