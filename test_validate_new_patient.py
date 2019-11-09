import pytest


@pytest.mark.parametrize("in_data, expected", [
                                ({"patient_id": 1,
                                  "attending_email": "p1@yourdomain.com",
                                  "patient_age": 3,
                                  }, True),
                                ({"pxatient_id": 1,
                                  "attending_email": "p1@yourdomain.com",
                                  "patient_age": 3,
                                  }, False),
                                ({"patient_id": 1,
                                  "sattending_email": "p1@yourdomain.com",
                                  "patient_age": 3,
                                  }, False),
                                ({"patient_id": 1,
                                  "attending_email": "p1@yourdomain.com",
                                  "2234patient_age": 3,
                                  }, False),
                                ({"patient_id": "1",
                                  "attending_email": "p1@yourdomain.com",
                                  "patient_age": 3,
                                  }, True),
                                ({"patientid": 1,
                                  "attendingemail": "p1@yourdomain.com",
                                  "patientage": 3,
                                  }, False),
                                ({"id": 1,
                                  "email": "p1@yourdomain.com",
                                  "age": 3,
                                  }, False),
                                ({"patient_id1": 1,
                                  "attending_email": "p1@yourdomain.com",
                                  "patient_age": 3,
                                  }, False),
                                ({"patient_id": 1,
                                  "attending_email": "email",
                                  "patient_age": "3",
                                  }, True),
                                ({"patient_id": 1,
                                  "attending_email": "p1@yourdomain.com",
                                  "patient__age": 3,
                                  }, False),
])
def test_validate_new_patient(in_data, expected):
    """Unit test for the validate_new_patient() function in my_server.py

    Args:
        in_data (dictionary): dictionary received from POST request
        expected (boolean): if dictionary contains right keys

    Returns:
        None
    """
    from my_server import validate_new_patient
    result = validate_new_patient(in_data)
    assert result == expected
