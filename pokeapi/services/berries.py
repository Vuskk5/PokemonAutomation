from requests_toolbelt import sessions

from models.berries import Berry, BerryFirmness, BerryFlavor
from models.utility import NamedAPIResourceList
from pokeapi.endpoint import Endpoint


class BerriesService(Endpoint[Berry, NamedAPIResourceList]):
    """
    Berries are small fruits that can provide HP and status condition restoration, stat enhancement, and even damage negation when eaten by Pokémon.
    Check out Bulbapedia for greater detail.
    """

    def __init__(self, session: sessions.BaseUrlSession):
        super().__init__(session, '/api/v2/berry', Berry, NamedAPIResourceList)


class BerryFirmnessesService(Endpoint[BerryFirmness, NamedAPIResourceList]):
    """
    Berries can be soft or hard. Check out Bulbapedia for greater detail.
    """

    def __init__(self, session: sessions.BaseUrlSession):
        super().__init__(session, '/api/v2/berry-firmness', BerryFirmness, NamedAPIResourceList)


class BerryFlavorsService(Endpoint[BerryFlavor, NamedAPIResourceList]):
    """
    Flavors determine whether a Pokémon will benefit or suffer from eating a berry based on their nature. Check out Bulbapedia for greater detail.
    """

    def __init__(self, session: sessions.BaseUrlSession):
        super().__init__(session, '/api/v2/berry-flavor', BerryFlavor, NamedAPIResourceList)
