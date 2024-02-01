from Requests import PokemonRequests
from jsonpath import jsonpath

from Utils.AssertionUtils import AssertionUtils


def test_1_get_type_has_exactly_20_different_types():
    expected_types_count = 20
    body = PokemonRequests.get_type()
    count = body.get('count')
    result_names = AssertionUtils.validate_jsonpath(body, 'results..name')

    AssertionUtils.assert_equal(expected_types_count, count, 'count')
    AssertionUtils.assert_equal(expected_types_count, len(set(result_names)), 'unique type names')


def test_2_fire_type_pokemons():
    body = PokemonRequests.get_type()
    fire_url = AssertionUtils.validate_jsonpath(body, 'results[?(@.name=="fire")].url')[0]
    fire_types = PokemonRequests.get_type(fire_url)
    fire_pokemon_names = AssertionUtils.validate_jsonpath(fire_types, 'pokemon..pokemon.name')
    AssertionUtils.validate_in_list('charmander', fire_pokemon_names, 'pokemon name')
    AssertionUtils.validate_not_in_list('bulbasaur', fire_pokemon_names, 'pokemon name')
