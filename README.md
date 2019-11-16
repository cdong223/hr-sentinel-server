# Heart Rate Sentinel Server

[![Build Status](https://travis-ci.com/bme547-fall2019/hr-sentinel-server-cdong223.svg?token=o3TBsFei64u2Cyoxf93i&branch=master)](https://travis-ci.com/bme547-fall2019/hr-sentinel-server-cdong223)

## Description
The purpose of this program is to act as a centralized server for storing heart rate data for a list of mock patients who have checked out heart rate monitors. The server is built to accommodate GET and POST requests relating to the data stored within, including patient ID, patient age, the email of the attending physician, a list of posted heart rate measurements, current heart condition (i.e. tachycardic vs. not tachycardic), and a list of posted date/time stamps associated with the heart rate measurements. All requests return with either the requested information or a confirmation message, in the form of a JSON, along with an appropriate status code.

## Instructions for Use
First create an appropriate virtual environment within which Python's `requests` library is installed. Subsequently, write a client program that uses the `requests` library to generate POST and GET requests to a server at `http://vcm-11703.vm.duke.edu:5000`. For syntax help, refer to `vm_client.py` included within the project repository: https://github.com/bme547-fall2019/hr-sentinel-server-cdong223. The server provides the following routes:

- `POST http://vcm-11703.vm.duke.edu:5000/api/new_patient`
allows registration of a new patient on server and is configured to allow input of future heart rate measurements for the patient. It takes a JSON in the format as follows:
```
{
    "patient_id": "1",  # must be numeric (int or str)
    "attending_email": "dr_user_id@yourdomain.com",
    "patient_age": 50,  # in years
}
```
- `POST http://vcm-11703.vm.duke.edu:5000/api/heart_rate`
stores new heart rate measurements for a specified patient and sends an email to the patient's attending physician if the most recent heart rate is categorized as tachycardic. The date/time stamp of the POST request is recorded along with the measurement. It takes a JSON in the format as follows:
```
{
  "patient_id": 1,  # must be numeric (int or str)
  "heart_rate": 100  # must be numeric (int or str)
}
```
- `GET http://vcm-11703.vm.duke.edu:5000/api/status/<patient_id>`
retrieves and returns a JSON containing the latest heart rate, whether the patient is tachycardic based on this heart rate, and the date/time stamp associated with the measurement for the patient specified. The return JSON will appear in the format as follows:
```
{
    "heart_rate": 100,
    "status":  "tachycardic" | "not tachycardic",
    "timestamp": "2018-03-09 11:00:36.372339"  
}
```
- `GET http://vcm-11703.vm.duke.edu:5000/api/heart_rate/<patient_id>`
retrieves and returns, in JSON format, a list of all the previous heart rate measurements for the specified patient.
- `GET http://vcm-11703.vm.duke.edu:5000/api/heart_rate/average/<patient_id>`
retrieves and returns, in JSON format, an integer representing the average of all previous heart rate measurements for the specified patient.  
- `POST http://vcm-11703.vm.duke.edu:5000/api/heart_rate/interval_average`
takes a JSON input containing the patient ID and a specified date/time stamp and returns, as an integer in JSON format, the average of all heart rate measurements since that specified date/time stamp for the particular patient. The date/time specified does not have to be the date/time stamp of a previous heart rate. The input JSON should be of the format as follows:
```
{
    "patient_id": "1",
    "heart_rate_average_since": "2018-03-09 11:00:36.372339" // date string
}
```

In addition to the POST and GET requests, the program generates a logging file, called `sequence.log`, which details certain information related to the program, including:

- `INFO`: when a new patient is registered on the server
- `INFO`: when a heart rate is posted for a patient is found to be tachycardic and an email is sent to the patient's attending physician

## Definition of Tachycardic
Whether a resting heart rate is considered tachycardic is based on the associated patient's age. The typical cutoffs are as follows:
- 1–2 years: Tachycardia > 151 bpm
- 3–4 years: Tachycardia > 137 bpm
- 5–7 years: Tachycardia > 133 bpm
- 8–11 years: Tachycardia > 130 bpm
- 12–15 years: Tachycardia > 119 bpm
- Older than 15 years: Tachycardia > 100 bpm

Source: https://en.wikipedia.org/wiki/Tachycardia

## License
MIT License

Copyright (c) 2019 Claire Dong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
