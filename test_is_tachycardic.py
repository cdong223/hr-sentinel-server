import pytest


@pytest.mark.parametrize("heart_rate, patient_age, expected", [
                                (97, 84, "not tachycardic"),
                                (112, 33, "tachycardic"),
                                (71, 7, "not tachycardic"),
                                (61, 51, "not tachycardic"),
                                (114, 94, "tachycardic"),
                                (94, 59, "not tachycardic"),
                                (98, 67, "not tachycardic"),
                                (66, 47, "not tachycardic"),
                                (140, 1, "not tachycardic"),
                                (126, 52, "tachycardic")
])
def test_is_tachycardic(heart_rate, patient_age, expected):
    """Unit test for the is_tachycardic() function in my_server.py

    Args:
        heart_rate (int): heart rate of specified patient
        patient_age (int): age of specified patient
        expected (str): tachycardic or not tachycardic

    Returns:
        None
    """
    from my_server import is_tachycardic
    result = is_tachycardic(heart_rate, patient_age)
    assert result == expected
