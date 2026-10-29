/**
* Type of dataset being submitted. This usually 
*/
export enum DatasetType {
    
    /** Variables such as dosing_onoff, dosing_rate, and flow_rate should be included here. */
    dosing = "dosing",
    /** Vertical profiles (e.g., optical packages, CTD) */
    cast = "cast",
    /** Any other types of measurements from water samples collected at discrete depths (e.g., nutrients) */
    bottle = "bottle",
    /** Continuous data (e.g., shipboard, underway flow through system) */
    flow_thru = "flow_thru",
    /** For laboratory measured pigment data (e.g. fluorometry, spectrophotometry, HPLC) */
    pigment = "pigment",
    /** For various types of marine snow catcher data */
    marine_snow_catcher = "marine_snow_catcher",
    /** Moored and buoy data */
    mooring = "mooring",
    /** Drifter and drogue data */
    drifter = "drifter",
    /** Measurements made via an aircraft */
    airborne = "airborne",
    /** For measurements made by a diver */
    diver = "diver",
    /** Measurements made by an autonomous underwater vehicle */
    auv = "auv",
    /** Measurements made by an autonomous surface vehicle */
    asv = "asv",
    /** Measurements that have a non-geospatial aspect (e.g., incubations or other laboratory measurements, etc.) */
    experimental = "experimental",
    /** Measurements from a sediment trap platform */
    sediment_trap = "sediment_trap",
    /** Data whose purpose is the classification or annotation of phytoplankton, zooplankton, or other marine groups. */
    taxonomy = "taxonomy",
    /** Measurements from sediment samples (e.g., core samples, grab samples) */
    sediment = "sediment",
    /** Data output from model experiments */
    model_output = "model_output",
    /** Information (quantitative or qualitative) from socioeconomic studies */
    socioeconomic = "socioeconomic",
    /** For measurements captured via net (e.g., zooplankton via MOCNESS) */
    net_tow = "net_tow",
    /** Data collected continuously from a moving platform (e.g., ship underway system sampling surface seawater during transit). */
    underway = "underway",
    /** For data types not included in the controlled vocabulary. Please fill in a the `dataset_type_custom` field with a more specific name for the custom mCDR data type. */
    other = "other",
};
/**
* Type of marine Carbon Dioxide Removal (mCDR) pathways.
*/
export enum MCDRPathway {
    
    /** Ocean Alkalinity Enhancement (OAE) is a method to help mitigate climate change by increasing the alkalinity of seawater to enhance its capacity to absorb and store atmospheric carbon dioxide (CO₂). */
    Ocean_Alkalinity_Enhancement = "ocean_alkalinity_enhancement",
    /** Biomass Sinking is a method that involves taking terrestrial or ocean biomass and sinking it into the deep ocean surface, subsurface, or anoxic basins, where it is sequestered. This can be accomplished by large-scale seaweed farming or macroalgae cultivation, which incorporates atmospheric CO2 as it grows, and then is sunk to the ocean floor. Alternatively, terrestrial plant biomass can be sunk to the ocean floor. */
    Biomass_Sinking = "biomass_sinking",
    /** Direct Ocean Capture (DOC) is a method that uses electrochemical processes to remove dissolved carbon dioxide (CO₂) directly from seawater for carbon storage or reuse. */
    Direct_Ocean_Capture = "direct_ocean_capture",
    /** Ocean Fertilization is a method that involves adding nutrients, such as iron, nitrogen, or phosphorus, to the ocean to stimulate the growth of phytoplankton or other microscopic plants that absorb carbon dioxide (CO₂) through photosynthesis. */
    Ocean_Nutrient_Fertilization = "ocean_nutrient_fertilization",
    /** Artificial Upwelling and Downwelling are mCDR methods that involve manipulating ocean water movement to enhance natural carbon sequestration processes. */
    Artificial_Upwelling_and_Downwelling = "artificial_upwelling_downwelling",
    /** Marine Ecosystem Recovery refers to the restoration and protection of marine ecosystems to enhance their natural ability to capture and store carbon dioxide (CO₂). This method leverages the natural carbon-sequestering processes of marine habitats such as salt marshes, mangrove forests, coral reefs, kelp forests, seagrass meadows, oyster beds, and deep-sea ecosystems, aiming to rebuild biodiversity, ecosystem functions, and carbon storage capacity. */
    Marine_Ecosystem_Recovery = "marine_ecosystem_recovery",
};
/**
* Types of mCDR experiments
*/
export enum ExperimentType {
    
    /** Baseline measurements taken before any intervention */
    baseline = "baseline",
    /** Control experiment without intervention for comparison */
    control = "control",
    /** Experiment with active OAE intervention */
    intervention = "intervention",
    /** Tracer study experiment (eg- dye or gas tracer study) */
    tracer_study = "tracer_study",
    /** Model-based experiment or simulation */
    model = "model",
    /** Other experiment type not covered by standard categories */
    other = "other",
};
/**
* Methods used to process alkalinity feedstock
*/
export enum AlkalinityFeedstockProcessing {
    
    /** Alkalinity generated via electrochemical processes (e.g., seawater electrolysis). */
    electrochemistry = "electrochemistry",
    /** Intentionally industrially manufactured chemical compounds (e.g., Ca(OH)2 via lime kilns). */
    synthetically_derived = "synthetically_derived",
    /** Mined geological material, including purified mineral or natural rock. */
    mineral_mining = "mineral_mining",
    /** A mix of multiple sources. */
    blended = "blended",
    /** Unclassified or novel; include a description in Experiment Description. */
    other = "other",
};
/**
* Physical form of the alkalinity feedstock upon ocean delivery
*/
export enum AlkalinityFeedstockForm {
    
    /** Involves adding alkaline minerals or particulate slurry (such as MgOH2, MgO, or CaO) to seawater or river systems either directly, through coastal outfalls (such as wastewater), or at breaking shorelines to increase its alkalinity. */
    solid = "solid",
    /** Aqueous alkalinity addition may use electrochemistry or fully dissolved mineral feedstock to increase seawater alkalinity. */
    aqueous = "aqueous",
    /** Slurry alkalinity additions include a mix of solid and aqueous alkalinity forms, where the solid alkaline particulates are suspended in a solution. */
    slurry = "slurry",
};
/**
* Equilibration status of the alkalinity feedstock
*/
export enum EquilibrationStatus {
    
    /** Pre-equilibrated with atmosphere before dosing */
    Pre_equilibrated = "pre_equilibrated",
    /** Not pre-equilibrated before dosing */
    unequilibrated = "unequilibrated",
};
/**
* Hydrologic location types for dosing
*/
export enum HydrologicLocation {
    
    /** Surface waters in coastal areas */
    Coastal_Surface = "coastal_surface",
    /** Surface waters in offshore areas */
    Offshore_Surface = "offshore_surface",
    /** River systems */
    river = "river",
    /** Wetland areas */
    wetland = "wetland",
    /** Seafloor or benthic zone */
    seafloor = "seafloor",
};
/**
* Types of dosing delivery methods
*/
export enum DosingDeliveryType {
    
    /** A single dosing location such as an outflow from a static platform with a pipe */
    Static_Point_Source = "static_point_source",
    /** A mobile dosing regimen described by a single location at each time step, such as an outflow from a mobile platform such as a ship or surface vessel. */
    Variable_Point_Source = "variable_point_source",
    /** A set location or locations of dosing that is not a point source, such as a distributed area over the seafloor or a diffusor. */
    Static_Distributed = "static_distributed",
    /** A distributed dosing area that varies in time, such as manually placed alkaline material over different areas at different times. */
    Variable_Distributed = "variable_distributed",
};
/**
* Forms of tracer used in tracer studies
*/
export enum TracerForm {
    
    /** Gas tracer */
    gas = "gas",
    /** Dye tracer (eg- rhodamine) */
    dye = "dye",
    /** Other tracer form not covered by standard categories */
    other = "other",
};
/**
* Types of materials used for alkalinity addition, as sourced from NCEI's OCADS controlled vocabulary: https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/vocabularies/alkalinization-types.html
*/
export enum FeedstockType {
    
    /** Lime (CaO) used as an alkalinity source. */
    lime = "lime",
    /** Portlandite (Ca(OH)₂) used as an alkalinity source. */
    portlandite = "portlandite",
    /** Calcium carbonate (CaCO₃) used as an alkalinity source. */
    calcium_carbonate = "calcium_carbonate",
    /** Anorthite (CaAl₂Si₂O₈) used as an alkalinity source. */
    anorthite = "anorthite",
    /** Dolomite (CaMg(CO₃)₂) used as an alkalinity source. */
    dolomite = "dolomite",
    /** Periclase (MgO) used as an alkalinity source. */
    periclase = "periclase",
    /** Brucite (Mg(OH)₂) used as an alkalinity source. */
    brucite = "brucite",
    /** Magnesite (MgCO₃) used as an alkalinity source. */
    magnesite = "magnesite",
    /** Forsterite (Mg₂SiO₄) used as an alkalinity source. */
    forsterite = "forsterite",
    /** Magnesium-rich olivine used as an alkalinity source. */
    mg_rich_olivine = "mg_rich_olivine",
    /** NaOH used as an alkalinity source. */
    sodium_hydroxide = "sodium_hydroxide",
    /** Natrite (Na₂CO₃) used as an alkalinity source. */
    natrite = "natrite",
    /** Nahcolite (NaHCO₃) used as an alkalinity source. */
    nahcolite = "nahcolite",
    /** Enter a custom value in the field provided */
    other = "other",
};
/**
* Type of grid in a multi-grid or nested model configuration
*/
export enum GridType {
    
    /** Inner (nested, higher-resolution) grid */
    inner_grid = "inner_grid",
    /** Outer (coarser-resolution) grid */
    outer_grid = "outer_grid",
    /** Single grid (no nesting) */
    single_grid = "single_grid",
};
/**
* Type of model component
*/
export enum ModelComponentType {
    
    /** Physical model component (e.g., ocean circulation) */
    Physics = "physics",
    /** Biogeochemical or ecosystem model component */
    BGC_SOLIDUS_Ecosystem = "bgc_ecosystem",
    /** Sea Ice model component */
    Sea_Ice = "sea_ice",
    /** Atmosphere model component */
    Atmosphere = "atmosphere",
    /** Other model component (e.g., sea ice, sediment, atmosphere) */
    other = "other",
};

export enum DataProductType {
    
    /** A dataset collected from a research cruise or laboratory experiment */
    originally_collected_dataset = "originally_collected_dataset",
    /** (e.g., SOCAT, GLODAP) */
    data_compilation_product = "data_compilation_product",
    /** (e.g. gridded products, or model output). */
    derived_product = "derived_product",
};
/**
* Type of model simulation dataset
*/
export enum SimulationType {
    
    /** Control/baseline simulation without alkalinity perturbation */
    counterfactual = "counterfactual",
    /** Simulation with alkalinity perturbation applied */
    perturbation = "perturbation",
    /** Other simulation type not listed above */
    other = "other",
};
/**
* Level of access to a dataset.
*/
export enum DataAccessibility {
    
    /** Data are freely available now, without restriction. */
    Open_Access = "open_access",
    /** Data are available upon request, subject to review. */
    Conditional_Access = "conditional_access",
    /** Data will become openly available after a specified date. */
    Scheduled_Access = "scheduled_access",
};

export enum MassConcentrationUnit {
    
    unitCOLONKiloGM_PER_M3 = "unit:KiloGM-PER-M3",
    unitCOLONMicroGM_PER_L = "unit:MicroGM-PER-L",
    unitCOLONMicroGM_PER_MilliL = "unit:MicroGM-PER-MilliL",
    unitCOLONMilliGM_PER_L = "unit:MilliGM-PER-L",
    unitCOLONMilliGM_PER_M3 = "unit:MilliGM-PER-M3",
    unitCOLONMilliGM_PER_MilliL = "unit:MilliGM-PER-MilliL",
    unitCOLONNanoGM_PER_L = "unit:NanoGM-PER-L",
    unitCOLONNanoGM_PER_MilliL = "unit:NanoGM-PER-MilliL",
    unitCOLONPicoGM_PER_MilliL = "unit:PicoGM-PER-MilliL",
};
/**
* Sea areas from the SeaDataNet C16 vocabulary.
*/
export enum SeaNames {
    
    Adriatic_Sea_LEFT_PARENTHESISMediterranean_SeaRIGHT_PARENTHESIS = "adriatic_sea_mediterranean_sea",
    Aegean_Sea_LEFT_PARENTHESISThe_ArchipelagoRIGHT_PARENTHESIS_LEFT_PARENTHESISMediterranean_SeaRIGHT_PARENTHESIS = "aegean_sea_the_archipelago_mediterranean_sea",
    Alboran_Sea_LEFT_PARENTHESISMediterranean_SeaRIGHT_PARENTHESIS = "alboran_sea_mediterranean_sea",
    Andaman_or_Burma_Sea = "andaman_or_burma_sea",
    Arabian_Sea = "arabian_sea",
    Arafura_Sea_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "arafura_sea_east_indian_archipelago",
    /** Large inland water body comprising three lakes (North Aral Sea, eastern and western basins of the South Aral Sea) having coastlines in Kazakhstan and Uzbekistan. */
    Aral_Sea = "aral_sea",
    Arctic_Ocean = "arctic_ocean",
    Arctic_Ocean___Lincoln_Sea = "arctic_ocean_lincoln_sea",
    /** Aggregation of North and South Atlantic Ocean areas */
    Atlantic_Ocean = "atlantic_ocean",
    Balearic_LEFT_PARENTHESISIberianRIGHT_PARENTHESIS_Sea_LEFT_PARENTHESISMediterranean_SeaRIGHT_PARENTHESIS = "balearic_iberian_sea_mediterranean_sea",
    Bali_Sea_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "bali_sea_east_indian_archipelago",
    Baltic_Sea = "baltic_sea",
    Banda_Sea_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "banda_sea_east_indian_archipelago",
    Barents_Sea = "barents_sea",
    Bass_Strait_LEFT_PARENTHESISGreat_Australian_BightRIGHT_PARENTHESIS = "bass_strait_great_australian_bight",
    Bay_of_Bengal = "bay_of_bengal",
    Bay_of_Biscay = "bay_of_biscay",
    Bay_of_Fundy = "bay_of_fundy",
    Beaufort_Sea = "beaufort_sea",
    Bering_Sea = "bering_sea",
    Bismarck_Sea = "bismarck_sea",
    Black_Sea = "black_sea",
    Bristol_Channel = "bristol_channel",
    Caribbean_Sea = "caribbean_sea",
    /** Large brackish inland water body having coastlines in Azerbaijan, Iran, Kazakhstan, Russia, and Turkmenistan. */
    Caspian_Sea = "caspian_sea",
    Celebes_Sea_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "celebes_sea_east_indian_archipelago",
    /** Formally accepted and defined by IHO as an S23(1953) extension. */
    Celtic_Sea = "celtic_sea",
    Ceram_Sea_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "ceram_sea_east_indian_archipelago",
    Chukchi_Sea = "chukchi_sea",
    Coastal_Waters_of_SE_Alaska_and_British_Columbia = "coastal_waters_of_se_alaska_and_british_columbia",
    Coral_Sea = "coral_sea",
    Davis_Strait = "davis_strait",
    East_Indian_Archipelago_LEFT_PARENTHESISIndonesiaRIGHT_PARENTHESIS = "east_indian_archipelago_indonesia",
    East_Siberian_Sea = "east_siberian_sea",
    Eastern_China_Sea_LEFT_PARENTHESISTung_HaiRIGHT_PARENTHESIS = "eastern_china_sea_tung_hai",
    /** The more northerly branch of the Scheldt Estuary.  Northern boundary is a man-made dam */
    Eastern_Scheldt = "eastern_scheldt",
    English_Channel = "english_channel",
    Flores_Sea_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "flores_sea_east_indian_archipelago",
    /** Body of water between Greenland and Svalbard */
    Fram_Strait = "fram_strait",
    Great_Australian_Bight = "great_australian_bight",
    Greenland_Sea = "greenland_sea",
    Gulf_of_Aden = "gulf_of_aden",
    Gulf_of_Alaska = "gulf_of_alaska",
    Gulf_of_Aqaba = "gulf_of_aqaba",
    Gulf_of_Boni_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "gulf_of_boni_east_indian_archipelago",
    Gulf_of_Bothnia_LEFT_PARENTHESISBaltic_SeaRIGHT_PARENTHESIS = "gulf_of_bothnia_baltic_sea",
    Gulf_of_California = "gulf_of_california",
    Gulf_of_Finland_LEFT_PARENTHESISBaltic_SeaRIGHT_PARENTHESIS = "gulf_of_finland_baltic_sea",
    Gulf_of_Guinea = "gulf_of_guinea",
    Gulf_of_Iran_LEFT_PARENTHESISPersian_GulfRIGHT_PARENTHESIS = "gulf_of_iran_persian_gulf",
    Gulf_of_Mexico = "gulf_of_mexico",
    Gulf_of_Oman = "gulf_of_oman",
    Gulf_of_Riga_LEFT_PARENTHESISBaltic_SeaRIGHT_PARENTHESIS = "gulf_of_riga_baltic_sea",
    Gulf_of_StFULL_STOP_Lawrence = "gulf_of_st_lawrence",
    Gulf_of_Suez = "gulf_of_suez",
    Gulf_of_Thailand_LEFT_PARENTHESISSiamRIGHT_PARENTHESIS = "gulf_of_thailand_siam",
    Gulf_of_Tomini_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "gulf_of_tomini_east_indian_archipelago",
    Halmahera_Sea_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "halmahera_sea_east_indian_archipelago",
    Hudson_Bay = "hudson_bay",
    Hudson_Strait = "hudson_strait",
    /** Part of the Arctic Ocean to the North of Iceland between Greenland and the Norwegian Sea */
    Iceland_Sea = "iceland_sea",
    /** Dutch freshwater lake with artificial dam boundaries between it and the Wadden Sea to the North and Markermeer to the South. */
    IJsselmeer = "ijsselmeer",
    Indian_Ocean = "indian_ocean",
    Inner_Seas_off_the_West_Coast_of_Scotland = "inner_seas_off_the_west_coast_of_scotland",
    Ionian_Sea_LEFT_PARENTHESISMediterranean_SeaRIGHT_PARENTHESIS = "ionian_sea_mediterranean_sea",
    Irish_Sea_and_StFULL_STOP_GeorgeAPOSTROPHEs_Channel = "irish_sea_and_st_george_s_channel",
    /** The sea area confined between Greenland and Iceland south of the Denmark Strait (the ridge) and bounded to the south by a line from Cape Farewell to the southern tip of the 2000m isobath on the Reykjanes Ridge and a line following the top of the ridge to Iceland. */
    Irminger_Sea = "irminger_sea",
    Japan_Sea = "japan_sea",
    Java_Sea_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "java_sea_east_indian_archipelago",
    Kara_Sea = "kara_sea",
    Kattegat_Sound_and_Belts = "kattegat_sound_and_belts",
    Labrador_Sea_LEFT_PARENTHESISDavis_StraitRIGHT_PARENTHESIS = "labrador_sea_davis_strait",
    Laccadive_Sea = "laccadive_sea",
    Laptev_Sea_LEFT_PARENTHESISor_Nordenskjold_SeaRIGHT_PARENTHESIS = "laptev_sea_or_nordenskjold_sea",
    Ligurian_Sea_LEFT_PARENTHESISMediterranean_SeaRIGHT_PARENTHESIS = "ligurian_sea_mediterranean_sea",
    Makassar_Strait_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "makassar_strait_east_indian_archipelago",
    Malacca_and_Singapore_Straits = "malacca_and_singapore_straits",
    Malacca_Strait = "malacca_strait",
    /** Dutch freshwater lake with an artificial dam boundaries between it and IJsselmeer. */
    Markermeer = "markermeer",
    Mediterranean_Sea = "mediterranean_sea",
    Mediterranean_Sea___Eastern_basin = "mediterranean_sea_eastern_basin",
    Mediterranean_Sea___Western_basin = "mediterranean_sea_western_basin",
    Molukka_Sea_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "molukka_sea_east_indian_archipelago",
    Mozambique_Channel_LEFT_PARENTHESISIndian_OceanRIGHT_PARENTHESIS = "mozambique_channel_indian_ocean",
    North_Atlantic_Ocean = "north_atlantic_ocean",
    /** Not a valid IHB Code - created for ROSCOP compatibility */
    North_East_Atlantic_Ocean_LEFT_PARENTHESISlimit_40WRIGHT_PARENTHESIS = "north_east_atlantic_ocean_limit_40w",
    /** Not a valid IHB Code - created for ROSCOP compatibility */
    North_East_Pacific_Ocean_LEFT_PARENTHESISlimit_180WRIGHT_PARENTHESIS = "north_east_pacific_ocean_limit_180w",
    North_Pacific_Ocean = "north_pacific_ocean",
    North_Sea = "north_sea",
    /** Not a valid IHB Code - created for ROSCOP compatibility */
    North_West_Atlantic_Ocean_LEFT_PARENTHESISlimit_40WRIGHT_PARENTHESIS = "north_west_atlantic_ocean_limit_40w",
    /** Not a valid IHB Code - created for ROSCOP compatibility */
    North_West_Pacific_Ocean_LEFT_PARENTHESISlimit_180WRIGHT_PARENTHESIS = "north_west_pacific_ocean_limit_180w",
    Norwegian_Sea = "norwegian_sea",
    /** Aggregation of North and South Pacific Ocean areas */
    Pacific_Ocean = "pacific_ocean",
    Philippine_Sea = "philippine_sea",
    Red_Sea = "red_sea",
    Rio_de_La_Plata = "rio_de_la_plata",
    Savu_Sea_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "savu_sea_east_indian_archipelago",
    Sea_of_Azov = "sea_of_azov",
    Sea_of_Marmara = "sea_of_marmara",
    Sea_of_Okhotsk = "sea_of_okhotsk",
    Seto_Naikai_or_Inland_Sea = "seto_naikai_or_inland_sea",
    Singapore_Strait = "singapore_strait",
    Skagerrak = "skagerrak",
    Solomon_Sea = "solomon_sea",
    South_Atlantic_Ocean = "south_atlantic_ocean",
    South_China_Sea_LEFT_PARENTHESISNan_HaiRIGHT_PARENTHESIS = "south_china_sea_nan_hai",
    /** Not a valid IHB Code - created for ROSCOP compatibility */
    South_East_Atlantic_Ocean_LEFT_PARENTHESISlimit_20WRIGHT_PARENTHESIS = "south_east_atlantic_ocean_limit_20w",
    /** Not a valid IHB Code - created for ROSCOP compatibility */
    South_East_Pacific_Ocean_LEFT_PARENTHESISlimit_140WRIGHT_PARENTHESIS = "south_east_pacific_ocean_limit_140w",
    South_Pacific_Ocean = "south_pacific_ocean",
    /** Not a valid IHB Code - created for ROSCOP compatibility */
    South_West_Atlantic_Ocean_LEFT_PARENTHESISlimit_20WRIGHT_PARENTHESIS = "south_west_atlantic_ocean_limit_20w",
    /** Not a valid IHB Code - created for ROSCOP compatibility */
    South_West_Pacific_Ocean_LEFT_PARENTHESISlimit_140WRIGHT_PARENTHESIS = "south_west_pacific_ocean_limit_140w",
    /** Waters south of 60S */
    Southern_Ocean = "southern_ocean",
    Strait_of_Gibraltar_LEFT_PARENTHESISMediterranean_SeaRIGHT_PARENTHESIS = "strait_of_gibraltar_mediterranean_sea",
    /** The region of the Mediterranean Sea between Sicily and Tunisia */
    Strait_of_Sicily = "strait_of_sicily",
    Sulu_Sea_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "sulu_sea_east_indian_archipelago",
    Tasman_Sea = "tasman_sea",
    The_Northwestern_Passages = "the_northwestern_passages",
    The_Northwestern_Passages___Baffin_Bay = "the_northwestern_passages_baffin_bay",
    Timor_Sea_LEFT_PARENTHESISEast_Indian_ArchipelagoRIGHT_PARENTHESIS = "timor_sea_east_indian_archipelago",
    Tyrrhenian_Sea_LEFT_PARENTHESISMediterranean_SeaRIGHT_PARENTHESIS = "tyrrhenian_sea_mediterranean_sea",
    /** The correct value is not known to and not computable by the creator of this information. However a correct value probably exists. */
    Unknown = "unknown",
    /** Part of the North Sea between the Dutch, German and Danish coasts and the Frisian islands. */
    Wadden_Sea = "wadden_sea",
    /** The more southerly branch of the Scheldt Estuary. */
    Western_Scheldt = "western_scheldt",
    White_Sea = "white_sea",
    /** Global coverage from 90S to 90N and 180E to 180W */
    Worldwide = "worldwide",
    Yellow_Sea_LEFT_PARENTHESISHwang_HaiRIGHT_PARENTHESIS = "yellow_sea_hwang_hai",
};
/**
* Platform categories from the SeaVoX L06 vocabulary.
*/
export enum PlatformType {
    
    /** A fixed-wing self-propelled aircraft. */
    aeroplane = "aeroplane",
    /** A programmed or remotely controlled self-propelled vessel operating on the surface of water bodies with no human occupants; includes saildrones. */
    autonomous_surface_water_vehicle = "autonomous_surface_water_vehicle",
    /** A free-roving platform operating in the water column with propulsion but no human operator on board (e.g. Autosub, Gavia). */
    autonomous_underwater_vehicle = "autonomous_underwater_vehicle",
    /** A structure to which instrumentation may be attached that is either in air or under water depending on the state of the tide and weather conditions. */
    beachSOLIDUSintertidal_zone_structure = "beach_intertidal_zone_structure",
    /** A fixed man-made structure permanently linked to land with access to water at all states of the tide to which instrumentation may be attached (e.g. pier). */
    coastal_structure = "coastal_structure",
    /** A human being with self-contained equipment or surface-connected suit enabling operation within the water column. */
    diver = "diver",
    /** An unmanned instrumented platform drifting freely in the water column at a depth governed by its density (e.g. Swallow float). */
    drifting_subsurface_float = "drifting_subsurface_float",
    /** An unmanned instrumented platform drifting freely in the water column that periodically makes vertical traverses through the water column (e.g. Argo float). */
    drifting_subsurface_profiling_float = "drifting_subsurface_profiling_float",
    /** An unmanned instrumented platform operating on the surface of the water column often attached to a drogue to track currents rather than winds (e.g. Argos buoy). */
    drifting_surface_float = "drifting_surface_float",
    /** A platform operating on the surface of the water column whose primary purpose is the commercial harvesting of fish or shellfish but may be engaged in scientific activities such as fish stock surveys or mooring deployments and recoveries. */
    fishing_vessel = "fishing_vessel",
    /** A collection of oceanographic instruments mounted at a fixed position on the seabed (e.g. POL Monitoring Platform, seabed ADCP). */
    fixed_benthic_node = "fixed_benthic_node",
    /** A platform that periodically makes an automated vertical traverse of the water column at a predetermined fixed location. (e.g. YSI vertical profiler, HOMER CTD). */
    fixed_subsurface_vertical_profiler = "fixed_subsurface_vertical_profiler",
    /** A free-floating platform either on the surface of the water column or at a predetermined depth within the water column. */
    float = "float",
    /** A fixed-wing aircraft with no propulsion. */
    glider = "glider",
    /** An aircraft without wings that obtains its lift from the rotation of overhead blades. */
    helicopter = "helicopter",
    /** A human being without specialised equipment operating on land or the surface of the water column. */
    human = "human",
    /** A platform located on the solid surface of the Earth either above or below sea level. */
    land_or_seafloor = "land_or_seafloor",
    /** A fixed man-made structure on land to which instrumentation may be attached (e.g. meteorological tower). */
    landSOLIDUSonshore_structure = "land_onshore_structure",
    /** An instrumented vehicle or sample collector that operates on the solid surface of the Earth (e.g. mobile meteorological station, land crawler, snowmobile). */
    landSOLIDUSonshore_vehicle = "land_onshore_vehicle",
    /** An unmanned platform lowered and raised vertically by a cable from the mothership.  Includes any type of profiling sensor mounting such as CTD frames, profiling radiometers and instrumented nets. */
    lowered_unmanned_submersible = "lowered_unmanned_submersible",
    /** A platform operating on the surface of the water column that is manually propelled and may not be easily removed from the water (e.g. trireme). */
    man_powered_boat = "man_powered_boat",
    /** A platform operating on the surface of the water column that is manually propelled and may be easily removed from the water (e.g. rowing boat, canoe). */
    man_powered_small_boat = "man_powered_small_boat",
    /** A large polythene bag containing a water sample suspended in the natural environment so that it shares ambient physical conditions such as temperature and light levels, but is chemically isolated to allow experiments such as fertilisation. */
    mesocosm_bag = "mesocosm_bag",
    /** An indoor or outdoor tank containing water, used to house an experimental system. Instruments attached to the tank are used to measure and control conditions to help evaluate how organisms or communities react to controlled environmental changes. */
    mesocosm_tank = "mesocosm_tank",
    /** An unmanned instrumented platform operating on the surface of the water column loosely tethered to the seafloor to maintain a fixed position (e.g. ODAS buoy). */
    moored_surface_buoy = "moored_surface_buoy",
    /** A tethered collection of oceanographic instruments at a fixed location that may include seafloor, mid-water and surface components. */
    mooring = "mooring",
    /** A fixed (for the duration of the measurements) man-made structure away from the coast to which instrumentation may be attached (e.g. oil rig, gas rig or jack-up barge). */
    offshore_structure = "offshore_structure",
    /** A platform operating in the water column attached to a mothership by an umbilical with limited propulsion and no human operator on board (e.g. ROV). */
    propelled_unmanned_submersible = "propelled_unmanned_submersible",
    /** A fixed-wing self-propelled aircraft that is equipped, manned and operated for atmospheric, meteorological or oceanographic research, sometimes also called 'instrumented platform'. */
    research_aeroplane = "research_aeroplane",
    /** A platform of any size operating on the surface of the water column in unpredictable locations that is specifically equipped, manned and operated for scientific, usually oceanographic, research. */
    research_vessel = "research_vessel",
    /** An instrumented structure in a river upstream of its tidal limit. */
    river_station = "river_station",
    /** A vehicle operating beyond the Earth's atmosphere without human occupants that orbits the Earth. */
    satellite = "satellite",
    /** An instrumented platform that is propelled on wheels or tracks on the seabed (e.g benthic crawler). */
    sea_bed_vehicle = "sea_bed_vehicle",
    /** A small self-propelled platform operating on the surface of the water column in unpredictable locations that is smaller than a ship, but too large to easily remove from the water. */
    self_propelled_boat = "self_propelled_boat",
    /** A small self-propelled platform operating on the surface of the water column that may be easily removed from the water (e.g. shore-based RIBs, ships' boats). */
    self_propelled_small_boat = "self_propelled_small_boat",
    /** A large platform operating on the surface of the water column. Objective definitions for guidelines: >50m length (EU), >100 foot length (USA), >300 GRT weight (SOLAS). Subjective definition: a ship is a vessel big enough to carry a boat. */
    ship = "ship",
    /** Platforms with buoyancy-based propulsion that are capable of operations at variable depths which are not constrained to be near the sea surface. */
    sub_surface_gliders = "sub_surface_gliders",
    /** A platform operating within a water body. */
    submersible = "submersible",
    /** A collection of oceanographic instruments attached to wires suspended between anchors on the seabed and buoyant spheres in the water column. */
    subsurface_mooring = "subsurface_mooring",
    /** Platforms operating at a single depth near the sea surface, using a combination of solar energy and wave motion as means of propulsion. */
    surface_gliders = "surface_gliders",
    /** A mobile platform with propulsion operating on and restricted to the surface of a water body. */
    surface_vessel = "surface_vessel",
    /** A vehicle towed by rigid cable through the water column at fixed or varying depth with no propulsion and no human operator (e.g. Towfish, Scanfish, UOR, SeaSoar). */
    towed_unmanned_submersible = "towed_unmanned_submersible",
    /** Any untethered heavier-than-air aircraft that is not occupied by people: may be a remotely piloted aircraft or an autonomous aircraft. Also referred to as a drone. */
    unmanned_aerial_vehicle = "unmanned_aerial_vehicle",
    /** A platform of any size occupying a fixed location on the surface of the water column for prolonged periods collecting scientific (oceanographic and meteorological) data as a primary or secondary mission.  Includes light vessels and weather ships. */
    vessel_at_fixed_position = "vessel_at_fixed_position",
};

export enum PublicCommentType {
    
    Permitting = "permitting",
    Non_mandated_consultation = "non_mandated_consultation",
    Informal_public_input = "informal_public_input",
    Other = "other",
};

export enum ResearcherIDType {
    
    orcid = "orcid",
    researcher_id = "researcher_id",
    ocean_expert = "ocean_expert",
};
/**
* Where the calibration was performed.
*/
export enum CalibrationLocation {
    
    /** Factory calibration performed by manufacturer. */
    factory = "factory",
    /** Laboratory calibration. */
    lab = "lab",
    /** Field calibration performed during deployment. */
    field = "field",
};
/**
* Standard used to calibrate a pH measurement.
*/
export enum PHCalibrationStandard {
    
    /** Indicator dye, e.g., m-cresol purple. */
    Dye = "dye",
    /** TRIS buffer in synthetic seawater. */
    TRIS = "tris",
    /** A standard not listed here. Name it in the custom field. */
    Other = "other",
};

export enum SamplingInstrumentType {
    
    /** A CTD rosette consists of a metal frame that houses a collection of sensors and water sampling bottles (e.g., Niskin) */
    ctd_rosette = "ctd_rosette",
    /** A device that collects an in-situ discrete water sample from any depth and returns it to the surface without contamination by the waters through which it passes, such as a water bottle. */
    niskin_bottle = "niskin_bottle",
    /** A device that continuously supplies a flow of water either to an analytical instrument, over a sensor or from which samples may be drawn. */
    flow_through_system = "flow_through_system",
    /** Such flasks are typically made of glass and have a capacity of around one liter. Seawater samples are collected from a specific depth using a Niskin bottle or other sampling device and transferred to the flask without exposing them to the air. The flask is then sealed with a stopper and transported to the laboratory for analysis. */
    flask_for_discrete_co2_measurement = "flask_for_discrete_co2_measurement",
    /** A net towed through the water column designed to sample free-swimming nekton or fish */
    biological_trawl = "biological_trawl",
    /** Phytoplankton net is used to collect and identify phytoplankton, which are microscopic plants that form the base of the marine food web. */
    phytoplankton_net = "phytoplankton_net",
    /** Zooplankton net is used to collect and identify zooplankton, which are microscopic animals that feed on phytoplankton and are important prey for many marine organisms. */
    zooplankton_net = "zooplankton_net",
    /** Environmental DNA (eDNA) samplers: used to collect and analyze genetic material shed by marine organisms, which can provide information about their distribution, abundance, and diversity. */
    edna_sampler = "edna_sampler",
    /** A device used in the measurement of a variety of oceanographic variables that functions autonomously */
    autonomous_sensor = "autonomous_sensor",
    other = "other",
};

export enum AnalyzingInstrumentType {
    
    /** A reusable instrument that always simultaneously measures conductivity and temperature (for salinity) and pressure (for depth). */
    ctd_sensor = "ctd_sensor",
    /** A device that continuously supplies a flow of water either to an analytical instrument, over a sensor or from which samples may be drawn. */
    flow_through_system = "flow_through_system",
    /** Temperature and conductivity sensors mounted on a sea-surface platform continuously measuring a surface water supply. */
    thermosalinograph = "thermosalinograph",
    /** Instruments that measure the salinity of a collected water sample based on its electrical conductivity or optical properties. */
    salinometer_for_discrete_salinity_measurement = "salinometer_for_discrete_salinity_measurement",
    /** DIC coulometers are widely used in oceanographic research to measure the concentration of dissolved inorganic carbon in seawater samples. They are often coupled with computer-controlled automated dynamic headspace analyzers that extracts total carbon dioxide from seawater using Single-Operator Multiparameter Metabolic Analyzers (SOMMAs). */
    dic_analyzers_based_on_coulometers = "dic_analyzers_based_on_coulometers",
    /** DIC analyzers based on a CO2 gas detector including Non-dispersive infrared absorption (NDIR) (e.g., Licor LI-850), Cavity Enhanced Absorption Spectroscopy (e.g., Licor's LI-7815), and Cavity Ring-Down Spectroscopy (CRDS) (e.g., Picarro G2131i) detectors. */
    dic_analyzers_based_on_co2_gas_detectors = "dic_analyzers_based_on_co2_gas_detectors",
    /** Autonomous dissolved inorganic carbon (DIC) sensors are devices that can measure the concentration of DIC in seawater or other natural waters in situ, without the need for manual sampling and laboratory analysis. */
    autonomous_dic_sensor = "autonomous_dic_sensor",
    /** An alkalinity titrator is a device used to measure the total alkalinity of a seawater by titration. */
    alkalinity_titrator = "alkalinity_titrator",
    /** Autonomous total alkalinity (TA) sensors are devices that can measure the concentration of TA in seawater or other natural waters in situ, without the need for manual sampling and laboratory analysis. */
    autonomous_ta_sensor = "autonomous_ta_sensor",
    /** This type of equilibrator works by spraying seawater into a gas chamber, allowing the CO2 in the water to equilibrate with a gas mixture in the chamber. */
    showerhead_equilibrator = "showerhead_equilibrator",
    /** An "h"-shaped bubble equilibrator assembly commonly used in MAPCO2 systems on moorings. For more information, refer to Friederich et al. (1995). */
    floating_air_water_equilibrator = "floating_air_water_equilibrator",
    /** While seawater is passed through a membrane, CO2 in the water diffuses across the membrane and equilibrates with the gas mixture, which is then analyzed to determine the CO2 concentration. */
    membrane_equilibrator = "membrane_equilibrator",
    /** Instruments measuring the relative absorption of electromagnetic radiation of different wavelengths in the near infra-red, visible and ultraviolet wavebands by samples. */
    spectrophotometer = "spectrophotometer",
    /** One example of a handheld pH spectrophotometer is the "pHyter". Refer to Pardis et al. (2022) for more details. */
    handheld_ph_spectrophotometer = "handheld_ph_spectrophotometer",
    /** A pH electrode, sometimes referred to as a pH probe or pH sensor, is a glass device used to measure the pH of a solution. */
    ph_electrode = "ph_electrode",
    /** A pH sensor. The sensor can be used for ocean acidification, research coral reef sensitivity analysis and environmental monitoring. The sensor measures pH with a range of 6.5 to 9.0. The sensing element is an ion sensitive field effect transistor. The pH sensor has an initial accuracy of +/-0.05 pH, precision of 0.001 pH and stability of 0.005 pH/month. It can operate in temperatures ranging from 0 deg C to 50 deg C and up to depths of 50 m. */
    sea_bird_seafet_v1 = "sea_bird_seafet_v1",
    /** A pH sensor. The sensor can be used for ocean acidification, research coral reef sensitivity analysis and environmental monitoring. The sensor measures pH with a range of 6.5 to 9.0. The sensing element is an ion sensitive field effect transistor. V2 implements improvements to the original SeaFET's reliability, data quality, ease of operation, and deployment endurance, with significant changes to how users interface with the instrument. The pH sensor has an accuracy to +/-0.05 pH, precision of 0.004 pH and stability of 0.003 pH/month. It can operate in temperatures ranging from 0 deg C to 50 deg C and up to depths of 50 m. */
    sea_bird_seafet_v2 = "sea_bird_seafet_v2",
    /** An oxygen titrator is a device used to measure the concentration of dissolved oxygen in a water sample, as required for the Winkler method. */
    oxygen_titrator = "oxygen_titrator",
    /** An oxygen sensor or probe or sonde, is an electronic device that measures the concentration of dissolved oxygen in the ocean. */
    oxygen_sensor = "oxygen_sensor",
    /** Sea-Bird SeapHOx is a type of oceanographic instrument that measures both the pH and dissolved oxygen concentration of seawater in real-time. */
    sea_bird_seaphox = "sea_bird_seaphox",
    /** YSI (Yellow Springs Instruments) is a company that produces a variety of water quality monitoring instruments. The YSI sensors are designed to measure a wide range of parameters, including temperature, salinity, and dissolved oxygen. */
    ysi = "ysi",
    /** Instrument that makes in-situ measurements of one or more of nitrate, nitrite, ammonium, urea, phosphate or silicate dissolved in the water column. */
    nutrient_analyzer = "nutrient_analyzer",
    /** Instrument that measures the amount of stimulated electromagnetic radiation produced by pulses of electromagnetic radiation emitted into the water column. */
    fluorometers = "fluorometers",
    /** Instruments that separate and analyse mixtures of substances by high pressure pumping the sample through a column packed with microspheres coated with the stationary phase. */
    high_performance_liquid_chromatography = "high_performance_liquid_chromatography",
    /** Acoustic Doppler Current Profiler (ADCP), is a type of instrument used to measure water currents in oceans, rivers, and other bodies of water. */
    acoustic_doppler_current_profiler = "acoustic_doppler_current_profiler",
    /** Instruments used to measure the mass-to-charge ratio of ions most generally used to find the composition of a sample by generating a mass spectrum representing the masses of sample components. */
    mass_spectrometers = "mass_spectrometers",
    /** Instruments that measure isotopic ratios using an electron ionisation source. Atoms in purified samples are ionised using a beam of electrons under vacuum. Subsequently, ions are focused into a beam by an electromagnet and then separated into individual beams based on their mass/charge ratio */
    isotope_ratio_mass_spectrometers = "isotope_ratio_mass_spectrometers",
    /** Instrument that makes routine meteorological measurements on the atmosphere, typically air pressure, temperature and humidity */
    barometric_pressure_sensor = "barometric_pressure_sensor",
    /** Instruments that generate enlarged images of samples using the phenomena of reflection and absorption of visible light. Includes conventional and inverted instruments */
    microscopes = "microscopes",
    /** A scanning electron microscope (SEM) is a type of microscope that uses a focused beam of electrons to create high-resolution images of the surface of a specimen. */
    scanning_electron_microscopes = "scanning_electron_microscopes",
    /** Instruments that suspend cells in a stream of fluid past detection sensors whilst illuminating them with laser light. Used for cell counting, sorting, biomarker detection and protein engineering. */
    flow_cytometers = "flow_cytometers",
    /** Environmental DNA (eDNA) samplers: used to collect and analyze genetic material shed by marine organisms, which can provide information about their distribution, abundance, and diversity. */
    edna_sampler = "edna_sampler",
    /** TBD */
    gas_analyzer = "gas_analyzer",
    other = "other",
};

export enum SamplingType {
    
    discrete = "discrete",
    continuous = "continuous",
};
/**
* High-level classification of the variable. Determines which schema class to use in combination with genesis (measured/calculated) and sampling (discrete/continuous).
*/
export enum VariableType {
    
    /** pH measurement — use with Discrete/ContinuousPHVariable or CalculatedVariable */
    pH = "pH",
    /** Total alkalinity — use with Discrete/ContinuousTAVariable or CalculatedVariable */
    ta = "ta",
    /** Dissolved inorganic carbon — use with Discrete/ContinuousDICVariable or CalculatedVariable */
    dic = "dic",
    /** CO₂ variables (xCO₂, pCO₂, fCO₂) — use with DiscreteCO2Variable or CalculatedVariable */
    co2 = "co2",
    /** Sediment variable — use with Discrete/ContinuousSedimentVariable or CalculatedVariable */
    sediment = "sediment",
    /** HPLC pigment analysis — use with HPLCVariable (always discrete, always measured) */
    hplc = "hplc",
    /** Physiological response variable — organism response data from field experiments. Use with Discrete/ContinuousPhysiologicalVariable or CalculatedVariable. */
    physiological = "physiological",
    /** Socioeconomic variable — social and economic data. Use only with SocioeconomicVariable. Does not include QC fields. */
    socioeconomic = "socioeconomic",
    /** Any directly measured or calculated variable that does not fall into a specific category above (e.g., temperature, salinity, conductivity, pressure, fluorescence). Use with DiscreteMeasuredVariable, ContinuousMeasuredVariable, or CalculatedVariable. */
    other = "other",
    /** Contextual or ancillary columns that are not directly measured or calculated by the project — identifiers, timestamps, coordinates and external source data. QC flag columns should NOT be listed as separate variables; instead set dataset_variable_name_qc_flag on the parent variable. Use only with NonMeasuredVariable. */
    non_measured = "non_measured",
};
/**
* Classification of a variable output by a model simulation. Used in place of VariableType on ModelOutputVariable. Model output covers a different set of quantities than field measurement (velocities and fluxes rather than sampling-based observations), so this enum is different than VariableType.
*/
export enum ModelVariableType {
    
    /** Air-sea CO₂ flux */
    air_sea_co2_flux = "air_sea_co2_flux",
    /** Dissolved inorganic carbon (DIC) */
    dissolved_inorganic_carbon = "dissolved_inorganic_carbon",
    /** Total alkalinity (TA) */
    total_alkalinity = "total_alkalinity",
    /** Temperature */
    temperature = "temperature",
    /** Salinity */
    salinity = "salinity",
    /** pH of seawater */
    ph = "ph",
    /** Biological tracers (e.g., chlorophyll, phytoplankton, zooplankton) — biomass or concentration */
    biological_tracers = "biological_tracers",
    /** Nutrients (e.g., dissolved oxygen, NO₃⁻, NH₄⁺) */
    nutrients = "nutrients",
    /** Zonal velocity (u) */
    zonal_velocity = "zonal_velocity",
    /** Meridional velocity (v) */
    meridional_velocity = "meridional_velocity",
    /** Vertical velocity (w) */
    vertical_velocity = "vertical_velocity",
    /** CO₂ variables (xCO₂, pCO₂, fCO₂) */
    co2 = "co2",
    /** Any model output variable that does not fall into a specific category above. */
    other = "other",
};

export enum GenesisType {
    
    measured = "measured",
    calculated = "calculated",
};

export enum ObservationType {
    
    profile = "profile",
    surface_underway = "surface_underway",
    time_series = "time_series",
    laboratory_experiments = "laboratory_experiments",
    mesocosm = "mesocosm",
    field_experiments = "field_experiments",
    natural_analogues = "natural_analogues",
    model_outputs = "model_outputs",
};

export enum AppropriateUseQuality {
    
    weather_quality = "weather_quality",
    climate_quality = "climate_quality",
    other = "other",
};

export enum TitrationCellType {
    
    open = "open",
    closed = "closed",
};
/**
* Whether concentration measurements are expressed per unit volume or per unit mass.
*/
export enum ConcentrationBasis {
    
    /** Concentration expressed per unit volume (e.g., μmol/L, mmol/L) */
    per_volume = "per_volume",
    /** Concentration expressed per unit mass (e.g., μmol/kg-seawater) */
    per_mass = "per_mass",
};
/**
* Taxonomic code system used for species identification.
*/
export enum TaxonomicCodeSystem {
    
    /** Integrated Taxonomic Information System */
    itis = "itis",
    /** World Register of Marine Species */
    worms = "worms",
    /** Catalogue of Life */
    col = "col",
    /** Paleobiology Database */
    pbdb = "pbdb",
};
/**
* Life stage of the biological subject.
*/
export enum LifeStage {
    
    egg = "egg",
    embryo = "embryo",
    larva = "larva",
    juvenile = "juvenile",
    adult = "adult",
    other = "other",
};
/**
* Whether the socioeconomic data is quantitative or qualitative.
*/
export enum QuantitativeQualitative {
    
    quantitative = "quantitative",
    qualitative = "qualitative",
};
/**
* Type of social study conducted.
*/
export enum SocialStudyType {
    
    /** Public perception survey */
    public_perception_survey = "public_perception_survey",
    /** Ecosystem service valuation survey */
    ecosystem_service_valuation_survey = "ecosystem_service_valuation_survey",
    /** Text analysis */
    text_analysis = "text_analysis",
    /** Other study type */
    other = "other",
};



export interface PropertyValue {
}



export interface Any {
}


/**
 * A geospatial area of interest, defined by a bounding box, polygon/line, or a point designated as a pair of geo-coordinates.
 */
export interface Place {
    /** Entities that have a somewhat fixed, physical extension. (imported from schema.org) */
    geo?: Any,
}


/**
 * A bounding box defined by latitude and longitude coordinates.
 */
export interface SpatialCoverage extends Place {
}


/**
 * A specific location of dosing for an OAE intervention and/or tracer study. Can be a point, line, or bounding box
 */
export interface DosingLocation extends Place {
    /** Exact filename, URL and/or DOI to access the location file. Format should be one of GeoJSON or Shapefile. */
    dosing_location_file?: string,
}


/**
 * The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points. (imported from schema.org)
 */
export interface GeoShape {
    /** A bounding box defined by two corner points — the southwest (lower-left) corner followed by the northeast (upper-right) corner. Per science-on-schema.org, each point is written as `<latitude> <longitude>` in decimal degrees (WGS 84), with all four values space-separated: `"<minLat> <minLon> <maxLat> <maxLon>"`. Example: `"39.3280 120.1633 40.445 123.7878"`. See https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md#spatial-coverage */
    box?: string,
    /** A line is a point-to-point path consisting of two or more points. A line is expressed as a series of two or more point objects separated by space. */
    line?: string,
}


/**
 * A geographic coordinate in decimal degrees.
 */
export interface GeoCoordinates {
    /** Latitude in decimal degrees of a location. For example 37.42242 (WGS 84). */
    latitude: number,
    /** Longitude in decimal degrees of a location. For example -122.08585 (WGS 84). */
    longitude: number,
}


/**
 * The vertical extent of a place or structure in meters.
 */
export interface VerticalExtent {
    /** Minimum depth of observation in meters. Use negative numbers for depths below sea level. */
    min_depth_in_m?: number,
    /** Maximum depth of observation in meters. Use negative numbers for depths below sea level. */
    max_depth_in_m?: number,
    /** Minimum height of observation (in meters) for above ground aerial coverage. */
    min_height_in_m?: number,
    /** Maximum height of observation (in meters) for above ground aerial coverage. */
    max_height_in_m?: number,
}



export interface Organization {
    /** Organization identifier in the form of an ROR URL (e.g., https://ror.org/02mhbdp94). Please visit [https://ror.org](https://ror.org) to search for the organization and find the appropriate ROR URL. */
    identifier?: string,
    /** Name of the organization */
    name: string,
    /** The country in which the organization belongs. */
    country?: string,
}


/**
 * A project conducting OAE field trials or modeling.
 */
export interface Project {
    /** Name of the project the data collection is part of. For example, West Coast Ocean Acidification (WCOA) Project. */
    name: string,
    /** The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable. */
    project_id: string,
    /** A narrative description of the project. For example, what were the goals of the project? What were the research questions? What were the processes to achieve these goals and answer these questions? Who were the key stakeholders, organizers, project leaders? Was this building off a previous or ongoing project, or is this a new region/experiment/mechanistic study?
If there are relevant regulatory parameters and/or limits to dosing trials at this location, these may be described here. */
    description: string,
    /** The start and end date (optional) of the project */
    temporal_coverage: string,
    /** Latitude/longitude bounds of project site (e.g., boundary domain of observations or relevant activities), expressed as a schema.org GeoShape bounding box. */
    spatial_coverage: SpatialCoverage,
    experiments?: Experiment[],
    /** Provide details for each project lead / principal investigator (PI) including: Name, institutional information (name, address), phone, email, ID type (e.g., ORCID, etc), researcher ID, and role. */
    project_leads: Person[],
    /** Names of the seas where the data collection takes place, See Controlled Vocabularies section for definitions. */
    sea_names?: string,
    /** Provide information to help characterize the field site and provide context when interpreting the data. For example, descriptions of tidal patterns, climatological conditions, notable geological characteristics, the geographical and marine setting (coastal, intertidal, island region, sheltered environment), and characteristic meteorological events. If possible based on the file type of this submission, please include useful maps or figures here.
Links to relevant datasets, cruise reports, etc may be provided here. */
    physical_site_description?: string,
    /** Details may include:
  - Commercial, recreational, ecological, and cultural uses of study site
  - Industrial site history
  - Demographics of site area
  - Notable events that may impact local sentiment to mCDR (for example: site had significant toxic spill in past decade, local positive support for offshore wind farming, frequent HAB site) -Ecologically protected species, economically significant operations in the marine environment
  - In study areas with nearby state or federal jurisdiction borders, potential conflicts with other countries or permits from foreign governments should be described.
  - Links to relevant social science surveys, engaged community groups, etc. */
    social_context_site_description?: string,
    /** A description of any social research conducted to date. If provided as a separate file, list filename here. Information may include:
  - Description of Community engagement research approach conducted and results
  - Stakeholder mapping method and link to output */
    social_research_conducted_to_date?: string,
    /** The Marine Carbon Dioxide Removal (MCDR) pathway being studied. */
    mcdr_pathway: string,
    /** This field is required for co-located operations that potentially impact the project results. If previous or on-going mCDR field operations have occurred in the study domain by any project developer, they may be mentioned here either as a description, and/or if a reference to the study exists in the form of a data set, publication, etc, the DOI or other identifying information should be provided. Please provide direct links to data when available. */
    previous_or_ongoing_colocated_research?: ExternalProject[],
    /** A description is required if any nearby operations exist that may influence the waters over the time period covered by this data. This might be a nearby mCDR project, a facility that discharges water with different characteristics than the inflow (e.g., a desalination plant), frequent boating operations, etc. */
    colocated_operations?: string,
    /** Include the name of the funder, funder country, project title, project ID, and the project start and end dates. If there is no funding source (e.g., in the case of commercial projects), leave this field empty. */
    funding?: MonetaryGrant[],
    /** Open text area to include additional information. These may include information for sediment processes data, biological data, or any other required information if not included in the main metadata or data files.
See [General Guidelines for Your Data](https://www.carbontosea.org/oae-data-protocol/1-0-0/#general-guidelines-for-your-data) for relevant sections of your data. Additional informational files, such as digitized laboratory notebooks, blogs, etc., may be linked here. */
    additional_details?: string,
}


/**
 * A link to a resource with a name and URL.
 */
export interface NamedLink {
    /** The name of the linked resource. */
    name: string,
    /** The URL of the linked resource. */
    url: string,
}


/**
 * A research project that is not directly managed by the OAE project, but whose location is proximal to the OAE project and whose data may be relevant to understanding the context or impacts of OAE activities.
 */
export interface ExternalProject {
    /** Start date and end date (if known) of the project in ISO-8601 interval format (YYYY-MM-DD/YYY-MM-DD). If the end date is not known, use open-ended format YYYY-MM-DD/.. */
    temporal_coverage: string,
    /** Latitude/longitude bounds of project site (e.g., boundary domain of observations or relevant activities), expressed as a schema.org GeoShape bounding box. */
    spatial_coverage: SpatialCoverage,
    /** The name of the external research project. */
    name: string,
    /** A brief description of the external research project. */
    description?: string,
    /** Links to websites or documents related to the external research project. */
    related_links?: string[],
}



export interface MonetaryGrant {
    /** Name of the grant */
    name?: string,
    /** Unique identifier of the grant. Should be be URL or project id used by the funder */
    identifier?: string,
    start_date?: date,
    end_date?: date,
    funder?: Organization,
}


/**
 * A permit associated with the project.
 */
export interface Permit {
    /** The unique identifier or number associated with this permit. */
    permit_id: string,
    /** The group that issued the permit. */
    permitting_authority: string,
    /** The point of contact at the permitting agency. */
    agency_contact?: string,
    /** e.g., changes of discharge pH and basis for changes */
    changes_to_evolution_of_permit_criteria?: string,
    /** The category of permit (E.g., experimental permit, commercial permit) */
    permit_type?: string,
    /** The time period during which the permit will be applicable, or expected duration of the permit. */
    time_period?: string,
    /** Filename(s), links and/or DOIs to access files of permitting documents, separated by commas */
    approval_document: string,
}


/**
 * Abstract base class for all experiment types. Contains fields common to both in-situ and model experiments.
 */
export interface Experiment {
    /** Common name for experiment. */
    name: string,
    /** A narrative description of the experiment. For example, what part of the project do these data represent (e.g., baseline, intervention, control) and what do they contribute to the overall project? Are all project research questions listed in Project description relevant? What were the processes to achieve these goals and answer these questions? Data submitters are encouraged to note any significant changes to the original experimental plan due to unforeseen circumstances here. */
    description: string,
    /** Latitude/longitude bounds of observed data in experiment, expressed as a schema.org GeoShape bounding box. */
    spatial_coverage: SpatialCoverage,
    /** The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable. */
    project_id: string,
    /** The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:
Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01 */
    experiment_id: string,
    /** The type(s) of mCDR experiment conducted. See Controlled Vocabularies section for definitions. */
    experiment_types: string,
    /** Public comment documents, each with a link or DOI and an optional description.
Please group/concatenate all public comments associated with a specific consultation (e.g., for permitting, non-mandated consultations on a specific topic, or informal public input such as unsolicited comments and media attention) into a single document if possible, and link to it here. */
    public_comments?: PublicComment[],
    /** Provide details for each experiment lead / principal investigator (PI) including: Name, institutional information (name, address), phone, email, ID type (e.g., ORCID, etc), researcher ID, and role. */
    experiment_leads: Person[],
    /** Start date and time of experiment in UTC ISO-8601 */
    start_datetime: string,
    /** End date and time of experiment in UTC ISO-8601 */
    end_datetime?: string,
}


/**
 * Experiment metadata for in-situ studies (interventions, tracer studies, etc.). Contains fields specific to field-based experiments that don't apply to model experiments.
 */
export interface InSituExperiment extends Experiment {
    /** Minimum and maximum depths of observations in meters. */
    vertical_coverage?: VerticalExtent,
    /** Associated permit number(s). */
    permits?: Permit[],
    /** If data exist that are or have been used by the project but are not provided due to conflicts (e.g., geopolitical or other), data availability (e.g., a dataset is no longer available), it may be noted here. */
    data_conflicts_and_unreported_data?: string,
    /** Include links to relevant open datasets if referenced in the experiment but not provided in the submission. */
    meteorological_and_tidal_data?: NamedLink[],
    /** Open text area to include additional information. These may include information for sediment processes data, biological data, or any other required information if not included in the main metadata or data files; see General Guidelines for Your Data for relevant sections of your data. Additional informational files, such as digitized laboratory notebooks, blogs, etc., may be linked here. */
    additional_details?: string,
}


/**
 * Additional metadata that applies to experiments where an intervention, such as an alkalinity addition, was conducted.
 */
export interface Intervention extends InSituExperiment, InterventionDetails, DosingDetails {
}


/**
 * Additional metadata that applies to experiments where a tracer study was conducted
 */
export interface Tracer extends InSituExperiment, TracerDetails, DosingDetails {
}


/**
 * Additional metadata that applies to hybrid experiments where an intervention was conducted simultaneously alongside a tracer study, using the same instrumentation.
 */
export interface InterventionWithTracer extends Intervention, TracerDetails {
}


/**
 * A public comment document associated with a consultation for this experiment.
 */
export interface PublicComment {
    /** A narrative description of what this public comment contains. */
    description?: string,
    /** Link or DOI to access the public comment document. */
    url: string,
    /** The kind of consultation these comments came from. */
    comment_type: string,
}


/**
 * An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are specific to an Experiment with type "Intervention"
 */
export interface InterventionDetails {
    /** Method(s) used to process the alkalinity feedstock. See Controlled Vocabularies section for definitions. */
    alkalinity_feedstock_processing: string,
    /** Custom description of alkalinity feedstock processing method when 'other' is selected in alkalinity_feedstock_processing. */
    alkalinity_feedstock_processing_custom?: string,
    /** The phase upon delivery to the ocean. See Controlled Vocabularies section for definitions. */
    alkalinity_feedstock_form: string,
    /** Examples may include: olivine, potassium hydroxide, magnesium hydroxide, lime, portlandite, calcium carbonate, anorthite, dolomite, periclase, brucite, magnesite, forsterite, sodium hydroxide, natrite, nahcolite, akermanite, akermanite, alunoakermanite, etc.
See Controlled Vocabularies section for selected examples (this list is not exhaustive, you may need to include your unique feedstock). */
    alkalinity_feedstock: string,
    /** Custom description of alkalinity feedstock when using a feedstock type not listed in the controlled vocabulary. */
    alkalinity_feedstock_custom?: string,
    /** Maximum CO₂ removal potential of a feedstock material. We recommend using an adjusted version of the Steinour equation (Gunning et al., 2010), which uses bulk elemental oxide composition to estimate the maximum CO₂ removal potential of a feedstock material. The calculation output is in the form of kg of CO₂ per tonne of feedstock and represents the quantitative hypothetical potential of the material to capture CO₂ as bicarbonate or carbonate. See Isometric's CO2 removal potential module for details. */
    alkalinity_feedstock_co2_removal_potential: number,
    /** Information such as feedstock source, characteristics, impurities, dilution prior to dosing, and concentration. For feedstock other than NaOH: trace metal composition and particulate grain size. Any variable information must be provided in the dosing data file, in this case include the data file and column header names here provided as variables. See [Intervention Data](https://www.carbontosea.org/oae-data-protocol/1-0-0/#intervention-data) for details. */
    alkalinity_feedstock_description: string,
    /** Whether the feedstock was pre-equilibrated or unequilibrated */
    equilibration: string,
    /** Fixed density or provide link/source to effluent density data if applicable. Please include whether density is directly measured or a derived value. If this is a variable included with your data, please note so here as 'alkalinity dosing effluent density is provided as a variable' and use 'dosing_effluent_density' for your column header name. */
    alkalinity_dosing_effluent_density: DosingConcentration,
}


/**
 * An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are specific to an Experiment with type "Tracer"
 */
export interface TracerDetails {
    /** The form of tracer upon delivery to the ocean (e.g. gas or dye-release) */
    tracer_form: string,
    /** If "other" was selected for Tracer Form, please specify the custom tracer form here. */
    tracer_form_custom?: string,
    /** state the kind of tracer used (e.g. rhodamine, or a specific gas) */
    tracer_details: string,
    /** Fixed concentration or provide link/source to tracer concentration separately in the dosing file. Please include whether concentration is directly measured or a derived value. If this is a variable included with your data, please note so here as 'tracer concentration provided as a variable' and use 'tracer_concentration' for your column header name. */
    tracer_concentration: DosingConcentration,
}


/**
 * Details of tracer concentration information
 */
export interface DosingConcentration {
    /** Indicates that the field in question is a derived value as opposed to one measured directly. */
    is_derived_value: boolean,
    /** Select ‘Variable’ if the concentration varies over time, or ‘Fixed Value’ if it is constant. Note: Variable concentrations must be provided in a data file. */
    is_provided_as_a_file: boolean,
    amount?: number,
    unit?: string,
}


/**
 * An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are specific to an Experiment with active dosing (e.g. type "Tracer", "Intervention", or "InterventionWithDosing")
 */
export interface DosingDetails {
    /** Type of dosing delivery method. See Controlled Vocabularies for definitions. */
    dosing_delivery_type: string,
    /** Provide latitude and longitude in decimal degrees. Depending on your method of dispersal, this information may be provided as a point source, vector, or bounding box. If provided as a vector, the latitude and longitude values should be included in the dosing data file. */
    dosing_location: DosingLocation,
    /** Descriptive dosing location */
    dosing_dispersal_hydrologic_location: string,
    /** Depth in meters. If this is variable, please include the schedule of depth changes and depths, or as a vector in meters with the data. */
    dosing_depth: string,
    /** A human readable summary description of the dosing regimen / frequency. Exact details must be provided in the corresponding dosing file with exact timestamps for dosing on/off schedule. */
    dosing_regimen: string,
    /** Please be descriptive. Information about the dosing mechanism must be included (outflow from pipe, diffuser, doser, manual placement)
E.g., outflow from existing facility pipe directly to ocean, manual riverine introduction, coastal distribution at three separate 30 meter long sections, pier-based diffuser to intercoastal bay, distributed from stationary barge 10 miles offshore. */
    dosing_description: string,
}


/**
 * Information about a researcher or investigator involved in the experiment.
 */
export interface Person {
    /** Full name of the person. */
    name: string,
    /** Institutional affiliation of the investigator. */
    affiliation?: Organization,
    /** Contact phone number. */
    phone?: string,
    /** Contact email address. */
    email: string,
    /** Type of Researcher ID (e.g., ORCID, ResearcherID). */
    identifier_type?: string,
    /** Unique researcher identifier value. */
    identifier?: string,
    /** Role of the investigator in the experiment (e.g., chief scientist, data submitter). */
    role?: string,
}


/**
 * Base calibration information for instruments.
 */
export interface Calibration {
    /** Factory calibration, lab calibration, or field calibration. */
    calibration_location?: string,
    /** Details of the calibration technique used. */
    technique_description: string,
    /** Citation or reference for the calibration method. */
    method_reference?: string,
    /** How often the instrument was calibrated. */
    frequency?: string,
    /** Date and time of most recent calibration in UTC. */
    last_calibration_date?: string,
    /** Information about calibration certificates. Ideally, the certificate should be made available in a PDF file with filename listed here. */
    calibration_certificates?: string,
}


/**
 * Calibration using Certified Reference Materials, used for DIC and TA instruments.
 */
export interface CRMCalibration extends Calibration {
    /** Manufacturer of the Certified Reference Material (e.g., Scripps, JAMSTEC). */
    crm_manufacturer: string,
    /** Batch number of the Certified Reference Material. */
    crm_batch_number: string,
}


/**
 * pH instrument calibration. Use this class directly for TRIS or other standards, and DyeCalibration when standard_used is dye.
 */
export interface PHCalibration extends Calibration {
    /** Temperature at which calibration was performed. */
    calibration_temperature?: string,
    /** Type of standard used to calibrate the pH measurement. */
    standard_used: string,
    /** Name of the standard used, when it is not in the list. */
    standard_used_custom?: string,
    /** Details on the standard (e.g., type of dye used) and how or where it was produced. */
    standard_type_and_production?: string,
    /** pH values of the calibration standards used. */
    ph_of_standards?: string,
}


/**
 * pH instrument calibration with an indicator dye standard.
 */
export interface DyeCalibration extends PHCalibration {
    /** Whether the dye has been purified. */
    dye_purified?: boolean,
    /** Correction method applied if dye was not purified. */
    correction_for_unpurified_dye?: string,
    /** Method used to correct for dye effects. */
    dye_correction_method?: string,
}


/**
 * Base CO2 gas detector calibration with standard gas information.
 */
export interface CO2Calibration extends Calibration {
    /** Standard gases used for calibration. */
    standard_gas_info?: StandardGas,
}


/**
 * CO2 calibration for discrete measurements, with calibration temperature.
 */
export interface DiscreteCO2Calibration extends CO2Calibration {
    /** Temperature at which calibration was performed. */
    calibration_temperature?: string,
}


/**
 * CO2 calibration for continuous measurements, with extended standard gas details.
 */
export interface ContinuousCO2Calibration extends CO2Calibration {
    /** Standard gases used for calibration. */
    standard_gas_info?: ContinuousStandardGas,
}


/**
 * Standard gas used for CO2 calibration.
 */
export interface StandardGas {
    /** Manufacturer of the standard gas. */
    manufacturer?: string,
    /** Concentrations of the CO2 standard gases that are used to calibrate the CO2 sensor, e.g., 260, 350, 510ppm. */
    concentration?: string,
    /** Uncertainties of the CO2 standard gas, e.g., 0.5%. */
    uncertainty?: string,
}


/**
 * Standard gas used for continuous CO2 calibration, with additional traceability and count information.
 */
export interface ContinuousStandardGas extends StandardGas {
    /** How many non-zero gas standards were used for the calibration. */
    number_of_nonzero_standards?: number,
    /** Information about traceability of standard gases to WMO standards. */
    traceability_to_wmo_standards?: string,
}


/**
 * Base class for scientific instruments used in analyzing samples for measurement.
 */
export interface AnalyzingInstrument {
    /** Manufacturer name of the instrument. */
    manufacturer?: string,
    /** Model number or name of the instrument. */
    model?: string,
    /** Type of instrument used to analyze samples or measure continuously. */
    instrument_type: string,
    instrument_type_custom?: string,
    /** Serial number of the instrument. */
    serial_number?: string,
    /** Precision of the instrument measurements. */
    precision?: string,
    /** Accuracy of the instrument measurements. */
    accuracy: string,
    /** Calibration information for this instrument. */
    calibration?: Calibration,
}


/**
 * pH measurement instrument with dye-based calibration.
 */
export interface PHInstrument extends AnalyzingInstrument {
    /** pH calibration information for this instrument. */
    calibration: Any,
}


/**
 * Instrument calibrated with Certified Reference Materials, used for DIC and TA measurements.
 */
export interface CRMInstrument extends AnalyzingInstrument {
    /** CRM calibration information for this instrument. */
    calibration: CRMCalibration,
}


/**
 * CO2 gas detector with standard gas calibration.
 */
export interface CO2GasDetector extends AnalyzingInstrument {
    /** Type of the CO2 gas detector (E.g., Infrared) */
    detector_type: string,
    /** CO2 calibration information for this instrument. */
    calibration: DiscreteCO2Calibration,
    /** Resolution of the CO2 sensor. */
    resolution?: string,
    /** Uncertainty of the CO2 sensor. */
    uncertainty?: string,
}


/**
 * CO2 gas detector for continuous measurements, with measurement frequency.
 */
export interface ContinuousCO2GasDetector extends CO2GasDetector {
    /** How often measurements are taken, e.g., every 140 seconds except during calibration. */
    measurement_frequency?: string,
    /** CO2 calibration information for this continuous instrument. */
    calibration: ContinuousCO2Calibration,
}


/**
 * Equilibrator used for continuous CO2 measurement.
 */
export interface CO2Equilibrator {
    /** Type of the equilibrator for the CO2 measurement. */
    equilibrator_type?: string,
    /** The total volume (in liters) of the CO2 equilibrator. */
    volume?: number,
    /** Is the equilibrator vented or not? */
    vented?: boolean,
    /** Flow rate (in L/min) of the flow through seawater. */
    water_flow_rate?: number,
    /** Flow rate (in L/min) of the gas from the equilibrator to the CO2 analyzer. */
    headspace_gas_flow_rate?: number,
}


/**
 * Generic sensor base class used in continuous CO2 measurements. Subclasses (e.g., TemperatureSensor, PressureSensor) specialize accuracy and precision units via slot_usage.
 */
export interface GenericSensor {
    /** Location of the sensor. */
    location?: string,
    /** Manufacturer of the sensor. */
    manufacturer?: string,
    /** Model number of the sensor. */
    model?: string,
    /** Serial number of the sensor. */
    serial_number?: string,
    /** Accuracy of the sensor. */
    accuracy?: number,
    /** Precision of the sensor. */
    precision?: number,
    /** Calibration information for the sensor. */
    calibration?: string,
    /** Additional comments about the sensor. */
    comments?: string,
}


/**
 * Temperature sensor used in continuous CO2 measurements. Accuracy and precision are reported in degrees Celsius.
 */
export interface TemperatureSensor extends GenericSensor {
}


/**
 * Pressure sensor used in continuous CO2 measurements. Accuracy and precision are reported in hectopascals (hPa).
 */
export interface PressureSensor extends GenericSensor {
}


/**
 * Information about CO2 measurements in marine air.
 */
export interface MarineAirMeasurement {
    /** Whether CO2 in marine air was measured. */
    measured: boolean,
    /** How often marine air CO2 is measured, e.g., 5 readings in a group every 5 hours. */
    measurement_interval?: string,
    /** Location and height of the marine air intake. */
    location_and_height?: string,
    /** Method used to dry the gas stream for marine air measurements. */
    drying_method?: string,
}


/**
 * Abstract root for all variable types (including non-measured)
 */
export interface Variable {
    /** Unit of measurement for this variable. */
    units?: string,
    /** High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use. */
    variable_type: string,
    /** The schema class name for this variable (e.g., "DiscretePHVariable"). Auto-populated by the metadata builder. */
    schema_class: string,
    /** A term from a community vocabulary that identifies this variable. CF standard names (NERC P07) are recommended. */
    standard_identifier?: VocabularyItemReference,
    /** The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name). */
    dataset_variable_name: string,
    /** Full descriptive name of the variable. */
    long_name: string,
}


/**
 * Abstract root for every variable that can appear in a FieldDataset — measured, calculated or contextual. Exists so FieldDataset.variables can range over exactly these classes: ranging over Variable would also admit ModelOutputVariable, which belongs only to a ModelOutputDataset.
 */
export interface FieldVariable extends Variable {
}


/**
 * A contextual or ancillary variable that is NOT directly measured or calculated by the project. Use for identifiers (Cruise_ID, Exp_ID), timestamps (Year_UTC, Time_UTC), coordinates (Latitude, Longitude), and any other data included in the dataset for context. Do NOT create a NonMeasuredVariable for quality control flag columns — instead, set dataset_variable_name_qc_flag on the parent measured or calculated variable that the flag relates to. variable_type must be "non_measured".
 */
export interface NonMeasuredVariable extends FieldVariable {
}


/**
 * Base class for project-acquired variables (measured or calculated in-situ). Reference: OAPMetadata XSD variables.xsd - insitu_variable
 */
export interface InSituVariable extends FieldVariable {
    genesis: string,
    /** If applicable, the column header name used for the quality control flag corresponding to this variable. */
    dataset_variable_name_qc_flag?: string,
    /** If applicable, the column header name used for the raw data corresponding to this variable. */
    dataset_variable_name_raw?: string,
    /** Any additional information about this variable. */
    other_detailed_information?: string,
    /** Citation for the method used. */
    method_reference?: string,
    /** The name of the PI whose research team measured or derived this parameter. */
    measurement_researcher?: Person,
}


/**
 * Variable that is directly measured in-situ using instruments. Reference: OAPMetadata XSD variables.xsd - basic_measured_observation_base
 */
export interface MeasuredVariable extends InSituVariable, QCFields {
    /** Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information. */
    analyzing_instrument: AnalyzingInstrument,
    /** Method used to collect samples. */
    sampling_method: string,
    /** Repetition of sample collection and measurement, e.g., triplicate samples. */
    field_replicate_information?: string,
    /** Additional information describing how the sample was analyzed. DOIs provided as applicable. */
    analyzing_method: string,
    observation_type: string,
    sampling: string,
    sampling_instrument_type: string,
    sampling_instrument_type_custom?: string,
}


/**
 * A variable measured in-situ from discrete water samples (e.g., bottle samples analyzed in a lab or shipboard). Use this class for generic measured variables that do not fall under a specific category (pH, TA, DIC, CO2, sediment, HPLC). For those, use the type-specific subclass instead (e.g., DiscretePHVariable). Set variable_type to "other", genesis to "measured", and sampling to "discrete".
 */
export interface DiscreteMeasuredVariable extends MeasuredVariable {
}


/**
 * A variable measured in-situ by a continuous autonomous sensor (e.g., temperature, salinity, conductivity, pressure from a deployed sonde or underway system). Use this class for generic measured variables that do not fall under a specific category (pH, TA, DIC, CO2, sediment). For those, use the type-specific subclass instead (e.g., ContinuousPHVariable). Set variable_type to "other", genesis to "measured", and sampling to "continuous".
 */
export interface ContinuousMeasuredVariable extends MeasuredVariable {
    /** The method used to calculate reported values from raw sensor data. */
    raw_data_calculation_method: string,
    /** Version of the software used to calculate reported values from raw values. */
    calculation_software_version?: string,
}


/**
 * A variable that is calculated or derived from other measured variables rather than directly measured by an instrument (e.g., carbonate system parameters computed via CO2SYS). Set genesis to "calculated". The variable_type should reflect the quantity being calculated (e.g., "pH", "ta", "dic", "co2", or "other").
 */
export interface CalculatedVariable extends InSituVariable, QCFields {
    /** Information about how the variable was calculated and the parameters used in calculation, e.g.: Calculation software = CO2SYSv1 (MATLAB) Input variables =  pH and DIC (column header names 'ph_t_insitu' and 'dic' in associated dataset file) Additional information = the dissociation constants of Lueker et al., 2000 for carbonic acid, etc. */
    calculation_method_and_parameters: string,
}


/**
 * pH measured variable from continuous autonomous sensor
 */
export interface ContinuousPHVariable extends ContinuousMeasuredVariable, MeasuredPHFields {
}


/**
 * pH measured variable with dye-based spectrophotometric measurement. Reference: OAPMetadata XSD variables.xsd - pH_measured
 */
export interface DiscretePHVariable extends DiscreteMeasuredVariable, MeasuredPHFields {
    /** Temperature at which pH was measured. */
    measurement_temperature: string,
    /** Method used to correct pH for temperature. */
    temperature_correction_method?: string,
    /** The input could be a constant temperature value, or something like, in-situ temperature, temperature of analysis, etc. */
    ph_reported_temperature: string,
}


/**
 * Total Alkalinity (TA) measured variable from continuous autonomous sensor
 */
export interface ContinuousTAVariable extends ContinuousMeasuredVariable, MeasuredTAFields {
}


/**
 * Total Alkalinity (TA) measured variable from discrete bottle samples
 */
export interface DiscreteTAVariable extends DiscreteMeasuredVariable, MeasuredTAFields {
    /** How the samples were preserved for analysis. */
    sample_preservation: SamplePreservation,
    /** Whether the reported variables were corrected for blank, and if so, how they were corrected. */
    blank_correction: string,
    /** Type of the titration used to determine alkalinity. */
    titration_type: string,
    /** Whether the titration cell is open or closed. */
    titration_cell_type?: string,
    /** Curve fitting method used to determine the alkalinity. */
    curve_fitting_method?: string,
}


/**
 * Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous sensor.
 */
export interface ContinuousDICVariable extends ContinuousMeasuredVariable, MeasuredDICFields {
}


/**
 * Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle samples. Uses CRM-calibrated instrument and includes sample preservation information. Reference: OAPMetadata XSD variables.xsd - DIC_measured
 */
export interface DiscreteDICVariable extends DiscreteMeasuredVariable, MeasuredDICFields {
    /** How the samples were preserved for analysis. */
    sample_preservation: SamplePreservation,
    /** Whether the reported variables were corrected for blank, and if so, how they were corrected. */
    blank_correction: string,
}


/**
 * Measured sediment variable collected from continuous autonomous sensor
 */
export interface ContinuousSedimentVariable extends ContinuousMeasuredVariable, MeasuredSedimentFields {
}


/**
 * Measured sediment variable collected from discrete bottle samples
 */
export interface DiscreteSedimentVariable extends DiscreteMeasuredVariable, MeasuredSedimentFields {
}


/**
 * CO2 discrete (bottle) measured variable (pCO2/fCO2). Reference: OAPMetadata XSD variables.xsd - co2_discrete
 */
export interface DiscreteCO2Variable extends DiscreteMeasuredVariable, MeasuredCO2Fields {
    /** How the samples were stored before the measurement. */
    storage_method: string,
    /** Volume (in mL) of seawater in the flask. */
    seawater_volume?: number,
    /** Volume (in mL) of headspace (water displaced in the flask plus volume of the tubing). */
    headspace_volume?: number,
    /** Temperature at which the samples were analyzed in Celsius. */
    measurement_temperature: number,
}


/**
 * CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2). Reference: OAPMetadata XSD variables.xsd - co2_continuous
 */
export interface ContinuousCO2Variable extends ContinuousMeasuredVariable, MeasuredCO2Fields {
    /** Equilibrator used for CO2 measurement. */
    equilibrator?: CO2Equilibrator,
    /** Temperature sensor for the equilibrator. */
    equilibrator_temperature_sensor?: TemperatureSensor,
    /** Pressure sensor for the equilibrator. */
    equilibrator_pressure_sensor?: PressureSensor,
    /** Atmospheric pressure sensor. */
    atmospheric_pressure_sensor?: PressureSensor,
    /** Whereabouts of the seawater intake. */
    seawater_intake_location: string,
    /** Water depth of the seawater intake. */
    seawater_intake_depth: string,
    /** The method used to dry the gas coming out of CO2 equilibrator, before it is pumped into the CO2 sensor. */
    drying_method?: string,
    /** Information about CO2 measurements in marine air. */
    marine_air_measurement?: MarineAirMeasurement,
}


/**
 * HPLC (High-Performance Liquid Chromatography) measured variable for pigment analysis. Always measured, not calculated.
 */
export interface HPLCVariable extends DiscreteMeasuredVariable {
    /** The name of the lab where the HPLC analysis was run (e.g., 'NASA_GSFC' */
    hplc_lab: string,
    /** Name and contact information for HPLC technician. */
    hplc_lab_technician?: string,
}


/**
 * Physiological response variable from discrete field samples (e.g., organism growth rates, calcification rates, gene expression from bottle or tissue samples collected in the field).
 */
export interface DiscretePhysiologicalVariable extends DiscreteMeasuredVariable, MeasuredPhysiologicalFields {
}


/**
 * Physiological response variable from continuous autonomous field sensors (e.g., respiration rates from deployed oxygen consumption monitors, heart rate from bio-loggers).
 */
export interface ContinuousPhysiologicalVariable extends ContinuousMeasuredVariable, MeasuredPhysiologicalFields {
}


/**
 * Socioeconomic variable for social and economic data such as survey responses, ecosystem service valuations, or text analysis. A field variable: includes method_reference and measurement_researcher, but does NOT include QCFields, instrument details, or calibration.
 */
export interface SocioeconomicVariable extends InSituVariable {
    /** Whether this variable captures quantitative (numerical) or qualitative (categorical/textual) data. */
    quantitative_or_qualitative: string,
    /** The type of social science study this variable comes from. */
    social_study_type?: string,
    /** Custom study type description when "other" is selected. */
    social_study_type_custom?: string,
    /** Time period and location description for the social study (e.g., "2023-2024, coastal communities in Maine, USA"). */
    social_study_site_characterization?: string,
}


/**
 * A variable output by a model simulation (e.g., air-sea CO2 flux, dissolved inorganic carbon, total alkalinity, pH, temperature, salinity from an OAE model run). Model outputs are produced by the simulation itself, so they carry none of the sampling, instrument, calibration or in-situ QC metadata that field-collected variables do — how the output was produced is described by the simulation configuration on the parent ModelOutputDataset.
 */
export interface ModelOutputVariable extends Variable {
}


/**
 * Sample preservation information for DIC and TA measurements. Reference: OAPMetadata XSD variables.xsd - sample_preservation
 */
export interface SamplePreservation {
    /** As described, e.g., Mercury Chloride. */
    preservative: string,
    /** The volume of preservative used. */
    volume: string,
    /** Description of how the preservative effect was corrected for. */
    correction_description?: string,
}



export interface VocabularyItemReference {
    /** A narrative description of the thing. */
    description?: string,
    term: string,
    uri: string,
}


/**
 * Fields applied to all measured TA variable types (discrete and continuous)
 */
export interface MeasuredTAFields {
    /** Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf. */
    appropriate_use_quality?: string,
    /** Whether measurements are expressed per unit volume or per unit mass (for DIC, TA, etc.) */
    concentration_basis: string,
}


/**
 * Fields applied to all measured DIC variable types (discrete and continuous)
 */
export interface MeasuredDICFields {
    /** Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf. */
    appropriate_use_quality?: string,
    /** Whether measurements are expressed per unit volume or per unit mass (for DIC, TA, etc.) */
    concentration_basis: string,
}


/**
 * Fields applied to all measured pH variable types (discrete and continuous)
 */
export interface MeasuredPHFields {
    /** Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf. */
    appropriate_use_quality?: string,
}


/**
 * Fields applied to all measured sediment variable types (discrete and continuous)
 */
export interface MeasuredSedimentFields {
    /** e.g., mud, sand, etc. */
    sediment_type: string,
    /** Depth that sediment was collected below sediment surface. If provided as a variable (recommended), please list the column header name here. */
    sediment_sampling_depth: string,
    /** Water depth where sediment was collected. If provided as a variable (recommended), please list the column header name here. */
    sediment_sampling_water_depth: string,
}


/**
 * Fields applied to all measured physiological variable types (discrete and continuous). Captures biological subject identification and experimental design information for organism response field studies.
 */
export interface MeasuredPhysiologicalFields {
    /** Taxonomy (species, genus, or community) being studied (e.g., Crassostrea gigas, coral reef community). */
    biological_subject: string,
    /** Species reference code from a taxonomic database (e.g., WoRMS AphiaID 140656, ITIS TSN 79861). */
    species_identification_code?: string,
    /** Which taxonomic code system the identification code refers to. */
    taxonomic_code_system?: string,
    /** Life stage of the organism at time of measurement. */
    life_stage?: string,
    /** Custom life stage description when "other" is selected. */
    life_stage_custom?: string,
}


/**
 * Fields applied to all measured CO2 variable types (discrete and continuous)
 */
export interface MeasuredCO2Fields {
    /** Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf. */
    appropriate_use_quality?: string,
    /** In Celsius. The input could be a constant temperature value, or something like, in-situ temperature, temperature of analysis, etc. */
    pco2_reported_temperature: string,
    /** How the water vapor pressure inside the equilibrator was determined. */
    water_vapor_correction_method?: string,
    /** How the temperature effect was corrected. */
    temperature_correction_method?: string,
}


/**
 * Quality control fields applicable to measured and calculated variables. Not applied to socioeconomic variables.
 */
export interface QCFields {
    /** Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here. */
    qc_steps_taken?: string,
    /** It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here. */
    uncertainty?: string,
    /** A description of the uncertainties involved in this method. */
    uncertainty_definition?: string,
    /** The indicator used to represent missing values in the data file, e.g., -999, NaN, etc. */
    missing_value_indicators?: string,
    /** The name of the PI whose research team QCed this parameter. */
    qc_researcher?: string,
    /** The institution of the PI whose research team QCed this parameter. */
    qc_researcher_institution?: string,
}


/**
 * Abstract base class for all dataset types. Contains fields common to both field/observational and model simulation datasets. Generally following guidelines & best practices as outlined in [science-on-schema.org](https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md)
 */
export interface Dataset {
    /** A brief descriptive sentence that summarizes the content of a dataset. Here is one example:
"Dissolved inorganic carbon, total alkalinity, pH, temperature, salinity and other variables collected from profile and discrete sample observations using CTD, Niskin bottle, and other instruments from R/V Wecoma in the U.S. West Coast California Current System during the 2011 West Coast Ocean Acidification Cruise (WCOA2011) from 2011-08-12 to 2011-08-30" */
    name: string,
    /** The abstract of a dataset is a brief summary that provides an overview of the dataset's content, purpose, and scope. It is used to provide context and background information to users who are interested in using the dataset. An abstract may include information such as the dataset's source, how the data was collected or generated, the variables or attributes included in the dataset, and any limitations or restrictions on the use of the data. It may also include information on how the data can be accessed or used. */
    description: string,
    /** The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable. */
    project_id: string,
    /** The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:
Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01 */
    experiment_id: string,
    filenames: string[],
    /** Selected controlled vocabularies for data types relevant to mCDR have been referenced from NASA's SeaBASS metadata system and are provided below, for additional data types of optical characteristics see the [SeaBASS controlled definitions list](https://seabass.gsfc.nasa.gov/wiki/metadataheaders#data_type). Additional data types have been included to meet the needs of mCDR field projects. */
    dataset_type: string,
    /** Custom "data type" when an appropriate value is not found in the controlled vocabulary list for mCDR Data Type and the corresponding `data_type` field is set to "other". */
    dataset_type_custom?: string,
    /** Information about the individual submitting the dataset(s), including contact information */
    data_submitter: Person,
    /** Author list in the format of Lastname1, Firstname1 Middlename1; Lastname2, Firstname2 Middlename2; ... */
    author_list_for_citation?: string,
    /** Link a Dataset to its license to document legal constraints by adding a schema:license property. The guide recommends providing a URL that unambiguously identifies a specific version of the license used, but for many licenses it is hard to determine what that URL should be. Thus, we recommend that the license URL be drawn from the [SPDX license list](https://spdx.org/licenses/), which provides a curated list of licenses and their properties that is well maintained. For each SPDX entry, SPDX provides a canonical URL for the license (e.g., http://spdx.org/licenses/CC0-1.0), a unique licenseId (e.g., CC0-1.0), and other metadata about the license. */
    license?: string,
    /** A statement from the data producer regarding how this dataset should be used. */
    fair_use_data_request?: string,
    /** Level of access to this dataset. Open Access data are freely available now, without restriction. Conditional Access data are available upon request, subject to review. Scheduled Access data will become openly available after a specified date; choose it for any data that are not openly available yet. */
    data_accessibility: string,
    /** URL to access this dataset, if it is already archived or published elsewhere. DOIs are preferred if available (e.g., https://doi.org/10.25921/xxxx-xxx). Required for open access, optional otherwise. */
    data_access_link?: string,
    /** The date by when this dataset will be openly available on a public repository. Only used when data_accessibility is scheduled_access; leave empty otherwise. */
    data_access_date?: date,
}


/**
 * A field or observational dataset related to an OAE experiment. Contains fields specific to in-situ data collection such as platform information, calibration files, QC flags, and measured variables.
 */
export interface FieldDataset extends Dataset {
    /** Start date and end date (if known) of the project in ISO-8601 interval format (YYYY-MM-DD/YYY-MM-DD). If the end date is not known, use open-ended format YYYY-MM-DD/.. */
    temporal_coverage: string,
    /** The variables in this dataset, each with its own metadata. */
    variables?: FieldVariable[],
    /** One of the three choices: (a) Originally collected dataset (e.g., a dataset collected from a research cruise or laboratory experiment), (b) Data compilation product (e.g., SOCAT, GLODAP), or (c) Derived product (e.g., gridded products, or model output). */
    data_product_type: string,
    /** Describe what the quality control flags stand for, e.g.,
  0 = interpolated or calculated data
  1 = not evaluated/quality unknown
  2 = acceptable
  3 = questionable
  4 = known bad
  6 = median of replicates
  9 = missing value" */
    qc_flag_scheme?: string,
    platform_info: Platform,
    /** A list of supplementary file names containing coefficients and techniques used to calibrate the instruments used in data collection. The named files can be found within the relevant documents folder accompanying the submitted data files. */
    calibration_files?: string[],
}


/**
 * A model simulation output dataset. Contains fields specific to computational model output including simulation configuration, output variables, and hardware information.
 */
export interface ModelOutputDataset extends Dataset {
    /** The variables in this dataset, each with its own metadata. */
    variables?: ModelOutputVariable[],
    /** The type(s) of model simulation (e.g., counterfactual, perturbation, or both). */
    simulation_type: string,
    /** Start date and time of the simulation in UTC ISO-8601. */
    start_datetime: string,
    /** End date and time of the simulation in UTC ISO-8601. */
    end_datetime: string,
    /** Frequency of model output (e.g., 'hourly mean', 'daily mean'). */
    output_frequency?: string,
    /** Description of the mCDR forcing applied in the simulation (e.g., the alkalinity perturbation). Required when simulation_type is "perturbation". */
    mcdr_forcing_description?: string,
    /** Details about the computational hardware used for the simulation. */
    hardware_configuration?: HardwareConfiguration,
}


/**
 * Details about the computational hardware used to run a model simulation.
 */
export interface HardwareConfiguration {
    /** Name of the machine or cluster (e.g., 'Perlmutter'). */
    machine?: string,
    /** Operating system used (e.g., 'Linux'). */
    operating_system?: string,
    /** Details about CPU/GPU hardware or link to specifications. */
    cpu_gpu_details?: string,
    /** Memory available (e.g., '512 GB DDR4'). */
    memory?: string,
    /** Storage available (e.g., '44 PB'). */
    storage?: string,
    /** Parallelization details (e.g., '3 nodes, 108 ntasks per node'). */
    parallelization?: string,
}



export interface Platform {
    /** Name of the observing platform, e.g., RV Ronald Brown, Saildrone#0132, Mooring_First_Landing, etc. */
    name?: string,
    /** For Platform Type definitions, see: https://vocab.nerc.ac.uk/collection/L06/current/ */
    platform_type: string,
    /** Synonymous with glider ID, cruise ID. A unique name assigned to oceanographic assets such as buoys, moorings, floats, drifters, towed vehicles like the Scanfish or StingRay. This is synonymous with the BCO-DMO “platform” parameter (https://www.bco-dmo.org/parameter/932), NERC “platform type” term (https://vocab.nerc.ac.uk/collection/W06/current/CLSS0001/), and the “platform_id” term within the Climate and Forecast (CF) metadata conventions (https://cfconventions.org/Data/cf-standard-names/current/build/cf-standard-name-table.html). e.g., ICES platform code (e.g., 33RO). */
    platform_id?: string,
    /** Institution that owns the platform. */
    owner?: string,
    /** Country to which the platform belongs. */
    country?: string,
}


/**
 * A computational model experiment related to OAE.
 */
export interface Model extends Experiment {
    /** Links to model configuration files or documentation. */
    model_configuration?: string[],
    /** Components of the model (e.g., physics, biogeochemistry). */
    model_components?: ModelComponent[],
    /** Details about the model grid(s). Use multiple entries for nested grid configurations. */
    grid_details?: ModelGrid[],
    /** Description of the model spin-up process. */
    spin_up_protocol?: string,
    /** Time-stepping method and time step used in the simulation. */
    time_stepping_scheme?: string,
}


/**
 * A component of a model (e.g., physics, biogeochemistry/ecosystem).
 */
export interface ModelComponent {
    /** A description of the model component characteristics.
For physics components, this should include the version of equations being solved (hydrostatic vs non-hydrostatic), tracer advection scheme, how bottom drag is represented, mixed layer parameterizations, sub-grid mixing parameterizations if applicable, etc.
For BGC components, this should include details of which parameters are modeled explicitly, derived carbonate system parameters, advection scheme for biological tracers, CO₂ solver protocol (e.g., CO₂SYS), links to data/code with biological model parameters (e.g., growth and mortality rates), etc. Equations for each explicitly modeled parameter should be provided (can be links to publications), and it should be noted if any equations or parameter values (e.g. growth rates) were modified. Description and/or references of air-sea CO₂ flux parameterization used, gas transfer velocity formulation and atmospheric CO₂ details (e.g., fixed or time varying, and if time varying which data were used). Also include details on whether dissolution and precipitation of calcium carbonate are considered, how exchanges between sediment and overlying water are represented (if applicable), and whether active feedbacks between biological processes and the carbonate system are represented.
Associated links to data, DOIs, or publications can be noted here, but should be supplemental. */
    description?: string,
    /** The type of model component (physics, BGC/ecosystem, or other). */
    model_component_type: string,
    model_component_type_custom?: string,
    /** Name of the model component (e.g., ROMS, MARBL, Oceananigans). */
    name: string,
    /** Release version of the model component. */
    version?: string,
    /** Link to model code repository. */
    codebase?: string,
    /** Links or DOIs to any reference(s) relevant to the model components/development, specific model configuration, model validation etc. */
    references?: string[],
}


/**
 * Details about a model grid. Use multiple ModelGrid entries to describe nested or multi-grid configurations.
 */
export interface ModelGrid {
    /** Name of the grid (e.g., 'inner grid', 'L1', 'global'). */
    grid_name?: string,
    /** Descriptive structure of the grid (e.g., latitude-longitude, unstructured triangular, tripolar). */
    grid_geometry?: string,
    /** Role of this grid in a nested or multi-grid configuration. */
    grid_type: string,
    /** Region covered by the grid. */
    region?: string,
    /** Bounding box for this grid, expressed as a schema.org GeoShape bounding box. */
    spatial_coverage?: SpatialCoverage,
    /** The grid arrangement of orthogonal physical quantities (e.g., Arakawa A, Arakawa B, Arakawa C). */
    arrangement?: string,
    /** The vertical grid coordinate type (e.g. z-coordinate, z*-coordinate, terrain-following coordinate, isopycnal coordinate) */
    vertical_coordinate_type?: string,
    /** Number of grid points in the x-direction. */
    n_x?: number,
    /** Number of grid points in the y-direction. */
    n_y?: number,
    /** Number of vertical coordinate levels. */
    n_z?: number,
    /** Number of nodes in the grid (for unstructured grids). */
    n_nodes?: number,
    /** Description of horizontal resolution (e.g., '3.3 km', '1/12 degree'). */
    horizontal_resolution_range?: string,
    /** Description of vertical resolution (e.g., 'Max. 4 m near surface, stretching to 500 m at depth'). */
    vertical_resolution_range?: string,
    /** Details about input data sources used to drive the model on this grid. */
    input_details?: ModelInputDetails,
}


/**
 * Details about input data sources used to drive the model.
 */
export interface ModelInputDetails {
    /** Bathymetry data source(s). */
    bathymetry?: NamedLink[],
    /** Initial condition data source(s). */
    initial_conditions?: NamedLink[],
    /** Boundary condition data source(s). */
    boundary_conditions?: NamedLink[],
    /** Atmospheric forcing data source(s). */
    atmospheric_forcing?: NamedLink[],
    /** Tidal forcing data source(s). */
    tidal_forcing?: NamedLink[],
    /** River and/or sediment flux data source(s). */
    river_sediment_flux_details?: NamedLink[],
    /** Narrative description of any processing applied to input data before use in the model. */
    processing_of_input_data?: string,
    /** If applicable, link to any code for processing of raw forcing and input data listed in the fields above. */
    processing_code?: NamedLink[],
}



export interface Container {
    project?: Project,
    experiments?: Experiment[],
    datasets?: Dataset[],
    /** Version of the oae-data-protocol */
    version?: string,
    /** Git commit hash of the oae-data-protocol */
    protocol_git_hash?: string,
    /** Git commit hash of the metadata-builder UI */
    metadata_builder_git_hash?: string,
}



