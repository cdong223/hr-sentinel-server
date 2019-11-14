import pytest
from datetime import datetime


@pytest.mark.parametrize("timestamp, expected", [
    ('2019-11-13 22:51:42.712118', datetime(2019, 11, 13, 22, 51, 42, 712118)),
    ('2019-11-13 22:51:42', False),
    ('2019-11-13 22:51:712118', False),
    ('2019-11-13 22:51', False),
    ('2019-11-13 22', False),
    ('2019-11-13', False),
    ('2005-03-08 11:32:49.129361', datetime(2005, 3, 8, 11, 32, 49, 129361)),
    ('hi', False),
    ('22:51:42.712118', False),
    ('2019-18-13 22:51:42.712118', False)
])
def test_validate_timestamp(timestamp, expected):
    """Unit test for the validate_timestamp() function in my_server.py

    Args:
        timestamp (str): datetime string
        expected (datetime or boolean): datetime if correct format;
                                        False otherwise

    Returns:
        None
    """
    from my_server import validate_timestamp
    result = validate_timestamp(timestamp)
    assert result == expected
