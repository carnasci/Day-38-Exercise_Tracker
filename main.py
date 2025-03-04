import requests
import os
from datetime import datetime
from credentials import app_id, app_key, sheety_endpoint, sheety_auth


APP_ID = app_id
APP_KEY = app_key
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = sheety_endpoint
SHEETY_AUTH = sheety_auth

query = input("What exercises did you do today?: ")

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY,
}
json_params = {
    "query" : query,
    "weight_kg" : 92.5,
    "height_cm" : 185.4,
    "age" : 36,
}

today = datetime.now().strftime("%m/%d/%Y")
today_time = datetime.now().strftime("%H:%M:%S")
print(today_time)
print(today)
response = requests.post(url=API_ENDPOINT, json=json_params, headers=headers)
print(response.text)
data = response.json()

for exercise in data["exercises"]:
    sheety_inputs = {
        "workout" : {
            "date": today,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheety_header = {
    "Authorization" : SHEETY_AUTH,
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_inputs, headers=sheety_header)
print(sheety_response.text)