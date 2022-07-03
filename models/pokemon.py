from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from models.berries import BerryFlavor
    from models.evolution import EvolutionChain
    from models.games import Generation, VersionGroup, Version, Pokedex
    from models.items import Item
    from models.locations import LocationArea, PalParkArea
    from models.moves import MoveBattleStyle, Move, MoveLearnMethod, MoveDamageClass
    from models.utility import NamedAPIResource, Name, VerboseEffect, Effect, Language, Description, VersionGameIndex, VersionEncounterDetail, \
        APIResource, FlavorText, GenerationGameIndex


class Ability(BaseModel):
    id: int
    name: str
    is_main_series: bool
    generation: NamedAPIResource[Generation]
    names: list[Name]
    effect_entries: list[VerboseEffect]
    effect_changes: list[AbilityEffectChange]
    flavor_text_entries: list[AbilityFlavorText]
    pokemon: AbilityPokemon


class AbilityEffectChange(BaseModel):
    effect_entries: list[Effect]
    version_group: NamedAPIResource[VersionGroup]


class AbilityFlavorText(BaseModel):
    flavor_text: str
    language: NamedAPIResource[Language]
    version_group: NamedAPIResource[VersionGroup]


class AbilityPokemon(BaseModel):
    is_hidden: bool
    slot: int
    pokemon: NamedAPIResource[Pokemon]


class Characteristic(BaseModel):
    id: int
    gene_modulo: int
    possible_values: list[int]


class EggGroup(BaseModel):
    id: int
    name: str
    names: list[Name]
    pokemon_species: list[NamedAPIResource[PokemonSpecies]]


class Gender(BaseModel):
    id: int
    name: str
    pokemon_species_details: list[PokemonSpeciesGender]
    required_for_evolution: list[NamedAPIResource[PokemonSpecies]]


class PokemonSpeciesGender(BaseModel):
    rate: int
    pokemon_species: NamedAPIResource[PokemonSpecies]


class GrowthRate(BaseModel):
    id: int
    name: str
    formula: str
    descriptions: list[Description]
    levels: list[GrowthRateExperienceLevel]
    pokemon_species: list[NamedAPIResource[PokemonSpecies]]


class GrowthRateExperienceLevel(BaseModel):
    level: int
    experience: int


class Nature(BaseModel):
    id: int
    name: str
    decreased_stat: NamedAPIResource[Stat]
    increased_stat: NamedAPIResource[Stat]
    hates_flavor: NamedAPIResource[BerryFlavor]
    likes_flavor: NamedAPIResource[BerryFlavor]
    pokeathlon_stat_changes: list[NatureStatChange]
    move_battle_style_preferences: list[MoveBattleStylePreference]
    names: list[Name]


class NatureStatChange(BaseModel):
    max_change: int
    pokeathlon_stat: NamedAPIResource[PokeathlonStat]


class MoveBattleStylePreference(BaseModel):
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: NamedAPIResource[MoveBattleStyle]


class PokeathlonStat(BaseModel):
    id: int
    name: str
    names: list[Name]
    affecting_natures: NaturePokeathlonStatAffectSets


class NaturePokeathlonStatAffectSets(BaseModel):
    increase: list[NaturePokeathlonStatAffect]
    decrease: list[NaturePokeathlonStatAffect]


class NaturePokeathlonStatAffect(BaseModel):
    max_change: int
    nature: NamedAPIResource[Nature]


class Pokemon(BaseModel):
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: list[PokemonAbility]
    forms: list[NamedAPIResource[PokemonForm]]
    game_indices: list[VersionGameIndex]
    held_items: list[PokemonHeldItem]
    location_area_encounters: str
    moves: list[PokemonMove]
    past_types: list[PokemonTypePast]
    sprites: PokemonSprites
    species: NamedAPIResource[PokemonSpecies]
    stats: list[PokemonStat]
    types: list[PokemonType]


class PokemonAbility(BaseModel):
    is_hidden: bool
    slot: int
    ability: NamedAPIResource[Ability]


class PokemonType(BaseModel):
    slot: int
    type: NamedAPIResource[Type]


class PokemonFormType(BaseModel):
    slot: int
    type: NamedAPIResource[Type]


class PokemonTypePast(BaseModel):
    generation: NamedAPIResource[Generation]
    types: list[PokemonType]


class PokemonHeldItem(BaseModel):
    item: NamedAPIResource[Item]
    version_details: list[PokemonHeldItemVersion]


class PokemonHeldItemVersion(BaseModel):
    version: NamedAPIResource[Version]
    rarity: int


class PokemonMove(BaseModel):
    move: NamedAPIResource[Move]
    version_group_details: list[PokemonMoveVersion]


class PokemonMoveVersion(BaseModel):
    move_learn_method: NamedAPIResource[MoveLearnMethod]
    version_group: NamedAPIResource[VersionGroup]
    level_learned_at: int


class PokemonStat(BaseModel):
    stat: NamedAPIResource[Stat]
    effort: int
    base_stat: int


class PokemonSprites(BaseModel):
    front_default: str
    front_shiny: str
    front_female: str
    front_shiny_female: str
    back_default: str
    back_shiny: str
    back_female: str
    back_shiny_female: str


class LocationAreaEncounter(BaseModel):
    location_area: NamedAPIResource[LocationArea]
    version_details: list[VersionEncounterDetail]


class PokemonColor(BaseModel):
    id: int
    name: str
    names: list[Name]
    pokemon_species: list[NamedAPIResource[PokemonSpecies]]


class PokemonForm(BaseModel):
    id: int
    name: str
    order: int
    form_order: int
    is_default: bool
    is_battle_only: bool
    is_mega: bool
    form_name: str
    pokemon: NamedAPIResource[Pokemon]
    types: list[PokemonFormType]
    sprites: PokemonFormSprites
    version_group: NamedAPIResource[VersionGroup]
    names: list[Name]
    form_names: list[Name]


class PokemonFormSprites(BaseModel):
    front_default: str
    front_shiny: str
    back_default: str
    back_shiny: str


class PokemonHabitat(BaseModel):
    id: int
    name: str
    names: list[Name]
    pokemon_species: list[NamedAPIResource[PokemonSpecies]]


class PokemonShape(BaseModel):
    id: int
    name: str
    awesome_names: list[AwesomeName]
    names: list[Name]
    pokemon_species: list[NamedAPIResource[PokemonSpecies]]


class AwesomeName(BaseModel):
    awesome_name: str
    language: NamedAPIResource[Language]


class PokemonSpecies(BaseModel):
    id: int
    name: str
    order: int
    gender_rate: int
    capture_rate: int
    base_happiness: int
    is_baby: bool
    is_legendary: bool
    is_mythical: bool
    hatch_counter: int
    has_gender_differences: bool
    forms_switchable: bool
    growth_rate: NamedAPIResource[GrowthRate]
    pokedex_numbers: list[PokemonSpeciesDexEntry]
    egg_groups: list[NamedAPIResource[EggGroup]]
    color: NamedAPIResource[PokemonColor]
    shape: NamedAPIResource[PokemonShape]
    evolves_from_species: NamedAPIResource[PokemonSpecies]
    evolution_chain: APIResource[EvolutionChain]
    habitat: NamedAPIResource[PokemonHabitat]
    generation: NamedAPIResource[Generation]
    names: list[Name]
    pal_park_encounters: list[PalParkEncounterArea]
    flavor_text_entries: list[FlavorText]
    form_descriptions: list[Description]
    genera: list[Genus]
    varieties: list[PokemonSpeciesVariety]


class Genus(BaseModel):
    genus: str
    language: NamedAPIResource[Language]


class PokemonSpeciesDexEntry(BaseModel):
    entry_number: int
    pokedex: NamedAPIResource[Pokedex]


class PalParkEncounterArea(BaseModel):
    base_score: int
    rate: int
    area: NamedAPIResource[PalParkArea]


class PokemonSpeciesVariety(BaseModel):
    is_default: bool
    pokemon: NamedAPIResource[Pokemon]


class Stat(BaseModel):
    id: int
    name: str
    game_index: int
    is_battle_only: bool
    affecting_moves: MoveStatAffectSets
    affecting_natures: NatureStatAffectSets
    characteristics: list[APIResource[Characteristic]]
    move_damage_class: NamedAPIResource[MoveDamageClass]
    names: list[Name]


class MoveStatAffectSets(BaseModel):
    increase: list[MoveStatAffect]
    decrease: list[MoveStatAffect]


class MoveStatAffect(BaseModel):
    change: int
    move: NamedAPIResource[Move]


class NatureStatAffectSets(BaseModel):
    increase: list[NamedAPIResource[Nature]]
    decrease: list[NamedAPIResource[Nature]]


class Type(BaseModel):
    id: int
    name: str
    damage_relations: TypeRelations
    past_damage_relations: list[TypeRelationsPast]
    game_indices: list[GenerationGameIndex]
    generation: NamedAPIResource[Generation]
    move_damage_class: NamedAPIResource[MoveDamageClass]
    names: list[Name]
    pokemon: list[TypePokemon]
    moves: list[NamedAPIResource[Move]]


class TypePokemon(BaseModel):
    slot: int
    pokemon: NamedAPIResource[Pokemon]


class TypeRelations(BaseModel):
    no_damage_to: list[NamedAPIResource[Type]]
    half_damage_to: list[NamedAPIResource[Type]]
    double_damage_to: list[NamedAPIResource[Type]]
    no_damage_from: list[NamedAPIResource[Type]]
    half_damage_from: list[NamedAPIResource[Type]]
    double_damage_from: list[NamedAPIResource[Type]]


class TypeRelationsPast(BaseModel):
    generation: NamedAPIResource[Generation]
    damage_relations: TypeRelations
