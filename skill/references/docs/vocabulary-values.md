# Vocabulary Values

What each value means, for the vocabularies whose values need explaining, and the names behind the
sea-name and platform-type URIs. Generated from the schema and the NERC vocabularies. A vocabulary
that is not listed has self-explanatory values; see its own page.

## AlkalinityFeedstockForm

Physical form of the alkalinity feedstock upon ocean delivery

- `solid`: Involves adding alkaline minerals or particulate slurry (such as MgOH2, MgO, or CaO) to seawater or river systems either directly, through coastal outfalls (such as wastewater), or at breaking shorelines to increase its alkalinity.
- `aqueous`: Aqueous alkalinity addition may use electrochemistry or fully dissolved mineral feedstock to increase seawater alkalinity.
- `slurry`: Slurry alkalinity additions include a mix of solid and aqueous alkalinity forms, where the solid alkaline particulates are suspended in a solution.

## AlkalinityFeedstockProcessing

Methods used to process alkalinity feedstock

- `electrochemistry`: Alkalinity generated via electrochemical processes (e.g., seawater electrolysis).
- `synthetically_derived`: Intentionally industrially manufactured chemical compounds (e.g., Ca(OH)2 via lime kilns).
- `mineral_mining`: Mined geological material, including purified mineral or natural rock.
- `blended`: A mix of multiple sources.
- `other`: Unclassified or novel; include a description in Experiment Description.

## AnalyzingInstrumentType

- `ctd_sensor`: A reusable instrument that always simultaneously measures conductivity and temperature (for salinity) and pressure (for depth).
- `flow_through_system`: A device that continuously supplies a flow of water either to an analytical instrument, over a sensor or from which samples may be drawn.
- `thermosalinograph`: Temperature and conductivity sensors mounted on a sea-surface platform continuously measuring a surface water supply.
- `salinometer_for_discrete_salinity_measurement`: Instruments that measure the salinity of a collected water sample based on its electrical conductivity or optical properties.
- `dic_analyzers_based_on_coulometers`: DIC coulometers are widely used in oceanographic research to measure the concentration of dissolved inorganic carbon in seawater samples. They are often coupled with computer-controlled automated dynamic headspace analyzers that extracts total carbon dioxide from seawater using Single-Operator Multiparameter Metabolic Analyzers (SOMMAs).
- `dic_analyzers_based_on_co2_gas_detectors`: DIC analyzers based on a CO2 gas detector including Non-dispersive infrared absorption (NDIR) (e.g., Licor LI-850), Cavity Enhanced Absorption Spectroscopy (e.g., Licor's LI-7815), and Cavity Ring-Down Spectroscopy (CRDS) (e.g., Picarro G2131i) detectors.
- `autonomous_dic_sensor`: Autonomous dissolved inorganic carbon (DIC) sensors are devices that can measure the concentration of DIC in seawater or other natural waters in situ, without the need for manual sampling and laboratory analysis.
- `alkalinity_titrator`: An alkalinity titrator is a device used to measure the total alkalinity of a seawater by titration.
- `autonomous_ta_sensor`: Autonomous total alkalinity (TA) sensors are devices that can measure the concentration of TA in seawater or other natural waters in situ, without the need for manual sampling and laboratory analysis.
- `showerhead_equilibrator`: This type of equilibrator works by spraying seawater into a gas chamber, allowing the CO2 in the water to equilibrate with a gas mixture in the chamber.
- `floating_air_water_equilibrator`: An "h"-shaped bubble equilibrator assembly commonly used in MAPCO2 systems on moorings. For more information, refer to Friederich et al. (1995).
- `membrane_equilibrator`: While seawater is passed through a membrane, CO2 in the water diffuses across the membrane and equilibrates with the gas mixture, which is then analyzed to determine the CO2 concentration.
- `spectrophotometer`: Instruments measuring the relative absorption of electromagnetic radiation of different wavelengths in the near infra-red, visible and ultraviolet wavebands by samples.
- `handheld_ph_spectrophotometer`: One example of a handheld pH spectrophotometer is the "pHyter". Refer to Pardis et al. (2022) for more details.
- `ph_electrode`: A pH electrode, sometimes referred to as a pH probe or pH sensor, is a glass device used to measure the pH of a solution.
- `sea_bird_seafet_v1`: A pH sensor. The sensor can be used for ocean acidification, research coral reef sensitivity analysis and environmental monitoring. The sensor measures pH with a range of 6.5 to 9.0. The sensing element is an ion sensitive field effect transistor. The pH sensor has an initial accuracy of +/-0.05 pH, precision of 0.001 pH and stability of 0.005 pH/month. It can operate in temperatures ranging from 0 deg C to 50 deg C and up to depths of 50 m.
- `sea_bird_seafet_v2`: A pH sensor. The sensor can be used for ocean acidification, research coral reef sensitivity analysis and environmental monitoring. The sensor measures pH with a range of 6.5 to 9.0. The sensing element is an ion sensitive field effect transistor. V2 implements improvements to the original SeaFET's reliability, data quality, ease of operation, and deployment endurance, with significant changes to how users interface with the instrument. The pH sensor has an accuracy to +/-0.05 pH, precision of 0.004 pH and stability of 0.003 pH/month. It can operate in temperatures ranging from 0 deg C to 50 deg C and up to depths of 50 m.
- `oxygen_titrator`: An oxygen titrator is a device used to measure the concentration of dissolved oxygen in a water sample, as required for the Winkler method.
- `oxygen_sensor`: An oxygen sensor or probe or sond, is an electronic device that measures the concentration of dissolved oxygen in the ocean.
- `sea_bird_seaphox`: Sea-Bird SeapHOx is a type of oceanographic instrument that measures both the pH and dissolved oxygen concentration of seawater in real-time.
- `ysi`: YSI (Yellow Springs Instruments) is a company that produces a variety of water quality monitoring instruments. The YSI sensors are designed to measure a wide range of parameters, including temperature, salinity, and dissolved oxygen.
- `nutrient_analyzer`: Instrument that makes in-situ measurements of one or more of nitrate, nitrite, ammonium, urea, phosphate or silicate dissolved in the water column.
- `fluorometers`: Instrument that measures the amount of stimulated electromagnetic radiation produced by pulses of electromagnetic radiation emitted into the water column.
- `high_performance_liquid_chromatography`: Instruments that separate and analyse mixtures of substances by high pressure pumping the sample through a column packed with microspheres coated with the stationary phase.
- `acoustic_doppler_current_profiler`: Acoustic Doppler Current Profiler (ADCP), is a type of instrument used to measure water currents in oceans, rivers, and other bodies of water.
- `mass_spectrometers`: Instruments used to measure the mass-to-charge ratio of ions most generally used to find the composition of a sample by generating a mass spectrum representing the masses of sample components.
- `isotope_ratio_mass_spectrometers`: Instruments that measure isotopic ratios using an electron ionisation source. Atoms in purified samples are ionised using a beam of electrons under vacuum. Subsequently, ions are focused into a beam by an electromagnet and then separated into individual beams based on their mass/charge ratio
- `barometric_pressure_sensor`: Instrument that makes routine meteorological measurements on the atmosphere, typically air pressure, temperature and humidity
- `microscopes`: Instruments that generate enlarged images of samples using the phenomena of reflection and absorption of visible light. Includes conventional and inverted instruments
- `scanning_electron_microscopes`: A scanning electron microscope (SEM) is a type of microscope that uses a focused beam of electrons to create high-resolution images of the surface of a specimen.
- `flow_cytometers`: Instruments that suspend cells in a stream of fluid past detection sensors whilst illuminating them with laser light. Used for cell counting, sorting, biomarker detection and protein engineering.
- `edna_sampler`: Environmental DNA (eDNA) samplers: used to collect and analyze genetic material shed by marine organisms, which can provide information about their distribution, abundance, and diversity.
- `gas_analyzer`: TBD
- `other`

## CalibrationLocation

Where the calibration was performed.

- `factory`: Factory calibration performed by manufacturer.
- `lab`: Laboratory calibration.
- `field`: Field calibration performed during deployment.

## ConcentrationBasis

Whether concentration measurements are expressed per unit volume or per unit mass.

- `per_volume`: Concentration expressed per unit volume (e.g., μmol/L, mmol/L)
- `per_mass`: Concentration expressed per unit mass (e.g., μmol/kg-seawater)

## DataAccessibility

Level of access to a dataset.

- `open_access`: Data are freely available now, without restriction.
- `conditional_access`: Data are available upon request, subject to review.
- `scheduled_access`: Data will become openly available after a specified date.

## DataProductType

- `originally_collected_dataset`: A dataset collected from a research cruise or laboratory experiment
- `data_compilation_product`: (e.g., SOCAT, GLODAP)
- `derived_product`: (e.g. gridded products, or model output).

## DatasetType

Type of dataset being submitted. This usually

- `dosing`: Variables such as dosing_onoff, dosing_rate, and flow_rate should be included here.
- `cast`: Vertical profiles (e.g., optical packages, CTD)
- `bottle`: Any other types of measurements from water samples collected at discrete depths (e.g., nutrients)
- `flow_thru`: Continuous data (e.g., shipboard, underway flow through system)
- `pigment`: For laboratory measured pigment data (e.g. fluorometry, spectrophotometry, HPLC)
- `marine_snow_catcher`: For various types of marine snow catcher data
- `mooring`: Moored and buoy data
- `drifter`: Drifter and drogue data
- `airborne`: Measurements made via an aircraft
- `diver`: For measurements made by a diver
- `auv`: Measurements made by an autonomous underwater vehicle
- `asv`: Measurements made by an autonomous surface vehicle
- `experimental`: Measurements that have a non-geospatial aspect (e.g., incubations or other laboratory measurements, etc.)
- `sediment_trap`: Measurements from a sediment trap platform
- `taxonomy`: Data whose purpose is the classification or annotation of phytoplankton, zooplankton, or other marine groups.
- `sediment`: Measurements from sediment samples (e.g., core samples, grab samples)
- `model_output`: Data output from model experiments
- `socioeconomic`: Information (quantitative or qualitative) from socioeconomic studies
- `net_tow`: For measurements captured via net (e.g., zooplankton via MOCNESS)
- `underway`: Data collected continuously from a moving platform (e.g., ship underway system sampling surface seawater during transit).
- `other`: For data types not included in the controlled vocabulary. Please fill in a the `dataset_type_custom` field with a more specific name for the custom mCDR data type.

## DosingDeliveryType

Types of dosing delivery methods

- `static_point_source`: A single dosing location that does not move, such as an outfall pipe from a static platform. The dosing rate may change over time.
- `variable_point_source`: A dosing location that moves: a single location at each time step, such as an outflow from a mobile platform such as a ship or surface vessel. "Variable" refers to the location, not the dosing rate.
- `static_distributed`: A set location or locations of dosing that is not a point source, such as a distributed area over the seafloor or a diffusor.
- `variable_distributed`: A distributed dosing area that varies in time, such as manually placed alkaline material over different areas at different times.

## EquilibrationStatus

Equilibration status of the alkalinity feedstock

- `pre_equilibrated`: Pre-equilibrated with atmosphere before dosing
- `unequilibrated`: Not pre-equilibrated before dosing

## ExperimentType

Types of mCDR experiments

- `baseline`: Baseline measurements taken before any intervention
- `control`: Control experiment without intervention for comparison
- `intervention`: Experiment with active OAE intervention
- `tracer_study`: Tracer study experiment (eg- dye or gas tracer study)
- `model`: Model-based experiment or simulation
- `other`: Other experiment type not covered by standard categories

## FeedstockType

Types of materials used for alkalinity addition, as sourced from NCEI's OCADS controlled vocabulary: https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/vocabularies/alkalinization-types.html

- `lime`: Lime (CaO) used as an alkalinity source.
- `portlandite`: Portlandite (Ca(OH)₂) used as an alkalinity source.
- `calcium_carbonate`: Calcium carbonate (CaCO₃) used as an alkalinity source.
- `anorthite`: Anorthite (CaAl₂Si₂O₈) used as an alkalinity source.
- `dolomite`: Dolomite (CaMg(CO₃)₂) used as an alkalinity source.
- `periclase`: Periclase (MgO) used as an alkalinity source.
- `brucite`: Brucite (Mg(OH)₂) used as an alkalinity source.
- `magnesite`: Magnesite (MgCO₃) used as an alkalinity source.
- `forsterite`: Forsterite (Mg₂SiO₄) used as an alkalinity source.
- `mg_rich_olivine`: Magnesium-rich olivine used as an alkalinity source.
- `sodium_hydroxide`: NaOH used as an alkalinity source.
- `natrite`: Natrite (Na₂CO₃) used as an alkalinity source.
- `nahcolite`: Nahcolite (NaHCO₃) used as an alkalinity source.
- `other`: Enter a custom value in the field provided

## GridType

Type of grid in a multi-grid or nested model configuration

- `inner_grid`: Inner (nested, higher-resolution) grid
- `outer_grid`: Outer (coarser-resolution) grid
- `single_grid`: Single grid (no nesting)

## HydrologicLocation

Hydrologic location types for dosing

- `coastal_surface`: Surface waters in coastal areas
- `offshore_surface`: Surface waters in offshore areas
- `river`: River systems
- `wetland`: Wetland areas
- `seafloor`: Seafloor or benthic zone

## MCDRPathway

Type of marine Carbon Dioxide Removal (mCDR) pathways.

- `ocean_alkalinity_enhancement`: Ocean Alkalinity Enhancement (OAE) is a method to help mitigate climate change by increasing the alkalinity of seawater to enhance its capacity to absorb and store atmospheric carbon dioxide (CO₂).
- `biomass_sinking`: Biomass Sinking is a method that involves taking terrestrial or ocean biomass and sinking it into the deep ocean surface, subsurface, or anoxic basins, where it is sequestered. This can be accomplished by large-scale seaweed farming or macroalgae cultivation, which incorporates atmospheric CO2 as it grows, and then is sunk to the ocean floor. Alternatively, terrestrial plant biomass can be sunk to the ocean floor.
- `direct_ocean_capture`: Direct Ocean Capture (DOC) is a method that uses electrochemical processes to remove dissolved carbon dioxide (CO₂) directly from seawater for carbon storage or reuse.
- `ocean_nutrient_fertilization`: Ocean Fertilization is a method that involves adding nutrients, such as iron, nitrogen, or phosphorus, to the ocean to stimulate the growth of phytoplankton or other microscopic plants that absorb carbon dioxide (CO₂) through photosynthesis.
- `artificial_upwelling_downwelling`: Artificial Upwelling and Downwelling are mCDR methods that involve manipulating ocean water movement to enhance natural carbon sequestration processes.
- `marine_ecosystem_recovery`: Marine Ecosystem Recovery refers to the restoration and protection of marine ecosystems to enhance their natural ability to capture and store carbon dioxide (CO₂). This method leverages the natural carbon-sequestering processes of marine habitats such as salt marshes, mangrove forests, coral reefs, kelp forests, seagrass meadows, oyster beds, and deep-sea ecosystems, aiming to rebuild biodiversity, ecosystem functions, and carbon storage capacity.

## ModelComponentType

Type of model component

- `physics`: Physical model component (e.g., ocean circulation)
- `bgc_ecosystem`: Biogeochemical or ecosystem model component
- `sea_ice`: Sea Ice model component
- `atmosphere`: Atmosphere model component
- `other`: Other model component (e.g., sea ice, sediment, atmosphere)

## ModelVariableType

Classification of a variable output by a model simulation. Used in place of VariableType on ModelOutputVariable. Model output covers a different set of quantities than field measurement (velocities and fluxes rather than sampling-based observations), so this enum is different than VariableType.

- `air_sea_co2_flux`: Air-sea CO₂ flux
- `dissolved_inorganic_carbon`: Dissolved inorganic carbon (DIC)
- `total_alkalinity`: Total alkalinity (TA)
- `temperature`: Temperature
- `salinity`: Salinity
- `ph`: pH of seawater
- `biological_tracers`: Biological tracers (e.g., chlorophyll, phytoplankton, zooplankton) — biomass or concentration
- `nutrients`: Nutrients (e.g., dissolved oxygen, NO₃⁻, NH₄⁺)
- `zonal_velocity`: Zonal velocity (u)
- `meridional_velocity`: Meridional velocity (v)
- `vertical_velocity`: Vertical velocity (w)
- `co2`: CO₂ variables (xCO₂, pCO₂, fCO₂)
- `other`: Any model output variable that does not fall into a specific category above.

## PHCalibrationStandard

Standard used to calibrate a pH measurement.

- `dye`: Indicator dye, e.g., m-cresol purple.
- `tris`: TRIS buffer in synthetic seawater.
- `other`: A standard not listed here. Name it in the custom field.

## PlatformType

- `http://vocab.nerc.ac.uk/collection/L06/current/62/`: aeroplane
- `http://vocab.nerc.ac.uk/collection/L06/current/3B/`: autonomous surface water vehicle
- `http://vocab.nerc.ac.uk/collection/L06/current/25/`: autonomous underwater vehicle
- `http://vocab.nerc.ac.uk/collection/L06/current/13/`: beach/intertidal zone structure
- `http://vocab.nerc.ac.uk/collection/L06/current/17/`: coastal structure
- `http://vocab.nerc.ac.uk/collection/L06/current/72/`: diver
- `http://vocab.nerc.ac.uk/collection/L06/current/44/`: drifting subsurface float
- `http://vocab.nerc.ac.uk/collection/L06/current/46/`: drifting subsurface profiling float
- `http://vocab.nerc.ac.uk/collection/L06/current/42/`: drifting surface float
- `http://vocab.nerc.ac.uk/collection/L06/current/36/`: fishing vessel
- `http://vocab.nerc.ac.uk/collection/L06/current/11/`: fixed benthic node
- `http://vocab.nerc.ac.uk/collection/L06/current/45/`: fixed subsurface vertical profiler
- `http://vocab.nerc.ac.uk/collection/L06/current/47/`: float
- `http://vocab.nerc.ac.uk/collection/L06/current/6A/`: glider
- `http://vocab.nerc.ac.uk/collection/L06/current/67/`: helicopter
- `http://vocab.nerc.ac.uk/collection/L06/current/71/`: human
- `http://vocab.nerc.ac.uk/collection/L06/current/10/`: land or seafloor
- `http://vocab.nerc.ac.uk/collection/L06/current/14/`: land/onshore structure
- `http://vocab.nerc.ac.uk/collection/L06/current/15/`: land/onshore vehicle
- `http://vocab.nerc.ac.uk/collection/L06/current/26/`: lowered unmanned submersible
- `http://vocab.nerc.ac.uk/collection/L06/current/38/`: man-powered boat
- `http://vocab.nerc.ac.uk/collection/L06/current/3A/`: man-powered small boat
- `http://vocab.nerc.ac.uk/collection/L06/current/19/`: mesocosm bag
- `http://vocab.nerc.ac.uk/collection/L06/current/99/`: mesocosm tank
- `http://vocab.nerc.ac.uk/collection/L06/current/41/`: moored surface buoy
- `http://vocab.nerc.ac.uk/collection/L06/current/48/`: mooring
- `http://vocab.nerc.ac.uk/collection/L06/current/16/`: offshore structure
- `http://vocab.nerc.ac.uk/collection/L06/current/22/`: propelled unmanned submersible
- `http://vocab.nerc.ac.uk/collection/L06/current/61/`: research aeroplane
- `http://vocab.nerc.ac.uk/collection/L06/current/31/`: research vessel
- `http://vocab.nerc.ac.uk/collection/L06/current/18/`: river station
- `http://vocab.nerc.ac.uk/collection/L06/current/68/`: satellite
- `http://vocab.nerc.ac.uk/collection/L06/current/12/`: sea bed vehicle
- `http://vocab.nerc.ac.uk/collection/L06/current/37/`: self-propelled boat
- `http://vocab.nerc.ac.uk/collection/L06/current/33/`: self-propelled small boat
- `http://vocab.nerc.ac.uk/collection/L06/current/30/`: ship
- `http://vocab.nerc.ac.uk/collection/L06/current/27/`: sub-surface gliders
- `http://vocab.nerc.ac.uk/collection/L06/current/20/`: submersible
- `http://vocab.nerc.ac.uk/collection/L06/current/43/`: subsurface mooring
- `http://vocab.nerc.ac.uk/collection/L06/current/3C/`: surface gliders
- `http://vocab.nerc.ac.uk/collection/L06/current/3Z/`: surface vessel
- `http://vocab.nerc.ac.uk/collection/L06/current/23/`: towed unmanned submersible
- `http://vocab.nerc.ac.uk/collection/L06/current/6D/`: unmanned aerial vehicle
- `http://vocab.nerc.ac.uk/collection/L06/current/34/`: vessel at fixed position

## PublicCommentType

- `permitting`: Permitting
- `non_mandated_consultation`: Non-mandated consultation
- `informal_public_input`: Informal public input
- `other`: Other

## SamplingInstrumentType

- `ctd_rosette`: A CTD rosette consists of a metal frame that houses a collection of sensors and water sampling bottles (e.g., Niskin)
- `niskin_bottle`: A device that collects an in-situ discrete water sample from any depth and returns it to the surface without contamination by the waters through which it passes, such as a water bottle.
- `flow_through_system`: A device that continuously supplies a flow of water either to an analytical instrument, over a sensor or from which samples may be drawn.
- `flask_for_discrete_co2_measurement`: Such flasks are typically made of glass and have a capacity of around one liter. Seawater samples are collected from a specific depth using a Niskin bottle or other sampling device and transferred to the flask without exposing them to the air. The flask is then sealed with a stopper and transported to the laboratory for analysis.
- `biological_trawl`: A net towed through the water column designed to sample free-swimming nekton or fish
- `phytoplankton_net`: Phytoplankton net is used to collect and identify phytoplankton, which are microscopic plants that form the base of the marine food web.
- `zooplankton_net`: Zooplankton net is used to collect and identify zooplankton, which are microscopic animals that feed on phytoplankton and are important prey for many marine organisms.
- `edna_sampler`: Environmental DNA (eDNA) samplers: used to collect and analyze genetic material shed by marine organisms, which can provide information about their distribution, abundance, and diversity.
- `autonomous_sensor`: A device used in the measurement of a variety of oceanographic variables that functions autonomously
- `other`

## SeaNames

- `http://vocab.nerc.ac.uk/collection/C16/current/28Bg/`: Adriatic Sea (Mediterranean Sea)
- `http://vocab.nerc.ac.uk/collection/C16/current/28Bh/`: Aegean Sea (The Archipelago) (Mediterranean Sea)
- `http://vocab.nerc.ac.uk/collection/C16/current/28Ab/`: Alboran Sea (Mediterranean Sea)
- `http://vocab.nerc.ac.uk/collection/C16/current/44/`: Andaman or Burma Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/39/`: Arabian Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/48h/`: Arafura Sea (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/ARA/`: Aral Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/17/`: Arctic Ocean
- `http://vocab.nerc.ac.uk/collection/C16/current/17a/`: Arctic Ocean - Lincoln Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/200/`: Atlantic Ocean
- `http://vocab.nerc.ac.uk/collection/C16/current/28Ac/`: Balearic (Iberian) Sea (Mediterranean Sea)
- `http://vocab.nerc.ac.uk/collection/C16/current/48l/`: Bali Sea (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/01/`: Baltic Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/48g/`: Banda Sea (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/07/`: Barents Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/62a/`: Bass Strait (Great Australian Bight)
- `http://vocab.nerc.ac.uk/collection/C16/current/43/`: Bay of Bengal
- `http://vocab.nerc.ac.uk/collection/C16/current/22/`: Bay of Biscay
- `http://vocab.nerc.ac.uk/collection/C16/current/25/`: Bay of Fundy
- `http://vocab.nerc.ac.uk/collection/C16/current/13/`: Beaufort Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/55/`: Bering Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/66/`: Bismarck Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/30/`: Black Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/20/`: Bristol Channel
- `http://vocab.nerc.ac.uk/collection/C16/current/27/`: Caribbean Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/CAS/`: Caspian Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/48b/`: Celebes Sea (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/21a/`: Celtic Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/48f/`: Ceram Sea (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/12/`: Chukchi Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/59/`: Coastal Waters of SE Alaska and British Columbia
- `http://vocab.nerc.ac.uk/collection/C16/current/64/`: Coral Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/15/`: Davis Strait
- `http://vocab.nerc.ac.uk/collection/C16/current/48/`: East Indian Archipelago (Indonesia)
- `http://vocab.nerc.ac.uk/collection/C16/current/11/`: East Siberian Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/50/`: Eastern China Sea (Tung Hai)
- `http://vocab.nerc.ac.uk/collection/C16/current/ESC/`: Eastern Scheldt
- `http://vocab.nerc.ac.uk/collection/C16/current/21/`: English Channel
- `http://vocab.nerc.ac.uk/collection/C16/current/48j/`: Flores Sea (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/FRM/`: Fram Strait
- `http://vocab.nerc.ac.uk/collection/C16/current/62/`: Great Australian Bight
- `http://vocab.nerc.ac.uk/collection/C16/current/05/`: Greenland Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/38/`: Gulf of Aden
- `http://vocab.nerc.ac.uk/collection/C16/current/58/`: Gulf of Alaska
- `http://vocab.nerc.ac.uk/collection/C16/current/36/`: Gulf of Aqaba
- `http://vocab.nerc.ac.uk/collection/C16/current/48k/`: Gulf of Boni (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/01a/`: Gulf of Bothnia (Baltic Sea)
- `http://vocab.nerc.ac.uk/collection/C16/current/60/`: Gulf of California
- `http://vocab.nerc.ac.uk/collection/C16/current/01b/`: Gulf of Finland (Baltic Sea)
- `http://vocab.nerc.ac.uk/collection/C16/current/34/`: Gulf of Guinea
- `http://vocab.nerc.ac.uk/collection/C16/current/41/`: Gulf of Iran (Persian Gulf)
- `http://vocab.nerc.ac.uk/collection/C16/current/26/`: Gulf of Mexico
- `http://vocab.nerc.ac.uk/collection/C16/current/40/`: Gulf of Oman
- `http://vocab.nerc.ac.uk/collection/C16/current/01c/`: Gulf of Riga (Baltic Sea)
- `http://vocab.nerc.ac.uk/collection/C16/current/24/`: Gulf of St. Lawrence
- `http://vocab.nerc.ac.uk/collection/C16/current/35/`: Gulf of Suez
- `http://vocab.nerc.ac.uk/collection/C16/current/47/`: Gulf of Thailand (Siam)
- `http://vocab.nerc.ac.uk/collection/C16/current/48d/`: Gulf of Tomini (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/48e/`: Halmahera Sea (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/16/`: Hudson Bay
- `http://vocab.nerc.ac.uk/collection/C16/current/16a/`: Hudson Strait
- `http://vocab.nerc.ac.uk/collection/C16/current/IJM/`: IJsselmeer
- `http://vocab.nerc.ac.uk/collection/C16/current/ICS/`: Iceland Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/45/`: Indian Ocean
- `http://vocab.nerc.ac.uk/collection/C16/current/18/`: Inner Seas off the West Coast of Scotland
- `http://vocab.nerc.ac.uk/collection/C16/current/28Bf/`: Ionian Sea (Mediterranean Sea)
- `http://vocab.nerc.ac.uk/collection/C16/current/19/`: Irish Sea and St. George's Channel
- `http://vocab.nerc.ac.uk/collection/C16/current/IRM/`: Irminger Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/52/`: Japan Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/48n/`: Java Sea (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/09/`: Kara Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/02/`: Kattegat, Sound and Belts
- `http://vocab.nerc.ac.uk/collection/C16/current/15a/`: Labrador Sea (Davis Strait)
- `http://vocab.nerc.ac.uk/collection/C16/current/42/`: Laccadive Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/10/`: Laptev Sea (or Nordenskjold Sea)
- `http://vocab.nerc.ac.uk/collection/C16/current/28Ad/`: Ligurian Sea (Mediterranean Sea)
- `http://vocab.nerc.ac.uk/collection/C16/current/48m/`: Makassar Strait (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/46a/`: Malacca Strait
- `http://vocab.nerc.ac.uk/collection/C16/current/46/`: Malacca and Singapore Straits
- `http://vocab.nerc.ac.uk/collection/C16/current/MKM/`: Markermeer
- `http://vocab.nerc.ac.uk/collection/C16/current/28/`: Mediterranean Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/28B/`: Mediterranean Sea - Eastern basin
- `http://vocab.nerc.ac.uk/collection/C16/current/28A/`: Mediterranean Sea - Western basin
- `http://vocab.nerc.ac.uk/collection/C16/current/48c/`: Molukka Sea (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/45a/`: Mozambique Channel (Indian Ocean)
- `http://vocab.nerc.ac.uk/collection/C16/current/23/`: North Atlantic Ocean
- `http://vocab.nerc.ac.uk/collection/C16/current/23a/`: North East Atlantic Ocean (limit 40W)
- `http://vocab.nerc.ac.uk/collection/C16/current/57a/`: North East Pacific Ocean (limit 180W)
- `http://vocab.nerc.ac.uk/collection/C16/current/57/`: North Pacific Ocean
- `http://vocab.nerc.ac.uk/collection/C16/current/04/`: North Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/23b/`: North West Atlantic Ocean (limit 40W)
- `http://vocab.nerc.ac.uk/collection/C16/current/57b/`: North West Pacific Ocean (limit 180W)
- `http://vocab.nerc.ac.uk/collection/C16/current/06/`: Norwegian Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/500/`: Pacific Ocean
- `http://vocab.nerc.ac.uk/collection/C16/current/56/`: Philippine Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/37/`: Red Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/33/`: Rio de La Plata
- `http://vocab.nerc.ac.uk/collection/C16/current/48o/`: Savu Sea (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/31/`: Sea of Azov
- `http://vocab.nerc.ac.uk/collection/C16/current/29/`: Sea of Marmara
- `http://vocab.nerc.ac.uk/collection/C16/current/54/`: Sea of Okhotsk
- `http://vocab.nerc.ac.uk/collection/C16/current/53/`: Seto Naikai or Inland Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/46b/`: Singapore Strait
- `http://vocab.nerc.ac.uk/collection/C16/current/03/`: Skagerrak
- `http://vocab.nerc.ac.uk/collection/C16/current/65/`: Solomon Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/32/`: South Atlantic Ocean
- `http://vocab.nerc.ac.uk/collection/C16/current/49/`: South China Sea (Nan Hai)
- `http://vocab.nerc.ac.uk/collection/C16/current/32a/`: South East Atlantic Ocean (limit 20W)
- `http://vocab.nerc.ac.uk/collection/C16/current/61a/`: South East Pacific Ocean (limit 140W)
- `http://vocab.nerc.ac.uk/collection/C16/current/61/`: South Pacific Ocean
- `http://vocab.nerc.ac.uk/collection/C16/current/32b/`: South West Atlantic Ocean (limit 20W)
- `http://vocab.nerc.ac.uk/collection/C16/current/61b/`: South West Pacific Ocean (limit 140W)
- `http://vocab.nerc.ac.uk/collection/C16/current/SOC/`: Southern Ocean
- `http://vocab.nerc.ac.uk/collection/C16/current/28Aa/`: Strait of Gibraltar (Mediterranean Sea)
- `http://vocab.nerc.ac.uk/collection/C16/current/28C/`: Strait of Sicily
- `http://vocab.nerc.ac.uk/collection/C16/current/48a/`: Sulu Sea (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/63/`: Tasman Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/14/`: The Northwestern Passages
- `http://vocab.nerc.ac.uk/collection/C16/current/14a/`: The Northwestern Passages - Baffin Bay
- `http://vocab.nerc.ac.uk/collection/C16/current/48i/`: Timor Sea (East Indian Archipelago)
- `http://vocab.nerc.ac.uk/collection/C16/current/28Ae/`: Tyrrhenian Sea (Mediterranean Sea)
- `http://vocab.nerc.ac.uk/collection/C16/current/ZZ/`: Unknown
- `http://vocab.nerc.ac.uk/collection/C16/current/WAS/`: Wadden Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/WSC/`: Western Scheldt
- `http://vocab.nerc.ac.uk/collection/C16/current/08/`: White Sea
- `http://vocab.nerc.ac.uk/collection/C16/current/GLO/`: Worldwide
- `http://vocab.nerc.ac.uk/collection/C16/current/51/`: Yellow Sea (Hwang Hai)

## SimulationType

Type of model simulation dataset

- `counterfactual`: Control/baseline simulation without alkalinity perturbation
- `perturbation`: Simulation with alkalinity perturbation applied
- `other`: Other simulation type not listed above

## SocialStudyType

Type of social study conducted.

- `public_perception_survey`: Public perception survey
- `ecosystem_service_valuation_survey`: Ecosystem service valuation survey
- `text_analysis`: Text analysis
- `other`: Other study type

## TaxonomicCodeSystem

Taxonomic code system used for species identification.

- `itis`: Integrated Taxonomic Information System
- `worms`: World Register of Marine Species
- `col`: Catalogue of Life
- `pbdb`: Paleobiology Database

## TracerForm

Forms of tracer used in tracer studies

- `gas`: Gas tracer
- `dye`: Dye tracer (eg- rhodamine)
- `other`: Other tracer form not covered by standard categories

## VariableType

High-level classification of the variable. Determines which schema class to use in combination with genesis (measured/calculated) and sampling (discrete/continuous).

- `pH`: pH measurement — use with Discrete/ContinuousPHVariable or CalculatedVariable
- `ta`: Total alkalinity — use with Discrete/ContinuousTAVariable or CalculatedVariable
- `dic`: Dissolved inorganic carbon — use with Discrete/ContinuousDICVariable or CalculatedVariable
- `co2`: CO₂ variables (xCO₂, pCO₂, fCO₂) — use with DiscreteCO2Variable or CalculatedVariable
- `sediment`: Sediment variable — use with Discrete/ContinuousSedimentVariable or CalculatedVariable
- `hplc`: HPLC pigment analysis — use with HPLCVariable (always discrete, always measured)
- `physiological`: Physiological response variable — organism response data from field experiments. Use with Discrete/ContinuousPhysiologicalVariable or CalculatedVariable.
- `socioeconomic`: Socioeconomic variable — social and economic data. Use only with SocioeconomicVariable. Does not include QC fields.
- `other`: Any directly measured or calculated variable that does not fall into a specific category above (e.g., temperature, salinity, conductivity, pressure, fluorescence). Use with DiscreteMeasuredVariable, ContinuousMeasuredVariable, or CalculatedVariable.
- `non_measured`: Contextual or ancillary columns that are not directly measured or calculated by the project — identifiers, timestamps, coordinates and external source data. QC flag columns should NOT be listed as separate variables; instead set dataset_variable_name_qc_flag on the parent variable. Use only with NonMeasuredVariable.
