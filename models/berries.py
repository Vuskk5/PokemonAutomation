from __future__ import annotations

from pydantic import BaseModel

from models.contests import ContestType
from models.items import Item
from models.pokemon import Type
from models.utility import Name
from models.utility import NamedAPIResource


class BerryFlavorMap(BaseModel):
    potency: int
    flavor: NamedAPIResource[BerryFlavor]


class FlavorBerryMap(BaseModel):
    potency: int
    berry: NamedAPIResource[Berry]


class BerryFirmness(BaseModel):
    id: int
    name: str
    berries: list[NamedAPIResource[Berry]]
    names: list[Name]


class BerryFlavor(BaseModel):
    id: int
    name: str
    berries: list[FlavorBerryMap]
    contest_type: NamedAPIResource[ContestType]
    names: list[Name]


class Berry(BaseModel):
    id: int
    name: str
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    size: int
    smoothness: int
    soil_dryness: int
    firmness: NamedAPIResource[BerryFirmness]
    flavors: list[BerryFlavorMap]
    item: NamedAPIResource[Item]
    natural_gift_type: NamedAPIResource[Type]


BerryFlavorMap.update_forward_refs()
FlavorBerryMap.update_forward_refs()
BerryFirmness.update_forward_refs()
BerryFlavor.update_forward_refs()
Berry.update_forward_refs()
