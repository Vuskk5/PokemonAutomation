import logging
import os

import requests
from requests_toolbelt import sessions

import pokeapi.services as services


log = logging.getLogger('pokeapi')
log.setLevel(logging.DEBUG)


def _log_response(response: requests.Response, *args, **kwargs):
    log.info(f'{response.request.method.ljust(7)} {response.url} {response.status_code} {len(response.content)}{os.linesep}')
    log.debug(f'Request body     : {response.request.body}{os.linesep}'
              f'Response content : {response.content}')


def _verify_response(response: requests.Response, *args, **kwargs):
    response.raise_for_status()


class PokeAPI:
    def __init__(self, base_url: str):
        self.session = sessions.BaseUrlSession(base_url=base_url)
        self.session.hooks['response'] = [_log_response, _verify_response]
        # Berries
        self.berries = services.BerriesService(self.session)
        self.berry_firmnesses = services.BerryFirmnessesService(self.session)
        self.berry_flavors = services.BerryFlavorsService(self.session)
        # Contests
        self.contest_types = services.ContestTypesService(self.session)
        self.contest_effects = services.ContestEffectsService(self.session)
        self.super_contest_effects = services.SuperContestEffectsService(self.session)
        # Encounters
        self.encounter_methods = services.EncounterMethodsService(self.session)
        self.encounter_conditions = services.EncounterConditionsService(self.session)
        self.encounter_condition_values = services.EncounterConditionValuesService(self.session)
