import json

from Requests import PokemonRequests
from Utils.AssertionUtils import AssertionUtils


def test_1_get_type_has_exactly_20_different_types():
    expected_types_count = 20
    body = PokemonRequests.get_type()
    count = body.get('count')
    result_names = AssertionUtils.validate_jsonpath(body, 'results..name')

    AssertionUtils.assert_equal(expected_types_count, count, 'count')
    AssertionUtils.assert_equal(expected_types_count, len(set(result_names)), 'unique type names')


def test_2_fire_type_pokemons():
    fire_types = PokemonRequests.get_pokemon_types('fire')
    fire_pokemon_names = AssertionUtils.validate_jsonpath(fire_types, 'pokemon..pokemon.name')
    AssertionUtils.validate_in_list('charmander', fire_pokemon_names, 'pokemon name')
    AssertionUtils.validate_not_in_list('bulbasaur', fire_pokemon_names, 'pokemon name')


def test_3_fire_type_weight():
    try:
        with open('../ExpectedFiles/ExpectedTop5WeightsPokemons.json', 'r') as file:
            expected_top_5_weights = json.load(file)
        expected_pokemon_weights = list(zip([list(p.keys())[0] for p in expected_top_5_weights],
                                            [list(list(p.values())[0].values())[0] for p in expected_top_5_weights]))
        pokemon_names = [list(pokemon.keys())[0] for pokemon in expected_top_5_weights]
    except:
        raise Exception('Failed to extract ExpectedTop5WeightsPokemons.json file.')

    actual_pokemon_weights = list(zip([pokemon_name for pokemon_name in pokemon_names],
                                      [PokemonRequests.get_pokemon(p).get('weight') for p in pokemon_names]))
    AssertionUtils.assert_equal(expected_pokemon_weights, actual_pokemon_weights, 'top 5 pokemon weights')
