from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from typing import TypeVar, Generic

from pydantic import BaseModel
from pydantic.generics import GenericModel

if TYPE_CHECKING:
    from models.encounters import EncounterConditionValue, EncounterMethod
    from models.games import Version, Generation, VersionGroup
    from models.machines import Machine

ResourceType = TypeVar('ResourceType')


class APIResource(GenericModel, Generic[ResourceType]):
    url: str


class APIResourceList(GenericModel, Generic[ResourceType]):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: list[APIResource[ResourceType]]


class NamedAPIResource(GenericModel, Generic[ResourceType]):
    name: str
    url: str


class NamedAPIResourceList(GenericModel, Generic[ResourceType]):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: list[NamedAPIResource[ResourceType]]


class Language(BaseModel):
    id: int
    name: str
    official: bool
    iso639: str
    iso3166: str
    names: list[Name]


class Name(BaseModel):
    name: str
    language: NamedAPIResource[Language]


class Description(BaseModel):
    description: str
    language: NamedAPIResource[Language]


class Effect(BaseModel):
    effect: str
    language: NamedAPIResource[Language]


class Encounter(BaseModel):
    min_level: int
    max_level: int
    condition_values: list[NamedAPIResource[EncounterConditionValue]]
    chance: int
    method: NamedAPIResource[EncounterMethod]


class FlavorText(BaseModel):
    flavor_text: str
    language: NamedAPIResource[Language]
    # Field could be missing
    version: Optional[NamedAPIResource[Version]] = None


class GenerationGameIndex(BaseModel):
    game_index: int
    generation: NamedAPIResource[Generation]


class MachineVersionDetail(BaseModel):
    machine: APIResource[Machine]
    version_group: NamedAPIResource[VersionGroup]


class VerboseEffect(BaseModel):
    effect: str
    short_effect: str
    language: NamedAPIResource[Language]


class VersionEncounterDetail(BaseModel):
    version: NamedAPIResource[Version]
    max_chance: int
    encounter_details: list[Encounter]


class VersionGameIndex(BaseModel):
    game_index: int
    version: NamedAPIResource[Version]


class VersionGroupFlavorText(BaseModel):
    text: str
    language: NamedAPIResource[Language]
    version_group: NamedAPIResource[VersionGroup]

