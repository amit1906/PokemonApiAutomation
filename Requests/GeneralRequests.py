import requests
from Utils.AssertionUtils import AssertionUtils


def request_and_validate_response(method, url, expected_status_code):
    print(f'Sending get_type request to: {url}')
    res = requests.request(method, url)
    AssertionUtils.assert_equal(expected_status_code, res.status_code, 'status_code')
    AssertionUtils.assert_equal('application/json; charset=utf-8', res.headers.get('Content-Type'), 'application/json')
    res_json = res.json()
    if not res_json:
        print('Response is empty.')
        assert res_json
    return res_json
