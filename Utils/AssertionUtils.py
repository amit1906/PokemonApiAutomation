from jsonpath import jsonpath


class AssertionUtils:

    @staticmethod
    def assert_equal(expected, actual, name):
        if actual == expected:
            print(f"Detected '{name}': {actual} - as expected.")
        else:
            print(f"Detected '{name}': {actual}\nExpected {name}: {expected} - failed.")
        assert expected == actual

    @staticmethod
    def validate_jsonpath(body, expr):
        res = jsonpath(body, expr)
        if not res:
            print(f"Field '{expr}' not found in response body.")
            assert res
        return res

    @staticmethod
    def validate_is_a_list(expected_list, name):
        if type(expected_list) is not list or len(expected_list) == 0:
            print(f'Expected list of {name}s is invalid.')
            assert type(expected_list) is expected_list or len(expected_list) > 0

    @staticmethod
    def validate_in_list(value, expected_list, name):
        AssertionUtils.validate_is_a_list(expected_list, name)
        if value not in expected_list:
            print(f"Expected '{name}': {value} should be in in the list.")
            assert value in expected_list
        print(f"Expected '{name}': {value} is in the list - as expected.")

    @staticmethod
    def validate_not_in_list(value, expected_list, name):
        AssertionUtils.validate_is_a_list(expected_list, name)
        if value in expected_list:
            print(f"Expected '{name}': {value} shouldn't be in the list.")
            assert value not in expected_list
        print(f"Expected '{name}': {value} is not in the list - as expected.")

