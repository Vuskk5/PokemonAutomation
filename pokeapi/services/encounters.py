from requests_toolbelt import sessions

from models.encounters import EncounterMethod, EncounterCondition, EncounterConditionValue
from models.utility import NamedAPIResourceList
from pokeapi.endpoint import Endpoint


class EncounterMethodsService(Endpoint[EncounterMethod, NamedAPIResourceList]):
    """
    Methods by which the player might can encounter Pokémon in the wild, e.g., walking in tall grass.
    Check out Bulbapedia for greater detail.
    """

    def __init__(self, session: sessions.BaseUrlSession):
        super().__init__(session, '/api/v2/encounter-method', EncounterMethod, NamedAPIResourceList)


class EncounterConditionsService(Endpoint[EncounterCondition, NamedAPIResourceList]):
    """
    Conditions which affect what pokemon might appear in the wild, e.g., day or night.
    """

    def __init__(self, session: sessions.BaseUrlSession):
        super().__init__(session, '/api/v2/encounter-condition', EncounterCondition, NamedAPIResourceList)


class EncounterConditionValuesService(Endpoint[EncounterConditionValue, NamedAPIResourceList]):
    """
    Encounter condition values are the various states that an encounter condition can have, i.e., time of day can be either day or night.
    """

    def __init__(self, session: sessions.BaseUrlSession):
        super().__init__(session, '/api/v2/encounter-condition-value', EncounterConditionValue, NamedAPIResourceList)
