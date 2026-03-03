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
};
/**
* Variables commonly included in model simulation output datasets
*/
export enum ModelOutputVariable {
    
    /** Air-sea exchange of carbon dioxide */
    Air_sea_CO2_flux = "air_sea_co2_flux",
    /** Dissolved inorganic carbon (DIC) */
    Dissolved_Inorganic_Carbon = "dissolved_inorganic_carbon",
    /** Total alkalinity (TA) */
    Total_Alkalinity = "total_alkalinity",
    /** Temperature */
    temperature = "temperature",
    /** Salinity */
    salinity = "salinity",
    /** pH of seawater */
    pH = "ph",
    /** Phytoplankton biomass or concentration */
    phytoplankton = "phytoplankton",
    /** Horizontal velocity components (u, v) */
    Horizontal_velocity = "horizontal_velocity",
    /** Vertical velocity component (w) */
    Vertical_velocity = "vertical_velocity",
};

export enum SeaNames {
    
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSZZSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/ZZ/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSIJMSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/IJM/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSMKMSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/MKM/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSIRMSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/IRM/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS10SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/10/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS62aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/62a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS04SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/04/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS01cSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/01c/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS25SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/25/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSSOCSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/SOC/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS33SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/33/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS16aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/16a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28AbSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Ab/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48oSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48o/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSESCSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/ESC/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS39SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/39/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS57bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/57b/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSICSSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/ICS/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS53SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/53/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS35SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/35/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS200SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/200/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS61bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/61b/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS22SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/22/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28BfSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Bf/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS11SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/11/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS63SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/63/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS03SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/03/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS12SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/12/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28BSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28B/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48eSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48e/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS47SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/47/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28AaSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Aa/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS45SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/45/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSWSCSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/WSC/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS62SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/62/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS40SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/40/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS23bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/23b/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS06SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/06/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS42SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/42/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS51SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/51/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS45aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/45a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS32bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/32b/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS21SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/21/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28CSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28C/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48mSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48m/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS01bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/01b/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS26SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/26/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS13SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/13/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28ASOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28A/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS32SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/32/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48jSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48j/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48hSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48h/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS31SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/31/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS57aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/57a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS05SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/05/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS50SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/50/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSARASOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/ARA/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS61aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/61a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS21aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/21a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28BgSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Bg/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48nSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48n/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS01aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/01a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS27SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/27/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS14SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/14/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS60SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/60/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48fSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48f/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS49SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/49/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48lSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48l/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48iSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48i/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS41SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/41/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS30SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/30/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS23aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/23a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS08SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/08/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS32aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/32a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS20SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/20/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS17aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/17a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28AeSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Ae/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS17SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/17/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS59SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/59/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS64SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/64/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48kSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48k/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48b/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS01SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/01/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS44SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/44/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS55SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/55/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS38SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/38/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS29SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/29/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS07SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/07/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS56SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/56/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS19SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/19/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS15aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/15a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS46bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/46b/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS14aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/14a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28AdSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Ad/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS61SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/61/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS58SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/58/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS65SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/65/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48gSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48g/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48dSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48d/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS23SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/23/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS43SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/43/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS54SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/54/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS37SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/37/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSCASSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/CAS/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS09SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/09/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS18SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/18/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS02SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/02/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS24SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/24/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS46SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/46/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS46aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/46a/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS16SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/16/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28AcSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Ac/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS57SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/57/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS66SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/66/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSWASSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/WAS/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48cSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48c/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSFRMSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/FRM/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS500SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/500/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS15SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/15/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS52SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/52/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS36SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/36/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSGLOSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/GLO/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS34SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/34/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28BhSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Bh/",
};

export enum PlatformType {
    
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS99SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/99/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS6DSOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/6D/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS3CSOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/3C/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS36SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/36/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS18SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/18/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS30SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/30/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS61SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/61/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS26SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/26/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS16SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/16/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS3ASOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/3A/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS41SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/41/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS72SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/72/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS43SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/43/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS15SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/15/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS13SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/13/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS6ASOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/6A/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS44SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/44/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS68SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/68/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS33SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/33/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS19SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/19/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS11SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/11/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS12SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/12/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS23SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/23/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS17SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/17/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS3BSOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/3B/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS45SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/45/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS42SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/42/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS47SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/47/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS14SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/14/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS71SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/71/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS46SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/46/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS20SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/20/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS27SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/27/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS25SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/25/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS3ZSOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/3Z/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS48SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/48/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS31SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/31/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS62SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/62/",
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS67SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/67/",
};

export enum MassConcentrationUnit {
    
    unitCOLONKiloGM_PER_M3 = "unit:KiloGM-PER-M3",
    unitCOLONMicroGM_PER_L = "unit:MicroGM-PER-L",
    unitCOLONMicroGM_PER_L_DAY = "unit:MicroGM-PER-L-DAY",
    unitCOLONMicroGM_PER_MilliL = "unit:MicroGM-PER-MilliL",
    unitCOLONMilliGM_PER_L = "unit:MilliGM-PER-L",
    unitCOLONMilliGM_PER_M3 = "unit:MilliGM-PER-M3",
    unitCOLONMilliGM_PER_MilliL = "unit:MilliGM-PER-MilliL",
    unitCOLONNanoGM_PER_L = "unit:NanoGM-PER-L",
    unitCOLONNanoGM_PER_MilliL = "unit:NanoGM-PER-MilliL",
    unitCOLONPicoGM_PER_MilliL = "unit:PicoGM-PER-MilliL",
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
    /** A pH sensor. The sensor can be used for ocean acidification, research coral reef sensitivity analysis and environmental monitoring. The sensor measures pH with a range of 6.5 to 9.0. The sensing element is an ion  sensitive field effect transistor. The pH sensor has an initial accuracy of +/-0.05 pH, precision of 0.001 pH and stability of 0.005 pH/month. It can operate in temperatures ranging from 0 deg C to 50 deg C and up to depths of 50 m. */
    sea_bird_seafet_v1 = "sea_bird_seafet_v1",
    /** A pH sensor. The sensor can be used for ocean acidification, research coral reef sensitivity analysis and environmental monitoring. The sensor measures pH with a range of 6.5 to 9.0. The sensing element is an ion sensitive field effect transistor. V2 implements improvements to the original SeaFET's reliability, data quality, ease of operation, and deployment endurance, with significant changes to how users interface with the instrument. The pH sensor has an accuracy to +/-0.05 pH, precision of 0.004 pH and stability of 0.003 pH/month. It can operate in temperatures ranging from 0 deg C to 50 deg C and up to depths of 50 m. */
    sea_bird_seafet_v2 = "sea_bird_seafet_v2",
    /** An oxygen titrator is a device used to measure the concentration of dissolved oxygen in a water sample, as required for the Winkler method. */
    oxygen_titrator = "oxygen_titrator",
    /** An oxygen sensor or probe or sond, is an electronic device that measures the concentration of dissolved oxygen in the ocean. */
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



export interface PropertyValue {
}



export interface Any {
}


/**
 * A geospatial area of interest, defined by a bounding box, polygon/line, or a point designated as a  pair of geo-coordinates.
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
    /** Exact path and filename for the location file (relative to root path of project), attached separately. Format should be one of GeoJSON or Shapefile. */
    dosing_location_file?: string,
}


/**
 * The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points. (imported from schema.org)
 */
export interface GeoShape {
    /** A box defined by two latitude-longitude points, southwest and northeast. */
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
    /** The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable. */
    project_id: string,
    /** A narrative description of the project. For example, what were the goals of the project? What were the research questions? What were the processes to achieve these goals and answer these questions? Who were the key stakeholders, organizers, project leaders? Was this building off a previous or ongoing project, or is this a new region/experiment/mechanistic study?
If there are relevant regulatory parameters and/or limits to dosing trials at this location, these may be described here. */
    description: string,
    /** The start and end date (optional) of the project */
    temporal_coverage: string,
    /** Latitude/longitude bounds of project site (e.g., boundary domain of observations or relevant activities) provided in decimal degrees as westernmost longitude, southernmost latitude, easternmost longitude, northernmost latitude. [S, W, N, E] */
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
    /** If possible, please provide public comments concatenated into a single pdf */
    public_comments?: string,
    /** Project, which the data collection is part of. For example, West Coast Ocean Acidification (WCOA) Project. */
    research_project?: string,
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
    /** Latitude/longitude bounds of project site (e.g., boundary domain of observations or relevant activities) provided in decimal degrees as westernmost longitude, southernmost latitude, easternmost longitude, northernmost latitude. [S, W, N, E] */
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
    /** Filename(s) of permitting documents included, separated by commas */
    approval_document: string,
}


/**
 * Abstract base class for all experiment types. Contains fields common to both in-situ and model experiments.
 */
export interface Experiment {
    /** Optional common name for experiment. */
    name?: string,
    /** A narrative description of the experiment. For example, what part of the project do these data represent (e.g., baseline, intervention, control) and what do they contribute to the overall project? Are all project research questions listed in Project description relevant? What were the processes to achieve these goals and answer these questions? Data submitters are encouraged to note any significant changes to the original experimental plan due to unforeseen circumstances here. */
    description: string,
    /** Latitude/longitude bounds of observed data in experiment, provided in decimal degrees as westernmost longitude, southernmost latitude, easternmost longitude, northernmost latitude. [S, W, N, E] */
    spatial_coverage: SpatialCoverage,
    /** The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable. */
    project_id: string,
    /** The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:
Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01 */
    experiment_id: string,
    /** The type of mCDR experiment conducted. See Controlled Vocabularies section for definitions. */
    experiment_type: string,
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
 * An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are  specific to an Experiment with type "Intervention"
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
    /** Information such as feedstock source, characteristics, impurities, dilution prior to dosing, and concentration. For feedstock other than NaOH: trace metal composition and particulate grain size. Any variable information must be provided in the dosing data file, in this case include the data file and column header names here provided as variables. See Intervention Data for details. */
    alkalinity_feedstock_description: string,
    /** Whether the feedstock was pre-equilibrated or unequilibrated */
    equilibration: string,
    /** Fixed density or provide link/source to effluent density data if applicable. Please include whether density is directly measured or a derived value. If this is a variable included with your data, please note so here as 'alkalinity dosing effluent density is provided as a variable' and use 'dosing_effluent_density' for your column header name. */
    alkalinity_dosing_effluent_density: DosingConcentration,
}


/**
 * An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are  specific to an Experiment with type "Tracer"
 */
export interface TracerDetails {
    /** The form of tracer upon delivery to the ocean (e.g. gas or dye-release) */
    tracer_form: string,
    /** state the kind of tracer used (e.g. rhodamine, or a specific gas) */
    tracer_details: string,
    /** Fixed concentration or provide link/source to tracer concentration separately in the dosing file. Please include whether concentration is directly measured or a derived value. If this is a variable included with  your data, please note so here as 'tracer concentration provided as a variable' and use 'tracer_concentration' for your column header name. */
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
 * An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are  specific to an Experiment with active dosing (e.g. type "Tracer", "Intervention", or "InterventionWithDosing")
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
 * pH instrument calibration with dye information.
 */
export interface PHCalibration extends Calibration {
    /** Temperature at which calibration was performed. */
    calibration_temperature?: string,
    /** Type of indicator dye and any detailed information about it, e.g., its manufacturer. */
    dye_type_and_manufacturer?: string,
    /** Whether the dye has been purified. */
    dye_purified?: boolean,
    /** Correction method applied if dye was not purified. */
    correction_for_unpurified_dye?: string,
    /** Method used to correct for dye effects. */
    dye_correction_method?: string,
    /** pH values of the calibration standards used. */
    ph_of_standards?: string,
}


/**
 * CO2 gas detector calibration with standard gas information.
 */
export interface CO2Calibration extends Calibration {
    /** Temperature at which calibration was performed. */
    calibration_temperature?: string,
    /** Standard gases used for calibration. */
    standard_gas_info?: StandardGas,
}


/**
 * Standard gas used for CO2 calibration.
 */
export interface StandardGas {
    /** Manufacturer of the standard gas. */
    manufacturer: string,
    /** Concentrations of the CO2 standard gases that are used to calibrate the CO2 sensor, e.g., 260, 350, 510ppm. */
    concentration: string,
    /** Uncertainties of the CO2 standard gas, e.g., 0.5%. */
    uncertainty?: string,
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
    calibration: PHCalibration,
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
    calibration: CO2Calibration,
    /** Resolution of the CO2 sensor. */
    resolution?: string,
    /** Uncertainty of the CO2 sensor. */
    uncertainty?: string,
}


/**
 * Basic variable fields across all (including non-measured) variables
 */
export interface BaseVariable {
    /** Unit of measurement for this variable. */
    units?: string,
    standard_identifier?: VocabularyItemReference,
    /** The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation  [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name). */
    dataset_variable_name: string,
    /** Full descriptive name of the variable. */
    long_name: string,
}


/**
 * Non-measured variable for data from external sources (e.g., satellite, model outputs, published data) that are not directly measured by the project but included in the dataset.
 */
export interface NonMeasuredVariable extends BaseVariable {
}


/**
 * Base class for all variable types. Contains common identification and description fields shared by all variables. Reference: OAPMetadata XSD variables.xsd - variable, basic_variable
 */
export interface Variable extends BaseVariable {
    /** If applicable, the column header name used for the quality control flag corresponding to this variable. */
    dataset_variable_name_qc_flag?: string,
    /** If applicable, the column header name used for the raw data corresponding to this variable. */
    dataset_variable_name_raw?: string,
    /** Citation for the method used. */
    method_reference?: string,
    /** The name of the PI whose research team measured or derived this parameter. */
    measurement_researcher?: Person,
    /** Any additional information about this variable. */
    other_detailed_information?: string,
}


/**
 * Variable that is directly measured in-situ using instruments. Reference: OAPMetadata XSD variables.xsd - basic_measured_observation_base
 */
export interface ObservedPropertyVariable extends Variable, QCFields {
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
    genesis: string,
    sampling_instrument_type: string,
    sampling_instrument_type_custom?: string,
}


/**
 * Analyzing instrument information fields, only applied to discretely measured variables. The instrument type can be narrowed in subclasses using slot_usage.
 */
export interface DiscreteMeasuredVariable extends ObservedPropertyVariable {
}


/**
 * Fields for continuous sampling information.
 */
export interface ContinuousMeasuredVariable extends ObservedPropertyVariable {
    /** The method used to calculate reported values from raw sensor data. */
    raw_data_calculation_method: string,
    /** Version of the software used to calculate reported values from raw values. */
    calculation_software_version?: string,
}


/**
 * Variable that is calculated or derived from other variables.
 */
export interface CalculatedVariable extends Variable, QCFields {
    genesis: string,
    /** Information about how the variable was calculated and the parameters used in calculation, e.g.: Calculation software = CO2SYSv1 (MATLAB)  Input variables =  pH and DIC (column header names 'ph_t_insitu' and 'dic' in associated dataset file) Additional information = the dissociation constants of Lueker et al., 2000 for carbonic acid, etc. */
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
 * HPLC (High-Performance Liquid Chromatography) measured variable for pigment analysis. Always measured, not calculated.
 */
export interface HPLCVariable extends DiscreteMeasuredVariable {
    /** The name of the lab where the HPLC analysis was run (e.g., 'NASA_GSFC' */
    hplc_lab: string,
    /** Name and contact information for HPLC technician. */
    hplc_lab_technician?: string,
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
    /** e.g., sediment core, grab sampling, dredging, etc. */
    sediment_sampling_method: string,
    /** Depth that sediment was collected below sediment surface. If provided as a variable (recommended), please list the column header name here. */
    sediment_sampling_depth: string,
    /** Water depth where sediment was collected. If provided as a variable (recommended), please list the column header name here. */
    sediment_sampling_water_depth: string,
}


/**
 * Fields applied to all measured CO2 variable types (discrete and continuous)
 */
export interface MeasuredCO2Fields {
    /** Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf. */
    appropriate_use_quality?: string,
    /** In Celsius. The input could be a constant temperature value, or something like, in-situ temperature, temperature of analysis, etc. */
    co2_reported_temperature: string,
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
    qc_researcher?: Person,
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
    /** Selected controlled vocabularies for data types relevant to mCDR have been referenced from NASA's SeaBASS metadata system and are provided below, for additional data types of optical characteristics see the [SeaBASS controlled definitions list](https://seabass.gsfc.nasa.gov/wiki/metadataheaders#data_type). Additional data types have been included to meet the needs of mCDR field projects. */
    dataset_type: string,
    /** Custom "data type" when an appropriate value is not found in the controlled vocabulary list for mCDR Data Type and the corresponding `data_type` field is set to "other". */
    dataset_type_custom?: string,
    data_submitter: Person,
    /** Author list in the format of Lastname1, Firstname1 Middlename1; Lastname2, Firstname2 Middlename2; ... */
    author_list_for_citation?: string,
    /** Link a Dataset to its license to document legal constraints by adding a schema:license property. The guide recommends providing a URL that unambiguously identifies a specific version of the license used, but for many licenses it is hard to determine what that URL should be. Thus, we recommend that the license URL be drawn from the [SPDX license list](https://spdx.org/licenses/), which provides a curated list of licenses and their properties that is well maintained. For each SPDX entry, SPDX provides a canonical URL for the license (e.g., http://spdx.org/licenses/CC0-1.0), a unique licenseId (e.g., CC0-1.0), and other metadata about the license. */
    license?: string,
    /** A statement from the data producer regarding how this dataset should be used. */
    fair_use_data_request?: string,
    filenames: string[],
}


/**
 * A field or observational dataset related to an OAE experiment. Contains fields specific to in-situ data collection such as platform information, calibration files, QC flags, and measured variables.
 */
export interface FieldDataset extends Dataset {
    /** Start date and end date (if known) of the project in ISO-8601 interval format (YYYY-MM-DD/YYY-MM-DD). If the end date is not known, use open-ended format YYYY-MM-DD/.. */
    temporal_coverage: string,
    /** "Controlled vocabulary" One of the three choices: (a) Originally collected dataset (e.g., a dataset collected from a research cruise or laboratory experiment), (b) Data compilation product (e.g., SOCAT, GLODAP), or (c) Derived product (e.g., gridded products, or model output). */
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
    variables?: Variable[],
}


/**
 * A model simulation output dataset. Contains fields specific to computational model output including simulation configuration, output variables, and hardware information.
 */
export interface ModelOutputDataset extends Dataset {
    /** Whether this is a counterfactual (control/baseline) or perturbation simulation. */
    simulation_type: string,
    /** Description of the model spin-up process. */
    spin_up_protocol?: string,
    /** Start date and time of the simulation in UTC ISO-8601. */
    start_datetime: string,
    /** End date and time of the simulation in UTC ISO-8601. */
    end_datetime: string,
    /** Frequency of model output (e.g., 'hourly mean', 'daily mean'). */
    output_frequency?: string,
    /** Time-stepping method and time step used in the simulation. */
    time_stepping_scheme?: string,
    /** Description of the alkalinity perturbation applied in the simulation. Required when simulation_type is "perturbation". */
    alkalinity_perturbation_description?: string,
    /** Details about the computational hardware used for the simulation. */
    hardware_configuration?: HardwareConfiguration,
    /** Checklist of variables included in the model simulation output. */
    model_output_variables?: string,
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
    /** Controlled vocabularies for the types of the platform: https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/vocabularies/platform-types.html */
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
    /** Details about input data sources used to drive the model. */
    input_details?: ModelInputDetails,
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
    /** Bounding box for this grid, provided as westernmost longitude, southernmost latitude, easternmost longitude, northernmost latitude. */
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


