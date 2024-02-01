import ApiConfig
from Requests import GeneralRequests


def get_type():
    return GeneralRequests.request_and_validate_response('get', ApiConfig.GET_TYPE, 200)
