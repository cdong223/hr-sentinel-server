import requests


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
    print(a1)
    print(r1.status_code)
    print(a2)
    print(r2.status_code)
    print(a3)
    print(r3.status_code)


if __name__ == "__main__":
    add_patient()
