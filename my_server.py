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


def is_tachycardic(heart_rate, patient_age):  # Test
    """Checks to see if heart rate is tachycardic considering age

    Args:
        heart_rate (int): heart rate of specified patient
        patient_age (int): age of specified patient

    Returns:
        str: tachycardic or not tachycardic
    """
    if 1 <= patient_age <= 2:
        threshold = 151
    elif 3 <= patient_age <= 4:
        threshold = 137
    elif 5 <= patient_age <= 7:
        threshold = 133
    elif 8 <= patient_age <= 11:
        threshold = 130
    elif 12 <= patient_age <= 15:
        threshold = 119
    else:
        threshold = 100
    if heart_rate > threshold:
        return "tachycardic"
    else:
        return "not tachycardic"


def add_HR_data(index, heart_rate):
    patient = patients[index]
    patient["heart_rate"].append(heart_rate)
    status = is_tachycardic(heart_rate, patient["patient_age"])
    patient["status"] = status
    timestamp = datetime.now()
    patient["time_stamp"] = timestamp
    if status == "tachycardic":
        email = patient["attending_email"]
        patient_id = patient["patient_id"]
        logging.info("Tachycardic: ID: {}, HR: {}, Attending email: {}".format(
                     patient_id, heart_rate, email))
        return jsonify("{}: {} has a HR of {} at {}".format(email, patient_id,
                                                            heart_rate,
                                                            timestamp))
    else:
        return jsonify("not tachycardic")


def find_patient(patient_id, patients):
    """Retrieves the index corresponding to a specified patient

    Args:
        patient_id (int): ID of patient to be located in list

    Returns:
        Boolean or int: Index corresponding to patient in list;
                        False if patient is not in list
    """
    for i in range(len(patients)):
        if patients[i]["patient_id"] == patient_id:
            return i
    return False


def validate_HR_data(in_data):  # test
    """Validates input to add_heart_rate for correct fields

    Args:
        in_data: dictionary received from POST request

    Returns:
        boolean: if in_data contains the correct fields
    """
    expected_keys = {"patient_id", "heart_rate"}
    for key in in_data.keys():
        if key not in expected_keys:
            return False
    return True


@app.route("/api/heart_rate", methods=["POST"])
def add_heart_rate():
    """Stores the sent heart rate measurement in the record for the specified
       patient along when the date/time stamp. Sends an email to the associated
       attending email if the heart rate is found to be tachycardic.

    Args:
        None

    Returns:
        JSON: either email for "not tachycardic"
    """
    in_data = request.get_json()
    good_info = validate_HR_data(in_data)
    if good_info is False:
        return jsonify("ERROR: Invalid keys."), 400

    patient_id_input = in_data["patient_id"]  # integer or numeric string
    patient_id = validate_numeric(patient_id_input)
    if patient_id is False:
        return jsonify("ERROR: ID must be a number."), 400

    heart_rate_input = in_data["heart_rate"]  # integer or numeric string
    heart_rate = validate_numeric(heart_rate_input)
    if heart_rate is False:
        return jsonify("ERROR: Heart rate must be a number."), 400

    index = find_patient(patient_id, patients)
    if index is False:
        return jsonify("ERROR: patient not on file, address invalid"), 404

    return add_HR_data(index, heart_rate)


if __name__ == "__main__":
    logging.basicConfig(filename="sequence.log", level=logging.DEBUG,
                        filemode="w")
    app.run()
