import pytest
from datetime import datetime


@pytest.mark.parametrize("index, heart_rate, timestamp, expected", [
                        (0, 99, datetime.now(), "not tachycardic"),
                        (0, 101, datetime.now(), "p1@email.com"),
                        (0, 87, datetime.now(), "not tachycardic"),
                        (1, 119, datetime.now(), "not tachycardic"),
                        (1, 100, datetime.now(), "not tachycardic"),
                        (1, 120, datetime.now(), "p2@email.com"),
                        (2, 120, datetime.now(), "not tachycardic"),
                        (2, 130, datetime.now(), "not tachycardic"),
                        (2, 138, datetime.now(), "p3@email.com"),
                        (2, 145, datetime.now(), "p3@email.com"),
])
def test_add_HR_data(index, heart_rate, timestamp, expected):
    """Unit test for the add_HR_data() function in my_server.py

    Args:
        index (int): index of patient to be located in list
        heart_rate (int): heart rate to be recorded for specified patient
        expected (str): attending email of patient if tachycardic;
                                "not tachycardic" otherwise

    Returns:
        None
    """
    from my_server import add_HR_data
    p1 = {
        "patient_id": 4,
        "attending_email": "p1@email.com",
        "patient_age": 50,
        "heart_rate": [100],
        "status": None,
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
        "status": None,
        "time_stamp": [datetime(2018, 10, 11, 9, 44, 37, 901441),
                       datetime(2019, 11, 11, 11, 44, 37, 701431)]
        }

    patients = [p1, p2, p3]
    result = add_HR_data(index, heart_rate, timestamp, patients)
    assert result == expected
