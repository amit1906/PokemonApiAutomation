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
