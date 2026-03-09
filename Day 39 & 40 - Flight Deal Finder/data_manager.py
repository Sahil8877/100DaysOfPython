import sheets_data
import flight_search
import logging
import urllib.parse

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
            # BEST FLIGHTS
            flight_options_list = data.get('best_flights') or []
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
                    continue

                logging.info(
                    f"VERYFING | {targets['user_email']} | "
                    f"{segments[0]['departure_airport']['id']}→{segments[-1]['arrival_airport']['id']} | {search_date} | "
                    f"£{price} | {total_duration}min | {layover_count} stops"
                )

                # Check target limits (Price, Duration, and Layovers)
                price_ok = price <= targets.get('price_target', float('inf'))
                duration_ok = total_duration <= targets.get('duration_target', float('inf'))
                layover_ok = layover_count <= targets.get('layover_count', float('inf'))

                if price_ok and duration_ok and layover_ok:
                    logging.info(
                        f"ACCEPTED | {targets['user_email']} | "
                        f"{segments[0]['departure_airport']['id']}→{segments[-1]['arrival_airport']['id']} | {search_date} | "
                        f"£{price} | {total_duration}min | {layover_count} stops"
                    )

                    # GOOGLE FLIGHTS URL
                    dest = targets['destination_code']
                    dep = targets['departure_code']
                    
                    # query with param for type= "one way" and sets exact dates/airports
                    search_query = f"Flights from {dep} to {dest} on {search_date} one way"
                    
                    # Encode spaces to %20
                    encoded_query = urllib.parse.quote(search_query)
                    custom_booking_link = f"https://www.google.com/travel/flights?q={encoded_query}"
                    
                    # Get layover details
                    layovers = []
                    for i, l in enumerate(flight_options.get('layovers', [])):
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
                        "booking_link": custom_booking_link,
                        "booking_token": flight_options.get('booking_token'),
                        "user_email": targets['user_email'],
                        "layover_count": layover_count
                    })
                else:
                    logging.info(
                        f"REJECTED | {targets['user_email']} | "
                        f"{segments[0]['departure_airport']['id']}→{segments[-1]['arrival_airport']['id']} | {search_date} | "
                        f"£{price} | {total_duration}min | {layover_count} stops"
                    )

    # Sort the final extracted deals by price
    flight_deals = sorted(flight_deals, key=lambda x: x['price'])
    
    logging.info(f"\nTotal flight deals found: {len(flight_deals)}")
    return flight_deals