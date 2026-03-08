import sheets_data
import flight_search
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:%(message)s"
)

logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)
print("\nData Logs:")

target_data = sheets_data.sheets_data_list

def flight_deal_checker():

    flight_deal = []
    best_flights_data = flight_search.search_result()

    for idx, targets in enumerate(target_data):
        if "best_flights" not in best_flights_data[idx]:
            print(f"No flights found for {targets['user_email']}")
        
        data = best_flights_data[idx].get("best_flights", [])

        for flight_options in data:

            segments = flight_options['flights']
            if 'layovers' not in flight_options:
                layover = "No"
            else:
                layover = targets['layover_count']

            logging.info(
            f"Requested | {targets['user_email']} | "
            f"{segments[0]['departure_airport']['id']}→{segments[-1]['arrival_airport']['id']} | "
            f"£{flight_options['price']} | "
            f"{flight_options['total_duration']}min | "
            f"{layover} stops"
            ) 

            if flight_options['price'] <= targets['price_target'] and flight_options['total_duration'] <= targets['duration_target']:
                departure = segments[0]['departure_airport']
                arrival = segments[-1]['arrival_airport']
                # print(flight_options)

                logging.debug(
                f"MATCHED | {targets['user_email']} | "
                f"{segments[0]['departure_airport']['id']}→{segments[-1]['arrival_airport']['id']} | "
                f"£{flight_options['price']} | "
                f"{flight_options['total_duration']}min | "
                f"{layover} stops"
                )   
                layovers = []

                for i in range(len(segments) - 1):
                    layovers.append({
                        "airport": segments[i]['arrival_airport']['name'],
                        "arrival_time": segments[i]['arrival_airport']['time'],
                        "departure_time": segments[i+1]['departure_airport']['time']
                    })

                flight_deal.append({
                    "departure": departure,
                    "layovers": layovers,
                    "arrival": arrival,
                    "price": flight_options['price'],
                    "duration": flight_options['total_duration'],
                    "booking_link": best_flights_data[idx]["search_metadata"]["google_flights_url"],
                    "booking_token": flight_options['booking_token'],
                    "user_email" : targets['user_email'],
                    "layover_count" : layover,
                })
                
    # print(flight_deal)
    return flight_deal
# flight_deal_checker()