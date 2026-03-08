import requests
import logging

logging.basicConfig(
    level=logging.INFO,
)

sheets_data = requests.get(url=f"https://api.sheety.co/2a738664cb10b9ea4971b2ff1892cbd3/flightDealData/sheet1")
sheets_data_list = []
sheets_data_json = sheets_data.json()
print("\nSheets Data:")
for data in sheets_data_json['sheet1']:
    try:
        if len(data.keys()) > 2:
            sheets_data_list.append({
                'destination_code' : data['destinationCode'],
                'departure_code' : data['departureCode'],
                'price_target' : int(data['priceTarget']),
                'duration_target' : int(data['durationTarget']),
                'layover_count' : data['layoverCount'],
                'user_email' : data['emailAddress']
            }
            )
            logging.info(
            f"destination_code {data['destinationCode']} | "
            f"departure_code {data['departureCode']} | "
            f"price_target {int(data['priceTarget'])} | "
            f"duration_target {int(data['durationTarget'])} | "
            f"layover_count {data['layoverCount']} | "
            f"user_email {data['emailAddress']}"
            ) 
        pass
    except KeyError as e:
        print(f"Error detected for route: {data['destinationCode']}-{data['departureCode']}: [{e}]")
