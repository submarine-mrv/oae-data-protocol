# Auto generated from oae_data_protocol.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-02-22T19:47:55
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

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDate, XSDDateTime

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



@dataclass(repr=False)
class Container(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Container"]
    class_class_curie: ClassVar[str] = "oae:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = OAE.Container

    project: Optional[Union[dict, "Project"]] = None
    experiments: Optional[Union[Union[dict, "Experiment"], List[Union[dict, "Experiment"]]]] = empty_list()
    datasets: Optional[Union[Union[dict, "Dataset"], List[Union[dict, "Dataset"]]]] = empty_list()
    version: Optional[str] = None
    protocol_git_hash: Optional[str] = None
    metadata_builder_git_hash: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.project is not None and not isinstance(self.project, Project):
            self.project = Project(**as_dict(self.project))

        self._normalize_inlined_as_dict(slot_name="experiments", slot_type=Experiment, key_name="description", keyed=False)

        self._normalize_inlined_as_dict(slot_name="datasets", slot_type=Dataset, key_name="name", keyed=False)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.protocol_git_hash is not None and not isinstance(self.protocol_git_hash, str):
            self.protocol_git_hash = str(self.protocol_git_hash)

        if self.metadata_builder_git_hash is not None and not isinstance(self.metadata_builder_git_hash, str):
            self.metadata_builder_git_hash = str(self.metadata_builder_git_hash)

        super().__post_init__(**kwargs)


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
    A geospatial area of interest, defined by a bounding box, polygon/line, or a point designated as a pair of
    geo-coordinates.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Place"]
    class_class_curie: ClassVar[str] = "schema:Place"
    class_name: ClassVar[str] = "Place"
    class_model_uri: ClassVar[URIRef] = OAE.Place

    geo: Optional[Union[dict, Any]] = None

@dataclass(repr=False)
class SpatialCoverage(Place):
    """
    A bounding box defined by latitude and longitude coordinates.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["SpatialCoverage"]
    class_class_curie: ClassVar[str] = "oae:SpatialCoverage"
    class_name: ClassVar[str] = "SpatialCoverage"
    class_model_uri: ClassVar[URIRef] = OAE.SpatialCoverage

    geo: Union[dict, "GeoShape"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.geo):
            self.MissingRequiredField("geo")
        if not isinstance(self.geo, GeoShape):
            self.geo = GeoShape(**as_dict(self.geo))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DosingLocation(Place):
    """
    A specific location of dosing for an OAE intervention and/or tracer study. Can be a point, line, or bounding box
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["DosingLocation"]
    class_class_curie: ClassVar[str] = "oae:DosingLocation"
    class_name: ClassVar[str] = "DosingLocation"
    class_model_uri: ClassVar[URIRef] = OAE.DosingLocation

    dosing_location_file: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dosing_location_file is not None and not isinstance(self.dosing_location_file, str):
            self.dosing_location_file = str(self.dosing_location_file)

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

    box: Optional[str] = None
    line: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.box is not None and not isinstance(self.box, str):
            self.box = str(self.box)

        if self.line is not None and not isinstance(self.line, str):
            self.line = str(self.line)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeoCoordinates(YAMLRoot):
    """
    A geographic coordinate in decimal degrees.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["GeoCoordinates"]
    class_class_curie: ClassVar[str] = "schema:GeoCoordinates"
    class_name: ClassVar[str] = "GeoCoordinates"
    class_model_uri: ClassVar[URIRef] = OAE.GeoCoordinates

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

    min_depth_in_m: Optional[float] = None
    max_depth_in_m: Optional[float] = None
    min_height_in_m: Optional[float] = None
    max_height_in_m: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.min_depth_in_m is not None and not isinstance(self.min_depth_in_m, float):
            self.min_depth_in_m = float(self.min_depth_in_m)

        if self.max_depth_in_m is not None and not isinstance(self.max_depth_in_m, float):
            self.max_depth_in_m = float(self.max_depth_in_m)

        if self.min_height_in_m is not None and not isinstance(self.min_height_in_m, float):
            self.min_height_in_m = float(self.min_height_in_m)

        if self.max_height_in_m is not None and not isinstance(self.max_height_in_m, float):
            self.max_height_in_m = float(self.max_height_in_m)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Organization"]
    class_class_curie: ClassVar[str] = "schema:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = OAE.Organization

    name: str = None
    identifier: Optional[str] = None
    country: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Project(YAMLRoot):
    """
    A project conducting OAE field trials or modeling.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Project"]
    class_class_curie: ClassVar[str] = "oae:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = OAE.Project

    project_id: str = None
    description: str = None
    temporal_coverage: str = None
    spatial_coverage: Union[dict, SpatialCoverage] = None
    mcdr_pathway: Union[str, "MCDRPathway"] = None
    experiments: Optional[Union[Union[dict, "Experiment"], List[Union[dict, "Experiment"]]]] = empty_list()
    sea_names: Optional[Union[Union[str, "SeaNames"], List[Union[str, "SeaNames"]]]] = empty_list()
    physical_site_description: Optional[str] = None
    social_context_site_description: Optional[str] = None
    social_research_conducted_to_date: Optional[str] = None
    previous_or_ongoing_colocated_research: Optional[Union[Union[dict, "ExternalProject"], List[Union[dict, "ExternalProject"]]]] = empty_list()
    colocated_operations: Optional[str] = None
    public_comments: Optional[str] = None
    research_project: Optional[str] = None
    funding: Optional[Union[Union[dict, "MonetaryGrant"], List[Union[dict, "MonetaryGrant"]]]] = empty_list()
    additional_details: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.project_id):
            self.MissingRequiredField("project_id")
        if not isinstance(self.project_id, str):
            self.project_id = str(self.project_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.temporal_coverage):
            self.MissingRequiredField("temporal_coverage")
        if not isinstance(self.temporal_coverage, str):
            self.temporal_coverage = str(self.temporal_coverage)

        if self._is_empty(self.spatial_coverage):
            self.MissingRequiredField("spatial_coverage")
        if not isinstance(self.spatial_coverage, SpatialCoverage):
            self.spatial_coverage = SpatialCoverage(**as_dict(self.spatial_coverage))

        if self._is_empty(self.mcdr_pathway):
            self.MissingRequiredField("mcdr_pathway")
        if not isinstance(self.mcdr_pathway, MCDRPathway):
            self.mcdr_pathway = MCDRPathway(self.mcdr_pathway)

        self._normalize_inlined_as_dict(slot_name="experiments", slot_type=Experiment, key_name="description", keyed=False)

        if not isinstance(self.sea_names, list):
            self.sea_names = [self.sea_names] if self.sea_names is not None else []
        self.sea_names = [v if isinstance(v, SeaNames) else SeaNames(v) for v in self.sea_names]

        if self.physical_site_description is not None and not isinstance(self.physical_site_description, str):
            self.physical_site_description = str(self.physical_site_description)

        if self.social_context_site_description is not None and not isinstance(self.social_context_site_description, str):
            self.social_context_site_description = str(self.social_context_site_description)

        if self.social_research_conducted_to_date is not None and not isinstance(self.social_research_conducted_to_date, str):
            self.social_research_conducted_to_date = str(self.social_research_conducted_to_date)

        self._normalize_inlined_as_dict(slot_name="previous_or_ongoing_colocated_research", slot_type=ExternalProject, key_name="temporal_coverage", keyed=False)

        if self.colocated_operations is not None and not isinstance(self.colocated_operations, str):
            self.colocated_operations = str(self.colocated_operations)

        if self.public_comments is not None and not isinstance(self.public_comments, str):
            self.public_comments = str(self.public_comments)

        if self.research_project is not None and not isinstance(self.research_project, str):
            self.research_project = str(self.research_project)

        if not isinstance(self.funding, list):
            self.funding = [self.funding] if self.funding is not None else []
        self.funding = [v if isinstance(v, MonetaryGrant) else MonetaryGrant(**as_dict(v)) for v in self.funding]

        if self.additional_details is not None and not isinstance(self.additional_details, str):
            self.additional_details = str(self.additional_details)

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
    spatial_coverage: Union[dict, SpatialCoverage] = None
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
        if not isinstance(self.spatial_coverage, SpatialCoverage):
            self.spatial_coverage = SpatialCoverage(**as_dict(self.spatial_coverage))

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
    approval_document: str = None
    agency_contact: Optional[str] = None
    changes_to_evolution_of_permit_criteria: Optional[str] = None
    permit_type: Optional[str] = None
    time_period: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.permit_id):
            self.MissingRequiredField("permit_id")
        if not isinstance(self.permit_id, str):
            self.permit_id = str(self.permit_id)

        if self._is_empty(self.permitting_authority):
            self.MissingRequiredField("permitting_authority")
        if not isinstance(self.permitting_authority, str):
            self.permitting_authority = str(self.permitting_authority)

        if self._is_empty(self.approval_document):
            self.MissingRequiredField("approval_document")
        if not isinstance(self.approval_document, str):
            self.approval_document = str(self.approval_document)

        if self.agency_contact is not None and not isinstance(self.agency_contact, str):
            self.agency_contact = str(self.agency_contact)

        if self.changes_to_evolution_of_permit_criteria is not None and not isinstance(self.changes_to_evolution_of_permit_criteria, str):
            self.changes_to_evolution_of_permit_criteria = str(self.changes_to_evolution_of_permit_criteria)

        if self.permit_type is not None and not isinstance(self.permit_type, str):
            self.permit_type = str(self.permit_type)

        if self.time_period is not None and not isinstance(self.time_period, str):
            self.time_period = str(self.time_period)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Experiment(YAMLRoot):
    """
    Abstract base class for all experiment types. Contains fields common to both in-situ and model experiments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Experiment"]
    class_class_curie: ClassVar[str] = "oae:Experiment"
    class_name: ClassVar[str] = "Experiment"
    class_model_uri: ClassVar[URIRef] = OAE.Experiment

    description: str = None
    spatial_coverage: Union[dict, SpatialCoverage] = None
    project_id: str = None
    experiment_id: str = None
    experiment_type: Union[str, "ExperimentType"] = None
    principal_investigators: Union[Union[dict, "Person"], List[Union[dict, "Person"]]] = None
    start_datetime: Union[str, XSDDateTime] = None
    name: Optional[str] = None
    end_datetime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.spatial_coverage):
            self.MissingRequiredField("spatial_coverage")
        if not isinstance(self.spatial_coverage, SpatialCoverage):
            self.spatial_coverage = SpatialCoverage(**as_dict(self.spatial_coverage))

        if self._is_empty(self.project_id):
            self.MissingRequiredField("project_id")
        if not isinstance(self.project_id, str):
            self.project_id = str(self.project_id)

        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, str):
            self.experiment_id = str(self.experiment_id)

        if self._is_empty(self.experiment_type):
            self.MissingRequiredField("experiment_type")
        if not isinstance(self.experiment_type, ExperimentType):
            self.experiment_type = ExperimentType(self.experiment_type)

        if self._is_empty(self.principal_investigators):
            self.MissingRequiredField("principal_investigators")
        if not isinstance(self.principal_investigators, list):
            self.principal_investigators = [self.principal_investigators] if self.principal_investigators is not None else []
        self.principal_investigators = [v if isinstance(v, Person) else Person(**as_dict(v)) for v in self.principal_investigators]

        if self._is_empty(self.start_datetime):
            self.MissingRequiredField("start_datetime")
        if not isinstance(self.start_datetime, XSDDateTime):
            self.start_datetime = XSDDateTime(self.start_datetime)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.end_datetime is not None and not isinstance(self.end_datetime, XSDDateTime):
            self.end_datetime = XSDDateTime(self.end_datetime)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InSituExperiment(Experiment):
    """
    Experiment metadata for in-situ studies (interventions, tracer studies, etc.). Contains fields specific to
    field-based experiments that don't apply to model experiments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["InSituExperiment"]
    class_class_curie: ClassVar[str] = "oae:InSituExperiment"
    class_name: ClassVar[str] = "InSituExperiment"
    class_model_uri: ClassVar[URIRef] = OAE.InSituExperiment

    description: str = None
    spatial_coverage: Union[dict, SpatialCoverage] = None
    project_id: str = None
    experiment_id: str = None
    experiment_type: Union[str, "ExperimentType"] = None
    principal_investigators: Union[Union[dict, "Person"], List[Union[dict, "Person"]]] = None
    start_datetime: Union[str, XSDDateTime] = None
    vertical_coverage: Optional[Union[dict, VerticalExtent]] = None
    permits: Optional[Union[Union[dict, Permit], List[Union[dict, Permit]]]] = empty_list()
    data_conflicts_and_unreported_data: Optional[str] = None
    meteorological_and_tidal_data: Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]] = empty_list()
    additional_details: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.vertical_coverage is not None and not isinstance(self.vertical_coverage, VerticalExtent):
            self.vertical_coverage = VerticalExtent(**as_dict(self.vertical_coverage))

        if not isinstance(self.permits, list):
            self.permits = [self.permits] if self.permits is not None else []
        self.permits = [v if isinstance(v, Permit) else Permit(**as_dict(v)) for v in self.permits]

        if self.data_conflicts_and_unreported_data is not None and not isinstance(self.data_conflicts_and_unreported_data, str):
            self.data_conflicts_and_unreported_data = str(self.data_conflicts_and_unreported_data)

        if not isinstance(self.meteorological_and_tidal_data, list):
            self.meteorological_and_tidal_data = [self.meteorological_and_tidal_data] if self.meteorological_and_tidal_data is not None else []
        self.meteorological_and_tidal_data = [v if isinstance(v, NamedLink) else NamedLink(**as_dict(v)) for v in self.meteorological_and_tidal_data]

        if self.additional_details is not None and not isinstance(self.additional_details, str):
            self.additional_details = str(self.additional_details)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Intervention(InSituExperiment):
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
    spatial_coverage: Union[dict, SpatialCoverage] = None
    project_id: str = None
    experiment_id: str = None
    experiment_type: Union[str, "ExperimentType"] = None
    principal_investigators: Union[Union[dict, "Person"], List[Union[dict, "Person"]]] = None
    start_datetime: Union[str, XSDDateTime] = None
    alkalinity_feedstock_processing: Union[str, "AlkalinityFeedstockProcessing"] = None
    alkalinity_feedstock_form: Union[str, "AlkalinityFeedstockForm"] = None
    alkalinity_feedstock: Union[str, "FeedstockType"] = None
    alkalinity_feedstock_co2_removal_potential: float = None
    alkalinity_feedstock_description: str = None
    equilibration: Union[str, "EquilibrationStatus"] = None
    alkalinity_dosing_effluent_density: Union[dict, "DosingConcentration"] = None
    dosing_delivery_type: Union[str, "DosingDeliveryType"] = None
    dosing_location: Union[dict, DosingLocation] = None
    dosing_dispersal_hydrologic_location: Union[str, "HydrologicLocation"] = None
    dosing_depth: str = None
    dosing_regimen: str = None
    dosing_description: str = None
    alkalinity_feedstock_processing_custom: Optional[str] = None
    alkalinity_feedstock_custom: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.alkalinity_feedstock_processing):
            self.MissingRequiredField("alkalinity_feedstock_processing")
        if not isinstance(self.alkalinity_feedstock_processing, AlkalinityFeedstockProcessing):
            self.alkalinity_feedstock_processing = AlkalinityFeedstockProcessing(self.alkalinity_feedstock_processing)

        if self._is_empty(self.alkalinity_feedstock_form):
            self.MissingRequiredField("alkalinity_feedstock_form")
        if not isinstance(self.alkalinity_feedstock_form, AlkalinityFeedstockForm):
            self.alkalinity_feedstock_form = AlkalinityFeedstockForm(self.alkalinity_feedstock_form)

        if self._is_empty(self.alkalinity_feedstock):
            self.MissingRequiredField("alkalinity_feedstock")
        if not isinstance(self.alkalinity_feedstock, FeedstockType):
            self.alkalinity_feedstock = FeedstockType(self.alkalinity_feedstock)

        if self._is_empty(self.alkalinity_feedstock_co2_removal_potential):
            self.MissingRequiredField("alkalinity_feedstock_co2_removal_potential")
        if not isinstance(self.alkalinity_feedstock_co2_removal_potential, float):
            self.alkalinity_feedstock_co2_removal_potential = float(self.alkalinity_feedstock_co2_removal_potential)

        if self._is_empty(self.alkalinity_feedstock_description):
            self.MissingRequiredField("alkalinity_feedstock_description")
        if not isinstance(self.alkalinity_feedstock_description, str):
            self.alkalinity_feedstock_description = str(self.alkalinity_feedstock_description)

        if self._is_empty(self.equilibration):
            self.MissingRequiredField("equilibration")
        if not isinstance(self.equilibration, EquilibrationStatus):
            self.equilibration = EquilibrationStatus(self.equilibration)

        if self._is_empty(self.alkalinity_dosing_effluent_density):
            self.MissingRequiredField("alkalinity_dosing_effluent_density")
        if not isinstance(self.alkalinity_dosing_effluent_density, DosingConcentration):
            self.alkalinity_dosing_effluent_density = DosingConcentration(**as_dict(self.alkalinity_dosing_effluent_density))

        if self._is_empty(self.dosing_delivery_type):
            self.MissingRequiredField("dosing_delivery_type")
        if not isinstance(self.dosing_delivery_type, DosingDeliveryType):
            self.dosing_delivery_type = DosingDeliveryType(self.dosing_delivery_type)

        if self._is_empty(self.dosing_location):
            self.MissingRequiredField("dosing_location")
        if not isinstance(self.dosing_location, DosingLocation):
            self.dosing_location = DosingLocation(**as_dict(self.dosing_location))

        if self._is_empty(self.dosing_dispersal_hydrologic_location):
            self.MissingRequiredField("dosing_dispersal_hydrologic_location")
        if not isinstance(self.dosing_dispersal_hydrologic_location, HydrologicLocation):
            self.dosing_dispersal_hydrologic_location = HydrologicLocation(self.dosing_dispersal_hydrologic_location)

        if self._is_empty(self.dosing_depth):
            self.MissingRequiredField("dosing_depth")
        if not isinstance(self.dosing_depth, str):
            self.dosing_depth = str(self.dosing_depth)

        if self._is_empty(self.dosing_regimen):
            self.MissingRequiredField("dosing_regimen")
        if not isinstance(self.dosing_regimen, str):
            self.dosing_regimen = str(self.dosing_regimen)

        if self._is_empty(self.dosing_description):
            self.MissingRequiredField("dosing_description")
        if not isinstance(self.dosing_description, str):
            self.dosing_description = str(self.dosing_description)

        if self.alkalinity_feedstock_processing_custom is not None and not isinstance(self.alkalinity_feedstock_processing_custom, str):
            self.alkalinity_feedstock_processing_custom = str(self.alkalinity_feedstock_processing_custom)

        if self.alkalinity_feedstock_custom is not None and not isinstance(self.alkalinity_feedstock_custom, str):
            self.alkalinity_feedstock_custom = str(self.alkalinity_feedstock_custom)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tracer(InSituExperiment):
    """
    Additional metadata that applies to experiments where a tracer study was conducted
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Tracer"]
    class_class_curie: ClassVar[str] = "oae:Tracer"
    class_name: ClassVar[str] = "Tracer"
    class_model_uri: ClassVar[URIRef] = OAE.Tracer

    description: str = None
    spatial_coverage: Union[dict, SpatialCoverage] = None
    project_id: str = None
    experiment_id: str = None
    experiment_type: Union[str, "ExperimentType"] = None
    principal_investigators: Union[Union[dict, "Person"], List[Union[dict, "Person"]]] = None
    start_datetime: Union[str, XSDDateTime] = None
    tracer_form: Union[str, "TracerForm"] = None
    tracer_details: str = None
    tracer_concentration: Union[dict, "DosingConcentration"] = None
    dosing_delivery_type: Union[str, "DosingDeliveryType"] = None
    dosing_location: Union[dict, DosingLocation] = None
    dosing_dispersal_hydrologic_location: Union[str, "HydrologicLocation"] = None
    dosing_depth: str = None
    dosing_regimen: str = None
    dosing_description: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.tracer_form):
            self.MissingRequiredField("tracer_form")
        if not isinstance(self.tracer_form, TracerForm):
            self.tracer_form = TracerForm(self.tracer_form)

        if self._is_empty(self.tracer_details):
            self.MissingRequiredField("tracer_details")
        if not isinstance(self.tracer_details, str):
            self.tracer_details = str(self.tracer_details)

        if self._is_empty(self.tracer_concentration):
            self.MissingRequiredField("tracer_concentration")
        if not isinstance(self.tracer_concentration, DosingConcentration):
            self.tracer_concentration = DosingConcentration(**as_dict(self.tracer_concentration))

        if self._is_empty(self.dosing_delivery_type):
            self.MissingRequiredField("dosing_delivery_type")
        if not isinstance(self.dosing_delivery_type, DosingDeliveryType):
            self.dosing_delivery_type = DosingDeliveryType(self.dosing_delivery_type)

        if self._is_empty(self.dosing_location):
            self.MissingRequiredField("dosing_location")
        if not isinstance(self.dosing_location, DosingLocation):
            self.dosing_location = DosingLocation(**as_dict(self.dosing_location))

        if self._is_empty(self.dosing_dispersal_hydrologic_location):
            self.MissingRequiredField("dosing_dispersal_hydrologic_location")
        if not isinstance(self.dosing_dispersal_hydrologic_location, HydrologicLocation):
            self.dosing_dispersal_hydrologic_location = HydrologicLocation(self.dosing_dispersal_hydrologic_location)

        if self._is_empty(self.dosing_depth):
            self.MissingRequiredField("dosing_depth")
        if not isinstance(self.dosing_depth, str):
            self.dosing_depth = str(self.dosing_depth)

        if self._is_empty(self.dosing_regimen):
            self.MissingRequiredField("dosing_regimen")
        if not isinstance(self.dosing_regimen, str):
            self.dosing_regimen = str(self.dosing_regimen)

        if self._is_empty(self.dosing_description):
            self.MissingRequiredField("dosing_description")
        if not isinstance(self.dosing_description, str):
            self.dosing_description = str(self.dosing_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterventionWithTracer(Intervention):
    """
    Additional metadata that applies to hybrid experiments where an intervention was conducted simultaneously
    alongside a tracer study, using the same instrumentation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["InterventionWithTracer"]
    class_class_curie: ClassVar[str] = "oae:InterventionWithTracer"
    class_name: ClassVar[str] = "InterventionWithTracer"
    class_model_uri: ClassVar[URIRef] = OAE.InterventionWithTracer

    description: str = None
    spatial_coverage: Union[dict, SpatialCoverage] = None
    project_id: str = None
    experiment_id: str = None
    experiment_type: Union[str, "ExperimentType"] = None
    principal_investigators: Union[Union[dict, "Person"], List[Union[dict, "Person"]]] = None
    start_datetime: Union[str, XSDDateTime] = None
    alkalinity_feedstock_processing: Union[str, "AlkalinityFeedstockProcessing"] = None
    alkalinity_feedstock_form: Union[str, "AlkalinityFeedstockForm"] = None
    alkalinity_feedstock: Union[str, "FeedstockType"] = None
    alkalinity_feedstock_co2_removal_potential: float = None
    alkalinity_feedstock_description: str = None
    equilibration: Union[str, "EquilibrationStatus"] = None
    alkalinity_dosing_effluent_density: Union[dict, "DosingConcentration"] = None
    dosing_delivery_type: Union[str, "DosingDeliveryType"] = None
    dosing_location: Union[dict, DosingLocation] = None
    dosing_dispersal_hydrologic_location: Union[str, "HydrologicLocation"] = None
    dosing_depth: str = None
    dosing_regimen: str = None
    dosing_description: str = None
    tracer_form: Union[str, "TracerForm"] = None
    tracer_details: str = None
    tracer_concentration: Union[dict, "DosingConcentration"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.tracer_form):
            self.MissingRequiredField("tracer_form")
        if not isinstance(self.tracer_form, TracerForm):
            self.tracer_form = TracerForm(self.tracer_form)

        if self._is_empty(self.tracer_details):
            self.MissingRequiredField("tracer_details")
        if not isinstance(self.tracer_details, str):
            self.tracer_details = str(self.tracer_details)

        if self._is_empty(self.tracer_concentration):
            self.MissingRequiredField("tracer_concentration")
        if not isinstance(self.tracer_concentration, DosingConcentration):
            self.tracer_concentration = DosingConcentration(**as_dict(self.tracer_concentration))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterventionDetails(YAMLRoot):
    """
    An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are specific
    to an Experiment with type "Intervention"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["InterventionDetails"]
    class_class_curie: ClassVar[str] = "oae:InterventionDetails"
    class_name: ClassVar[str] = "InterventionDetails"
    class_model_uri: ClassVar[URIRef] = OAE.InterventionDetails

    alkalinity_feedstock_processing: Union[str, "AlkalinityFeedstockProcessing"] = None
    alkalinity_feedstock_form: Union[str, "AlkalinityFeedstockForm"] = None
    alkalinity_feedstock: Union[str, "FeedstockType"] = None
    alkalinity_feedstock_co2_removal_potential: float = None
    alkalinity_feedstock_description: str = None
    equilibration: Union[str, "EquilibrationStatus"] = None
    alkalinity_dosing_effluent_density: Union[dict, "DosingConcentration"] = None
    alkalinity_feedstock_processing_custom: Optional[str] = None
    alkalinity_feedstock_custom: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.alkalinity_feedstock_processing):
            self.MissingRequiredField("alkalinity_feedstock_processing")
        if not isinstance(self.alkalinity_feedstock_processing, AlkalinityFeedstockProcessing):
            self.alkalinity_feedstock_processing = AlkalinityFeedstockProcessing(self.alkalinity_feedstock_processing)

        if self._is_empty(self.alkalinity_feedstock_form):
            self.MissingRequiredField("alkalinity_feedstock_form")
        if not isinstance(self.alkalinity_feedstock_form, AlkalinityFeedstockForm):
            self.alkalinity_feedstock_form = AlkalinityFeedstockForm(self.alkalinity_feedstock_form)

        if self._is_empty(self.alkalinity_feedstock):
            self.MissingRequiredField("alkalinity_feedstock")
        if not isinstance(self.alkalinity_feedstock, FeedstockType):
            self.alkalinity_feedstock = FeedstockType(self.alkalinity_feedstock)

        if self._is_empty(self.alkalinity_feedstock_co2_removal_potential):
            self.MissingRequiredField("alkalinity_feedstock_co2_removal_potential")
        if not isinstance(self.alkalinity_feedstock_co2_removal_potential, float):
            self.alkalinity_feedstock_co2_removal_potential = float(self.alkalinity_feedstock_co2_removal_potential)

        if self._is_empty(self.alkalinity_feedstock_description):
            self.MissingRequiredField("alkalinity_feedstock_description")
        if not isinstance(self.alkalinity_feedstock_description, str):
            self.alkalinity_feedstock_description = str(self.alkalinity_feedstock_description)

        if self._is_empty(self.equilibration):
            self.MissingRequiredField("equilibration")
        if not isinstance(self.equilibration, EquilibrationStatus):
            self.equilibration = EquilibrationStatus(self.equilibration)

        if self._is_empty(self.alkalinity_dosing_effluent_density):
            self.MissingRequiredField("alkalinity_dosing_effluent_density")
        if not isinstance(self.alkalinity_dosing_effluent_density, DosingConcentration):
            self.alkalinity_dosing_effluent_density = DosingConcentration(**as_dict(self.alkalinity_dosing_effluent_density))

        if self.alkalinity_feedstock_processing_custom is not None and not isinstance(self.alkalinity_feedstock_processing_custom, str):
            self.alkalinity_feedstock_processing_custom = str(self.alkalinity_feedstock_processing_custom)

        if self.alkalinity_feedstock_custom is not None and not isinstance(self.alkalinity_feedstock_custom, str):
            self.alkalinity_feedstock_custom = str(self.alkalinity_feedstock_custom)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TracerDetails(YAMLRoot):
    """
    An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are specific
    to an Experiment with type "Tracer"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["TracerDetails"]
    class_class_curie: ClassVar[str] = "oae:TracerDetails"
    class_name: ClassVar[str] = "TracerDetails"
    class_model_uri: ClassVar[URIRef] = OAE.TracerDetails

    tracer_form: Union[str, "TracerForm"] = None
    tracer_details: str = None
    tracer_concentration: Union[dict, "DosingConcentration"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.tracer_form):
            self.MissingRequiredField("tracer_form")
        if not isinstance(self.tracer_form, TracerForm):
            self.tracer_form = TracerForm(self.tracer_form)

        if self._is_empty(self.tracer_details):
            self.MissingRequiredField("tracer_details")
        if not isinstance(self.tracer_details, str):
            self.tracer_details = str(self.tracer_details)

        if self._is_empty(self.tracer_concentration):
            self.MissingRequiredField("tracer_concentration")
        if not isinstance(self.tracer_concentration, DosingConcentration):
            self.tracer_concentration = DosingConcentration(**as_dict(self.tracer_concentration))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DosingConcentration(YAMLRoot):
    """
    Details of tracer concentration information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["DosingConcentration"]
    class_class_curie: ClassVar[str] = "oae:DosingConcentration"
    class_name: ClassVar[str] = "DosingConcentration"
    class_model_uri: ClassVar[URIRef] = OAE.DosingConcentration

    is_derived_value: Union[bool, Bool] = None
    is_provided_as_a_file: Union[bool, Bool] = None
    amount: Optional[float] = None
    unit: Optional[Union[str, "MassConcentrationUnit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.is_derived_value):
            self.MissingRequiredField("is_derived_value")
        if not isinstance(self.is_derived_value, Bool):
            self.is_derived_value = Bool(self.is_derived_value)

        if self._is_empty(self.is_provided_as_a_file):
            self.MissingRequiredField("is_provided_as_a_file")
        if not isinstance(self.is_provided_as_a_file, Bool):
            self.is_provided_as_a_file = Bool(self.is_provided_as_a_file)

        if self.amount is not None and not isinstance(self.amount, float):
            self.amount = float(self.amount)

        if self.unit is not None and not isinstance(self.unit, MassConcentrationUnit):
            self.unit = MassConcentrationUnit(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DosingDetails(YAMLRoot):
    """
    An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are specific
    to an Experiment with active dosing (e.g. type "Tracer", "Intervention", or "InterventionWithDosing")
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["DosingDetails"]
    class_class_curie: ClassVar[str] = "oae:DosingDetails"
    class_name: ClassVar[str] = "DosingDetails"
    class_model_uri: ClassVar[URIRef] = OAE.DosingDetails

    dosing_delivery_type: Union[str, "DosingDeliveryType"] = None
    dosing_location: Union[dict, DosingLocation] = None
    dosing_dispersal_hydrologic_location: Union[str, "HydrologicLocation"] = None
    dosing_depth: str = None
    dosing_regimen: str = None
    dosing_description: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dosing_delivery_type):
            self.MissingRequiredField("dosing_delivery_type")
        if not isinstance(self.dosing_delivery_type, DosingDeliveryType):
            self.dosing_delivery_type = DosingDeliveryType(self.dosing_delivery_type)

        if self._is_empty(self.dosing_location):
            self.MissingRequiredField("dosing_location")
        if not isinstance(self.dosing_location, DosingLocation):
            self.dosing_location = DosingLocation(**as_dict(self.dosing_location))

        if self._is_empty(self.dosing_dispersal_hydrologic_location):
            self.MissingRequiredField("dosing_dispersal_hydrologic_location")
        if not isinstance(self.dosing_dispersal_hydrologic_location, HydrologicLocation):
            self.dosing_dispersal_hydrologic_location = HydrologicLocation(self.dosing_dispersal_hydrologic_location)

        if self._is_empty(self.dosing_depth):
            self.MissingRequiredField("dosing_depth")
        if not isinstance(self.dosing_depth, str):
            self.dosing_depth = str(self.dosing_depth)

        if self._is_empty(self.dosing_regimen):
            self.MissingRequiredField("dosing_regimen")
        if not isinstance(self.dosing_regimen, str):
            self.dosing_regimen = str(self.dosing_regimen)

        if self._is_empty(self.dosing_description):
            self.MissingRequiredField("dosing_description")
        if not isinstance(self.dosing_description, str):
            self.dosing_description = str(self.dosing_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    Information about a researcher or investigator involved in the experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = OAE.Person

    name: str = None
    email: str = None
    affiliation: Optional[Union[dict, Organization]] = None
    phone: Optional[str] = None
    identifier_type: Optional[Union[str, "ResearcherIDType"]] = None
    identifier: Optional[str] = None
    role: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.email):
            self.MissingRequiredField("email")
        if not isinstance(self.email, str):
            self.email = str(self.email)

        if self.affiliation is not None and not isinstance(self.affiliation, Organization):
            self.affiliation = Organization(**as_dict(self.affiliation))

        if self.phone is not None and not isinstance(self.phone, str):
            self.phone = str(self.phone)

        if self.identifier_type is not None and not isinstance(self.identifier_type, ResearcherIDType):
            self.identifier_type = ResearcherIDType(self.identifier_type)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BaseVariable(YAMLRoot):
    """
    Basic variable fields across all (including non-measured) variables
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["BaseVariable"]
    class_class_curie: ClassVar[str] = "oae:BaseVariable"
    class_name: ClassVar[str] = "BaseVariable"
    class_model_uri: ClassVar[URIRef] = OAE.BaseVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: Optional[str] = None
    standard_identifier: Optional[Union[dict, "VocabularyItemReference"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dataset_variable_name):
            self.MissingRequiredField("dataset_variable_name")
        if not isinstance(self.dataset_variable_name, str):
            self.dataset_variable_name = str(self.dataset_variable_name)

        if self._is_empty(self.long_name):
            self.MissingRequiredField("long_name")
        if not isinstance(self.long_name, str):
            self.long_name = str(self.long_name)

        if self.units is not None and not isinstance(self.units, str):
            self.units = str(self.units)

        if self.standard_identifier is not None and not isinstance(self.standard_identifier, VocabularyItemReference):
            self.standard_identifier = VocabularyItemReference(**as_dict(self.standard_identifier))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NonMeasuredVariable(BaseVariable):
    """
    Non-measured variable for data from external sources (e.g., satellite, model outputs, published data) that are not
    directly measured by the project but included in the dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["NonMeasuredVariable"]
    class_class_curie: ClassVar[str] = "oae:NonMeasuredVariable"
    class_name: ClassVar[str] = "NonMeasuredVariable"
    class_model_uri: ClassVar[URIRef] = OAE.NonMeasuredVariable

    dataset_variable_name: str = None
    long_name: str = None

@dataclass(repr=False)
class Variable(BaseVariable):
    """
    Base class for all variable types. Contains common identification and description fields shared by all variables.
    Reference: OAPMetadata XSD variables.xsd - variable, basic_variable
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Variable"]
    class_class_curie: ClassVar[str] = "oae:Variable"
    class_name: ClassVar[str] = "Variable"
    class_model_uri: ClassVar[URIRef] = OAE.Variable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    dataset_variable_name_qc_flag: Optional[str] = None
    dataset_variable_name_raw: Optional[str] = None
    method_reference: Optional[str] = None
    measurement_researcher: Optional[Union[dict, Person]] = None
    other_detailed_information: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.units):
            self.MissingRequiredField("units")
        if not isinstance(self.units, str):
            self.units = str(self.units)

        if self.dataset_variable_name_qc_flag is not None and not isinstance(self.dataset_variable_name_qc_flag, str):
            self.dataset_variable_name_qc_flag = str(self.dataset_variable_name_qc_flag)

        if self.dataset_variable_name_raw is not None and not isinstance(self.dataset_variable_name_raw, str):
            self.dataset_variable_name_raw = str(self.dataset_variable_name_raw)

        if self.method_reference is not None and not isinstance(self.method_reference, str):
            self.method_reference = str(self.method_reference)

        if self.measurement_researcher is not None and not isinstance(self.measurement_researcher, Person):
            self.measurement_researcher = Person(**as_dict(self.measurement_researcher))

        if self.other_detailed_information is not None and not isinstance(self.other_detailed_information, str):
            self.other_detailed_information = str(self.other_detailed_information)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservedPropertyVariable(Variable):
    """
    Variable that is directly measured in-situ using instruments. Reference: OAPMetadata XSD variables.xsd -
    basic_measured_observation_base
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ObservedPropertyVariable"]
    class_class_curie: ClassVar[str] = "oae:ObservedPropertyVariable"
    class_name: ClassVar[str] = "ObservedPropertyVariable"
    class_model_uri: ClassVar[URIRef] = OAE.ObservedPropertyVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    analyzing_instrument: Union[dict, "AnalyzingInstrument"] = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None
    field_replicate_information: Optional[str] = None
    sampling_instrument_type_custom: Optional[str] = None
    qc_researcher: Optional[Union[dict, Person]] = None
    qc_researcher_institution: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.analyzing_instrument):
            self.MissingRequiredField("analyzing_instrument")
        if not isinstance(self.analyzing_instrument, AnalyzingInstrument):
            self.analyzing_instrument = AnalyzingInstrument(**as_dict(self.analyzing_instrument))

        if self._is_empty(self.sampling_method):
            self.MissingRequiredField("sampling_method")
        if not isinstance(self.sampling_method, str):
            self.sampling_method = str(self.sampling_method)

        if self._is_empty(self.analyzing_method):
            self.MissingRequiredField("analyzing_method")
        if not isinstance(self.analyzing_method, str):
            self.analyzing_method = str(self.analyzing_method)

        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, ObservationType):
            self.observation_type = ObservationType(self.observation_type)

        if self._is_empty(self.sampling):
            self.MissingRequiredField("sampling")
        if not isinstance(self.sampling, SamplingType):
            self.sampling = SamplingType(self.sampling)

        if self._is_empty(self.genesis):
            self.MissingRequiredField("genesis")
        if not isinstance(self.genesis, GenesisType):
            self.genesis = GenesisType(self.genesis)

        if self._is_empty(self.sampling_instrument_type):
            self.MissingRequiredField("sampling_instrument_type")
        if not isinstance(self.sampling_instrument_type, SamplingInstrumentType):
            self.sampling_instrument_type = SamplingInstrumentType(self.sampling_instrument_type)

        if self._is_empty(self.qc_steps_taken):
            self.MissingRequiredField("qc_steps_taken")
        if not isinstance(self.qc_steps_taken, str):
            self.qc_steps_taken = str(self.qc_steps_taken)

        if self._is_empty(self.uncertainty):
            self.MissingRequiredField("uncertainty")
        if not isinstance(self.uncertainty, str):
            self.uncertainty = str(self.uncertainty)

        if self._is_empty(self.uncertainty_definition):
            self.MissingRequiredField("uncertainty_definition")
        if not isinstance(self.uncertainty_definition, str):
            self.uncertainty_definition = str(self.uncertainty_definition)

        if self._is_empty(self.missing_value_indicators):
            self.MissingRequiredField("missing_value_indicators")
        if not isinstance(self.missing_value_indicators, str):
            self.missing_value_indicators = str(self.missing_value_indicators)

        if self.field_replicate_information is not None and not isinstance(self.field_replicate_information, str):
            self.field_replicate_information = str(self.field_replicate_information)

        if self.sampling_instrument_type_custom is not None and not isinstance(self.sampling_instrument_type_custom, str):
            self.sampling_instrument_type_custom = str(self.sampling_instrument_type_custom)

        if self.qc_researcher is not None and not isinstance(self.qc_researcher, Person):
            self.qc_researcher = Person(**as_dict(self.qc_researcher))

        if self.qc_researcher_institution is not None and not isinstance(self.qc_researcher_institution, str):
            self.qc_researcher_institution = str(self.qc_researcher_institution)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiscreteMeasuredVariable(ObservedPropertyVariable):
    """
    Analyzing instrument information fields, only applied to discretely measured variables. The instrument type can be
    narrowed in subclasses using slot_usage.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["DiscreteMeasuredVariable"]
    class_class_curie: ClassVar[str] = "oae:DiscreteMeasuredVariable"
    class_name: ClassVar[str] = "DiscreteMeasuredVariable"
    class_model_uri: ClassVar[URIRef] = OAE.DiscreteMeasuredVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    analyzing_instrument: Union[dict, "AnalyzingInstrument"] = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None

@dataclass(repr=False)
class ContinuousMeasuredVariable(ObservedPropertyVariable):
    """
    Fields for continuous sampling information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ContinuousMeasuredVariable"]
    class_class_curie: ClassVar[str] = "oae:ContinuousMeasuredVariable"
    class_name: ClassVar[str] = "ContinuousMeasuredVariable"
    class_model_uri: ClassVar[URIRef] = OAE.ContinuousMeasuredVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    analyzing_instrument: Union[dict, "AnalyzingInstrument"] = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None
    raw_data_calculation_method: str = None
    calculation_software_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.raw_data_calculation_method):
            self.MissingRequiredField("raw_data_calculation_method")
        if not isinstance(self.raw_data_calculation_method, str):
            self.raw_data_calculation_method = str(self.raw_data_calculation_method)

        if self.calculation_software_version is not None and not isinstance(self.calculation_software_version, str):
            self.calculation_software_version = str(self.calculation_software_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalculatedVariable(Variable):
    """
    Variable that is calculated or derived from other variables.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["CalculatedVariable"]
    class_class_curie: ClassVar[str] = "oae:CalculatedVariable"
    class_name: ClassVar[str] = "CalculatedVariable"
    class_model_uri: ClassVar[URIRef] = OAE.CalculatedVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    genesis: Union[str, "GenesisType"] = None
    calculation_method_and_parameters: str = None
    qc_steps_taken: Optional[str] = None
    uncertainty: Optional[str] = None
    uncertainty_definition: Optional[str] = None
    missing_value_indicators: Optional[str] = None
    qc_researcher: Optional[Union[dict, Person]] = None
    qc_researcher_institution: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.genesis):
            self.MissingRequiredField("genesis")
        if not isinstance(self.genesis, GenesisType):
            self.genesis = GenesisType(self.genesis)

        if self._is_empty(self.calculation_method_and_parameters):
            self.MissingRequiredField("calculation_method_and_parameters")
        if not isinstance(self.calculation_method_and_parameters, str):
            self.calculation_method_and_parameters = str(self.calculation_method_and_parameters)

        if self.qc_steps_taken is not None and not isinstance(self.qc_steps_taken, str):
            self.qc_steps_taken = str(self.qc_steps_taken)

        if self.uncertainty is not None and not isinstance(self.uncertainty, str):
            self.uncertainty = str(self.uncertainty)

        if self.uncertainty_definition is not None and not isinstance(self.uncertainty_definition, str):
            self.uncertainty_definition = str(self.uncertainty_definition)

        if self.missing_value_indicators is not None and not isinstance(self.missing_value_indicators, str):
            self.missing_value_indicators = str(self.missing_value_indicators)

        if self.qc_researcher is not None and not isinstance(self.qc_researcher, Person):
            self.qc_researcher = Person(**as_dict(self.qc_researcher))

        if self.qc_researcher_institution is not None and not isinstance(self.qc_researcher_institution, str):
            self.qc_researcher_institution = str(self.qc_researcher_institution)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContinuousPHVariable(ContinuousMeasuredVariable):
    """
    pH measured variable from continuous autonomous sensor
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ContinuousPHVariable"]
    class_class_curie: ClassVar[str] = "oae:ContinuousPHVariable"
    class_name: ClassVar[str] = "ContinuousPHVariable"
    class_model_uri: ClassVar[URIRef] = OAE.ContinuousPHVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    analyzing_instrument: Union[dict, "AnalyzingInstrument"] = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None
    raw_data_calculation_method: str = None
    appropriate_use_quality: Optional[Union[str, "AppropriateUseQuality"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.appropriate_use_quality is not None and not isinstance(self.appropriate_use_quality, AppropriateUseQuality):
            self.appropriate_use_quality = AppropriateUseQuality(self.appropriate_use_quality)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiscretePHVariable(DiscreteMeasuredVariable):
    """
    pH measured variable with dye-based spectrophotometric measurement. Reference: OAPMetadata XSD variables.xsd -
    pH_measured
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["DiscretePHVariable"]
    class_class_curie: ClassVar[str] = "oae:DiscretePHVariable"
    class_name: ClassVar[str] = "DiscretePHVariable"
    class_model_uri: ClassVar[URIRef] = OAE.DiscretePHVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None
    measurement_temperature: str = None
    ph_reported_temperature: str = None
    analyzing_instrument: Union[dict, "PHInstrument"] = None
    temperature_correction_method: Optional[str] = None
    appropriate_use_quality: Optional[Union[str, "AppropriateUseQuality"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.measurement_temperature):
            self.MissingRequiredField("measurement_temperature")
        if not isinstance(self.measurement_temperature, str):
            self.measurement_temperature = str(self.measurement_temperature)

        if self._is_empty(self.ph_reported_temperature):
            self.MissingRequiredField("ph_reported_temperature")
        if not isinstance(self.ph_reported_temperature, str):
            self.ph_reported_temperature = str(self.ph_reported_temperature)

        if self._is_empty(self.analyzing_instrument):
            self.MissingRequiredField("analyzing_instrument")
        if not isinstance(self.analyzing_instrument, PHInstrument):
            self.analyzing_instrument = PHInstrument(**as_dict(self.analyzing_instrument))

        if self.temperature_correction_method is not None and not isinstance(self.temperature_correction_method, str):
            self.temperature_correction_method = str(self.temperature_correction_method)

        if self.appropriate_use_quality is not None and not isinstance(self.appropriate_use_quality, AppropriateUseQuality):
            self.appropriate_use_quality = AppropriateUseQuality(self.appropriate_use_quality)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContinuousTAVariable(ContinuousMeasuredVariable):
    """
    Total Alkalinity (TA) measured variable from continuous autonomous sensor
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ContinuousTAVariable"]
    class_class_curie: ClassVar[str] = "oae:ContinuousTAVariable"
    class_name: ClassVar[str] = "ContinuousTAVariable"
    class_model_uri: ClassVar[URIRef] = OAE.ContinuousTAVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    analyzing_instrument: Union[dict, "AnalyzingInstrument"] = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None
    raw_data_calculation_method: str = None
    concentration_basis: Union[str, "ConcentrationBasis"] = None
    appropriate_use_quality: Optional[Union[str, "AppropriateUseQuality"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.concentration_basis):
            self.MissingRequiredField("concentration_basis")
        if not isinstance(self.concentration_basis, ConcentrationBasis):
            self.concentration_basis = ConcentrationBasis(self.concentration_basis)

        if self.appropriate_use_quality is not None and not isinstance(self.appropriate_use_quality, AppropriateUseQuality):
            self.appropriate_use_quality = AppropriateUseQuality(self.appropriate_use_quality)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiscreteTAVariable(DiscreteMeasuredVariable):
    """
    Total Alkalinity (TA) measured variable from discrete bottle samples
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["DiscreteTAVariable"]
    class_class_curie: ClassVar[str] = "oae:DiscreteTAVariable"
    class_name: ClassVar[str] = "DiscreteTAVariable"
    class_model_uri: ClassVar[URIRef] = OAE.DiscreteTAVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None
    sample_preservation: Union[dict, "SamplePreservation"] = None
    blank_correction: str = None
    titration_type: str = None
    analyzing_instrument: Union[dict, "CRMInstrument"] = None
    concentration_basis: Union[str, "ConcentrationBasis"] = None
    titration_cell_type: Optional[Union[str, "TitrationCellType"]] = None
    curve_fitting_method: Optional[str] = None
    appropriate_use_quality: Optional[Union[str, "AppropriateUseQuality"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sample_preservation):
            self.MissingRequiredField("sample_preservation")
        if not isinstance(self.sample_preservation, SamplePreservation):
            self.sample_preservation = SamplePreservation(**as_dict(self.sample_preservation))

        if self._is_empty(self.blank_correction):
            self.MissingRequiredField("blank_correction")
        if not isinstance(self.blank_correction, str):
            self.blank_correction = str(self.blank_correction)

        if self._is_empty(self.titration_type):
            self.MissingRequiredField("titration_type")
        if not isinstance(self.titration_type, str):
            self.titration_type = str(self.titration_type)

        if self._is_empty(self.analyzing_instrument):
            self.MissingRequiredField("analyzing_instrument")
        if not isinstance(self.analyzing_instrument, CRMInstrument):
            self.analyzing_instrument = CRMInstrument(**as_dict(self.analyzing_instrument))

        if self._is_empty(self.concentration_basis):
            self.MissingRequiredField("concentration_basis")
        if not isinstance(self.concentration_basis, ConcentrationBasis):
            self.concentration_basis = ConcentrationBasis(self.concentration_basis)

        if self.titration_cell_type is not None and not isinstance(self.titration_cell_type, TitrationCellType):
            self.titration_cell_type = TitrationCellType(self.titration_cell_type)

        if self.curve_fitting_method is not None and not isinstance(self.curve_fitting_method, str):
            self.curve_fitting_method = str(self.curve_fitting_method)

        if self.appropriate_use_quality is not None and not isinstance(self.appropriate_use_quality, AppropriateUseQuality):
            self.appropriate_use_quality = AppropriateUseQuality(self.appropriate_use_quality)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContinuousDICVariable(ContinuousMeasuredVariable):
    """
    Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous sensor.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ContinuousDICVariable"]
    class_class_curie: ClassVar[str] = "oae:ContinuousDICVariable"
    class_name: ClassVar[str] = "ContinuousDICVariable"
    class_model_uri: ClassVar[URIRef] = OAE.ContinuousDICVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    analyzing_instrument: Union[dict, "AnalyzingInstrument"] = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None
    raw_data_calculation_method: str = None
    concentration_basis: Union[str, "ConcentrationBasis"] = None
    appropriate_use_quality: Optional[Union[str, "AppropriateUseQuality"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.concentration_basis):
            self.MissingRequiredField("concentration_basis")
        if not isinstance(self.concentration_basis, ConcentrationBasis):
            self.concentration_basis = ConcentrationBasis(self.concentration_basis)

        if self.appropriate_use_quality is not None and not isinstance(self.appropriate_use_quality, AppropriateUseQuality):
            self.appropriate_use_quality = AppropriateUseQuality(self.appropriate_use_quality)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiscreteDICVariable(DiscreteMeasuredVariable):
    """
    Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle samples. Uses CRM-calibrated instrument
    and includes sample preservation information. Reference: OAPMetadata XSD variables.xsd - DIC_measured
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["DiscreteDICVariable"]
    class_class_curie: ClassVar[str] = "oae:DiscreteDICVariable"
    class_name: ClassVar[str] = "DiscreteDICVariable"
    class_model_uri: ClassVar[URIRef] = OAE.DiscreteDICVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None
    sample_preservation: Union[dict, "SamplePreservation"] = None
    blank_correction: str = None
    analyzing_instrument: Union[dict, "CRMInstrument"] = None
    concentration_basis: Union[str, "ConcentrationBasis"] = None
    appropriate_use_quality: Optional[Union[str, "AppropriateUseQuality"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sample_preservation):
            self.MissingRequiredField("sample_preservation")
        if not isinstance(self.sample_preservation, SamplePreservation):
            self.sample_preservation = SamplePreservation(**as_dict(self.sample_preservation))

        if self._is_empty(self.blank_correction):
            self.MissingRequiredField("blank_correction")
        if not isinstance(self.blank_correction, str):
            self.blank_correction = str(self.blank_correction)

        if self._is_empty(self.analyzing_instrument):
            self.MissingRequiredField("analyzing_instrument")
        if not isinstance(self.analyzing_instrument, CRMInstrument):
            self.analyzing_instrument = CRMInstrument(**as_dict(self.analyzing_instrument))

        if self._is_empty(self.concentration_basis):
            self.MissingRequiredField("concentration_basis")
        if not isinstance(self.concentration_basis, ConcentrationBasis):
            self.concentration_basis = ConcentrationBasis(self.concentration_basis)

        if self.appropriate_use_quality is not None and not isinstance(self.appropriate_use_quality, AppropriateUseQuality):
            self.appropriate_use_quality = AppropriateUseQuality(self.appropriate_use_quality)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContinuousSedimentVariable(ContinuousMeasuredVariable):
    """
    Measured sediment variable collected from continuous autonomous sensor
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ContinuousSedimentVariable"]
    class_class_curie: ClassVar[str] = "oae:ContinuousSedimentVariable"
    class_name: ClassVar[str] = "ContinuousSedimentVariable"
    class_model_uri: ClassVar[URIRef] = OAE.ContinuousSedimentVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    analyzing_instrument: Union[dict, "AnalyzingInstrument"] = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None
    raw_data_calculation_method: str = None
    sediment_type: str = None
    sediment_sampling_method: str = None
    sediment_sampling_depth: str = None
    sediment_sampling_water_depth: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sediment_type):
            self.MissingRequiredField("sediment_type")
        if not isinstance(self.sediment_type, str):
            self.sediment_type = str(self.sediment_type)

        if self._is_empty(self.sediment_sampling_method):
            self.MissingRequiredField("sediment_sampling_method")
        if not isinstance(self.sediment_sampling_method, str):
            self.sediment_sampling_method = str(self.sediment_sampling_method)

        if self._is_empty(self.sediment_sampling_depth):
            self.MissingRequiredField("sediment_sampling_depth")
        if not isinstance(self.sediment_sampling_depth, str):
            self.sediment_sampling_depth = str(self.sediment_sampling_depth)

        if self._is_empty(self.sediment_sampling_water_depth):
            self.MissingRequiredField("sediment_sampling_water_depth")
        if not isinstance(self.sediment_sampling_water_depth, str):
            self.sediment_sampling_water_depth = str(self.sediment_sampling_water_depth)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiscreteSedimentVariable(DiscreteMeasuredVariable):
    """
    Measured sediment variable collected from discrete bottle samples
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["DiscreteSedimentVariable"]
    class_class_curie: ClassVar[str] = "oae:DiscreteSedimentVariable"
    class_name: ClassVar[str] = "DiscreteSedimentVariable"
    class_model_uri: ClassVar[URIRef] = OAE.DiscreteSedimentVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    analyzing_instrument: Union[dict, "AnalyzingInstrument"] = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None
    sediment_type: str = None
    sediment_sampling_method: str = None
    sediment_sampling_depth: str = None
    sediment_sampling_water_depth: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sediment_type):
            self.MissingRequiredField("sediment_type")
        if not isinstance(self.sediment_type, str):
            self.sediment_type = str(self.sediment_type)

        if self._is_empty(self.sediment_sampling_method):
            self.MissingRequiredField("sediment_sampling_method")
        if not isinstance(self.sediment_sampling_method, str):
            self.sediment_sampling_method = str(self.sediment_sampling_method)

        if self._is_empty(self.sediment_sampling_depth):
            self.MissingRequiredField("sediment_sampling_depth")
        if not isinstance(self.sediment_sampling_depth, str):
            self.sediment_sampling_depth = str(self.sediment_sampling_depth)

        if self._is_empty(self.sediment_sampling_water_depth):
            self.MissingRequiredField("sediment_sampling_water_depth")
        if not isinstance(self.sediment_sampling_water_depth, str):
            self.sediment_sampling_water_depth = str(self.sediment_sampling_water_depth)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiscreteCO2Variable(DiscreteMeasuredVariable):
    """
    CO2 discrete (bottle) measured variable (pCO2/fCO2). Reference: OAPMetadata XSD variables.xsd - co2_discrete
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["DiscreteCO2Variable"]
    class_class_curie: ClassVar[str] = "oae:DiscreteCO2Variable"
    class_name: ClassVar[str] = "DiscreteCO2Variable"
    class_model_uri: ClassVar[URIRef] = OAE.DiscreteCO2Variable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None
    storage_method: str = None
    measurement_temperature: int = None
    analyzing_instrument: Union[dict, "CO2GasDetector"] = None
    co2_reported_temperature: str = None
    seawater_volume: Optional[int] = None
    headspace_volume: Optional[int] = None
    appropriate_use_quality: Optional[Union[str, "AppropriateUseQuality"]] = None
    water_vapor_correction_method: Optional[str] = None
    temperature_correction_method: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.storage_method):
            self.MissingRequiredField("storage_method")
        if not isinstance(self.storage_method, str):
            self.storage_method = str(self.storage_method)

        if self._is_empty(self.measurement_temperature):
            self.MissingRequiredField("measurement_temperature")
        if not isinstance(self.measurement_temperature, int):
            self.measurement_temperature = int(self.measurement_temperature)

        if self._is_empty(self.analyzing_instrument):
            self.MissingRequiredField("analyzing_instrument")
        if not isinstance(self.analyzing_instrument, CO2GasDetector):
            self.analyzing_instrument = CO2GasDetector(**as_dict(self.analyzing_instrument))

        if self._is_empty(self.co2_reported_temperature):
            self.MissingRequiredField("co2_reported_temperature")
        if not isinstance(self.co2_reported_temperature, str):
            self.co2_reported_temperature = str(self.co2_reported_temperature)

        if self.seawater_volume is not None and not isinstance(self.seawater_volume, int):
            self.seawater_volume = int(self.seawater_volume)

        if self.headspace_volume is not None and not isinstance(self.headspace_volume, int):
            self.headspace_volume = int(self.headspace_volume)

        if self.appropriate_use_quality is not None and not isinstance(self.appropriate_use_quality, AppropriateUseQuality):
            self.appropriate_use_quality = AppropriateUseQuality(self.appropriate_use_quality)

        if self.water_vapor_correction_method is not None and not isinstance(self.water_vapor_correction_method, str):
            self.water_vapor_correction_method = str(self.water_vapor_correction_method)

        if self.temperature_correction_method is not None and not isinstance(self.temperature_correction_method, str):
            self.temperature_correction_method = str(self.temperature_correction_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HPLCVariable(DiscreteMeasuredVariable):
    """
    HPLC (High-Performance Liquid Chromatography) measured variable for pigment analysis. Always measured, not
    calculated.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["HPLCVariable"]
    class_class_curie: ClassVar[str] = "oae:HPLCVariable"
    class_name: ClassVar[str] = "HPLCVariable"
    class_model_uri: ClassVar[URIRef] = OAE.HPLCVariable

    dataset_variable_name: str = None
    long_name: str = None
    units: str = None
    analyzing_instrument: Union[dict, "AnalyzingInstrument"] = None
    sampling_method: str = None
    analyzing_method: str = None
    observation_type: Union[str, "ObservationType"] = None
    sampling: Union[str, "SamplingType"] = None
    genesis: Union[str, "GenesisType"] = None
    sampling_instrument_type: Union[str, "SamplingInstrumentType"] = None
    qc_steps_taken: str = None
    uncertainty: str = None
    uncertainty_definition: str = None
    missing_value_indicators: str = None
    hplc_lab: str = None
    hplc_lab_technician: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.hplc_lab):
            self.MissingRequiredField("hplc_lab")
        if not isinstance(self.hplc_lab, str):
            self.hplc_lab = str(self.hplc_lab)

        if self.hplc_lab_technician is not None and not isinstance(self.hplc_lab_technician, str):
            self.hplc_lab_technician = str(self.hplc_lab_technician)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SamplePreservation(YAMLRoot):
    """
    Sample preservation information for DIC and TA measurements. Reference: OAPMetadata XSD variables.xsd -
    sample_preservation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["SamplePreservation"]
    class_class_curie: ClassVar[str] = "oae:SamplePreservation"
    class_name: ClassVar[str] = "SamplePreservation"
    class_model_uri: ClassVar[URIRef] = OAE.SamplePreservation

    preservative: str = None
    volume: str = None
    correction_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.preservative):
            self.MissingRequiredField("preservative")
        if not isinstance(self.preservative, str):
            self.preservative = str(self.preservative)

        if self._is_empty(self.volume):
            self.MissingRequiredField("volume")
        if not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.correction_description is not None and not isinstance(self.correction_description, str):
            self.correction_description = str(self.correction_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VocabularyItemReference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["VocabularyItemReference"]
    class_class_curie: ClassVar[str] = "oae:VocabularyItemReference"
    class_name: ClassVar[str] = "VocabularyItemReference"
    class_model_uri: ClassVar[URIRef] = OAE.VocabularyItemReference

    term: str = None
    uri: Union[str, URIorCURIE] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, str):
            self.term = str(self.term)

        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, URIorCURIE):
            self.uri = URIorCURIE(self.uri)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasuredTAFields(YAMLRoot):
    """
    Fields applied to all measured TA variable types (discrete and continuous)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["MeasuredTAFields"]
    class_class_curie: ClassVar[str] = "oae:MeasuredTAFields"
    class_name: ClassVar[str] = "MeasuredTAFields"
    class_model_uri: ClassVar[URIRef] = OAE.MeasuredTAFields

    concentration_basis: Union[str, "ConcentrationBasis"] = None
    appropriate_use_quality: Optional[Union[str, "AppropriateUseQuality"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.concentration_basis):
            self.MissingRequiredField("concentration_basis")
        if not isinstance(self.concentration_basis, ConcentrationBasis):
            self.concentration_basis = ConcentrationBasis(self.concentration_basis)

        if self.appropriate_use_quality is not None and not isinstance(self.appropriate_use_quality, AppropriateUseQuality):
            self.appropriate_use_quality = AppropriateUseQuality(self.appropriate_use_quality)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasuredDICFields(YAMLRoot):
    """
    Fields applied to all measured DIC variable types (discrete and continuous)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["MeasuredDICFields"]
    class_class_curie: ClassVar[str] = "oae:MeasuredDICFields"
    class_name: ClassVar[str] = "MeasuredDICFields"
    class_model_uri: ClassVar[URIRef] = OAE.MeasuredDICFields

    concentration_basis: Union[str, "ConcentrationBasis"] = None
    appropriate_use_quality: Optional[Union[str, "AppropriateUseQuality"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.concentration_basis):
            self.MissingRequiredField("concentration_basis")
        if not isinstance(self.concentration_basis, ConcentrationBasis):
            self.concentration_basis = ConcentrationBasis(self.concentration_basis)

        if self.appropriate_use_quality is not None and not isinstance(self.appropriate_use_quality, AppropriateUseQuality):
            self.appropriate_use_quality = AppropriateUseQuality(self.appropriate_use_quality)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasuredPHFields(YAMLRoot):
    """
    Fields applied to all measured pH variable types (discrete and continuous)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["MeasuredPHFields"]
    class_class_curie: ClassVar[str] = "oae:MeasuredPHFields"
    class_name: ClassVar[str] = "MeasuredPHFields"
    class_model_uri: ClassVar[URIRef] = OAE.MeasuredPHFields

    appropriate_use_quality: Optional[Union[str, "AppropriateUseQuality"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.appropriate_use_quality is not None and not isinstance(self.appropriate_use_quality, AppropriateUseQuality):
            self.appropriate_use_quality = AppropriateUseQuality(self.appropriate_use_quality)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasuredSedimentFields(YAMLRoot):
    """
    Fields applied to all measured sediment variable types (discrete and continuous)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["MeasuredSedimentFields"]
    class_class_curie: ClassVar[str] = "oae:MeasuredSedimentFields"
    class_name: ClassVar[str] = "MeasuredSedimentFields"
    class_model_uri: ClassVar[URIRef] = OAE.MeasuredSedimentFields

    sediment_type: str = None
    sediment_sampling_method: str = None
    sediment_sampling_depth: str = None
    sediment_sampling_water_depth: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sediment_type):
            self.MissingRequiredField("sediment_type")
        if not isinstance(self.sediment_type, str):
            self.sediment_type = str(self.sediment_type)

        if self._is_empty(self.sediment_sampling_method):
            self.MissingRequiredField("sediment_sampling_method")
        if not isinstance(self.sediment_sampling_method, str):
            self.sediment_sampling_method = str(self.sediment_sampling_method)

        if self._is_empty(self.sediment_sampling_depth):
            self.MissingRequiredField("sediment_sampling_depth")
        if not isinstance(self.sediment_sampling_depth, str):
            self.sediment_sampling_depth = str(self.sediment_sampling_depth)

        if self._is_empty(self.sediment_sampling_water_depth):
            self.MissingRequiredField("sediment_sampling_water_depth")
        if not isinstance(self.sediment_sampling_water_depth, str):
            self.sediment_sampling_water_depth = str(self.sediment_sampling_water_depth)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasuredCO2Fields(YAMLRoot):
    """
    Fields applied to all measured CO2 variable types (discrete and continuous)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["MeasuredCO2Fields"]
    class_class_curie: ClassVar[str] = "oae:MeasuredCO2Fields"
    class_name: ClassVar[str] = "MeasuredCO2Fields"
    class_model_uri: ClassVar[URIRef] = OAE.MeasuredCO2Fields

    co2_reported_temperature: str = None
    appropriate_use_quality: Optional[Union[str, "AppropriateUseQuality"]] = None
    water_vapor_correction_method: Optional[str] = None
    temperature_correction_method: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.co2_reported_temperature):
            self.MissingRequiredField("co2_reported_temperature")
        if not isinstance(self.co2_reported_temperature, str):
            self.co2_reported_temperature = str(self.co2_reported_temperature)

        if self.appropriate_use_quality is not None and not isinstance(self.appropriate_use_quality, AppropriateUseQuality):
            self.appropriate_use_quality = AppropriateUseQuality(self.appropriate_use_quality)

        if self.water_vapor_correction_method is not None and not isinstance(self.water_vapor_correction_method, str):
            self.water_vapor_correction_method = str(self.water_vapor_correction_method)

        if self.temperature_correction_method is not None and not isinstance(self.temperature_correction_method, str):
            self.temperature_correction_method = str(self.temperature_correction_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QCFields(YAMLRoot):
    """
    Quality control fields applicable to measured and calculated variables. Not applied to socioeconomic variables.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["QCFields"]
    class_class_curie: ClassVar[str] = "oae:QCFields"
    class_name: ClassVar[str] = "QCFields"
    class_model_uri: ClassVar[URIRef] = OAE.QCFields

    qc_steps_taken: Optional[str] = None
    uncertainty: Optional[str] = None
    uncertainty_definition: Optional[str] = None
    missing_value_indicators: Optional[str] = None
    qc_researcher: Optional[Union[dict, Person]] = None
    qc_researcher_institution: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.qc_steps_taken is not None and not isinstance(self.qc_steps_taken, str):
            self.qc_steps_taken = str(self.qc_steps_taken)

        if self.uncertainty is not None and not isinstance(self.uncertainty, str):
            self.uncertainty = str(self.uncertainty)

        if self.uncertainty_definition is not None and not isinstance(self.uncertainty_definition, str):
            self.uncertainty_definition = str(self.uncertainty_definition)

        if self.missing_value_indicators is not None and not isinstance(self.missing_value_indicators, str):
            self.missing_value_indicators = str(self.missing_value_indicators)

        if self.qc_researcher is not None and not isinstance(self.qc_researcher, Person):
            self.qc_researcher = Person(**as_dict(self.qc_researcher))

        if self.qc_researcher_institution is not None and not isinstance(self.qc_researcher_institution, str):
            self.qc_researcher_institution = str(self.qc_researcher_institution)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    Abstract base class for all dataset types. Contains fields common to both field/observational and model simulation
    datasets. Generally following guidelines & best practices as outlined in
    [science-on-schema.org](https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Dataset"]
    class_class_curie: ClassVar[str] = "oae:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = OAE.Dataset

    name: str = None
    description: str = None
    project_id: str = None
    experiment_id: str = None
    dataset_type: Union[str, "DatasetType"] = None
    data_submitter: Union[dict, Person] = None
    filenames: Union[str, List[str]] = None
    dataset_type_custom: Optional[str] = None
    author_list_for_citation: Optional[str] = None
    license: Optional[Union[str, URI]] = None
    fair_use_data_request: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.project_id):
            self.MissingRequiredField("project_id")
        if not isinstance(self.project_id, str):
            self.project_id = str(self.project_id)

        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, str):
            self.experiment_id = str(self.experiment_id)

        if self._is_empty(self.dataset_type):
            self.MissingRequiredField("dataset_type")
        if not isinstance(self.dataset_type, DatasetType):
            self.dataset_type = DatasetType(self.dataset_type)

        if self._is_empty(self.data_submitter):
            self.MissingRequiredField("data_submitter")
        if not isinstance(self.data_submitter, Person):
            self.data_submitter = Person(**as_dict(self.data_submitter))

        if self._is_empty(self.filenames):
            self.MissingRequiredField("filenames")
        if not isinstance(self.filenames, list):
            self.filenames = [self.filenames] if self.filenames is not None else []
        self.filenames = [v if isinstance(v, str) else str(v) for v in self.filenames]

        if self.dataset_type_custom is not None and not isinstance(self.dataset_type_custom, str):
            self.dataset_type_custom = str(self.dataset_type_custom)

        if self.author_list_for_citation is not None and not isinstance(self.author_list_for_citation, str):
            self.author_list_for_citation = str(self.author_list_for_citation)

        if self.license is not None and not isinstance(self.license, URI):
            self.license = URI(self.license)

        if self.fair_use_data_request is not None and not isinstance(self.fair_use_data_request, str):
            self.fair_use_data_request = str(self.fair_use_data_request)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FieldDataset(Dataset):
    """
    A field or observational dataset related to an OAE experiment. Contains fields specific to in-situ data collection
    such as platform information, calibration files, QC flags, and measured variables.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["FieldDataset"]
    class_class_curie: ClassVar[str] = "oae:FieldDataset"
    class_name: ClassVar[str] = "FieldDataset"
    class_model_uri: ClassVar[URIRef] = OAE.FieldDataset

    name: str = None
    description: str = None
    project_id: str = None
    experiment_id: str = None
    dataset_type: Union[str, "DatasetType"] = None
    data_submitter: Union[dict, Person] = None
    filenames: Union[str, List[str]] = None
    temporal_coverage: str = None
    data_product_type: Union[str, "DataProductType"] = None
    platform_info: Union[dict, "Platform"] = None
    qc_flag_scheme: Optional[str] = None
    calibration_files: Optional[Union[str, List[str]]] = empty_list()
    variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.temporal_coverage):
            self.MissingRequiredField("temporal_coverage")
        if not isinstance(self.temporal_coverage, str):
            self.temporal_coverage = str(self.temporal_coverage)

        if self._is_empty(self.data_product_type):
            self.MissingRequiredField("data_product_type")
        if not isinstance(self.data_product_type, DataProductType):
            self.data_product_type = DataProductType(self.data_product_type)

        if self._is_empty(self.platform_info):
            self.MissingRequiredField("platform_info")
        if not isinstance(self.platform_info, Platform):
            self.platform_info = Platform(**as_dict(self.platform_info))

        if self.qc_flag_scheme is not None and not isinstance(self.qc_flag_scheme, str):
            self.qc_flag_scheme = str(self.qc_flag_scheme)

        if not isinstance(self.calibration_files, list):
            self.calibration_files = [self.calibration_files] if self.calibration_files is not None else []
        self.calibration_files = [v if isinstance(v, str) else str(v) for v in self.calibration_files]

        self._normalize_inlined_as_dict(slot_name="variables", slot_type=Variable, key_name="dataset_variable_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelSimulationDataset(Dataset):
    """
    A model simulation output dataset. Contains fields specific to computational model output including simulation
    configuration, output variables, and hardware information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ModelSimulationDataset"]
    class_class_curie: ClassVar[str] = "oae:ModelSimulationDataset"
    class_name: ClassVar[str] = "ModelSimulationDataset"
    class_model_uri: ClassVar[URIRef] = OAE.ModelSimulationDataset

    name: str = None
    description: str = None
    project_id: str = None
    experiment_id: str = None
    dataset_type: Union[str, "DatasetType"] = None
    data_submitter: Union[dict, Person] = None
    filenames: Union[str, List[str]] = None
    simulation_type: Union[str, "SimulationType"] = None
    start_datetime: Union[str, XSDDateTime] = None
    end_datetime: Union[str, XSDDateTime] = None
    spin_up_protocol: Optional[str] = None
    output_frequency: Optional[str] = None
    time_stepping_scheme: Optional[str] = None
    alkalinity_perturbation_description: Optional[str] = None
    hardware_configuration: Optional[Union[dict, "HardwareConfiguration"]] = None
    model_output_variables: Optional[Union[Union[str, "ModelSimulationVariable"], List[Union[str, "ModelSimulationVariable"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.simulation_type):
            self.MissingRequiredField("simulation_type")
        if not isinstance(self.simulation_type, SimulationType):
            self.simulation_type = SimulationType(self.simulation_type)

        if self._is_empty(self.start_datetime):
            self.MissingRequiredField("start_datetime")
        if not isinstance(self.start_datetime, XSDDateTime):
            self.start_datetime = XSDDateTime(self.start_datetime)

        if self._is_empty(self.end_datetime):
            self.MissingRequiredField("end_datetime")
        if not isinstance(self.end_datetime, XSDDateTime):
            self.end_datetime = XSDDateTime(self.end_datetime)

        if self.spin_up_protocol is not None and not isinstance(self.spin_up_protocol, str):
            self.spin_up_protocol = str(self.spin_up_protocol)

        if self.output_frequency is not None and not isinstance(self.output_frequency, str):
            self.output_frequency = str(self.output_frequency)

        if self.time_stepping_scheme is not None and not isinstance(self.time_stepping_scheme, str):
            self.time_stepping_scheme = str(self.time_stepping_scheme)

        if self.alkalinity_perturbation_description is not None and not isinstance(self.alkalinity_perturbation_description, str):
            self.alkalinity_perturbation_description = str(self.alkalinity_perturbation_description)

        if self.hardware_configuration is not None and not isinstance(self.hardware_configuration, HardwareConfiguration):
            self.hardware_configuration = HardwareConfiguration(**as_dict(self.hardware_configuration))

        if not isinstance(self.model_output_variables, list):
            self.model_output_variables = [self.model_output_variables] if self.model_output_variables is not None else []
        self.model_output_variables = [v if isinstance(v, ModelSimulationVariable) else ModelSimulationVariable(v) for v in self.model_output_variables]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HardwareConfiguration(YAMLRoot):
    """
    Details about the computational hardware used to run a model simulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["HardwareConfiguration"]
    class_class_curie: ClassVar[str] = "oae:HardwareConfiguration"
    class_name: ClassVar[str] = "HardwareConfiguration"
    class_model_uri: ClassVar[URIRef] = OAE.HardwareConfiguration

    machine: Optional[str] = None
    operating_system: Optional[str] = None
    cpu_gpu_details: Optional[str] = None
    memory: Optional[str] = None
    storage: Optional[str] = None
    parallelization: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.machine is not None and not isinstance(self.machine, str):
            self.machine = str(self.machine)

        if self.operating_system is not None and not isinstance(self.operating_system, str):
            self.operating_system = str(self.operating_system)

        if self.cpu_gpu_details is not None and not isinstance(self.cpu_gpu_details, str):
            self.cpu_gpu_details = str(self.cpu_gpu_details)

        if self.memory is not None and not isinstance(self.memory, str):
            self.memory = str(self.memory)

        if self.storage is not None and not isinstance(self.storage, str):
            self.storage = str(self.storage)

        if self.parallelization is not None and not isinstance(self.parallelization, str):
            self.parallelization = str(self.parallelization)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Platform(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Platform"]
    class_class_curie: ClassVar[str] = "oae:Platform"
    class_name: ClassVar[str] = "Platform"
    class_model_uri: ClassVar[URIRef] = OAE.Platform

    platform_type: Union[str, "PlatformType"] = None
    name: Optional[str] = None
    platform_id: Optional[str] = None
    owner: Optional[str] = None
    country: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.platform_type):
            self.MissingRequiredField("platform_type")
        if not isinstance(self.platform_type, PlatformType):
            self.platform_type = PlatformType(self.platform_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.platform_id is not None and not isinstance(self.platform_id, str):
            self.platform_id = str(self.platform_id)

        if self.owner is not None and not isinstance(self.owner, str):
            self.owner = str(self.owner)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Model(Experiment):
    """
    A computational model experiment related to OAE.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Model"]
    class_class_curie: ClassVar[str] = "oae:Model"
    class_name: ClassVar[str] = "Model"
    class_model_uri: ClassVar[URIRef] = OAE.Model

    description: str = None
    spatial_coverage: Union[dict, SpatialCoverage] = None
    project_id: str = None
    experiment_id: str = None
    experiment_type: Union[str, "ExperimentType"] = None
    principal_investigators: Union[Union[dict, Person], List[Union[dict, Person]]] = None
    start_datetime: Union[str, XSDDateTime] = None
    model_configuration: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()
    model_components: Optional[Union[Union[dict, "ModelComponent"], List[Union[dict, "ModelComponent"]]]] = empty_list()
    grid_details: Optional[Union[Union[dict, "ModelGrid"], List[Union[dict, "ModelGrid"]]]] = empty_list()
    input_details: Optional[Union[dict, "ModelInputDetails"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.model_configuration, list):
            self.model_configuration = [self.model_configuration] if self.model_configuration is not None else []
        self.model_configuration = [v if isinstance(v, URI) else URI(v) for v in self.model_configuration]

        if not isinstance(self.model_components, list):
            self.model_components = [self.model_components] if self.model_components is not None else []
        self.model_components = [v if isinstance(v, ModelComponent) else ModelComponent(**as_dict(v)) for v in self.model_components]

        if not isinstance(self.grid_details, list):
            self.grid_details = [self.grid_details] if self.grid_details is not None else []
        self.grid_details = [v if isinstance(v, ModelGrid) else ModelGrid(**as_dict(v)) for v in self.grid_details]

        if self.input_details is not None and not isinstance(self.input_details, ModelInputDetails):
            self.input_details = ModelInputDetails(**as_dict(self.input_details))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelComponent(YAMLRoot):
    """
    A component of a model (e.g., physics, biogeochemistry/ecosystem).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ModelComponent"]
    class_class_curie: ClassVar[str] = "oae:ModelComponent"
    class_name: ClassVar[str] = "ModelComponent"
    class_model_uri: ClassVar[URIRef] = OAE.ModelComponent

    model_component_type: Union[str, "ModelComponentType"] = None
    name: str = None
    description: Optional[str] = None
    model_component_type_custom: Optional[str] = None
    version: Optional[str] = None
    codebase: Optional[Union[str, URI]] = None
    references: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.model_component_type):
            self.MissingRequiredField("model_component_type")
        if not isinstance(self.model_component_type, ModelComponentType):
            self.model_component_type = ModelComponentType(self.model_component_type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.model_component_type_custom is not None and not isinstance(self.model_component_type_custom, str):
            self.model_component_type_custom = str(self.model_component_type_custom)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.codebase is not None and not isinstance(self.codebase, URI):
            self.codebase = URI(self.codebase)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, URI) else URI(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelGrid(YAMLRoot):
    """
    Details about a model grid. Use multiple ModelGrid entries to describe nested or multi-grid configurations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ModelGrid"]
    class_class_curie: ClassVar[str] = "oae:ModelGrid"
    class_name: ClassVar[str] = "ModelGrid"
    class_model_uri: ClassVar[URIRef] = OAE.ModelGrid

    grid_type: Union[str, "GridType"] = None
    grid_name: Optional[str] = None
    grid_geometry: Optional[str] = None
    region: Optional[str] = None
    spatial_coverage: Optional[Union[dict, SpatialCoverage]] = None
    arrangement: Optional[str] = None
    vertical_coordinate_type: Optional[str] = None
    n_x: Optional[int] = None
    n_y: Optional[int] = None
    n_z: Optional[int] = None
    n_nodes: Optional[int] = None
    horizontal_resolution_range: Optional[str] = None
    vertical_resolution_range: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.grid_type):
            self.MissingRequiredField("grid_type")
        if not isinstance(self.grid_type, GridType):
            self.grid_type = GridType(self.grid_type)

        if self.grid_name is not None and not isinstance(self.grid_name, str):
            self.grid_name = str(self.grid_name)

        if self.grid_geometry is not None and not isinstance(self.grid_geometry, str):
            self.grid_geometry = str(self.grid_geometry)

        if self.region is not None and not isinstance(self.region, str):
            self.region = str(self.region)

        if self.spatial_coverage is not None and not isinstance(self.spatial_coverage, SpatialCoverage):
            self.spatial_coverage = SpatialCoverage(**as_dict(self.spatial_coverage))

        if self.arrangement is not None and not isinstance(self.arrangement, str):
            self.arrangement = str(self.arrangement)

        if self.vertical_coordinate_type is not None and not isinstance(self.vertical_coordinate_type, str):
            self.vertical_coordinate_type = str(self.vertical_coordinate_type)

        if self.n_x is not None and not isinstance(self.n_x, int):
            self.n_x = int(self.n_x)

        if self.n_y is not None and not isinstance(self.n_y, int):
            self.n_y = int(self.n_y)

        if self.n_z is not None and not isinstance(self.n_z, int):
            self.n_z = int(self.n_z)

        if self.n_nodes is not None and not isinstance(self.n_nodes, int):
            self.n_nodes = int(self.n_nodes)

        if self.horizontal_resolution_range is not None and not isinstance(self.horizontal_resolution_range, str):
            self.horizontal_resolution_range = str(self.horizontal_resolution_range)

        if self.vertical_resolution_range is not None and not isinstance(self.vertical_resolution_range, str):
            self.vertical_resolution_range = str(self.vertical_resolution_range)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelInputDetails(YAMLRoot):
    """
    Details about input data sources used to drive the model.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["ModelInputDetails"]
    class_class_curie: ClassVar[str] = "oae:ModelInputDetails"
    class_name: ClassVar[str] = "ModelInputDetails"
    class_model_uri: ClassVar[URIRef] = OAE.ModelInputDetails

    bathymetry: Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]] = empty_list()
    initial_conditions: Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]] = empty_list()
    boundary_conditions: Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]] = empty_list()
    atmospheric_forcing: Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]] = empty_list()
    tidal_forcing: Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]] = empty_list()
    river_sediment_flux_details: Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]] = empty_list()
    processing_of_input_data: Optional[str] = None
    processing_code: Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.bathymetry, list):
            self.bathymetry = [self.bathymetry] if self.bathymetry is not None else []
        self.bathymetry = [v if isinstance(v, NamedLink) else NamedLink(**as_dict(v)) for v in self.bathymetry]

        if not isinstance(self.initial_conditions, list):
            self.initial_conditions = [self.initial_conditions] if self.initial_conditions is not None else []
        self.initial_conditions = [v if isinstance(v, NamedLink) else NamedLink(**as_dict(v)) for v in self.initial_conditions]

        if not isinstance(self.boundary_conditions, list):
            self.boundary_conditions = [self.boundary_conditions] if self.boundary_conditions is not None else []
        self.boundary_conditions = [v if isinstance(v, NamedLink) else NamedLink(**as_dict(v)) for v in self.boundary_conditions]

        if not isinstance(self.atmospheric_forcing, list):
            self.atmospheric_forcing = [self.atmospheric_forcing] if self.atmospheric_forcing is not None else []
        self.atmospheric_forcing = [v if isinstance(v, NamedLink) else NamedLink(**as_dict(v)) for v in self.atmospheric_forcing]

        if not isinstance(self.tidal_forcing, list):
            self.tidal_forcing = [self.tidal_forcing] if self.tidal_forcing is not None else []
        self.tidal_forcing = [v if isinstance(v, NamedLink) else NamedLink(**as_dict(v)) for v in self.tidal_forcing]

        if not isinstance(self.river_sediment_flux_details, list):
            self.river_sediment_flux_details = [self.river_sediment_flux_details] if self.river_sediment_flux_details is not None else []
        self.river_sediment_flux_details = [v if isinstance(v, NamedLink) else NamedLink(**as_dict(v)) for v in self.river_sediment_flux_details]

        if self.processing_of_input_data is not None and not isinstance(self.processing_of_input_data, str):
            self.processing_of_input_data = str(self.processing_of_input_data)

        if not isinstance(self.processing_code, list):
            self.processing_code = [self.processing_code] if self.processing_code is not None else []
        self.processing_code = [v if isinstance(v, NamedLink) else NamedLink(**as_dict(v)) for v in self.processing_code]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnalyzingInstrument(YAMLRoot):
    """
    Base class for scientific instruments used in analyzing samples for measurement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["AnalyzingInstrument"]
    class_class_curie: ClassVar[str] = "oae:AnalyzingInstrument"
    class_name: ClassVar[str] = "AnalyzingInstrument"
    class_model_uri: ClassVar[URIRef] = OAE.AnalyzingInstrument

    instrument_type: Union[str, "AnalyzingInstrumentType"] = None
    accuracy: str = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    instrument_type_custom: Optional[str] = None
    serial_number: Optional[str] = None
    precision: Optional[str] = None
    calibration: Optional[Union[dict, "Calibration"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.instrument_type):
            self.MissingRequiredField("instrument_type")
        if not isinstance(self.instrument_type, AnalyzingInstrumentType):
            self.instrument_type = AnalyzingInstrumentType(self.instrument_type)

        if self._is_empty(self.accuracy):
            self.MissingRequiredField("accuracy")
        if not isinstance(self.accuracy, str):
            self.accuracy = str(self.accuracy)

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        if self.instrument_type_custom is not None and not isinstance(self.instrument_type_custom, str):
            self.instrument_type_custom = str(self.instrument_type_custom)

        if self.serial_number is not None and not isinstance(self.serial_number, str):
            self.serial_number = str(self.serial_number)

        if self.precision is not None and not isinstance(self.precision, str):
            self.precision = str(self.precision)

        if self.calibration is not None and not isinstance(self.calibration, Calibration):
            self.calibration = Calibration(**as_dict(self.calibration))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PHInstrument(AnalyzingInstrument):
    """
    pH measurement instrument with dye-based calibration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["PHInstrument"]
    class_class_curie: ClassVar[str] = "oae:PHInstrument"
    class_name: ClassVar[str] = "PHInstrument"
    class_model_uri: ClassVar[URIRef] = OAE.PHInstrument

    instrument_type: Union[str, "AnalyzingInstrumentType"] = None
    accuracy: str = None
    calibration: Union[dict, "PHCalibration"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.calibration):
            self.MissingRequiredField("calibration")
        if not isinstance(self.calibration, PHCalibration):
            self.calibration = PHCalibration(**as_dict(self.calibration))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CRMInstrument(AnalyzingInstrument):
    """
    Instrument calibrated with Certified Reference Materials, used for DIC and TA measurements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["CRMInstrument"]
    class_class_curie: ClassVar[str] = "oae:CRMInstrument"
    class_name: ClassVar[str] = "CRMInstrument"
    class_model_uri: ClassVar[URIRef] = OAE.CRMInstrument

    instrument_type: Union[str, "AnalyzingInstrumentType"] = None
    accuracy: str = None
    calibration: Union[dict, "CRMCalibration"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.calibration):
            self.MissingRequiredField("calibration")
        if not isinstance(self.calibration, CRMCalibration):
            self.calibration = CRMCalibration(**as_dict(self.calibration))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CO2GasDetector(AnalyzingInstrument):
    """
    CO2 gas detector with standard gas calibration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["CO2GasDetector"]
    class_class_curie: ClassVar[str] = "oae:CO2GasDetector"
    class_name: ClassVar[str] = "CO2GasDetector"
    class_model_uri: ClassVar[URIRef] = OAE.CO2GasDetector

    instrument_type: Union[str, "AnalyzingInstrumentType"] = None
    accuracy: str = None
    detector_type: str = None
    calibration: Union[dict, "CO2Calibration"] = None
    manufacturer: str = None
    resolution: Optional[str] = None
    uncertainty: Optional[str] = None
    analyzing_instrument_type: Optional[str] = None
    model: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.detector_type):
            self.MissingRequiredField("detector_type")
        if not isinstance(self.detector_type, str):
            self.detector_type = str(self.detector_type)

        if self._is_empty(self.calibration):
            self.MissingRequiredField("calibration")
        if not isinstance(self.calibration, CO2Calibration):
            self.calibration = CO2Calibration(**as_dict(self.calibration))

        if self._is_empty(self.manufacturer):
            self.MissingRequiredField("manufacturer")
        if not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.resolution is not None and not isinstance(self.resolution, str):
            self.resolution = str(self.resolution)

        if self.uncertainty is not None and not isinstance(self.uncertainty, str):
            self.uncertainty = str(self.uncertainty)

        if self.analyzing_instrument_type is not None and not isinstance(self.analyzing_instrument_type, str):
            self.analyzing_instrument_type = str(self.analyzing_instrument_type)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Calibration(YAMLRoot):
    """
    Base calibration information for instruments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["Calibration"]
    class_class_curie: ClassVar[str] = "oae:Calibration"
    class_name: ClassVar[str] = "Calibration"
    class_model_uri: ClassVar[URIRef] = OAE.Calibration

    technique_description: str = None
    calibration_location: Optional[Union[str, "CalibrationLocation"]] = None
    method_reference: Optional[str] = None
    frequency: Optional[str] = None
    last_calibration_date: Optional[Union[str, XSDDateTime]] = None
    calibration_certificates: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.technique_description):
            self.MissingRequiredField("technique_description")
        if not isinstance(self.technique_description, str):
            self.technique_description = str(self.technique_description)

        if self.calibration_location is not None and not isinstance(self.calibration_location, CalibrationLocation):
            self.calibration_location = CalibrationLocation(self.calibration_location)

        if self.method_reference is not None and not isinstance(self.method_reference, str):
            self.method_reference = str(self.method_reference)

        if self.frequency is not None and not isinstance(self.frequency, str):
            self.frequency = str(self.frequency)

        if self.last_calibration_date is not None and not isinstance(self.last_calibration_date, XSDDateTime):
            self.last_calibration_date = XSDDateTime(self.last_calibration_date)

        if self.calibration_certificates is not None and not isinstance(self.calibration_certificates, str):
            self.calibration_certificates = str(self.calibration_certificates)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CRMCalibration(Calibration):
    """
    Calibration using Certified Reference Materials, used for DIC and TA instruments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["CRMCalibration"]
    class_class_curie: ClassVar[str] = "oae:CRMCalibration"
    class_name: ClassVar[str] = "CRMCalibration"
    class_model_uri: ClassVar[URIRef] = OAE.CRMCalibration

    technique_description: str = None
    crm_manufacturer: str = None
    crm_batch_number: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.crm_manufacturer):
            self.MissingRequiredField("crm_manufacturer")
        if not isinstance(self.crm_manufacturer, str):
            self.crm_manufacturer = str(self.crm_manufacturer)

        if self._is_empty(self.crm_batch_number):
            self.MissingRequiredField("crm_batch_number")
        if not isinstance(self.crm_batch_number, str):
            self.crm_batch_number = str(self.crm_batch_number)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PHCalibration(Calibration):
    """
    pH instrument calibration with dye information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["PHCalibration"]
    class_class_curie: ClassVar[str] = "oae:PHCalibration"
    class_name: ClassVar[str] = "pHCalibration"
    class_model_uri: ClassVar[URIRef] = OAE.PHCalibration

    technique_description: str = None
    calibration_temperature: Optional[str] = None
    dye_type_and_manufacturer: Optional[str] = None
    dye_purified: Optional[Union[bool, Bool]] = None
    correction_for_unpurified_dye: Optional[str] = None
    dye_correction_method: Optional[str] = None
    ph_of_standards: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.calibration_temperature is not None and not isinstance(self.calibration_temperature, str):
            self.calibration_temperature = str(self.calibration_temperature)

        if self.dye_type_and_manufacturer is not None and not isinstance(self.dye_type_and_manufacturer, str):
            self.dye_type_and_manufacturer = str(self.dye_type_and_manufacturer)

        if self.dye_purified is not None and not isinstance(self.dye_purified, Bool):
            self.dye_purified = Bool(self.dye_purified)

        if self.correction_for_unpurified_dye is not None and not isinstance(self.correction_for_unpurified_dye, str):
            self.correction_for_unpurified_dye = str(self.correction_for_unpurified_dye)

        if self.dye_correction_method is not None and not isinstance(self.dye_correction_method, str):
            self.dye_correction_method = str(self.dye_correction_method)

        if self.ph_of_standards is not None and not isinstance(self.ph_of_standards, str):
            self.ph_of_standards = str(self.ph_of_standards)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CO2Calibration(Calibration):
    """
    CO2 gas detector calibration with standard gas information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["CO2Calibration"]
    class_class_curie: ClassVar[str] = "oae:CO2Calibration"
    class_name: ClassVar[str] = "CO2Calibration"
    class_model_uri: ClassVar[URIRef] = OAE.CO2Calibration

    technique_description: str = None
    calibration_temperature: Optional[str] = None
    standard_gas_info: Optional[Union[dict, "StandardGas"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.calibration_temperature is not None and not isinstance(self.calibration_temperature, str):
            self.calibration_temperature = str(self.calibration_temperature)

        if self.standard_gas_info is not None and not isinstance(self.standard_gas_info, StandardGas):
            self.standard_gas_info = StandardGas(**as_dict(self.standard_gas_info))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StandardGas(YAMLRoot):
    """
    Standard gas used for CO2 calibration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE["StandardGas"]
    class_class_curie: ClassVar[str] = "oae:StandardGas"
    class_name: ClassVar[str] = "StandardGas"
    class_model_uri: ClassVar[URIRef] = OAE.StandardGas

    manufacturer: str = None
    concentration: str = None
    uncertainty: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.manufacturer):
            self.MissingRequiredField("manufacturer")
        if not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self._is_empty(self.concentration):
            self.MissingRequiredField("concentration")
        if not isinstance(self.concentration, str):
            self.concentration = str(self.concentration)

        if self.uncertainty is not None and not isinstance(self.uncertainty, str):
            self.uncertainty = str(self.uncertainty)

        super().__post_init__(**kwargs)


# Enumerations
class DatasetType(EnumDefinitionImpl):
    """
    Type of dataset being submitted. This usually
    """
    dosing = PermissibleValue(
        text="dosing",
        description="Variables such as dosing_onoff, dosing_rate, and flow_rate should be included here.")
    cast = PermissibleValue(
        text="cast",
        description="Vertical profiles (e.g., optical packages, CTD)")
    bottle = PermissibleValue(
        text="bottle",
        description="""Any other types of measurements from water samples collected at discrete depths (e.g., nutrients)""")
    flow_thru = PermissibleValue(
        text="flow_thru",
        description="Continuous data (e.g., shipboard, underway flow through system)")
    pigment = PermissibleValue(
        text="pigment",
        description="For laboratory measured pigment data (e.g. fluorometry, spectrophotometry, HPLC)")
    marine_snow_catcher = PermissibleValue(
        text="marine_snow_catcher",
        description="For various types of marine snow catcher data")
    mooring = PermissibleValue(
        text="mooring",
        description="Moored and buoy data")
    drifter = PermissibleValue(
        text="drifter",
        description="Drifter and drogue data")
    airborne = PermissibleValue(
        text="airborne",
        description="Measurements made via an aircraft")
    diver = PermissibleValue(
        text="diver",
        description="For measurements made by a diver")
    auv = PermissibleValue(
        text="auv",
        description="Measurements made by an autonomous underwater vehicle")
    asv = PermissibleValue(
        text="asv",
        description="Measurements made by an autonomous surface vehicle")
    experimental = PermissibleValue(
        text="experimental",
        description="""Measurements that have a non-geospatial aspect (e.g., incubations or other laboratory measurements, etc.)""")
    sediment_trap = PermissibleValue(
        text="sediment_trap",
        description="Measurements from a sediment trap platform")
    taxonomy = PermissibleValue(
        text="taxonomy",
        description="""Data whose purpose is the classification or annotation of phytoplankton, zooplankton, or other marine groups.""")
    sediment = PermissibleValue(
        text="sediment",
        description="Measurements from sediment samples (e.g., core samples, grab samples)")
    model_output = PermissibleValue(
        text="model_output",
        description="Data output from model experiments")
    socioeconomic = PermissibleValue(
        text="socioeconomic",
        description="Information (quantitative or qualitative) from socioeconomic studies")
    net_tow = PermissibleValue(
        text="net_tow",
        description="For measurements captured via net (e.g., zooplankton via MOCNESS)")
    other = PermissibleValue(
        text="other",
        description="""For data types not included in the controlled vocabulary. Please fill in a the `dataset_type_custom` field with a more specific name for the custom mCDR data type.""")

    _defn = EnumDefinition(
        name="DatasetType",
        description="Type of dataset being submitted. This usually",
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
    tracer_study = PermissibleValue(
        text="tracer_study",
        description="Tracer study experiment (eg- dye or gas tracer study)")
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

class TracerForm(EnumDefinitionImpl):
    """
    Forms of tracer used in tracer studies
    """
    gas = PermissibleValue(
        text="gas",
        description="Gas tracer")
    dye = PermissibleValue(
        text="dye",
        description="Dye tracer (eg- rhodamine)")
    other = PermissibleValue(
        text="other",
        description="Other tracer form not covered by standard categories")

    _defn = EnumDefinition(
        name="TracerForm",
        description="Forms of tracer used in tracer studies",
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
    other = PermissibleValue(
        text="other",
        description="Enter a custom value in the field provided")

    _defn = EnumDefinition(
        name="FeedstockType",
        description="""Types of materials used for alkalinity addition, as sourced from NCEI's OCADS controlled vocabulary: https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/vocabularies/alkalinization-types.html""",
    )

class GridType(EnumDefinitionImpl):
    """
    Type of grid in a multi-grid or nested model configuration
    """
    inner_grid = PermissibleValue(
        text="inner_grid",
        description="Inner (nested, higher-resolution) grid")
    outer_grid = PermissibleValue(
        text="outer_grid",
        description="Outer (coarser-resolution) grid")
    single_grid = PermissibleValue(
        text="single_grid",
        description="Single grid (no nesting)")

    _defn = EnumDefinition(
        name="GridType",
        description="Type of grid in a multi-grid or nested model configuration",
    )

class ModelComponentType(EnumDefinitionImpl):
    """
    Type of model component
    """
    physics = PermissibleValue(
        text="physics",
        description="Physical model component (e.g., ocean circulation)")
    bgc_ecosystem = PermissibleValue(
        text="bgc_ecosystem",
        description="Biogeochemical or ecosystem model component")
    sea_ice = PermissibleValue(
        text="sea_ice",
        description="Sea Ice model component")
    atmosphere = PermissibleValue(
        text="atmosphere",
        description="Atmosphere model component")
    other = PermissibleValue(
        text="other",
        description="Other model component (e.g., sea ice, sediment, atmosphere)")

    _defn = EnumDefinition(
        name="ModelComponentType",
        description="Type of model component",
    )

class DataProductType(EnumDefinitionImpl):

    originally_collected_dataset = PermissibleValue(
        text="originally_collected_dataset",
        description="A dataset collected from a research cruise or laboratory experiment")
    data_compilation_product = PermissibleValue(
        text="data_compilation_product",
        description="(e.g., SOCAT, GLODAP)")
    derived_product = PermissibleValue(
        text="derived_product",
        description="(e.g. gridded products, or model output).")

    _defn = EnumDefinition(
        name="DataProductType",
    )

class SimulationType(EnumDefinitionImpl):
    """
    Type of model simulation dataset
    """
    counterfactual = PermissibleValue(
        text="counterfactual",
        description="Control/baseline simulation without alkalinity perturbation")
    perturbation = PermissibleValue(
        text="perturbation",
        description="Simulation with alkalinity perturbation applied")

    _defn = EnumDefinition(
        name="SimulationType",
        description="Type of model simulation dataset",
    )

class ModelSimulationVariable(EnumDefinitionImpl):
    """
    Variables commonly included in model simulation output datasets
    """
    air_sea_co2_flux = PermissibleValue(
        text="air_sea_co2_flux",
        description="Air-sea exchange of carbon dioxide")
    dissolved_inorganic_carbon = PermissibleValue(
        text="dissolved_inorganic_carbon",
        description="Dissolved inorganic carbon (DIC)")
    total_alkalinity = PermissibleValue(
        text="total_alkalinity",
        description="Total alkalinity (TA)")
    temperature = PermissibleValue(
        text="temperature",
        description="Temperature")
    salinity = PermissibleValue(
        text="salinity",
        description="Salinity")
    ph = PermissibleValue(
        text="ph",
        description="pH of seawater")
    phytoplankton = PermissibleValue(
        text="phytoplankton",
        description="Phytoplankton biomass or concentration")
    horizontal_velocity = PermissibleValue(
        text="horizontal_velocity",
        description="Horizontal velocity components (u, v)")
    vertical_velocity = PermissibleValue(
        text="vertical_velocity",
        description="Vertical velocity component (w)")
    other = PermissibleValue(
        text="other",
        description="Other model output variable not listed above")

    _defn = EnumDefinition(
        name="ModelSimulationVariable",
        description="Variables commonly included in model simulation output datasets",
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

class PlatformType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="PlatformType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/99/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/99/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/6D/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/6D/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/3C/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/3C/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/36/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/36/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/18/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/18/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/30/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/30/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/61/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/61/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/26/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/26/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/16/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/16/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/3A/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/3A/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/41/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/41/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/72/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/72/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/43/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/43/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/15/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/15/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/13/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/13/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/6A/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/6A/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/44/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/44/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/68/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/68/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/33/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/33/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/19/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/19/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/11/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/11/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/12/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/12/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/23/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/23/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/17/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/17/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/3B/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/3B/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/45/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/45/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/42/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/42/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/47/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/47/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/14/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/14/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/71/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/71/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/46/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/46/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/20/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/20/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/27/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/27/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/25/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/25/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/3Z/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/3Z/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/48/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/48/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/31/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/31/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/62/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/62/",
                meaning=None))
        setattr(cls, "http://vocab.nerc.ac.uk/collection/L06/current/67/",
            PermissibleValue(
                text="http://vocab.nerc.ac.uk/collection/L06/current/67/",
                meaning=None))

class MassConcentrationUnit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MassConcentrationUnit",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "unit:KiloGM-PER-M3",
            PermissibleValue(
                text="unit:KiloGM-PER-M3",
                meaning=UNIT["KiloGM-PER-M3"]))
        setattr(cls, "unit:MicroGM-PER-L",
            PermissibleValue(
                text="unit:MicroGM-PER-L",
                meaning=UNIT["MicroGM-PER-L"]))
        setattr(cls, "unit:MicroGM-PER-L-DAY",
            PermissibleValue(
                text="unit:MicroGM-PER-L-DAY",
                meaning=UNIT["MicroGM-PER-L-DAY"]))
        setattr(cls, "unit:MicroGM-PER-MilliL",
            PermissibleValue(
                text="unit:MicroGM-PER-MilliL",
                meaning=UNIT["MicroGM-PER-MilliL"]))
        setattr(cls, "unit:MilliGM-PER-L",
            PermissibleValue(
                text="unit:MilliGM-PER-L",
                meaning=UNIT["MilliGM-PER-L"]))
        setattr(cls, "unit:MilliGM-PER-M3",
            PermissibleValue(
                text="unit:MilliGM-PER-M3",
                meaning=UNIT["MilliGM-PER-M3"]))
        setattr(cls, "unit:MilliGM-PER-MilliL",
            PermissibleValue(
                text="unit:MilliGM-PER-MilliL",
                meaning=UNIT["MilliGM-PER-MilliL"]))
        setattr(cls, "unit:NanoGM-PER-L",
            PermissibleValue(
                text="unit:NanoGM-PER-L",
                meaning=UNIT["NanoGM-PER-L"]))
        setattr(cls, "unit:NanoGM-PER-MilliL",
            PermissibleValue(
                text="unit:NanoGM-PER-MilliL",
                meaning=UNIT["NanoGM-PER-MilliL"]))
        setattr(cls, "unit:PicoGM-PER-MilliL",
            PermissibleValue(
                text="unit:PicoGM-PER-MilliL",
                meaning=UNIT["PicoGM-PER-MilliL"]))

class ResearcherIDType(EnumDefinitionImpl):

    orcid = PermissibleValue(text="orcid")
    researcher_id = PermissibleValue(text="researcher_id")
    ocean_expert = PermissibleValue(text="ocean_expert")

    _defn = EnumDefinition(
        name="ResearcherIDType",
    )

class SamplingType(EnumDefinitionImpl):

    discrete = PermissibleValue(text="discrete")
    continuous = PermissibleValue(text="continuous")

    _defn = EnumDefinition(
        name="SamplingType",
    )

class GenesisType(EnumDefinitionImpl):

    measured = PermissibleValue(text="measured")
    calculated = PermissibleValue(text="calculated")

    _defn = EnumDefinition(
        name="GenesisType",
    )

class ObservationType(EnumDefinitionImpl):

    profile = PermissibleValue(text="profile")
    surface_underway = PermissibleValue(text="surface_underway")
    time_series = PermissibleValue(text="time_series")
    laboratory_experiments = PermissibleValue(text="laboratory_experiments")
    mesocosm = PermissibleValue(text="mesocosm")
    field_experiments = PermissibleValue(text="field_experiments")
    natural_analogues = PermissibleValue(text="natural_analogues")
    model_outputs = PermissibleValue(text="model_outputs")

    _defn = EnumDefinition(
        name="ObservationType",
    )

class AppropriateUseQuality(EnumDefinitionImpl):

    weather_quality = PermissibleValue(text="weather_quality")
    climate_quality = PermissibleValue(text="climate_quality")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="AppropriateUseQuality",
    )

class TitrationCellType(EnumDefinitionImpl):

    open = PermissibleValue(text="open")
    closed = PermissibleValue(text="closed")

    _defn = EnumDefinition(
        name="TitrationCellType",
    )

class ConcentrationBasis(EnumDefinitionImpl):
    """
    Whether concentration measurements are expressed per unit volume or per unit mass.
    """
    per_volume = PermissibleValue(
        text="per_volume",
        description="Concentration expressed per unit volume (e.g., μmol/L, mmol/L)")
    per_mass = PermissibleValue(
        text="per_mass",
        description="Concentration expressed per unit mass (e.g., μmol/kg-seawater)")

    _defn = EnumDefinition(
        name="ConcentrationBasis",
        description="Whether concentration measurements are expressed per unit volume or per unit mass.",
    )

class SamplingInstrumentType(EnumDefinitionImpl):

    ctd_rosette = PermissibleValue(
        text="ctd_rosette",
        description="""A CTD rosette consists of a metal frame that houses a collection of sensors and water sampling bottles (e.g., Niskin)""")
    niskin_bottle = PermissibleValue(
        text="niskin_bottle",
        description="""A device that collects an in-situ discrete water sample from any depth and returns it to the surface without contamination by the waters through which it passes, such as a water bottle.""",
        meaning=SDN_L05["30"])
    flow_through_system = PermissibleValue(
        text="flow_through_system",
        description="""A device that continuously supplies a flow of water either to an analytical instrument, over a sensor or from which samples may be drawn.""",
        meaning=SDN_L05["31"])
    flask_for_discrete_co2_measurement = PermissibleValue(
        text="flask_for_discrete_co2_measurement",
        description="""Such flasks are typically made of glass and have a capacity of around one liter. Seawater samples are collected from a specific depth using a Niskin bottle or other sampling device and transferred to the flask without exposing them to the air. The flask is then sealed with a stopper and transported to the laboratory for analysis.""")
    biological_trawl = PermissibleValue(
        text="biological_trawl",
        description="A net towed through the water column designed to sample free-swimming nekton or fish",
        meaning=SDN_L05["23"])
    phytoplankton_net = PermissibleValue(
        text="phytoplankton_net",
        description="""Phytoplankton net is used to collect and identify phytoplankton, which are microscopic plants that form the base of the marine food web.""",
        meaning=SDN_L05["22"])
    zooplankton_net = PermissibleValue(
        text="zooplankton_net",
        description="""Zooplankton net is used to collect and identify zooplankton, which are microscopic animals that feed on phytoplankton and are important prey for many marine organisms.""",
        meaning=SDN_L05["22"])
    edna_sampler = PermissibleValue(
        text="edna_sampler",
        description="""Environmental DNA (eDNA) samplers: used to collect and analyze genetic material shed by marine organisms, which can provide information about their distribution, abundance, and diversity.""")
    autonomous_sensor = PermissibleValue(
        text="autonomous_sensor",
        description="""A device used in the measurement of a variety of oceanographic variables that functions autonomously""")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SamplingInstrumentType",
    )

class AnalyzingInstrumentType(EnumDefinitionImpl):

    ctd_sensor = PermissibleValue(
        text="ctd_sensor",
        description="""A reusable instrument that always simultaneously measures conductivity and temperature (for salinity) and pressure (for depth).""",
        meaning=SDN_L05["130"])
    flow_through_system = PermissibleValue(
        text="flow_through_system",
        description="""A device that continuously supplies a flow of water either to an analytical instrument, over a sensor or from which samples may be drawn.""",
        meaning=SDN_L05["31"])
    thermosalinograph = PermissibleValue(
        text="thermosalinograph",
        description="""Temperature and conductivity sensors mounted on a sea-surface platform continuously measuring a surface water supply.""",
        meaning=SDN_L05["133"])
    salinometer_for_discrete_salinity_measurement = PermissibleValue(
        text="salinometer_for_discrete_salinity_measurement",
        description="""Instruments that measure the salinity of a collected water sample based on its electrical conductivity or optical properties.""",
        meaning=SDN_L05["LAB30"])
    dic_analyzers_based_on_coulometers = PermissibleValue(
        text="dic_analyzers_based_on_coulometers",
        description="""DIC coulometers are widely used in oceanographic research to measure the concentration of dissolved inorganic carbon in seawater samples. They are often coupled with computer-controlled automated dynamic headspace analyzers that extracts total carbon dioxide from seawater using Single-Operator Multiparameter Metabolic Analyzers (SOMMAs).""")
    dic_analyzers_based_on_co2_gas_detectors = PermissibleValue(
        text="dic_analyzers_based_on_co2_gas_detectors",
        description="""DIC analyzers based on a CO2 gas detector including Non-dispersive infrared absorption (NDIR) (e.g., Licor LI-850), Cavity Enhanced Absorption Spectroscopy (e.g., Licor's LI-7815), and Cavity Ring-Down Spectroscopy (CRDS) (e.g., Picarro G2131i) detectors.""")
    autonomous_dic_sensor = PermissibleValue(
        text="autonomous_dic_sensor",
        description="""Autonomous dissolved inorganic carbon (DIC) sensors are devices that can measure the concentration of DIC in seawater or other natural waters in situ, without the need for manual sampling and laboratory analysis.""",
        meaning=SDN_L05["86"])
    alkalinity_titrator = PermissibleValue(
        text="alkalinity_titrator",
        description="""An alkalinity titrator is a device used to measure the total alkalinity of a seawater by titration.""",
        meaning=SDN_L05["LAB12"])
    autonomous_ta_sensor = PermissibleValue(
        text="autonomous_ta_sensor",
        description="""Autonomous total alkalinity (TA) sensors are devices that can measure the concentration of TA in seawater or other natural waters in situ, without the need for manual sampling and laboratory analysis.""")
    showerhead_equilibrator = PermissibleValue(
        text="showerhead_equilibrator",
        description="""This type of equilibrator works by spraying seawater into a gas chamber, allowing the CO2 in the water to equilibrate with a gas mixture in the chamber.""",
        meaning=SDN_L05["EQUIL"])
    floating_air_water_equilibrator = PermissibleValue(
        text="floating_air_water_equilibrator",
        description="""An \"h\"-shaped bubble equilibrator assembly commonly used in MAPCO2 systems on moorings. For more information, refer to Friederich et al. (1995).""",
        meaning=SDN_L05["EQUIL"])
    membrane_equilibrator = PermissibleValue(
        text="membrane_equilibrator",
        description="""While seawater is passed through a membrane, CO2 in the water diffuses across the membrane and equilibrates with the gas mixture, which is then analyzed to determine the CO2 concentration.""",
        meaning=SDN_L05["EQUIL"])
    spectrophotometer = PermissibleValue(
        text="spectrophotometer",
        description="""Instruments measuring the relative absorption of electromagnetic radiation of different wavelengths in the near infra-red, visible and ultraviolet wavebands by samples.""",
        meaning=SDN_L05["LAB20"])
    handheld_ph_spectrophotometer = PermissibleValue(
        text="handheld_ph_spectrophotometer",
        description="""One example of a handheld pH spectrophotometer is the \"pHyter\". Refer to Pardis et al. (2022) for more details.""")
    ph_electrode = PermissibleValue(
        text="ph_electrode",
        description="""A pH electrode, sometimes referred to as a pH probe or pH sensor, is a glass device used to measure the pH of a solution.""",
        meaning=SDN_L05["355"])
    sea_bird_seafet_v1 = PermissibleValue(
        text="sea_bird_seafet_v1",
        description="""A pH sensor. The sensor can be used for ocean acidification, research coral reef sensitivity analysis and environmental monitoring. The sensor measures pH with a range of 6.5 to 9.0. The sensing element is an ion  sensitive field effect transistor. The pH sensor has an initial accuracy of +/-0.05 pH, precision of 0.001 pH and stability of 0.005 pH/month. It can operate in temperatures ranging from 0 deg C to 50 deg C and up to depths of 50 m.""",
        meaning=SDN_L22["TOOL1292"])
    sea_bird_seafet_v2 = PermissibleValue(
        text="sea_bird_seafet_v2",
        description="""A pH sensor. The sensor can be used for ocean acidification, research coral reef sensitivity analysis and environmental monitoring. The sensor measures pH with a range of 6.5 to 9.0. The sensing element is an ion sensitive field effect transistor. V2 implements improvements to the original SeaFET's reliability, data quality, ease of operation, and deployment endurance, with significant changes to how users interface with the instrument. The pH sensor has an accuracy to +/-0.05 pH, precision of 0.004 pH and stability of 0.003 pH/month. It can operate in temperatures ranging from 0 deg C to 50 deg C and up to depths of 50 m.""",
        meaning=SDN_L22["TOOL1293"])
    oxygen_titrator = PermissibleValue(
        text="oxygen_titrator",
        description="""An oxygen titrator is a device used to measure the concentration of dissolved oxygen in a water sample, as required for the Winkler method.""",
        meaning=SDN_L05["LAB12"])
    oxygen_sensor = PermissibleValue(
        text="oxygen_sensor",
        description="""An oxygen sensor or probe or sond, is an electronic device that measures the concentration of dissolved oxygen in the ocean.""",
        meaning=SDN_L05["351"])
    sea_bird_seaphox = PermissibleValue(
        text="sea_bird_seaphox",
        description="""Sea-Bird SeapHOx is a type of oceanographic instrument that measures both the pH and dissolved oxygen concentration of seawater in real-time.""",
        meaning=SDN_L22["TOOL1895"])
    ysi = PermissibleValue(
        text="ysi",
        description="""YSI (Yellow Springs Instruments) is a company that produces a variety of water quality monitoring instruments. The YSI sensors are designed to measure a wide range of parameters, including temperature, salinity, and dissolved oxygen.""",
        meaning=SDN_B75["ORG00475"])
    nutrient_analyzer = PermissibleValue(
        text="nutrient_analyzer",
        description="""Instrument that makes in-situ measurements of one or more of nitrate, nitrite, ammonium, urea, phosphate or silicate dissolved in the water column.""",
        meaning=SDN_L05["181"])
    fluorometers = PermissibleValue(
        text="fluorometers",
        description="""Instrument that measures the amount of stimulated electromagnetic radiation produced by pulses of electromagnetic radiation emitted into the water column.""",
        meaning=SDN_L05["113"])
    high_performance_liquid_chromatography = PermissibleValue(
        text="high_performance_liquid_chromatography",
        description="""Instruments that separate and analyse mixtures of substances by high pressure pumping the sample through a column packed with microspheres coated with the stationary phase.""",
        meaning=SDN_L05["LAB11"])
    acoustic_doppler_current_profiler = PermissibleValue(
        text="acoustic_doppler_current_profiler",
        description="""Acoustic Doppler Current Profiler (ADCP), is a type of instrument used to measure water currents in oceans, rivers, and other bodies of water.""",
        meaning=SDN_L05["115"])
    mass_spectrometers = PermissibleValue(
        text="mass_spectrometers",
        description="""Instruments used to measure the mass-to-charge ratio of ions most generally used to find the composition of a sample by generating a mass spectrum representing the masses of sample components.""",
        meaning=SDN_L05["LAB16"])
    isotope_ratio_mass_spectrometers = PermissibleValue(
        text="isotope_ratio_mass_spectrometers",
        description="""Instruments that measure isotopic ratios using an electron ionisation source. Atoms in purified samples are ionised using a beam of electrons under vacuum. Subsequently, ions are focused into a beam by an electromagnet and then separated into individual beams based on their mass/charge ratio""",
        meaning=SDN_L05["LAB48"])
    barometric_pressure_sensor = PermissibleValue(
        text="barometric_pressure_sensor",
        description="""Instrument that makes routine meteorological measurements on the atmosphere, typically air pressure, temperature and humidity""",
        meaning=SDN_L05["102"])
    microscopes = PermissibleValue(
        text="microscopes",
        description="""Instruments that generate enlarged images of samples using the phenomena of reflection and absorption of visible light. Includes conventional and inverted instruments""",
        meaning=SDN_L05["LAB05"])
    scanning_electron_microscopes = PermissibleValue(
        text="scanning_electron_microscopes",
        description="""A scanning electron microscope (SEM) is a type of microscope that uses a focused beam of electrons to create high-resolution images of the surface of a specimen.""",
        meaning=SDN_L05["LAB07"])
    flow_cytometers = PermissibleValue(
        text="flow_cytometers",
        description="""Instruments that suspend cells in a stream of fluid past detection sensors whilst illuminating them with laser light. Used for cell counting, sorting, biomarker detection and protein engineering.""",
        meaning=SDN_L05["LAB37"])
    edna_sampler = PermissibleValue(
        text="edna_sampler",
        description="""Environmental DNA (eDNA) samplers: used to collect and analyze genetic material shed by marine organisms, which can provide information about their distribution, abundance, and diversity.""")
    gas_analyzer = PermissibleValue(
        text="gas_analyzer",
        description="TBD")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="AnalyzingInstrumentType",
    )

class CalibrationLocation(EnumDefinitionImpl):
    """
    Where the calibration was performed.
    """
    factory = PermissibleValue(
        text="factory",
        description="Factory calibration performed by manufacturer.")
    lab = PermissibleValue(
        text="lab",
        description="Laboratory calibration.")
    field = PermissibleValue(
        text="field",
        description="Field calibration performed during deployment.")

    _defn = EnumDefinition(
        name="CalibrationLocation",
        description="Where the calibration was performed.",
    )

# Slots
class slots:
    pass

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=OAE.description, domain=None, range=Optional[str])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=OAE.name, domain=None, range=Optional[str])

slots.identifier = Slot(uri=SCHEMA.identifier, name="identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=OAE.identifier, domain=None, range=Optional[str])

slots.experiment_id = Slot(uri=OAE.experiment_id, name="experiment_id", curie=OAE.curie('experiment_id'),
                   model_uri=OAE.experiment_id, domain=None, range=Optional[str])

slots.project_id = Slot(uri=OAE.project_id, name="project_id", curie=OAE.curie('project_id'),
                   model_uri=OAE.project_id, domain=None, range=Optional[str])

slots.temporal_coverage = Slot(uri=SCHEMA.temporalCoverage, name="temporal_coverage", curie=SCHEMA.curie('temporalCoverage'),
                   model_uri=OAE.temporal_coverage, domain=None, range=str,
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}/(\d{4}-\d{2}-\d{2}|\.\.)$'))

slots.spatial_coverage = Slot(uri=SCHEMA.spatialCoverage, name="spatial_coverage", curie=SCHEMA.curie('spatialCoverage'),
                   model_uri=OAE.spatial_coverage, domain=None, range=Union[dict, SpatialCoverage])

slots.vertical_coverage = Slot(uri=OAE.vertical_coverage, name="vertical_coverage", curie=OAE.curie('vertical_coverage'),
                   model_uri=OAE.vertical_coverage, domain=None, range=Optional[Union[dict, VerticalExtent]])

slots.permits = Slot(uri=OAE.permits, name="permits", curie=OAE.curie('permits'),
                   model_uri=OAE.permits, domain=None, range=Optional[Union[Union[dict, Permit], List[Union[dict, Permit]]]])

slots.geo = Slot(uri=OAE.geo, name="geo", curie=OAE.curie('geo'),
                   model_uri=OAE.geo, domain=None, range=Optional[Union[dict, Any]])

slots.is_provided_as_a_file = Slot(uri=OAE.is_provided_as_a_file, name="is_provided_as_a_file", curie=OAE.curie('is_provided_as_a_file'),
                   model_uri=OAE.is_provided_as_a_file, domain=None, range=Union[bool, Bool])

slots.is_derived_value = Slot(uri=OAE.is_derived_value, name="is_derived_value", curie=OAE.curie('is_derived_value'),
                   model_uri=OAE.is_derived_value, domain=None, range=Union[bool, Bool])

slots.units = Slot(uri=OAE.units, name="units", curie=OAE.curie('units'),
                   model_uri=OAE.units, domain=None, range=Optional[str])

slots.analyzing_instrument = Slot(uri=OAE.analyzing_instrument, name="analyzing_instrument", curie=OAE.curie('analyzing_instrument'),
                   model_uri=OAE.analyzing_instrument, domain=None, range=Union[dict, AnalyzingInstrument])

slots.sample_preservation = Slot(uri=OAE.sample_preservation, name="sample_preservation", curie=OAE.curie('sample_preservation'),
                   model_uri=OAE.sample_preservation, domain=None, range=Union[dict, SamplePreservation])

slots.blank_correction = Slot(uri=OAE.blank_correction, name="blank_correction", curie=OAE.curie('blank_correction'),
                   model_uri=OAE.blank_correction, domain=None, range=str)

slots.concentration_basis = Slot(uri=OAE.concentration_basis, name="concentration_basis", curie=OAE.curie('concentration_basis'),
                   model_uri=OAE.concentration_basis, domain=None, range=Union[str, "ConcentrationBasis"])

slots.qc_steps_taken = Slot(uri=OAE.qc_steps_taken, name="qc_steps_taken", curie=OAE.curie('qc_steps_taken'),
                   model_uri=OAE.qc_steps_taken, domain=None, range=Optional[str])

slots.uncertainty = Slot(uri=OAE.uncertainty, name="uncertainty", curie=OAE.curie('uncertainty'),
                   model_uri=OAE.uncertainty, domain=None, range=Optional[str])

slots.uncertainty_definition = Slot(uri=OAE.uncertainty_definition, name="uncertainty_definition", curie=OAE.curie('uncertainty_definition'),
                   model_uri=OAE.uncertainty_definition, domain=None, range=Optional[str])

slots.missing_value_indicators = Slot(uri=OAE.missing_value_indicators, name="missing_value_indicators", curie=OAE.curie('missing_value_indicators'),
                   model_uri=OAE.missing_value_indicators, domain=None, range=Optional[str])

slots.appropriate_use_quality = Slot(uri=OAE.appropriate_use_quality, name="appropriate_use_quality", curie=OAE.curie('appropriate_use_quality'),
                   model_uri=OAE.appropriate_use_quality, domain=None, range=Optional[Union[str, "AppropriateUseQuality"]])

slots.manufacturer = Slot(uri=OAE.manufacturer, name="manufacturer", curie=OAE.curie('manufacturer'),
                   model_uri=OAE.manufacturer, domain=None, range=Optional[str])

slots.model = Slot(uri=OAE.model, name="model", curie=OAE.curie('model'),
                   model_uri=OAE.model, domain=None, range=Optional[str])

slots.calibration_location = Slot(uri=OAE.calibration_location, name="calibration_location", curie=OAE.curie('calibration_location'),
                   model_uri=OAE.calibration_location, domain=None, range=Optional[Union[str, "CalibrationLocation"]])

slots.calibration_temperature = Slot(uri=OAE.calibration_temperature, name="calibration_temperature", curie=OAE.curie('calibration_temperature'),
                   model_uri=OAE.calibration_temperature, domain=None, range=Optional[str])

slots.container__project = Slot(uri=OAE.project, name="container__project", curie=OAE.curie('project'),
                   model_uri=OAE.container__project, domain=None, range=Optional[Union[dict, Project]])

slots.container__experiments = Slot(uri=OAE.experiments, name="container__experiments", curie=OAE.curie('experiments'),
                   model_uri=OAE.container__experiments, domain=None, range=Optional[Union[Union[dict, Experiment], List[Union[dict, Experiment]]]])

slots.container__datasets = Slot(uri=OAE.datasets, name="container__datasets", curie=OAE.curie('datasets'),
                   model_uri=OAE.container__datasets, domain=None, range=Optional[Union[Union[dict, Dataset], List[Union[dict, Dataset]]]])

slots.container__version = Slot(uri=OAE.version, name="container__version", curie=OAE.curie('version'),
                   model_uri=OAE.container__version, domain=None, range=Optional[str])

slots.container__protocol_git_hash = Slot(uri=OAE.protocol_git_hash, name="container__protocol_git_hash", curie=OAE.curie('protocol_git_hash'),
                   model_uri=OAE.container__protocol_git_hash, domain=None, range=Optional[str])

slots.container__metadata_builder_git_hash = Slot(uri=OAE.metadata_builder_git_hash, name="container__metadata_builder_git_hash", curie=OAE.curie('metadata_builder_git_hash'),
                   model_uri=OAE.container__metadata_builder_git_hash, domain=None, range=Optional[str])

slots.dosingLocation__dosing_location_file = Slot(uri=OAE.dosing_location_file, name="dosingLocation__dosing_location_file", curie=OAE.curie('dosing_location_file'),
                   model_uri=OAE.dosingLocation__dosing_location_file, domain=None, range=Optional[str])

slots.geoShape__box = Slot(uri=SCHEMA.box, name="geoShape__box", curie=SCHEMA.curie('box'),
                   model_uri=OAE.geoShape__box, domain=None, range=Optional[str])

slots.geoShape__line = Slot(uri=SCHEMA.line, name="geoShape__line", curie=SCHEMA.curie('line'),
                   model_uri=OAE.geoShape__line, domain=None, range=Optional[str])

slots.geoCoordinates__latitude = Slot(uri=SCHEMA.latitude, name="geoCoordinates__latitude", curie=SCHEMA.curie('latitude'),
                   model_uri=OAE.geoCoordinates__latitude, domain=None, range=float)

slots.geoCoordinates__longitude = Slot(uri=SCHEMA.longitude, name="geoCoordinates__longitude", curie=SCHEMA.curie('longitude'),
                   model_uri=OAE.geoCoordinates__longitude, domain=None, range=float)

slots.verticalExtent__min_depth_in_m = Slot(uri=OAE.min_depth_in_m, name="verticalExtent__min_depth_in_m", curie=OAE.curie('min_depth_in_m'),
                   model_uri=OAE.verticalExtent__min_depth_in_m, domain=None, range=Optional[float])

slots.verticalExtent__max_depth_in_m = Slot(uri=OAE.max_depth_in_m, name="verticalExtent__max_depth_in_m", curie=OAE.curie('max_depth_in_m'),
                   model_uri=OAE.verticalExtent__max_depth_in_m, domain=None, range=Optional[float])

slots.verticalExtent__min_height_in_m = Slot(uri=OAE.min_height_in_m, name="verticalExtent__min_height_in_m", curie=OAE.curie('min_height_in_m'),
                   model_uri=OAE.verticalExtent__min_height_in_m, domain=None, range=Optional[float])

slots.verticalExtent__max_height_in_m = Slot(uri=OAE.max_height_in_m, name="verticalExtent__max_height_in_m", curie=OAE.curie('max_height_in_m'),
                   model_uri=OAE.verticalExtent__max_height_in_m, domain=None, range=Optional[float])

slots.organization__country = Slot(uri=OAE.country, name="organization__country", curie=OAE.curie('country'),
                   model_uri=OAE.organization__country, domain=None, range=Optional[str])

slots.project__experiments = Slot(uri=OAE.experiments, name="project__experiments", curie=OAE.curie('experiments'),
                   model_uri=OAE.project__experiments, domain=None, range=Optional[Union[Union[dict, Experiment], List[Union[dict, Experiment]]]])

slots.project__sea_names = Slot(uri=OAE.sea_names, name="project__sea_names", curie=OAE.curie('sea_names'),
                   model_uri=OAE.project__sea_names, domain=None, range=Optional[Union[Union[str, "SeaNames"], List[Union[str, "SeaNames"]]]])

slots.project__physical_site_description = Slot(uri=OAE.physical_site_description, name="project__physical_site_description", curie=OAE.curie('physical_site_description'),
                   model_uri=OAE.project__physical_site_description, domain=None, range=Optional[str])

slots.project__social_context_site_description = Slot(uri=OAE.social_context_site_description, name="project__social_context_site_description", curie=OAE.curie('social_context_site_description'),
                   model_uri=OAE.project__social_context_site_description, domain=None, range=Optional[str])

slots.project__social_research_conducted_to_date = Slot(uri=OAE.social_research_conducted_to_date, name="project__social_research_conducted_to_date", curie=OAE.curie('social_research_conducted_to_date'),
                   model_uri=OAE.project__social_research_conducted_to_date, domain=None, range=Optional[str])

slots.project__mcdr_pathway = Slot(uri=OAE.mcdr_pathway, name="project__mcdr_pathway", curie=OAE.curie('mcdr_pathway'),
                   model_uri=OAE.project__mcdr_pathway, domain=None, range=Union[str, "MCDRPathway"])

slots.project__previous_or_ongoing_colocated_research = Slot(uri=OAE.previous_or_ongoing_colocated_research, name="project__previous_or_ongoing_colocated_research", curie=OAE.curie('previous_or_ongoing_colocated_research'),
                   model_uri=OAE.project__previous_or_ongoing_colocated_research, domain=None, range=Optional[Union[Union[dict, ExternalProject], List[Union[dict, ExternalProject]]]])

slots.project__colocated_operations = Slot(uri=OAE.colocated_operations, name="project__colocated_operations", curie=OAE.curie('colocated_operations'),
                   model_uri=OAE.project__colocated_operations, domain=None, range=Optional[str])

slots.project__public_comments = Slot(uri=OAE.public_comments, name="project__public_comments", curie=OAE.curie('public_comments'),
                   model_uri=OAE.project__public_comments, domain=None, range=Optional[str])

slots.project__research_project = Slot(uri=OAE.research_project, name="project__research_project", curie=OAE.curie('research_project'),
                   model_uri=OAE.project__research_project, domain=None, range=Optional[str])

slots.project__funding = Slot(uri=SCHEMA.funding, name="project__funding", curie=SCHEMA.curie('funding'),
                   model_uri=OAE.project__funding, domain=None, range=Optional[Union[Union[dict, MonetaryGrant], List[Union[dict, MonetaryGrant]]]])

slots.project__additional_details = Slot(uri=OAE.additional_details, name="project__additional_details", curie=OAE.curie('additional_details'),
                   model_uri=OAE.project__additional_details, domain=None, range=Optional[str])

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

slots.permit__permit_id = Slot(uri=OAE.permit_id, name="permit__permit_id", curie=OAE.curie('permit_id'),
                   model_uri=OAE.permit__permit_id, domain=None, range=str)

slots.permit__permitting_authority = Slot(uri=OAE.permitting_authority, name="permit__permitting_authority", curie=OAE.curie('permitting_authority'),
                   model_uri=OAE.permit__permitting_authority, domain=None, range=str)

slots.permit__agency_contact = Slot(uri=OAE.agency_contact, name="permit__agency_contact", curie=OAE.curie('agency_contact'),
                   model_uri=OAE.permit__agency_contact, domain=None, range=Optional[str])

slots.permit__changes_to_evolution_of_permit_criteria = Slot(uri=OAE.changes_to_evolution_of_permit_criteria, name="permit__changes_to_evolution_of_permit_criteria", curie=OAE.curie('changes_to_evolution_of_permit_criteria'),
                   model_uri=OAE.permit__changes_to_evolution_of_permit_criteria, domain=None, range=Optional[str])

slots.permit__permit_type = Slot(uri=OAE.permit_type, name="permit__permit_type", curie=OAE.curie('permit_type'),
                   model_uri=OAE.permit__permit_type, domain=None, range=Optional[str])

slots.permit__time_period = Slot(uri=OAE.time_period, name="permit__time_period", curie=OAE.curie('time_period'),
                   model_uri=OAE.permit__time_period, domain=None, range=Optional[str])

slots.permit__approval_document = Slot(uri=OAE.approval_document, name="permit__approval_document", curie=OAE.curie('approval_document'),
                   model_uri=OAE.permit__approval_document, domain=None, range=str)

slots.experiment__experiment_type = Slot(uri=OAE.experiment_type, name="experiment__experiment_type", curie=OAE.curie('experiment_type'),
                   model_uri=OAE.experiment__experiment_type, domain=None, range=Union[str, "ExperimentType"])

slots.experiment__principal_investigators = Slot(uri=OAE.principal_investigators, name="experiment__principal_investigators", curie=OAE.curie('principal_investigators'),
                   model_uri=OAE.experiment__principal_investigators, domain=None, range=Union[Union[dict, Person], List[Union[dict, Person]]])

slots.experiment__start_datetime = Slot(uri=OAE.start_datetime, name="experiment__start_datetime", curie=OAE.curie('start_datetime'),
                   model_uri=OAE.experiment__start_datetime, domain=None, range=Union[str, XSDDateTime])

slots.experiment__end_datetime = Slot(uri=OAE.end_datetime, name="experiment__end_datetime", curie=OAE.curie('end_datetime'),
                   model_uri=OAE.experiment__end_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.inSituExperiment__data_conflicts_and_unreported_data = Slot(uri=OAE.data_conflicts_and_unreported_data, name="inSituExperiment__data_conflicts_and_unreported_data", curie=OAE.curie('data_conflicts_and_unreported_data'),
                   model_uri=OAE.inSituExperiment__data_conflicts_and_unreported_data, domain=None, range=Optional[str])

slots.inSituExperiment__meteorological_and_tidal_data = Slot(uri=OAE.meteorological_and_tidal_data, name="inSituExperiment__meteorological_and_tidal_data", curie=OAE.curie('meteorological_and_tidal_data'),
                   model_uri=OAE.inSituExperiment__meteorological_and_tidal_data, domain=None, range=Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]])

slots.inSituExperiment__additional_details = Slot(uri=OAE.additional_details, name="inSituExperiment__additional_details", curie=OAE.curie('additional_details'),
                   model_uri=OAE.inSituExperiment__additional_details, domain=None, range=Optional[str])

slots.interventionDetails__alkalinity_feedstock_processing = Slot(uri=OAE.alkalinity_feedstock_processing, name="interventionDetails__alkalinity_feedstock_processing", curie=OAE.curie('alkalinity_feedstock_processing'),
                   model_uri=OAE.interventionDetails__alkalinity_feedstock_processing, domain=None, range=Union[str, "AlkalinityFeedstockProcessing"])

slots.interventionDetails__alkalinity_feedstock_processing_custom = Slot(uri=OAE.alkalinity_feedstock_processing_custom, name="interventionDetails__alkalinity_feedstock_processing_custom", curie=OAE.curie('alkalinity_feedstock_processing_custom'),
                   model_uri=OAE.interventionDetails__alkalinity_feedstock_processing_custom, domain=None, range=Optional[str])

slots.interventionDetails__alkalinity_feedstock_form = Slot(uri=OAE.alkalinity_feedstock_form, name="interventionDetails__alkalinity_feedstock_form", curie=OAE.curie('alkalinity_feedstock_form'),
                   model_uri=OAE.interventionDetails__alkalinity_feedstock_form, domain=None, range=Union[str, "AlkalinityFeedstockForm"])

slots.interventionDetails__alkalinity_feedstock = Slot(uri=OAE.alkalinity_feedstock, name="interventionDetails__alkalinity_feedstock", curie=OAE.curie('alkalinity_feedstock'),
                   model_uri=OAE.interventionDetails__alkalinity_feedstock, domain=None, range=Union[str, "FeedstockType"])

slots.interventionDetails__alkalinity_feedstock_custom = Slot(uri=OAE.alkalinity_feedstock_custom, name="interventionDetails__alkalinity_feedstock_custom", curie=OAE.curie('alkalinity_feedstock_custom'),
                   model_uri=OAE.interventionDetails__alkalinity_feedstock_custom, domain=None, range=Optional[str])

slots.interventionDetails__alkalinity_feedstock_co2_removal_potential = Slot(uri=OAE.alkalinity_feedstock_co2_removal_potential, name="interventionDetails__alkalinity_feedstock_co2_removal_potential", curie=OAE.curie('alkalinity_feedstock_co2_removal_potential'),
                   model_uri=OAE.interventionDetails__alkalinity_feedstock_co2_removal_potential, domain=None, range=float)

slots.interventionDetails__alkalinity_feedstock_description = Slot(uri=OAE.alkalinity_feedstock_description, name="interventionDetails__alkalinity_feedstock_description", curie=OAE.curie('alkalinity_feedstock_description'),
                   model_uri=OAE.interventionDetails__alkalinity_feedstock_description, domain=None, range=str)

slots.interventionDetails__equilibration = Slot(uri=OAE.equilibration, name="interventionDetails__equilibration", curie=OAE.curie('equilibration'),
                   model_uri=OAE.interventionDetails__equilibration, domain=None, range=Union[str, "EquilibrationStatus"])

slots.interventionDetails__alkalinity_dosing_effluent_density = Slot(uri=OAE.alkalinity_dosing_effluent_density, name="interventionDetails__alkalinity_dosing_effluent_density", curie=OAE.curie('alkalinity_dosing_effluent_density'),
                   model_uri=OAE.interventionDetails__alkalinity_dosing_effluent_density, domain=None, range=Union[dict, DosingConcentration])

slots.tracerDetails__tracer_form = Slot(uri=OAE.tracer_form, name="tracerDetails__tracer_form", curie=OAE.curie('tracer_form'),
                   model_uri=OAE.tracerDetails__tracer_form, domain=None, range=Union[str, "TracerForm"])

slots.tracerDetails__tracer_details = Slot(uri=OAE.tracer_details, name="tracerDetails__tracer_details", curie=OAE.curie('tracer_details'),
                   model_uri=OAE.tracerDetails__tracer_details, domain=None, range=str)

slots.tracerDetails__tracer_concentration = Slot(uri=OAE.tracer_concentration, name="tracerDetails__tracer_concentration", curie=OAE.curie('tracer_concentration'),
                   model_uri=OAE.tracerDetails__tracer_concentration, domain=None, range=Union[dict, DosingConcentration])

slots.dosingConcentration__amount = Slot(uri=OAE.amount, name="dosingConcentration__amount", curie=OAE.curie('amount'),
                   model_uri=OAE.dosingConcentration__amount, domain=None, range=Optional[float])

slots.dosingConcentration__unit = Slot(uri=OAE.unit, name="dosingConcentration__unit", curie=OAE.curie('unit'),
                   model_uri=OAE.dosingConcentration__unit, domain=None, range=Optional[Union[str, "MassConcentrationUnit"]])

slots.dosingDetails__dosing_delivery_type = Slot(uri=OAE.dosing_delivery_type, name="dosingDetails__dosing_delivery_type", curie=OAE.curie('dosing_delivery_type'),
                   model_uri=OAE.dosingDetails__dosing_delivery_type, domain=None, range=Union[str, "DosingDeliveryType"])

slots.dosingDetails__dosing_location = Slot(uri=OAE.dosing_location, name="dosingDetails__dosing_location", curie=OAE.curie('dosing_location'),
                   model_uri=OAE.dosingDetails__dosing_location, domain=None, range=Union[dict, DosingLocation])

slots.dosingDetails__dosing_dispersal_hydrologic_location = Slot(uri=OAE.dosing_dispersal_hydrologic_location, name="dosingDetails__dosing_dispersal_hydrologic_location", curie=OAE.curie('dosing_dispersal_hydrologic_location'),
                   model_uri=OAE.dosingDetails__dosing_dispersal_hydrologic_location, domain=None, range=Union[str, "HydrologicLocation"])

slots.dosingDetails__dosing_depth = Slot(uri=OAE.dosing_depth, name="dosingDetails__dosing_depth", curie=OAE.curie('dosing_depth'),
                   model_uri=OAE.dosingDetails__dosing_depth, domain=None, range=str)

slots.dosingDetails__dosing_regimen = Slot(uri=OAE.dosing_regimen, name="dosingDetails__dosing_regimen", curie=OAE.curie('dosing_regimen'),
                   model_uri=OAE.dosingDetails__dosing_regimen, domain=None, range=str)

slots.dosingDetails__dosing_description = Slot(uri=OAE.dosing_description, name="dosingDetails__dosing_description", curie=OAE.curie('dosing_description'),
                   model_uri=OAE.dosingDetails__dosing_description, domain=None, range=str)

slots.person__name = Slot(uri=OAE.name, name="person__name", curie=OAE.curie('name'),
                   model_uri=OAE.person__name, domain=None, range=str)

slots.person__affiliation = Slot(uri=OAE.affiliation, name="person__affiliation", curie=OAE.curie('affiliation'),
                   model_uri=OAE.person__affiliation, domain=None, range=Optional[Union[dict, Organization]])

slots.person__phone = Slot(uri=OAE.phone, name="person__phone", curie=OAE.curie('phone'),
                   model_uri=OAE.person__phone, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\+?[0-9\s\-\(\)]+$'))

slots.person__email = Slot(uri=OAE.email, name="person__email", curie=OAE.curie('email'),
                   model_uri=OAE.person__email, domain=None, range=str,
                   pattern=re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'))

slots.person__identifier_type = Slot(uri=OAE.identifier_type, name="person__identifier_type", curie=OAE.curie('identifier_type'),
                   model_uri=OAE.person__identifier_type, domain=None, range=Optional[Union[str, "ResearcherIDType"]])

slots.person__identifier = Slot(uri=OAE.identifier, name="person__identifier", curie=OAE.curie('identifier'),
                   model_uri=OAE.person__identifier, domain=None, range=Optional[str])

slots.person__role = Slot(uri=OAE.role, name="person__role", curie=OAE.curie('role'),
                   model_uri=OAE.person__role, domain=None, range=Optional[str])

slots.baseVariable__standard_identifier = Slot(uri=OAE.standard_identifier, name="baseVariable__standard_identifier", curie=OAE.curie('standard_identifier'),
                   model_uri=OAE.baseVariable__standard_identifier, domain=None, range=Optional[Union[dict, VocabularyItemReference]])

slots.baseVariable__dataset_variable_name = Slot(uri=OAE.dataset_variable_name, name="baseVariable__dataset_variable_name", curie=OAE.curie('dataset_variable_name'),
                   model_uri=OAE.baseVariable__dataset_variable_name, domain=None, range=str)

slots.baseVariable__long_name = Slot(uri=OAE.long_name, name="baseVariable__long_name", curie=OAE.curie('long_name'),
                   model_uri=OAE.baseVariable__long_name, domain=None, range=str)

slots.variable__dataset_variable_name_qc_flag = Slot(uri=OAE.dataset_variable_name_qc_flag, name="variable__dataset_variable_name_qc_flag", curie=OAE.curie('dataset_variable_name_qc_flag'),
                   model_uri=OAE.variable__dataset_variable_name_qc_flag, domain=None, range=Optional[str])

slots.variable__dataset_variable_name_raw = Slot(uri=OAE.dataset_variable_name_raw, name="variable__dataset_variable_name_raw", curie=OAE.curie('dataset_variable_name_raw'),
                   model_uri=OAE.variable__dataset_variable_name_raw, domain=None, range=Optional[str])

slots.variable__method_reference = Slot(uri=OAE.method_reference, name="variable__method_reference", curie=OAE.curie('method_reference'),
                   model_uri=OAE.variable__method_reference, domain=None, range=Optional[str])

slots.variable__measurement_researcher = Slot(uri=OAE.measurement_researcher, name="variable__measurement_researcher", curie=OAE.curie('measurement_researcher'),
                   model_uri=OAE.variable__measurement_researcher, domain=None, range=Optional[Union[dict, Person]])

slots.variable__other_detailed_information = Slot(uri=OAE.other_detailed_information, name="variable__other_detailed_information", curie=OAE.curie('other_detailed_information'),
                   model_uri=OAE.variable__other_detailed_information, domain=None, range=Optional[str])

slots.observedPropertyVariable__sampling_method = Slot(uri=OAE.sampling_method, name="observedPropertyVariable__sampling_method", curie=OAE.curie('sampling_method'),
                   model_uri=OAE.observedPropertyVariable__sampling_method, domain=None, range=str)

slots.observedPropertyVariable__field_replicate_information = Slot(uri=OAE.field_replicate_information, name="observedPropertyVariable__field_replicate_information", curie=OAE.curie('field_replicate_information'),
                   model_uri=OAE.observedPropertyVariable__field_replicate_information, domain=None, range=Optional[str])

slots.observedPropertyVariable__analyzing_method = Slot(uri=OAE.analyzing_method, name="observedPropertyVariable__analyzing_method", curie=OAE.curie('analyzing_method'),
                   model_uri=OAE.observedPropertyVariable__analyzing_method, domain=None, range=str)

slots.observedPropertyVariable__observation_type = Slot(uri=OAE.observation_type, name="observedPropertyVariable__observation_type", curie=OAE.curie('observation_type'),
                   model_uri=OAE.observedPropertyVariable__observation_type, domain=None, range=Union[str, "ObservationType"])

slots.observedPropertyVariable__sampling = Slot(uri=OAE.sampling, name="observedPropertyVariable__sampling", curie=OAE.curie('sampling'),
                   model_uri=OAE.observedPropertyVariable__sampling, domain=None, range=Union[str, "SamplingType"])

slots.observedPropertyVariable__genesis = Slot(uri=OAE.genesis, name="observedPropertyVariable__genesis", curie=OAE.curie('genesis'),
                   model_uri=OAE.observedPropertyVariable__genesis, domain=None, range=Union[str, "GenesisType"])

slots.observedPropertyVariable__sampling_instrument_type = Slot(uri=OAE.sampling_instrument_type, name="observedPropertyVariable__sampling_instrument_type", curie=OAE.curie('sampling_instrument_type'),
                   model_uri=OAE.observedPropertyVariable__sampling_instrument_type, domain=None, range=Union[str, "SamplingInstrumentType"])

slots.observedPropertyVariable__sampling_instrument_type_custom = Slot(uri=OAE.sampling_instrument_type_custom, name="observedPropertyVariable__sampling_instrument_type_custom", curie=OAE.curie('sampling_instrument_type_custom'),
                   model_uri=OAE.observedPropertyVariable__sampling_instrument_type_custom, domain=None, range=Optional[str])

slots.continuousMeasuredVariable__raw_data_calculation_method = Slot(uri=OAE.raw_data_calculation_method, name="continuousMeasuredVariable__raw_data_calculation_method", curie=OAE.curie('raw_data_calculation_method'),
                   model_uri=OAE.continuousMeasuredVariable__raw_data_calculation_method, domain=None, range=str)

slots.continuousMeasuredVariable__calculation_software_version = Slot(uri=OAE.calculation_software_version, name="continuousMeasuredVariable__calculation_software_version", curie=OAE.curie('calculation_software_version'),
                   model_uri=OAE.continuousMeasuredVariable__calculation_software_version, domain=None, range=Optional[str])

slots.calculatedVariable__genesis = Slot(uri=OAE.genesis, name="calculatedVariable__genesis", curie=OAE.curie('genesis'),
                   model_uri=OAE.calculatedVariable__genesis, domain=None, range=Union[str, "GenesisType"])

slots.calculatedVariable__calculation_method_and_parameters = Slot(uri=OAE.calculation_method_and_parameters, name="calculatedVariable__calculation_method_and_parameters", curie=OAE.curie('calculation_method_and_parameters'),
                   model_uri=OAE.calculatedVariable__calculation_method_and_parameters, domain=None, range=str)

slots.discretePHVariable__measurement_temperature = Slot(uri=OAE.measurement_temperature, name="discretePHVariable__measurement_temperature", curie=OAE.curie('measurement_temperature'),
                   model_uri=OAE.discretePHVariable__measurement_temperature, domain=None, range=str)

slots.discretePHVariable__temperature_correction_method = Slot(uri=OAE.temperature_correction_method, name="discretePHVariable__temperature_correction_method", curie=OAE.curie('temperature_correction_method'),
                   model_uri=OAE.discretePHVariable__temperature_correction_method, domain=None, range=Optional[str])

slots.discretePHVariable__ph_reported_temperature = Slot(uri=OAE.ph_reported_temperature, name="discretePHVariable__ph_reported_temperature", curie=OAE.curie('ph_reported_temperature'),
                   model_uri=OAE.discretePHVariable__ph_reported_temperature, domain=None, range=str)

slots.discreteTAVariable__titration_type = Slot(uri=OAE.titration_type, name="discreteTAVariable__titration_type", curie=OAE.curie('titration_type'),
                   model_uri=OAE.discreteTAVariable__titration_type, domain=None, range=str)

slots.discreteTAVariable__titration_cell_type = Slot(uri=OAE.titration_cell_type, name="discreteTAVariable__titration_cell_type", curie=OAE.curie('titration_cell_type'),
                   model_uri=OAE.discreteTAVariable__titration_cell_type, domain=None, range=Optional[Union[str, "TitrationCellType"]])

slots.discreteTAVariable__curve_fitting_method = Slot(uri=OAE.curve_fitting_method, name="discreteTAVariable__curve_fitting_method", curie=OAE.curie('curve_fitting_method'),
                   model_uri=OAE.discreteTAVariable__curve_fitting_method, domain=None, range=Optional[str])

slots.discreteCO2Variable__storage_method = Slot(uri=OAE.storage_method, name="discreteCO2Variable__storage_method", curie=OAE.curie('storage_method'),
                   model_uri=OAE.discreteCO2Variable__storage_method, domain=None, range=str)

slots.discreteCO2Variable__seawater_volume = Slot(uri=OAE.seawater_volume, name="discreteCO2Variable__seawater_volume", curie=OAE.curie('seawater_volume'),
                   model_uri=OAE.discreteCO2Variable__seawater_volume, domain=None, range=Optional[int])

slots.discreteCO2Variable__headspace_volume = Slot(uri=OAE.headspace_volume, name="discreteCO2Variable__headspace_volume", curie=OAE.curie('headspace_volume'),
                   model_uri=OAE.discreteCO2Variable__headspace_volume, domain=None, range=Optional[int])

slots.discreteCO2Variable__measurement_temperature = Slot(uri=OAE.measurement_temperature, name="discreteCO2Variable__measurement_temperature", curie=OAE.curie('measurement_temperature'),
                   model_uri=OAE.discreteCO2Variable__measurement_temperature, domain=None, range=int)

slots.hPLCVariable__hplc_lab = Slot(uri=OAE.hplc_lab, name="hPLCVariable__hplc_lab", curie=OAE.curie('hplc_lab'),
                   model_uri=OAE.hPLCVariable__hplc_lab, domain=None, range=str)

slots.hPLCVariable__hplc_lab_technician = Slot(uri=OAE.hplc_lab_technician, name="hPLCVariable__hplc_lab_technician", curie=OAE.curie('hplc_lab_technician'),
                   model_uri=OAE.hPLCVariable__hplc_lab_technician, domain=None, range=Optional[str])

slots.samplePreservation__preservative = Slot(uri=OAE.preservative, name="samplePreservation__preservative", curie=OAE.curie('preservative'),
                   model_uri=OAE.samplePreservation__preservative, domain=None, range=str)

slots.samplePreservation__volume = Slot(uri=OAE.volume, name="samplePreservation__volume", curie=OAE.curie('volume'),
                   model_uri=OAE.samplePreservation__volume, domain=None, range=str)

slots.samplePreservation__correction_description = Slot(uri=OAE.correction_description, name="samplePreservation__correction_description", curie=OAE.curie('correction_description'),
                   model_uri=OAE.samplePreservation__correction_description, domain=None, range=Optional[str])

slots.vocabularyItemReference__term = Slot(uri=OAE.term, name="vocabularyItemReference__term", curie=OAE.curie('term'),
                   model_uri=OAE.vocabularyItemReference__term, domain=None, range=str)

slots.vocabularyItemReference__uri = Slot(uri=OAE.uri, name="vocabularyItemReference__uri", curie=OAE.curie('uri'),
                   model_uri=OAE.vocabularyItemReference__uri, domain=None, range=Union[str, URIorCURIE])

slots.measuredSedimentFields__sediment_type = Slot(uri=OAE.sediment_type, name="measuredSedimentFields__sediment_type", curie=OAE.curie('sediment_type'),
                   model_uri=OAE.measuredSedimentFields__sediment_type, domain=None, range=str)

slots.measuredSedimentFields__sediment_sampling_method = Slot(uri=OAE.sediment_sampling_method, name="measuredSedimentFields__sediment_sampling_method", curie=OAE.curie('sediment_sampling_method'),
                   model_uri=OAE.measuredSedimentFields__sediment_sampling_method, domain=None, range=str)

slots.measuredSedimentFields__sediment_sampling_depth = Slot(uri=OAE.sediment_sampling_depth, name="measuredSedimentFields__sediment_sampling_depth", curie=OAE.curie('sediment_sampling_depth'),
                   model_uri=OAE.measuredSedimentFields__sediment_sampling_depth, domain=None, range=str)

slots.measuredSedimentFields__sediment_sampling_water_depth = Slot(uri=OAE.sediment_sampling_water_depth, name="measuredSedimentFields__sediment_sampling_water_depth", curie=OAE.curie('sediment_sampling_water_depth'),
                   model_uri=OAE.measuredSedimentFields__sediment_sampling_water_depth, domain=None, range=str)

slots.measuredCO2Fields__co2_reported_temperature = Slot(uri=OAE.co2_reported_temperature, name="measuredCO2Fields__co2_reported_temperature", curie=OAE.curie('co2_reported_temperature'),
                   model_uri=OAE.measuredCO2Fields__co2_reported_temperature, domain=None, range=str)

slots.measuredCO2Fields__water_vapor_correction_method = Slot(uri=OAE.water_vapor_correction_method, name="measuredCO2Fields__water_vapor_correction_method", curie=OAE.curie('water_vapor_correction_method'),
                   model_uri=OAE.measuredCO2Fields__water_vapor_correction_method, domain=None, range=Optional[str])

slots.measuredCO2Fields__temperature_correction_method = Slot(uri=OAE.temperature_correction_method, name="measuredCO2Fields__temperature_correction_method", curie=OAE.curie('temperature_correction_method'),
                   model_uri=OAE.measuredCO2Fields__temperature_correction_method, domain=None, range=Optional[str])

slots.qCFields__qc_researcher = Slot(uri=OAE.qc_researcher, name="qCFields__qc_researcher", curie=OAE.curie('qc_researcher'),
                   model_uri=OAE.qCFields__qc_researcher, domain=None, range=Optional[Union[dict, Person]])

slots.qCFields__qc_researcher_institution = Slot(uri=OAE.qc_researcher_institution, name="qCFields__qc_researcher_institution", curie=OAE.curie('qc_researcher_institution'),
                   model_uri=OAE.qCFields__qc_researcher_institution, domain=None, range=Optional[str])

slots.dataset__dataset_type = Slot(uri=OAE.dataset_type, name="dataset__dataset_type", curie=OAE.curie('dataset_type'),
                   model_uri=OAE.dataset__dataset_type, domain=None, range=Union[str, "DatasetType"])

slots.dataset__dataset_type_custom = Slot(uri=OAE.dataset_type_custom, name="dataset__dataset_type_custom", curie=OAE.curie('dataset_type_custom'),
                   model_uri=OAE.dataset__dataset_type_custom, domain=None, range=Optional[str])

slots.dataset__data_submitter = Slot(uri=OAE.data_submitter, name="dataset__data_submitter", curie=OAE.curie('data_submitter'),
                   model_uri=OAE.dataset__data_submitter, domain=None, range=Union[dict, Person])

slots.dataset__author_list_for_citation = Slot(uri=OAE.author_list_for_citation, name="dataset__author_list_for_citation", curie=OAE.curie('author_list_for_citation'),
                   model_uri=OAE.dataset__author_list_for_citation, domain=None, range=Optional[str])

slots.dataset__license = Slot(uri=SCHEMA.license, name="dataset__license", curie=SCHEMA.curie('license'),
                   model_uri=OAE.dataset__license, domain=None, range=Optional[Union[str, URI]])

slots.dataset__fair_use_data_request = Slot(uri=OAE.fair_use_data_request, name="dataset__fair_use_data_request", curie=OAE.curie('fair_use_data_request'),
                   model_uri=OAE.dataset__fair_use_data_request, domain=None, range=Optional[str])

slots.dataset__filenames = Slot(uri=OAE.filenames, name="dataset__filenames", curie=OAE.curie('filenames'),
                   model_uri=OAE.dataset__filenames, domain=None, range=Union[str, List[str]])

slots.fieldDataset__data_product_type = Slot(uri=OAE.data_product_type, name="fieldDataset__data_product_type", curie=OAE.curie('data_product_type'),
                   model_uri=OAE.fieldDataset__data_product_type, domain=None, range=Union[str, "DataProductType"])

slots.fieldDataset__qc_flag_scheme = Slot(uri=OAE.qc_flag_scheme, name="fieldDataset__qc_flag_scheme", curie=OAE.curie('qc_flag_scheme'),
                   model_uri=OAE.fieldDataset__qc_flag_scheme, domain=None, range=Optional[str])

slots.fieldDataset__platform_info = Slot(uri=OAE.platform_info, name="fieldDataset__platform_info", curie=OAE.curie('platform_info'),
                   model_uri=OAE.fieldDataset__platform_info, domain=None, range=Union[dict, Platform])

slots.fieldDataset__calibration_files = Slot(uri=OAE.calibration_files, name="fieldDataset__calibration_files", curie=OAE.curie('calibration_files'),
                   model_uri=OAE.fieldDataset__calibration_files, domain=None, range=Optional[Union[str, List[str]]])

slots.fieldDataset__variables = Slot(uri=SCHEMA.variableMeasured, name="fieldDataset__variables", curie=SCHEMA.curie('variableMeasured'),
                   model_uri=OAE.fieldDataset__variables, domain=None, range=Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]])

slots.modelSimulationDataset__simulation_type = Slot(uri=OAE.simulation_type, name="modelSimulationDataset__simulation_type", curie=OAE.curie('simulation_type'),
                   model_uri=OAE.modelSimulationDataset__simulation_type, domain=None, range=Union[str, "SimulationType"])

slots.modelSimulationDataset__spin_up_protocol = Slot(uri=OAE.spin_up_protocol, name="modelSimulationDataset__spin_up_protocol", curie=OAE.curie('spin_up_protocol'),
                   model_uri=OAE.modelSimulationDataset__spin_up_protocol, domain=None, range=Optional[str])

slots.modelSimulationDataset__start_datetime = Slot(uri=OAE.start_datetime, name="modelSimulationDataset__start_datetime", curie=OAE.curie('start_datetime'),
                   model_uri=OAE.modelSimulationDataset__start_datetime, domain=None, range=Union[str, XSDDateTime])

slots.modelSimulationDataset__end_datetime = Slot(uri=OAE.end_datetime, name="modelSimulationDataset__end_datetime", curie=OAE.curie('end_datetime'),
                   model_uri=OAE.modelSimulationDataset__end_datetime, domain=None, range=Union[str, XSDDateTime])

slots.modelSimulationDataset__output_frequency = Slot(uri=OAE.output_frequency, name="modelSimulationDataset__output_frequency", curie=OAE.curie('output_frequency'),
                   model_uri=OAE.modelSimulationDataset__output_frequency, domain=None, range=Optional[str])

slots.modelSimulationDataset__time_stepping_scheme = Slot(uri=OAE.time_stepping_scheme, name="modelSimulationDataset__time_stepping_scheme", curie=OAE.curie('time_stepping_scheme'),
                   model_uri=OAE.modelSimulationDataset__time_stepping_scheme, domain=None, range=Optional[str])

slots.modelSimulationDataset__alkalinity_perturbation_description = Slot(uri=OAE.alkalinity_perturbation_description, name="modelSimulationDataset__alkalinity_perturbation_description", curie=OAE.curie('alkalinity_perturbation_description'),
                   model_uri=OAE.modelSimulationDataset__alkalinity_perturbation_description, domain=None, range=Optional[str])

slots.modelSimulationDataset__hardware_configuration = Slot(uri=OAE.hardware_configuration, name="modelSimulationDataset__hardware_configuration", curie=OAE.curie('hardware_configuration'),
                   model_uri=OAE.modelSimulationDataset__hardware_configuration, domain=None, range=Optional[Union[dict, HardwareConfiguration]])

slots.modelSimulationDataset__model_output_variables = Slot(uri=OAE.model_output_variables, name="modelSimulationDataset__model_output_variables", curie=OAE.curie('model_output_variables'),
                   model_uri=OAE.modelSimulationDataset__model_output_variables, domain=None, range=Optional[Union[Union[str, "ModelSimulationVariable"], List[Union[str, "ModelSimulationVariable"]]]])

slots.hardwareConfiguration__machine = Slot(uri=OAE.machine, name="hardwareConfiguration__machine", curie=OAE.curie('machine'),
                   model_uri=OAE.hardwareConfiguration__machine, domain=None, range=Optional[str])

slots.hardwareConfiguration__operating_system = Slot(uri=OAE.operating_system, name="hardwareConfiguration__operating_system", curie=OAE.curie('operating_system'),
                   model_uri=OAE.hardwareConfiguration__operating_system, domain=None, range=Optional[str])

slots.hardwareConfiguration__cpu_gpu_details = Slot(uri=OAE.cpu_gpu_details, name="hardwareConfiguration__cpu_gpu_details", curie=OAE.curie('cpu_gpu_details'),
                   model_uri=OAE.hardwareConfiguration__cpu_gpu_details, domain=None, range=Optional[str])

slots.hardwareConfiguration__memory = Slot(uri=OAE.memory, name="hardwareConfiguration__memory", curie=OAE.curie('memory'),
                   model_uri=OAE.hardwareConfiguration__memory, domain=None, range=Optional[str])

slots.hardwareConfiguration__storage = Slot(uri=OAE.storage, name="hardwareConfiguration__storage", curie=OAE.curie('storage'),
                   model_uri=OAE.hardwareConfiguration__storage, domain=None, range=Optional[str])

slots.hardwareConfiguration__parallelization = Slot(uri=OAE.parallelization, name="hardwareConfiguration__parallelization", curie=OAE.curie('parallelization'),
                   model_uri=OAE.hardwareConfiguration__parallelization, domain=None, range=Optional[str])

slots.platform__platform_type = Slot(uri=OAE.platform_type, name="platform__platform_type", curie=OAE.curie('platform_type'),
                   model_uri=OAE.platform__platform_type, domain=None, range=Union[str, "PlatformType"])

slots.platform__platform_id = Slot(uri=OAE.platform_id, name="platform__platform_id", curie=OAE.curie('platform_id'),
                   model_uri=OAE.platform__platform_id, domain=None, range=Optional[str])

slots.platform__owner = Slot(uri=OAE.owner, name="platform__owner", curie=OAE.curie('owner'),
                   model_uri=OAE.platform__owner, domain=None, range=Optional[str])

slots.platform__country = Slot(uri=OAE.country, name="platform__country", curie=OAE.curie('country'),
                   model_uri=OAE.platform__country, domain=None, range=Optional[str])

slots.model__model_configuration = Slot(uri=OAE.model_configuration, name="model__model_configuration", curie=OAE.curie('model_configuration'),
                   model_uri=OAE.model__model_configuration, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.model__model_components = Slot(uri=OAE.model_components, name="model__model_components", curie=OAE.curie('model_components'),
                   model_uri=OAE.model__model_components, domain=None, range=Optional[Union[Union[dict, ModelComponent], List[Union[dict, ModelComponent]]]])

slots.model__grid_details = Slot(uri=OAE.grid_details, name="model__grid_details", curie=OAE.curie('grid_details'),
                   model_uri=OAE.model__grid_details, domain=None, range=Optional[Union[Union[dict, ModelGrid], List[Union[dict, ModelGrid]]]])

slots.model__input_details = Slot(uri=OAE.input_details, name="model__input_details", curie=OAE.curie('input_details'),
                   model_uri=OAE.model__input_details, domain=None, range=Optional[Union[dict, ModelInputDetails]])

slots.modelComponent__model_component_type = Slot(uri=OAE.model_component_type, name="modelComponent__model_component_type", curie=OAE.curie('model_component_type'),
                   model_uri=OAE.modelComponent__model_component_type, domain=None, range=Union[str, "ModelComponentType"])

slots.modelComponent__model_component_type_custom = Slot(uri=OAE.model_component_type_custom, name="modelComponent__model_component_type_custom", curie=OAE.curie('model_component_type_custom'),
                   model_uri=OAE.modelComponent__model_component_type_custom, domain=None, range=Optional[str])

slots.modelComponent__name = Slot(uri=OAE.name, name="modelComponent__name", curie=OAE.curie('name'),
                   model_uri=OAE.modelComponent__name, domain=None, range=str)

slots.modelComponent__version = Slot(uri=OAE.version, name="modelComponent__version", curie=OAE.curie('version'),
                   model_uri=OAE.modelComponent__version, domain=None, range=Optional[str])

slots.modelComponent__codebase = Slot(uri=OAE.codebase, name="modelComponent__codebase", curie=OAE.curie('codebase'),
                   model_uri=OAE.modelComponent__codebase, domain=None, range=Optional[Union[str, URI]])

slots.modelComponent__references = Slot(uri=OAE.references, name="modelComponent__references", curie=OAE.curie('references'),
                   model_uri=OAE.modelComponent__references, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.modelGrid__grid_name = Slot(uri=OAE.grid_name, name="modelGrid__grid_name", curie=OAE.curie('grid_name'),
                   model_uri=OAE.modelGrid__grid_name, domain=None, range=Optional[str])

slots.modelGrid__grid_geometry = Slot(uri=OAE.grid_geometry, name="modelGrid__grid_geometry", curie=OAE.curie('grid_geometry'),
                   model_uri=OAE.modelGrid__grid_geometry, domain=None, range=Optional[str])

slots.modelGrid__grid_type = Slot(uri=OAE.grid_type, name="modelGrid__grid_type", curie=OAE.curie('grid_type'),
                   model_uri=OAE.modelGrid__grid_type, domain=None, range=Union[str, "GridType"])

slots.modelGrid__region = Slot(uri=OAE.region, name="modelGrid__region", curie=OAE.curie('region'),
                   model_uri=OAE.modelGrid__region, domain=None, range=Optional[str])

slots.modelGrid__spatial_coverage = Slot(uri=OAE.spatial_coverage, name="modelGrid__spatial_coverage", curie=OAE.curie('spatial_coverage'),
                   model_uri=OAE.modelGrid__spatial_coverage, domain=None, range=Optional[Union[dict, SpatialCoverage]])

slots.modelGrid__arrangement = Slot(uri=OAE.arrangement, name="modelGrid__arrangement", curie=OAE.curie('arrangement'),
                   model_uri=OAE.modelGrid__arrangement, domain=None, range=Optional[str])

slots.modelGrid__vertical_coordinate_type = Slot(uri=OAE.vertical_coordinate_type, name="modelGrid__vertical_coordinate_type", curie=OAE.curie('vertical_coordinate_type'),
                   model_uri=OAE.modelGrid__vertical_coordinate_type, domain=None, range=Optional[str])

slots.modelGrid__n_x = Slot(uri=OAE.n_x, name="modelGrid__n_x", curie=OAE.curie('n_x'),
                   model_uri=OAE.modelGrid__n_x, domain=None, range=Optional[int])

slots.modelGrid__n_y = Slot(uri=OAE.n_y, name="modelGrid__n_y", curie=OAE.curie('n_y'),
                   model_uri=OAE.modelGrid__n_y, domain=None, range=Optional[int])

slots.modelGrid__n_z = Slot(uri=OAE.n_z, name="modelGrid__n_z", curie=OAE.curie('n_z'),
                   model_uri=OAE.modelGrid__n_z, domain=None, range=Optional[int])

slots.modelGrid__n_nodes = Slot(uri=OAE.n_nodes, name="modelGrid__n_nodes", curie=OAE.curie('n_nodes'),
                   model_uri=OAE.modelGrid__n_nodes, domain=None, range=Optional[int])

slots.modelGrid__horizontal_resolution_range = Slot(uri=OAE.horizontal_resolution_range, name="modelGrid__horizontal_resolution_range", curie=OAE.curie('horizontal_resolution_range'),
                   model_uri=OAE.modelGrid__horizontal_resolution_range, domain=None, range=Optional[str])

slots.modelGrid__vertical_resolution_range = Slot(uri=OAE.vertical_resolution_range, name="modelGrid__vertical_resolution_range", curie=OAE.curie('vertical_resolution_range'),
                   model_uri=OAE.modelGrid__vertical_resolution_range, domain=None, range=Optional[str])

slots.modelInputDetails__bathymetry = Slot(uri=OAE.bathymetry, name="modelInputDetails__bathymetry", curie=OAE.curie('bathymetry'),
                   model_uri=OAE.modelInputDetails__bathymetry, domain=None, range=Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]])

slots.modelInputDetails__initial_conditions = Slot(uri=OAE.initial_conditions, name="modelInputDetails__initial_conditions", curie=OAE.curie('initial_conditions'),
                   model_uri=OAE.modelInputDetails__initial_conditions, domain=None, range=Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]])

slots.modelInputDetails__boundary_conditions = Slot(uri=OAE.boundary_conditions, name="modelInputDetails__boundary_conditions", curie=OAE.curie('boundary_conditions'),
                   model_uri=OAE.modelInputDetails__boundary_conditions, domain=None, range=Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]])

slots.modelInputDetails__atmospheric_forcing = Slot(uri=OAE.atmospheric_forcing, name="modelInputDetails__atmospheric_forcing", curie=OAE.curie('atmospheric_forcing'),
                   model_uri=OAE.modelInputDetails__atmospheric_forcing, domain=None, range=Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]])

slots.modelInputDetails__tidal_forcing = Slot(uri=OAE.tidal_forcing, name="modelInputDetails__tidal_forcing", curie=OAE.curie('tidal_forcing'),
                   model_uri=OAE.modelInputDetails__tidal_forcing, domain=None, range=Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]])

slots.modelInputDetails__river_sediment_flux_details = Slot(uri=OAE.river_sediment_flux_details, name="modelInputDetails__river_sediment_flux_details", curie=OAE.curie('river_sediment_flux_details'),
                   model_uri=OAE.modelInputDetails__river_sediment_flux_details, domain=None, range=Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]])

slots.modelInputDetails__processing_of_input_data = Slot(uri=OAE.processing_of_input_data, name="modelInputDetails__processing_of_input_data", curie=OAE.curie('processing_of_input_data'),
                   model_uri=OAE.modelInputDetails__processing_of_input_data, domain=None, range=Optional[str])

slots.modelInputDetails__processing_code = Slot(uri=OAE.processing_code, name="modelInputDetails__processing_code", curie=OAE.curie('processing_code'),
                   model_uri=OAE.modelInputDetails__processing_code, domain=None, range=Optional[Union[Union[dict, NamedLink], List[Union[dict, NamedLink]]]])

slots.analyzingInstrument__instrument_type = Slot(uri=OAE.instrument_type, name="analyzingInstrument__instrument_type", curie=OAE.curie('instrument_type'),
                   model_uri=OAE.analyzingInstrument__instrument_type, domain=None, range=Union[str, "AnalyzingInstrumentType"])

slots.analyzingInstrument__instrument_type_custom = Slot(uri=OAE.instrument_type_custom, name="analyzingInstrument__instrument_type_custom", curie=OAE.curie('instrument_type_custom'),
                   model_uri=OAE.analyzingInstrument__instrument_type_custom, domain=None, range=Optional[str])

slots.analyzingInstrument__serial_number = Slot(uri=OAE.serial_number, name="analyzingInstrument__serial_number", curie=OAE.curie('serial_number'),
                   model_uri=OAE.analyzingInstrument__serial_number, domain=None, range=Optional[str])

slots.analyzingInstrument__precision = Slot(uri=OAE.precision, name="analyzingInstrument__precision", curie=OAE.curie('precision'),
                   model_uri=OAE.analyzingInstrument__precision, domain=None, range=Optional[str])

slots.analyzingInstrument__accuracy = Slot(uri=OAE.accuracy, name="analyzingInstrument__accuracy", curie=OAE.curie('accuracy'),
                   model_uri=OAE.analyzingInstrument__accuracy, domain=None, range=str)

slots.analyzingInstrument__calibration = Slot(uri=OAE.calibration, name="analyzingInstrument__calibration", curie=OAE.curie('calibration'),
                   model_uri=OAE.analyzingInstrument__calibration, domain=None, range=Optional[Union[dict, Calibration]])

slots.pHInstrument__calibration = Slot(uri=OAE.calibration, name="pHInstrument__calibration", curie=OAE.curie('calibration'),
                   model_uri=OAE.pHInstrument__calibration, domain=None, range=Union[dict, PHCalibration])

slots.cRMInstrument__calibration = Slot(uri=OAE.calibration, name="cRMInstrument__calibration", curie=OAE.curie('calibration'),
                   model_uri=OAE.cRMInstrument__calibration, domain=None, range=Union[dict, CRMCalibration])

slots.cO2GasDetector__detector_type = Slot(uri=OAE.detector_type, name="cO2GasDetector__detector_type", curie=OAE.curie('detector_type'),
                   model_uri=OAE.cO2GasDetector__detector_type, domain=None, range=str)

slots.cO2GasDetector__calibration = Slot(uri=OAE.calibration, name="cO2GasDetector__calibration", curie=OAE.curie('calibration'),
                   model_uri=OAE.cO2GasDetector__calibration, domain=None, range=Union[dict, CO2Calibration])

slots.cO2GasDetector__resolution = Slot(uri=OAE.resolution, name="cO2GasDetector__resolution", curie=OAE.curie('resolution'),
                   model_uri=OAE.cO2GasDetector__resolution, domain=None, range=Optional[str])

slots.cO2GasDetector__uncertainty = Slot(uri=OAE.uncertainty, name="cO2GasDetector__uncertainty", curie=OAE.curie('uncertainty'),
                   model_uri=OAE.cO2GasDetector__uncertainty, domain=None, range=Optional[str])

slots.calibration__technique_description = Slot(uri=OAE.technique_description, name="calibration__technique_description", curie=OAE.curie('technique_description'),
                   model_uri=OAE.calibration__technique_description, domain=None, range=str)

slots.calibration__method_reference = Slot(uri=OAE.method_reference, name="calibration__method_reference", curie=OAE.curie('method_reference'),
                   model_uri=OAE.calibration__method_reference, domain=None, range=Optional[str])

slots.calibration__frequency = Slot(uri=OAE.frequency, name="calibration__frequency", curie=OAE.curie('frequency'),
                   model_uri=OAE.calibration__frequency, domain=None, range=Optional[str])

slots.calibration__last_calibration_date = Slot(uri=OAE.last_calibration_date, name="calibration__last_calibration_date", curie=OAE.curie('last_calibration_date'),
                   model_uri=OAE.calibration__last_calibration_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.calibration__calibration_certificates = Slot(uri=OAE.calibration_certificates, name="calibration__calibration_certificates", curie=OAE.curie('calibration_certificates'),
                   model_uri=OAE.calibration__calibration_certificates, domain=None, range=Optional[str])

slots.cRMCalibration__crm_manufacturer = Slot(uri=OAE.crm_manufacturer, name="cRMCalibration__crm_manufacturer", curie=OAE.curie('crm_manufacturer'),
                   model_uri=OAE.cRMCalibration__crm_manufacturer, domain=None, range=str)

slots.cRMCalibration__crm_batch_number = Slot(uri=OAE.crm_batch_number, name="cRMCalibration__crm_batch_number", curie=OAE.curie('crm_batch_number'),
                   model_uri=OAE.cRMCalibration__crm_batch_number, domain=None, range=str)

slots.pHCalibration__dye_type_and_manufacturer = Slot(uri=OAE.dye_type_and_manufacturer, name="pHCalibration__dye_type_and_manufacturer", curie=OAE.curie('dye_type_and_manufacturer'),
                   model_uri=OAE.pHCalibration__dye_type_and_manufacturer, domain=None, range=Optional[str])

slots.pHCalibration__dye_purified = Slot(uri=OAE.dye_purified, name="pHCalibration__dye_purified", curie=OAE.curie('dye_purified'),
                   model_uri=OAE.pHCalibration__dye_purified, domain=None, range=Optional[Union[bool, Bool]])

slots.pHCalibration__correction_for_unpurified_dye = Slot(uri=OAE.correction_for_unpurified_dye, name="pHCalibration__correction_for_unpurified_dye", curie=OAE.curie('correction_for_unpurified_dye'),
                   model_uri=OAE.pHCalibration__correction_for_unpurified_dye, domain=None, range=Optional[str])

slots.pHCalibration__dye_correction_method = Slot(uri=OAE.dye_correction_method, name="pHCalibration__dye_correction_method", curie=OAE.curie('dye_correction_method'),
                   model_uri=OAE.pHCalibration__dye_correction_method, domain=None, range=Optional[str])

slots.pHCalibration__ph_of_standards = Slot(uri=OAE.ph_of_standards, name="pHCalibration__ph_of_standards", curie=OAE.curie('ph_of_standards'),
                   model_uri=OAE.pHCalibration__ph_of_standards, domain=None, range=Optional[str])

slots.cO2Calibration__standard_gas_info = Slot(uri=OAE.standard_gas_info, name="cO2Calibration__standard_gas_info", curie=OAE.curie('standard_gas_info'),
                   model_uri=OAE.cO2Calibration__standard_gas_info, domain=None, range=Optional[Union[dict, StandardGas]])

slots.standardGas__manufacturer = Slot(uri=OAE.manufacturer, name="standardGas__manufacturer", curie=OAE.curie('manufacturer'),
                   model_uri=OAE.standardGas__manufacturer, domain=None, range=str)

slots.standardGas__concentration = Slot(uri=OAE.concentration, name="standardGas__concentration", curie=OAE.curie('concentration'),
                   model_uri=OAE.standardGas__concentration, domain=None, range=str)

slots.standardGas__uncertainty = Slot(uri=OAE.uncertainty, name="standardGas__uncertainty", curie=OAE.curie('uncertainty'),
                   model_uri=OAE.standardGas__uncertainty, domain=None, range=Optional[str])

slots.analyzing_instrument_type = Slot(uri=OAE.analyzing_instrument_type, name="analyzing_instrument_type", curie=OAE.curie('analyzing_instrument_type'),
                   model_uri=OAE.analyzing_instrument_type, domain=None, range=Optional[str])

slots.SpatialCoverage_geo = Slot(uri=OAE.geo, name="SpatialCoverage_geo", curie=OAE.curie('geo'),
                   model_uri=OAE.SpatialCoverage_geo, domain=SpatialCoverage, range=Union[dict, "GeoShape"])

slots.Organization_identifier = Slot(uri=SCHEMA.identifier, name="Organization_identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=OAE.Organization_identifier, domain=Organization, range=Optional[str])

slots.Organization_name = Slot(uri=SCHEMA.name, name="Organization_name", curie=SCHEMA.curie('name'),
                   model_uri=OAE.Organization_name, domain=Organization, range=str)

slots.Project_temporal_coverage = Slot(uri=SCHEMA.temporalCoverage, name="Project_temporal_coverage", curie=SCHEMA.curie('temporalCoverage'),
                   model_uri=OAE.Project_temporal_coverage, domain=Project, range=str,
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}/(\d{4}-\d{2}-\d{2}|\.\.)$'))

slots.Project_spatial_coverage = Slot(uri=SCHEMA.spatialCoverage, name="Project_spatial_coverage", curie=SCHEMA.curie('spatialCoverage'),
                   model_uri=OAE.Project_spatial_coverage, domain=Project, range=Union[dict, SpatialCoverage])

slots.Project_project_id = Slot(uri=OAE.project_id, name="Project_project_id", curie=OAE.curie('project_id'),
                   model_uri=OAE.Project_project_id, domain=Project, range=str)

slots.Project_description = Slot(uri=SCHEMA.description, name="Project_description", curie=SCHEMA.curie('description'),
                   model_uri=OAE.Project_description, domain=Project, range=str)

slots.MonetaryGrant_name = Slot(uri=SCHEMA.name, name="MonetaryGrant_name", curie=SCHEMA.curie('name'),
                   model_uri=OAE.MonetaryGrant_name, domain=MonetaryGrant, range=Optional[str])

slots.MonetaryGrant_identifier = Slot(uri=SCHEMA.identifier, name="MonetaryGrant_identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=OAE.MonetaryGrant_identifier, domain=MonetaryGrant, range=Optional[str])

slots.Experiment_project_id = Slot(uri=OAE.project_id, name="Experiment_project_id", curie=OAE.curie('project_id'),
                   model_uri=OAE.Experiment_project_id, domain=Experiment, range=str)

slots.Experiment_experiment_id = Slot(uri=OAE.experiment_id, name="Experiment_experiment_id", curie=OAE.curie('experiment_id'),
                   model_uri=OAE.Experiment_experiment_id, domain=Experiment, range=str)

slots.Experiment_description = Slot(uri=SCHEMA.description, name="Experiment_description", curie=SCHEMA.curie('description'),
                   model_uri=OAE.Experiment_description, domain=Experiment, range=str)

slots.Experiment_name = Slot(uri=SCHEMA.name, name="Experiment_name", curie=SCHEMA.curie('name'),
                   model_uri=OAE.Experiment_name, domain=Experiment, range=Optional[str])

slots.Experiment_spatial_coverage = Slot(uri=SCHEMA.spatialCoverage, name="Experiment_spatial_coverage", curie=SCHEMA.curie('spatialCoverage'),
                   model_uri=OAE.Experiment_spatial_coverage, domain=Experiment, range=Union[dict, SpatialCoverage])

slots.InSituExperiment_vertical_coverage = Slot(uri=OAE.vertical_coverage, name="InSituExperiment_vertical_coverage", curie=OAE.curie('vertical_coverage'),
                   model_uri=OAE.InSituExperiment_vertical_coverage, domain=InSituExperiment, range=Optional[Union[dict, VerticalExtent]])

slots.DosingConcentration_is_provided_as_a_file = Slot(uri=OAE.is_provided_as_a_file, name="DosingConcentration_is_provided_as_a_file", curie=OAE.curie('is_provided_as_a_file'),
                   model_uri=OAE.DosingConcentration_is_provided_as_a_file, domain=DosingConcentration, range=Union[bool, Bool])

slots.Variable_units = Slot(uri=OAE.units, name="Variable_units", curie=OAE.curie('units'),
                   model_uri=OAE.Variable_units, domain=Variable, range=str)

slots.ObservedPropertyVariable_qc_steps_taken = Slot(uri=OAE.qc_steps_taken, name="ObservedPropertyVariable_qc_steps_taken", curie=OAE.curie('qc_steps_taken'),
                   model_uri=OAE.ObservedPropertyVariable_qc_steps_taken, domain=ObservedPropertyVariable, range=str)

slots.ObservedPropertyVariable_uncertainty = Slot(uri=OAE.uncertainty, name="ObservedPropertyVariable_uncertainty", curie=OAE.curie('uncertainty'),
                   model_uri=OAE.ObservedPropertyVariable_uncertainty, domain=ObservedPropertyVariable, range=str)

slots.ObservedPropertyVariable_uncertainty_definition = Slot(uri=OAE.uncertainty_definition, name="ObservedPropertyVariable_uncertainty_definition", curie=OAE.curie('uncertainty_definition'),
                   model_uri=OAE.ObservedPropertyVariable_uncertainty_definition, domain=ObservedPropertyVariable, range=str)

slots.ObservedPropertyVariable_missing_value_indicators = Slot(uri=OAE.missing_value_indicators, name="ObservedPropertyVariable_missing_value_indicators", curie=OAE.curie('missing_value_indicators'),
                   model_uri=OAE.ObservedPropertyVariable_missing_value_indicators, domain=ObservedPropertyVariable, range=str)

slots.DiscretePHVariable_analyzing_instrument = Slot(uri=OAE.analyzing_instrument, name="DiscretePHVariable_analyzing_instrument", curie=OAE.curie('analyzing_instrument'),
                   model_uri=OAE.DiscretePHVariable_analyzing_instrument, domain=DiscretePHVariable, range=Union[dict, "PHInstrument"])

slots.DiscreteTAVariable_analyzing_instrument = Slot(uri=OAE.analyzing_instrument, name="DiscreteTAVariable_analyzing_instrument", curie=OAE.curie('analyzing_instrument'),
                   model_uri=OAE.DiscreteTAVariable_analyzing_instrument, domain=DiscreteTAVariable, range=Union[dict, "CRMInstrument"])

slots.DiscreteDICVariable_analyzing_instrument = Slot(uri=OAE.analyzing_instrument, name="DiscreteDICVariable_analyzing_instrument", curie=OAE.curie('analyzing_instrument'),
                   model_uri=OAE.DiscreteDICVariable_analyzing_instrument, domain=DiscreteDICVariable, range=Union[dict, "CRMInstrument"])

slots.DiscreteCO2Variable_analyzing_instrument = Slot(uri=OAE.analyzing_instrument, name="DiscreteCO2Variable_analyzing_instrument", curie=OAE.curie('analyzing_instrument'),
                   model_uri=OAE.DiscreteCO2Variable_analyzing_instrument, domain=DiscreteCO2Variable, range=Union[dict, "CO2GasDetector"])

slots.Dataset_name = Slot(uri=SCHEMA.name, name="Dataset_name", curie=SCHEMA.curie('name'),
                   model_uri=OAE.Dataset_name, domain=Dataset, range=str)

slots.Dataset_description = Slot(uri=SCHEMA.description, name="Dataset_description", curie=SCHEMA.curie('description'),
                   model_uri=OAE.Dataset_description, domain=Dataset, range=str)

slots.Dataset_project_id = Slot(uri=OAE.project_id, name="Dataset_project_id", curie=OAE.curie('project_id'),
                   model_uri=OAE.Dataset_project_id, domain=Dataset, range=str)

slots.Dataset_experiment_id = Slot(uri=OAE.experiment_id, name="Dataset_experiment_id", curie=OAE.curie('experiment_id'),
                   model_uri=OAE.Dataset_experiment_id, domain=Dataset, range=str)

slots.Platform_name = Slot(uri=SCHEMA.name, name="Platform_name", curie=SCHEMA.curie('name'),
                   model_uri=OAE.Platform_name, domain=Platform, range=Optional[str])

slots.ModelComponent_description = Slot(uri=SCHEMA.description, name="ModelComponent_description", curie=SCHEMA.curie('description'),
                   model_uri=OAE.ModelComponent_description, domain=ModelComponent, range=Optional[str])

slots.CO2GasDetector_analyzing_instrument_type = Slot(uri=OAE.analyzing_instrument_type, name="CO2GasDetector_analyzing_instrument_type", curie=OAE.curie('analyzing_instrument_type'),
                   model_uri=OAE.CO2GasDetector_analyzing_instrument_type, domain=CO2GasDetector, range=Optional[str])

slots.CO2GasDetector_manufacturer = Slot(uri=OAE.manufacturer, name="CO2GasDetector_manufacturer", curie=OAE.curie('manufacturer'),
                   model_uri=OAE.CO2GasDetector_manufacturer, domain=CO2GasDetector, range=str)

slots.CO2GasDetector_model = Slot(uri=OAE.model, name="CO2GasDetector_model", curie=OAE.curie('model'),
                   model_uri=OAE.CO2GasDetector_model, domain=CO2GasDetector, range=Optional[str])