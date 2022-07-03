from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from models.encounters import EncounterMethod
    from models.games import Version, Generation, Pokedex, VersionGroup
    from models.pokemon import Pokemon, PokemonSpecies
    from models.utility import NamedAPIResource, Name, GenerationGameIndex, VersionEncounterDetail


class Location(BaseModel):
    id: int
    name: str
    region: NamedAPIResource[Region]
    names: list[Name]
    game_indices: list[GenerationGameIndex]
    areas: list[NamedAPIResource[LocationArea]]


class LocationArea(BaseModel):
    id: int
    name: str
    game_index: int
    encounter_method_rates: list[EncounterMethodRate]
    location: NamedAPIResource[Location]
    names: list[Name]
    pokemon_encounters: list[PokemonEncounter]


class EncounterMethodRate(BaseModel):
    encounter_method: NamedAPIResource[EncounterMethod]
    version_details: list[EncounterVersionDetails]


class EncounterVersionDetails(BaseModel):
    rate: int
    version: NamedAPIResource[Version]


class PokemonEncounter(BaseModel):
    pokemon: NamedAPIResource[Pokemon]
    version_details: list[VersionEncounterDetail]


class PalParkArea(BaseModel):
    id: int
    name: str
    names: list[Name]
    pokemon_encounters: list[PalParkEncounterSpecies]


class PalParkEncounterSpecies(BaseModel):
    base_score: int
    rate: int
    pokemon_species: NamedAPIResource[PokemonSpecies]


class Region(BaseModel):
    id: int
    locations: list[NamedAPIResource[Location]]
    name: str
    names: list[Name]
    main_generation: NamedAPIResource[Generation]
    pokedexes: list[NamedAPIResource[Pokedex]]
    version_groups: list[NamedAPIResource[VersionGroup]]
