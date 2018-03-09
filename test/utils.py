async def async_coro(response):
    return response


class MockValidator(object):

    def __init__(self, validator):
        # validator is a function that takes a single argument and returns a bool.
        self.validator = validator

    def __eq__(self, other):
        return bool(self.validator(other))


def call_name(call_name: str):
    def test_coro(coro):
        return coro.cr_code.co_name == call_name

    return MockValidator(test_coro)