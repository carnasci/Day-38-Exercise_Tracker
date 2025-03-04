import requests
from credentials import app_id, app_key

APP_ID = app_id
APP_KEY = app_key
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
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

response = requests.post(url=API_ENDPOINT, json=json_params, headers=headers)
print(response.text)