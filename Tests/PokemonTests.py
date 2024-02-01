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
