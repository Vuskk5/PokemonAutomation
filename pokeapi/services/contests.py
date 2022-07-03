from requests_toolbelt import sessions

from models.contests import ContestType, ContestEffect, SuperContestEffect
from models.utility import APIResourceList, NamedAPIResourceList
from pokeapi.endpoint import Endpoint


class ContestTypesService(Endpoint[ContestType, NamedAPIResourceList]):
    """
    Contest types are categories judges used to weigh a Pokémon's condition in Pokémon contests.
    Check out Bulbapedia for greater detail.
    """

    def __init__(self, session: sessions.BaseUrlSession):
        super().__init__(session, '/api/v2/contest-type', ContestType, NamedAPIResourceList)


class ContestEffectsService(Endpoint[ContestEffect, APIResourceList]):
    """
    Contest effects refer to the effects of moves when used in contests.
    """

    def __init__(self, session: sessions.BaseUrlSession):
        super().__init__(session, '/api/v2/contest-effect', ContestEffect, APIResourceList)


class SuperContestEffectsService(Endpoint[SuperContestEffect, APIResourceList]):
    """
    Super contest effects refer to the effects of moves when used in super contests.
    """

    def __init__(self, session: sessions.BaseUrlSession):
        super().__init__(session, '/api/v2/super-contest-effect', SuperContestEffect, APIResourceList)
