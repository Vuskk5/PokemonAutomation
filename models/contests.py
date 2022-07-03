from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from models.moves import Move
from models.utility import NamedAPIResource, Language, Effect, FlavorText

if TYPE_CHECKING:
    from models.berries import BerryFlavor


class ContestName(BaseModel):
    name: str
    color: str
    language: NamedAPIResource[Language]


class ContestType(BaseModel):
    id: int
    name: str
    berry_flavor: NamedAPIResource['BerryFlavor']
    names: list[ContestName]


class ContestEffect(BaseModel):
    id: int
    appeal: int
    jam: int
    effect_entries: list[Effect]
    flavor_text_entries: list[FlavorText]


class SuperContestEffect(BaseModel):
    id: int
    appeal: int
    flavor_text_entries: list[FlavorText]
    moves: list[NamedAPIResource[Move]]


ContestType.update_forward_refs()
