class AssertionUtils:

    @staticmethod
    def assert_equal(expected, actual, name):
        if actual == expected:
            print(f"Detected '{name}': {actual} - as expected.")
        else:
            print(f"Detected '{name}': {actual}\nExpected {name}: {expected} - failed.")
        assert expected == actual
