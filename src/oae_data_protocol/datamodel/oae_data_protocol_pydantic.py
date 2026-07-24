from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "0.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'oae',
     'id': 'https://schema.oaedata.org/OAEDataSchema',
     'imports': ['linkml:types',
                 'core',
                 'enums',
                 'dynamic_enums_expanded',
                 'oae_project',
                 'external_project',
                 'monetary_grant',
                 'permit',
                 'experiment',
                 'person',
                 'variable',
                 'dataset',
                 'platform',
                 'model'],
     'name': 'OAEDataSchema',
     'prefixes': {'PUBCHEM': {'prefix_prefix': 'PUBCHEM',
                              'prefix_reference': 'https://pubchem.ncbi.nlm.nih.gov/compound/'},
                  'SDN_B75': {'prefix_prefix': 'SDN_B75',
                              'prefix_reference': 'http://vocab.nerc.ac.uk/collection/B75/current/'},
                  'SDN_L05': {'prefix_prefix': 'SDN_L05',
                              'prefix_reference': 'http://vocab.nerc.ac.uk/collection/L05/current/'},
                  'SDN_L22': {'prefix_prefix': 'SDN_L22',
                              'prefix_reference': 'http://vocab.nerc.ac.uk/collection/L22/current/'},
                  'dcat': {'prefix_prefix': 'dcat',
                           'prefix_reference': 'http://www.w3.org/ns/dcat#'},
                  'envthes': {'prefix_prefix': 'envthes',
                              'prefix_reference': 'https://w3id.org/envthes/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'oae': {'prefix_prefix': 'oae',
                          'prefix_reference': 'https://schema.oaedata.org/'},
                  'unit': {'prefix_prefix': 'unit',
                           'prefix_reference': 'https://qudt.org/vocab/unit/'}},
     'source_file': 'src/oae_data_protocol/schema/oae_data_protocol.yaml',
     'title': 'OAE Data Protocol - Technical Documentation'} )

class DatasetType(str, Enum):
    """
    Type of dataset being submitted. This usually 
    """
    # Variables such as dosing_onoff, dosing_rate, and flow_rate should be included here.
    dosing = "dosing"
    # Vertical profiles (e.g., optical packages, CTD)
    cast = "cast"
    # Any other types of measurements from water samples collected at discrete depths (e.g., nutrients)
    bottle = "bottle"
    # Continuous data (e.g., shipboard, underway flow through system)
    flow_thru = "flow_thru"
    # For laboratory measured pigment data (e.g. fluorometry, spectrophotometry, HPLC)
    pigment = "pigment"
    # For various types of marine snow catcher data
    marine_snow_catcher = "marine_snow_catcher"
    # Moored and buoy data
    mooring = "mooring"
    # Drifter and drogue data
    drifter = "drifter"
    # Measurements made via an aircraft
    airborne = "airborne"
    # For measurements made by a diver
    diver = "diver"
    # Measurements made by an autonomous underwater vehicle
    auv = "auv"
    # Measurements made by an autonomous surface vehicle
    asv = "asv"
    # Measurements that have a non-geospatial aspect (e.g., incubations or other laboratory measurements, etc.)
    experimental = "experimental"
    # Measurements from a sediment trap platform
    sediment_trap = "sediment_trap"
    # Data whose purpose is the classification or annotation of phytoplankton, zooplankton, or other marine groups.
    taxonomy = "taxonomy"
    # Measurements from sediment samples (e.g., core samples, grab samples)
    sediment = "sediment"
    # Data output from model experiments
    model_output = "model_output"
    # Information (quantitative or qualitative) from socioeconomic studies
    socioeconomic = "socioeconomic"
    # For measurements captured via net (e.g., zooplankton via MOCNESS)
    net_tow = "net_tow"
    # Data collected continuously from a moving platform (e.g., ship underway system sampling surface seawater during transit).
    underway = "underway"
    # For data types not included in the controlled vocabulary. Please fill in a the `dataset_type_custom` field with a more specific name for the custom mCDR data type.
    other = "other"


class MCDRPathway(str, Enum):
    """
    Type of marine Carbon Dioxide Removal (mCDR) pathways.
    """
    # Ocean Alkalinity Enhancement (OAE) is a method to help mitigate climate change by increasing the alkalinity of seawater to enhance its capacity to absorb and store atmospheric carbon dioxide (CO₂).
    Ocean_Alkalinity_Enhancement = "ocean_alkalinity_enhancement"
    # Biomass Sinking is a method that involves taking terrestrial or ocean biomass and sinking it into the deep ocean surface, subsurface, or anoxic basins, where it is sequestered. This can be accomplished by large-scale seaweed farming or macroalgae cultivation, which incorporates atmospheric CO2 as it grows, and then is sunk to the ocean floor. Alternatively, terrestrial plant biomass can be sunk to the ocean floor.
    Biomass_Sinking = "biomass_sinking"
    # Direct Ocean Capture (DOC) is a method that uses electrochemical processes to remove dissolved carbon dioxide (CO₂) directly from seawater for carbon storage or reuse.
    Direct_Ocean_Capture = "direct_ocean_capture"
    # Ocean Fertilization is a method that involves adding nutrients, such as iron, nitrogen, or phosphorus, to the ocean to stimulate the growth of phytoplankton or other microscopic plants that absorb carbon dioxide (CO₂) through photosynthesis.
    Ocean_Nutrient_Fertilization = "ocean_nutrient_fertilization"
    # Artificial Upwelling and Downwelling are mCDR methods that involve manipulating ocean water movement to enhance natural carbon sequestration processes.
    Artificial_Upwelling_and_Downwelling = "artificial_upwelling_downwelling"
    # Marine Ecosystem Recovery refers to the restoration and protection of marine ecosystems to enhance their natural ability to capture and store carbon dioxide (CO₂). This method leverages the natural carbon-sequestering processes of marine habitats such as salt marshes, mangrove forests, coral reefs, kelp forests, seagrass meadows, oyster beds, and deep-sea ecosystems, aiming to rebuild biodiversity, ecosystem functions, and carbon storage capacity.
    Marine_Ecosystem_Recovery = "marine_ecosystem_recovery"


class ExperimentType(str, Enum):
    """
    Types of mCDR experiments
    """
    # Baseline measurements taken before any intervention
    baseline = "baseline"
    # Control experiment without intervention for comparison
    control = "control"
    # Experiment with active OAE intervention
    intervention = "intervention"
    # Tracer study experiment (eg- dye or gas tracer study)
    tracer_study = "tracer_study"
    # Model-based experiment or simulation
    model = "model"
    # Other experiment type not covered by standard categories
    other = "other"


class AlkalinityFeedstockProcessing(str, Enum):
    """
    Methods used to process alkalinity feedstock
    """
    # Alkalinity generated via electrochemical processes (e.g., seawater electrolysis).
    electrochemistry = "electrochemistry"
    # Intentionally industrially manufactured chemical compounds (e.g., Ca(OH)2 via lime kilns).
    synthetically_derived = "synthetically_derived"
    # Mined geological material, including purified mineral or natural rock.
    mineral_mining = "mineral_mining"
    # A mix of multiple sources.
    blended = "blended"
    # Unclassified or novel; include a description in Experiment Description.
    other = "other"


class AlkalinityFeedstockForm(str, Enum):
    """
    Physical form of the alkalinity feedstock upon ocean delivery
    """
    # Involves adding alkaline minerals or particulate slurry (such as MgOH2, MgO, or CaO) to seawater or river systems either directly, through coastal outfalls (such as wastewater), or at breaking shorelines to increase its alkalinity.
    solid = "solid"
    # Aqueous alkalinity addition may use electrochemistry or fully dissolved mineral feedstock to increase seawater alkalinity.
    aqueous = "aqueous"
    # Slurry alkalinity additions include a mix of solid and aqueous alkalinity forms, where the solid alkaline particulates are suspended in a solution.
    slurry = "slurry"


class EquilibrationStatus(str, Enum):
    """
    Equilibration status of the alkalinity feedstock
    """
    # Pre-equilibrated with atmosphere before dosing
    Pre_equilibrated = "pre_equilibrated"
    # Not pre-equilibrated before dosing
    unequilibrated = "unequilibrated"


class HydrologicLocation(str, Enum):
    """
    Hydrologic location types for dosing
    """
    # Surface waters in coastal areas
    Coastal_Surface = "coastal_surface"
    # Surface waters in offshore areas
    Offshore_Surface = "offshore_surface"
    # River systems
    river = "river"
    # Wetland areas
    wetland = "wetland"
    # Seafloor or benthic zone
    seafloor = "seafloor"


class DosingDeliveryType(str, Enum):
    """
    Types of dosing delivery methods
    """
    # A single dosing location such as an outflow from a static platform with a pipe
    Static_Point_Source = "static_point_source"
    # A mobile dosing regimen described by a single location at each time step, such as an outflow from a mobile platform such as a ship or surface vessel.
    Variable_Point_Source = "variable_point_source"
    # A set location or locations of dosing that is not a point source, such as a distributed area over the seafloor or a diffusor.
    Static_Distributed = "static_distributed"
    # A distributed dosing area that varies in time, such as manually placed alkaline material over different areas at different times.
    Variable_Distributed = "variable_distributed"


class TracerForm(str, Enum):
    """
    Forms of tracer used in tracer studies
    """
    # Gas tracer
    gas = "gas"
    # Dye tracer (eg- rhodamine)
    dye = "dye"
    # Other tracer form not covered by standard categories
    other = "other"


class FeedstockType(str, Enum):
    """
    Types of materials used for alkalinity addition, as sourced from NCEI's OCADS controlled vocabulary: https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/vocabularies/alkalinization-types.html
    """
    # Lime (CaO) used as an alkalinity source.
    lime = "lime"
    # Portlandite (Ca(OH)₂) used as an alkalinity source.
    portlandite = "portlandite"
    # Calcium carbonate (CaCO₃) used as an alkalinity source.
    calcium_carbonate = "calcium_carbonate"
    # Anorthite (CaAl₂Si₂O₈) used as an alkalinity source.
    anorthite = "anorthite"
    # Dolomite (CaMg(CO₃)₂) used as an alkalinity source.
    dolomite = "dolomite"
    # Periclase (MgO) used as an alkalinity source.
    periclase = "periclase"
    # Brucite (Mg(OH)₂) used as an alkalinity source.
    brucite = "brucite"
    # Magnesite (MgCO₃) used as an alkalinity source.
    magnesite = "magnesite"
    # Forsterite (Mg₂SiO₄) used as an alkalinity source.
    forsterite = "forsterite"
    # Magnesium-rich olivine used as an alkalinity source.
    mg_rich_olivine = "mg_rich_olivine"
    # NaOH used as an alkalinity source.
    sodium_hydroxide = "sodium_hydroxide"
    # Natrite (Na₂CO₃) used as an alkalinity source.
    natrite = "natrite"
    # Nahcolite (NaHCO₃) used as an alkalinity source.
    nahcolite = "nahcolite"
    # Enter a custom value in the field provided
    other = "other"


class GridType(str, Enum):
    """
    Type of grid in a multi-grid or nested model configuration
    """
    # Inner (nested, higher-resolution) grid
    inner_grid = "inner_grid"
    # Outer (coarser-resolution) grid
    outer_grid = "outer_grid"
    # Single grid (no nesting)
    single_grid = "single_grid"


class ModelComponentType(str, Enum):
    """
    Type of model component
    """
    # Physical model component (e.g., ocean circulation)
    Physics = "physics"
    # Biogeochemical or ecosystem model component
    BGC_SOLIDUS_Ecosystem = "bgc_ecosystem"
    # Sea Ice model component
    Sea_Ice = "sea_ice"
    # Atmosphere model component
    Atmosphere = "atmosphere"
    # Other model component (e.g., sea ice, sediment, atmosphere)
    other = "other"


class DataProductType(str, Enum):
    # A dataset collected from a research cruise or laboratory experiment
    originally_collected_dataset = "originally_collected_dataset"
    # (e.g., SOCAT, GLODAP)
    data_compilation_product = "data_compilation_product"
    # (e.g. gridded products, or model output).
    derived_product = "derived_product"


class SimulationType(str, Enum):
    """
    Type of model simulation dataset
    """
    # Control/baseline simulation without alkalinity perturbation
    counterfactual = "counterfactual"
    # Simulation with alkalinity perturbation applied
    perturbation = "perturbation"
    # Other simulation type not listed above
    other = "other"


class ModelOutputVariable(str, Enum):
    """
    Variables commonly included in model simulation output datasets
    """
    # Air-sea exchange of carbon dioxide
    Air_sea_CO2_flux = "air_sea_co2_flux"
    # Dissolved inorganic carbon (DIC)
    Dissolved_Inorganic_Carbon = "dissolved_inorganic_carbon"
    # Total alkalinity (TA)
    Total_Alkalinity = "total_alkalinity"
    # Temperature
    temperature = "temperature"
    # Salinity
    salinity = "salinity"
    # pH of seawater
    pH = "ph"
    # Phytoplankton biomass or concentration
    phytoplankton = "phytoplankton"
    # Horizontal velocity components (u, v)
    Horizontal_velocity = "horizontal_velocity"
    # Vertical velocity component (w)
    Vertical_velocity = "vertical_velocity"


class DataAccessibility(str, Enum):
    """
    Level of access to a dataset.
    """
    # Data are freely available without restriction.
    Open_Access = "open_access"
    # Data are available upon request, subject to review.
    Conditional_Access = "conditional_access"
    # Data will become openly available after a specified date.
    Scheduled_Access = "scheduled_access"


class SeaNames(str, Enum):
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSZZSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/ZZ/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSIJMSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/IJM/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSMKMSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/MKM/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSIRMSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/IRM/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS10SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/10/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS62aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/62a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS04SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/04/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS01cSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/01c/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS25SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/25/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSSOCSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/SOC/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS33SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/33/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS16aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/16a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28AbSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Ab/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48oSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48o/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSESCSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/ESC/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS39SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/39/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS57bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/57b/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSICSSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/ICS/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS53SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/53/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS35SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/35/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS200SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/200/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS61bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/61b/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS22SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/22/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28BfSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Bf/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS11SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/11/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS63SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/63/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS03SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/03/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS12SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/12/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28BSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28B/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48eSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48e/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS47SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/47/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28AaSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Aa/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS45SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/45/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSWSCSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/WSC/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS62SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/62/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS40SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/40/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS23bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/23b/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS06SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/06/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS42SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/42/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS51SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/51/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS45aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/45a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS32bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/32b/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS21SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/21/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28CSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28C/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48mSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48m/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS01bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/01b/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS26SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/26/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS13SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/13/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28ASOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28A/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS32SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/32/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48jSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48j/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48hSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48h/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS31SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/31/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS57aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/57a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS05SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/05/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS50SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/50/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSARASOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/ARA/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS61aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/61a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS21aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/21a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28BgSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Bg/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48nSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48n/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS01aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/01a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS27SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/27/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS14SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/14/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS60SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/60/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48fSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48f/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS49SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/49/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48lSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48l/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48iSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48i/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS41SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/41/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS30SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/30/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS23aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/23a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS08SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/08/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS32aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/32a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS20SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/20/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS17aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/17a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28AeSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Ae/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS17SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/17/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS59SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/59/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS64SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/64/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48kSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48k/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48b/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS01SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/01/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS44SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/44/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS55SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/55/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS38SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/38/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS29SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/29/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS07SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/07/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS56SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/56/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS19SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/19/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS15aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/15a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS46bSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/46b/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS14aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/14a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28AdSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Ad/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS61SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/61/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS58SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/58/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS65SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/65/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48gSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48g/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48dSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48d/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS23SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/23/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS43SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/43/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS54SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/54/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS37SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/37/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSCASSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/CAS/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS09SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/09/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS18SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/18/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS02SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/02/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS24SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/24/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS46SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/46/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS46aSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/46a/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS16SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/16/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28AcSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Ac/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS57SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/57/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS66SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/66/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSWASSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/WAS/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS48cSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/48c/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSFRMSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/FRM/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS500SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/500/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS15SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/15/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS52SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/52/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS36SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/36/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUSGLOSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/GLO/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS34SOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/34/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSC16SOLIDUScurrentSOLIDUS28BhSOLIDUS = "http://vocab.nerc.ac.uk/collection/C16/current/28Bh/"


class PlatformType(str, Enum):
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS99SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/99/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS6DSOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/6D/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS3CSOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/3C/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS36SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/36/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS18SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/18/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS30SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/30/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS61SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/61/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS26SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/26/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS16SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/16/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS3ASOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/3A/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS41SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/41/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS72SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/72/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS43SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/43/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS15SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/15/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS13SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/13/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS6ASOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/6A/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS44SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/44/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS68SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/68/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS33SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/33/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS19SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/19/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS11SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/11/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS12SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/12/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS23SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/23/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS17SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/17/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS3BSOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/3B/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS45SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/45/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS42SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/42/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS47SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/47/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS14SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/14/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS71SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/71/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS46SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/46/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS20SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/20/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS27SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/27/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS25SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/25/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS3ZSOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/3Z/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS48SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/48/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS31SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/31/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS62SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/62/"
    httpCOLONSOLIDUSSOLIDUSvocabFULL_STOPnercFULL_STOPacFULL_STOPukSOLIDUScollectionSOLIDUSL06SOLIDUScurrentSOLIDUS67SOLIDUS = "http://vocab.nerc.ac.uk/collection/L06/current/67/"


class MassConcentrationUnit(str, Enum):
    unitCOLONKiloGM_PER_M3 = "unit:KiloGM-PER-M3"
    unitCOLONMicroGM_PER_L = "unit:MicroGM-PER-L"
    unitCOLONMicroGM_PER_L_DAY = "unit:MicroGM-PER-L-DAY"
    unitCOLONMicroGM_PER_MilliL = "unit:MicroGM-PER-MilliL"
    unitCOLONMilliGM_PER_L = "unit:MilliGM-PER-L"
    unitCOLONMilliGM_PER_M3 = "unit:MilliGM-PER-M3"
    unitCOLONMilliGM_PER_MilliL = "unit:MilliGM-PER-MilliL"
    unitCOLONNanoGM_PER_L = "unit:NanoGM-PER-L"
    unitCOLONNanoGM_PER_MilliL = "unit:NanoGM-PER-MilliL"
    unitCOLONPicoGM_PER_MilliL = "unit:PicoGM-PER-MilliL"


class ResearcherIDType(str, Enum):
    orcid = "orcid"
    researcher_id = "researcher_id"
    ocean_expert = "ocean_expert"


class CalibrationLocation(str, Enum):
    """
    Where the calibration was performed.
    """
    # Factory calibration performed by manufacturer.
    factory = "factory"
    # Laboratory calibration.
    lab = "lab"
    # Field calibration performed during deployment.
    field = "field"


class SamplingInstrumentType(str, Enum):
    # A CTD rosette consists of a metal frame that houses a collection of sensors and water sampling bottles (e.g., Niskin)
    ctd_rosette = "ctd_rosette"
    # A device that collects an in-situ discrete water sample from any depth and returns it to the surface without contamination by the waters through which it passes, such as a water bottle.
    niskin_bottle = "niskin_bottle"
    # A device that continuously supplies a flow of water either to an analytical instrument, over a sensor or from which samples may be drawn.
    flow_through_system = "flow_through_system"
    # Such flasks are typically made of glass and have a capacity of around one liter. Seawater samples are collected from a specific depth using a Niskin bottle or other sampling device and transferred to the flask without exposing them to the air. The flask is then sealed with a stopper and transported to the laboratory for analysis.
    flask_for_discrete_co2_measurement = "flask_for_discrete_co2_measurement"
    # A net towed through the water column designed to sample free-swimming nekton or fish
    biological_trawl = "biological_trawl"
    # Phytoplankton net is used to collect and identify phytoplankton, which are microscopic plants that form the base of the marine food web.
    phytoplankton_net = "phytoplankton_net"
    # Zooplankton net is used to collect and identify zooplankton, which are microscopic animals that feed on phytoplankton and are important prey for many marine organisms.
    zooplankton_net = "zooplankton_net"
    # Environmental DNA (eDNA) samplers: used to collect and analyze genetic material shed by marine organisms, which can provide information about their distribution, abundance, and diversity.
    edna_sampler = "edna_sampler"
    # A device used in the measurement of a variety of oceanographic variables that functions autonomously
    autonomous_sensor = "autonomous_sensor"
    other = "other"


class AnalyzingInstrumentType(str, Enum):
    # A reusable instrument that always simultaneously measures conductivity and temperature (for salinity) and pressure (for depth).
    ctd_sensor = "ctd_sensor"
    # A device that continuously supplies a flow of water either to an analytical instrument, over a sensor or from which samples may be drawn.
    flow_through_system = "flow_through_system"
    # Temperature and conductivity sensors mounted on a sea-surface platform continuously measuring a surface water supply.
    thermosalinograph = "thermosalinograph"
    # Instruments that measure the salinity of a collected water sample based on its electrical conductivity or optical properties.
    salinometer_for_discrete_salinity_measurement = "salinometer_for_discrete_salinity_measurement"
    # DIC coulometers are widely used in oceanographic research to measure the concentration of dissolved inorganic carbon in seawater samples. They are often coupled with computer-controlled automated dynamic headspace analyzers that extracts total carbon dioxide from seawater using Single-Operator Multiparameter Metabolic Analyzers (SOMMAs).
    dic_analyzers_based_on_coulometers = "dic_analyzers_based_on_coulometers"
    # DIC analyzers based on a CO2 gas detector including Non-dispersive infrared absorption (NDIR) (e.g., Licor LI-850), Cavity Enhanced Absorption Spectroscopy (e.g., Licor's LI-7815), and Cavity Ring-Down Spectroscopy (CRDS) (e.g., Picarro G2131i) detectors.
    dic_analyzers_based_on_co2_gas_detectors = "dic_analyzers_based_on_co2_gas_detectors"
    # Autonomous dissolved inorganic carbon (DIC) sensors are devices that can measure the concentration of DIC in seawater or other natural waters in situ, without the need for manual sampling and laboratory analysis.
    autonomous_dic_sensor = "autonomous_dic_sensor"
    # An alkalinity titrator is a device used to measure the total alkalinity of a seawater by titration.
    alkalinity_titrator = "alkalinity_titrator"
    # Autonomous total alkalinity (TA) sensors are devices that can measure the concentration of TA in seawater or other natural waters in situ, without the need for manual sampling and laboratory analysis.
    autonomous_ta_sensor = "autonomous_ta_sensor"
    # This type of equilibrator works by spraying seawater into a gas chamber, allowing the CO2 in the water to equilibrate with a gas mixture in the chamber.
    showerhead_equilibrator = "showerhead_equilibrator"
    # An "h"-shaped bubble equilibrator assembly commonly used in MAPCO2 systems on moorings. For more information, refer to Friederich et al. (1995).
    floating_air_water_equilibrator = "floating_air_water_equilibrator"
    # While seawater is passed through a membrane, CO2 in the water diffuses across the membrane and equilibrates with the gas mixture, which is then analyzed to determine the CO2 concentration.
    membrane_equilibrator = "membrane_equilibrator"
    # Instruments measuring the relative absorption of electromagnetic radiation of different wavelengths in the near infra-red, visible and ultraviolet wavebands by samples.
    spectrophotometer = "spectrophotometer"
    # One example of a handheld pH spectrophotometer is the "pHyter". Refer to Pardis et al. (2022) for more details.
    handheld_ph_spectrophotometer = "handheld_ph_spectrophotometer"
    # A pH electrode, sometimes referred to as a pH probe or pH sensor, is a glass device used to measure the pH of a solution.
    ph_electrode = "ph_electrode"
    # A pH sensor. The sensor can be used for ocean acidification, research coral reef sensitivity analysis and environmental monitoring. The sensor measures pH with a range of 6.5 to 9.0. The sensing element is an ion sensitive field effect transistor. The pH sensor has an initial accuracy of +/-0.05 pH, precision of 0.001 pH and stability of 0.005 pH/month. It can operate in temperatures ranging from 0 deg C to 50 deg C and up to depths of 50 m.
    sea_bird_seafet_v1 = "sea_bird_seafet_v1"
    # A pH sensor. The sensor can be used for ocean acidification, research coral reef sensitivity analysis and environmental monitoring. The sensor measures pH with a range of 6.5 to 9.0. The sensing element is an ion sensitive field effect transistor. V2 implements improvements to the original SeaFET's reliability, data quality, ease of operation, and deployment endurance, with significant changes to how users interface with the instrument. The pH sensor has an accuracy to +/-0.05 pH, precision of 0.004 pH and stability of 0.003 pH/month. It can operate in temperatures ranging from 0 deg C to 50 deg C and up to depths of 50 m.
    sea_bird_seafet_v2 = "sea_bird_seafet_v2"
    # An oxygen titrator is a device used to measure the concentration of dissolved oxygen in a water sample, as required for the Winkler method.
    oxygen_titrator = "oxygen_titrator"
    # An oxygen sensor or probe or sond, is an electronic device that measures the concentration of dissolved oxygen in the ocean.
    oxygen_sensor = "oxygen_sensor"
    # Sea-Bird SeapHOx is a type of oceanographic instrument that measures both the pH and dissolved oxygen concentration of seawater in real-time.
    sea_bird_seaphox = "sea_bird_seaphox"
    # YSI (Yellow Springs Instruments) is a company that produces a variety of water quality monitoring instruments. The YSI sensors are designed to measure a wide range of parameters, including temperature, salinity, and dissolved oxygen.
    ysi = "ysi"
    # Instrument that makes in-situ measurements of one or more of nitrate, nitrite, ammonium, urea, phosphate or silicate dissolved in the water column.
    nutrient_analyzer = "nutrient_analyzer"
    # Instrument that measures the amount of stimulated electromagnetic radiation produced by pulses of electromagnetic radiation emitted into the water column.
    fluorometers = "fluorometers"
    # Instruments that separate and analyse mixtures of substances by high pressure pumping the sample through a column packed with microspheres coated with the stationary phase.
    high_performance_liquid_chromatography = "high_performance_liquid_chromatography"
    # Acoustic Doppler Current Profiler (ADCP), is a type of instrument used to measure water currents in oceans, rivers, and other bodies of water.
    acoustic_doppler_current_profiler = "acoustic_doppler_current_profiler"
    # Instruments used to measure the mass-to-charge ratio of ions most generally used to find the composition of a sample by generating a mass spectrum representing the masses of sample components.
    mass_spectrometers = "mass_spectrometers"
    # Instruments that measure isotopic ratios using an electron ionisation source. Atoms in purified samples are ionised using a beam of electrons under vacuum. Subsequently, ions are focused into a beam by an electromagnet and then separated into individual beams based on their mass/charge ratio
    isotope_ratio_mass_spectrometers = "isotope_ratio_mass_spectrometers"
    # Instrument that makes routine meteorological measurements on the atmosphere, typically air pressure, temperature and humidity
    barometric_pressure_sensor = "barometric_pressure_sensor"
    # Instruments that generate enlarged images of samples using the phenomena of reflection and absorption of visible light. Includes conventional and inverted instruments
    microscopes = "microscopes"
    # A scanning electron microscope (SEM) is a type of microscope that uses a focused beam of electrons to create high-resolution images of the surface of a specimen.
    scanning_electron_microscopes = "scanning_electron_microscopes"
    # Instruments that suspend cells in a stream of fluid past detection sensors whilst illuminating them with laser light. Used for cell counting, sorting, biomarker detection and protein engineering.
    flow_cytometers = "flow_cytometers"
    # Environmental DNA (eDNA) samplers: used to collect and analyze genetic material shed by marine organisms, which can provide information about their distribution, abundance, and diversity.
    edna_sampler = "edna_sampler"
    # TBD
    gas_analyzer = "gas_analyzer"
    other = "other"


class SamplingType(str, Enum):
    discrete = "discrete"
    continuous = "continuous"


class VariableType(str, Enum):
    """
    High-level classification of the variable. Determines which schema class to use in combination with genesis (measured/calculated) and sampling (discrete/continuous).
    """
    # pH measurement — use with Discrete/ContinuousPHVariable or CalculatedVariable
    pH = "pH"
    # Total alkalinity — use with Discrete/ContinuousTAVariable or CalculatedVariable
    ta = "ta"
    # Dissolved inorganic carbon — use with Discrete/ContinuousDICVariable or CalculatedVariable
    dic = "dic"
    # CO₂ variables (xCO₂, pCO₂, fCO₂) — use with DiscreteCO2Variable or CalculatedVariable
    co2 = "co2"
    # Sediment variable — use with Discrete/ContinuousSedimentVariable or CalculatedVariable
    sediment = "sediment"
    # HPLC pigment analysis — use with HPLCVariable (always discrete, always measured)
    hplc = "hplc"
    # Physiological response variable — organism response data from field experiments. Use with Discrete/ContinuousPhysiologicalVariable or CalculatedVariable.
    physiological = "physiological"
    # Socioeconomic variable — social and economic data. Use only with SocioeconomicVariable. Does not include QC fields.
    socioeconomic = "socioeconomic"
    # Any directly measured or calculated variable that does not fall into a specific category above (e.g., temperature, salinity, conductivity, pressure, fluorescence). Use with DiscreteMeasuredVariable, ContinuousMeasuredVariable, or CalculatedVariable.
    other = "other"
    # Contextual or ancillary columns that are not directly measured or calculated by the project — identifiers, timestamps, coordinates and external source data. QC flag columns should NOT be listed as separate variables; instead set dataset_variable_name_qc_flag on the parent variable. Use only with NonMeasuredVariable.
    non_measured = "non_measured"


class GenesisType(str, Enum):
    measured = "measured"
    calculated = "calculated"


class ObservationType(str, Enum):
    profile = "profile"
    surface_underway = "surface_underway"
    time_series = "time_series"
    laboratory_experiments = "laboratory_experiments"
    mesocosm = "mesocosm"
    field_experiments = "field_experiments"
    natural_analogues = "natural_analogues"
    model_outputs = "model_outputs"


class AppropriateUseQuality(str, Enum):
    weather_quality = "weather_quality"
    climate_quality = "climate_quality"
    other = "other"


class TitrationCellType(str, Enum):
    open = "open"
    closed = "closed"


class ConcentrationBasis(str, Enum):
    """
    Whether concentration measurements are expressed per unit volume or per unit mass.
    """
    # Concentration expressed per unit volume (e.g., μmol/L, mmol/L)
    per_volume = "per_volume"
    # Concentration expressed per unit mass (e.g., μmol/kg-seawater)
    per_mass = "per_mass"


class TaxonomicCodeSystem(str, Enum):
    """
    Taxonomic code system used for species identification.
    """
    # Integrated Taxonomic Information System
    itis = "itis"
    # World Register of Marine Species
    worms = "worms"
    # Catalogue of Life
    col = "col"
    # Paleobiology Database
    pbdb = "pbdb"


class LifeStage(str, Enum):
    """
    Life stage of the biological subject.
    """
    egg = "egg"
    embryo = "embryo"
    larva = "larva"
    juvenile = "juvenile"
    adult = "adult"
    other = "other"


class QuantitativeQualitative(str, Enum):
    """
    Whether the socioeconomic data is quantitative or qualitative.
    """
    quantitative = "quantitative"
    qualitative = "qualitative"


class SocialStudyType(str, Enum):
    """
    Type of social study conducted.
    """
    # Public perception survey
    public_perception_survey = "public_perception_survey"
    # Ecosystem service valuation survey
    ecosystem_service_valuation_survey = "ecosystem_service_valuation_survey"
    # Text analysis
    text_analysis = "text_analysis"
    # Other study type
    other = "other"



class PropertyValue(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:PropertyValue', 'from_schema': 'Core'})

    pass


class Place(ConfiguredBaseModel):
    """
    A geospatial area of interest, defined by a bounding box, polygon/line, or a point designated as a pair of geo-coordinates.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Place', 'from_schema': 'Core'})

    geo: Optional[Union[GeoCoordinates, GeoShape]] = Field(default=None, description="""Entities that have a somewhat fixed, physical extension. (imported from schema.org)""", json_schema_extra = { "linkml_meta": {'alias': 'geo',
         'any_of': [{'range': 'GeoShape'}, {'range': 'GeoCoordinates'}],
         'domain_of': ['Place']} })


class SpatialCoverage(Place):
    """
    A bounding box defined by latitude and longitude coordinates.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Core',
         'slot_usage': {'geo': {'name': 'geo', 'range': 'GeoShape', 'required': True}}})

    geo: Union[GeoCoordinates, GeoShape] = Field(default=..., description="""Entities that have a somewhat fixed, physical extension. (imported from schema.org)""", json_schema_extra = { "linkml_meta": {'alias': 'geo',
         'any_of': [{'range': 'GeoShape'}, {'range': 'GeoCoordinates'}],
         'domain_of': ['Place']} })


class DosingLocation(Place):
    """
    A specific location of dosing for an OAE intervention and/or tracer study. Can be a point, line, or bounding box
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Core'})

    dosing_location_file: Optional[str] = Field(default=None, description="""Exact path and filename for the location file (relative to root path of project), attached separately. Format should be one of GeoJSON or Shapefile.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_location_file', 'domain_of': ['DosingLocation']} })
    geo: Optional[Union[GeoCoordinates, GeoShape]] = Field(default=None, description="""Entities that have a somewhat fixed, physical extension. (imported from schema.org)""", json_schema_extra = { "linkml_meta": {'alias': 'geo',
         'any_of': [{'range': 'GeoShape'}, {'range': 'GeoCoordinates'}],
         'domain_of': ['Place']} })


class GeoShape(ConfiguredBaseModel):
    """
    The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points. (imported from schema.org)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:GeoShape', 'from_schema': 'Core'})

    box: Optional[str] = Field(default=None, description="""A bounding box defined by two corner points — the southwest (lower-left) corner followed by the northeast (upper-right) corner. Per science-on-schema.org, each point is written as `<latitude> <longitude>` in decimal degrees (WGS 84), with all four values space-separated: `\"<minLat> <minLon> <maxLat> <maxLon>\"`. Example: `\"39.3280 120.1633 40.445 123.7878\"`. See https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md#spatial-coverage""", json_schema_extra = { "linkml_meta": {'alias': 'box', 'domain_of': ['GeoShape'], 'slot_uri': 'schema:box'} })
    line: Optional[str] = Field(default=None, description="""A line is a point-to-point path consisting of two or more points. A line is expressed as a series of two or more point objects separated by space.""", json_schema_extra = { "linkml_meta": {'alias': 'line', 'domain_of': ['GeoShape'], 'slot_uri': 'schema:line'} })


class GeoCoordinates(ConfiguredBaseModel):
    """
    A geographic coordinate in decimal degrees.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:GeoCoordinates', 'from_schema': 'Core'})

    latitude: float = Field(default=..., title="Latitude", description="""Latitude in decimal degrees of a location. For example 37.42242 (WGS 84).""", json_schema_extra = { "linkml_meta": {'alias': 'latitude',
         'domain_of': ['GeoCoordinates'],
         'slot_uri': 'schema:latitude'} })
    longitude: float = Field(default=..., title="Longitude", description="""Longitude in decimal degrees of a location. For example -122.08585 (WGS 84).""", json_schema_extra = { "linkml_meta": {'alias': 'longitude',
         'domain_of': ['GeoCoordinates'],
         'slot_uri': 'schema:longitude'} })


class VerticalExtent(ConfiguredBaseModel):
    """
    The vertical extent of a place or structure in meters.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Core'})

    min_depth_in_m: Optional[float] = Field(default=None, title="Minimum Depth (in meters)", description="""Minimum depth of observation in meters. Use negative numbers for depths below sea level.""", le=0, json_schema_extra = { "linkml_meta": {'alias': 'min_depth_in_m', 'domain_of': ['VerticalExtent']} })
    max_depth_in_m: Optional[float] = Field(default=None, title="Maximum Depth (in meters)", description="""Maximum depth of observation in meters. Use negative numbers for depths below sea level.""", le=0, json_schema_extra = { "linkml_meta": {'alias': 'max_depth_in_m', 'domain_of': ['VerticalExtent']} })
    min_height_in_m: Optional[float] = Field(default=None, title="Minimum Height (in meters)", description="""Minimum height of observation (in meters) for above ground aerial coverage.""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'min_height_in_m', 'domain_of': ['VerticalExtent']} })
    max_height_in_m: Optional[float] = Field(default=None, title="Maximum Height (in meters)", description="""Maximum height of observation (in meters) for above ground aerial coverage.""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'max_height_in_m', 'domain_of': ['VerticalExtent']} })


class Organization(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Organization',
         'from_schema': 'Core',
         'slot_usage': {'identifier': {'description': 'Organization identifier in the '
                                                      'form of an ROR URL (e.g., '
                                                      'https://ror.org/02mhbdp94). '
                                                      'Please visit '
                                                      '[https://ror.org](https://ror.org) '
                                                      'to search for the organization '
                                                      'and find the appropriate ROR '
                                                      'URL.',
                                       'name': 'identifier'},
                        'name': {'description': 'Name of the organization',
                                 'name': 'name',
                                 'required': True}}})

    identifier: Optional[str] = Field(default=None, description="""Organization identifier in the form of an ROR URL (e.g., https://ror.org/02mhbdp94). Please visit [https://ror.org](https://ror.org) to search for the organization and find the appropriate ROR URL.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Organization', 'MonetaryGrant', 'Person'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., title="Name", description="""Name of the organization""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent'],
         'slot_uri': 'schema:name'} })
    country: Optional[str] = Field(default=None, title="Country", description="""The country in which the organization belongs.""", json_schema_extra = { "linkml_meta": {'alias': 'country', 'domain_of': ['Organization', 'Platform']} })


class Project(ConfiguredBaseModel):
    """
    A project conducting OAE field trials or modeling.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['schema:ResearchProject'],
         'from_schema': 'Project',
         'slot_usage': {'description': {'description': 'A narrative description of the '
                                                       'project. For example, what '
                                                       'were the goals of the project? '
                                                       'What were the research '
                                                       'questions? What were the '
                                                       'processes to achieve these '
                                                       'goals and answer these '
                                                       'questions? Who were the key '
                                                       'stakeholders, organizers, '
                                                       'project leaders? Was this '
                                                       'building off a previous or '
                                                       'ongoing project, or is this a '
                                                       'new '
                                                       'region/experiment/mechanistic '
                                                       'study?\n'
                                                       'If there are relevant '
                                                       'regulatory parameters and/or '
                                                       'limits to dosing trials at '
                                                       'this location, these may be '
                                                       'described here.',
                                        'name': 'description',
                                        'required': True,
                                        'title': 'Project Description'},
                        'project_id': {'name': 'project_id', 'required': True},
                        'spatial_coverage': {'name': 'spatial_coverage',
                                             'required': True},
                        'temporal_coverage': {'description': 'The start and end date '
                                                             '(optional) of the '
                                                             'project',
                                              'name': 'temporal_coverage',
                                              'required': True}}})

    project_id: str = Field(default=..., title="Project ID", description="""The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable.""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Project', 'Experiment', 'Dataset']} })
    description: str = Field(default=..., title="Project Description", description="""A narrative description of the project. For example, what were the goals of the project? What were the research questions? What were the processes to achieve these goals and answer these questions? Who were the key stakeholders, organizers, project leaders? Was this building off a previous or ongoing project, or is this a new region/experiment/mechanistic study?
If there are relevant regulatory parameters and/or limits to dosing trials at this location, these may be described here.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent'],
         'slot_uri': 'schema:description'} })
    temporal_coverage: str = Field(default=..., title="Temporal Coverage", description="""The start and end date (optional) of the project""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_coverage',
         'domain_of': ['Project', 'ExternalProject', 'FieldDataset'],
         'slot_uri': 'schema:temporalCoverage'} })
    spatial_coverage: SpatialCoverage = Field(default=..., title="Spatial Coverage", description="""Latitude/longitude bounds of project site (e.g., boundary domain of observations or relevant activities), expressed as a schema.org GeoShape bounding box.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_coverage',
         'domain_of': ['Project', 'ExternalProject', 'Experiment', 'ModelGrid'],
         'slot_uri': 'schema:spatialCoverage'} })
    experiments: Optional[List[Experiment]] = Field(default=None, title="Related Experiments", json_schema_extra = { "linkml_meta": {'alias': 'experiments',
         'domain_of': ['Project', 'Container'],
         'recommended': True} })
    project_leads: List[Person] = Field(default=..., title="Project Lead(s)", description="""Provide details for each project lead / principal investigator (PI) including: Name, institutional information (name, address), phone, email, ID type (e.g., ORCID, etc), researcher ID, and role.""", json_schema_extra = { "linkml_meta": {'alias': 'project_leads', 'domain_of': ['Project']} })
    sea_names: Optional[List[SeaNames]] = Field(default=None, title="Sea Names", description="""Names of the seas where the data collection takes place, See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'sea_names', 'domain_of': ['Project'], 'recommended': True} })
    physical_site_description: Optional[str] = Field(default=None, title="Physical Site Description", description="""Provide information to help characterize the field site and provide context when interpreting the data. For example, descriptions of tidal patterns, climatological conditions, notable geological characteristics, the geographical and marine setting (coastal, intertidal, island region, sheltered environment), and characteristic meteorological events. If possible based on the file type of this submission, please include useful maps or figures here.
Links to relevant datasets, cruise reports, etc may be provided here.""", json_schema_extra = { "linkml_meta": {'alias': 'physical_site_description', 'domain_of': ['Project']} })
    social_context_site_description: Optional[str] = Field(default=None, title="Social Context Site Description", description="""Details may include:
  - Commercial, recreational, ecological, and cultural uses of study site
  - Industrial site history
  - Demographics of site area
  - Notable events that may impact local sentiment to mCDR (for example: site had significant toxic spill in past decade, local positive support for offshore wind farming, frequent HAB site) -Ecologically protected species, economically significant operations in the marine environment
  - In study areas with nearby state or federal jurisdiction borders, potential conflicts with other countries or permits from foreign governments should be described.
  - Links to relevant social science surveys, engaged community groups, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'social_context_site_description', 'domain_of': ['Project']} })
    social_research_conducted_to_date: Optional[str] = Field(default=None, title="Social Research Conducted to Date", description="""A description of any social research conducted to date. If provided as a separate file, list filename here. Information may include:
  - Description of Community engagement research approach conducted and results
  - Stakeholder mapping method and link to output""", json_schema_extra = { "linkml_meta": {'alias': 'social_research_conducted_to_date', 'domain_of': ['Project']} })
    mcdr_pathway: MCDRPathway = Field(default=..., title="MCDR Pathway", description="""The Marine Carbon Dioxide Removal (MCDR) pathway being studied.""", json_schema_extra = { "linkml_meta": {'alias': 'mcdr_pathway', 'domain_of': ['Project']} })
    previous_or_ongoing_colocated_research: Optional[List[ExternalProject]] = Field(default=None, title="Previous or Ongoing Co-located Research", description="""This field is required for co-located operations that potentially impact the project results. If previous or on-going mCDR field operations have occurred in the study domain by any project developer, they may be mentioned here either as a description, and/or if a reference to the study exists in the form of a data set, publication, etc, the DOI or other identifying information should be provided. Please provide direct links to data when available.""", json_schema_extra = { "linkml_meta": {'alias': 'previous_or_ongoing_colocated_research', 'domain_of': ['Project']} })
    colocated_operations: Optional[str] = Field(default=None, title="Co-located Operations", description="""A description is required if any nearby operations exist that may influence the waters over the time period covered by this data. This might be a nearby mCDR project, a facility that discharges water with different characteristics than the inflow (e.g., a desalination plant), frequent boating operations, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'colocated_operations', 'domain_of': ['Project']} })
    research_project: Optional[str] = Field(default=None, title="Research Project", description="""Project, which the data collection is part of. For example, West Coast Ocean Acidification (WCOA) Project.""", json_schema_extra = { "linkml_meta": {'alias': 'research_project', 'domain_of': ['Project']} })
    funding: Optional[List[MonetaryGrant]] = Field(default=None, title="Funding Info", description="""Include the name of the funder, funder country, project title, project ID, and the project start and end dates. If there is no funding source (e.g., in the case of commercial projects), leave this field empty.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Project'], 'slot_uri': 'schema:funding'} })
    additional_details: Optional[str] = Field(default=None, title="Additional Details", description="""Open text area to include additional information. These may include information for sediment processes data, biological data, or any other required information if not included in the main metadata or data files.
See [General Guidelines for Your Data](https://www.carbontosea.org/oae-data-protocol/1-0-0/#general-guidelines-for-your-data) for relevant sections of your data. Additional informational files, such as digitized laboratory notebooks, blogs, etc., may be linked here.""", json_schema_extra = { "linkml_meta": {'alias': 'additional_details', 'domain_of': ['Project', 'InSituExperiment']} })

    @field_validator('temporal_coverage')
    def pattern_temporal_coverage(cls, v):
        pattern=re.compile(r"^\d{4}-\d{2}-\d{2}/(\d{4}-\d{2}-\d{2}|\.\.)$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid temporal_coverage format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid temporal_coverage format: {v}")
        return v


class NamedLink(ConfiguredBaseModel):
    """
    A link to a resource with a name and URL.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Project'})

    name: str = Field(default=..., title="Name", description="""The name of the linked resource.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent']} })
    url: str = Field(default=..., title="URL", description="""The URL of the linked resource.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['NamedLink']} })


class ExternalProject(ConfiguredBaseModel):
    """
    A research project that is not directly managed by the OAE project, but whose location is proximal to the OAE project and whose data may be relevant to understanding the context or impacts of OAE activities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'ExternalProject'})

    temporal_coverage: str = Field(default=..., title="Temporal Coverage", description="""Start date and end date (if known) of the project in ISO-8601 interval format (YYYY-MM-DD/YYY-MM-DD). If the end date is not known, use open-ended format YYYY-MM-DD/..""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_coverage',
         'domain_of': ['Project', 'ExternalProject', 'FieldDataset'],
         'slot_uri': 'schema:temporalCoverage'} })
    spatial_coverage: SpatialCoverage = Field(default=..., title="Spatial Coverage", description="""Latitude/longitude bounds of project site (e.g., boundary domain of observations or relevant activities), expressed as a schema.org GeoShape bounding box.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_coverage',
         'domain_of': ['Project', 'ExternalProject', 'Experiment', 'ModelGrid'],
         'slot_uri': 'schema:spatialCoverage'} })
    name: str = Field(default=..., title="Name", description="""The name of the external research project.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent']} })
    description: Optional[str] = Field(default=None, title="Description", description="""A brief description of the external research project.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent']} })
    related_links: Optional[List[str]] = Field(default=None, title="Related Links", description="""Links to websites or documents related to the external research project.""", json_schema_extra = { "linkml_meta": {'alias': 'related_links', 'domain_of': ['ExternalProject']} })

    @field_validator('temporal_coverage')
    def pattern_temporal_coverage(cls, v):
        pattern=re.compile(r"^\d{4}-\d{2}-\d{2}/(\d{4}-\d{2}-\d{2}|\.\.)$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid temporal_coverage format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid temporal_coverage format: {v}")
        return v


class MonetaryGrant(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:MonetaryGrant',
         'from_schema': 'MonetaryGrant',
         'slot_usage': {'identifier': {'description': 'Unique identifier of the grant. '
                                                      'Should be be URL or project id '
                                                      'used by the funder',
                                       'name': 'identifier'},
                        'name': {'description': 'Name of the grant', 'name': 'name'}}})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the grant""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent'],
         'slot_uri': 'schema:name'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier of the grant. Should be be URL or project id used by the funder""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Organization', 'MonetaryGrant', 'Person'],
         'slot_uri': 'schema:identifier'} })
    start_date: Optional[date] = Field(default=None, title="Start Date", json_schema_extra = { "linkml_meta": {'alias': 'start_date', 'domain_of': ['MonetaryGrant']} })
    end_date: Optional[date] = Field(default=None, title="End Date", json_schema_extra = { "linkml_meta": {'alias': 'end_date', 'domain_of': ['MonetaryGrant']} })
    funder: Optional[Organization] = Field(default=None, title="Funder", json_schema_extra = { "linkml_meta": {'alias': 'funder', 'domain_of': ['MonetaryGrant']} })


class Permit(ConfiguredBaseModel):
    """
    A permit associated with the project.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Permit'})

    permit_id: str = Field(default=..., title="Permit ID or Number", description="""The unique identifier or number associated with this permit.""", json_schema_extra = { "linkml_meta": {'alias': 'permit_id', 'domain_of': ['Permit']} })
    permitting_authority: str = Field(default=..., title="Permitting Authority", description="""The group that issued the permit.""", json_schema_extra = { "linkml_meta": {'alias': 'permitting_authority', 'domain_of': ['Permit']} })
    agency_contact: Optional[str] = Field(default=None, title="Agency Contact", description="""The point of contact at the permitting agency.""", json_schema_extra = { "linkml_meta": {'alias': 'agency_contact', 'domain_of': ['Permit']} })
    changes_to_evolution_of_permit_criteria: Optional[str] = Field(default=None, title="Changes to evolution of permit criteria", description="""e.g., changes of discharge pH and basis for changes""", json_schema_extra = { "linkml_meta": {'alias': 'changes_to_evolution_of_permit_criteria', 'domain_of': ['Permit']} })
    permit_type: Optional[str] = Field(default=None, title="Permit Type", description="""The category of permit (E.g., experimental permit, commercial permit)""", json_schema_extra = { "linkml_meta": {'alias': 'permit_type', 'domain_of': ['Permit']} })
    time_period: Optional[str] = Field(default=None, title="Permit Time Period", description="""The time period during which the permit will be applicable, or expected duration of the permit.""", json_schema_extra = { "linkml_meta": {'alias': 'time_period', 'domain_of': ['Permit']} })
    approval_document: str = Field(default=..., title="Permit Document", description="""Filename(s) of permitting documents included, separated by commas""", json_schema_extra = { "linkml_meta": {'alias': 'approval_document', 'domain_of': ['Permit']} })


class Experiment(ConfiguredBaseModel):
    """
    Abstract base class for all experiment types. Contains fields common to both in-situ and model experiments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Experiment',
         'slot_usage': {'description': {'description': 'A narrative description of the '
                                                       'experiment. For example, what '
                                                       'part of the project do these '
                                                       'data represent (e.g., '
                                                       'baseline, intervention, '
                                                       'control) and what do they '
                                                       'contribute to the overall '
                                                       'project? Are all project '
                                                       'research questions listed in '
                                                       'Project description relevant? '
                                                       'What were the processes to '
                                                       'achieve these goals and answer '
                                                       'these questions? Data '
                                                       'submitters are encouraged to '
                                                       'note any significant changes '
                                                       'to the original experimental '
                                                       'plan due to unforeseen '
                                                       'circumstances here.',
                                        'name': 'description',
                                        'required': True,
                                        'title': 'Experiment Description'},
                        'experiment_id': {'name': 'experiment_id', 'required': True},
                        'name': {'description': 'Optional common name for experiment.',
                                 'name': 'name'},
                        'project_id': {'name': 'project_id', 'required': True},
                        'spatial_coverage': {'description': 'Latitude/longitude bounds '
                                                            'of observed data in '
                                                            'experiment, expressed as '
                                                            'a schema.org GeoShape '
                                                            'bounding box.',
                                             'name': 'spatial_coverage',
                                             'required': True}}})

    name: Optional[str] = Field(default=None, title="Name", description="""Optional common name for experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., title="Experiment Description", description="""A narrative description of the experiment. For example, what part of the project do these data represent (e.g., baseline, intervention, control) and what do they contribute to the overall project? Are all project research questions listed in Project description relevant? What were the processes to achieve these goals and answer these questions? Data submitters are encouraged to note any significant changes to the original experimental plan due to unforeseen circumstances here.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent'],
         'slot_uri': 'schema:description'} })
    spatial_coverage: SpatialCoverage = Field(default=..., title="Spatial Coverage", description="""Latitude/longitude bounds of observed data in experiment, expressed as a schema.org GeoShape bounding box.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_coverage',
         'domain_of': ['Project', 'ExternalProject', 'Experiment', 'ModelGrid'],
         'slot_uri': 'schema:spatialCoverage'} })
    project_id: str = Field(default=..., title="Project ID", description="""The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable.""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Project', 'Experiment', 'Dataset']} })
    experiment_id: str = Field(default=..., title="Experiment ID", description="""The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:
Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_id', 'domain_of': ['Experiment', 'Dataset']} })
    experiment_types: List[ExperimentType] = Field(default=..., title="mCDR Experiment Type(s)", description="""The type(s) of mCDR experiment conducted. See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_types', 'domain_of': ['Experiment']} })
    public_comments: Optional[str] = Field(default=None, title="Public Comments", description="""File name(s) of public comment related documents. If possible, please provide public comments concatenated into a single pdf""", json_schema_extra = { "linkml_meta": {'alias': 'public_comments', 'domain_of': ['Experiment'], 'recommended': True} })
    experiment_leads: List[Person] = Field(default=..., title="Experiment Lead(s)", description="""Provide details for each experiment lead / principal investigator (PI) including: Name, institutional information (name, address), phone, email, ID type (e.g., ORCID, etc), researcher ID, and role.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_leads', 'domain_of': ['Experiment']} })
    start_datetime: datetime  = Field(default=..., title="Start Date and Time (UTC)", description="""Start date and time of experiment in UTC ISO-8601""", json_schema_extra = { "linkml_meta": {'alias': 'start_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })
    end_datetime: Optional[datetime ] = Field(default=None, title="End Date and Time (UTC)", description="""End date and time of experiment in UTC ISO-8601""", json_schema_extra = { "linkml_meta": {'alias': 'end_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })


class InSituExperiment(Experiment):
    """
    Experiment metadata for in-situ studies (interventions, tracer studies, etc.). Contains fields specific to field-based experiments that don't apply to model experiments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Experiment',
         'slot_usage': {'vertical_coverage': {'description': 'Minimum and maximum '
                                                             'depths of observations '
                                                             'in meters.',
                                              'name': 'vertical_coverage'}}})

    vertical_coverage: Optional[VerticalExtent] = Field(default=None, title="Vertical Coverage", description="""Minimum and maximum depths of observations in meters.""", json_schema_extra = { "linkml_meta": {'alias': 'vertical_coverage', 'domain_of': ['InSituExperiment']} })
    permits: Optional[List[Permit]] = Field(default=None, title="Permits", description="""Associated permit number(s).""", json_schema_extra = { "linkml_meta": {'alias': 'permits', 'domain_of': ['InSituExperiment']} })
    data_conflicts_and_unreported_data: Optional[str] = Field(default=None, title="Data Conflicts and Unreported Data", description="""If data exist that are or have been used by the project but are not provided due to conflicts (e.g., geopolitical or other), data availability (e.g., a dataset is no longer available), it may be noted here.""", json_schema_extra = { "linkml_meta": {'alias': 'data_conflicts_and_unreported_data',
         'domain_of': ['InSituExperiment']} })
    meteorological_and_tidal_data: Optional[List[NamedLink]] = Field(default=None, title="Meteorological and Tidal Data", description="""Include links to relevant open datasets if referenced in the experiment but not provided in the submission.""", json_schema_extra = { "linkml_meta": {'alias': 'meteorological_and_tidal_data', 'domain_of': ['InSituExperiment']} })
    additional_details: Optional[str] = Field(default=None, title="Additional Details", description="""Open text area to include additional information. These may include information for sediment processes data, biological data, or any other required information if not included in the main metadata or data files; see General Guidelines for Your Data for relevant sections of your data. Additional informational files, such as digitized laboratory notebooks, blogs, etc., may be linked here.""", json_schema_extra = { "linkml_meta": {'alias': 'additional_details', 'domain_of': ['Project', 'InSituExperiment']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Optional common name for experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., title="Experiment Description", description="""A narrative description of the experiment. For example, what part of the project do these data represent (e.g., baseline, intervention, control) and what do they contribute to the overall project? Are all project research questions listed in Project description relevant? What were the processes to achieve these goals and answer these questions? Data submitters are encouraged to note any significant changes to the original experimental plan due to unforeseen circumstances here.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent'],
         'slot_uri': 'schema:description'} })
    spatial_coverage: SpatialCoverage = Field(default=..., title="Spatial Coverage", description="""Latitude/longitude bounds of observed data in experiment, expressed as a schema.org GeoShape bounding box.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_coverage',
         'domain_of': ['Project', 'ExternalProject', 'Experiment', 'ModelGrid'],
         'slot_uri': 'schema:spatialCoverage'} })
    project_id: str = Field(default=..., title="Project ID", description="""The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable.""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Project', 'Experiment', 'Dataset']} })
    experiment_id: str = Field(default=..., title="Experiment ID", description="""The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:
Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_id', 'domain_of': ['Experiment', 'Dataset']} })
    experiment_types: List[ExperimentType] = Field(default=..., title="mCDR Experiment Type(s)", description="""The type(s) of mCDR experiment conducted. See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_types', 'domain_of': ['Experiment']} })
    public_comments: Optional[str] = Field(default=None, title="Public Comments", description="""File name(s) of public comment related documents. If possible, please provide public comments concatenated into a single pdf""", json_schema_extra = { "linkml_meta": {'alias': 'public_comments', 'domain_of': ['Experiment'], 'recommended': True} })
    experiment_leads: List[Person] = Field(default=..., title="Experiment Lead(s)", description="""Provide details for each experiment lead / principal investigator (PI) including: Name, institutional information (name, address), phone, email, ID type (e.g., ORCID, etc), researcher ID, and role.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_leads', 'domain_of': ['Experiment']} })
    start_datetime: datetime  = Field(default=..., title="Start Date and Time (UTC)", description="""Start date and time of experiment in UTC ISO-8601""", json_schema_extra = { "linkml_meta": {'alias': 'start_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })
    end_datetime: Optional[datetime ] = Field(default=None, title="End Date and Time (UTC)", description="""End date and time of experiment in UTC ISO-8601""", json_schema_extra = { "linkml_meta": {'alias': 'end_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })


class InterventionDetails(ConfiguredBaseModel):
    """
    An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are specific to an Experiment with type \"Intervention\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Experiment', 'mixin': True})

    alkalinity_feedstock_processing: AlkalinityFeedstockProcessing = Field(default=..., title="Alkalinity Feedstock Processing", description="""Method(s) used to process the alkalinity feedstock. See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_processing',
         'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_processing_custom: Optional[str] = Field(default=None, title="Alkalinity Feedstock Processing (Custom)", description="""Custom description of alkalinity feedstock processing method when 'other' is selected in alkalinity_feedstock_processing.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_processing_custom',
         'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_form: AlkalinityFeedstockForm = Field(default=..., title="Alkalinity Feedstock Form", description="""The phase upon delivery to the ocean. See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_form', 'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock: FeedstockType = Field(default=..., title="Alkalinity Feedstock", description="""Examples may include: olivine, potassium hydroxide, magnesium hydroxide, lime, portlandite, calcium carbonate, anorthite, dolomite, periclase, brucite, magnesite, forsterite, sodium hydroxide, natrite, nahcolite, akermanite, akermanite, alunoakermanite, etc.
See Controlled Vocabularies section for selected examples (this list is not exhaustive, you may need to include your unique feedstock).""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock', 'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_custom: Optional[str] = Field(default=None, title="Alkalinity Feedstock (Custom)", description="""Custom description of alkalinity feedstock when using a feedstock type not listed in the controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_custom', 'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_co2_removal_potential: float = Field(default=..., title="Alkalinity Feedstock CO₂ Removal Potential", description="""Maximum CO₂ removal potential of a feedstock material. We recommend using an adjusted version of the Steinour equation (Gunning et al., 2010), which uses bulk elemental oxide composition to estimate the maximum CO₂ removal potential of a feedstock material. The calculation output is in the form of kg of CO₂ per tonne of feedstock and represents the quantitative hypothetical potential of the material to capture CO₂ as bicarbonate or carbonate. See Isometric's CO2 removal potential module for details.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_co2_removal_potential',
         'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_description: str = Field(default=..., title="Alkalinity Feedstock Description", description="""Information such as feedstock source, characteristics, impurities, dilution prior to dosing, and concentration. For feedstock other than NaOH: trace metal composition and particulate grain size. Any variable information must be provided in the dosing data file, in this case include the data file and column header names here provided as variables. See Intervention Data for details.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_description',
         'domain_of': ['InterventionDetails']} })
    equilibration: EquilibrationStatus = Field(default=..., title="Equilibration", description="""Whether the feedstock was pre-equilibrated or unequilibrated""", json_schema_extra = { "linkml_meta": {'alias': 'equilibration', 'domain_of': ['InterventionDetails']} })
    alkalinity_dosing_effluent_density: DosingConcentration = Field(default=..., title="Alkalinity Dosing Effluent Density", description="""Fixed density or provide link/source to effluent density data if applicable. Please include whether density is directly measured or a derived value. If this is a variable included with your data, please note so here as 'alkalinity dosing effluent density is provided as a variable' and use 'dosing_effluent_density' for your column header name.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_dosing_effluent_density',
         'domain_of': ['InterventionDetails']} })


class TracerDetails(ConfiguredBaseModel):
    """
    An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are specific to an Experiment with type \"Tracer\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Experiment', 'mixin': True})

    tracer_form: TracerForm = Field(default=..., title="Tracer Form", description="""The form of tracer upon delivery to the ocean (e.g. gas or dye-release)""", json_schema_extra = { "linkml_meta": {'alias': 'tracer_form', 'domain_of': ['TracerDetails']} })
    tracer_form_custom: Optional[str] = Field(default=None, title="Tracer Form (Custom)", description="""If \"other\" was selected for Tracer Form, please specify the custom tracer form here.""", json_schema_extra = { "linkml_meta": {'alias': 'tracer_form_custom', 'domain_of': ['TracerDetails']} })
    tracer_details: str = Field(default=..., title="Tracer Details", description="""state the kind of tracer used (e.g. rhodamine, or a specific gas)""", json_schema_extra = { "linkml_meta": {'alias': 'tracer_details', 'domain_of': ['TracerDetails']} })
    tracer_concentration: DosingConcentration = Field(default=..., title="Tracer Concentration", description="""Fixed concentration or provide link/source to tracer concentration separately in the dosing file. Please include whether concentration is directly measured or a derived value. If this is a variable included with your data, please note so here as 'tracer concentration provided as a variable' and use 'tracer_concentration' for your column header name.""", json_schema_extra = { "linkml_meta": {'alias': 'tracer_concentration', 'domain_of': ['TracerDetails']} })


class DosingConcentration(ConfiguredBaseModel):
    """
    Details of tracer concentration information
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Experiment',
         'slot_usage': {'is_provided_as_a_file': {'description': 'Select ‘Variable’ if '
                                                                 'the concentration '
                                                                 'varies over time, or '
                                                                 '‘Fixed Value’ if it '
                                                                 'is constant. Note: '
                                                                 'Variable '
                                                                 'concentrations must '
                                                                 'be provided in a '
                                                                 'data file.',
                                                  'name': 'is_provided_as_a_file'}}})

    is_derived_value: bool = Field(default=..., description="""Indicates that the field in question is a derived value as opposed to one measured directly.""", json_schema_extra = { "linkml_meta": {'alias': 'is_derived_value', 'domain_of': ['DosingConcentration']} })
    is_provided_as_a_file: bool = Field(default=..., description="""Select ‘Variable’ if the concentration varies over time, or ‘Fixed Value’ if it is constant. Note: Variable concentrations must be provided in a data file.""", json_schema_extra = { "linkml_meta": {'alias': 'is_provided_as_a_file', 'domain_of': ['DosingConcentration']} })
    amount: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'amount', 'domain_of': ['DosingConcentration']} })
    unit: Optional[MassConcentrationUnit] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['DosingConcentration']} })


class DosingDetails(ConfiguredBaseModel):
    """
    An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are specific to an Experiment with active dosing (e.g. type \"Tracer\", \"Intervention\", or \"InterventionWithDosing\")
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Experiment', 'mixin': True})

    dosing_delivery_type: DosingDeliveryType = Field(default=..., title="Dosing Delivery Type", description="""Type of dosing delivery method. See Controlled Vocabularies for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_delivery_type', 'domain_of': ['DosingDetails']} })
    dosing_location: DosingLocation = Field(default=..., title="Dosing Location", description="""Provide latitude and longitude in decimal degrees. Depending on your method of dispersal, this information may be provided as a point source, vector, or bounding box. If provided as a vector, the latitude and longitude values should be included in the dosing data file.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_location', 'domain_of': ['DosingDetails']} })
    dosing_dispersal_hydrologic_location: HydrologicLocation = Field(default=..., title="Dosing Dispersal Hydrologic Location", description="""Descriptive dosing location""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_dispersal_hydrologic_location',
         'domain_of': ['DosingDetails']} })
    dosing_depth: str = Field(default=..., title="Dosing Depth", description="""Depth in meters. If this is variable, please include the schedule of depth changes and depths, or as a vector in meters with the data.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_depth', 'domain_of': ['DosingDetails']} })
    dosing_regimen: str = Field(default=..., title="Dosing Regimen", description="""A human readable summary description of the dosing regimen / frequency. Exact details must be provided in the corresponding dosing file with exact timestamps for dosing on/off schedule.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_regimen', 'domain_of': ['DosingDetails']} })
    dosing_description: str = Field(default=..., title="Dosing Description", description="""Please be descriptive. Information about the dosing mechanism must be included (outflow from pipe, diffuser, doser, manual placement)
E.g., outflow from existing facility pipe directly to ocean, manual riverine introduction, coastal distribution at three separate 30 meter long sections, pier-based diffuser to intercoastal bay, distributed from stationary barge 10 miles offshore.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_description', 'domain_of': ['DosingDetails']} })


class Intervention(DosingDetails, InterventionDetails, InSituExperiment):
    """
    Additional metadata that applies to experiments where an intervention, such as an alkalinity addition, was conducted.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Experiment',
         'mixins': ['InterventionDetails', 'DosingDetails'],
         'rules': [{'postconditions': {'slot_conditions': {'alkalinity_feedstock_custom': {'name': 'alkalinity_feedstock_custom',
                                                                                           'required': True}}},
                    'preconditions': {'slot_conditions': {'alkalinity_feedstock': {'equals_string': 'other',
                                                                                   'name': 'alkalinity_feedstock'}}}},
                   {'postconditions': {'slot_conditions': {'alkalinity_feedstock_processing_custom': {'name': 'alkalinity_feedstock_processing_custom',
                                                                                                      'required': True}}},
                    'preconditions': {'slot_conditions': {'alkalinity_feedstock_processing': {'equals_string': 'other',
                                                                                              'name': 'alkalinity_feedstock_processing'}}}}]})

    alkalinity_feedstock_processing: AlkalinityFeedstockProcessing = Field(default=..., title="Alkalinity Feedstock Processing", description="""Method(s) used to process the alkalinity feedstock. See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_processing',
         'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_processing_custom: Optional[str] = Field(default=None, title="Alkalinity Feedstock Processing (Custom)", description="""Custom description of alkalinity feedstock processing method when 'other' is selected in alkalinity_feedstock_processing.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_processing_custom',
         'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_form: AlkalinityFeedstockForm = Field(default=..., title="Alkalinity Feedstock Form", description="""The phase upon delivery to the ocean. See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_form', 'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock: FeedstockType = Field(default=..., title="Alkalinity Feedstock", description="""Examples may include: olivine, potassium hydroxide, magnesium hydroxide, lime, portlandite, calcium carbonate, anorthite, dolomite, periclase, brucite, magnesite, forsterite, sodium hydroxide, natrite, nahcolite, akermanite, akermanite, alunoakermanite, etc.
See Controlled Vocabularies section for selected examples (this list is not exhaustive, you may need to include your unique feedstock).""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock', 'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_custom: Optional[str] = Field(default=None, title="Alkalinity Feedstock (Custom)", description="""Custom description of alkalinity feedstock when using a feedstock type not listed in the controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_custom', 'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_co2_removal_potential: float = Field(default=..., title="Alkalinity Feedstock CO₂ Removal Potential", description="""Maximum CO₂ removal potential of a feedstock material. We recommend using an adjusted version of the Steinour equation (Gunning et al., 2010), which uses bulk elemental oxide composition to estimate the maximum CO₂ removal potential of a feedstock material. The calculation output is in the form of kg of CO₂ per tonne of feedstock and represents the quantitative hypothetical potential of the material to capture CO₂ as bicarbonate or carbonate. See Isometric's CO2 removal potential module for details.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_co2_removal_potential',
         'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_description: str = Field(default=..., title="Alkalinity Feedstock Description", description="""Information such as feedstock source, characteristics, impurities, dilution prior to dosing, and concentration. For feedstock other than NaOH: trace metal composition and particulate grain size. Any variable information must be provided in the dosing data file, in this case include the data file and column header names here provided as variables. See Intervention Data for details.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_description',
         'domain_of': ['InterventionDetails']} })
    equilibration: EquilibrationStatus = Field(default=..., title="Equilibration", description="""Whether the feedstock was pre-equilibrated or unequilibrated""", json_schema_extra = { "linkml_meta": {'alias': 'equilibration', 'domain_of': ['InterventionDetails']} })
    alkalinity_dosing_effluent_density: DosingConcentration = Field(default=..., title="Alkalinity Dosing Effluent Density", description="""Fixed density or provide link/source to effluent density data if applicable. Please include whether density is directly measured or a derived value. If this is a variable included with your data, please note so here as 'alkalinity dosing effluent density is provided as a variable' and use 'dosing_effluent_density' for your column header name.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_dosing_effluent_density',
         'domain_of': ['InterventionDetails']} })
    dosing_delivery_type: DosingDeliveryType = Field(default=..., title="Dosing Delivery Type", description="""Type of dosing delivery method. See Controlled Vocabularies for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_delivery_type', 'domain_of': ['DosingDetails']} })
    dosing_location: DosingLocation = Field(default=..., title="Dosing Location", description="""Provide latitude and longitude in decimal degrees. Depending on your method of dispersal, this information may be provided as a point source, vector, or bounding box. If provided as a vector, the latitude and longitude values should be included in the dosing data file.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_location', 'domain_of': ['DosingDetails']} })
    dosing_dispersal_hydrologic_location: HydrologicLocation = Field(default=..., title="Dosing Dispersal Hydrologic Location", description="""Descriptive dosing location""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_dispersal_hydrologic_location',
         'domain_of': ['DosingDetails']} })
    dosing_depth: str = Field(default=..., title="Dosing Depth", description="""Depth in meters. If this is variable, please include the schedule of depth changes and depths, or as a vector in meters with the data.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_depth', 'domain_of': ['DosingDetails']} })
    dosing_regimen: str = Field(default=..., title="Dosing Regimen", description="""A human readable summary description of the dosing regimen / frequency. Exact details must be provided in the corresponding dosing file with exact timestamps for dosing on/off schedule.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_regimen', 'domain_of': ['DosingDetails']} })
    dosing_description: str = Field(default=..., title="Dosing Description", description="""Please be descriptive. Information about the dosing mechanism must be included (outflow from pipe, diffuser, doser, manual placement)
E.g., outflow from existing facility pipe directly to ocean, manual riverine introduction, coastal distribution at three separate 30 meter long sections, pier-based diffuser to intercoastal bay, distributed from stationary barge 10 miles offshore.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_description', 'domain_of': ['DosingDetails']} })
    vertical_coverage: Optional[VerticalExtent] = Field(default=None, title="Vertical Coverage", description="""Minimum and maximum depths of observations in meters.""", json_schema_extra = { "linkml_meta": {'alias': 'vertical_coverage', 'domain_of': ['InSituExperiment']} })
    permits: Optional[List[Permit]] = Field(default=None, title="Permits", description="""Associated permit number(s).""", json_schema_extra = { "linkml_meta": {'alias': 'permits', 'domain_of': ['InSituExperiment']} })
    data_conflicts_and_unreported_data: Optional[str] = Field(default=None, title="Data Conflicts and Unreported Data", description="""If data exist that are or have been used by the project but are not provided due to conflicts (e.g., geopolitical or other), data availability (e.g., a dataset is no longer available), it may be noted here.""", json_schema_extra = { "linkml_meta": {'alias': 'data_conflicts_and_unreported_data',
         'domain_of': ['InSituExperiment']} })
    meteorological_and_tidal_data: Optional[List[NamedLink]] = Field(default=None, title="Meteorological and Tidal Data", description="""Include links to relevant open datasets if referenced in the experiment but not provided in the submission.""", json_schema_extra = { "linkml_meta": {'alias': 'meteorological_and_tidal_data', 'domain_of': ['InSituExperiment']} })
    additional_details: Optional[str] = Field(default=None, title="Additional Details", description="""Open text area to include additional information. These may include information for sediment processes data, biological data, or any other required information if not included in the main metadata or data files; see General Guidelines for Your Data for relevant sections of your data. Additional informational files, such as digitized laboratory notebooks, blogs, etc., may be linked here.""", json_schema_extra = { "linkml_meta": {'alias': 'additional_details', 'domain_of': ['Project', 'InSituExperiment']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Optional common name for experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., title="Experiment Description", description="""A narrative description of the experiment. For example, what part of the project do these data represent (e.g., baseline, intervention, control) and what do they contribute to the overall project? Are all project research questions listed in Project description relevant? What were the processes to achieve these goals and answer these questions? Data submitters are encouraged to note any significant changes to the original experimental plan due to unforeseen circumstances here.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent'],
         'slot_uri': 'schema:description'} })
    spatial_coverage: SpatialCoverage = Field(default=..., title="Spatial Coverage", description="""Latitude/longitude bounds of observed data in experiment, expressed as a schema.org GeoShape bounding box.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_coverage',
         'domain_of': ['Project', 'ExternalProject', 'Experiment', 'ModelGrid'],
         'slot_uri': 'schema:spatialCoverage'} })
    project_id: str = Field(default=..., title="Project ID", description="""The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable.""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Project', 'Experiment', 'Dataset']} })
    experiment_id: str = Field(default=..., title="Experiment ID", description="""The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:
Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_id', 'domain_of': ['Experiment', 'Dataset']} })
    experiment_types: List[ExperimentType] = Field(default=..., title="mCDR Experiment Type(s)", description="""The type(s) of mCDR experiment conducted. See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_types', 'domain_of': ['Experiment']} })
    public_comments: Optional[str] = Field(default=None, title="Public Comments", description="""File name(s) of public comment related documents. If possible, please provide public comments concatenated into a single pdf""", json_schema_extra = { "linkml_meta": {'alias': 'public_comments', 'domain_of': ['Experiment'], 'recommended': True} })
    experiment_leads: List[Person] = Field(default=..., title="Experiment Lead(s)", description="""Provide details for each experiment lead / principal investigator (PI) including: Name, institutional information (name, address), phone, email, ID type (e.g., ORCID, etc), researcher ID, and role.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_leads', 'domain_of': ['Experiment']} })
    start_datetime: datetime  = Field(default=..., title="Start Date and Time (UTC)", description="""Start date and time of experiment in UTC ISO-8601""", json_schema_extra = { "linkml_meta": {'alias': 'start_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })
    end_datetime: Optional[datetime ] = Field(default=None, title="End Date and Time (UTC)", description="""End date and time of experiment in UTC ISO-8601""", json_schema_extra = { "linkml_meta": {'alias': 'end_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })


class Tracer(DosingDetails, TracerDetails, InSituExperiment):
    """
    Additional metadata that applies to experiments where a tracer study was conducted
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Experiment',
         'mixins': ['TracerDetails', 'DosingDetails'],
         'rules': [{'postconditions': {'slot_conditions': {'tracer_form_custom': {'name': 'tracer_form_custom',
                                                                                  'required': True}}},
                    'preconditions': {'slot_conditions': {'tracer_form': {'equals_string': 'other',
                                                                          'name': 'tracer_form'}}}}]})

    tracer_form: TracerForm = Field(default=..., title="Tracer Form", description="""The form of tracer upon delivery to the ocean (e.g. gas or dye-release)""", json_schema_extra = { "linkml_meta": {'alias': 'tracer_form', 'domain_of': ['TracerDetails']} })
    tracer_form_custom: Optional[str] = Field(default=None, title="Tracer Form (Custom)", description="""If \"other\" was selected for Tracer Form, please specify the custom tracer form here.""", json_schema_extra = { "linkml_meta": {'alias': 'tracer_form_custom', 'domain_of': ['TracerDetails']} })
    tracer_details: str = Field(default=..., title="Tracer Details", description="""state the kind of tracer used (e.g. rhodamine, or a specific gas)""", json_schema_extra = { "linkml_meta": {'alias': 'tracer_details', 'domain_of': ['TracerDetails']} })
    tracer_concentration: DosingConcentration = Field(default=..., title="Tracer Concentration", description="""Fixed concentration or provide link/source to tracer concentration separately in the dosing file. Please include whether concentration is directly measured or a derived value. If this is a variable included with your data, please note so here as 'tracer concentration provided as a variable' and use 'tracer_concentration' for your column header name.""", json_schema_extra = { "linkml_meta": {'alias': 'tracer_concentration', 'domain_of': ['TracerDetails']} })
    dosing_delivery_type: DosingDeliveryType = Field(default=..., title="Dosing Delivery Type", description="""Type of dosing delivery method. See Controlled Vocabularies for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_delivery_type', 'domain_of': ['DosingDetails']} })
    dosing_location: DosingLocation = Field(default=..., title="Dosing Location", description="""Provide latitude and longitude in decimal degrees. Depending on your method of dispersal, this information may be provided as a point source, vector, or bounding box. If provided as a vector, the latitude and longitude values should be included in the dosing data file.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_location', 'domain_of': ['DosingDetails']} })
    dosing_dispersal_hydrologic_location: HydrologicLocation = Field(default=..., title="Dosing Dispersal Hydrologic Location", description="""Descriptive dosing location""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_dispersal_hydrologic_location',
         'domain_of': ['DosingDetails']} })
    dosing_depth: str = Field(default=..., title="Dosing Depth", description="""Depth in meters. If this is variable, please include the schedule of depth changes and depths, or as a vector in meters with the data.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_depth', 'domain_of': ['DosingDetails']} })
    dosing_regimen: str = Field(default=..., title="Dosing Regimen", description="""A human readable summary description of the dosing regimen / frequency. Exact details must be provided in the corresponding dosing file with exact timestamps for dosing on/off schedule.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_regimen', 'domain_of': ['DosingDetails']} })
    dosing_description: str = Field(default=..., title="Dosing Description", description="""Please be descriptive. Information about the dosing mechanism must be included (outflow from pipe, diffuser, doser, manual placement)
E.g., outflow from existing facility pipe directly to ocean, manual riverine introduction, coastal distribution at three separate 30 meter long sections, pier-based diffuser to intercoastal bay, distributed from stationary barge 10 miles offshore.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_description', 'domain_of': ['DosingDetails']} })
    vertical_coverage: Optional[VerticalExtent] = Field(default=None, title="Vertical Coverage", description="""Minimum and maximum depths of observations in meters.""", json_schema_extra = { "linkml_meta": {'alias': 'vertical_coverage', 'domain_of': ['InSituExperiment']} })
    permits: Optional[List[Permit]] = Field(default=None, title="Permits", description="""Associated permit number(s).""", json_schema_extra = { "linkml_meta": {'alias': 'permits', 'domain_of': ['InSituExperiment']} })
    data_conflicts_and_unreported_data: Optional[str] = Field(default=None, title="Data Conflicts and Unreported Data", description="""If data exist that are or have been used by the project but are not provided due to conflicts (e.g., geopolitical or other), data availability (e.g., a dataset is no longer available), it may be noted here.""", json_schema_extra = { "linkml_meta": {'alias': 'data_conflicts_and_unreported_data',
         'domain_of': ['InSituExperiment']} })
    meteorological_and_tidal_data: Optional[List[NamedLink]] = Field(default=None, title="Meteorological and Tidal Data", description="""Include links to relevant open datasets if referenced in the experiment but not provided in the submission.""", json_schema_extra = { "linkml_meta": {'alias': 'meteorological_and_tidal_data', 'domain_of': ['InSituExperiment']} })
    additional_details: Optional[str] = Field(default=None, title="Additional Details", description="""Open text area to include additional information. These may include information for sediment processes data, biological data, or any other required information if not included in the main metadata or data files; see General Guidelines for Your Data for relevant sections of your data. Additional informational files, such as digitized laboratory notebooks, blogs, etc., may be linked here.""", json_schema_extra = { "linkml_meta": {'alias': 'additional_details', 'domain_of': ['Project', 'InSituExperiment']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Optional common name for experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., title="Experiment Description", description="""A narrative description of the experiment. For example, what part of the project do these data represent (e.g., baseline, intervention, control) and what do they contribute to the overall project? Are all project research questions listed in Project description relevant? What were the processes to achieve these goals and answer these questions? Data submitters are encouraged to note any significant changes to the original experimental plan due to unforeseen circumstances here.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent'],
         'slot_uri': 'schema:description'} })
    spatial_coverage: SpatialCoverage = Field(default=..., title="Spatial Coverage", description="""Latitude/longitude bounds of observed data in experiment, expressed as a schema.org GeoShape bounding box.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_coverage',
         'domain_of': ['Project', 'ExternalProject', 'Experiment', 'ModelGrid'],
         'slot_uri': 'schema:spatialCoverage'} })
    project_id: str = Field(default=..., title="Project ID", description="""The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable.""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Project', 'Experiment', 'Dataset']} })
    experiment_id: str = Field(default=..., title="Experiment ID", description="""The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:
Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_id', 'domain_of': ['Experiment', 'Dataset']} })
    experiment_types: List[ExperimentType] = Field(default=..., title="mCDR Experiment Type(s)", description="""The type(s) of mCDR experiment conducted. See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_types', 'domain_of': ['Experiment']} })
    public_comments: Optional[str] = Field(default=None, title="Public Comments", description="""File name(s) of public comment related documents. If possible, please provide public comments concatenated into a single pdf""", json_schema_extra = { "linkml_meta": {'alias': 'public_comments', 'domain_of': ['Experiment'], 'recommended': True} })
    experiment_leads: List[Person] = Field(default=..., title="Experiment Lead(s)", description="""Provide details for each experiment lead / principal investigator (PI) including: Name, institutional information (name, address), phone, email, ID type (e.g., ORCID, etc), researcher ID, and role.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_leads', 'domain_of': ['Experiment']} })
    start_datetime: datetime  = Field(default=..., title="Start Date and Time (UTC)", description="""Start date and time of experiment in UTC ISO-8601""", json_schema_extra = { "linkml_meta": {'alias': 'start_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })
    end_datetime: Optional[datetime ] = Field(default=None, title="End Date and Time (UTC)", description="""End date and time of experiment in UTC ISO-8601""", json_schema_extra = { "linkml_meta": {'alias': 'end_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })


class InterventionWithTracer(Intervention, TracerDetails):
    """
    Additional metadata that applies to hybrid experiments where an intervention was conducted simultaneously alongside a tracer study, using the same instrumentation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Experiment',
         'mixins': ['TracerDetails'],
         'rules': [{'postconditions': {'slot_conditions': {'tracer_form_custom': {'name': 'tracer_form_custom',
                                                                                  'required': True}}},
                    'preconditions': {'slot_conditions': {'tracer_form': {'equals_string': 'other',
                                                                          'name': 'tracer_form'}}}}]})

    tracer_form: TracerForm = Field(default=..., title="Tracer Form", description="""The form of tracer upon delivery to the ocean (e.g. gas or dye-release)""", json_schema_extra = { "linkml_meta": {'alias': 'tracer_form', 'domain_of': ['TracerDetails']} })
    tracer_form_custom: Optional[str] = Field(default=None, title="Tracer Form (Custom)", description="""If \"other\" was selected for Tracer Form, please specify the custom tracer form here.""", json_schema_extra = { "linkml_meta": {'alias': 'tracer_form_custom', 'domain_of': ['TracerDetails']} })
    tracer_details: str = Field(default=..., title="Tracer Details", description="""state the kind of tracer used (e.g. rhodamine, or a specific gas)""", json_schema_extra = { "linkml_meta": {'alias': 'tracer_details', 'domain_of': ['TracerDetails']} })
    tracer_concentration: DosingConcentration = Field(default=..., title="Tracer Concentration", description="""Fixed concentration or provide link/source to tracer concentration separately in the dosing file. Please include whether concentration is directly measured or a derived value. If this is a variable included with your data, please note so here as 'tracer concentration provided as a variable' and use 'tracer_concentration' for your column header name.""", json_schema_extra = { "linkml_meta": {'alias': 'tracer_concentration', 'domain_of': ['TracerDetails']} })
    alkalinity_feedstock_processing: AlkalinityFeedstockProcessing = Field(default=..., title="Alkalinity Feedstock Processing", description="""Method(s) used to process the alkalinity feedstock. See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_processing',
         'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_processing_custom: Optional[str] = Field(default=None, title="Alkalinity Feedstock Processing (Custom)", description="""Custom description of alkalinity feedstock processing method when 'other' is selected in alkalinity_feedstock_processing.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_processing_custom',
         'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_form: AlkalinityFeedstockForm = Field(default=..., title="Alkalinity Feedstock Form", description="""The phase upon delivery to the ocean. See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_form', 'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock: FeedstockType = Field(default=..., title="Alkalinity Feedstock", description="""Examples may include: olivine, potassium hydroxide, magnesium hydroxide, lime, portlandite, calcium carbonate, anorthite, dolomite, periclase, brucite, magnesite, forsterite, sodium hydroxide, natrite, nahcolite, akermanite, akermanite, alunoakermanite, etc.
See Controlled Vocabularies section for selected examples (this list is not exhaustive, you may need to include your unique feedstock).""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock', 'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_custom: Optional[str] = Field(default=None, title="Alkalinity Feedstock (Custom)", description="""Custom description of alkalinity feedstock when using a feedstock type not listed in the controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_custom', 'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_co2_removal_potential: float = Field(default=..., title="Alkalinity Feedstock CO₂ Removal Potential", description="""Maximum CO₂ removal potential of a feedstock material. We recommend using an adjusted version of the Steinour equation (Gunning et al., 2010), which uses bulk elemental oxide composition to estimate the maximum CO₂ removal potential of a feedstock material. The calculation output is in the form of kg of CO₂ per tonne of feedstock and represents the quantitative hypothetical potential of the material to capture CO₂ as bicarbonate or carbonate. See Isometric's CO2 removal potential module for details.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_co2_removal_potential',
         'domain_of': ['InterventionDetails']} })
    alkalinity_feedstock_description: str = Field(default=..., title="Alkalinity Feedstock Description", description="""Information such as feedstock source, characteristics, impurities, dilution prior to dosing, and concentration. For feedstock other than NaOH: trace metal composition and particulate grain size. Any variable information must be provided in the dosing data file, in this case include the data file and column header names here provided as variables. See Intervention Data for details.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_feedstock_description',
         'domain_of': ['InterventionDetails']} })
    equilibration: EquilibrationStatus = Field(default=..., title="Equilibration", description="""Whether the feedstock was pre-equilibrated or unequilibrated""", json_schema_extra = { "linkml_meta": {'alias': 'equilibration', 'domain_of': ['InterventionDetails']} })
    alkalinity_dosing_effluent_density: DosingConcentration = Field(default=..., title="Alkalinity Dosing Effluent Density", description="""Fixed density or provide link/source to effluent density data if applicable. Please include whether density is directly measured or a derived value. If this is a variable included with your data, please note so here as 'alkalinity dosing effluent density is provided as a variable' and use 'dosing_effluent_density' for your column header name.""", json_schema_extra = { "linkml_meta": {'alias': 'alkalinity_dosing_effluent_density',
         'domain_of': ['InterventionDetails']} })
    dosing_delivery_type: DosingDeliveryType = Field(default=..., title="Dosing Delivery Type", description="""Type of dosing delivery method. See Controlled Vocabularies for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_delivery_type', 'domain_of': ['DosingDetails']} })
    dosing_location: DosingLocation = Field(default=..., title="Dosing Location", description="""Provide latitude and longitude in decimal degrees. Depending on your method of dispersal, this information may be provided as a point source, vector, or bounding box. If provided as a vector, the latitude and longitude values should be included in the dosing data file.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_location', 'domain_of': ['DosingDetails']} })
    dosing_dispersal_hydrologic_location: HydrologicLocation = Field(default=..., title="Dosing Dispersal Hydrologic Location", description="""Descriptive dosing location""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_dispersal_hydrologic_location',
         'domain_of': ['DosingDetails']} })
    dosing_depth: str = Field(default=..., title="Dosing Depth", description="""Depth in meters. If this is variable, please include the schedule of depth changes and depths, or as a vector in meters with the data.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_depth', 'domain_of': ['DosingDetails']} })
    dosing_regimen: str = Field(default=..., title="Dosing Regimen", description="""A human readable summary description of the dosing regimen / frequency. Exact details must be provided in the corresponding dosing file with exact timestamps for dosing on/off schedule.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_regimen', 'domain_of': ['DosingDetails']} })
    dosing_description: str = Field(default=..., title="Dosing Description", description="""Please be descriptive. Information about the dosing mechanism must be included (outflow from pipe, diffuser, doser, manual placement)
E.g., outflow from existing facility pipe directly to ocean, manual riverine introduction, coastal distribution at three separate 30 meter long sections, pier-based diffuser to intercoastal bay, distributed from stationary barge 10 miles offshore.""", json_schema_extra = { "linkml_meta": {'alias': 'dosing_description', 'domain_of': ['DosingDetails']} })
    vertical_coverage: Optional[VerticalExtent] = Field(default=None, title="Vertical Coverage", description="""Minimum and maximum depths of observations in meters.""", json_schema_extra = { "linkml_meta": {'alias': 'vertical_coverage', 'domain_of': ['InSituExperiment']} })
    permits: Optional[List[Permit]] = Field(default=None, title="Permits", description="""Associated permit number(s).""", json_schema_extra = { "linkml_meta": {'alias': 'permits', 'domain_of': ['InSituExperiment']} })
    data_conflicts_and_unreported_data: Optional[str] = Field(default=None, title="Data Conflicts and Unreported Data", description="""If data exist that are or have been used by the project but are not provided due to conflicts (e.g., geopolitical or other), data availability (e.g., a dataset is no longer available), it may be noted here.""", json_schema_extra = { "linkml_meta": {'alias': 'data_conflicts_and_unreported_data',
         'domain_of': ['InSituExperiment']} })
    meteorological_and_tidal_data: Optional[List[NamedLink]] = Field(default=None, title="Meteorological and Tidal Data", description="""Include links to relevant open datasets if referenced in the experiment but not provided in the submission.""", json_schema_extra = { "linkml_meta": {'alias': 'meteorological_and_tidal_data', 'domain_of': ['InSituExperiment']} })
    additional_details: Optional[str] = Field(default=None, title="Additional Details", description="""Open text area to include additional information. These may include information for sediment processes data, biological data, or any other required information if not included in the main metadata or data files; see General Guidelines for Your Data for relevant sections of your data. Additional informational files, such as digitized laboratory notebooks, blogs, etc., may be linked here.""", json_schema_extra = { "linkml_meta": {'alias': 'additional_details', 'domain_of': ['Project', 'InSituExperiment']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Optional common name for experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., title="Experiment Description", description="""A narrative description of the experiment. For example, what part of the project do these data represent (e.g., baseline, intervention, control) and what do they contribute to the overall project? Are all project research questions listed in Project description relevant? What were the processes to achieve these goals and answer these questions? Data submitters are encouraged to note any significant changes to the original experimental plan due to unforeseen circumstances here.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent'],
         'slot_uri': 'schema:description'} })
    spatial_coverage: SpatialCoverage = Field(default=..., title="Spatial Coverage", description="""Latitude/longitude bounds of observed data in experiment, expressed as a schema.org GeoShape bounding box.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_coverage',
         'domain_of': ['Project', 'ExternalProject', 'Experiment', 'ModelGrid'],
         'slot_uri': 'schema:spatialCoverage'} })
    project_id: str = Field(default=..., title="Project ID", description="""The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable.""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Project', 'Experiment', 'Dataset']} })
    experiment_id: str = Field(default=..., title="Experiment ID", description="""The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:
Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_id', 'domain_of': ['Experiment', 'Dataset']} })
    experiment_types: List[ExperimentType] = Field(default=..., title="mCDR Experiment Type(s)", description="""The type(s) of mCDR experiment conducted. See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_types', 'domain_of': ['Experiment']} })
    public_comments: Optional[str] = Field(default=None, title="Public Comments", description="""File name(s) of public comment related documents. If possible, please provide public comments concatenated into a single pdf""", json_schema_extra = { "linkml_meta": {'alias': 'public_comments', 'domain_of': ['Experiment'], 'recommended': True} })
    experiment_leads: List[Person] = Field(default=..., title="Experiment Lead(s)", description="""Provide details for each experiment lead / principal investigator (PI) including: Name, institutional information (name, address), phone, email, ID type (e.g., ORCID, etc), researcher ID, and role.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_leads', 'domain_of': ['Experiment']} })
    start_datetime: datetime  = Field(default=..., title="Start Date and Time (UTC)", description="""Start date and time of experiment in UTC ISO-8601""", json_schema_extra = { "linkml_meta": {'alias': 'start_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })
    end_datetime: Optional[datetime ] = Field(default=None, title="End Date and Time (UTC)", description="""End date and time of experiment in UTC ISO-8601""", json_schema_extra = { "linkml_meta": {'alias': 'end_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })


class Person(ConfiguredBaseModel):
    """
    Information about a researcher or investigator involved in the experiment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Person', 'from_schema': 'Person'})

    name: str = Field(default=..., title="Name", description="""Full name of the person.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent']} })
    affiliation: Optional[Organization] = Field(default=None, title="Affiliation", description="""Institutional affiliation of the investigator.""", json_schema_extra = { "linkml_meta": {'alias': 'affiliation', 'domain_of': ['Person']} })
    phone: Optional[str] = Field(default=None, title="Phone", description="""Contact phone number.""", json_schema_extra = { "linkml_meta": {'alias': 'phone', 'domain_of': ['Person']} })
    email: str = Field(default=..., title="Email", description="""Contact email address.""", json_schema_extra = { "linkml_meta": {'alias': 'email', 'domain_of': ['Person']} })
    identifier_type: Optional[ResearcherIDType] = Field(default=None, title="Researcher ID Type", description="""Type of Researcher ID (e.g., ORCID, ResearcherID).""", json_schema_extra = { "linkml_meta": {'alias': 'identifier_type', 'domain_of': ['Person']} })
    identifier: Optional[str] = Field(default=None, title="Researcher ID", description="""Unique researcher identifier value.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Organization', 'MonetaryGrant', 'Person']} })
    role: Optional[str] = Field(default=None, title="Role", description="""Role of the investigator in the experiment (e.g., chief scientist, data submitter).""", json_schema_extra = { "linkml_meta": {'alias': 'role', 'domain_of': ['Person']} })

    @field_validator('phone')
    def pattern_phone(cls, v):
        pattern=re.compile(r"^\+?[0-9\s\-\(\)]+$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid phone format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid phone format: {v}")
        return v

    @field_validator('email')
    def pattern_email(cls, v):
        pattern=re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid email format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid email format: {v}")
        return v


class Calibration(ConfiguredBaseModel):
    """
    Base calibration information for instruments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Calibration'})

    calibration_location: Optional[CalibrationLocation] = Field(default=None, title="Calibration location", description="""Factory calibration, lab calibration, or field calibration.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_location', 'domain_of': ['Calibration']} })
    technique_description: str = Field(default=..., title="Calibration technique description", description="""Details of the calibration technique used.""", json_schema_extra = { "linkml_meta": {'alias': 'technique_description', 'domain_of': ['Calibration']} })
    method_reference: Optional[str] = Field(default=None, title="Calibration method reference", description="""Citation or reference for the calibration method.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    frequency: Optional[str] = Field(default=None, title="Frequency of calibration", description="""How often the instrument was calibrated.""", json_schema_extra = { "linkml_meta": {'alias': 'frequency', 'domain_of': ['Calibration']} })
    last_calibration_date: Optional[datetime ] = Field(default=None, title="Last calibration date (UTC)", description="""Date and time of most recent calibration in UTC.""", json_schema_extra = { "linkml_meta": {'alias': 'last_calibration_date', 'domain_of': ['Calibration']} })
    calibration_certificates: Optional[str] = Field(default=None, title="Calibration certificate information", description="""Information about calibration certificates. Ideally, the certificate should be made available in a PDF file with filename listed here.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_certificates', 'domain_of': ['Calibration']} })


class CRMCalibration(Calibration):
    """
    Calibration using Certified Reference Materials, used for DIC and TA instruments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Calibration'})

    crm_manufacturer: str = Field(default=..., title="CRM manufacturer", description="""Manufacturer of the Certified Reference Material (e.g., Scripps, JAMSTEC).""", json_schema_extra = { "linkml_meta": {'alias': 'crm_manufacturer', 'domain_of': ['CRMCalibration']} })
    crm_batch_number: str = Field(default=..., title="CRM batch number", description="""Batch number of the Certified Reference Material.""", json_schema_extra = { "linkml_meta": {'alias': 'crm_batch_number', 'domain_of': ['CRMCalibration']} })
    calibration_location: Optional[CalibrationLocation] = Field(default=None, title="Calibration location", description="""Factory calibration, lab calibration, or field calibration.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_location', 'domain_of': ['Calibration']} })
    technique_description: str = Field(default=..., title="Calibration technique description", description="""Details of the calibration technique used.""", json_schema_extra = { "linkml_meta": {'alias': 'technique_description', 'domain_of': ['Calibration']} })
    method_reference: Optional[str] = Field(default=None, title="Calibration method reference", description="""Citation or reference for the calibration method.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    frequency: Optional[str] = Field(default=None, title="Frequency of calibration", description="""How often the instrument was calibrated.""", json_schema_extra = { "linkml_meta": {'alias': 'frequency', 'domain_of': ['Calibration']} })
    last_calibration_date: Optional[datetime ] = Field(default=None, title="Last calibration date (UTC)", description="""Date and time of most recent calibration in UTC.""", json_schema_extra = { "linkml_meta": {'alias': 'last_calibration_date', 'domain_of': ['Calibration']} })
    calibration_certificates: Optional[str] = Field(default=None, title="Calibration certificate information", description="""Information about calibration certificates. Ideally, the certificate should be made available in a PDF file with filename listed here.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_certificates', 'domain_of': ['Calibration']} })


class PHCalibration(Calibration):
    """
    pH instrument calibration with dye information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Calibration'})

    calibration_temperature: Optional[str] = Field(default=None, title="Calibration temperature", description="""Temperature at which calibration was performed.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_temperature',
         'domain_of': ['pHCalibration', 'DiscreteCO2Calibration']} })
    dye_type_and_manufacturer: Optional[str] = Field(default=None, title="Type of dye and manufacturer information", description="""Type of indicator dye and any detailed information about it, e.g., its manufacturer.""", json_schema_extra = { "linkml_meta": {'alias': 'dye_type_and_manufacturer', 'domain_of': ['pHCalibration']} })
    dye_purified: Optional[bool] = Field(default=None, title="Dye purified", description="""Whether the dye has been purified.""", json_schema_extra = { "linkml_meta": {'alias': 'dye_purified', 'domain_of': ['pHCalibration']} })
    correction_for_unpurified_dye: Optional[str] = Field(default=None, title="Correction for unpurified dye", description="""Correction method applied if dye was not purified.""", json_schema_extra = { "linkml_meta": {'alias': 'correction_for_unpurified_dye', 'domain_of': ['pHCalibration']} })
    dye_correction_method: Optional[str] = Field(default=None, title="Dye correction method", description="""Method used to correct for dye effects.""", json_schema_extra = { "linkml_meta": {'alias': 'dye_correction_method', 'domain_of': ['pHCalibration']} })
    ph_of_standards: Optional[str] = Field(default=None, title="pH of standards", description="""pH values of the calibration standards used.""", json_schema_extra = { "linkml_meta": {'alias': 'ph_of_standards', 'domain_of': ['pHCalibration']} })
    calibration_location: Optional[CalibrationLocation] = Field(default=None, title="Calibration location", description="""Factory calibration, lab calibration, or field calibration.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_location', 'domain_of': ['Calibration']} })
    technique_description: str = Field(default=..., title="Calibration technique description", description="""Details of the calibration technique used.""", json_schema_extra = { "linkml_meta": {'alias': 'technique_description', 'domain_of': ['Calibration']} })
    method_reference: Optional[str] = Field(default=None, title="Calibration method reference", description="""Citation or reference for the calibration method.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    frequency: Optional[str] = Field(default=None, title="Frequency of calibration", description="""How often the instrument was calibrated.""", json_schema_extra = { "linkml_meta": {'alias': 'frequency', 'domain_of': ['Calibration']} })
    last_calibration_date: Optional[datetime ] = Field(default=None, title="Last calibration date (UTC)", description="""Date and time of most recent calibration in UTC.""", json_schema_extra = { "linkml_meta": {'alias': 'last_calibration_date', 'domain_of': ['Calibration']} })
    calibration_certificates: Optional[str] = Field(default=None, title="Calibration certificate information", description="""Information about calibration certificates. Ideally, the certificate should be made available in a PDF file with filename listed here.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_certificates', 'domain_of': ['Calibration']} })


class CO2Calibration(Calibration):
    """
    Base CO2 gas detector calibration with standard gas information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Calibration'})

    standard_gas_info: Optional[StandardGas] = Field(default=None, title="Standard gas information", description="""Standard gases used for calibration.""", json_schema_extra = { "linkml_meta": {'alias': 'standard_gas_info',
         'domain_of': ['CO2Calibration', 'ContinuousCO2Calibration']} })
    calibration_location: Optional[CalibrationLocation] = Field(default=None, title="Calibration location", description="""Factory calibration, lab calibration, or field calibration.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_location', 'domain_of': ['Calibration']} })
    technique_description: str = Field(default=..., title="Calibration technique description", description="""Details of the calibration technique used.""", json_schema_extra = { "linkml_meta": {'alias': 'technique_description', 'domain_of': ['Calibration']} })
    method_reference: Optional[str] = Field(default=None, title="Calibration method reference", description="""Citation or reference for the calibration method.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    frequency: Optional[str] = Field(default=None, title="Frequency of calibration", description="""How often the instrument was calibrated.""", json_schema_extra = { "linkml_meta": {'alias': 'frequency', 'domain_of': ['Calibration']} })
    last_calibration_date: Optional[datetime ] = Field(default=None, title="Last calibration date (UTC)", description="""Date and time of most recent calibration in UTC.""", json_schema_extra = { "linkml_meta": {'alias': 'last_calibration_date', 'domain_of': ['Calibration']} })
    calibration_certificates: Optional[str] = Field(default=None, title="Calibration certificate information", description="""Information about calibration certificates. Ideally, the certificate should be made available in a PDF file with filename listed here.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_certificates', 'domain_of': ['Calibration']} })


class DiscreteCO2Calibration(CO2Calibration):
    """
    CO2 calibration for discrete measurements, with calibration temperature.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Calibration'})

    calibration_temperature: Optional[str] = Field(default=None, title="Calibration temperature", description="""Temperature at which calibration was performed.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_temperature',
         'domain_of': ['pHCalibration', 'DiscreteCO2Calibration']} })
    standard_gas_info: Optional[StandardGas] = Field(default=None, title="Standard gas information", description="""Standard gases used for calibration.""", json_schema_extra = { "linkml_meta": {'alias': 'standard_gas_info',
         'domain_of': ['CO2Calibration', 'ContinuousCO2Calibration']} })
    calibration_location: Optional[CalibrationLocation] = Field(default=None, title="Calibration location", description="""Factory calibration, lab calibration, or field calibration.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_location', 'domain_of': ['Calibration']} })
    technique_description: str = Field(default=..., title="Calibration technique description", description="""Details of the calibration technique used.""", json_schema_extra = { "linkml_meta": {'alias': 'technique_description', 'domain_of': ['Calibration']} })
    method_reference: Optional[str] = Field(default=None, title="Calibration method reference", description="""Citation or reference for the calibration method.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    frequency: Optional[str] = Field(default=None, title="Frequency of calibration", description="""How often the instrument was calibrated.""", json_schema_extra = { "linkml_meta": {'alias': 'frequency', 'domain_of': ['Calibration']} })
    last_calibration_date: Optional[datetime ] = Field(default=None, title="Last calibration date (UTC)", description="""Date and time of most recent calibration in UTC.""", json_schema_extra = { "linkml_meta": {'alias': 'last_calibration_date', 'domain_of': ['Calibration']} })
    calibration_certificates: Optional[str] = Field(default=None, title="Calibration certificate information", description="""Information about calibration certificates. Ideally, the certificate should be made available in a PDF file with filename listed here.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_certificates', 'domain_of': ['Calibration']} })


class ContinuousCO2Calibration(CO2Calibration):
    """
    CO2 calibration for continuous measurements, with extended standard gas details.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Calibration'})

    standard_gas_info: Optional[ContinuousStandardGas] = Field(default=None, title="Standard gas information", description="""Standard gases used for calibration.""", json_schema_extra = { "linkml_meta": {'alias': 'standard_gas_info',
         'domain_of': ['CO2Calibration', 'ContinuousCO2Calibration']} })
    calibration_location: Optional[CalibrationLocation] = Field(default=None, title="Calibration location", description="""Factory calibration, lab calibration, or field calibration.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_location', 'domain_of': ['Calibration']} })
    technique_description: str = Field(default=..., title="Calibration technique description", description="""Details of the calibration technique used.""", json_schema_extra = { "linkml_meta": {'alias': 'technique_description', 'domain_of': ['Calibration']} })
    method_reference: Optional[str] = Field(default=None, title="Calibration method reference", description="""Citation or reference for the calibration method.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    frequency: Optional[str] = Field(default=None, title="Frequency of calibration", description="""How often the instrument was calibrated.""", json_schema_extra = { "linkml_meta": {'alias': 'frequency', 'domain_of': ['Calibration']} })
    last_calibration_date: Optional[datetime ] = Field(default=None, title="Last calibration date (UTC)", description="""Date and time of most recent calibration in UTC.""", json_schema_extra = { "linkml_meta": {'alias': 'last_calibration_date', 'domain_of': ['Calibration']} })
    calibration_certificates: Optional[str] = Field(default=None, title="Calibration certificate information", description="""Information about calibration certificates. Ideally, the certificate should be made available in a PDF file with filename listed here.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_certificates', 'domain_of': ['Calibration']} })


class StandardGas(ConfiguredBaseModel):
    """
    Standard gas used for CO2 calibration.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Calibration'})

    manufacturer: Optional[str] = Field(default=None, title="Standard Gas Manufacturer", description="""Manufacturer of the standard gas.""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer',
         'domain_of': ['StandardGas', 'AnalyzingInstrument', 'GenericSensor']} })
    concentration: Optional[str] = Field(default=None, title="Standard Gas Concentration", description="""Concentrations of the CO2 standard gases that are used to calibrate the CO2 sensor, e.g., 260, 350, 510ppm.""", json_schema_extra = { "linkml_meta": {'alias': 'concentration', 'domain_of': ['StandardGas']} })
    uncertainty: Optional[str] = Field(default=None, title="Standard Gas Uncertainty", description="""Uncertainties of the CO2 standard gas, e.g., 0.5%.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })


class ContinuousStandardGas(StandardGas):
    """
    Standard gas used for continuous CO2 calibration, with additional traceability and count information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Calibration'})

    number_of_nonzero_standards: Optional[int] = Field(default=None, title="Number of non-zero gas standards", description="""How many non-zero gas standards were used for the calibration.""", json_schema_extra = { "linkml_meta": {'alias': 'number_of_nonzero_standards', 'domain_of': ['ContinuousStandardGas']} })
    traceability_to_wmo_standards: Optional[str] = Field(default=None, title="Traceability to WMO standards", description="""Information about traceability of standard gases to WMO standards.""", json_schema_extra = { "linkml_meta": {'alias': 'traceability_to_wmo_standards',
         'domain_of': ['ContinuousStandardGas']} })
    manufacturer: Optional[str] = Field(default=None, title="Standard Gas Manufacturer", description="""Manufacturer of the standard gas.""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer',
         'domain_of': ['StandardGas', 'AnalyzingInstrument', 'GenericSensor']} })
    concentration: Optional[str] = Field(default=None, title="Standard Gas Concentration", description="""Concentrations of the CO2 standard gases that are used to calibrate the CO2 sensor, e.g., 260, 350, 510ppm.""", json_schema_extra = { "linkml_meta": {'alias': 'concentration', 'domain_of': ['StandardGas']} })
    uncertainty: Optional[str] = Field(default=None, title="Standard Gas Uncertainty", description="""Uncertainties of the CO2 standard gas, e.g., 0.5%.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })


class AnalyzingInstrument(ConfiguredBaseModel):
    """
    Base class for scientific instruments used in analyzing samples for measurement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Instrument'})

    manufacturer: Optional[str] = Field(default=None, title="Manufacturer", description="""Manufacturer name of the instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer',
         'domain_of': ['StandardGas', 'AnalyzingInstrument', 'GenericSensor']} })
    model: Optional[str] = Field(default=None, title="Model", description="""Model number or name of the instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    instrument_type: AnalyzingInstrumentType = Field(default=..., title="Instrument type", description="""Type of instrument used to analyze samples or measure continuously.""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_type', 'domain_of': ['AnalyzingInstrument']} })
    instrument_type_custom: Optional[str] = Field(default=None, title="Instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'instrument_type_custom', 'domain_of': ['AnalyzingInstrument']} })
    serial_number: Optional[str] = Field(default=None, title="Serial number", description="""Serial number of the instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'serial_number',
         'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    precision: Optional[str] = Field(default=None, title="Precision", description="""Precision of the instrument measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'precision', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    accuracy: str = Field(default=..., title="Accuracy", description="""Accuracy of the instrument measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'accuracy', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    calibration: Optional[Calibration] = Field(default=None, title="Calibration", description="""Calibration information for this instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration',
         'domain_of': ['AnalyzingInstrument',
                       'PHInstrument',
                       'CRMInstrument',
                       'CO2GasDetector',
                       'ContinuousCO2GasDetector',
                       'GenericSensor']} })


class PHInstrument(AnalyzingInstrument):
    """
    pH measurement instrument with dye-based calibration.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Instrument'})

    calibration: PHCalibration = Field(default=..., title="Calibration", description="""pH calibration information for this instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration',
         'domain_of': ['AnalyzingInstrument',
                       'PHInstrument',
                       'CRMInstrument',
                       'CO2GasDetector',
                       'ContinuousCO2GasDetector',
                       'GenericSensor']} })
    manufacturer: Optional[str] = Field(default=None, title="Manufacturer", description="""Manufacturer name of the instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer',
         'domain_of': ['StandardGas', 'AnalyzingInstrument', 'GenericSensor']} })
    model: Optional[str] = Field(default=None, title="Model", description="""Model number or name of the instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    instrument_type: AnalyzingInstrumentType = Field(default=..., title="Instrument type", description="""Type of instrument used to analyze samples or measure continuously.""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_type', 'domain_of': ['AnalyzingInstrument']} })
    instrument_type_custom: Optional[str] = Field(default=None, title="Instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'instrument_type_custom', 'domain_of': ['AnalyzingInstrument']} })
    serial_number: Optional[str] = Field(default=None, title="Serial number", description="""Serial number of the instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'serial_number',
         'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    precision: Optional[str] = Field(default=None, title="Precision", description="""Precision of the instrument measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'precision', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    accuracy: str = Field(default=..., title="Accuracy", description="""Accuracy of the instrument measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'accuracy', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })


class CRMInstrument(AnalyzingInstrument):
    """
    Instrument calibrated with Certified Reference Materials, used for DIC and TA measurements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Instrument'})

    calibration: CRMCalibration = Field(default=..., title="Calibration", description="""CRM calibration information for this instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration',
         'domain_of': ['AnalyzingInstrument',
                       'PHInstrument',
                       'CRMInstrument',
                       'CO2GasDetector',
                       'ContinuousCO2GasDetector',
                       'GenericSensor']} })
    manufacturer: Optional[str] = Field(default=None, title="Manufacturer", description="""Manufacturer name of the instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer',
         'domain_of': ['StandardGas', 'AnalyzingInstrument', 'GenericSensor']} })
    model: Optional[str] = Field(default=None, title="Model", description="""Model number or name of the instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    instrument_type: AnalyzingInstrumentType = Field(default=..., title="Instrument type", description="""Type of instrument used to analyze samples or measure continuously.""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_type', 'domain_of': ['AnalyzingInstrument']} })
    instrument_type_custom: Optional[str] = Field(default=None, title="Instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'instrument_type_custom', 'domain_of': ['AnalyzingInstrument']} })
    serial_number: Optional[str] = Field(default=None, title="Serial number", description="""Serial number of the instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'serial_number',
         'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    precision: Optional[str] = Field(default=None, title="Precision", description="""Precision of the instrument measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'precision', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    accuracy: str = Field(default=..., title="Accuracy", description="""Accuracy of the instrument measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'accuracy', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })


class CO2GasDetector(AnalyzingInstrument):
    """
    CO2 gas detector with standard gas calibration.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Instrument',
         'slot_usage': {'instrument_type': {'equals_string': 'gas_analyzer',
                                            'name': 'instrument_type',
                                            'range': 'string'},
                        'manufacturer': {'description': 'Manufacture of the CO2 sensor',
                                         'name': 'manufacturer',
                                         'required': True},
                        'model': {'description': 'Model number of the CO2 sensor, '
                                                 'e.g., 6262',
                                  'name': 'model'}}})

    detector_type: str = Field(default=..., title="Detector Type", description="""Type of the CO2 gas detector (E.g., Infrared)""", json_schema_extra = { "linkml_meta": {'alias': 'detector_type', 'domain_of': ['CO2GasDetector']} })
    calibration: DiscreteCO2Calibration = Field(default=..., title="Calibration", description="""CO2 calibration information for this instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration',
         'domain_of': ['AnalyzingInstrument',
                       'PHInstrument',
                       'CRMInstrument',
                       'CO2GasDetector',
                       'ContinuousCO2GasDetector',
                       'GenericSensor']} })
    resolution: Optional[str] = Field(default=None, title="Resolution", description="""Resolution of the CO2 sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'resolution', 'domain_of': ['CO2GasDetector']} })
    uncertainty: Optional[str] = Field(default=None, title="Uncertainty", description="""Uncertainty of the CO2 sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    manufacturer: str = Field(default=..., title="Manufacturer", description="""Manufacture of the CO2 sensor""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer',
         'domain_of': ['StandardGas', 'AnalyzingInstrument', 'GenericSensor']} })
    model: Optional[str] = Field(default=None, title="Model", description="""Model number of the CO2 sensor, e.g., 6262""", json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    instrument_type: Literal["gas_analyzer"] = Field(default=..., title="Instrument type", description="""Type of instrument used to analyze samples or measure continuously.""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_type',
         'domain_of': ['AnalyzingInstrument'],
         'equals_string': 'gas_analyzer'} })
    instrument_type_custom: Optional[str] = Field(default=None, title="Instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'instrument_type_custom', 'domain_of': ['AnalyzingInstrument']} })
    serial_number: Optional[str] = Field(default=None, title="Serial number", description="""Serial number of the instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'serial_number',
         'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    precision: Optional[str] = Field(default=None, title="Precision", description="""Precision of the instrument measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'precision', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    accuracy: str = Field(default=..., title="Accuracy", description="""Accuracy of the instrument measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'accuracy', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })


class ContinuousCO2GasDetector(CO2GasDetector):
    """
    CO2 gas detector for continuous measurements, with measurement frequency.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Instrument'})

    measurement_frequency: Optional[str] = Field(default=None, title="Measurement frequency", description="""How often measurements are taken, e.g., every 140 seconds except during calibration.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_frequency', 'domain_of': ['ContinuousCO2GasDetector']} })
    calibration: ContinuousCO2Calibration = Field(default=..., title="Calibration", description="""CO2 calibration information for this continuous instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration',
         'domain_of': ['AnalyzingInstrument',
                       'PHInstrument',
                       'CRMInstrument',
                       'CO2GasDetector',
                       'ContinuousCO2GasDetector',
                       'GenericSensor']} })
    detector_type: str = Field(default=..., title="Detector Type", description="""Type of the CO2 gas detector (E.g., Infrared)""", json_schema_extra = { "linkml_meta": {'alias': 'detector_type', 'domain_of': ['CO2GasDetector']} })
    resolution: Optional[str] = Field(default=None, title="Resolution", description="""Resolution of the CO2 sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'resolution', 'domain_of': ['CO2GasDetector']} })
    uncertainty: Optional[str] = Field(default=None, title="Uncertainty", description="""Uncertainty of the CO2 sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    manufacturer: str = Field(default=..., title="Manufacturer", description="""Manufacture of the CO2 sensor""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer',
         'domain_of': ['StandardGas', 'AnalyzingInstrument', 'GenericSensor']} })
    model: Optional[str] = Field(default=None, title="Model", description="""Model number of the CO2 sensor, e.g., 6262""", json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    instrument_type: Literal["gas_analyzer"] = Field(default=..., title="Instrument type", description="""Type of instrument used to analyze samples or measure continuously.""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_type',
         'domain_of': ['AnalyzingInstrument'],
         'equals_string': 'gas_analyzer'} })
    instrument_type_custom: Optional[str] = Field(default=None, title="Instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'instrument_type_custom', 'domain_of': ['AnalyzingInstrument']} })
    serial_number: Optional[str] = Field(default=None, title="Serial number", description="""Serial number of the instrument.""", json_schema_extra = { "linkml_meta": {'alias': 'serial_number',
         'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    precision: Optional[str] = Field(default=None, title="Precision", description="""Precision of the instrument measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'precision', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    accuracy: str = Field(default=..., title="Accuracy", description="""Accuracy of the instrument measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'accuracy', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })


class CO2Equilibrator(ConfiguredBaseModel):
    """
    Equilibrator used for continuous CO2 measurement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Instrument'})

    equilibrator_type: Optional[str] = Field(default=None, title="Equilibrator type", description="""Type of the equilibrator for the CO2 measurement.""", json_schema_extra = { "linkml_meta": {'alias': 'equilibrator_type', 'domain_of': ['CO2Equilibrator']} })
    volume: Optional[float] = Field(default=None, title="Equilibrator volume (L)", description="""The total volume (in liters) of the CO2 equilibrator.""", json_schema_extra = { "linkml_meta": {'alias': 'volume', 'domain_of': ['CO2Equilibrator', 'SamplePreservation']} })
    vented: Optional[bool] = Field(default=None, title="Vented or not", description="""Is the equilibrator vented or not?""", json_schema_extra = { "linkml_meta": {'alias': 'vented', 'domain_of': ['CO2Equilibrator']} })
    water_flow_rate: Optional[float] = Field(default=None, title="Water flow rate (L/min)", description="""Flow rate (in L/min) of the flow through seawater.""", json_schema_extra = { "linkml_meta": {'alias': 'water_flow_rate', 'domain_of': ['CO2Equilibrator']} })
    headspace_gas_flow_rate: Optional[float] = Field(default=None, title="Headspace gas flow rate (L/min)", description="""Flow rate (in L/min) of the gas from the equilibrator to the CO2 analyzer.""", json_schema_extra = { "linkml_meta": {'alias': 'headspace_gas_flow_rate', 'domain_of': ['CO2Equilibrator']} })


class GenericSensor(ConfiguredBaseModel):
    """
    Generic sensor base class used in continuous CO2 measurements. Subclasses (e.g., TemperatureSensor, PressureSensor) specialize accuracy and precision units via slot_usage.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Instrument'})

    location: Optional[str] = Field(default=None, title="Location", description="""Location of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'location', 'domain_of': ['GenericSensor']} })
    manufacturer: Optional[str] = Field(default=None, title="Manufacturer", description="""Manufacturer of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer',
         'domain_of': ['StandardGas', 'AnalyzingInstrument', 'GenericSensor']} })
    model: Optional[str] = Field(default=None, title="Model", description="""Model number of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    serial_number: Optional[str] = Field(default=None, title="Serial number", description="""Serial number of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'serial_number',
         'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    accuracy: Optional[float] = Field(default=None, title="Accuracy", description="""Accuracy of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'accuracy', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    precision: Optional[float] = Field(default=None, title="Precision", description="""Precision of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'precision', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    calibration: Optional[str] = Field(default=None, title="Calibration", description="""Calibration information for the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration',
         'domain_of': ['AnalyzingInstrument',
                       'PHInstrument',
                       'CRMInstrument',
                       'CO2GasDetector',
                       'ContinuousCO2GasDetector',
                       'GenericSensor']} })
    comments: Optional[str] = Field(default=None, title="Comments", description="""Additional comments about the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'comments', 'domain_of': ['GenericSensor']} })


class TemperatureSensor(GenericSensor):
    """
    Temperature sensor used in continuous CO2 measurements. Accuracy and precision are reported in degrees Celsius.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Instrument',
         'slot_usage': {'accuracy': {'description': 'Accuracy of the temperature '
                                                    'sensor in degrees Celsius.',
                                     'name': 'accuracy',
                                     'title': 'Accuracy (°C)'},
                        'precision': {'description': 'Precision of the temperature '
                                                     'sensor in degrees Celsius.',
                                      'name': 'precision',
                                      'title': 'Precision (°C)'}}})

    location: Optional[str] = Field(default=None, title="Location", description="""Location of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'location', 'domain_of': ['GenericSensor']} })
    manufacturer: Optional[str] = Field(default=None, title="Manufacturer", description="""Manufacturer of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer',
         'domain_of': ['StandardGas', 'AnalyzingInstrument', 'GenericSensor']} })
    model: Optional[str] = Field(default=None, title="Model", description="""Model number of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    serial_number: Optional[str] = Field(default=None, title="Serial number", description="""Serial number of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'serial_number',
         'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    accuracy: Optional[float] = Field(default=None, title="Accuracy (°C)", description="""Accuracy of the temperature sensor in degrees Celsius.""", json_schema_extra = { "linkml_meta": {'alias': 'accuracy', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    precision: Optional[float] = Field(default=None, title="Precision (°C)", description="""Precision of the temperature sensor in degrees Celsius.""", json_schema_extra = { "linkml_meta": {'alias': 'precision', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    calibration: Optional[str] = Field(default=None, title="Calibration", description="""Calibration information for the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration',
         'domain_of': ['AnalyzingInstrument',
                       'PHInstrument',
                       'CRMInstrument',
                       'CO2GasDetector',
                       'ContinuousCO2GasDetector',
                       'GenericSensor']} })
    comments: Optional[str] = Field(default=None, title="Comments", description="""Additional comments about the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'comments', 'domain_of': ['GenericSensor']} })


class PressureSensor(GenericSensor):
    """
    Pressure sensor used in continuous CO2 measurements. Accuracy and precision are reported in hectopascals (hPa).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Instrument',
         'slot_usage': {'accuracy': {'description': 'Accuracy of the pressure sensor '
                                                    'in hectopascals (hPa).',
                                     'name': 'accuracy',
                                     'title': 'Accuracy (hPa)'},
                        'precision': {'description': 'Precision of the pressure sensor '
                                                     'in hectopascals (hPa).',
                                      'name': 'precision',
                                      'title': 'Precision (hPa)'}}})

    location: Optional[str] = Field(default=None, title="Location", description="""Location of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'location', 'domain_of': ['GenericSensor']} })
    manufacturer: Optional[str] = Field(default=None, title="Manufacturer", description="""Manufacturer of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer',
         'domain_of': ['StandardGas', 'AnalyzingInstrument', 'GenericSensor']} })
    model: Optional[str] = Field(default=None, title="Model", description="""Model number of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    serial_number: Optional[str] = Field(default=None, title="Serial number", description="""Serial number of the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'serial_number',
         'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    accuracy: Optional[float] = Field(default=None, title="Accuracy (hPa)", description="""Accuracy of the pressure sensor in hectopascals (hPa).""", json_schema_extra = { "linkml_meta": {'alias': 'accuracy', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    precision: Optional[float] = Field(default=None, title="Precision (hPa)", description="""Precision of the pressure sensor in hectopascals (hPa).""", json_schema_extra = { "linkml_meta": {'alias': 'precision', 'domain_of': ['AnalyzingInstrument', 'GenericSensor']} })
    calibration: Optional[str] = Field(default=None, title="Calibration", description="""Calibration information for the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration',
         'domain_of': ['AnalyzingInstrument',
                       'PHInstrument',
                       'CRMInstrument',
                       'CO2GasDetector',
                       'ContinuousCO2GasDetector',
                       'GenericSensor']} })
    comments: Optional[str] = Field(default=None, title="Comments", description="""Additional comments about the sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'comments', 'domain_of': ['GenericSensor']} })


class MarineAirMeasurement(ConfiguredBaseModel):
    """
    Information about CO2 measurements in marine air.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Instrument'})

    measured: bool = Field(default=..., title="CO2 in marine air measured", description="""Whether CO2 in marine air was measured.""", json_schema_extra = { "linkml_meta": {'alias': 'measured', 'domain_of': ['MarineAirMeasurement']} })
    measurement_interval: Optional[str] = Field(default=None, title="Measurement interval", description="""How often marine air CO2 is measured, e.g., 5 readings in a group every 5 hours.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_interval', 'domain_of': ['MarineAirMeasurement']} })
    location_and_height: Optional[str] = Field(default=None, title="Location and height", description="""Location and height of the marine air intake.""", json_schema_extra = { "linkml_meta": {'alias': 'location_and_height', 'domain_of': ['MarineAirMeasurement']} })
    drying_method: Optional[str] = Field(default=None, title="Drying method", description="""Method used to dry the gas stream for marine air measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'drying_method',
         'domain_of': ['MarineAirMeasurement', 'ContinuousCO2Variable']} })


class Variable(ConfiguredBaseModel):
    """
    Abstract root for all variable types (including non-measured)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'Variable'})

    units: Optional[str] = Field(default=None, title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["Variable"] = Field(default="Variable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: VariableType = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable']} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class NonMeasuredVariable(Variable):
    """
    A contextual or ancillary variable that is NOT directly measured or calculated by the project. Use for identifiers (Cruise_ID, Exp_ID), timestamps (Year_UTC, Time_UTC), coordinates (Latitude, Longitude), and any other data included in the dataset for context. Do NOT create a NonMeasuredVariable for quality control flag columns — instead, set dataset_variable_name_qc_flag on the parent measured or calculated variable that the flag relates to. variable_type must be \"non_measured\".
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'slot_usage': {'variable_type': {'equals_string': 'non_measured',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    units: Optional[str] = Field(default=None, title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["NonMeasuredVariable"] = Field(default="NonMeasuredVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["non_measured"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type',
         'domain_of': ['Variable'],
         'equals_string': 'non_measured'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class InSituVariable(Variable):
    """
    Base class for project-acquired variables (measured or calculated in-situ). Reference: OAPMetadata XSD variables.xsd - insitu_variable
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'Variable',
         'slot_usage': {'units': {'name': 'units', 'required': True}}})

    genesis: GenesisType = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["InSituVariable"] = Field(default="InSituVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: VariableType = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable']} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class SocioeconomicVariable(InSituVariable):
    """
    Socioeconomic variable for social and economic data such as survey responses, ecosystem service valuations, or text analysis. Extends InSituVariable to inherit method_reference and measurement_researcher, but does NOT include QCFields, instrument details, or calibration.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'slot_usage': {'variable_type': {'equals_string': 'socioeconomic',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    quantitative_or_qualitative: QuantitativeQualitative = Field(default=..., title="Quantitative or Qualitative", description="""Whether this variable captures quantitative (numerical) or qualitative (categorical/textual) data.""", json_schema_extra = { "linkml_meta": {'alias': 'quantitative_or_qualitative', 'domain_of': ['SocioeconomicVariable']} })
    social_study_type: Optional[SocialStudyType] = Field(default=None, title="Social Study Type", description="""The type of social science study this variable comes from.""", json_schema_extra = { "linkml_meta": {'alias': 'social_study_type', 'domain_of': ['SocioeconomicVariable']} })
    social_study_type_custom: Optional[str] = Field(default=None, title="Social Study Type (custom)", description="""Custom study type description when \"other\" is selected.""", json_schema_extra = { "linkml_meta": {'alias': 'social_study_type_custom', 'domain_of': ['SocioeconomicVariable']} })
    social_study_site_characterization: Optional[str] = Field(default=None, title="Study Site Characterization", description="""Time period and location description for the social study (e.g., \"2023-2024, coastal communities in Maine, USA\").""", json_schema_extra = { "linkml_meta": {'alias': 'social_study_site_characterization',
         'domain_of': ['SocioeconomicVariable']} })
    genesis: GenesisType = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["SocioeconomicVariable"] = Field(default="SocioeconomicVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["socioeconomic"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type',
         'domain_of': ['Variable'],
         'equals_string': 'socioeconomic'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class SamplePreservation(ConfiguredBaseModel):
    """
    Sample preservation information for DIC and TA measurements. Reference: OAPMetadata XSD variables.xsd - sample_preservation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable'})

    preservative: str = Field(default=..., title="Preservative used", description="""As described, e.g., Mercury Chloride.""", json_schema_extra = { "linkml_meta": {'alias': 'preservative', 'domain_of': ['SamplePreservation']} })
    volume: str = Field(default=..., title="Preservative volume", description="""The volume of preservative used.""", json_schema_extra = { "linkml_meta": {'alias': 'volume', 'domain_of': ['CO2Equilibrator', 'SamplePreservation']} })
    correction_description: Optional[str] = Field(default=None, title="Preservative correction description", description="""Description of how the preservative effect was corrected for.""", json_schema_extra = { "linkml_meta": {'alias': 'correction_description', 'domain_of': ['SamplePreservation']} })


class VocabularyItemReference(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable'})

    description: Optional[str] = Field(default=None, title="Description", description="""A narrative description of the thing.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent'],
         'slot_uri': 'schema:description'} })
    term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'term', 'domain_of': ['VocabularyItemReference']} })
    uri: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'uri', 'domain_of': ['VocabularyItemReference']} })


class MeasuredTAFields(ConfiguredBaseModel):
    """
    Fields applied to all measured TA variable types (discrete and continuous)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable', 'mixin': True})

    appropriate_use_quality: Optional[AppropriateUseQuality] = Field(default=None, title="Weather or climate quality", description="""Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.""", json_schema_extra = { "linkml_meta": {'alias': 'appropriate_use_quality',
         'domain_of': ['MeasuredTAFields',
                       'MeasuredDICFields',
                       'MeasuredPHFields',
                       'MeasuredCO2Fields']} })
    concentration_basis: ConcentrationBasis = Field(default=..., title="Per-volume vs per-mass based units", description="""Whether measurements are expressed per unit volume or per unit mass (for DIC, TA, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'concentration_basis',
         'domain_of': ['MeasuredTAFields', 'MeasuredDICFields']} })


class MeasuredDICFields(ConfiguredBaseModel):
    """
    Fields applied to all measured DIC variable types (discrete and continuous)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable', 'mixin': True})

    appropriate_use_quality: Optional[AppropriateUseQuality] = Field(default=None, title="Weather or climate quality", description="""Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.""", json_schema_extra = { "linkml_meta": {'alias': 'appropriate_use_quality',
         'domain_of': ['MeasuredTAFields',
                       'MeasuredDICFields',
                       'MeasuredPHFields',
                       'MeasuredCO2Fields']} })
    concentration_basis: ConcentrationBasis = Field(default=..., title="Per-volume vs per-mass based units", description="""Whether measurements are expressed per unit volume or per unit mass (for DIC, TA, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'concentration_basis',
         'domain_of': ['MeasuredTAFields', 'MeasuredDICFields']} })


class MeasuredPHFields(ConfiguredBaseModel):
    """
    Fields applied to all measured pH variable types (discrete and continuous)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable', 'mixin': True})

    appropriate_use_quality: Optional[AppropriateUseQuality] = Field(default=None, title="Weather or climate quality", description="""Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.""", json_schema_extra = { "linkml_meta": {'alias': 'appropriate_use_quality',
         'domain_of': ['MeasuredTAFields',
                       'MeasuredDICFields',
                       'MeasuredPHFields',
                       'MeasuredCO2Fields']} })


class MeasuredSedimentFields(ConfiguredBaseModel):
    """
    Fields applied to all measured sediment variable types (discrete and continuous)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable', 'mixin': True})

    sediment_type: str = Field(default=..., title="Sediment Type", description="""e.g., mud, sand, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'sediment_type', 'domain_of': ['MeasuredSedimentFields']} })
    sediment_sampling_method: str = Field(default=..., title="Sediment Sampling Method", description="""e.g., sediment core, grab sampling, dredging, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'sediment_sampling_method', 'domain_of': ['MeasuredSedimentFields']} })
    sediment_sampling_depth: str = Field(default=..., title="Sediment Sampling Depth", description="""Depth that sediment was collected below sediment surface. If provided as a variable (recommended), please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'sediment_sampling_depth', 'domain_of': ['MeasuredSedimentFields']} })
    sediment_sampling_water_depth: str = Field(default=..., title="Sediment Sampling Water Depth", description="""Water depth where sediment was collected. If provided as a variable (recommended), please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'sediment_sampling_water_depth',
         'domain_of': ['MeasuredSedimentFields']} })


class MeasuredPhysiologicalFields(ConfiguredBaseModel):
    """
    Fields applied to all measured physiological variable types (discrete and continuous). Captures biological subject identification and experimental design information for organism response field studies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable', 'mixin': True})

    biological_subject: str = Field(default=..., title="Biological Subject", description="""Taxonomy (species, genus, or community) being studied (e.g., Crassostrea gigas, coral reef community).""", json_schema_extra = { "linkml_meta": {'alias': 'biological_subject', 'domain_of': ['MeasuredPhysiologicalFields']} })
    species_identification_code: Optional[str] = Field(default=None, title="Species Identification Code", description="""Species reference code from a taxonomic database (e.g., WoRMS AphiaID 140656, ITIS TSN 79861).""", json_schema_extra = { "linkml_meta": {'alias': 'species_identification_code',
         'domain_of': ['MeasuredPhysiologicalFields']} })
    taxonomic_code_system: Optional[TaxonomicCodeSystem] = Field(default=None, title="Taxonomic Code System", description="""Which taxonomic code system the identification code refers to.""", json_schema_extra = { "linkml_meta": {'alias': 'taxonomic_code_system', 'domain_of': ['MeasuredPhysiologicalFields']} })
    life_stage: Optional[LifeStage] = Field(default=None, title="Life Stage", description="""Life stage of the organism at time of measurement.""", json_schema_extra = { "linkml_meta": {'alias': 'life_stage', 'domain_of': ['MeasuredPhysiologicalFields']} })
    life_stage_custom: Optional[str] = Field(default=None, title="Life Stage (custom)", description="""Custom life stage description when \"other\" is selected.""", json_schema_extra = { "linkml_meta": {'alias': 'life_stage_custom', 'domain_of': ['MeasuredPhysiologicalFields']} })


class MeasuredCO2Fields(ConfiguredBaseModel):
    """
    Fields applied to all measured CO2 variable types (discrete and continuous)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable', 'mixin': True})

    appropriate_use_quality: Optional[AppropriateUseQuality] = Field(default=None, title="Weather or climate quality", description="""Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.""", json_schema_extra = { "linkml_meta": {'alias': 'appropriate_use_quality',
         'domain_of': ['MeasuredTAFields',
                       'MeasuredDICFields',
                       'MeasuredPHFields',
                       'MeasuredCO2Fields']} })
    pco2_reported_temperature: str = Field(default=..., title="Temperature at which pCO2 was reported", description="""In Celsius. The input could be a constant temperature value, or something like, in-situ temperature, temperature of analysis, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'pco2_reported_temperature', 'domain_of': ['MeasuredCO2Fields']} })
    water_vapor_correction_method: Optional[str] = Field(default=None, title="Water vapor correction method", description="""How the water vapor pressure inside the equilibrator was determined.""", json_schema_extra = { "linkml_meta": {'alias': 'water_vapor_correction_method', 'domain_of': ['MeasuredCO2Fields']} })
    temperature_correction_method: Optional[str] = Field(default=None, title="Temperature correction method", description="""How the temperature effect was corrected.""", json_schema_extra = { "linkml_meta": {'alias': 'temperature_correction_method',
         'domain_of': ['DiscretePHVariable', 'MeasuredCO2Fields']} })


class QCFields(ConfiguredBaseModel):
    """
    Quality control fields applicable to measured and calculated variables. Not applied to socioeconomic variables.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable', 'mixin': True})

    qc_steps_taken: Optional[str] = Field(default=None, title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: Optional[str] = Field(default=None, title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: Optional[str] = Field(default=None, title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: Optional[str] = Field(default=None, title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })


class MeasuredVariable(QCFields, InSituVariable):
    """
    Variable that is directly measured in-situ using instruments. Reference: OAPMetadata XSD variables.xsd - basic_measured_observation_base
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'Variable',
         'mixins': ['QCFields'],
         'slot_usage': {'genesis': {'equals_string': 'measured',
                                    'name': 'genesis',
                                    'range': 'string'},
                        'missing_value_indicators': {'name': 'missing_value_indicators',
                                                     'required': True},
                        'qc_steps_taken': {'name': 'qc_steps_taken', 'required': True},
                        'uncertainty': {'name': 'uncertainty', 'required': True},
                        'uncertainty_definition': {'name': 'uncertainty_definition',
                                                   'required': True}}})

    analyzing_instrument: AnalyzingInstrument = Field(default=..., title="Analyzing instrument", description="""Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: SamplingType = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["MeasuredVariable"] = Field(default="MeasuredVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: VariableType = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable']} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class DiscreteMeasuredVariable(MeasuredVariable):
    """
    A variable measured in-situ from discrete water samples (e.g., bottle samples analyzed in a lab or shipboard). Use this class for generic measured variables that do not fall under a specific category (pH, TA, DIC, CO2, sediment, HPLC). For those, use the type-specific subclass instead (e.g., DiscretePHVariable). Set variable_type to \"other\", genesis to \"measured\", and sampling to \"discrete\".
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'slot_usage': {'sampling': {'equals_string': 'discrete',
                                     'name': 'sampling',
                                     'range': 'string'}}})

    analyzing_instrument: AnalyzingInstrument = Field(default=..., title="Analyzing instrument", description="""Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["discrete"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'discrete'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["DiscreteMeasuredVariable"] = Field(default="DiscreteMeasuredVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: VariableType = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable']} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class ContinuousMeasuredVariable(MeasuredVariable):
    """
    A variable measured in-situ by a continuous autonomous sensor (e.g., temperature, salinity, conductivity, pressure from a deployed sonde or underway system). Use this class for generic measured variables that do not fall under a specific category (pH, TA, DIC, CO2, sediment). For those, use the type-specific subclass instead (e.g., ContinuousPHVariable). Set variable_type to \"other\", genesis to \"measured\", and sampling to \"continuous\".
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'slot_usage': {'sampling': {'equals_string': 'continuous',
                                     'name': 'sampling',
                                     'range': 'string'}}})

    raw_data_calculation_method: str = Field(default=..., title="Method to calculate reported values from raw data", description="""The method used to calculate reported values from raw sensor data.""", json_schema_extra = { "linkml_meta": {'alias': 'raw_data_calculation_method',
         'domain_of': ['ContinuousMeasuredVariable']} })
    calculation_software_version: Optional[str] = Field(default=None, title="Software version for the calculation", description="""Version of the software used to calculate reported values from raw values.""", json_schema_extra = { "linkml_meta": {'alias': 'calculation_software_version',
         'domain_of': ['ContinuousMeasuredVariable']} })
    analyzing_instrument: AnalyzingInstrument = Field(default=..., title="Analyzing instrument", description="""Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["continuous"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'continuous'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["ContinuousMeasuredVariable"] = Field(default="ContinuousMeasuredVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: VariableType = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable']} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class CalculatedVariable(QCFields, InSituVariable):
    """
    A variable that is calculated or derived from other measured variables rather than directly measured by an instrument (e.g., carbonate system parameters computed via CO2SYS). Set genesis to \"calculated\". The variable_type should reflect the quantity being calculated (e.g., \"pH\", \"ta\", \"dic\", \"co2\", or \"other\").
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['QCFields'],
         'slot_usage': {'genesis': {'equals_string': 'calculated',
                                    'name': 'genesis',
                                    'range': 'string'}}})

    calculation_method_and_parameters: str = Field(default=..., title="Calculated Method And Parameters", description="""Information about how the variable was calculated and the parameters used in calculation, e.g.: Calculation software = CO2SYSv1 (MATLAB) Input variables =  pH and DIC (column header names 'ph_t_insitu' and 'dic' in associated dataset file) Additional information = the dissociation constants of Lueker et al., 2000 for carbonic acid, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'calculation_method_and_parameters',
         'domain_of': ['CalculatedVariable']} })
    qc_steps_taken: Optional[str] = Field(default=None, title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: Optional[str] = Field(default=None, title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: Optional[str] = Field(default=None, title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: Optional[str] = Field(default=None, title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["calculated"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'calculated'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["CalculatedVariable"] = Field(default="CalculatedVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: VariableType = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable']} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class ContinuousPHVariable(ContinuousMeasuredVariable, MeasuredPHFields):
    """
    pH measured variable from continuous autonomous sensor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['MeasuredPHFields'],
         'slot_usage': {'variable_type': {'equals_string': 'pH',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    appropriate_use_quality: Optional[AppropriateUseQuality] = Field(default=None, title="Weather or climate quality", description="""Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.""", json_schema_extra = { "linkml_meta": {'alias': 'appropriate_use_quality',
         'domain_of': ['MeasuredTAFields',
                       'MeasuredDICFields',
                       'MeasuredPHFields',
                       'MeasuredCO2Fields']} })
    raw_data_calculation_method: str = Field(default=..., title="Method to calculate reported values from raw data", description="""The method used to calculate reported values from raw sensor data.""", json_schema_extra = { "linkml_meta": {'alias': 'raw_data_calculation_method',
         'domain_of': ['ContinuousMeasuredVariable']} })
    calculation_software_version: Optional[str] = Field(default=None, title="Software version for the calculation", description="""Version of the software used to calculate reported values from raw values.""", json_schema_extra = { "linkml_meta": {'alias': 'calculation_software_version',
         'domain_of': ['ContinuousMeasuredVariable']} })
    analyzing_instrument: AnalyzingInstrument = Field(default=..., title="Analyzing instrument", description="""Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["continuous"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'continuous'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["ContinuousPHVariable"] = Field(default="ContinuousPHVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["pH"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable'], 'equals_string': 'pH'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class DiscretePHVariable(DiscreteMeasuredVariable, MeasuredPHFields):
    """
    pH measured variable with dye-based spectrophotometric measurement. Reference: OAPMetadata XSD variables.xsd - pH_measured
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['MeasuredPHFields'],
         'slot_usage': {'analyzing_instrument': {'description': 'pH instrument with '
                                                                'dye-based calibration '
                                                                'used for '
                                                                'measurements.',
                                                 'name': 'analyzing_instrument',
                                                 'range': 'PHInstrument'},
                        'variable_type': {'equals_string': 'pH',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    measurement_temperature: str = Field(default=..., title="Temperature at which pH was measured", description="""Temperature at which pH was measured.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_temperature',
         'domain_of': ['DiscretePHVariable', 'DiscreteCO2Variable']} })
    temperature_correction_method: Optional[str] = Field(default=None, title="Temperature correction method", description="""Method used to correct pH for temperature.""", json_schema_extra = { "linkml_meta": {'alias': 'temperature_correction_method',
         'domain_of': ['DiscretePHVariable', 'MeasuredCO2Fields']} })
    ph_reported_temperature: str = Field(default=..., title="Temperature at which pH was reported", description="""The input could be a constant temperature value, or something like, in-situ temperature, temperature of analysis, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'ph_reported_temperature', 'domain_of': ['DiscretePHVariable']} })
    appropriate_use_quality: Optional[AppropriateUseQuality] = Field(default=None, title="Weather or climate quality", description="""Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.""", json_schema_extra = { "linkml_meta": {'alias': 'appropriate_use_quality',
         'domain_of': ['MeasuredTAFields',
                       'MeasuredDICFields',
                       'MeasuredPHFields',
                       'MeasuredCO2Fields']} })
    analyzing_instrument: PHInstrument = Field(default=..., title="Analyzing instrument", description="""pH instrument with dye-based calibration used for measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["discrete"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'discrete'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["DiscretePHVariable"] = Field(default="DiscretePHVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["pH"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable'], 'equals_string': 'pH'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class ContinuousTAVariable(ContinuousMeasuredVariable, MeasuredTAFields):
    """
    Total Alkalinity (TA) measured variable from continuous autonomous sensor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['MeasuredTAFields'],
         'slot_usage': {'variable_type': {'equals_string': 'ta',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    appropriate_use_quality: Optional[AppropriateUseQuality] = Field(default=None, title="Weather or climate quality", description="""Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.""", json_schema_extra = { "linkml_meta": {'alias': 'appropriate_use_quality',
         'domain_of': ['MeasuredTAFields',
                       'MeasuredDICFields',
                       'MeasuredPHFields',
                       'MeasuredCO2Fields']} })
    concentration_basis: ConcentrationBasis = Field(default=..., title="Per-volume vs per-mass based units", description="""Whether measurements are expressed per unit volume or per unit mass (for DIC, TA, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'concentration_basis',
         'domain_of': ['MeasuredTAFields', 'MeasuredDICFields']} })
    raw_data_calculation_method: str = Field(default=..., title="Method to calculate reported values from raw data", description="""The method used to calculate reported values from raw sensor data.""", json_schema_extra = { "linkml_meta": {'alias': 'raw_data_calculation_method',
         'domain_of': ['ContinuousMeasuredVariable']} })
    calculation_software_version: Optional[str] = Field(default=None, title="Software version for the calculation", description="""Version of the software used to calculate reported values from raw values.""", json_schema_extra = { "linkml_meta": {'alias': 'calculation_software_version',
         'domain_of': ['ContinuousMeasuredVariable']} })
    analyzing_instrument: AnalyzingInstrument = Field(default=..., title="Analyzing instrument", description="""Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["continuous"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'continuous'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["ContinuousTAVariable"] = Field(default="ContinuousTAVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["ta"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable'], 'equals_string': 'ta'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class DiscreteTAVariable(DiscreteMeasuredVariable, MeasuredTAFields):
    """
    Total Alkalinity (TA) measured variable from discrete bottle samples
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['MeasuredTAFields'],
         'slot_usage': {'analyzing_instrument': {'description': 'CRM-calibrated '
                                                                'instrument used to '
                                                                'analyze TA samples.',
                                                 'name': 'analyzing_instrument',
                                                 'range': 'CRMInstrument'},
                        'variable_type': {'equals_string': 'ta',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    sample_preservation: SamplePreservation = Field(default=..., title="Sample preservation", description="""How the samples were preserved for analysis.""", json_schema_extra = { "linkml_meta": {'alias': 'sample_preservation',
         'domain_of': ['DiscreteTAVariable', 'DiscreteDICVariable']} })
    blank_correction: str = Field(default=..., title="Magnitude of blank correction", description="""Whether the reported variables were corrected for blank, and if so, how they were corrected.""", json_schema_extra = { "linkml_meta": {'alias': 'blank_correction',
         'domain_of': ['DiscreteTAVariable', 'DiscreteDICVariable']} })
    titration_type: str = Field(default=..., title="Titration type", description="""Type of the titration used to determine alkalinity.""", json_schema_extra = { "linkml_meta": {'alias': 'titration_type', 'domain_of': ['DiscreteTAVariable']} })
    titration_cell_type: Optional[TitrationCellType] = Field(default=None, title="Cell type", description="""Whether the titration cell is open or closed.""", json_schema_extra = { "linkml_meta": {'alias': 'titration_cell_type', 'domain_of': ['DiscreteTAVariable']} })
    curve_fitting_method: Optional[str] = Field(default=None, title="Curve fitting method", description="""Curve fitting method used to determine the alkalinity.""", json_schema_extra = { "linkml_meta": {'alias': 'curve_fitting_method', 'domain_of': ['DiscreteTAVariable']} })
    appropriate_use_quality: Optional[AppropriateUseQuality] = Field(default=None, title="Weather or climate quality", description="""Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.""", json_schema_extra = { "linkml_meta": {'alias': 'appropriate_use_quality',
         'domain_of': ['MeasuredTAFields',
                       'MeasuredDICFields',
                       'MeasuredPHFields',
                       'MeasuredCO2Fields']} })
    concentration_basis: ConcentrationBasis = Field(default=..., title="Per-volume vs per-mass based units", description="""Whether measurements are expressed per unit volume or per unit mass (for DIC, TA, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'concentration_basis',
         'domain_of': ['MeasuredTAFields', 'MeasuredDICFields']} })
    analyzing_instrument: CRMInstrument = Field(default=..., title="Analyzing instrument", description="""CRM-calibrated instrument used to analyze TA samples.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["discrete"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'discrete'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["DiscreteTAVariable"] = Field(default="DiscreteTAVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["ta"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable'], 'equals_string': 'ta'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class ContinuousDICVariable(ContinuousMeasuredVariable, MeasuredDICFields):
    """
    Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous sensor.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['MeasuredDICFields'],
         'slot_usage': {'variable_type': {'equals_string': 'dic',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    appropriate_use_quality: Optional[AppropriateUseQuality] = Field(default=None, title="Weather or climate quality", description="""Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.""", json_schema_extra = { "linkml_meta": {'alias': 'appropriate_use_quality',
         'domain_of': ['MeasuredTAFields',
                       'MeasuredDICFields',
                       'MeasuredPHFields',
                       'MeasuredCO2Fields']} })
    concentration_basis: ConcentrationBasis = Field(default=..., title="Per-volume vs per-mass based units", description="""Whether measurements are expressed per unit volume or per unit mass (for DIC, TA, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'concentration_basis',
         'domain_of': ['MeasuredTAFields', 'MeasuredDICFields']} })
    raw_data_calculation_method: str = Field(default=..., title="Method to calculate reported values from raw data", description="""The method used to calculate reported values from raw sensor data.""", json_schema_extra = { "linkml_meta": {'alias': 'raw_data_calculation_method',
         'domain_of': ['ContinuousMeasuredVariable']} })
    calculation_software_version: Optional[str] = Field(default=None, title="Software version for the calculation", description="""Version of the software used to calculate reported values from raw values.""", json_schema_extra = { "linkml_meta": {'alias': 'calculation_software_version',
         'domain_of': ['ContinuousMeasuredVariable']} })
    analyzing_instrument: AnalyzingInstrument = Field(default=..., title="Analyzing instrument", description="""Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["continuous"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'continuous'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["ContinuousDICVariable"] = Field(default="ContinuousDICVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["dic"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable'], 'equals_string': 'dic'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class DiscreteDICVariable(DiscreteMeasuredVariable, MeasuredDICFields):
    """
    Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle samples. Uses CRM-calibrated instrument and includes sample preservation information. Reference: OAPMetadata XSD variables.xsd - DIC_measured
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['MeasuredDICFields'],
         'slot_usage': {'analyzing_instrument': {'description': 'CRM-calibrated '
                                                                'instrument used to '
                                                                'analyze DIC samples.',
                                                 'name': 'analyzing_instrument',
                                                 'range': 'CRMInstrument'},
                        'variable_type': {'equals_string': 'dic',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    sample_preservation: SamplePreservation = Field(default=..., title="Sample preservation", description="""How the samples were preserved for analysis.""", json_schema_extra = { "linkml_meta": {'alias': 'sample_preservation',
         'domain_of': ['DiscreteTAVariable', 'DiscreteDICVariable']} })
    blank_correction: str = Field(default=..., title="Magnitude of blank correction", description="""Whether the reported variables were corrected for blank, and if so, how they were corrected.""", json_schema_extra = { "linkml_meta": {'alias': 'blank_correction',
         'domain_of': ['DiscreteTAVariable', 'DiscreteDICVariable']} })
    appropriate_use_quality: Optional[AppropriateUseQuality] = Field(default=None, title="Weather or climate quality", description="""Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.""", json_schema_extra = { "linkml_meta": {'alias': 'appropriate_use_quality',
         'domain_of': ['MeasuredTAFields',
                       'MeasuredDICFields',
                       'MeasuredPHFields',
                       'MeasuredCO2Fields']} })
    concentration_basis: ConcentrationBasis = Field(default=..., title="Per-volume vs per-mass based units", description="""Whether measurements are expressed per unit volume or per unit mass (for DIC, TA, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'concentration_basis',
         'domain_of': ['MeasuredTAFields', 'MeasuredDICFields']} })
    analyzing_instrument: CRMInstrument = Field(default=..., title="Analyzing instrument", description="""CRM-calibrated instrument used to analyze DIC samples.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["discrete"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'discrete'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["DiscreteDICVariable"] = Field(default="DiscreteDICVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["dic"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable'], 'equals_string': 'dic'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class ContinuousSedimentVariable(ContinuousMeasuredVariable, MeasuredSedimentFields):
    """
    Measured sediment variable collected from continuous autonomous sensor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['MeasuredSedimentFields'],
         'slot_usage': {'variable_type': {'equals_string': 'sediment',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    sediment_type: str = Field(default=..., title="Sediment Type", description="""e.g., mud, sand, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'sediment_type', 'domain_of': ['MeasuredSedimentFields']} })
    sediment_sampling_method: str = Field(default=..., title="Sediment Sampling Method", description="""e.g., sediment core, grab sampling, dredging, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'sediment_sampling_method', 'domain_of': ['MeasuredSedimentFields']} })
    sediment_sampling_depth: str = Field(default=..., title="Sediment Sampling Depth", description="""Depth that sediment was collected below sediment surface. If provided as a variable (recommended), please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'sediment_sampling_depth', 'domain_of': ['MeasuredSedimentFields']} })
    sediment_sampling_water_depth: str = Field(default=..., title="Sediment Sampling Water Depth", description="""Water depth where sediment was collected. If provided as a variable (recommended), please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'sediment_sampling_water_depth',
         'domain_of': ['MeasuredSedimentFields']} })
    raw_data_calculation_method: str = Field(default=..., title="Method to calculate reported values from raw data", description="""The method used to calculate reported values from raw sensor data.""", json_schema_extra = { "linkml_meta": {'alias': 'raw_data_calculation_method',
         'domain_of': ['ContinuousMeasuredVariable']} })
    calculation_software_version: Optional[str] = Field(default=None, title="Software version for the calculation", description="""Version of the software used to calculate reported values from raw values.""", json_schema_extra = { "linkml_meta": {'alias': 'calculation_software_version',
         'domain_of': ['ContinuousMeasuredVariable']} })
    analyzing_instrument: AnalyzingInstrument = Field(default=..., title="Analyzing instrument", description="""Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["continuous"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'continuous'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["ContinuousSedimentVariable"] = Field(default="ContinuousSedimentVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["sediment"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type',
         'domain_of': ['Variable'],
         'equals_string': 'sediment'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class DiscreteSedimentVariable(DiscreteMeasuredVariable, MeasuredSedimentFields):
    """
    Measured sediment variable collected from discrete bottle samples
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['MeasuredSedimentFields'],
         'slot_usage': {'variable_type': {'equals_string': 'sediment',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    sediment_type: str = Field(default=..., title="Sediment Type", description="""e.g., mud, sand, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'sediment_type', 'domain_of': ['MeasuredSedimentFields']} })
    sediment_sampling_method: str = Field(default=..., title="Sediment Sampling Method", description="""e.g., sediment core, grab sampling, dredging, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'sediment_sampling_method', 'domain_of': ['MeasuredSedimentFields']} })
    sediment_sampling_depth: str = Field(default=..., title="Sediment Sampling Depth", description="""Depth that sediment was collected below sediment surface. If provided as a variable (recommended), please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'sediment_sampling_depth', 'domain_of': ['MeasuredSedimentFields']} })
    sediment_sampling_water_depth: str = Field(default=..., title="Sediment Sampling Water Depth", description="""Water depth where sediment was collected. If provided as a variable (recommended), please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'sediment_sampling_water_depth',
         'domain_of': ['MeasuredSedimentFields']} })
    analyzing_instrument: AnalyzingInstrument = Field(default=..., title="Analyzing instrument", description="""Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["discrete"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'discrete'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["DiscreteSedimentVariable"] = Field(default="DiscreteSedimentVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["sediment"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type',
         'domain_of': ['Variable'],
         'equals_string': 'sediment'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class DiscreteCO2Variable(DiscreteMeasuredVariable, MeasuredCO2Fields):
    """
    CO2 discrete (bottle) measured variable (pCO2/fCO2). Reference: OAPMetadata XSD variables.xsd - co2_discrete
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['MeasuredCO2Fields'],
         'slot_usage': {'analyzing_instrument': {'description': 'CO2 gas detector with '
                                                                'standard gas '
                                                                'calibration.',
                                                 'name': 'analyzing_instrument',
                                                 'range': 'CO2GasDetector'},
                        'variable_type': {'equals_string': 'co2',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    storage_method: str = Field(default=..., title="Storage method", description="""How the samples were stored before the measurement.""", json_schema_extra = { "linkml_meta": {'alias': 'storage_method', 'domain_of': ['DiscreteCO2Variable']} })
    seawater_volume: Optional[float] = Field(default=None, title="Seawater volume (mL)", description="""Volume (in mL) of seawater in the flask.""", json_schema_extra = { "linkml_meta": {'alias': 'seawater_volume', 'domain_of': ['DiscreteCO2Variable']} })
    headspace_volume: Optional[float] = Field(default=None, title="Headspace volume (mL)", description="""Volume (in mL) of headspace (water displaced in the flask plus volume of the tubing).""", json_schema_extra = { "linkml_meta": {'alias': 'headspace_volume', 'domain_of': ['DiscreteCO2Variable']} })
    measurement_temperature: float = Field(default=..., title="Temperature of measurement (°C)", description="""Temperature at which the samples were analyzed in Celsius.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_temperature',
         'domain_of': ['DiscretePHVariable', 'DiscreteCO2Variable']} })
    appropriate_use_quality: Optional[AppropriateUseQuality] = Field(default=None, title="Weather or climate quality", description="""Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.""", json_schema_extra = { "linkml_meta": {'alias': 'appropriate_use_quality',
         'domain_of': ['MeasuredTAFields',
                       'MeasuredDICFields',
                       'MeasuredPHFields',
                       'MeasuredCO2Fields']} })
    pco2_reported_temperature: str = Field(default=..., title="Temperature at which pCO2 was reported", description="""In Celsius. The input could be a constant temperature value, or something like, in-situ temperature, temperature of analysis, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'pco2_reported_temperature', 'domain_of': ['MeasuredCO2Fields']} })
    water_vapor_correction_method: Optional[str] = Field(default=None, title="Water vapor correction method", description="""How the water vapor pressure inside the equilibrator was determined.""", json_schema_extra = { "linkml_meta": {'alias': 'water_vapor_correction_method', 'domain_of': ['MeasuredCO2Fields']} })
    temperature_correction_method: Optional[str] = Field(default=None, title="Temperature correction method", description="""How the temperature effect was corrected.""", json_schema_extra = { "linkml_meta": {'alias': 'temperature_correction_method',
         'domain_of': ['DiscretePHVariable', 'MeasuredCO2Fields']} })
    analyzing_instrument: CO2GasDetector = Field(default=..., title="Analyzing instrument", description="""CO2 gas detector with standard gas calibration.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["discrete"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'discrete'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["DiscreteCO2Variable"] = Field(default="DiscreteCO2Variable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["co2"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable'], 'equals_string': 'co2'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class ContinuousCO2Variable(ContinuousMeasuredVariable, MeasuredCO2Fields):
    """
    CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2). Reference: OAPMetadata XSD variables.xsd - co2_continuous
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['MeasuredCO2Fields'],
         'slot_usage': {'analyzing_instrument': {'description': 'CO2 gas detector with '
                                                                'standard gas '
                                                                'calibration for '
                                                                'continuous '
                                                                'measurements.',
                                                 'name': 'analyzing_instrument',
                                                 'range': 'ContinuousCO2GasDetector'},
                        'variable_type': {'equals_string': 'co2',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    equilibrator: Optional[CO2Equilibrator] = Field(default=None, title="Equilibrator", description="""Equilibrator used for CO2 measurement.""", json_schema_extra = { "linkml_meta": {'alias': 'equilibrator', 'domain_of': ['ContinuousCO2Variable']} })
    equilibrator_temperature_sensor: Optional[TemperatureSensor] = Field(default=None, title="Equilibrator temperature sensor", description="""Temperature sensor for the equilibrator.""", json_schema_extra = { "linkml_meta": {'alias': 'equilibrator_temperature_sensor',
         'domain_of': ['ContinuousCO2Variable']} })
    equilibrator_pressure_sensor: Optional[PressureSensor] = Field(default=None, title="Equilibrator pressure sensor", description="""Pressure sensor for the equilibrator.""", json_schema_extra = { "linkml_meta": {'alias': 'equilibrator_pressure_sensor',
         'domain_of': ['ContinuousCO2Variable']} })
    atmospheric_pressure_sensor: Optional[PressureSensor] = Field(default=None, title="Atmospheric pressure sensor", description="""Atmospheric pressure sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'atmospheric_pressure_sensor', 'domain_of': ['ContinuousCO2Variable']} })
    seawater_intake_location: str = Field(default=..., title="Location of seawater intake", description="""Whereabouts of the seawater intake.""", json_schema_extra = { "linkml_meta": {'alias': 'seawater_intake_location', 'domain_of': ['ContinuousCO2Variable']} })
    seawater_intake_depth: str = Field(default=..., title="Depth of seawater intake", description="""Water depth of the seawater intake.""", json_schema_extra = { "linkml_meta": {'alias': 'seawater_intake_depth', 'domain_of': ['ContinuousCO2Variable']} })
    drying_method: Optional[str] = Field(default=None, title="Drying method for CO2 gas", description="""The method used to dry the gas coming out of CO2 equilibrator, before it is pumped into the CO2 sensor.""", json_schema_extra = { "linkml_meta": {'alias': 'drying_method',
         'domain_of': ['MarineAirMeasurement', 'ContinuousCO2Variable']} })
    marine_air_measurement: Optional[MarineAirMeasurement] = Field(default=None, title="CO2 in marine air", description="""Information about CO2 measurements in marine air.""", json_schema_extra = { "linkml_meta": {'alias': 'marine_air_measurement', 'domain_of': ['ContinuousCO2Variable']} })
    appropriate_use_quality: Optional[AppropriateUseQuality] = Field(default=None, title="Weather or climate quality", description="""Climate quality is defined as measurements of quality sufficient to assess long term trends with a defined level of confidence. Weather quality is defined as measurements of quality sufficient to identify relative spatial patterns and short term variation.
For more details, refer to Newton J.A., Feely R. A., Jewett E. B., Williamson P. & Mathis J., 2015. Global Ocean Acidification Observing Network: Requirements and Governance Plan. Second Edition, GOA-ON, http://www.goa-on.org/docs/GOA-ON_plan_print.pdf.""", json_schema_extra = { "linkml_meta": {'alias': 'appropriate_use_quality',
         'domain_of': ['MeasuredTAFields',
                       'MeasuredDICFields',
                       'MeasuredPHFields',
                       'MeasuredCO2Fields']} })
    pco2_reported_temperature: str = Field(default=..., title="Temperature at which pCO2 was reported", description="""In Celsius. The input could be a constant temperature value, or something like, in-situ temperature, temperature of analysis, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'pco2_reported_temperature', 'domain_of': ['MeasuredCO2Fields']} })
    water_vapor_correction_method: Optional[str] = Field(default=None, title="Water vapor correction method", description="""How the water vapor pressure inside the equilibrator was determined.""", json_schema_extra = { "linkml_meta": {'alias': 'water_vapor_correction_method', 'domain_of': ['MeasuredCO2Fields']} })
    temperature_correction_method: Optional[str] = Field(default=None, title="Temperature correction method", description="""How the temperature effect was corrected.""", json_schema_extra = { "linkml_meta": {'alias': 'temperature_correction_method',
         'domain_of': ['DiscretePHVariable', 'MeasuredCO2Fields']} })
    raw_data_calculation_method: str = Field(default=..., title="Method to calculate reported values from raw data", description="""The method used to calculate reported values from raw sensor data.""", json_schema_extra = { "linkml_meta": {'alias': 'raw_data_calculation_method',
         'domain_of': ['ContinuousMeasuredVariable']} })
    calculation_software_version: Optional[str] = Field(default=None, title="Software version for the calculation", description="""Version of the software used to calculate reported values from raw values.""", json_schema_extra = { "linkml_meta": {'alias': 'calculation_software_version',
         'domain_of': ['ContinuousMeasuredVariable']} })
    analyzing_instrument: ContinuousCO2GasDetector = Field(default=..., title="Analyzing instrument", description="""CO2 gas detector with standard gas calibration for continuous measurements.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["continuous"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'continuous'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["ContinuousCO2Variable"] = Field(default="ContinuousCO2Variable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["co2"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable'], 'equals_string': 'co2'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class HPLCVariable(DiscreteMeasuredVariable):
    """
    HPLC (High-Performance Liquid Chromatography) measured variable for pigment analysis. Always measured, not calculated.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'slot_usage': {'variable_type': {'equals_string': 'hplc',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    hplc_lab: str = Field(default=..., title="HPLC Lab", description="""The name of the lab where the HPLC analysis was run (e.g., 'NASA_GSFC'""", json_schema_extra = { "linkml_meta": {'alias': 'hplc_lab', 'domain_of': ['HPLCVariable']} })
    hplc_lab_technician: Optional[str] = Field(default=None, title="HPLC Lab Technician", description="""Name and contact information for HPLC technician.""", json_schema_extra = { "linkml_meta": {'alias': 'hplc_lab_technician', 'domain_of': ['HPLCVariable']} })
    analyzing_instrument: AnalyzingInstrument = Field(default=..., title="Analyzing instrument", description="""Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["discrete"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'discrete'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["HPLCVariable"] = Field(default="HPLCVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["hplc"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type', 'domain_of': ['Variable'], 'equals_string': 'hplc'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class DiscretePhysiologicalVariable(DiscreteMeasuredVariable, MeasuredPhysiologicalFields):
    """
    Physiological response variable from discrete field samples (e.g., organism growth rates, calcification rates, gene expression from bottle or tissue samples collected in the field).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['MeasuredPhysiologicalFields'],
         'slot_usage': {'variable_type': {'equals_string': 'physiological',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    biological_subject: str = Field(default=..., title="Biological Subject", description="""Taxonomy (species, genus, or community) being studied (e.g., Crassostrea gigas, coral reef community).""", json_schema_extra = { "linkml_meta": {'alias': 'biological_subject', 'domain_of': ['MeasuredPhysiologicalFields']} })
    species_identification_code: Optional[str] = Field(default=None, title="Species Identification Code", description="""Species reference code from a taxonomic database (e.g., WoRMS AphiaID 140656, ITIS TSN 79861).""", json_schema_extra = { "linkml_meta": {'alias': 'species_identification_code',
         'domain_of': ['MeasuredPhysiologicalFields']} })
    taxonomic_code_system: Optional[TaxonomicCodeSystem] = Field(default=None, title="Taxonomic Code System", description="""Which taxonomic code system the identification code refers to.""", json_schema_extra = { "linkml_meta": {'alias': 'taxonomic_code_system', 'domain_of': ['MeasuredPhysiologicalFields']} })
    life_stage: Optional[LifeStage] = Field(default=None, title="Life Stage", description="""Life stage of the organism at time of measurement.""", json_schema_extra = { "linkml_meta": {'alias': 'life_stage', 'domain_of': ['MeasuredPhysiologicalFields']} })
    life_stage_custom: Optional[str] = Field(default=None, title="Life Stage (custom)", description="""Custom life stage description when \"other\" is selected.""", json_schema_extra = { "linkml_meta": {'alias': 'life_stage_custom', 'domain_of': ['MeasuredPhysiologicalFields']} })
    analyzing_instrument: AnalyzingInstrument = Field(default=..., title="Analyzing instrument", description="""Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["discrete"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'discrete'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["DiscretePhysiologicalVariable"] = Field(default="DiscretePhysiologicalVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["physiological"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type',
         'domain_of': ['Variable'],
         'equals_string': 'physiological'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class ContinuousPhysiologicalVariable(ContinuousMeasuredVariable, MeasuredPhysiologicalFields):
    """
    Physiological response variable from continuous autonomous field sensors (e.g., respiration rates from deployed oxygen consumption monitors, heart rate from bio-loggers).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Variable',
         'mixins': ['MeasuredPhysiologicalFields'],
         'slot_usage': {'variable_type': {'equals_string': 'physiological',
                                          'name': 'variable_type',
                                          'range': 'string'}}})

    biological_subject: str = Field(default=..., title="Biological Subject", description="""Taxonomy (species, genus, or community) being studied (e.g., Crassostrea gigas, coral reef community).""", json_schema_extra = { "linkml_meta": {'alias': 'biological_subject', 'domain_of': ['MeasuredPhysiologicalFields']} })
    species_identification_code: Optional[str] = Field(default=None, title="Species Identification Code", description="""Species reference code from a taxonomic database (e.g., WoRMS AphiaID 140656, ITIS TSN 79861).""", json_schema_extra = { "linkml_meta": {'alias': 'species_identification_code',
         'domain_of': ['MeasuredPhysiologicalFields']} })
    taxonomic_code_system: Optional[TaxonomicCodeSystem] = Field(default=None, title="Taxonomic Code System", description="""Which taxonomic code system the identification code refers to.""", json_schema_extra = { "linkml_meta": {'alias': 'taxonomic_code_system', 'domain_of': ['MeasuredPhysiologicalFields']} })
    life_stage: Optional[LifeStage] = Field(default=None, title="Life Stage", description="""Life stage of the organism at time of measurement.""", json_schema_extra = { "linkml_meta": {'alias': 'life_stage', 'domain_of': ['MeasuredPhysiologicalFields']} })
    life_stage_custom: Optional[str] = Field(default=None, title="Life Stage (custom)", description="""Custom life stage description when \"other\" is selected.""", json_schema_extra = { "linkml_meta": {'alias': 'life_stage_custom', 'domain_of': ['MeasuredPhysiologicalFields']} })
    raw_data_calculation_method: str = Field(default=..., title="Method to calculate reported values from raw data", description="""The method used to calculate reported values from raw sensor data.""", json_schema_extra = { "linkml_meta": {'alias': 'raw_data_calculation_method',
         'domain_of': ['ContinuousMeasuredVariable']} })
    calculation_software_version: Optional[str] = Field(default=None, title="Software version for the calculation", description="""Version of the software used to calculate reported values from raw values.""", json_schema_extra = { "linkml_meta": {'alias': 'calculation_software_version',
         'domain_of': ['ContinuousMeasuredVariable']} })
    analyzing_instrument: AnalyzingInstrument = Field(default=..., title="Analyzing instrument", description="""Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_instrument', 'domain_of': ['MeasuredVariable']} })
    sampling_method: str = Field(default=..., title="Sampling Method", description="""Method used to collect samples.""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_method', 'domain_of': ['MeasuredVariable']} })
    field_replicate_information: Optional[str] = Field(default=None, title="Field replicate information", description="""Repetition of sample collection and measurement, e.g., triplicate samples.""", json_schema_extra = { "linkml_meta": {'alias': 'field_replicate_information', 'domain_of': ['MeasuredVariable']} })
    analyzing_method: str = Field(default=..., title="Analyzing Method", description="""Additional information describing how the sample was analyzed. DOIs provided as applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'analyzing_method', 'domain_of': ['MeasuredVariable']} })
    observation_type: ObservationType = Field(default=..., title="Observation Type", json_schema_extra = { "linkml_meta": {'alias': 'observation_type', 'domain_of': ['MeasuredVariable']} })
    sampling: Literal["continuous"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling',
         'domain_of': ['MeasuredVariable'],
         'equals_string': 'continuous'} })
    sampling_instrument_type: SamplingInstrumentType = Field(default=..., title="Sampling instrument type", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type', 'domain_of': ['MeasuredVariable']} })
    sampling_instrument_type_custom: Optional[str] = Field(default=None, title="Sampling instrument type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'sampling_instrument_type_custom', 'domain_of': ['MeasuredVariable']} })
    qc_steps_taken: str = Field(default=..., title="QC steps taken", description="""Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.).
If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_steps_taken', 'domain_of': ['QCFields']} })
    uncertainty: str = Field(default=..., title="Uncertainty", description="""It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset.
If uncertainty is provided as a variable, please list the column header name here.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty',
         'domain_of': ['StandardGas', 'CO2GasDetector', 'QCFields']} })
    uncertainty_definition: str = Field(default=..., title="How was the uncertainty defined", description="""A description of the uncertainties involved in this method.""", json_schema_extra = { "linkml_meta": {'alias': 'uncertainty_definition', 'domain_of': ['QCFields']} })
    missing_value_indicators: str = Field(default=..., title="Missing value indicators", description="""The indicator used to represent missing values in the data file, e.g., -999, NaN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_value_indicators', 'domain_of': ['QCFields']} })
    qc_researcher: Optional[Person] = Field(default=None, title="Researcher who QCed this variable", description="""The name of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher', 'domain_of': ['QCFields']} })
    qc_researcher_institution: Optional[str] = Field(default=None, title="QC Researcher Institution", description="""The institution of the PI whose research team QCed this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'qc_researcher_institution', 'domain_of': ['QCFields']} })
    genesis: Literal["measured"] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'genesis',
         'domain_of': ['InSituVariable'],
         'equals_string': 'measured'} })
    dataset_variable_name_qc_flag: Optional[str] = Field(default=None, title="Dataset variable name (Quality Flag)", description="""If applicable, the column header name used for the quality control flag corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_qc_flag', 'domain_of': ['InSituVariable']} })
    dataset_variable_name_raw: Optional[str] = Field(default=None, title="Dataset variable name (raw)", description="""If applicable, the column header name used for the raw data corresponding to this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name_raw', 'domain_of': ['InSituVariable']} })
    method_reference: Optional[str] = Field(default=None, title="Method Reference", description="""Citation for the method used.""", json_schema_extra = { "linkml_meta": {'alias': 'method_reference', 'domain_of': ['Calibration', 'InSituVariable']} })
    measurement_researcher: Optional[Person] = Field(default=None, title="Researcher who measured the variable", description="""The name of the PI whose research team measured or derived this parameter.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_researcher', 'domain_of': ['InSituVariable']} })
    other_detailed_information: Optional[str] = Field(default=None, title="Other Detailed Information", description="""Any additional information about this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'other_detailed_information', 'domain_of': ['InSituVariable']} })
    units: str = Field(default=..., title="Unit", description="""Unit of measurement for this variable.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['Variable']} })
    schema_class: Literal["ContinuousPhysiologicalVariable"] = Field(default="ContinuousPhysiologicalVariable", description="""The schema class name for this variable (e.g., \"DiscretePHVariable\"). Auto-populated by the metadata builder.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_class', 'designates_type': True, 'domain_of': ['Variable']} })
    variable_type: Literal["physiological"] = Field(default=..., title="Variable Type", description="""High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use.""", json_schema_extra = { "linkml_meta": {'alias': 'variable_type',
         'domain_of': ['Variable'],
         'equals_string': 'physiological'} })
    standard_identifier: Optional[VocabularyItemReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'standard_identifier', 'domain_of': ['Variable']} })
    dataset_variable_name: str = Field(default=..., title="Dataset variable name", description="""The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_variable_name', 'domain_of': ['Variable']} })
    long_name: str = Field(default=..., title="Variable full name", description="""Full descriptive name of the variable.""", json_schema_extra = { "linkml_meta": {'alias': 'long_name', 'domain_of': ['Variable']} })


class Dataset(ConfiguredBaseModel):
    """
    Abstract base class for all dataset types. Contains fields common to both field/observational and model simulation datasets. Generally following guidelines & best practices as outlined in [science-on-schema.org](https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['schema:Dataset', 'dcat:Dataset'],
         'from_schema': 'Dataset',
         'slot_usage': {'description': {'description': 'The abstract of a dataset is a '
                                                       'brief summary that provides an '
                                                       "overview of the dataset's "
                                                       'content, purpose, and scope. '
                                                       'It is used to provide context '
                                                       'and background information to '
                                                       'users who are interested in '
                                                       'using the dataset. An abstract '
                                                       'may include information such '
                                                       "as the dataset's source, how "
                                                       'the data was collected or '
                                                       'generated, the variables or '
                                                       'attributes included in the '
                                                       'dataset, and any limitations '
                                                       'or restrictions on the use of '
                                                       'the data. It may also include '
                                                       'information on how the data '
                                                       'can be accessed or used.',
                                        'name': 'description',
                                        'range': 'string',
                                        'required': True},
                        'experiment_id': {'name': 'experiment_id', 'required': True},
                        'name': {'description': 'A brief descriptive sentence that '
                                                'summarizes the content of a dataset. '
                                                'Here is one example:\n'
                                                '"Dissolved inorganic carbon, total '
                                                'alkalinity, pH, temperature, salinity '
                                                'and other variables collected from '
                                                'profile and discrete sample '
                                                'observations using CTD, Niskin '
                                                'bottle, and other instruments from '
                                                'R/V Wecoma in the U.S. West Coast '
                                                'California Current System during the '
                                                '2011 West Coast Ocean Acidification '
                                                'Cruise (WCOA2011) from 2011-08-12 to '
                                                '2011-08-30"',
                                 'name': 'name',
                                 'range': 'string',
                                 'required': True,
                                 'title': 'Dataset Title'},
                        'project_id': {'name': 'project_id', 'required': True}}})

    name: str = Field(default=..., title="Dataset Title", description="""A brief descriptive sentence that summarizes the content of a dataset. Here is one example:
\"Dissolved inorganic carbon, total alkalinity, pH, temperature, salinity and other variables collected from profile and discrete sample observations using CTD, Niskin bottle, and other instruments from R/V Wecoma in the U.S. West Coast California Current System during the 2011 West Coast Ocean Acidification Cruise (WCOA2011) from 2011-08-12 to 2011-08-30\"""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., title="Description", description="""The abstract of a dataset is a brief summary that provides an overview of the dataset's content, purpose, and scope. It is used to provide context and background information to users who are interested in using the dataset. An abstract may include information such as the dataset's source, how the data was collected or generated, the variables or attributes included in the dataset, and any limitations or restrictions on the use of the data. It may also include information on how the data can be accessed or used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent'],
         'slot_uri': 'schema:description'} })
    project_id: str = Field(default=..., title="Project ID", description="""The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable.""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Project', 'Experiment', 'Dataset']} })
    experiment_id: str = Field(default=..., title="Experiment ID", description="""The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:
Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_id', 'domain_of': ['Experiment', 'Dataset']} })
    filenames: List[str] = Field(default=..., title="Filenames", min_length=1, json_schema_extra = { "linkml_meta": {'alias': 'filenames', 'domain_of': ['Dataset']} })
    dataset_type: DatasetType = Field(default=..., title="Dataset Type", description="""Selected controlled vocabularies for data types relevant to mCDR have been referenced from NASA's SeaBASS metadata system and are provided below, for additional data types of optical characteristics see the [SeaBASS controlled definitions list](https://seabass.gsfc.nasa.gov/wiki/metadataheaders#data_type). Additional data types have been included to meet the needs of mCDR field projects.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_type', 'domain_of': ['Dataset']} })
    dataset_type_custom: Optional[str] = Field(default=None, title="Dataset Type (Custom)", description="""Custom \"data type\" when an appropriate value is not found in the controlled vocabulary list for mCDR Data Type and the corresponding `data_type` field is set to \"other\".""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_type_custom', 'domain_of': ['Dataset']} })
    data_submitter: Person = Field(default=..., title="Data Submitter", json_schema_extra = { "linkml_meta": {'alias': 'data_submitter', 'domain_of': ['Dataset']} })
    author_list_for_citation: Optional[str] = Field(default=None, title="Author List (for citation)", description="""Author list in the format of Lastname1, Firstname1 Middlename1; Lastname2, Firstname2 Middlename2; ...""", json_schema_extra = { "linkml_meta": {'alias': 'author_list_for_citation', 'domain_of': ['Dataset']} })
    license: Optional[str] = Field(default=None, title="License", description="""Link a Dataset to its license to document legal constraints by adding a schema:license property. The guide recommends providing a URL that unambiguously identifies a specific version of the license used, but for many licenses it is hard to determine what that URL should be. Thus, we recommend that the license URL be drawn from the [SPDX license list](https://spdx.org/licenses/), which provides a curated list of licenses and their properties that is well maintained. For each SPDX entry, SPDX provides a canonical URL for the license (e.g., http://spdx.org/licenses/CC0-1.0), a unique licenseId (e.g., CC0-1.0), and other metadata about the license.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Dataset'], 'slot_uri': 'schema:license'} })
    fair_use_data_request: Optional[str] = Field(default=None, title="Fair Use Data Request", description="""A statement from the data producer regarding how this dataset should be used.""", json_schema_extra = { "linkml_meta": {'alias': 'fair_use_data_request', 'domain_of': ['Dataset']} })
    data_accessibility: DataAccessibility = Field(default=..., title="Data Accessibility", description="""Level of access to this dataset. Open Access data are freely available without restriction. Conditional Access data are available upon request, subject to review. Scheduled Access data will become openly available after a specified date.""", json_schema_extra = { "linkml_meta": {'alias': 'data_accessibility', 'domain_of': ['Dataset']} })


class FieldDataset(Dataset):
    """
    A field or observational dataset related to an OAE experiment. Contains fields specific to in-situ data collection such as platform information, calibration files, QC flags, and measured variables.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Dataset'})

    temporal_coverage: str = Field(default=..., title="Temporal Coverage", description="""Start date and end date (if known) of the project in ISO-8601 interval format (YYYY-MM-DD/YYY-MM-DD). If the end date is not known, use open-ended format YYYY-MM-DD/..""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_coverage',
         'domain_of': ['Project', 'ExternalProject', 'FieldDataset'],
         'slot_uri': 'schema:temporalCoverage'} })
    data_product_type: DataProductType = Field(default=..., title="Data Product Type", description="""\"Controlled vocabulary\" One of the three choices: (a) Originally collected dataset (e.g., a dataset collected from a research cruise or laboratory experiment), (b) Data compilation product (e.g., SOCAT, GLODAP), or (c) Derived product (e.g., gridded products, or model output).""", json_schema_extra = { "linkml_meta": {'alias': 'data_product_type', 'domain_of': ['FieldDataset']} })
    qc_flag_scheme: Optional[str] = Field(default=None, title="QC Flag Scheme", description="""Describe what the quality control flags stand for, e.g.,
  0 = interpolated or calculated data
  1 = not evaluated/quality unknown
  2 = acceptable
  3 = questionable
  4 = known bad
  6 = median of replicates
  9 = missing value\"""", json_schema_extra = { "linkml_meta": {'alias': 'qc_flag_scheme', 'domain_of': ['FieldDataset']} })
    platform_info: Platform = Field(default=..., title="Platform Information", json_schema_extra = { "linkml_meta": {'alias': 'platform_info', 'domain_of': ['FieldDataset']} })
    calibration_files: Optional[List[str]] = Field(default=None, title="Calibration Files (required if providing sensor data)", description="""A list of supplementary file names containing coefficients and techniques used to calibrate the instruments used in data collection. The named files can be found within the relevant documents folder accompanying the submitted data files.""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_files', 'domain_of': ['FieldDataset']} })
    variables: Optional[List[Union[Variable,NonMeasuredVariable,InSituVariable,MeasuredVariable,CalculatedVariable,SocioeconomicVariable,DiscreteMeasuredVariable,ContinuousMeasuredVariable,ContinuousPHVariable,ContinuousTAVariable,ContinuousDICVariable,ContinuousSedimentVariable,ContinuousCO2Variable,ContinuousPhysiologicalVariable,DiscretePHVariable,DiscreteTAVariable,DiscreteDICVariable,DiscreteSedimentVariable,DiscreteCO2Variable,HPLCVariable,DiscretePhysiologicalVariable]]] = Field(default=None, title="Variables", json_schema_extra = { "linkml_meta": {'alias': 'variables',
         'domain_of': ['FieldDataset'],
         'slot_uri': 'schema:variableMeasured'} })
    name: str = Field(default=..., title="Dataset Title", description="""A brief descriptive sentence that summarizes the content of a dataset. Here is one example:
\"Dissolved inorganic carbon, total alkalinity, pH, temperature, salinity and other variables collected from profile and discrete sample observations using CTD, Niskin bottle, and other instruments from R/V Wecoma in the U.S. West Coast California Current System during the 2011 West Coast Ocean Acidification Cruise (WCOA2011) from 2011-08-12 to 2011-08-30\"""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., title="Description", description="""The abstract of a dataset is a brief summary that provides an overview of the dataset's content, purpose, and scope. It is used to provide context and background information to users who are interested in using the dataset. An abstract may include information such as the dataset's source, how the data was collected or generated, the variables or attributes included in the dataset, and any limitations or restrictions on the use of the data. It may also include information on how the data can be accessed or used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent'],
         'slot_uri': 'schema:description'} })
    project_id: str = Field(default=..., title="Project ID", description="""The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable.""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Project', 'Experiment', 'Dataset']} })
    experiment_id: str = Field(default=..., title="Experiment ID", description="""The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:
Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_id', 'domain_of': ['Experiment', 'Dataset']} })
    filenames: List[str] = Field(default=..., title="Filenames", min_length=1, json_schema_extra = { "linkml_meta": {'alias': 'filenames', 'domain_of': ['Dataset']} })
    dataset_type: DatasetType = Field(default=..., title="Dataset Type", description="""Selected controlled vocabularies for data types relevant to mCDR have been referenced from NASA's SeaBASS metadata system and are provided below, for additional data types of optical characteristics see the [SeaBASS controlled definitions list](https://seabass.gsfc.nasa.gov/wiki/metadataheaders#data_type). Additional data types have been included to meet the needs of mCDR field projects.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_type', 'domain_of': ['Dataset']} })
    dataset_type_custom: Optional[str] = Field(default=None, title="Dataset Type (Custom)", description="""Custom \"data type\" when an appropriate value is not found in the controlled vocabulary list for mCDR Data Type and the corresponding `data_type` field is set to \"other\".""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_type_custom', 'domain_of': ['Dataset']} })
    data_submitter: Person = Field(default=..., title="Data Submitter", json_schema_extra = { "linkml_meta": {'alias': 'data_submitter', 'domain_of': ['Dataset']} })
    author_list_for_citation: Optional[str] = Field(default=None, title="Author List (for citation)", description="""Author list in the format of Lastname1, Firstname1 Middlename1; Lastname2, Firstname2 Middlename2; ...""", json_schema_extra = { "linkml_meta": {'alias': 'author_list_for_citation', 'domain_of': ['Dataset']} })
    license: Optional[str] = Field(default=None, title="License", description="""Link a Dataset to its license to document legal constraints by adding a schema:license property. The guide recommends providing a URL that unambiguously identifies a specific version of the license used, but for many licenses it is hard to determine what that URL should be. Thus, we recommend that the license URL be drawn from the [SPDX license list](https://spdx.org/licenses/), which provides a curated list of licenses and their properties that is well maintained. For each SPDX entry, SPDX provides a canonical URL for the license (e.g., http://spdx.org/licenses/CC0-1.0), a unique licenseId (e.g., CC0-1.0), and other metadata about the license.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Dataset'], 'slot_uri': 'schema:license'} })
    fair_use_data_request: Optional[str] = Field(default=None, title="Fair Use Data Request", description="""A statement from the data producer regarding how this dataset should be used.""", json_schema_extra = { "linkml_meta": {'alias': 'fair_use_data_request', 'domain_of': ['Dataset']} })
    data_accessibility: DataAccessibility = Field(default=..., title="Data Accessibility", description="""Level of access to this dataset. Open Access data are freely available without restriction. Conditional Access data are available upon request, subject to review. Scheduled Access data will become openly available after a specified date.""", json_schema_extra = { "linkml_meta": {'alias': 'data_accessibility', 'domain_of': ['Dataset']} })

    @field_validator('temporal_coverage')
    def pattern_temporal_coverage(cls, v):
        pattern=re.compile(r"^\d{4}-\d{2}-\d{2}/(\d{4}-\d{2}-\d{2}|\.\.)$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid temporal_coverage format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid temporal_coverage format: {v}")
        return v


class ModelOutputDataset(Dataset):
    """
    A model simulation output dataset. Contains fields specific to computational model output including simulation configuration, output variables, and hardware information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Dataset',
         'rules': [{'postconditions': {'slot_conditions': {'mcdr_forcing_description': {'name': 'mcdr_forcing_description',
                                                                                        'required': True}}},
                    'preconditions': {'slot_conditions': {'simulation_type': {'has_member': {'equals_string': 'perturbation'},
                                                                              'name': 'simulation_type'}}}}],
         'slot_usage': {'filenames': {'name': 'filenames',
                                      'title': 'Model Output Filenames'}}})

    simulation_type: List[SimulationType] = Field(default=..., title="Simulation Type", description="""The type(s) of model simulation (e.g., counterfactual, perturbation, or both).""", min_length=1, json_schema_extra = { "linkml_meta": {'alias': 'simulation_type', 'domain_of': ['ModelOutputDataset']} })
    start_datetime: datetime  = Field(default=..., title="Start Date and Time", description="""Start date and time of the simulation in UTC ISO-8601.""", json_schema_extra = { "linkml_meta": {'alias': 'start_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })
    end_datetime: datetime  = Field(default=..., title="End Date and Time", description="""End date and time of the simulation in UTC ISO-8601.""", json_schema_extra = { "linkml_meta": {'alias': 'end_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })
    output_frequency: Optional[str] = Field(default=None, title="Output Frequency", description="""Frequency of model output (e.g., 'hourly mean', 'daily mean').""", json_schema_extra = { "linkml_meta": {'alias': 'output_frequency', 'domain_of': ['ModelOutputDataset']} })
    mcdr_forcing_description: Optional[str] = Field(default=None, title="Description of mCDR Forcing", description="""Description of the mCDR forcing applied in the simulation (e.g., the alkalinity perturbation). Required when simulation_type is \"perturbation\".""", json_schema_extra = { "linkml_meta": {'alias': 'mcdr_forcing_description', 'domain_of': ['ModelOutputDataset']} })
    hardware_configuration: Optional[HardwareConfiguration] = Field(default=None, title="Hardware Configuration", description="""Details about the computational hardware used for the simulation.""", json_schema_extra = { "linkml_meta": {'alias': 'hardware_configuration', 'domain_of': ['ModelOutputDataset']} })
    model_output_variables: Optional[List[ModelOutputVariable]] = Field(default=None, title="Key Model Output Variables", description="""Checklist of variables included in the model simulation output.""", json_schema_extra = { "linkml_meta": {'alias': 'model_output_variables', 'domain_of': ['ModelOutputDataset']} })
    name: str = Field(default=..., title="Dataset Title", description="""A brief descriptive sentence that summarizes the content of a dataset. Here is one example:
\"Dissolved inorganic carbon, total alkalinity, pH, temperature, salinity and other variables collected from profile and discrete sample observations using CTD, Niskin bottle, and other instruments from R/V Wecoma in the U.S. West Coast California Current System during the 2011 West Coast Ocean Acidification Cruise (WCOA2011) from 2011-08-12 to 2011-08-30\"""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., title="Description", description="""The abstract of a dataset is a brief summary that provides an overview of the dataset's content, purpose, and scope. It is used to provide context and background information to users who are interested in using the dataset. An abstract may include information such as the dataset's source, how the data was collected or generated, the variables or attributes included in the dataset, and any limitations or restrictions on the use of the data. It may also include information on how the data can be accessed or used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent'],
         'slot_uri': 'schema:description'} })
    project_id: str = Field(default=..., title="Project ID", description="""The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable.""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Project', 'Experiment', 'Dataset']} })
    experiment_id: str = Field(default=..., title="Experiment ID", description="""The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:
Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_id', 'domain_of': ['Experiment', 'Dataset']} })
    filenames: List[str] = Field(default=..., title="Model Output Filenames", min_length=1, json_schema_extra = { "linkml_meta": {'alias': 'filenames', 'domain_of': ['Dataset']} })
    dataset_type: DatasetType = Field(default=..., title="Dataset Type", description="""Selected controlled vocabularies for data types relevant to mCDR have been referenced from NASA's SeaBASS metadata system and are provided below, for additional data types of optical characteristics see the [SeaBASS controlled definitions list](https://seabass.gsfc.nasa.gov/wiki/metadataheaders#data_type). Additional data types have been included to meet the needs of mCDR field projects.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_type', 'domain_of': ['Dataset']} })
    dataset_type_custom: Optional[str] = Field(default=None, title="Dataset Type (Custom)", description="""Custom \"data type\" when an appropriate value is not found in the controlled vocabulary list for mCDR Data Type and the corresponding `data_type` field is set to \"other\".""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_type_custom', 'domain_of': ['Dataset']} })
    data_submitter: Person = Field(default=..., title="Data Submitter", json_schema_extra = { "linkml_meta": {'alias': 'data_submitter', 'domain_of': ['Dataset']} })
    author_list_for_citation: Optional[str] = Field(default=None, title="Author List (for citation)", description="""Author list in the format of Lastname1, Firstname1 Middlename1; Lastname2, Firstname2 Middlename2; ...""", json_schema_extra = { "linkml_meta": {'alias': 'author_list_for_citation', 'domain_of': ['Dataset']} })
    license: Optional[str] = Field(default=None, title="License", description="""Link a Dataset to its license to document legal constraints by adding a schema:license property. The guide recommends providing a URL that unambiguously identifies a specific version of the license used, but for many licenses it is hard to determine what that URL should be. Thus, we recommend that the license URL be drawn from the [SPDX license list](https://spdx.org/licenses/), which provides a curated list of licenses and their properties that is well maintained. For each SPDX entry, SPDX provides a canonical URL for the license (e.g., http://spdx.org/licenses/CC0-1.0), a unique licenseId (e.g., CC0-1.0), and other metadata about the license.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Dataset'], 'slot_uri': 'schema:license'} })
    fair_use_data_request: Optional[str] = Field(default=None, title="Fair Use Data Request", description="""A statement from the data producer regarding how this dataset should be used.""", json_schema_extra = { "linkml_meta": {'alias': 'fair_use_data_request', 'domain_of': ['Dataset']} })
    data_accessibility: DataAccessibility = Field(default=..., title="Data Accessibility", description="""Level of access to this dataset. Open Access data are freely available without restriction. Conditional Access data are available upon request, subject to review. Scheduled Access data will become openly available after a specified date.""", json_schema_extra = { "linkml_meta": {'alias': 'data_accessibility', 'domain_of': ['Dataset']} })


class HardwareConfiguration(ConfiguredBaseModel):
    """
    Details about the computational hardware used to run a model simulation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Dataset'})

    machine: Optional[str] = Field(default=None, title="Machine", description="""Name of the machine or cluster (e.g., 'Perlmutter').""", json_schema_extra = { "linkml_meta": {'alias': 'machine', 'domain_of': ['HardwareConfiguration']} })
    operating_system: Optional[str] = Field(default=None, title="Operating System", description="""Operating system used (e.g., 'Linux').""", json_schema_extra = { "linkml_meta": {'alias': 'operating_system', 'domain_of': ['HardwareConfiguration']} })
    cpu_gpu_details: Optional[str] = Field(default=None, title="CPU/GPU Details", description="""Details about CPU/GPU hardware or link to specifications.""", json_schema_extra = { "linkml_meta": {'alias': 'cpu_gpu_details', 'domain_of': ['HardwareConfiguration']} })
    memory: Optional[str] = Field(default=None, title="Memory", description="""Memory available (e.g., '512 GB DDR4').""", json_schema_extra = { "linkml_meta": {'alias': 'memory', 'domain_of': ['HardwareConfiguration']} })
    storage: Optional[str] = Field(default=None, title="Storage", description="""Storage available (e.g., '44 PB').""", json_schema_extra = { "linkml_meta": {'alias': 'storage', 'domain_of': ['HardwareConfiguration']} })
    parallelization: Optional[str] = Field(default=None, title="Parallelization", description="""Parallelization details (e.g., '3 nodes, 108 ntasks per node').""", json_schema_extra = { "linkml_meta": {'alias': 'parallelization', 'domain_of': ['HardwareConfiguration']} })


class Platform(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Platform',
         'slot_usage': {'name': {'description': 'Name of the observing platform, e.g., '
                                                'RV Ronald Brown, Saildrone#0132, '
                                                'Mooring_First_Landing, etc.',
                                 'name': 'name'}}})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the observing platform, e.g., RV Ronald Brown, Saildrone#0132, Mooring_First_Landing, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent'],
         'slot_uri': 'schema:name'} })
    platform_type: PlatformType = Field(default=..., title="Platform Type", description="""Controlled vocabularies for the types of the platform: https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/vocabularies/platform-types.html""", json_schema_extra = { "linkml_meta": {'alias': 'platform_type', 'domain_of': ['Platform']} })
    platform_id: Optional[str] = Field(default=None, title="Platform ID", description="""Synonymous with glider ID, cruise ID. A unique name assigned to oceanographic assets such as buoys, moorings, floats, drifters, towed vehicles like the Scanfish or StingRay. This is synonymous with the BCO-DMO “platform” parameter (https://www.bco-dmo.org/parameter/932), NERC “platform type” term (https://vocab.nerc.ac.uk/collection/W06/current/CLSS0001/), and the “platform_id” term within the Climate and Forecast (CF) metadata conventions (https://cfconventions.org/Data/cf-standard-names/current/build/cf-standard-name-table.html). e.g., ICES platform code (e.g., 33RO).""", json_schema_extra = { "linkml_meta": {'alias': 'platform_id', 'domain_of': ['Platform']} })
    owner: Optional[str] = Field(default=None, title="Owner", description="""Institution that owns the platform.""", json_schema_extra = { "linkml_meta": {'alias': 'owner', 'domain_of': ['Platform']} })
    country: Optional[str] = Field(default=None, title="Country", description="""Country to which the platform belongs.""", json_schema_extra = { "linkml_meta": {'alias': 'country', 'domain_of': ['Organization', 'Platform']} })


class Model(Experiment):
    """
    A computational model experiment related to OAE.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Model'})

    model_configuration: Optional[List[str]] = Field(default=None, title="Model Configuration", description="""Links to model configuration files or documentation.""", json_schema_extra = { "linkml_meta": {'alias': 'model_configuration', 'domain_of': ['Model']} })
    model_components: Optional[List[ModelComponent]] = Field(default=None, title="Model Components", description="""Components of the model (e.g., physics, biogeochemistry).""", json_schema_extra = { "linkml_meta": {'alias': 'model_components', 'domain_of': ['Model']} })
    grid_details: Optional[List[ModelGrid]] = Field(default=None, title="Grid Details", description="""Details about the model grid(s). Use multiple entries for nested grid configurations.""", json_schema_extra = { "linkml_meta": {'alias': 'grid_details', 'domain_of': ['Model']} })
    spin_up_protocol: Optional[str] = Field(default=None, title="Spin-up Protocol", description="""Description of the model spin-up process.""", json_schema_extra = { "linkml_meta": {'alias': 'spin_up_protocol', 'domain_of': ['Model']} })
    time_stepping_scheme: Optional[str] = Field(default=None, title="Time-stepping Scheme", description="""Time-stepping method and time step used in the simulation.""", json_schema_extra = { "linkml_meta": {'alias': 'time_stepping_scheme', 'domain_of': ['Model']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Optional common name for experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., title="Experiment Description", description="""A narrative description of the experiment. For example, what part of the project do these data represent (e.g., baseline, intervention, control) and what do they contribute to the overall project? Are all project research questions listed in Project description relevant? What were the processes to achieve these goals and answer these questions? Data submitters are encouraged to note any significant changes to the original experimental plan due to unforeseen circumstances here.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent'],
         'slot_uri': 'schema:description'} })
    spatial_coverage: SpatialCoverage = Field(default=..., title="Spatial Coverage", description="""Latitude/longitude bounds of observed data in experiment, expressed as a schema.org GeoShape bounding box.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_coverage',
         'domain_of': ['Project', 'ExternalProject', 'Experiment', 'ModelGrid'],
         'slot_uri': 'schema:spatialCoverage'} })
    project_id: str = Field(default=..., title="Project ID", description="""The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example.
If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location.
Any method that creates a unique ID that will link all project data is acceptable.""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Project', 'Experiment', 'Dataset']} })
    experiment_id: str = Field(default=..., title="Experiment ID", description="""The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is:
Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_id', 'domain_of': ['Experiment', 'Dataset']} })
    experiment_types: List[ExperimentType] = Field(default=..., title="mCDR Experiment Type(s)", description="""The type(s) of mCDR experiment conducted. See Controlled Vocabularies section for definitions.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_types', 'domain_of': ['Experiment']} })
    public_comments: Optional[str] = Field(default=None, title="Public Comments", description="""File name(s) of public comment related documents. If possible, please provide public comments concatenated into a single pdf""", json_schema_extra = { "linkml_meta": {'alias': 'public_comments', 'domain_of': ['Experiment'], 'recommended': True} })
    experiment_leads: List[Person] = Field(default=..., title="Experiment Lead(s)", description="""Provide details for each experiment lead / principal investigator (PI) including: Name, institutional information (name, address), phone, email, ID type (e.g., ORCID, etc), researcher ID, and role.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_leads', 'domain_of': ['Experiment']} })
    start_datetime: datetime  = Field(default=..., title="Start Date and Time (UTC)", description="""Start date and time of experiment in UTC ISO-8601""", json_schema_extra = { "linkml_meta": {'alias': 'start_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })
    end_datetime: Optional[datetime ] = Field(default=None, title="End Date and Time (UTC)", description="""End date and time of experiment in UTC ISO-8601""", json_schema_extra = { "linkml_meta": {'alias': 'end_datetime', 'domain_of': ['Experiment', 'ModelOutputDataset']} })


class ModelComponent(ConfiguredBaseModel):
    """
    A component of a model (e.g., physics, biogeochemistry/ecosystem).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Model',
         'rules': [{'postconditions': {'slot_conditions': {'model_component_type_custom': {'name': 'model_component_type_custom',
                                                                                           'required': True}}},
                    'preconditions': {'slot_conditions': {'model_component_type': {'equals_string': 'other',
                                                                                   'name': 'model_component_type'}}}}],
         'slot_usage': {'description': {'description': 'A description of the model '
                                                       'component characteristics.\n'
                                                       'For physics components, this '
                                                       'should include the version of '
                                                       'equations being solved '
                                                       '(hydrostatic vs '
                                                       'non-hydrostatic), tracer '
                                                       'advection scheme, how bottom '
                                                       'drag is represented, mixed '
                                                       'layer parameterizations, '
                                                       'sub-grid mixing '
                                                       'parameterizations if '
                                                       'applicable, etc.\n'
                                                       'For BGC components, this '
                                                       'should include details of '
                                                       'which parameters are modeled '
                                                       'explicitly, derived carbonate '
                                                       'system parameters, advection '
                                                       'scheme for biological tracers, '
                                                       'CO₂ solver protocol (e.g., '
                                                       'CO₂SYS), links to data/code '
                                                       'with biological model '
                                                       'parameters (e.g., growth and '
                                                       'mortality rates), etc. '
                                                       'Equations for each explicitly '
                                                       'modeled parameter should be '
                                                       'provided (can be links to '
                                                       'publications), and it should '
                                                       'be noted if any equations or '
                                                       'parameter values (e.g. growth '
                                                       'rates) were modified. '
                                                       'Description and/or references '
                                                       'of air-sea CO₂ flux '
                                                       'parameterization used, gas '
                                                       'transfer velocity formulation '
                                                       'and atmospheric CO₂ details '
                                                       '(e.g., fixed or time varying, '
                                                       'and if time varying which data '
                                                       'were used). Also include '
                                                       'details on whether dissolution '
                                                       'and precipitation of calcium '
                                                       'carbonate are considered, how '
                                                       'exchanges between sediment and '
                                                       'overlying water are '
                                                       'represented (if applicable), '
                                                       'and whether active feedbacks '
                                                       'between biological processes '
                                                       'and the carbonate system are '
                                                       'represented.\n'
                                                       'Associated links to data, '
                                                       'DOIs, or publications can be '
                                                       'noted here, but should be '
                                                       'supplemental.',
                                        'name': 'description',
                                        'title': 'Model Component Description'}}})

    description: Optional[str] = Field(default=None, title="Model Component Description", description="""A description of the model component characteristics.
For physics components, this should include the version of equations being solved (hydrostatic vs non-hydrostatic), tracer advection scheme, how bottom drag is represented, mixed layer parameterizations, sub-grid mixing parameterizations if applicable, etc.
For BGC components, this should include details of which parameters are modeled explicitly, derived carbonate system parameters, advection scheme for biological tracers, CO₂ solver protocol (e.g., CO₂SYS), links to data/code with biological model parameters (e.g., growth and mortality rates), etc. Equations for each explicitly modeled parameter should be provided (can be links to publications), and it should be noted if any equations or parameter values (e.g. growth rates) were modified. Description and/or references of air-sea CO₂ flux parameterization used, gas transfer velocity formulation and atmospheric CO₂ details (e.g., fixed or time varying, and if time varying which data were used). Also include details on whether dissolution and precipitation of calcium carbonate are considered, how exchanges between sediment and overlying water are represented (if applicable), and whether active feedbacks between biological processes and the carbonate system are represented.
Associated links to data, DOIs, or publications can be noted here, but should be supplemental.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Project',
                       'ExternalProject',
                       'Experiment',
                       'VocabularyItemReference',
                       'Dataset',
                       'ModelComponent'],
         'slot_uri': 'schema:description'} })
    model_component_type: ModelComponentType = Field(default=..., title="Model Component Type", description="""The type of model component (physics, BGC/ecosystem, or other).""", json_schema_extra = { "linkml_meta": {'alias': 'model_component_type', 'domain_of': ['ModelComponent']} })
    model_component_type_custom: Optional[str] = Field(default=None, title="Model Component Type (custom)", json_schema_extra = { "linkml_meta": {'alias': 'model_component_type_custom', 'domain_of': ['ModelComponent']} })
    name: str = Field(default=..., title="Component Name", description="""Name of the model component (e.g., ROMS, MARBL, Oceananigans).""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Organization',
                       'NamedLink',
                       'ExternalProject',
                       'MonetaryGrant',
                       'Experiment',
                       'Person',
                       'Dataset',
                       'Platform',
                       'ModelComponent']} })
    version: Optional[str] = Field(default=None, title="Version", description="""Release version of the model component.""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['ModelComponent', 'Container']} })
    codebase: Optional[str] = Field(default=None, title="Codebase", description="""Link to model code repository.""", json_schema_extra = { "linkml_meta": {'alias': 'codebase', 'domain_of': ['ModelComponent']} })
    references: Optional[List[str]] = Field(default=None, title="References", description="""Links or DOIs to any reference(s) relevant to the model components/development, specific model configuration, model validation etc.""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['ModelComponent']} })


class ModelGrid(ConfiguredBaseModel):
    """
    Details about a model grid. Use multiple ModelGrid entries to describe nested or multi-grid configurations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Model'})

    grid_name: Optional[str] = Field(default=None, title="Grid Name", description="""Name of the grid (e.g., 'inner grid', 'L1', 'global').""", json_schema_extra = { "linkml_meta": {'alias': 'grid_name', 'domain_of': ['ModelGrid']} })
    grid_geometry: Optional[str] = Field(default=None, title="Grid Geometry", description="""Descriptive structure of the grid (e.g., latitude-longitude, unstructured triangular, tripolar).""", json_schema_extra = { "linkml_meta": {'alias': 'grid_geometry', 'domain_of': ['ModelGrid']} })
    grid_type: GridType = Field(default=..., title="Grid Type", description="""Role of this grid in a nested or multi-grid configuration.""", json_schema_extra = { "linkml_meta": {'alias': 'grid_type', 'domain_of': ['ModelGrid']} })
    region: Optional[str] = Field(default=None, title="Region", description="""Region covered by the grid.""", json_schema_extra = { "linkml_meta": {'alias': 'region', 'domain_of': ['ModelGrid']} })
    spatial_coverage: Optional[SpatialCoverage] = Field(default=None, title="Spatial Coverage", description="""Bounding box for this grid, expressed as a schema.org GeoShape bounding box.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_coverage',
         'domain_of': ['Project', 'ExternalProject', 'Experiment', 'ModelGrid']} })
    arrangement: Optional[str] = Field(default=None, title="Arrangement", description="""The grid arrangement of orthogonal physical quantities (e.g., Arakawa A, Arakawa B, Arakawa C).""", json_schema_extra = { "linkml_meta": {'alias': 'arrangement', 'domain_of': ['ModelGrid']} })
    vertical_coordinate_type: Optional[str] = Field(default=None, title="Vertical coordinate type", description="""The vertical grid coordinate type (e.g. z-coordinate, z*-coordinate, terrain-following coordinate, isopycnal coordinate)""", json_schema_extra = { "linkml_meta": {'alias': 'vertical_coordinate_type', 'domain_of': ['ModelGrid']} })
    n_x: Optional[int] = Field(default=None, title="Nx", description="""Number of grid points in the x-direction.""", json_schema_extra = { "linkml_meta": {'alias': 'n_x', 'domain_of': ['ModelGrid']} })
    n_y: Optional[int] = Field(default=None, title="Ny", description="""Number of grid points in the y-direction.""", json_schema_extra = { "linkml_meta": {'alias': 'n_y', 'domain_of': ['ModelGrid']} })
    n_z: Optional[int] = Field(default=None, title="Nz", description="""Number of vertical coordinate levels.""", json_schema_extra = { "linkml_meta": {'alias': 'n_z', 'domain_of': ['ModelGrid']} })
    n_nodes: Optional[int] = Field(default=None, title="N nodes", description="""Number of nodes in the grid (for unstructured grids).""", json_schema_extra = { "linkml_meta": {'alias': 'n_nodes', 'domain_of': ['ModelGrid']} })
    horizontal_resolution_range: Optional[str] = Field(default=None, title="Horizontal Resolution Range", description="""Description of horizontal resolution (e.g., '3.3 km', '1/12 degree').""", json_schema_extra = { "linkml_meta": {'alias': 'horizontal_resolution_range', 'domain_of': ['ModelGrid']} })
    vertical_resolution_range: Optional[str] = Field(default=None, title="Vertical Resolution Range", description="""Description of vertical resolution (e.g., 'Max. 4 m near surface, stretching to 500 m at depth').""", json_schema_extra = { "linkml_meta": {'alias': 'vertical_resolution_range', 'domain_of': ['ModelGrid']} })
    input_details: Optional[ModelInputDetails] = Field(default=None, title="Input Details", description="""Details about input data sources used to drive the model on this grid.""", json_schema_extra = { "linkml_meta": {'alias': 'input_details', 'domain_of': ['ModelGrid']} })


class ModelInputDetails(ConfiguredBaseModel):
    """
    Details about input data sources used to drive the model.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'Model'})

    bathymetry: Optional[List[NamedLink]] = Field(default=None, title="Bathymetry", description="""Bathymetry data source(s).""", json_schema_extra = { "linkml_meta": {'alias': 'bathymetry', 'domain_of': ['ModelInputDetails']} })
    initial_conditions: Optional[List[NamedLink]] = Field(default=None, title="Initial Conditions", description="""Initial condition data source(s).""", json_schema_extra = { "linkml_meta": {'alias': 'initial_conditions', 'domain_of': ['ModelInputDetails']} })
    boundary_conditions: Optional[List[NamedLink]] = Field(default=None, title="Boundary Conditions", description="""Boundary condition data source(s).""", json_schema_extra = { "linkml_meta": {'alias': 'boundary_conditions', 'domain_of': ['ModelInputDetails']} })
    atmospheric_forcing: Optional[List[NamedLink]] = Field(default=None, title="Atmospheric Forcing", description="""Atmospheric forcing data source(s).""", json_schema_extra = { "linkml_meta": {'alias': 'atmospheric_forcing', 'domain_of': ['ModelInputDetails']} })
    tidal_forcing: Optional[List[NamedLink]] = Field(default=None, title="Tidal Forcing", description="""Tidal forcing data source(s).""", json_schema_extra = { "linkml_meta": {'alias': 'tidal_forcing', 'domain_of': ['ModelInputDetails']} })
    river_sediment_flux_details: Optional[List[NamedLink]] = Field(default=None, title="River/Sediment Flux Details", description="""River and/or sediment flux data source(s).""", json_schema_extra = { "linkml_meta": {'alias': 'river_sediment_flux_details', 'domain_of': ['ModelInputDetails']} })
    processing_of_input_data: Optional[str] = Field(default=None, title="Processing of Input Data", description="""Narrative description of any processing applied to input data before use in the model.""", json_schema_extra = { "linkml_meta": {'alias': 'processing_of_input_data', 'domain_of': ['ModelInputDetails']} })
    processing_code: Optional[List[NamedLink]] = Field(default=None, title="Processing code", description="""If applicable, link to any code for processing of raw forcing and input data listed in the fields above.""", json_schema_extra = { "linkml_meta": {'alias': 'processing_code', 'domain_of': ['ModelInputDetails']} })


class Container(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://schema.oaedata.org/OAEDataSchema', 'tree_root': True})

    project: Optional[Project] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'project', 'domain_of': ['Container']} })
    experiments: Optional[List[Experiment]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'experiments', 'domain_of': ['Project', 'Container']} })
    datasets: Optional[List[Dataset]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'datasets', 'domain_of': ['Container']} })
    version: Optional[str] = Field(default=None, description="""Version of the oae-data-protocol""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['ModelComponent', 'Container']} })
    protocol_git_hash: Optional[str] = Field(default=None, description="""Git commit hash of the oae-data-protocol""", json_schema_extra = { "linkml_meta": {'alias': 'protocol_git_hash', 'domain_of': ['Container']} })
    metadata_builder_git_hash: Optional[str] = Field(default=None, description="""Git commit hash of the metadata-builder UI""", json_schema_extra = { "linkml_meta": {'alias': 'metadata_builder_git_hash', 'domain_of': ['Container']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
PropertyValue.model_rebuild()
Place.model_rebuild()
SpatialCoverage.model_rebuild()
DosingLocation.model_rebuild()
GeoShape.model_rebuild()
GeoCoordinates.model_rebuild()
VerticalExtent.model_rebuild()
Organization.model_rebuild()
Project.model_rebuild()
NamedLink.model_rebuild()
ExternalProject.model_rebuild()
MonetaryGrant.model_rebuild()
Permit.model_rebuild()
Experiment.model_rebuild()
InSituExperiment.model_rebuild()
InterventionDetails.model_rebuild()
TracerDetails.model_rebuild()
DosingConcentration.model_rebuild()
DosingDetails.model_rebuild()
Intervention.model_rebuild()
Tracer.model_rebuild()
InterventionWithTracer.model_rebuild()
Person.model_rebuild()
Calibration.model_rebuild()
CRMCalibration.model_rebuild()
PHCalibration.model_rebuild()
CO2Calibration.model_rebuild()
DiscreteCO2Calibration.model_rebuild()
ContinuousCO2Calibration.model_rebuild()
StandardGas.model_rebuild()
ContinuousStandardGas.model_rebuild()
AnalyzingInstrument.model_rebuild()
PHInstrument.model_rebuild()
CRMInstrument.model_rebuild()
CO2GasDetector.model_rebuild()
ContinuousCO2GasDetector.model_rebuild()
CO2Equilibrator.model_rebuild()
GenericSensor.model_rebuild()
TemperatureSensor.model_rebuild()
PressureSensor.model_rebuild()
MarineAirMeasurement.model_rebuild()
Variable.model_rebuild()
NonMeasuredVariable.model_rebuild()
InSituVariable.model_rebuild()
SocioeconomicVariable.model_rebuild()
SamplePreservation.model_rebuild()
VocabularyItemReference.model_rebuild()
MeasuredTAFields.model_rebuild()
MeasuredDICFields.model_rebuild()
MeasuredPHFields.model_rebuild()
MeasuredSedimentFields.model_rebuild()
MeasuredPhysiologicalFields.model_rebuild()
MeasuredCO2Fields.model_rebuild()
QCFields.model_rebuild()
MeasuredVariable.model_rebuild()
DiscreteMeasuredVariable.model_rebuild()
ContinuousMeasuredVariable.model_rebuild()
CalculatedVariable.model_rebuild()
ContinuousPHVariable.model_rebuild()
DiscretePHVariable.model_rebuild()
ContinuousTAVariable.model_rebuild()
DiscreteTAVariable.model_rebuild()
ContinuousDICVariable.model_rebuild()
DiscreteDICVariable.model_rebuild()
ContinuousSedimentVariable.model_rebuild()
DiscreteSedimentVariable.model_rebuild()
DiscreteCO2Variable.model_rebuild()
ContinuousCO2Variable.model_rebuild()
HPLCVariable.model_rebuild()
DiscretePhysiologicalVariable.model_rebuild()
ContinuousPhysiologicalVariable.model_rebuild()
Dataset.model_rebuild()
FieldDataset.model_rebuild()
ModelOutputDataset.model_rebuild()
HardwareConfiguration.model_rebuild()
Platform.model_rebuild()
Model.model_rebuild()
ModelComponent.model_rebuild()
ModelGrid.model_rebuild()
ModelInputDetails.model_rebuild()
Container.model_rebuild()

