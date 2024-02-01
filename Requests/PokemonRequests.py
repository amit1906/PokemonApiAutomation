import ApiConfig
from Requests import GeneralRequests
from Utils import StringUtils
from Utils.AssertionUtils import AssertionUtils


def get_type(type_id=''):
    return GeneralRequests.request_and_validate_response('get', ApiConfig.GET_TYPE + type_id, 200)


def get_pokemon(pokemon_id=''):
    return GeneralRequests.request_and_validate_response('get', ApiConfig.GET_POKEMON + pokemon_id, 200)


def get_pokemon_types(type_name):
    body = get_type()
    fire_url = AssertionUtils.validate_jsonpath(body, f'results[?(@.name=="{type_name}")].url')[0]
    type_id = StringUtils.get_url_id(fire_url)
    return get_type(type_id)
