from flask import Flask, jsonify, request
from datetime import datetime
import logging


app = Flask(__name__)
patients = []


def validate_numeric(input):  # test
    """Validates input to see if it's an int or integer numeric string

    Args:
        input: data corresponding to key in dictionary from POST request

    Returns:
        boolean: False if input cannot be cast as int
        int: value of input if castable as int
    """
    try:
        output = int(input)
    except ValueError:
        return False
    return output


def validate_new_patient(in_data):  # test
    """Validates input to add_new_patient for correct fields

    Args:
        in_data: dictionary received from POST request

    Returns:
        boolean: if in_data contains the correct fields
    """
    expected_keys = {"patient_id", "attending_email", "patient_age"}
    for key in in_data.keys():
        if key not in expected_keys:
            return False
    return True


@app.route("/api/new_patient", methods=["POST"])
def add_new_patient():
    """Registers new patient on server; configured to allow input of future
       heart rate measurements for the patient. Logs registration.

    Args:
        None

    Returns:
        JSON: dictionary with fields corresponding to relevant patient info
    """
    in_data = request.get_json()
    good_info = validate_new_patient(in_data)
    if good_info is False:
        return jsonify("ERROR: Invalid keys."), 400

    patient_id_input = in_data["patient_id"]  # integer or numeric string
    patient_id = validate_numeric(patient_id_input)
    if patient_id is False:
        return jsonify("ERROR: ID must be a number."), 400

    attending_email = in_data["attending_email"]  # "dr_user_id@yourdomain.com"

    patient_age_input = in_data["patient_age"]  # integer or numeric string
    patient_age = validate_numeric(patient_age_input)
    if patient_age is False:
        return jsonify("ERROR: Age must be a number."), 400

    return_dictionary = {
        "patient_id": patient_id,
        "attending_email": attending_email,
        "patient_age": patient_age,
        "heart_rate": [],
        "status": None,
        "time_stamp": []
        }
    patients.append(return_dictionary)
    logging.info("New patient registered, ID: {}".format(patient_id))
    return jsonify(return_dictionary)


if __name__ == "__main__":
    logging.basicConfig(filename="sequence.log", level=logging.DEBUG,
                        filemode="w")
    app.run()
