import requests


def check_patients_list():
    r = requests.get("http://127.0.0.1:5000/patients")
    a = r.json()
    print(a)


def check_HR_list():
    r1 = requests.get("http://127.0.0.1:5000/api/heart_rate/1")
    r2 = requests.get("http://127.0.0.1:5000/api/heart_rate/2")
    r3 = requests.get("http://127.0.0.1:5000/api/heart_rate/3")
    print(r1.json())
    print(r1.status_code)
    print(r2.json())
    print(r2.status_code)
    print(r3.json())
    print(r3.status_code)


def check_status():
    r1 = requests.get("http://127.0.0.1:5000/api/status/1")
    r2 = requests.get("http://127.0.0.1:5000/api/status/2")
    r3 = requests.get("http://127.0.0.1:5000/api/status/3")
    # print(r1.json())
    # print(r1.status_code)
    # print(r2.json())
    # print(r2.status_code)
    # print(r3.json())
    # print(r3.status_code)


def add_heart_rate():
    p1 = {
        "patient_id": 2,
        "heart_rate": "101"
        }
    p2 = {
        "patient_id": "3",
        "heart_rate": 60
        }
    p3 = {
        "patient_id": 2,
        "heart_rate": "90"
        }
    p4 = {
        "patient_id": 1,
        "heart_rate": "137"
        }
    r1 = requests.post("http://127.0.0.1:5000/api/heart_rate", json=p1)
    r2 = requests.post("http://127.0.0.1:5000/api/heart_rate", json=p2)
    r3 = requests.post("http://127.0.0.1:5000/api/heart_rate", json=p3)
    r4 = requests.post("http://127.0.0.1:5000/api/heart_rate", json=p4)
    # print(r1.json())
    # print(r1.status_code)
    # print(r2.json())
    # print(r2.status_code)
    # print(r3.json())
    # print(r3.status_code)
    # print(r4.json())
    # print(r4.status_code)


def add_patient():
    p1 = {
        "patient_id": 1,  # usually this would be the patient MRN
        "attending_email": "p1@yourdomain.com",
        "patient_age": 3,  # in years
        }
    p2 = {
        "patient_id": "2",  # usually this would be the patient MRN
        "attending_email": "p2@yourdomain.com",
        "patient_age": 50,  # in years
        }
    p3 = {
        "patient_id": "3",  # usually this would be the patient MRN
        "attending_email": "p3@yourdomain.com",
        "patient_age": "22",  # in years
        }
    r1 = requests.post("http://127.0.0.1:5000/api/new_patient", json=p1)
    r2 = requests.post("http://127.0.0.1:5000/api/new_patient", json=p2)
    r3 = requests.post("http://127.0.0.1:5000/api/new_patient", json=p3)
    a1 = r1.json()
    a2 = r2.json()
    a3 = r3.json()
    # print(a1)
    # print(r1.status_code)
    # print(a2)
    # print(r2.status_code)
    # print(a3)
    # print(r3.status_code)


if __name__ == "__main__":
    add_patient()
    add_heart_rate()
    # check_patients_list()
    # check_status()
    check_HR_list()
