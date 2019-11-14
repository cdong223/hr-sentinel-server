import pytest
from datetime import datetime


@pytest.mark.parametrize("index, dt, expected", [
                (0, datetime(2019, 11, 11, 9, 35, 15, 176049), 100),
                (0, datetime(2020, 11, 11, 9, 35, 15, 176049), False),
                (1, datetime(2018, 9, 10, 10, 12, 13, 123456), False),
                (1, datetime(2018, 10, 11, 9, 44, 37, 901441), False),
                (2, datetime(2017, 10, 11, 9, 44, 37, 901441), 117),
                (2, datetime(2018, 11, 10, 9, 44, 37, 901441), 115),
                (3, datetime(2017, 8, 11, 9, 20, 12, 601231), 65),
                (3, datetime(2019, 11, 11, 9, 35, 15, 176049), 67),
                (3, datetime(2019, 11, 12, 12, 42, 27, 201431), 70),
                (3, datetime(2020, 9, 8, 1, 32, 12, 183748), False)
])
def test_find_avg_since(index, dt, expected):
    """Unit test for the find_avg_since() function in my_server.py

    Args:
        index (int): index of patient to be located in list
        dt (datetime): datetime to be compared to
        expected (int/boolean): average heart rate if measurements available;
                                False otherwise

    Returns:
        None
    """
    from my_server import find_avg_since
    p1 = {
        "patient_id": 4,
        "attending_email": "p1@email.com",
        "patient_age": 50,
        "heart_rate": [100],
        "status": "not tachycardic",
        "time_stamp": [datetime(2019, 11, 11, 9, 35, 15,
                                176049).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }
    p2 = {
        "patient_id": 103,
        "attending_email": "p2@email.com",
        "patient_age": 12,
        "heart_rate": [],
        "status": None,
        "time_stamp": []
        }
    p3 = {
        "patient_id": 82,
        "attending_email": "p3@email.com",
        "patient_age": 4,
        "heart_rate": [120, 115],
        "status": "not tachycardic",
        "time_stamp": [datetime(2018, 10, 11, 9, 44, 37,
                                901441).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2019, 11, 11, 11, 44, 37,
                                701431).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }
    p4 = {
        "patient_id": 19,
        "attending_email": "p4@email.com",
        "patient_age": 23,
        "heart_rate": [60, 65, 70],
        "status": "not tachycardic",
        "time_stamp": [datetime(2018, 8, 11, 9, 20,
                                12, 601231).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2019, 11, 11, 9, 35,
                                15, 176049).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2019, 11, 12, 12, 42, 27,
                                201431).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }

    patients = [p1, p2, p3, p4]
    result = find_avg_since(index, dt, patients)
    assert result == expected
