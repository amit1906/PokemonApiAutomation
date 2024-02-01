import json

from Requests import PokemonRequests
from Utils.AssertionUtils import AssertionUtils


def test_1_get_type_has_exactly_20_different_types():
    expected_types_count = 20
    body = PokemonRequests.get_type()
    count = body.get('count')
    result_names = AssertionUtils.validate_jsonpath(body, 'results..name')

    # field of 'count' should equal expected
    AssertionUtils.assert_equal(expected_types_count, count, 'count')
    # number of unique pokimon names should equal expected
    AssertionUtils.assert_equal(expected_types_count, len(set(result_names)), 'unique type names')


def test_2_fire_type_pokemons():
    fire_types = PokemonRequests.get_pokemon_types('fire')
    fire_pokemon_names = AssertionUtils.validate_jsonpath(fire_types, 'pokemon..pokemon.name')

    # charmander should be in 'fire' type pokimons list
    AssertionUtils.validate_in_list('charmander', fire_pokemon_names, 'pokemon name')
    # bulbasaur should not be in 'fire' type pokimons list
    AssertionUtils.validate_not_in_list('bulbasaur', fire_pokemon_names, 'pokemon name')


def test_3_top_5_fire_type_weight():
    try:
        with open('../ExpectedFiles/ExpectedTop5WeightsPokemons.json', 'r') as file:
            expected_top_5_weights = json.load(file)
        expected_pokemon_weights = [{name: value} for name, value in
                                    zip([list(p.keys())[0] for p in expected_top_5_weights],
                                        [list(list(p.values())[0].values())[0] for p in expected_top_5_weights])]
    except:
        raise Exception('Failed to extract ExpectedTop5WeightsPokemons.json file.')

    fire_types = PokemonRequests.get_pokemon_types('fire')
    fire_pokemon_names = AssertionUtils.validate_jsonpath(fire_types, 'pokemon..pokemon.name')

    # convert actual pokemons list to be same type of expected list {name: weight}
    actual_pokemon_weights = [{name: value} for name, value in
                              zip([pokemon_name for pokemon_name in fire_pokemon_names],
                                  [PokemonRequests.get_pokemon(p).get('weight') for p in fire_pokemon_names])]
    # sort by the value of weight and go the top 5 items from the beginning
    actual_top_5_pokemon_weights = list(
        sorted(actual_pokemon_weights, key=lambda p: list(p.values())[0], reverse=True))[:5]

    # top 5 with biggest weight pokimons should equal the expected object.
    AssertionUtils.assert_equal(expected_pokemon_weights, actual_top_5_pokemon_weights, 'top 5 pokemon weights')
