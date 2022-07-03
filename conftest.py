import logging

import pytest

import pokeapi as poke


logging.getLogger('urllib3.connectionpool').setLevel(logging.INFO)


@pytest.fixture()
def pokeapi() -> poke.PokeAPI:
    return poke.PokeAPI(base_url='https://pokeapi.co/')
