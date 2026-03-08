import sheets_data
import flight_search
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:%(message)s"
)

logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)

target_data = sheets_data.sheets_data_list

def flight_deal_checker():
    flight_deal = []
    best_flights_data = flight_search.search_result()

    # ---- Header for data logs ----
    logging.info("\n==================== DATA LOGS ====================")

    for idx, targets in enumerate(target_data):
        if "best_flights" not in best_flights_data[idx]:
            logging.info(f"No flights found for {targets['user_email']}")
            continue

        data = best_flights_data[idx].get("best_flights", [])

        for flight_options in data:
            segments = flight_options['flights']
            layover = max(len(segments) - 1, 0)

            # ---- Requested flights log ----
            logging.info(
                f"REQUESTED | {targets['user_email']} | "
                f"{segments[0]['departure_airport']['id']}→{segments[-1]['arrival_airport']['id']} | "
                f"£{flight_options['price']} | "
                f"{flight_options['total_duration']}min | "
                f"{layover} stops"
            )

            # ---- Filter by target price/duration ----
            if flight_options['price'] <= targets['price_target'] and flight_options['total_duration'] <= targets['duration_target']:
                departure = segments[0]['departure_airport']
                arrival = segments[-1]['arrival_airport']

                # ---- Matched flights log ----
                logging.info(
                    f"MATCHED | {targets['user_email']} | "
                    f"{segments[0]['departure_airport']['id']}→{segments[-1]['arrival_airport']['id']} | "
                    f"£{flight_options['price']} | "
                    f"{flight_options['total_duration']}min | "
                    f"{layover} stops"
                )

                # ---- Layovers ----
                layovers = []
                if 'layovers' in flight_options and flight_options['layovers']:
                    for i, l in enumerate(flight_options['layovers']):
                        layovers.append({
                            "airport": l['name'],
                            "arrival_time": segments[i]['arrival_airport']['time'],
                            "departure_time": segments[i+1]['departure_airport']['time'],
                            "duration": round(float(l['duration'])/60, 1)
                        })

                # ---- Append matched flight ----
                flight_deal.append({
                    "departure": departure,
                    "layovers": layovers,
                    "arrival": arrival,
                    "price": flight_options['price'],
                    "duration": flight_options['total_duration'],
                    "booking_link": best_flights_data[idx]["search_metadata"]["google_flights_url"],
                    "booking_token": flight_options['booking_token'],
                    "user_email": targets['user_email'],
                    "layover_count": layover
                })
            else:
                # ---- Rejected flights log ----
                logging.info(
                    f"REJECTED | {targets['user_email']} | "
                    f"{segments[0]['departure_airport']['id']}→{segments[-1]['arrival_airport']['id']} | "
                    f"£{flight_options['price']} | "
                    f"{flight_options['total_duration']}min | "
                    f"{layover} stops"
                )

    return flight_deal