def test_api_contest_types_get(pokeapi):
    contest_type = pokeapi.contest_types['cool'].data()
    assert contest_type.id == 1


def test_api_contest_types_list(pokeapi):
    resource_list = pokeapi.contest_types.list(limit=30, offset=0).data()
    assert len(resource_list.results) == resource_list.count


def test_api_contest_types_pagination(pokeapi):
    for page in pokeapi.contest_types.paginator(limit=10):
        assert len(page.data().results) <= 10


def test_api_contest_effects_get(pokeapi):
    contest_effect = pokeapi.contest_effects['1'].data()
    assert contest_effect.id == 1


def test_api_contest_effects_list(pokeapi):
    resource_list = pokeapi.contest_effects.list(limit=30, offset=0).data()
    assert len(resource_list.results) == 30


def test_api_contest_effects_pagination(pokeapi):
    for page in pokeapi.contest_effects.paginator(limit=10):
        assert len(page.data().results) <= 10


def test_api_super_contest_effects_get(pokeapi):
    super_contest_effect = pokeapi.super_contest_effects['1'].data()
    assert super_contest_effect.id == 1


def test_api_super_contest_effects_list(pokeapi):
    resource_list = pokeapi.super_contest_effects.list(limit=30, offset=0).data()
    assert len(resource_list.results) == resource_list.count


def test_api_super_contest_effects_pagination(pokeapi):
    for page in pokeapi.super_contest_effects.paginator(limit=10):
        assert len(page.data().results) <= 10
