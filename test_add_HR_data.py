import pytest
from datetime import datetime


@pytest.mark.parametrize("index, heart_rate, timestamp, expected", [
    (0, 99, datetime(2019, 11, 11, 9, 35, 15,
                     176049).strftime('%Y-%m-%d %H:%M:%S.%f'),
     ["not tachycardic",
      {
          "patient_id": 4,
          "attending_email": "p1@email.com",
          "patient_age": 50,
          "heart_rate": [100, 99],
          "status": "not tachycardic",
          "time_stamp": [datetime(2016, 11, 11, 9, 35,
                                  15, 176049).strftime('%Y-%m-%d %H:%M:%S.%f'),
                         datetime(2019, 11, 11, 9, 35, 15,
                                  176049).strftime('%Y-%m-%d %H:%M:%S.%f')]
          }]),
    (0, 101, datetime(2020, 11, 11, 9, 35, 15,
                      176049).strftime('%Y-%m-%d %H:%M:%S.%f'),
     ["p1@email.com",
      {
          "patient_id": 4,
          "attending_email": "p1@email.com",
          "patient_age": 50,
          "heart_rate": [100, 101],
          "status": "tachycardic",
          "time_stamp": [datetime(2016, 11, 11, 9, 35,
                                  15, 176049).strftime('%Y-%m-%d %H:%M:%S.%f'),
                         datetime(2020, 11, 11, 9, 35, 15,
                                  176049).strftime('%Y-%m-%d %H:%M:%S.%f')]
          }]),
    (0, 87, datetime(2018, 9, 10, 10, 12, 13,
                     123456).strftime('%Y-%m-%d %H:%M:%S.%f'),
     ["not tachycardic",
      {
          "patient_id": 4,
          "attending_email": "p1@email.com",
          "patient_age": 50,
          "heart_rate": [100, 87],
          "status": "not tachycardic",
          "time_stamp": [datetime(2016, 11, 11, 9, 35,
                                  15, 176049).strftime('%Y-%m-%d %H:%M:%S.%f'),
                         datetime(2018, 9, 10, 10, 12, 13,
                                  123456).strftime('%Y-%m-%d %H:%M:%S.%f')]
          }]),
    (1, 119, datetime(2018, 10, 11, 9, 44, 37,
                      901441).strftime('%Y-%m-%d %H:%M:%S.%f'),
     ["not tachycardic",
      {
        "patient_id": 103,
        "attending_email": "p2@email.com",
        "patient_age": 12,
        "heart_rate": [119],
        "status": "not tachycardic",
        "time_stamp": [datetime(2018, 10, 11, 9, 44, 37,
                                901441).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }]),
    (1, 100, datetime(2017, 10, 11, 9, 44, 37,
                      901441).strftime('%Y-%m-%d %H:%M:%S.%f'),
     ["not tachycardic",
      {
        "patient_id": 103,
        "attending_email": "p2@email.com",
        "patient_age": 12,
        "heart_rate": [100],
        "status": "not tachycardic",
        "time_stamp": [datetime(2017, 10, 11, 9, 44, 37,
                                901441).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }]),
    (1, 120, datetime(2018, 11, 10, 9, 44, 37,
                      901441).strftime('%Y-%m-%d %H:%M:%S.%f'),
     ["p2@email.com",
      {
        "patient_id": 103,
        "attending_email": "p2@email.com",
        "patient_age": 12,
        "heart_rate": [120],
        "status": "tachycardic",
        "time_stamp": [datetime(2018, 11, 10, 9, 44, 37,
                                901441).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }]),
    (2, 120, datetime(2017, 8, 11, 9, 20, 12,
                      601231).strftime('%Y-%m-%d %H:%M:%S.%f'),
     ["not tachycardic",
      {
        "patient_id": 82,
        "attending_email": "p3@email.com",
        "patient_age": 4,
        "heart_rate": [120, 115, 120],
        "status": "not tachycardic",
        "time_stamp": [datetime(2016, 10, 11, 9, 44,
                                37, 901441).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2016, 11, 11, 11, 44,
                                37, 701431).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2017, 8, 11, 9, 20, 12,
                                601231).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }]),
    (2, 130, datetime(2019, 11, 11, 9, 35, 15,
                      176049).strftime('%Y-%m-%d %H:%M:%S.%f'),
     ["not tachycardic",
      {
        "patient_id": 82,
        "attending_email": "p3@email.com",
        "patient_age": 4,
        "heart_rate": [120, 115, 130],
        "status": "not tachycardic",
        "time_stamp": [datetime(2016, 10, 11, 9, 44,
                                37, 901441).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2016, 11, 11, 11, 44,
                                37, 701431).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2019, 11, 11, 9, 35, 15,
                                176049).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }]),
    (2, 138, datetime(2019, 11, 12, 12, 42, 27,
                      201431).strftime('%Y-%m-%d %H:%M:%S.%f'),
     ["p3@email.com",
      {
        "patient_id": 82,
        "attending_email": "p3@email.com",
        "patient_age": 4,
        "heart_rate": [120, 115, 138],
        "status": "tachycardic",
        "time_stamp": [datetime(2016, 10, 11, 9, 44,
                                37, 901441).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2016, 11, 11, 11, 44,
                                37, 701431).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2019, 11, 12, 12, 42, 27,
                                201431).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }]),
    (2, 145, datetime(2020, 9, 8, 1, 32, 12,
                      183748).strftime('%Y-%m-%d %H:%M:%S.%f'),
     ["p3@email.com",
      {
        "patient_id": 82,
        "attending_email": "p3@email.com",
        "patient_age": 4,
        "heart_rate": [120, 115, 145],
        "status": "tachycardic",
        "time_stamp": [datetime(2016, 10, 11, 9, 44,
                                37, 901441).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2016, 11, 11, 11, 44,
                                37, 701431).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2020, 9, 8, 1, 32, 12,
                                183748).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }])
])
def test_add_HR_data(index, heart_rate, timestamp, expected):
    """Unit test for the add_HR_data() function in my_server.py

    Args:
        index (int): index of patient to be located in list
        heart_rate (int): heart rate to be recorded for specified patient
        timestamp (str): date/time stamp associated with post request
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
        "time_stamp": [datetime(2016, 11, 11, 9, 35,
                                15, 176049).strftime('%Y-%m-%d %H:%M:%S.%f')]
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
        "time_stamp": [datetime(2016, 10, 11, 9, 44,
                                37, 901441).strftime('%Y-%m-%d %H:%M:%S.%f'),
                       datetime(2016, 11, 11, 11, 44,
                                37, 701431).strftime('%Y-%m-%d %H:%M:%S.%f')]
        }

    patients = [p1, p2, p3]
    result = [add_HR_data(index, heart_rate, timestamp, patients),
              patients[index]]
    assert result == expected
