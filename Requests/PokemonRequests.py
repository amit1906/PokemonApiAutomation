import ApiConfig
from Requests import GeneralRequests


def get_type(url=''):
    if not url:
        url = ApiConfig.GET_TYPE
    return GeneralRequests.request_and_validate_response('get', url, 200)
