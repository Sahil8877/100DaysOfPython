import sheets_data
import flight_search
import logging
import pprint

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s"
)

logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)

target_data = sheets_data.sheets_data_list

def flight_deal_checker():
    flight_deals = []
    # This contains a list of lists (each sublist represents all dates searched for one target)
    best_flights_data = flight_search.search_result()
    logging.debug(f"Total flight search targets processed: {len(best_flights_data)}")

    for idx, targets in enumerate(target_data):
        logging.debug(f"\nProcessing target index {idx}: {targets['user_email']}")

        if idx >= len(best_flights_data):
            logging.warning(f"No flight data for target index {idx}")
            continue

        target_search_results = best_flights_data[idx]
        
        if not target_search_results:
             logging.info(f"NO FLIGHTS | API search results empty for {targets['user_email']}")
             continue

        for data in target_search_results:
            flight_options_list = data.get('best_flights') or []
            
            # Grab the search date here so we can use it for ALL logs (No Flights, Requested, Accepted, Rejected)
            search_date = data.get('search_parameters', {}).get('outbound_date', 'Unknown Date')

            if not flight_options_list:
                logging.info(
                    f"NO FLIGHTS | {targets['user_email']} | "
                    f"{targets['departure_code']}→{targets['destination_code']} | {search_date}"
                )
                continue

            for flight_options in flight_options_list:
                segments = flight_options.get('flights') or []

                if not segments:
                    logging.warning("Flight option has no segments, skipping")
                    continue

                price = flight_options.get('price')
                total_duration = flight_options.get('total_duration', float('inf'))
                layover_count = max(len(segments) - 1, 0)

                if price is None:
                    logging.warning("Flight option missing price, skipping")
                    continue

                # Added {search_date} to the REQUESTED log
                logging.info(
                    f"REQUESTED | {targets['user_email']} | "
                    f"{segments[0]['departure_airport']['id']}→{segments[-1]['arrival_airport']['id']} | {search_date} | "
                    f"£{price} | {total_duration}min | {layover_count} stops"
                )

                price_ok = price <= targets.get('price_target', float('inf'))
                duration_ok = total_duration <= targets.get('duration_target', float('inf'))

                if price_ok and duration_ok:
                    # Added {search_date} to the ACCEPTED log
                    logging.info(
                        f"ACCEPTED | {targets['user_email']} | "
                        f"{segments[0]['departure_airport']['id']}→{segments[-1]['arrival_airport']['id']} | {search_date} | "
                        f"£{price} | {total_duration}min | {layover_count} stops"
                    )
                    
                    layovers = []
                    for i, l in enumerate(flight_options.get('layovers', [])):
                        # segments[i+1] represents the flight departing the layover
                        if i + 1 < len(segments):
                            layovers.append({
                                "airport": l.get('name'),
                                "arrival_time": segments[i]['arrival_airport'].get('time'),
                                "departure_time": segments[i + 1]['departure_airport'].get('time'),
                                "duration": round(float(l.get('duration', 0)) / 60, 1),
                                "airline": segments[i + 1].get('airline', 'Unknown Airline'),
                                "airline_logo": segments[i + 1].get('airline_logo', '')
                            })

                    flight_deals.append({
                        "departure": segments[0]['departure_airport'],
                        "airline": segments[0].get('airline', 'Unknown Airline'),
                        "airline_logo": segments[0].get('airline_logo', ''),
                        "layovers": layovers,
                        "arrival": segments[-1]['arrival_airport'],
                        "price": price,
                        "duration": total_duration,
                        "booking_link": data.get("search_metadata", {}).get("google_flights_url"),
                        "booking_token": flight_options.get('booking_token'),
                        "user_email": targets['user_email'],
                        "layover_count": layover_count
                    })
                else:
                    # Added {search_date} to the REJECTED log
                    logging.info(
                        f"REJECTED | {targets['user_email']} | "
                        f"{segments[0]['departure_airport']['id']}→{segments[-1]['arrival_airport']['id']} | {search_date} | "
                        f"£{price} | {total_duration}min | {layover_count} stops"
                    )

    logging.debug(f"\nTotal flight deals found: {len(flight_deals)}")
    return flight_deals