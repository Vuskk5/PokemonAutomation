import logging

from models.evolution import EvolutionChain

log = logging.getLogger(__name__)


def test_api_berries_get(pokeapi):
    berry = pokeapi.berries.get('cheri').data()
    assert berry.id == 1


def test_api_berries_list(pokeapi):
    berries = pokeapi.berries.list(limit=30, offset=0).data().results
    assert len(berries) == 30


def test_api_berries_pagination(pokeapi):
    for page in pokeapi.berries.paginator(limit=10):
        assert len(page.data().results) <= 10


def test_api_berry_firmness_get(pokeapi):
    firmness = pokeapi.berry_firmnesses['very-soft'].data()
    assert firmness.id == 1


def test_api_berry_firmness_list(pokeapi):
    resource_list = pokeapi.berry_firmnesses.list(limit=30, offset=0).data()
    assert len(resource_list.results) == resource_list.count


def test_api_berry_firmness_pagination(pokeapi):
    for page in pokeapi.berry_firmnesses.paginator(limit=10):
        assert len(page.data().results) <= 10


def test_api_berry_flavor_get(pokeapi):
    firmness = pokeapi.berry_flavors['1'].data()
    assert firmness.id == 1


def test_api_berry_flavor_list(pokeapi):
    resource_list = pokeapi.berry_flavors.list(limit=30, offset=0).data()
    assert len(resource_list.results) == resource_list.count


def test_api_berry_flavor_pagination(pokeapi):
    for page in pokeapi.berry_flavors.paginator(limit=10):
        assert len(page.data().results) <= 10
