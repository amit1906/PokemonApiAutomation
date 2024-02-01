import ApiConfig
from Requests import GeneralRequests


def get_type(type_id=''):
    return GeneralRequests.request_and_validate_response('get', ApiConfig.GET_TYPE + type_id, 200)
