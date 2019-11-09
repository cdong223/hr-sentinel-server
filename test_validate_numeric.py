import pytest


@pytest.mark.parametrize("input, expected", [
                          (1, 1),
                          ("1", 1),
                          ("two", False),
                          ("asdlfk1", False),
                          ("12312s", False),
                          (123, 123),
                          ("hi", False),
                          ("12a45", False),
                          (90, 90),
                          ("152", 152)
])
def test_validate_numeric(input, expected):
    """Unit test for the validate_numeric() function in my_server.py

    Args:
        input (int or str): data corresponding to key in dictionary from
                            POST request
        expected (boolean or int): False if non-numeric, int if castable as int

    Returns:
        None
    """
    from my_server import validate_numeric
    result = validate_numeric(input)
    assert result == expected
