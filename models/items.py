from __future__ import annotations

from pydantic import BaseModel

from models.evolution import EvolutionChain
from models.games import Version
from models.pokemon import Pokemon
from models.utility import NamedAPIResource, VerboseEffect, VersionGroupFlavorText, GenerationGameIndex, Name, APIResource, MachineVersionDetail, \
    Description, Effect


class Item(BaseModel):
    id: int
    name: str
    cost: int
    fling_power: int
    fling_effect: NamedAPIResource[ItemFlingEffect]
    attributes: list[NamedAPIResource[ItemAttribute]]
    category: NamedAPIResource[ItemCategory]
    effect_entries: list[VerboseEffect]
    flavor_text_entries: list[VersionGroupFlavorText]
    game_indices: list[GenerationGameIndex]
    names: list[Name]
    sprites: ItemSprites
    held_by_pokemon: list[ItemHolderPokemon]
    baby_trigger_for: APIResource[EvolutionChain]
    machines: list[MachineVersionDetail]


class ItemSprites(BaseModel):
    default: str


class ItemHolderPokemon(BaseModel):
    pokemon: NamedAPIResource[Pokemon]
    version_details: list[ItemHolderPokemonVersionDetail]


class ItemHolderPokemonVersionDetail(BaseModel):
    rarity: int
    version: NamedAPIResource[Version]


class ItemAttribute(BaseModel):
    id: int
    name: str
    items: list[NamedAPIResource[Item]]
    names: list[Name]
    descriptions: list[Description]


class ItemCategory(BaseModel):
    id: int
    name: str
    items: list[NamedAPIResource[Item]]
    names: list[Name]
    pocket: NamedAPIResource[ItemPocket]


class ItemFlingEffect(BaseModel):
    id: int
    name: str
    effect_entries: list[Effect]
    items: list[NamedAPIResource[Item]]


class ItemPocket(BaseModel):
    id: int
    name: str
    categories: list[NamedAPIResource[ItemCategory]]
    names: list[Name]


Item.update_forward_refs()
ItemSprites.update_forward_refs()
ItemHolderPokemon.update_forward_refs()
ItemHolderPokemonVersionDetail.update_forward_refs()
ItemAttribute.update_forward_refs()
ItemCategory.update_forward_refs()
ItemFlingEffect.update_forward_refs()
ItemPocket.update_forward_refs()
