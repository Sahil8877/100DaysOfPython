import os
import sheets_data
import datetime
from serpapi import GoogleSearch
from dotenv import load_dotenv
load_dotenv()

flight_list = sheets_data.sheets_data_list

def search_result():
    best_flights = []
    search_date = datetime.datetime.now().date() + datetime.timedelta(days=90)

    for target in flight_list:
        try:
            params = {
                "engine": "google_flights",
                "departure_id": target["departure_code"],
                "arrival_id": target["destination_code"],
                "outbound_date": search_date.strftime("%Y-%m-%d"),
                "currency": "GBP",
                "hl": "en",
                "gl": "uk",
                "api_key": os.getenv("SERP_API_KEY"),
                "type": "2"
            }

            search = GoogleSearch(params)
            result = search.get_dict()

            result = search.get_dict()
            # print("SERP RESULT:", result)
            best_flights.append(result)

        except Exception as e:
            print("Error:", e)

    return best_flights


