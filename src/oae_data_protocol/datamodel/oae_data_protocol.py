# Auto generated from oae_data_protocol.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-05T15:21:25
# Schema: oae-data-protocol
#
# id: https://w3id.org/clevinson/oae-data-protocol
# description: Base ontology and data schemas for ocean alkalinity enhancement projects, experiments, and field trails. This project aims to be a technical complement to Submarine Scientific's OAE Data Protocol, developed in conjunction with Carbon To Sea and NOAA.
# license: Apache Software License 2.0

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

from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OAE_DATA_PROTOCOL = CurieNamespace('oae_data_protocol', 'https://w3id.org/clevinson/oae-data-protocol/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = OAE_DATA_PROTOCOL


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class ProjectId(NamedThingId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = OAE_DATA_PROTOCOL.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Project(NamedThing):
    """
    Represents a Project
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE_DATA_PROTOCOL["Project"]
    class_class_curie: ClassVar[str] = "oae_data_protocol:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = OAE_DATA_PROTOCOL.Project

    id: Union[str, ProjectId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProjectCollection(YAMLRoot):
    """
    A holder for Project objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OAE_DATA_PROTOCOL["ProjectCollection"]
    class_class_curie: ClassVar[str] = "oae_data_protocol:ProjectCollection"
    class_name: ClassVar[str] = "ProjectCollection"
    class_model_uri: ClassVar[URIRef] = OAE_DATA_PROTOCOL.ProjectCollection

    entries: Optional[Union[Dict[Union[str, ProjectId], Union[dict, Project]], List[Union[dict, Project]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Project, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=OAE_DATA_PROTOCOL.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=OAE_DATA_PROTOCOL.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=OAE_DATA_PROTOCOL.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=OAE_DATA_PROTOCOL.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=OAE_DATA_PROTOCOL.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=OAE_DATA_PROTOCOL.age_in_years, name="age_in_years", curie=OAE_DATA_PROTOCOL.curie('age_in_years'),
                   model_uri=OAE_DATA_PROTOCOL.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=OAE_DATA_PROTOCOL.vital_status, name="vital_status", curie=OAE_DATA_PROTOCOL.curie('vital_status'),
                   model_uri=OAE_DATA_PROTOCOL.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.projectCollection__entries = Slot(uri=OAE_DATA_PROTOCOL.entries, name="projectCollection__entries", curie=OAE_DATA_PROTOCOL.curie('entries'),
                   model_uri=OAE_DATA_PROTOCOL.projectCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ProjectId], Union[dict, Project]], List[Union[dict, Project]]]])

slots.Project_primary_email = Slot(uri=SCHEMA.email, name="Project_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=OAE_DATA_PROTOCOL.Project_primary_email, domain=Project, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))