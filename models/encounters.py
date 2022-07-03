from __future__ import annotations

from pydantic import BaseModel

from models.utility import Name, NamedAPIResource


class EncounterMethod(BaseModel):
    id: int
    name: str
    order: int
    names: list[Name]


class EncounterCondition(BaseModel):
    id: int
    name: str
    names: list[Name]
    values: list[NamedAPIResource[EncounterConditionValue]]


class EncounterConditionValue(BaseModel):
    id: int
    name: str
    condition: NamedAPIResource[EncounterCondition]
    names: list[Name]
