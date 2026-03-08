import requests
import logging

logging.basicConfig(level=logging.INFO)

url = "https://api.sheety.co/2a738664cb10b9ea4971b2ff1892cbd3/flightDealData/sheet1"

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