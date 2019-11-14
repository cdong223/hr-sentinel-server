import pytest
from datetime import datetime


@pytest.mark.parametrize("index, expected", [
                (0, [100]),
                (1, False),
                (2, [120, 115]),
                (3, [120, 134]),
                (4, [110]),
                (5, [60, 65, 70]),
                (6, [100, 120, 131]),
                (7, False),
                (8, False),
                (9, [100, 99])
])
def test_get_list(index, expected):
    """Unit test for the get_list() function in my_server.py

    Args:
        index (int): index of patient to be located in list
        expected (list/boolean): if data available, list of heart rates;
                                 False otherwise

    Returns:
        None
    """
    from my_server import get_list
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
        "patient_id": 1,
        "attending_email": "p4@email.com",
        "patient_age": 7,
        "heart_rate": [120, 134],
        "status": "tachycardic",
        "time_stamp": [datetime(2018, 8, 11, 9, 20, 12,
                                601231).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2019, 11, 12, 12, 42, 27,
                                201431).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }
    p5 = {
        "patient_id": 25,
        "attending_email": "p5@email.com",
        "patient_age": 98,
        "heart_rate": [110],
        "status": "tachycardic",
        "time_stamp": [datetime(2019, 11, 11, 9, 35, 15,
                                176049).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }
    p6 = {
        "patient_id": 19,
        "attending_email": "p6@email.com",
        "patient_age": 23,
        "heart_rate": [60, 65, 70],
        "status": "not tachycardic",
        "time_stamp": [datetime(2018, 8, 11, 9, 20, 12,
                                601231).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2019, 11, 11, 9, 35, 15,
                                176049).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2019, 11, 12, 12, 42, 27,
                                201431).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }
    p7 = {
        "patient_id": 22,
        "attending_email": "p7@email.com",
        "patient_age": 8,
        "heart_rate": [100, 120, 131],
        "status": "tachycardic",
        "time_stamp": [datetime(2018, 8, 11, 9, 20, 12,
                                601231).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2019, 11, 11, 9, 35, 15,
                                176049).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2019, 11, 12, 12, 42, 27,
                                201431).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }
    p8 = {
        "patient_id": 100,
        "attending_email": "p8@email.com",
        "patient_age": 2,
        "heart_rate": [],
        "status": None,
        "time_stamp": []
        }
    p9 = {
        "patient_id": 41,
        "attending_email": "p9@email.com",
        "patient_age": 88,
        "heart_rate": [],
        "status": None,
        "time_stamp": []
        }
    p10 = {
        "patient_id": 32,
        "attending_email": "p4@email.com",
        "patient_age": 32,
        "heart_rate": [100, 99],
        "status": "not tachycardic",
        "time_stamp": [datetime(2018, 8, 11, 9, 20, 12,
                                601231).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2019, 11, 12, 12, 42, 27,
                                201431).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }

    patients = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    result = get_list(index, patients)
    assert result == expected
