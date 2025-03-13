# Auto generated from oae_data_protocol.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-12T16:45:29
# Schema: OAEDataManagementProtocol
#
# id: OAEDataManagementProtocol
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Datetime, Decimal, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Decimal, URI, XSDDateTime

metamodel_version = "1.7.0"
version = "0.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PUBCHEM = CurieNamespace('PUBCHEM', 'https://pubchem.ncbi.nlm.nih.gov/compound/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
ENVTHES = CurieNamespace('envthes', 'https://w3id.org/envthes/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OAE = CurieNamespace('oae', 'https://example.org/oae#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = OAE


# Types
class Doi(str):
    """ A Digital Object Identifier (DOI) for a digital object such as a document, dataset, or software package. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Doi"
    type_model_uri = OAE.Doi


# Class references
class OAEProjectProjectId(extended_str):
    pass


class ExperimentExperimentId(extended_str):
    pass


class InterventionExperimentId(ExperimentExperimentId):
    pass


class ModelSimulationExperimentId(ExperimentExperimentId):
    pass


class PropertyValue(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["PropertyValue"]
    class_class_curie: ClassVar[str] = "schema:PropertyValue"
    class_name: ClassVar[str] = "PropertyValue"
    class_model_uri: ClassVar[URIRef] = OAE.PropertyValue


Any = Any

@dataclass(repr=False)
class OAEProject(YAMLRoot):
    """
    A project conducting OAE field trials or modeling.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["OAEProject"]
    class_class_curie: ClassVar[str] = "oae:OAEProject"
    class_name: ClassVar[str] = "OAEProject"
    class_model_uri: ClassVar[URIRef] = OAE.OAEProject

    project_id: Union[str, OAEProjectProjectId] = None
    description: Optional[str] = None
    mcdr_pathway: Optional[Union[str, "MCDRPathway"]] = None
    site_description: Optional[str] = None
    permit_info: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.project_id):
            self.MissingRequiredField("project_id")
        if not isinstance(self.project_id, OAEProjectProjectId):
            self.project_id = OAEProjectProjectId(self.project_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.mcdr_pathway is not None and not isinstance(self.mcdr_pathway, MCDRPathway):
            self.mcdr_pathway = MCDRPathway(self.mcdr_pathway)

        if self.site_description is not None and not isinstance(self.site_description, str):
            self.site_description = str(self.site_description)

        if self.permit_info is not None and not isinstance(self.permit_info, str):
            self.permit_info = str(self.permit_info)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A dataset related to an OAE experiment. Generally following guidelines & best practices as outlined in
    [science-on-schema.org](https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Dataset"]
    class_class_curie: ClassVar[str] = "oae:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = OAE.Dataset

    description: Optional[str] = None
    name: Optional[str] = None
    identifier: Optional[str] = None
    url: Optional[str] = None
    temporal_coverage: Optional[str] = None
    spatial_coverage: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.temporal_coverage is not None and not isinstance(self.temporal_coverage, str):
            self.temporal_coverage = str(self.temporal_coverage)

        if self.spatial_coverage is not None and not isinstance(self.spatial_coverage, str):
            self.spatial_coverage = str(self.spatial_coverage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Experiment(YAMLRoot):
    """
    A single experiment conducted within an OAE project.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Experiment"]
    class_class_curie: ClassVar[str] = "oae:Experiment"
    class_name: ClassVar[str] = "Experiment"
    class_model_uri: ClassVar[URIRef] = OAE.Experiment

    experiment_id: Union[str, ExperimentExperimentId] = None
    description: Optional[str] = None
    experiment_type: Optional[Union[str, "ExperimentType"]] = None
    project: Optional[Union[dict, OAEProject]] = None
    observation_type: Optional[Union[Union[str, "ObservationType"], List[Union[str, "ObservationType"]]]] = empty_list()
    start_date: Optional[Union[str, XSDDateTime]] = None
    end_date: Optional[Union[str, XSDDateTime]] = None
    datasets: Optional[Union[Union[dict, Dataset], List[Union[dict, Dataset]]]] = empty_list()
    previous_research: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, ExperimentExperimentId):
            self.experiment_id = ExperimentExperimentId(self.experiment_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.experiment_type is not None and not isinstance(self.experiment_type, ExperimentType):
            self.experiment_type = ExperimentType(self.experiment_type)

        if self.project is not None and not isinstance(self.project, OAEProject):
            self.project = OAEProject(**as_dict(self.project))

        if not isinstance(self.observation_type, list):
            self.observation_type = [self.observation_type] if self.observation_type is not None else []
        self.observation_type = [v if isinstance(v, ObservationType) else ObservationType(v) for v in self.observation_type]

        if self.start_date is not None and not isinstance(self.start_date, XSDDateTime):
            self.start_date = XSDDateTime(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDateTime):
            self.end_date = XSDDateTime(self.end_date)

        if not isinstance(self.datasets, list):
            self.datasets = [self.datasets] if self.datasets is not None else []
        self.datasets = [v if isinstance(v, Dataset) else Dataset(**as_dict(v)) for v in self.datasets]

        if not isinstance(self.previous_research, list):
            self.previous_research = [self.previous_research] if self.previous_research is not None else []
        self.previous_research = [v if isinstance(v, str) else str(v) for v in self.previous_research]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Intervention(Experiment):
    """
    Details about an OAE intervention.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Intervention"]
    class_class_curie: ClassVar[str] = "oae:Intervention"
    class_name: ClassVar[str] = "Intervention"
    class_model_uri: ClassVar[URIRef] = OAE.Intervention

    experiment_id: Union[str, InterventionExperimentId] = None
    treatment_type: Optional[Union[str, "OAETreatmentType"]] = None
    alkalinity_feedstock_type: Optional[Union[str, "FeedstockType"]] = None
    alkalinity_feedstock_description: Optional[str] = None
    dosing_depth_in_m: Optional[Decimal] = None
    dosing_regimen: Optional[str] = None
    dosing_location: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, InterventionExperimentId):
            self.experiment_id = InterventionExperimentId(self.experiment_id)

        if self.treatment_type is not None and not isinstance(self.treatment_type, OAETreatmentType):
            self.treatment_type = OAETreatmentType(self.treatment_type)

        if self.alkalinity_feedstock_type is not None and not isinstance(self.alkalinity_feedstock_type, FeedstockType):
            self.alkalinity_feedstock_type = FeedstockType(self.alkalinity_feedstock_type)

        if self.alkalinity_feedstock_description is not None and not isinstance(self.alkalinity_feedstock_description, str):
            self.alkalinity_feedstock_description = str(self.alkalinity_feedstock_description)

        if self.dosing_depth_in_m is not None and not isinstance(self.dosing_depth_in_m, Decimal):
            self.dosing_depth_in_m = Decimal(self.dosing_depth_in_m)

        if self.dosing_regimen is not None and not isinstance(self.dosing_regimen, str):
            self.dosing_regimen = str(self.dosing_regimen)

        if self.dosing_location is not None and not isinstance(self.dosing_location, str):
            self.dosing_location = str(self.dosing_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelSimulation(Experiment):
    """
    A computational model run related to OAE.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ModelSimulation"]
    class_class_curie: ClassVar[str] = "oae:ModelSimulation"
    class_name: ClassVar[str] = "ModelSimulation"
    class_model_uri: ClassVar[URIRef] = OAE.ModelSimulation

    experiment_id: Union[str, ModelSimulationExperimentId] = None
    model_type: Optional[Union[str, "ModelType"]] = None
    model_configurations: Optional[Union[str, URI]] = None
    model_components: Optional[Union[Union[dict, "ModelComponent"], List[Union[dict, "ModelComponent"]]]] = empty_list()
    grid_details: Optional[Union[dict, "ModelGrid"]] = None
    description: Optional[str] = None
    experiment_type: Optional[Union[str, "ExperimentType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, ModelSimulationExperimentId):
            self.experiment_id = ModelSimulationExperimentId(self.experiment_id)

        if self.model_type is not None and not isinstance(self.model_type, ModelType):
            self.model_type = ModelType(self.model_type)

        if self.model_configurations is not None and not isinstance(self.model_configurations, URI):
            self.model_configurations = URI(self.model_configurations)

        if not isinstance(self.model_components, list):
            self.model_components = [self.model_components] if self.model_components is not None else []
        self.model_components = [v if isinstance(v, ModelComponent) else ModelComponent(**as_dict(v)) for v in self.model_components]

        if self.grid_details is not None and not isinstance(self.grid_details, ModelGrid):
            self.grid_details = ModelGrid(**as_dict(self.grid_details))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.experiment_type is not None and not isinstance(self.experiment_type, ExperimentType):
            self.experiment_type = ExperimentType(self.experiment_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelGrid(YAMLRoot):
    """
    Details about the model grid.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ModelGrid"]
    class_class_curie: ClassVar[str] = "oae:ModelGrid"
    class_name: ClassVar[str] = "ModelGrid"
    class_model_uri: ClassVar[URIRef] = OAE.ModelGrid

    grid_type: Optional[str] = None
    region: Optional[str] = None
    arrangement: Optional[str] = None
    n_x: Optional[int] = None
    n_y: Optional[int] = None
    n_z: Optional[int] = None
    n_nodes: Optional[int] = None
    horizontal_resolution_in_m: Optional[Decimal] = None
    vertical_resolution_in_m: Optional[Decimal] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.grid_type is not None and not isinstance(self.grid_type, str):
            self.grid_type = str(self.grid_type)

        if self.region is not None and not isinstance(self.region, str):
            self.region = str(self.region)

        if self.arrangement is not None and not isinstance(self.arrangement, str):
            self.arrangement = str(self.arrangement)

        if self.n_x is not None and not isinstance(self.n_x, int):
            self.n_x = int(self.n_x)

        if self.n_y is not None and not isinstance(self.n_y, int):
            self.n_y = int(self.n_y)

        if self.n_z is not None and not isinstance(self.n_z, int):
            self.n_z = int(self.n_z)

        if self.n_nodes is not None and not isinstance(self.n_nodes, int):
            self.n_nodes = int(self.n_nodes)

        if self.horizontal_resolution_in_m is not None and not isinstance(self.horizontal_resolution_in_m, Decimal):
            self.horizontal_resolution_in_m = Decimal(self.horizontal_resolution_in_m)

        if self.vertical_resolution_in_m is not None and not isinstance(self.vertical_resolution_in_m, Decimal):
            self.vertical_resolution_in_m = Decimal(self.vertical_resolution_in_m)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelComponent(YAMLRoot):
    """
    A component of a model.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ModelComponent"]
    class_class_curie: ClassVar[str] = "oae:ModelComponent"
    class_name: ClassVar[str] = "ModelComponent"
    class_model_uri: ClassVar[URIRef] = OAE.ModelComponent

    description: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    codebase: Optional[Union[str, URI]] = None
    references: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.codebase is not None and not isinstance(self.codebase, URI):
            self.codebase = URI(self.codebase)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, URI) else URI(v) for v in self.references]

        super().__post_init__(**kwargs)


class ModelPhysicsComponent(ModelComponent):
    """
    A physical component of a model.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ModelPhysicsComponent"]
    class_class_curie: ClassVar[str] = "oae:ModelPhysicsComponent"
    class_name: ClassVar[str] = "ModelPhysicsComponent"
    class_model_uri: ClassVar[URIRef] = OAE.ModelPhysicsComponent


@dataclass(repr=False)
class ModelBGCComponent(ModelComponent):
    """
    A biogeochemical / ecosystem component of a model
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ModelBGCComponent"]
    class_class_curie: ClassVar[str] = "oae:ModelBGCComponent"
    class_name: ClassVar[str] = "ModelBGCComponent"
    class_model_uri: ClassVar[URIRef] = OAE.ModelBGCComponent

    air_sea_co2_flux_parameterization: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.air_sea_co2_flux_parameterization is not None and not isinstance(self.air_sea_co2_flux_parameterization, str):
            self.air_sea_co2_flux_parameterization = str(self.air_sea_co2_flux_parameterization)

        super().__post_init__(**kwargs)


# Enumerations
class ExperimentType(EnumDefinitionImpl):
    """
    The type of experiment conducted in an OAE project.
    """
    natural = PermissibleValue(
        text="natural",
        description="""Refers to measurements representing its natural environment or context. This includes gridded or calculated values. For example, the gridded SOCAT data product is considered an in-situ data product.""")
    manipulated = PermissibleValue(
        text="manipulated",
        description="""This refers to data or measurements representing conditions that have been adjusted, or transformed from their original state. For example, observations from mCDR field trial, mesocosm, laboratory experiment, are all considered manipulated values.""")
    model_output = PermissibleValue(
        text="model_output",
        description="Model output refers to the results or data generated by numerical or computational models.")

    _defn = EnumDefinition(
        name="ExperimentType",
        description="The type of experiment conducted in an OAE project.",
    )

class ObservationType(EnumDefinitionImpl):
    """
    Types of observational data collected in ocean carbon and acidification studies, as defined in OCADS controlled
    vocabulary hosted at
    https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/vocabularies/observation-types.html
    """
    profile = PermissibleValue(
        text="profile",
        description="""Discrete water samples collected at specific ocean locations and depths, analyzed for parameters like dissolved inorganic carbon, total alkalinity, dissolved oxygen, and nutrients. Can also refer to continuous measurements using autonomous sensors mounted on a CTD rosette.""")
    surface_underway = PermissibleValue(
        text="surface_underway",
        description="""Continuous measurements of oceanographic variables at the ocean surface using sensors, often in flow-through systems onboard research vessels or ships of opportunity, to obtain real-time information about the ocean's physical and chemical conditions, such as temperature, salinity, and fCO₂.""")
    time_series = PermissibleValue(
        text="time_series",
        description="""Continuous measurements of oceanographic variables using autonomous or remotely operated platforms, including time-series moorings, uncrewed surface vehicles (USVs, e.g., Saildrones), profiling floats (e.g., Argo), and autonomous underwater vehicles (AUVs, e.g., gliders).""")
    laboratory_experiments = PermissibleValue(
        text="laboratory_experiments",
        description="""Scientific investigations where researchers manipulate parameters of the carbonate system in laboratory aquariums to simulate future ocean alkalinity enhancement (OAE) conditions and observe the responses of selected marine organisms.""")
    mesocosms = PermissibleValue(
        text="mesocosms",
        description="""Studies conducted in large, controlled outdoor tanks or enclosures that simulate natural ocean conditions, allowing examination of multiple interacting factors affecting marine communities' responses to OAE, including physical processes and complex biological interactions.""")
    field_experiments = PermissibleValue(
        text="field_experiments",
        description="""Studies involving the manipulation of total alkalinity and carbon dioxide levels in seawater at natural coastal or offshore sites, followed by monitoring the responses of the surrounding marine ecosystem.""")
    natural_analogues = PermissibleValue(
        text="natural_analogues",
        description="""Studies utilizing natural gradients in carbonate chemistry and other relevant parameters to assess the sensitivity of ocean systems to future OAE conditions, evaluating marine species' and ecosystems' long-term acclimation and adaptation to enhanced total alkalinity.""")
    model_outputs = PermissibleValue(
        text="model_outputs",
        description="""Outputs from mathematical models that simulate Earth system processes, used to replicate real-world scenarios and assess the impacts of different policies related to ocean carbon and alkalinity.""")

    _defn = EnumDefinition(
        name="ObservationType",
        description="""Types of observational data collected in ocean carbon and acidification studies, as defined in OCADS controlled vocabulary hosted at https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/vocabularies/observation-types.html""",
    )

class MCDRPathway(EnumDefinitionImpl):
    """
    Type of marine Carbon Dioxide Removal (mCDR) pathways.
    """
    ocean_alkalinity_enhancement = PermissibleValue(
        text="ocean_alkalinity_enhancement",
        description="""Ocean Alkalinity Enhancement (OAE) is a method to help mitigate climate change by increasing the alkalinity of seawater to enhance its capacity to absorb and store atmospheric carbon dioxide (CO₂).""")
    macroalgal_cultivation = PermissibleValue(
        text="macroalgal_cultivation",
        description="""Macroalgal Cultivation refers to the process of farming large seaweeds (macroalgae) such as kelp, sargassum, or other marine plants to absorb atmospheric carbon dioxide (CO₂) and potentially sequester it over the long term.""")
    direct_ocean_capture = PermissibleValue(
        text="direct_ocean_capture",
        description="""Direct Ocean Capture (DOC) is a technology-driven approach to extract carbon dioxide (CO₂) directly from seawater.""")
    ocean_fertilization = PermissibleValue(
        text="ocean_fertilization",
        description="""Ocean Fertilization is a mCDR strategy that involves adding nutrients, such as iron, nitrogen, or phosphorus, to the ocean to stimulate the growth of phytoplankton or other microscopic plants that absorb carbon dioxide (CO₂) through photosynthesis.""")
    artificial_upwelling_downwelling = PermissibleValue(
        text="artificial_upwelling_downwelling",
        description="""Artificial Upwelling and Downwelling are mCDR strategies that involve manipulating ocean water movement to enhance natural carbon sequestration processes.""")
    coastal_blue_carbon = PermissibleValue(
        text="coastal_blue_carbon",
        description="""Coastal Blue Carbon refers to the carbon captured and stored by coastal ecosystems, such as mangroves, salt marshes, and seagrasses. These ecosystems absorb carbon dioxide (CO₂) from the atmosphere and store it in their biomass (leaves, roots, stems) and sediments, making them natural and effective solutions for mCDR.""")
    marine_ecosystem_recovery = PermissibleValue(
        text="marine_ecosystem_recovery",
        description="""Marine Ecosystem Recovery refers to the restoration and protection of marine ecosystems to enhance their natural ability to capture and store carbon dioxide (CO₂). This approach leverages the natural carbon-sequestering processes of marine habitats like coral reefs, kelp forests, seagrass meadows, oyster beds, and deep-sea ecosystems, aiming to rebuild biodiversity, ecosystem functions, and carbon storage capacity.""")

    _defn = EnumDefinition(
        name="MCDRPathway",
        description="Type of marine Carbon Dioxide Removal (mCDR) pathways.",
    )

class OAETreatmentType(EnumDefinitionImpl):
    """
    Different types of alkalinity enhancement interventions.
    """
    electrochemical = PermissibleValue(
        text="electrochemical",
        description="""Uses electrochemistry to increase seawater alkalinity. This process typically involves separating seawater into acidic and alkaline streams, with the alkaline stream being released into the ocean to enhance carbon sequestration, with the acidic stream neutralized on land or used as a byproduct.""")
    mineral = PermissibleValue(
        text="mineral",
        description="""Involves adding alkaline minerals or particulate slurry (such as MgOH2, MgO, or CaO) to seawater either directly or through coastal outfalls (such as wastewater) to increase its alkalinity.""")
    dissolved = PermissibleValue(
        text="dissolved",
        description="""Involves the addition of dissolved or aqueous alkaline feedstocks (e.g. NaOH solution) into seawater either directly in coastal waters, through coastal outfalls or in the open ocean.""")
    river = PermissibleValue(
        text="river",
        description="""Involves adding alkaline substances (such as limestone) in rivers before they flow into the ocean for the purposes of carbon removal or emission reduction.""")
    coastal = PermissibleValue(
        text="coastal",
        description="""Introduces alkaline mineral sand (e.g. olivine), boulders or berms in coastal areas to promote the absorption of CO₂ from the atmosphere into carbonate minerals (e.g., calcium carbonate, CaCO₃).""")
    preequilibrated = PermissibleValue(
        text="preequilibrated",
        description="""Involves pre-treating seawater with alkalinity in a controlled setting, allowing equilibration with the atmosphere before returning into the marine system.""")

    _defn = EnumDefinition(
        name="OAETreatmentType",
        description="Different types of alkalinity enhancement interventions.",
    )

class FeedstockType(EnumDefinitionImpl):
    """
    Types of materials used for alkalinity addition, as sourced from NCEI's OCADS controlled vocabulary:
    https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/vocabularies/alkalinization-types.html
    """
    lime = PermissibleValue(
        text="lime",
        description="Lime (CaO) used as an alkalinity source.",
        meaning=PUBCHEM["14778"])
    portlandite = PermissibleValue(
        text="portlandite",
        description="Portlandite (Ca(OH)₂) used as an alkalinity source.",
        meaning=PUBCHEM["Portlandite"])
    calcium_carbonate = PermissibleValue(
        text="calcium_carbonate",
        description="Calcium carbonate (CaCO₃) used as an alkalinity source.",
        meaning=PUBCHEM["10112"])
    anorthite = PermissibleValue(
        text="anorthite",
        description="Anorthite (CaAl₂Si₂O₈) used as an alkalinity source.",
        meaning=PUBCHEM["56843091"])
    dolomite = PermissibleValue(
        text="dolomite",
        description="Dolomite (CaMg(CO₃)₂) used as an alkalinity source.",
        meaning=PUBCHEM["61833"])
    periclase = PermissibleValue(
        text="periclase",
        description="Periclase (MgO) used as an alkalinity source.",
        meaning=PUBCHEM["6850729"])
    brucite = PermissibleValue(
        text="brucite",
        description="Brucite (Mg(OH)₂) used as an alkalinity source.",
        meaning=PUBCHEM["14791"])
    magnesite = PermissibleValue(
        text="magnesite",
        description="Magnesite (MgCO₃) used as an alkalinity source.",
        meaning=PUBCHEM["11029"])
    forsterite = PermissibleValue(
        text="forsterite",
        description="Forsterite (Mg₂SiO₄) used as an alkalinity source.",
        meaning=PUBCHEM["517737"])
    mg_rich_olivine = PermissibleValue(
        text="mg_rich_olivine",
        description="Magnesium-rich olivine used as an alkalinity source.",
        meaning=PUBCHEM["71586774"])
    sodium_hydroxide = PermissibleValue(
        text="sodium_hydroxide",
        description="NaOH used as an alkalinity source.",
        meaning=PUBCHEM["14798"])
    natrite = PermissibleValue(
        text="natrite",
        description="Natrite (Na₂CO₃) used as an alkalinity source.",
        meaning=PUBCHEM["10340"])
    nahcolite = PermissibleValue(
        text="nahcolite",
        description="Nahcolite (NaHCO₃) used as an alkalinity source.",
        meaning=PUBCHEM["516892"])

    _defn = EnumDefinition(
        name="FeedstockType",
        description="""Types of materials used for alkalinity addition, as sourced from NCEI's OCADS controlled vocabulary: https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/vocabularies/alkalinization-types.html""",
    )

class ModelType(EnumDefinitionImpl):
    """
    Categories of computational modeling approaches used in OAE research.
    """
    counterfactual = PermissibleValue(
        text="counterfactual",
        description="""A counterfactual model experiment describes a simulation created to mimic current oceanic conditions without interventions, such as mCDR treatment.""")
    perturbation = PermissibleValue(
        text="perturbation",
        description="""A perturbed model experiment describes a simulation created to mimic an intervention or change from the natural ocean conditions.""")

    _defn = EnumDefinition(
        name="ModelType",
        description="Categories of computational modeling approaches used in OAE research.",
    )

# Slots
class slots:
    pass

slots.description = Slot(uri=OAE.description, name="description", curie=OAE.curie('description'),
                   model_uri=OAE.description, domain=None, range=Optional[str])

slots.name = Slot(uri=OAE.name, name="name", curie=OAE.curie('name'),
                   model_uri=OAE.name, domain=None, range=Optional[str])

slots.identifier = Slot(uri=OAE.identifier, name="identifier", curie=OAE.curie('identifier'),
                   model_uri=OAE.identifier, domain=None, range=Optional[Union[dict, Any]])

slots.experiment_type = Slot(uri=OAE.experiment_type, name="experiment_type", curie=OAE.curie('experiment_type'),
                   model_uri=OAE.experiment_type, domain=None, range=Optional[Union[str, "ExperimentType"]])

slots.oAEProject__project_id = Slot(uri=OAE.project_id, name="oAEProject__project_id", curie=OAE.curie('project_id'),
                   model_uri=OAE.oAEProject__project_id, domain=None, range=URIRef)

slots.oAEProject__mcdr_pathway = Slot(uri=OAE.mcdr_pathway, name="oAEProject__mcdr_pathway", curie=OAE.curie('mcdr_pathway'),
                   model_uri=OAE.oAEProject__mcdr_pathway, domain=None, range=Optional[Union[str, "MCDRPathway"]])

slots.oAEProject__site_description = Slot(uri=OAE.site_description, name="oAEProject__site_description", curie=OAE.curie('site_description'),
                   model_uri=OAE.oAEProject__site_description, domain=None, range=Optional[str])

slots.oAEProject__permit_info = Slot(uri=OAE.permit_info, name="oAEProject__permit_info", curie=OAE.curie('permit_info'),
                   model_uri=OAE.oAEProject__permit_info, domain=None, range=Optional[str])

slots.dataset__url = Slot(uri=SCHEMA.url, name="dataset__url", curie=SCHEMA.curie('url'),
                   model_uri=OAE.dataset__url, domain=None, range=Optional[str])

slots.dataset__temporal_coverage = Slot(uri=SCHEMA.temporalCoverage, name="dataset__temporal_coverage", curie=SCHEMA.curie('temporalCoverage'),
                   model_uri=OAE.dataset__temporal_coverage, domain=None, range=Optional[str])

slots.dataset__spatial_coverage = Slot(uri=SCHEMA.spatialCoverage, name="dataset__spatial_coverage", curie=SCHEMA.curie('spatialCoverage'),
                   model_uri=OAE.dataset__spatial_coverage, domain=None, range=Optional[str])

slots.experiment__experiment_id = Slot(uri=OAE.experiment_id, name="experiment__experiment_id", curie=OAE.curie('experiment_id'),
                   model_uri=OAE.experiment__experiment_id, domain=None, range=URIRef)

slots.experiment__project = Slot(uri=OAE.project, name="experiment__project", curie=OAE.curie('project'),
                   model_uri=OAE.experiment__project, domain=None, range=Optional[Union[dict, OAEProject]])

slots.experiment__observation_type = Slot(uri=OAE.observation_type, name="experiment__observation_type", curie=OAE.curie('observation_type'),
                   model_uri=OAE.experiment__observation_type, domain=None, range=Optional[Union[Union[str, "ObservationType"], List[Union[str, "ObservationType"]]]])

slots.experiment__start_date = Slot(uri=OAE.start_date, name="experiment__start_date", curie=OAE.curie('start_date'),
                   model_uri=OAE.experiment__start_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.experiment__end_date = Slot(uri=OAE.end_date, name="experiment__end_date", curie=OAE.curie('end_date'),
                   model_uri=OAE.experiment__end_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.experiment__datasets = Slot(uri=OAE.datasets, name="experiment__datasets", curie=OAE.curie('datasets'),
                   model_uri=OAE.experiment__datasets, domain=None, range=Optional[Union[Union[dict, Dataset], List[Union[dict, Dataset]]]])

slots.experiment__previous_research = Slot(uri=OAE.previous_research, name="experiment__previous_research", curie=OAE.curie('previous_research'),
                   model_uri=OAE.experiment__previous_research, domain=None, range=Optional[Union[str, List[str]]])

slots.intervention__treatment_type = Slot(uri=OAE.treatment_type, name="intervention__treatment_type", curie=OAE.curie('treatment_type'),
                   model_uri=OAE.intervention__treatment_type, domain=None, range=Optional[Union[str, "OAETreatmentType"]])

slots.intervention__alkalinity_feedstock_type = Slot(uri=OAE.alkalinity_feedstock_type, name="intervention__alkalinity_feedstock_type", curie=OAE.curie('alkalinity_feedstock_type'),
                   model_uri=OAE.intervention__alkalinity_feedstock_type, domain=None, range=Optional[Union[str, "FeedstockType"]])

slots.intervention__alkalinity_feedstock_description = Slot(uri=OAE.alkalinity_feedstock_description, name="intervention__alkalinity_feedstock_description", curie=OAE.curie('alkalinity_feedstock_description'),
                   model_uri=OAE.intervention__alkalinity_feedstock_description, domain=None, range=Optional[str])

slots.intervention__dosing_depth_in_m = Slot(uri=OAE.dosing_depth_in_m, name="intervention__dosing_depth_in_m", curie=OAE.curie('dosing_depth_in_m'),
                   model_uri=OAE.intervention__dosing_depth_in_m, domain=None, range=Optional[Decimal])

slots.intervention__dosing_regimen = Slot(uri=OAE.dosing_regimen, name="intervention__dosing_regimen", curie=OAE.curie('dosing_regimen'),
                   model_uri=OAE.intervention__dosing_regimen, domain=None, range=Optional[str])

slots.intervention__dosing_location = Slot(uri=OAE.dosing_location, name="intervention__dosing_location", curie=OAE.curie('dosing_location'),
                   model_uri=OAE.intervention__dosing_location, domain=None, range=Optional[str])

slots.modelSimulation__model_type = Slot(uri=OAE.model_type, name="modelSimulation__model_type", curie=OAE.curie('model_type'),
                   model_uri=OAE.modelSimulation__model_type, domain=None, range=Optional[Union[str, "ModelType"]])

slots.modelSimulation__model_configurations = Slot(uri=OAE.model_configurations, name="modelSimulation__model_configurations", curie=OAE.curie('model_configurations'),
                   model_uri=OAE.modelSimulation__model_configurations, domain=None, range=Optional[Union[str, URI]])

slots.modelSimulation__model_components = Slot(uri=OAE.model_components, name="modelSimulation__model_components", curie=OAE.curie('model_components'),
                   model_uri=OAE.modelSimulation__model_components, domain=None, range=Optional[Union[Union[dict, ModelComponent], List[Union[dict, ModelComponent]]]])

slots.modelSimulation__grid_details = Slot(uri=OAE.grid_details, name="modelSimulation__grid_details", curie=OAE.curie('grid_details'),
                   model_uri=OAE.modelSimulation__grid_details, domain=None, range=Optional[Union[dict, ModelGrid]])

slots.modelGrid__grid_type = Slot(uri=OAE.grid_type, name="modelGrid__grid_type", curie=OAE.curie('grid_type'),
                   model_uri=OAE.modelGrid__grid_type, domain=None, range=Optional[str])

slots.modelGrid__region = Slot(uri=OAE.region, name="modelGrid__region", curie=OAE.curie('region'),
                   model_uri=OAE.modelGrid__region, domain=None, range=Optional[str])

slots.modelGrid__arrangement = Slot(uri=OAE.arrangement, name="modelGrid__arrangement", curie=OAE.curie('arrangement'),
                   model_uri=OAE.modelGrid__arrangement, domain=None, range=Optional[str])

slots.modelGrid__n_x = Slot(uri=OAE.n_x, name="modelGrid__n_x", curie=OAE.curie('n_x'),
                   model_uri=OAE.modelGrid__n_x, domain=None, range=Optional[int])

slots.modelGrid__n_y = Slot(uri=OAE.n_y, name="modelGrid__n_y", curie=OAE.curie('n_y'),
                   model_uri=OAE.modelGrid__n_y, domain=None, range=Optional[int])

slots.modelGrid__n_z = Slot(uri=OAE.n_z, name="modelGrid__n_z", curie=OAE.curie('n_z'),
                   model_uri=OAE.modelGrid__n_z, domain=None, range=Optional[int])

slots.modelGrid__n_nodes = Slot(uri=OAE.n_nodes, name="modelGrid__n_nodes", curie=OAE.curie('n_nodes'),
                   model_uri=OAE.modelGrid__n_nodes, domain=None, range=Optional[int])

slots.modelGrid__horizontal_resolution_in_m = Slot(uri=OAE.horizontal_resolution_in_m, name="modelGrid__horizontal_resolution_in_m", curie=OAE.curie('horizontal_resolution_in_m'),
                   model_uri=OAE.modelGrid__horizontal_resolution_in_m, domain=None, range=Optional[Decimal])

slots.modelGrid__vertical_resolution_in_m = Slot(uri=OAE.vertical_resolution_in_m, name="modelGrid__vertical_resolution_in_m", curie=OAE.curie('vertical_resolution_in_m'),
                   model_uri=OAE.modelGrid__vertical_resolution_in_m, domain=None, range=Optional[Decimal])

slots.modelComponent__name = Slot(uri=OAE.name, name="modelComponent__name", curie=OAE.curie('name'),
                   model_uri=OAE.modelComponent__name, domain=None, range=Optional[str])

slots.modelComponent__version = Slot(uri=OAE.version, name="modelComponent__version", curie=OAE.curie('version'),
                   model_uri=OAE.modelComponent__version, domain=None, range=Optional[str])

slots.modelComponent__codebase = Slot(uri=OAE.codebase, name="modelComponent__codebase", curie=OAE.curie('codebase'),
                   model_uri=OAE.modelComponent__codebase, domain=None, range=Optional[Union[str, URI]])

slots.modelComponent__references = Slot(uri=OAE.references, name="modelComponent__references", curie=OAE.curie('references'),
                   model_uri=OAE.modelComponent__references, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.modelBGCComponent__air_sea_co2_flux_parameterization = Slot(uri=OAE.air_sea_co2_flux_parameterization, name="modelBGCComponent__air_sea_co2_flux_parameterization", curie=OAE.curie('air_sea_co2_flux_parameterization'),
                   model_uri=OAE.modelBGCComponent__air_sea_co2_flux_parameterization, domain=None, range=Optional[str])

slots.Dataset_identifier = Slot(uri=OAE.identifier, name="Dataset_identifier", curie=OAE.curie('identifier'),
                   model_uri=OAE.Dataset_identifier, domain=Dataset, range=Optional[str])

slots.ModelSimulation_description = Slot(uri=OAE.description, name="ModelSimulation_description", curie=OAE.curie('description'),
                   model_uri=OAE.ModelSimulation_description, domain=ModelSimulation, range=Optional[str])

slots.ModelSimulation_experiment_type = Slot(uri=OAE.experiment_type, name="ModelSimulation_experiment_type", curie=OAE.curie('experiment_type'),
                   model_uri=OAE.ModelSimulation_experiment_type, domain=ModelSimulation, range=Optional[Union[str, "ExperimentType"]])

slots.ModelComponent_description = Slot(uri=OAE.description, name="ModelComponent_description", curie=OAE.curie('description'),
                   model_uri=OAE.ModelComponent_description, domain=ModelComponent, range=Optional[str])