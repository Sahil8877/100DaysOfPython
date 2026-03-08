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
            "departure_id": target['departure_code'],
            "arrival_id": target['destination_code'],
            "outbound_date": search_date,
            "currency": "GBP",
            "hl": "en", #language
            "gl": 'uk', #country
            "api_key": os.getenv('SERP_API_KEY'),
            'type' : "2", #one_way_trip
            'stops' : int(target['layover_count']),
            }
            search = GoogleSearch(params)
            result = search.get_dict()
            best_flights.append(result)
        except:
            print("There was an error :",search.get_response())

    return best_flights

search_result()


