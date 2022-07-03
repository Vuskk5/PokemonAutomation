from __future__ import annotations

from pydantic import BaseModel

from models.locations import Region
from models.moves import Move, MoveLearnMethod
from models.pokemon import Ability, PokemonSpecies, Type
from models.utility import NamedAPIResource, Name, Description


class Generation(BaseModel):
    id: int
    name: str
    abilities: list[NamedAPIResource[Ability]]
    names: list[Name]
    main_region: NamedAPIResource[Region]
    moves: list[NamedAPIResource[Move]]
    pokemon_species: list[NamedAPIResource[PokemonSpecies]]
    types: list[NamedAPIResource[Type]]
    version_groups: list[NamedAPIResource[VersionGroup]]


class Pokedex(BaseModel):
    id: int
    name: str
    is_main_series: bool
    descriptions: list[Description]
    names: list[Name]
    pokemon_entries: list[PokemonEntry]
    region: NamedAPIResource[Region]
    version_groups: list[NamedAPIResource[VersionGroup]]


class PokemonEntry(BaseModel):
    entry_number: int
    pokemon_species: NamedAPIResource[PokemonSpecies]


class Version(BaseModel):
    id: int
    name: str
    names: list[Name]
    version_group: NamedAPIResource[VersionGroup]


class VersionGroup(BaseModel):
    id: int
    name: str
    order: int
    generation: NamedAPIResource[Generation]
    move_learn_methods: list[NamedAPIResource[MoveLearnMethod]]
    pokedexes: list[NamedAPIResource[Pokedex]]
    regions: list[NamedAPIResource[Region]]
    versions: list[NamedAPIResource[Version]]
