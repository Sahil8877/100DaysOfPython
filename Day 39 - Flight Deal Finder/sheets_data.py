import requests
import logging
import os
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)

url = os.getenv('SHEETS_URL_FLIGHT_DEAL')

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

print("Status:", response.status_code)

data_json = response.json()

sheets_data_list = []

for data in data_json["sheet1"]:
    if data.get("destinationCode"):
        sheets_data_list.append({
            "destination_code": data["destinationCode"],
            "departure_code": data["departureCode"],
            "price_target": int(data["priceTarget"]),
            "duration_target": int(data["durationTarget"]),
            "layover_count": data["layoverCount"],
            "user_email": data["emailAddress"]
        })