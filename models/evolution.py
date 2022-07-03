from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from models.locations import Location
from models.moves import Move
from models.pokemon import PokemonSpecies, Type
from models.utility import Name, NamedAPIResource

if TYPE_CHECKING:
    from models.items import Item


class EvolutionChain(BaseModel):
    id: int
    baby_trigger_item: NamedAPIResource['Item']
    chain: ChainLink


class ChainLink(BaseModel):
    is_baby: bool
    species: NamedAPIResource[PokemonSpecies]
    evolution_details: list[EvolutionDetail]
    evolves_to: list[ChainLink]


class EvolutionDetail(BaseModel):
    item: NamedAPIResource['Item']
    trigger: NamedAPIResource[EvolutionTrigger]
    gender: int
    held_item: NamedAPIResource['Item']
    known_move: NamedAPIResource[Move]
    known_move_type: NamedAPIResource[Type]
    location: NamedAPIResource[Location]
    min_level: int
    min_happiness: int
    min_beauty: int
    min_affection: int
    needs_overworld_rain: bool
    party_species: NamedAPIResource[PokemonSpecies]
    party_type: NamedAPIResource[Type]
    relative_physical_stats: int
    time_of_day: str
    trade_species: NamedAPIResource[PokemonSpecies]
    turn_upside_down: bool


class EvolutionTrigger(BaseModel):
    id: int
    name: str
    names: list[Name]
    pokemon_species: NamedAPIResource[PokemonSpecies]


EvolutionChain.update_forward_refs()
ChainLink.update_forward_refs()
EvolutionDetail.update_forward_refs()
EvolutionTrigger.update_forward_refs()
