from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from models.contests import ContestType, ContestEffect, SuperContestEffect
    from models.games import Generation, VersionGroup
    from models.pokemon import Pokemon, AbilityEffectChange, Type, Stat
    from models.utility import NamedAPIResource, APIResource, VerboseEffect, MachineVersionDetail, Name, Language, Description


class Move(BaseModel):
    id: int
    name: str
    accuracy: int
    effect_chance: int
    pp: int
    priority: int
    power: int
    contest_combos: ContestComboSet
    contest_type: NamedAPIResource[ContestType]
    contest_effect: APIResource[ContestEffect]
    damage_class: NamedAPIResource[MoveDamageClass]
    effect_entries: list[VerboseEffect]
    effect_changes: list[AbilityEffectChange]
    learned_by_pokemon: list[NamedAPIResource[Pokemon]]
    flavor_text_entries: list[MoveFlavorText]
    generation: NamedAPIResource[Generation]
    machines: list[MachineVersionDetail]
    meta: MoveMetaData
    names: list[Name]
    past_values: list[PastMoveStatValues]
    stat_changes: list[MoveStatChange]
    super_contest_effect: APIResource[SuperContestEffect]
    target: NamedAPIResource[MoveTarget]
    type: NamedAPIResource[Type]


class ContestComboSet(BaseModel):
    normal: ContestComboDetail
    super: ContestComboDetail


class ContestComboDetail(BaseModel):
    use_before: list[NamedAPIResource[Move]]
    use_after: list[NamedAPIResource[Move]]


class MoveFlavorText(BaseModel):
    flavor_text: str
    language: NamedAPIResource[Language]
    version_group: NamedAPIResource[VersionGroup]


class MoveMetaData(BaseModel):
    ailment: NamedAPIResource[MoveAilment]
    category: NamedAPIResource[MoveCategory]
    min_hits: int
    max_hits: int
    min_turns: Optional[int]
    max_turns: Optional[int]
    drain: int
    healing: int
    crit_rate: int
    ailment_chance: int
    flinch_chance: int
    stat_chance: int


class MoveStatChange(BaseModel):
    change: int
    stat: NamedAPIResource[Stat]


class PastMoveStatValues(BaseModel):
    accuracy: int
    effect_chance: int
    power: int
    pp: int
    effect_entries: list[VerboseEffect]
    type: NamedAPIResource[Type]
    version_group: NamedAPIResource[VersionGroup]


class MoveAilment(BaseModel):
    id: int
    name: str
    moves: list[NamedAPIResource[Move]]
    names: list[Name]


class MoveBattleStyle(BaseModel):
    id: int
    name: str
    names: list[Name]


class MoveCategory(BaseModel):
    id: int
    name: str
    moves: list[NamedAPIResource[Move]]
    descriptions: list[Description]


class MoveDamageClass(BaseModel):
    id: int
    name: str
    descriptions: list[Description]
    moves: list[NamedAPIResource[Move]]
    names: list[Name]


class MoveLearnMethod(BaseModel):
    id: int
    name: str
    descriptions: list[Description]
    names: list[Name]
    version_groups: list[NamedAPIResource[VersionGroup]]


class MoveTarget(BaseModel):
    id: int
    name: str
    descriptions: list[Description]
    moves: list[NamedAPIResource[Move]]
    names: list[Name]
