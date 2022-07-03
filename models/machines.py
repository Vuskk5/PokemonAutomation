from __future__ import annotations

from pydantic import BaseModel

from models.games import VersionGroup
from models.items import Item
from models.moves import Move
from models.utility import NamedAPIResource


class Machine(BaseModel):
    id: int
    item: NamedAPIResource[Item]
    move: NamedAPIResource[Move]
    version_group: NamedAPIResource[VersionGroup]
