import pytest

list = [{"patient_id": 4},
        {"patient_id": 5},
        {"patient_id": 0},
        {"patient_id": 10},
        {"patient_id": 934},
        {"patient_id": 298},
        {"patient_id": 1000},
        {"patient_id": 1},
        {"patient_id": 439},
        {"patient_id": 99}]


@pytest.mark.parametrize("patient_id, expected", [
                                (10, 3),
                                (4, 0),
                                (99, 9),
                                (439, 8),
                                (6, False),
                                (1000, 6),
                                (2, False),
                                (152, False),
                                (934, 4),
                                (5, 1)
])
def find_patient(patient_id, expected):
    """Unit test for the find_patient() function in my_server.py

    Args:
        patient_id (int): ID of patient to be located in list
        expected (boolean or int): Index corresponding to patient in list;
                                   False if patient is not in list

    Returns:
        None
    """
    from my_server import find_patient
    result = find_patient(patient_id)
    assert result == expected
