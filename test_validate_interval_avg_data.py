import pytest


@pytest.mark.parametrize("in_data, expected", [
                                ({"patient_id": 1,
                                  "heart_rate_average_since": 100,
                                  }, True),
                                ({"pxatient_id": 1,
                                  "heart_rate_average_since": 100,
                                  }, False),
                                ({"patient_id": 1,
                                  "heart_rate_average_since": "100",
                                  }, True),
                                ({"patient_id": "1",
                                  "heart_rate_average_since": 100,
                                  }, True),
                                ({"patientid": "1",
                                  "heart_rate_average_since": 100,
                                  }, False),
                                ({"patient_id": 1,
                                  "heartrate_average_since": 100,
                                  }, False),
                                ({"id": 1,
                                  "heartrateaverage_since": 100,
                                  }, False),
                                ({"patient_id": 2,
                                  "heart_rate_average_since": 50,
                                  }, True),
                                ({"patient_id": 5,
                                  "heart_rate_average_since": 98,
                                  }, True),
                                ({"patient_id": 1,
                                  "heartrateaveragesince": 100,
                                  }, False)
])
def test_validate_interval_avg_data(in_data, expected):
    """Unit test for the validate_interval_avg_data() function in my_server.py

    Args:
        in_data (dictionary): dictionary received from POST request
        expected (boolean): if dictionary contains right keys

    Returns:
        None
    """
    from my_server import validate_interval_avg_data
    result = validate_interval_avg_data(in_data)
    assert result == expected
