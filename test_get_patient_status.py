import pytest
from datetime import datetime


@pytest.mark.parametrize("index, expected", [
                (0, {"heart_rate": 100,
                     "status": "not tachycardic",
                     "timestamp": datetime(2019, 11, 11, 9, 35, 15, 176049)}),
                (1, False),
                (2, {"heart_rate": 115,
                     "status": "not tachycardic",
                     "timestamp": datetime(2019, 11, 11, 11, 44, 37, 701431)}),
                (3, {"heart_rate": 134,
                     "status": "tachycardic",
                     "timestamp": datetime(2019, 11, 12, 12, 42, 27, 201431)}),
                (4, {"heart_rate": 110,
                     "status": "tachycardic",
                     "timestamp": datetime(2019, 11, 11, 9, 35, 15, 176049)}),
                (5, {"heart_rate": 70,
                     "status": "not tachycardic",
                     "timestamp": datetime(2019, 11, 12, 12, 42, 27, 201431)}),
                (6, {"heart_rate": 131,
                     "status": "tachycardic",
                     "timestamp": datetime(2019, 11, 12, 12, 42, 27, 201431)}),
                (7, False),
                (8, False),
                (9, {"heart_rate": 99,
                     "status": "not tachycardic",
                     "timestamp": datetime(2019, 11, 12, 12, 42, 27, 201431)})
])
def get_patient_status(index, expected):
    """Unit test for the get_patient_status() function in my_server.py

    Args:
        index (int): index of patient to be located in list
        expected (dictionary/boolean): if data available, contains HR, status,
                                       and time stamp; False otherwise

    Returns:
        None
    """
    from my_server import get_patient_status
    p1 = {
        "patient_id": 4,
        "attending_email": "p1@email.com",
        "patient_age": 50,
        "heart_rate": [100],
        "status": "not tachycardic",
        "time_stamp": [datetime(2019, 11, 11, 9, 35, 15, 176049)]
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
        "time_stamp": [datetime(2018, 10, 11, 9, 44, 37, 901441),
                       datetime(2019, 11, 11, 11, 44, 37, 701431)]
        }
    p4 = {
        "patient_id": 1,
        "attending_email": "p4@email.com",
        "patient_age": 7,
        "heart_rate": [120, 134],
        "status": "tachycardic",
        "time_stamp": [datetime(2018, 8, 11, 9, 20, 12, 601231),
                       datetime(2019, 11, 12, 12, 42, 27, 201431)]
        }
    p5 = {
        "patient_id": 25,
        "attending_email": "p5@email.com",
        "patient_age": 98,
        "heart_rate": [110],
        "status": "tachycardic",
        "time_stamp": [datetime(2019, 11, 11, 9, 35, 15, 176049)]
        }
    p6 = {
        "patient_id": 19,
        "attending_email": "p6@email.com",
        "patient_age": 23,
        "heart_rate": [60, 65, 70],
        "status": "not tachycardic",
        "time_stamp": [datetime(2018, 8, 11, 9, 20, 12, 601231),
                       datetime(2019, 11, 11, 9, 35, 15, 176049),
                       datetime(2019, 11, 12, 12, 42, 27, 201431)]
        }
    p7 = {
        "patient_id": 22,
        "attending_email": "p7@email.com",
        "patient_age": 8,
        "heart_rate": [100, 120, 131],
        "status": "tachycardic",
        "time_stamp": [datetime(2018, 8, 11, 9, 20, 12, 601231),
                       datetime(2019, 11, 11, 9, 35, 15, 176049),
                       datetime(2019, 11, 12, 12, 42, 27, 201431)]
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
        "time_stamp": [datetime(2018, 8, 11, 9, 20, 12, 601231),
                       datetime(2019, 11, 12, 12, 42, 27, 201431)]
        }

    patients = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    result = get_patient_status(index, patients)
    assert result == expected
