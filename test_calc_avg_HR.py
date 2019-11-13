import pytest


@pytest.mark.parametrize("list, expected", [
                                ([110, 113, 90], 104),
                                ([84], 84),
                                ([95, 94], 94),
                                ([61, 51], 56),
                                ([114, 94, 130, 123], 115),
                                ([94, 59], 76),
                                ([98], 98),
                                ([66, 47], 56),
                                ([90, 91, 92, 93], 91),
                                ([80, 80, 80], 80)
])
def test_calc_avg_HR(list, expected):
    """Unit test for the calc_avg_HR() function in my_server.py

    Args:
        list (int): list of previous heart rates
        expected (int): average heart rate

    Returns:
        None
    """
    from my_server import calc_avg_HR
    result = calc_avg_HR(list)
    assert result == expected
