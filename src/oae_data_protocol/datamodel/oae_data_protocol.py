# Auto generated from oae_data_protocol.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-10-19T16:11:04
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

from linkml_runtime.linkml_model.types import Date, Datetime, Float, String, Uri
from linkml_runtime.utils.metamodelcore import URI, XSDDate, XSDDateTime

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



class PropertyValue(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["PropertyValue"]
    class_class_curie: ClassVar[str] = "schema:PropertyValue"
    class_name: ClassVar[str] = "PropertyValue"
    class_model_uri: ClassVar[URIRef] = OAE.PropertyValue


Any = Any

@dataclass(repr=False)
class Place(YAMLRoot):
    """
    A bounding box defined by latitude and longitude coordinates.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Place"]
    class_class_curie: ClassVar[str] = "schema:Place"
    class_name: ClassVar[str] = "Place"
    class_model_uri: ClassVar[URIRef] = OAE.Place

    geo: Union[dict, "GeoShape"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.geo):
            self.MissingRequiredField("geo")
        if not isinstance(self.geo, GeoShape):
            self.geo = GeoShape(**as_dict(self.geo))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeoShape(YAMLRoot):
    """
    The geographic shape of a place. A GeoShape can be described using several properties whose values are based on
    latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace
    should be used when writing a list of several such points. (imported from schema.org)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["GeoShape"]
    class_class_curie: ClassVar[str] = "schema:GeoShape"
    class_name: ClassVar[str] = "GeoShape"
    class_model_uri: ClassVar[URIRef] = OAE.GeoShape

    box: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.box):
            self.MissingRequiredField("box")
        if not isinstance(self.box, str):
            self.box = str(self.box)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VerticalExtent(YAMLRoot):
    """
    The vertical extent of a place or structure in meters.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["VerticalExtent"]
    class_class_curie: ClassVar[str] = "oae:VerticalExtent"
    class_name: ClassVar[str] = "VerticalExtent"
    class_model_uri: ClassVar[URIRef] = OAE.VerticalExtent

    min_depth_in_m: float = None
    max_depth_in_m: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.min_depth_in_m):
            self.MissingRequiredField("min_depth_in_m")
        if not isinstance(self.min_depth_in_m, float):
            self.min_depth_in_m = float(self.min_depth_in_m)

        if self._is_empty(self.max_depth_in_m):
            self.MissingRequiredField("max_depth_in_m")
        if not isinstance(self.max_depth_in_m, float):
            self.max_depth_in_m = float(self.max_depth_in_m)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Organization"]
    class_class_curie: ClassVar[str] = "schema:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = OAE.Organization

    identifier: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        super().__post_init__(**kwargs)


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

    temporal_coverage: str = None
    spatial_coverage: Union[dict, Place] = None
    vertical_coverage: Union[dict, VerticalExtent] = None
    project_id: str = None
    experiments: Optional[Union[Union[dict, "Experiment"], List[Union[dict, "Experiment"]]]] = empty_list()
    sea_names: Optional[Union[Union[str, "SeaNames"], List[Union[str, "SeaNames"]]]] = empty_list()
    project_description: Optional[str] = None
    physical_site_description: Optional[str] = None
    social_context_site_description: Optional[str] = None
    social_research_conducted_to_date: Optional[str] = None
    mcdr_pathway: Optional[Union[str, "MCDRPathway"]] = None
    previous_or_ongoing_colocated_research: Optional[Union[Union[dict, "ExternalProject"], List[Union[dict, "ExternalProject"]]]] = empty_list()
    colocated_operations: Optional[str] = None
    permits: Optional[Union[Union[dict, "Permit"], List[Union[dict, "Permit"]]]] = empty_list()
    public_comments: Optional[Union[Union[dict, "NamedLink"], List[Union[dict, "NamedLink"]]]] = empty_list()
    research_project: Optional[str] = None
    funding: Optional[Union[dict, "MonetaryGrant"]] = None
    additional_details: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.temporal_coverage):
            self.MissingRequiredField("temporal_coverage")
        if not isinstance(self.temporal_coverage, str):
            self.temporal_coverage = str(self.temporal_coverage)

        if self._is_empty(self.spatial_coverage):
            self.MissingRequiredField("spatial_coverage")
        if not isinstance(self.spatial_coverage, Place):
            self.spatial_coverage = Place(**as_dict(self.spatial_coverage))

        if self._is_empty(self.vertical_coverage):
            self.MissingRequiredField("vertical_coverage")
        if not isinstance(self.vertical_coverage, VerticalExtent):
            self.vertical_coverage = VerticalExtent(**as_dict(self.vertical_coverage))

        if self._is_empty(self.project_id):
            self.MissingRequiredField("project_id")
        if not isinstance(self.project_id, str):
            self.project_id = str(self.project_id)

        self._normalize_inlined_as_dict(slot_name="experiments", slot_type=Experiment, key_name="description", keyed=False)

        if not isinstance(self.sea_names, list):
            self.sea_names = [self.sea_names] if self.sea_names is not None else []
        self.sea_names = [v if isinstance(v, SeaNames) else SeaNames(v) for v in self.sea_names]

        if self.project_description is not None and not isinstance(self.project_description, str):
            self.project_description = str(self.project_description)

        if self.physical_site_description is not None and not isinstance(self.physical_site_description, str):
            self.physical_site_description = str(self.physical_site_description)

        if self.social_context_site_description is not None and not isinstance(self.social_context_site_description, str):
            self.social_context_site_description = str(self.social_context_site_description)

        if self.social_research_conducted_to_date is not None and not isinstance(self.social_research_conducted_to_date, str):
            self.social_research_conducted_to_date = str(self.social_research_conducted_to_date)

        if self.mcdr_pathway is not None and not isinstance(self.mcdr_pathway, MCDRPathway):
            self.mcdr_pathway = MCDRPathway(self.mcdr_pathway)

        self._normalize_inlined_as_dict(slot_name="previous_or_ongoing_colocated_research", slot_type=ExternalProject, key_name="temporal_coverage", keyed=False)

        if self.colocated_operations is not None and not isinstance(self.colocated_operations, str):
            self.colocated_operations = str(self.colocated_operations)

        if not isinstance(self.permits, list):
            self.permits = [self.permits] if self.permits is not None else []
        self.permits = [v if isinstance(v, Permit) else Permit(**as_dict(v)) for v in self.permits]

        self._normalize_inlined_as_dict(slot_name="public_comments", slot_type=NamedLink, key_name="name", keyed=False)

        if self.research_project is not None and not isinstance(self.research_project, str):
            self.research_project = str(self.research_project)

        if self.funding is not None and not isinstance(self.funding, MonetaryGrant):
            self.funding = MonetaryGrant(**as_dict(self.funding))

        if self.additional_details is not None and not isinstance(self.additional_details, str):
            self.additional_details = str(self.additional_details)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Permit(YAMLRoot):
    """
    A permit associated with the project.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Permit"]
    class_class_curie: ClassVar[str] = "oae:Permit"
    class_name: ClassVar[str] = "Permit"
    class_model_uri: ClassVar[URIRef] = OAE.Permit

    permit_id: str = None
    permitting_authority: str = None
    permit_status: Union[str, "PermitStatus"] = None
    approval_document: Union[str, URI] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.permit_id):
            self.MissingRequiredField("permit_id")
        if not isinstance(self.permit_id, str):
            self.permit_id = str(self.permit_id)

        if self._is_empty(self.permitting_authority):
            self.MissingRequiredField("permitting_authority")
        if not isinstance(self.permitting_authority, str):
            self.permitting_authority = str(self.permitting_authority)

        if self._is_empty(self.permit_status):
            self.MissingRequiredField("permit_status")
        if not isinstance(self.permit_status, PermitStatus):
            self.permit_status = PermitStatus(self.permit_status)

        if self._is_empty(self.approval_document):
            self.MissingRequiredField("approval_document")
        if not isinstance(self.approval_document, URI):
            self.approval_document = URI(self.approval_document)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedLink(YAMLRoot):
    """
    A link to a resource with a name and URL.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["NamedLink"]
    class_class_curie: ClassVar[str] = "oae:NamedLink"
    class_name: ClassVar[str] = "NamedLink"
    class_model_uri: ClassVar[URIRef] = OAE.NamedLink

    name: str = None
    url: Union[str, URI] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, URI):
            self.url = URI(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalProject(YAMLRoot):
    """
    A research project that is not directly managed by the OAE project, but whose location is proximal to the OAE
    project and whose data may be relevant to understanding the context or impacts of OAE activities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ExternalProject"]
    class_class_curie: ClassVar[str] = "oae:ExternalProject"
    class_name: ClassVar[str] = "ExternalProject"
    class_model_uri: ClassVar[URIRef] = OAE.ExternalProject

    temporal_coverage: str = None
    spatial_coverage: Union[dict, Place] = None
    name: str = None
    description: Optional[str] = None
    related_links: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.temporal_coverage):
            self.MissingRequiredField("temporal_coverage")
        if not isinstance(self.temporal_coverage, str):
            self.temporal_coverage = str(self.temporal_coverage)

        if self._is_empty(self.spatial_coverage):
            self.MissingRequiredField("spatial_coverage")
        if not isinstance(self.spatial_coverage, Place):
            self.spatial_coverage = Place(**as_dict(self.spatial_coverage))

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.related_links, list):
            self.related_links = [self.related_links] if self.related_links is not None else []
        self.related_links = [v if isinstance(v, URI) else URI(v) for v in self.related_links]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MonetaryGrant(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["MonetaryGrant"]
    class_class_curie: ClassVar[str] = "schema:MonetaryGrant"
    class_name: ClassVar[str] = "MonetaryGrant"
    class_model_uri: ClassVar[URIRef] = OAE.MonetaryGrant

    name: Optional[str] = None
    identifier: Optional[str] = None
    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    funder: Optional[Union[dict, Organization]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.funder is not None and not isinstance(self.funder, Organization):
            self.funder = Organization(**as_dict(self.funder))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Experiment(YAMLRoot):
    """
    Experiment metadata applies to a specific study but remains consistent across datasets.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Experiment"]
    class_class_curie: ClassVar[str] = "oae:Experiment"
    class_name: ClassVar[str] = "Experiment"
    class_model_uri: ClassVar[URIRef] = OAE.Experiment

    description: str = None
    spatial_coverage: Union[dict, Place] = None
    vertical_coverage: Union[dict, VerticalExtent] = None
    experiment_id: str = None
    experiment_type: Union[str, "ExperimentType"] = None
    investigators: Union[Union[dict, "Investigator"], List[Union[dict, "Investigator"]]] = None
    start_datetime: Union[str, XSDDateTime] = None
    end_datetime: Union[str, XSDDateTime] = None
    name: Optional[str] = None
    project_id: Optional[str] = None
    data_conflicts_and_unreported_data: Optional[str] = None
    meteorological_and_tidal_data: Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]] = empty_list()
    additional_details: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.spatial_coverage):
            self.MissingRequiredField("spatial_coverage")
        if not isinstance(self.spatial_coverage, Place):
            self.spatial_coverage = Place(**as_dict(self.spatial_coverage))

        if self._is_empty(self.vertical_coverage):
            self.MissingRequiredField("vertical_coverage")
        if not isinstance(self.vertical_coverage, VerticalExtent):
            self.vertical_coverage = VerticalExtent(**as_dict(self.vertical_coverage))

        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, str):
            self.experiment_id = str(self.experiment_id)

        if self._is_empty(self.experiment_type):
            self.MissingRequiredField("experiment_type")
        if not isinstance(self.experiment_type, ExperimentType):
            self.experiment_type = ExperimentType(self.experiment_type)

        if self._is_empty(self.investigators):
            self.MissingRequiredField("investigators")
        if not isinstance(self.investigators, list):
            self.investigators = [self.investigators] if self.investigators is not None else []
        self.investigators = [v if isinstance(v, Investigator) else Investigator(**as_dict(v)) for v in self.investigators]

        if self._is_empty(self.start_datetime):
            self.MissingRequiredField("start_datetime")
        if not isinstance(self.start_datetime, XSDDateTime):
            self.start_datetime = XSDDateTime(self.start_datetime)

        if self._is_empty(self.end_datetime):
            self.MissingRequiredField("end_datetime")
        if not isinstance(self.end_datetime, XSDDateTime):
            self.end_datetime = XSDDateTime(self.end_datetime)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.project_id is not None and not isinstance(self.project_id, str):
            self.project_id = str(self.project_id)

        if self.data_conflicts_and_unreported_data is not None and not isinstance(self.data_conflicts_and_unreported_data, str):
            self.data_conflicts_and_unreported_data = str(self.data_conflicts_and_unreported_data)

        if not isinstance(self.meteorological_and_tidal_data, list):
            self.meteorological_and_tidal_data = [self.meteorological_and_tidal_data] if self.meteorological_and_tidal_data is not None else []
        self.meteorological_and_tidal_data = [v if isinstance(v, NamedLink) else NamedLink(**as_dict(v)) for v in self.meteorological_and_tidal_data]

        if self.additional_details is not None and not isinstance(self.additional_details, str):
            self.additional_details = str(self.additional_details)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Investigator(YAMLRoot):
    """
    Information about a researcher or investigator involved in the experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Investigator"]
    class_class_curie: ClassVar[str] = "oae:Investigator"
    class_name: ClassVar[str] = "Investigator"
    class_model_uri: ClassVar[URIRef] = OAE.Investigator

    name: str = None
    affiliation: Optional[Union[dict, Organization]] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    identifier_type: Optional[str] = None
    identifier: Optional[str] = None
    role: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.affiliation is not None and not isinstance(self.affiliation, Organization):
            self.affiliation = Organization(**as_dict(self.affiliation))

        if self.phone is not None and not isinstance(self.phone, str):
            self.phone = str(self.phone)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.identifier_type is not None and not isinstance(self.identifier_type, str):
            self.identifier_type = str(self.identifier_type)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Intervention(Experiment):
    """
    Additional metadata that applies to experiments where an intervention, such as an alkalinity addition, was
    conducted.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Intervention"]
    class_class_curie: ClassVar[str] = "oae:Intervention"
    class_name: ClassVar[str] = "Intervention"
    class_model_uri: ClassVar[URIRef] = OAE.Intervention

    description: str = None
    spatial_coverage: Union[dict, Place] = None
    vertical_coverage: Union[dict, VerticalExtent] = None
    experiment_id: str = None
    experiment_type: Union[str, "ExperimentType"] = None
    investigators: Union[Union[dict, Investigator], List[Union[dict, Investigator]]] = None
    start_datetime: Union[str, XSDDateTime] = None
    end_datetime: Union[str, XSDDateTime] = None
    alkalinity_feedstock_processing: Union[Union[str, "AlkalinityFeedstockProcessing"], List[Union[str, "AlkalinityFeedstockProcessing"]]] = None
    alkalinity_feedstock_form: Union[str, "AlkalinityFeedstockForm"] = None
    alkalinity_feedstock: Union[str, "FeedstockType"] = None
    alkalinity_feedstock_description: str = None
    equilibration: Union[str, "EquilibrationStatus"] = None
    dosing_location: Union[dict, "GeoCoordinate"] = None
    dosing_dispersal_hydrologic_location: Union[str, "HydrologicLocation"] = None
    dosing_delivery_type: Union[str, "DosingDeliveryType"] = None
    alkalinity_dosing_effluent_density: str = None
    dosing_depth: str = None
    dosing_description: str = None
    dosing_regimen: str = None
    dosing_data: str = None
    alkalinity_feedstock_co2_removal_potential: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.alkalinity_feedstock_processing):
            self.MissingRequiredField("alkalinity_feedstock_processing")
        if not isinstance(self.alkalinity_feedstock_processing, list):
            self.alkalinity_feedstock_processing = [self.alkalinity_feedstock_processing] if self.alkalinity_feedstock_processing is not None else []
        self.alkalinity_feedstock_processing = [v if isinstance(v, AlkalinityFeedstockProcessing) else AlkalinityFeedstockProcessing(v) for v in self.alkalinity_feedstock_processing]

        if self._is_empty(self.alkalinity_feedstock_form):
            self.MissingRequiredField("alkalinity_feedstock_form")
        if not isinstance(self.alkalinity_feedstock_form, AlkalinityFeedstockForm):
            self.alkalinity_feedstock_form = AlkalinityFeedstockForm(self.alkalinity_feedstock_form)

        if self._is_empty(self.alkalinity_feedstock):
            self.MissingRequiredField("alkalinity_feedstock")
        if not isinstance(self.alkalinity_feedstock, FeedstockType):
            self.alkalinity_feedstock = FeedstockType(self.alkalinity_feedstock)

        if self._is_empty(self.alkalinity_feedstock_description):
            self.MissingRequiredField("alkalinity_feedstock_description")
        if not isinstance(self.alkalinity_feedstock_description, str):
            self.alkalinity_feedstock_description = str(self.alkalinity_feedstock_description)

        if self._is_empty(self.equilibration):
            self.MissingRequiredField("equilibration")
        if not isinstance(self.equilibration, EquilibrationStatus):
            self.equilibration = EquilibrationStatus(self.equilibration)

        if self._is_empty(self.dosing_location):
            self.MissingRequiredField("dosing_location")
        if not isinstance(self.dosing_location, GeoCoordinate):
            self.dosing_location = GeoCoordinate(**as_dict(self.dosing_location))

        if self._is_empty(self.dosing_dispersal_hydrologic_location):
            self.MissingRequiredField("dosing_dispersal_hydrologic_location")
        if not isinstance(self.dosing_dispersal_hydrologic_location, HydrologicLocation):
            self.dosing_dispersal_hydrologic_location = HydrologicLocation(self.dosing_dispersal_hydrologic_location)

        if self._is_empty(self.dosing_delivery_type):
            self.MissingRequiredField("dosing_delivery_type")
        if not isinstance(self.dosing_delivery_type, DosingDeliveryType):
            self.dosing_delivery_type = DosingDeliveryType(self.dosing_delivery_type)

        if self._is_empty(self.alkalinity_dosing_effluent_density):
            self.MissingRequiredField("alkalinity_dosing_effluent_density")
        if not isinstance(self.alkalinity_dosing_effluent_density, str):
            self.alkalinity_dosing_effluent_density = str(self.alkalinity_dosing_effluent_density)

        if self._is_empty(self.dosing_depth):
            self.MissingRequiredField("dosing_depth")
        if not isinstance(self.dosing_depth, str):
            self.dosing_depth = str(self.dosing_depth)

        if self._is_empty(self.dosing_description):
            self.MissingRequiredField("dosing_description")
        if not isinstance(self.dosing_description, str):
            self.dosing_description = str(self.dosing_description)

        if self._is_empty(self.dosing_regimen):
            self.MissingRequiredField("dosing_regimen")
        if not isinstance(self.dosing_regimen, str):
            self.dosing_regimen = str(self.dosing_regimen)

        if self._is_empty(self.dosing_data):
            self.MissingRequiredField("dosing_data")
        if not isinstance(self.dosing_data, str):
            self.dosing_data = str(self.dosing_data)

        if self.alkalinity_feedstock_co2_removal_potential is not None and not isinstance(self.alkalinity_feedstock_co2_removal_potential, float):
            self.alkalinity_feedstock_co2_removal_potential = float(self.alkalinity_feedstock_co2_removal_potential)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeoCoordinate(YAMLRoot):
    """
    A geographic coordinate in decimal degrees.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["GeoCoordinate"]
    class_class_curie: ClassVar[str] = "oae:GeoCoordinate"
    class_name: ClassVar[str] = "GeoCoordinate"
    class_model_uri: ClassVar[URIRef] = OAE.GeoCoordinate

    latitude: float = None
    longitude: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        super().__post_init__(**kwargs)


# Enumerations
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
    biomass_sinking = PermissibleValue(
        text="biomass_sinking",
        description="""Biomass Sinking is a method that involves taking terrestrial or ocean biomass and sinking it into the deep ocean surface, subsurface, or anoxic basins, where it is sequestered. This can be accomplished by large-scale seaweed farming or macroalgae cultivation, which incorporates atmospheric CO2 as it grows, and then is sunk to the ocean floor. Alternatively, terrestrial plant biomass can be sunk to the ocean floor.""")
    direct_ocean_capture = PermissibleValue(
        text="direct_ocean_capture",
        description="""Direct Ocean Capture (DOC) is a method that uses electrochemical processes to remove dissolved carbon dioxide (CO₂) directly from seawater for carbon storage or reuse.""")
    ocean_nutrient_fertilization = PermissibleValue(
        text="ocean_nutrient_fertilization",
        description="""Ocean Fertilization is a method that involves adding nutrients, such as iron, nitrogen, or phosphorus, to the ocean to stimulate the growth of phytoplankton or other microscopic plants that absorb carbon dioxide (CO₂) through photosynthesis.""")
    artificial_upwelling_downwelling = PermissibleValue(
        text="artificial_upwelling_downwelling",
        description="""Artificial Upwelling and Downwelling are mCDR methods that involve manipulating ocean water movement to enhance natural carbon sequestration processes.""")
    marine_ecosystem_recovery = PermissibleValue(
        text="marine_ecosystem_recovery",
        description="""Marine Ecosystem Recovery refers to the restoration and protection of marine ecosystems to enhance their natural ability to capture and store carbon dioxide (CO₂). This method leverages the natural carbon-sequestering processes of marine habitats such as salt marshes, mangrove forests, coral reefs, kelp forests, seagrass meadows, oyster beds, and deep-sea ecosystems, aiming to rebuild biodiversity, ecosystem functions, and carbon storage capacity.""")

    _defn = EnumDefinition(
        name="MCDRPathway",
        description="Type of marine Carbon Dioxide Removal (mCDR) pathways.",
    )

class ExperimentType(EnumDefinitionImpl):
    """
    Types of mCDR experiments
    """
    baseline = PermissibleValue(
        text="baseline",
        description="Baseline measurements taken before any intervention")
    control = PermissibleValue(
        text="control",
        description="Control experiment without intervention for comparison")
    intervention = PermissibleValue(
        text="intervention",
        description="Experiment with active OAE intervention")
    model = PermissibleValue(
        text="model",
        description="Model-based experiment or simulation")
    other = PermissibleValue(
        text="other",
        description="Other experiment type not covered by standard categories")

    _defn = EnumDefinition(
        name="ExperimentType",
        description="Types of mCDR experiments",
    )

class AlkalinityFeedstockProcessing(EnumDefinitionImpl):
    """
    Methods used to process alkalinity feedstock
    """
    electrochemistry = PermissibleValue(
        text="electrochemistry",
        description="Alkalinity generated via electrochemical processes (e.g., seawater electrolysis).")
    synthetically_derived = PermissibleValue(
        text="synthetically_derived",
        description="Intentionally industrially manufactured chemical compounds (e.g., Ca(OH)2 via lime kilns).")
    mineral_mining = PermissibleValue(
        text="mineral_mining",
        description="Mined geological material, including purified mineral or natural rock.")
    blended = PermissibleValue(
        text="blended",
        description="A mix of multiple sources.")
    other = PermissibleValue(
        text="other",
        description="Unclassified or novel; include a description in Experiment Description.")

    _defn = EnumDefinition(
        name="AlkalinityFeedstockProcessing",
        description="Methods used to process alkalinity feedstock",
    )

class AlkalinityFeedstockForm(EnumDefinitionImpl):
    """
    Physical form of the alkalinity feedstock upon ocean delivery
    """
    solid = PermissibleValue(
        text="solid",
        description="""Involves adding alkaline minerals or particulate slurry (such as MgOH2, MgO, or CaO) to seawater or river systems either directly, through coastal outfalls (such as wastewater), or at breaking shorelines to increase its alkalinity.""")
    aqueous = PermissibleValue(
        text="aqueous",
        description="""Aqueous alkalinity addition may use electrochemistry or fully dissolved mineral feedstock to increase seawater alkalinity.""")
    slurry = PermissibleValue(
        text="slurry",
        description="""Slurry alkalinity additions include a mix of solid and aqueous alkalinity forms, where the solid alkaline particulates are suspended in a solution.""")

    _defn = EnumDefinition(
        name="AlkalinityFeedstockForm",
        description="Physical form of the alkalinity feedstock upon ocean delivery",
    )

class EquilibrationStatus(EnumDefinitionImpl):
    """
    Equilibration status of the alkalinity feedstock
    """
    pre_equilibrated = PermissibleValue(
        text="pre_equilibrated",
        description="Pre-equilibrated with atmosphere before dosing")
    unequilibrated = PermissibleValue(
        text="unequilibrated",
        description="Not pre-equilibrated before dosing")

    _defn = EnumDefinition(
        name="EquilibrationStatus",
        description="Equilibration status of the alkalinity feedstock",
    )

class HydrologicLocation(EnumDefinitionImpl):
    """
    Hydrologic location types for dosing
    """
    coastal_surface = PermissibleValue(
        text="coastal_surface",
        description="Surface waters in coastal areas")
    offshore_surface = PermissibleValue(
        text="offshore_surface",
        description="Surface waters in offshore areas")
    river = PermissibleValue(
        text="river",
        description="River systems")
    wetland = PermissibleValue(
        text="wetland",
        description="Wetland areas")
    seafloor = PermissibleValue(
        text="seafloor",
        description="Seafloor or benthic zone")

    _defn = EnumDefinition(
        name="HydrologicLocation",
        description="Hydrologic location types for dosing",
    )

class DosingDeliveryType(EnumDefinitionImpl):
    """
    Types of dosing delivery methods
    """
    static_point_source = PermissibleValue(
        text="static_point_source",
        description="A single dosing location such as an outflow from a static platform with a pipe")
    variable_point_source = PermissibleValue(
        text="variable_point_source",
        description="""A mobile dosing regimen described by a single location at each time step, such as an outflow from a mobile platform such as a ship or surface vessel.""")
    static_distributed = PermissibleValue(
        text="static_distributed",
        description="""A set location or locations of dosing that is not a point source, such as a distributed area over the seafloor or a diffusor.""")
    variable_distributed = PermissibleValue(
        text="variable_distributed",
        description="""A distributed dosing area that varies in time, such as manually placed alkaline material over different areas at different times.""")

    _defn = EnumDefinition(
        name="DosingDeliveryType",
        description="Types of dosing delivery methods",
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

class SeaNames(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SeaNames",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/ZZ/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/ZZ/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/IJM/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/IJM/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/MKM/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/MKM/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/IRM/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/IRM/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/10/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/10/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/62a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/62a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/04/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/04/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/01c/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/01c/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/25/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/25/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/SOC/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/SOC/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/33/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/33/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/16a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/16a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/28Ab/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/28Ab/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48o/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48o/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/ESC/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/ESC/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/39/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/39/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/57b/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/57b/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/ICS/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/ICS/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/53/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/53/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/35/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/35/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/200/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/200/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/61b/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/61b/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/22/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/22/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/28Bf/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/28Bf/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/11/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/11/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/63/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/63/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/03/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/03/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/12/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/12/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/28B/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/28B/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48e/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48e/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/47/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/47/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/28Aa/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/28Aa/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/45/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/45/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/WSC/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/WSC/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/62/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/62/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/40/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/40/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/23b/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/23b/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/06/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/06/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/42/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/42/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/51/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/51/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/45a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/45a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/32b/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/32b/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/21/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/21/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/28C/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/28C/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48m/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48m/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/01b/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/01b/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/26/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/26/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/13/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/13/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/28A/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/28A/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/32/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/32/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48j/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48j/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48h/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48h/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/31/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/31/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/57a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/57a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/05/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/05/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/50/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/50/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/ARA/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/ARA/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/61a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/61a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/21a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/21a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/28Bg/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/28Bg/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48n/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48n/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/01a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/01a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/27/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/27/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/14/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/14/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/60/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/60/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48f/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48f/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/49/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/49/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48l/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48l/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48i/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48i/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/41/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/41/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/30/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/30/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/23a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/23a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/08/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/08/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/32a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/32a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/20/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/20/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/17a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/17a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/28Ae/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/28Ae/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/17/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/17/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/59/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/59/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/64/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/64/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48k/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48k/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48b/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48b/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/01/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/01/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/44/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/44/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/55/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/55/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/38/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/38/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/29/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/29/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/07/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/07/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/56/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/56/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/19/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/19/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/15a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/15a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/46b/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/46b/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/14a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/14a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/28Ad/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/28Ad/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/61/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/61/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/58/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/58/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/65/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/65/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48g/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48g/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48d/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48d/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/23/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/23/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/43/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/43/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/54/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/54/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/37/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/37/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/CAS/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/CAS/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/28/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/28/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/09/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/09/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/18/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/18/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/02/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/02/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/24/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/24/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/46/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/46/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/46a/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/46a/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/16/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/16/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/28Ac/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/28Ac/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/57/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/57/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/66/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/66/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/WAS/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/WAS/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/48c/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/48c/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/FRM/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/FRM/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/500/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/500/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/15/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/15/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/52/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/52/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/36/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/36/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/GLO/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/GLO/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/34/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/34/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/C16/current/28Bh/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/C16/current/28Bh/",
                meaning=None))

class PermitStatus(EnumDefinitionImpl):
    """
    The status of a permit.
    """
    pending = PermissibleValue(text="pending")
    active = PermissibleValue(text="active")
    expired = PermissibleValue(text="expired")
    revoked = PermissibleValue(text="revoked")

    _defn = EnumDefinition(
        name="PermitStatus",
        description="The status of a permit.",
    )

# Slots
class slots:
    pass

slots.description = Slot(uri=OAE.description, name="description", curie=OAE.curie('description'),
                   model_uri=OAE.description, domain=None, range=Optional[str])

slots.name = Slot(uri=OAE.name, name="name", curie=OAE.curie('name'),
                   model_uri=OAE.name, domain=None, range=Optional[str])

slots.identifier = Slot(uri=SCHEMA.identifier, name="identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=OAE.identifier, domain=None, range=Optional[str])

slots.temporal_coverage = Slot(uri=SCHEMA.temporalCoverage, name="temporal_coverage", curie=SCHEMA.curie('temporalCoverage'),
                   model_uri=OAE.temporal_coverage, domain=None, range=str,
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}/(\d{4}-\d{2}-\d{2}|\.\.)$'))

slots.spatial_coverage = Slot(uri=SCHEMA.spatialCoverage, name="spatial_coverage", curie=SCHEMA.curie('spatialCoverage'),
                   model_uri=OAE.spatial_coverage, domain=None, range=Union[dict, Place])

slots.vertical_coverage = Slot(uri=OAE.vertical_coverage, name="vertical_coverage", curie=OAE.curie('vertical_coverage'),
                   model_uri=OAE.vertical_coverage, domain=None, range=Union[dict, VerticalExtent])

slots.place__geo = Slot(uri=OAE.geo, name="place__geo", curie=OAE.curie('geo'),
                   model_uri=OAE.place__geo, domain=None, range=Union[dict, GeoShape])

slots.geoShape__box = Slot(uri=SCHEMA.box, name="geoShape__box", curie=SCHEMA.curie('box'),
                   model_uri=OAE.geoShape__box, domain=None, range=str)

slots.verticalExtent__min_depth_in_m = Slot(uri=OAE.min_depth_in_m, name="verticalExtent__min_depth_in_m", curie=OAE.curie('min_depth_in_m'),
                   model_uri=OAE.verticalExtent__min_depth_in_m, domain=None, range=float)

slots.verticalExtent__max_depth_in_m = Slot(uri=OAE.max_depth_in_m, name="verticalExtent__max_depth_in_m", curie=OAE.curie('max_depth_in_m'),
                   model_uri=OAE.verticalExtent__max_depth_in_m, domain=None, range=float)

slots.organization__country = Slot(uri=OAE.country, name="organization__country", curie=OAE.curie('country'),
                   model_uri=OAE.organization__country, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z]{2}$'))

slots.oAEProject__project_id = Slot(uri=OAE.project_id, name="oAEProject__project_id", curie=OAE.curie('project_id'),
                   model_uri=OAE.oAEProject__project_id, domain=None, range=str)

slots.oAEProject__experiments = Slot(uri=OAE.experiments, name="oAEProject__experiments", curie=OAE.curie('experiments'),
                   model_uri=OAE.oAEProject__experiments, domain=None, range=Optional[Union[Union[dict, Experiment], List[Union[dict, Experiment]]]])

slots.oAEProject__sea_names = Slot(uri=OAE.sea_names, name="oAEProject__sea_names", curie=OAE.curie('sea_names'),
                   model_uri=OAE.oAEProject__sea_names, domain=None, range=Optional[Union[Union[str, "SeaNames"], List[Union[str, "SeaNames"]]]])

slots.oAEProject__project_description = Slot(uri=OAE.project_description, name="oAEProject__project_description", curie=OAE.curie('project_description'),
                   model_uri=OAE.oAEProject__project_description, domain=None, range=Optional[str])

slots.oAEProject__physical_site_description = Slot(uri=OAE.physical_site_description, name="oAEProject__physical_site_description", curie=OAE.curie('physical_site_description'),
                   model_uri=OAE.oAEProject__physical_site_description, domain=None, range=Optional[str])

slots.oAEProject__social_context_site_description = Slot(uri=OAE.social_context_site_description, name="oAEProject__social_context_site_description", curie=OAE.curie('social_context_site_description'),
                   model_uri=OAE.oAEProject__social_context_site_description, domain=None, range=Optional[str])

slots.oAEProject__social_research_conducted_to_date = Slot(uri=OAE.social_research_conducted_to_date, name="oAEProject__social_research_conducted_to_date", curie=OAE.curie('social_research_conducted_to_date'),
                   model_uri=OAE.oAEProject__social_research_conducted_to_date, domain=None, range=Optional[str])

slots.oAEProject__mcdr_pathway = Slot(uri=OAE.mcdr_pathway, name="oAEProject__mcdr_pathway", curie=OAE.curie('mcdr_pathway'),
                   model_uri=OAE.oAEProject__mcdr_pathway, domain=None, range=Optional[Union[str, "MCDRPathway"]])

slots.oAEProject__previous_or_ongoing_colocated_research = Slot(uri=OAE.previous_or_ongoing_colocated_research, name="oAEProject__previous_or_ongoing_colocated_research", curie=OAE.curie('previous_or_ongoing_colocated_research'),
                   model_uri=OAE.oAEProject__previous_or_ongoing_colocated_research, domain=None, range=Optional[Union[Union[dict, ExternalProject], List[Union[dict, ExternalProject]]]])

slots.oAEProject__colocated_operations = Slot(uri=OAE.colocated_operations, name="oAEProject__colocated_operations", curie=OAE.curie('colocated_operations'),
                   model_uri=OAE.oAEProject__colocated_operations, domain=None, range=Optional[str])

slots.oAEProject__permits = Slot(uri=OAE.permits, name="oAEProject__permits", curie=OAE.curie('permits'),
                   model_uri=OAE.oAEProject__permits, domain=None, range=Optional[Union[Union[dict, Permit], List[Union[dict, Permit]]]])

slots.oAEProject__public_comments = Slot(uri=OAE.public_comments, name="oAEProject__public_comments", curie=OAE.curie('public_comments'),
                   model_uri=OAE.oAEProject__public_comments, domain=None, range=Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]])

slots.oAEProject__research_project = Slot(uri=OAE.research_project, name="oAEProject__research_project", curie=OAE.curie('research_project'),
                   model_uri=OAE.oAEProject__research_project, domain=None, range=Optional[str])

slots.oAEProject__funding = Slot(uri=SCHEMA.funding, name="oAEProject__funding", curie=SCHEMA.curie('funding'),
                   model_uri=OAE.oAEProject__funding, domain=None, range=Optional[Union[dict, MonetaryGrant]])

slots.oAEProject__additional_details = Slot(uri=OAE.additional_details, name="oAEProject__additional_details", curie=OAE.curie('additional_details'),
                   model_uri=OAE.oAEProject__additional_details, domain=None, range=Optional[str])

slots.permit__permit_id = Slot(uri=OAE.permit_id, name="permit__permit_id", curie=OAE.curie('permit_id'),
                   model_uri=OAE.permit__permit_id, domain=None, range=str)

slots.permit__permitting_authority = Slot(uri=OAE.permitting_authority, name="permit__permitting_authority", curie=OAE.curie('permitting_authority'),
                   model_uri=OAE.permit__permitting_authority, domain=None, range=str)

slots.permit__permit_status = Slot(uri=OAE.permit_status, name="permit__permit_status", curie=OAE.curie('permit_status'),
                   model_uri=OAE.permit__permit_status, domain=None, range=Union[str, "PermitStatus"])

slots.permit__approval_document = Slot(uri=OAE.approval_document, name="permit__approval_document", curie=OAE.curie('approval_document'),
                   model_uri=OAE.permit__approval_document, domain=None, range=Union[str, URI])

slots.namedLink__name = Slot(uri=OAE.name, name="namedLink__name", curie=OAE.curie('name'),
                   model_uri=OAE.namedLink__name, domain=None, range=str)

slots.namedLink__url = Slot(uri=OAE.url, name="namedLink__url", curie=OAE.curie('url'),
                   model_uri=OAE.namedLink__url, domain=None, range=Union[str, URI])

slots.externalProject__name = Slot(uri=OAE.name, name="externalProject__name", curie=OAE.curie('name'),
                   model_uri=OAE.externalProject__name, domain=None, range=str)

slots.externalProject__description = Slot(uri=OAE.description, name="externalProject__description", curie=OAE.curie('description'),
                   model_uri=OAE.externalProject__description, domain=None, range=Optional[str])

slots.externalProject__related_links = Slot(uri=OAE.related_links, name="externalProject__related_links", curie=OAE.curie('related_links'),
                   model_uri=OAE.externalProject__related_links, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.monetaryGrant__start_date = Slot(uri=OAE.start_date, name="monetaryGrant__start_date", curie=OAE.curie('start_date'),
                   model_uri=OAE.monetaryGrant__start_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.monetaryGrant__end_date = Slot(uri=OAE.end_date, name="monetaryGrant__end_date", curie=OAE.curie('end_date'),
                   model_uri=OAE.monetaryGrant__end_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.monetaryGrant__funder = Slot(uri=OAE.funder, name="monetaryGrant__funder", curie=OAE.curie('funder'),
                   model_uri=OAE.monetaryGrant__funder, domain=None, range=Optional[Union[dict, Organization]])

slots.experiment__experiment_id = Slot(uri=OAE.experiment_id, name="experiment__experiment_id", curie=OAE.curie('experiment_id'),
                   model_uri=OAE.experiment__experiment_id, domain=None, range=str)

slots.experiment__project_id = Slot(uri=OAE.project_id, name="experiment__project_id", curie=OAE.curie('project_id'),
                   model_uri=OAE.experiment__project_id, domain=None, range=Optional[str])

slots.experiment__experiment_type = Slot(uri=OAE.experiment_type, name="experiment__experiment_type", curie=OAE.curie('experiment_type'),
                   model_uri=OAE.experiment__experiment_type, domain=None, range=Union[str, "ExperimentType"])

slots.experiment__investigators = Slot(uri=OAE.investigators, name="experiment__investigators", curie=OAE.curie('investigators'),
                   model_uri=OAE.experiment__investigators, domain=None, range=Union[Union[dict, Investigator], List[Union[dict, Investigator]]])

slots.experiment__start_datetime = Slot(uri=OAE.start_datetime, name="experiment__start_datetime", curie=OAE.curie('start_datetime'),
                   model_uri=OAE.experiment__start_datetime, domain=None, range=Union[str, XSDDateTime])

slots.experiment__end_datetime = Slot(uri=OAE.end_datetime, name="experiment__end_datetime", curie=OAE.curie('end_datetime'),
                   model_uri=OAE.experiment__end_datetime, domain=None, range=Union[str, XSDDateTime])

slots.experiment__data_conflicts_and_unreported_data = Slot(uri=OAE.data_conflicts_and_unreported_data, name="experiment__data_conflicts_and_unreported_data", curie=OAE.curie('data_conflicts_and_unreported_data'),
                   model_uri=OAE.experiment__data_conflicts_and_unreported_data, domain=None, range=Optional[str])

slots.experiment__meteorological_and_tidal_data = Slot(uri=OAE.meteorological_and_tidal_data, name="experiment__meteorological_and_tidal_data", curie=OAE.curie('meteorological_and_tidal_data'),
                   model_uri=OAE.experiment__meteorological_and_tidal_data, domain=None, range=Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]])

slots.experiment__additional_details = Slot(uri=OAE.additional_details, name="experiment__additional_details", curie=OAE.curie('additional_details'),
                   model_uri=OAE.experiment__additional_details, domain=None, range=Optional[str])

slots.investigator__name = Slot(uri=OAE.name, name="investigator__name", curie=OAE.curie('name'),
                   model_uri=OAE.investigator__name, domain=None, range=str)

slots.investigator__affiliation = Slot(uri=OAE.affiliation, name="investigator__affiliation", curie=OAE.curie('affiliation'),
                   model_uri=OAE.investigator__affiliation, domain=None, range=Optional[Union[dict, Organization]])

slots.investigator__phone = Slot(uri=OAE.phone, name="investigator__phone", curie=OAE.curie('phone'),
                   model_uri=OAE.investigator__phone, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\+?[0-9\s\-\(\)]+$'))

slots.investigator__email = Slot(uri=OAE.email, name="investigator__email", curie=OAE.curie('email'),
                   model_uri=OAE.investigator__email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'))

slots.investigator__identifier_type = Slot(uri=OAE.identifier_type, name="investigator__identifier_type", curie=OAE.curie('identifier_type'),
                   model_uri=OAE.investigator__identifier_type, domain=None, range=Optional[str])

slots.investigator__identifier = Slot(uri=OAE.identifier, name="investigator__identifier", curie=OAE.curie('identifier'),
                   model_uri=OAE.investigator__identifier, domain=None, range=Optional[str])

slots.investigator__role = Slot(uri=OAE.role, name="investigator__role", curie=OAE.curie('role'),
                   model_uri=OAE.investigator__role, domain=None, range=Optional[str])

slots.intervention__alkalinity_feedstock_processing = Slot(uri=OAE.alkalinity_feedstock_processing, name="intervention__alkalinity_feedstock_processing", curie=OAE.curie('alkalinity_feedstock_processing'),
                   model_uri=OAE.intervention__alkalinity_feedstock_processing, domain=None, range=Union[Union[str, "AlkalinityFeedstockProcessing"], List[Union[str, "AlkalinityFeedstockProcessing"]]])

slots.intervention__alkalinity_feedstock_form = Slot(uri=OAE.alkalinity_feedstock_form, name="intervention__alkalinity_feedstock_form", curie=OAE.curie('alkalinity_feedstock_form'),
                   model_uri=OAE.intervention__alkalinity_feedstock_form, domain=None, range=Union[str, "AlkalinityFeedstockForm"])

slots.intervention__alkalinity_feedstock = Slot(uri=OAE.alkalinity_feedstock, name="intervention__alkalinity_feedstock", curie=OAE.curie('alkalinity_feedstock'),
                   model_uri=OAE.intervention__alkalinity_feedstock, domain=None, range=Union[str, "FeedstockType"])

slots.intervention__alkalinity_feedstock_co2_removal_potential = Slot(uri=OAE.alkalinity_feedstock_co2_removal_potential, name="intervention__alkalinity_feedstock_co2_removal_potential", curie=OAE.curie('alkalinity_feedstock_co2_removal_potential'),
                   model_uri=OAE.intervention__alkalinity_feedstock_co2_removal_potential, domain=None, range=Optional[float])

slots.intervention__alkalinity_feedstock_description = Slot(uri=OAE.alkalinity_feedstock_description, name="intervention__alkalinity_feedstock_description", curie=OAE.curie('alkalinity_feedstock_description'),
                   model_uri=OAE.intervention__alkalinity_feedstock_description, domain=None, range=str)

slots.intervention__equilibration = Slot(uri=OAE.equilibration, name="intervention__equilibration", curie=OAE.curie('equilibration'),
                   model_uri=OAE.intervention__equilibration, domain=None, range=Union[str, "EquilibrationStatus"])

slots.intervention__dosing_location = Slot(uri=OAE.dosing_location, name="intervention__dosing_location", curie=OAE.curie('dosing_location'),
                   model_uri=OAE.intervention__dosing_location, domain=None, range=Union[dict, GeoCoordinate])

slots.intervention__dosing_dispersal_hydrologic_location = Slot(uri=OAE.dosing_dispersal_hydrologic_location, name="intervention__dosing_dispersal_hydrologic_location", curie=OAE.curie('dosing_dispersal_hydrologic_location'),
                   model_uri=OAE.intervention__dosing_dispersal_hydrologic_location, domain=None, range=Union[str, "HydrologicLocation"])

slots.intervention__dosing_delivery_type = Slot(uri=OAE.dosing_delivery_type, name="intervention__dosing_delivery_type", curie=OAE.curie('dosing_delivery_type'),
                   model_uri=OAE.intervention__dosing_delivery_type, domain=None, range=Union[str, "DosingDeliveryType"])

slots.intervention__alkalinity_dosing_effluent_density = Slot(uri=OAE.alkalinity_dosing_effluent_density, name="intervention__alkalinity_dosing_effluent_density", curie=OAE.curie('alkalinity_dosing_effluent_density'),
                   model_uri=OAE.intervention__alkalinity_dosing_effluent_density, domain=None, range=str)

slots.intervention__dosing_depth = Slot(uri=OAE.dosing_depth, name="intervention__dosing_depth", curie=OAE.curie('dosing_depth'),
                   model_uri=OAE.intervention__dosing_depth, domain=None, range=str)

slots.intervention__dosing_description = Slot(uri=OAE.dosing_description, name="intervention__dosing_description", curie=OAE.curie('dosing_description'),
                   model_uri=OAE.intervention__dosing_description, domain=None, range=str)

slots.intervention__dosing_regimen = Slot(uri=OAE.dosing_regimen, name="intervention__dosing_regimen", curie=OAE.curie('dosing_regimen'),
                   model_uri=OAE.intervention__dosing_regimen, domain=None, range=str)

slots.intervention__dosing_data = Slot(uri=OAE.dosing_data, name="intervention__dosing_data", curie=OAE.curie('dosing_data'),
                   model_uri=OAE.intervention__dosing_data, domain=None, range=str)

slots.geoCoordinate__latitude = Slot(uri=OAE.latitude, name="geoCoordinate__latitude", curie=OAE.curie('latitude'),
                   model_uri=OAE.geoCoordinate__latitude, domain=None, range=float)

slots.geoCoordinate__longitude = Slot(uri=OAE.longitude, name="geoCoordinate__longitude", curie=OAE.curie('longitude'),
                   model_uri=OAE.geoCoordinate__longitude, domain=None, range=float)

slots.Organization_identifier = Slot(uri=SCHEMA.identifier, name="Organization_identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=OAE.Organization_identifier, domain=Organization, range=Optional[str])

slots.Organization_name = Slot(uri=OAE.name, name="Organization_name", curie=OAE.curie('name'),
                   model_uri=OAE.Organization_name, domain=Organization, range=Optional[str])

slots.OAEProject_temporal_coverage = Slot(uri=SCHEMA.temporalCoverage, name="OAEProject_temporal_coverage", curie=SCHEMA.curie('temporalCoverage'),
                   model_uri=OAE.OAEProject_temporal_coverage, domain=OAEProject, range=str,
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}/(\d{4}-\d{2}-\d{2}|\.\.)$'))

slots.OAEProject_spatial_coverage = Slot(uri=SCHEMA.spatialCoverage, name="OAEProject_spatial_coverage", curie=SCHEMA.curie('spatialCoverage'),
                   model_uri=OAE.OAEProject_spatial_coverage, domain=OAEProject, range=Union[dict, Place])

slots.OAEProject_vertical_coverage = Slot(uri=OAE.vertical_coverage, name="OAEProject_vertical_coverage", curie=OAE.curie('vertical_coverage'),
                   model_uri=OAE.OAEProject_vertical_coverage, domain=OAEProject, range=Union[dict, VerticalExtent])

slots.MonetaryGrant_name = Slot(uri=OAE.name, name="MonetaryGrant_name", curie=OAE.curie('name'),
                   model_uri=OAE.MonetaryGrant_name, domain=MonetaryGrant, range=Optional[str])

slots.MonetaryGrant_identifier = Slot(uri=SCHEMA.identifier, name="MonetaryGrant_identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=OAE.MonetaryGrant_identifier, domain=MonetaryGrant, range=Optional[str])

slots.Experiment_description = Slot(uri=OAE.description, name="Experiment_description", curie=OAE.curie('description'),
                   model_uri=OAE.Experiment_description, domain=Experiment, range=str)

slots.Experiment_spatial_coverage = Slot(uri=SCHEMA.spatialCoverage, name="Experiment_spatial_coverage", curie=SCHEMA.curie('spatialCoverage'),
                   model_uri=OAE.Experiment_spatial_coverage, domain=Experiment, range=Union[dict, Place])

slots.Experiment_vertical_coverage = Slot(uri=OAE.vertical_coverage, name="Experiment_vertical_coverage", curie=OAE.curie('vertical_coverage'),
                   model_uri=OAE.Experiment_vertical_coverage, domain=Experiment, range=Union[dict, VerticalExtent])