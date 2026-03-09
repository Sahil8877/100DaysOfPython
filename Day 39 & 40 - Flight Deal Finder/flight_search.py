import os
import sheets_data
import requests
import datetime
from serpapi import GoogleSearch
from dotenv import load_dotenv
import logging

load_dotenv()

flight_list = sheets_data.sheets_data_list
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")

def mark_row_as_expired(Object_ID):
    DELETE_URL = os.getenv('SHEETS_FLIGHT_DEAL_DELETE_URL')
    try:
        response = requests.delete(url=f"{DELETE_URL}{Object_ID}")
        print(response.status_code)
        if response.status_code in [200, 204]:
            logging.info(f"Row {Object_ID} deleted successfully")
        else:
            logging.warning(f"Failed to delete row {Object_ID}: {response.status_code} {response.text}")
    except Exception as e:
        logging.error(f"Error deleting row {Object_ID}: {e}")

def search_result():
    best_flights = []

    logging.info("\n==================== API LOGS ====================")

    today = datetime.datetime.today()

    for target in flight_list:
        # Group results for this specific target
        target_results = []

        # check empty email from sheets_data.py
        if not target.get("user_email", "").strip():
            best_flights.append(target_results)
            continue

        try:
            today = datetime.datetime.today()

            departure_date = datetime.datetime.strptime(
                target["departure_date"], "%Y-%m-%d"
            )

            # Skip if flight date has passed
            if departure_date < today:
                # Fetch Sheety rows
                form_data = os.getenv('SHEETS_URL_FORM_RESPONSES')
                row_data = requests.get(form_data).json()['formResponses2']

                # Find correct row_id in Sheety
                sheety_row_id = None
                for row in row_data:
                    try:
                        # normalize values
                        email_match = row['emailAddress'].strip().lower() == target['user_email'].strip().lower()
                        departure_code_match = row['enterYourDepartureAirportCode. [resourceInDescription]'].strip().upper() == target['departure_code'].upper()
                        arrival_code_match = row['enterYourArrivalAirportCode. [resourceInDescription]'].strip().upper() == target['destination_code'].upper()

                        # parse Sheety date to standard format
                        sheety_date = datetime.datetime.strptime(row['specifyAFlightDeadline.'], '%m/%d/%Y').strftime('%Y-%m-%d')
                        date_match = sheety_date == target['departure_date']

                        if email_match and departure_code_match and arrival_code_match and date_match:
                            sheety_row_id = row['id']
                            break
                    except Exception as e:
                        print("Validation error:", e)

                if sheety_row_id:
                    print("Matched Sheety Row ID:", sheety_row_id)
                    mark_row_as_expired(sheety_row_id)
                else:
                    logging.warning(f"No matching Sheety row found for {target['user_email']}")
                    
                best_flights.append(target_results)
                continue

            start_date = departure_date - datetime.timedelta(days=120)
            
            if start_date < today:
                start_date = today

            search_end = datetime.datetime.strptime(target['departure_date'],"%Y-%m-%d")
            current = start_date

            while current <= search_end:

                logging.info(
                    f"SEARCHING | {target['departure_code']}→{target['destination_code']} | {current.strftime('%Y-%m-%d')}"
                )

                params = {
                    "engine": "google_flights",
                    "departure_id": target["departure_code"],
                    "arrival_id": target["destination_code"],
                    "outbound_date": current.strftime("%Y-%m-%d"),
                    "currency": "GBP",
                    "hl": "en",
                    "gl": "uk",
                    "api_key": os.getenv("SERP_API_KEY"),
                    "type": "2"
                }

                search = GoogleSearch(params)
                result = search.get_dict()
                target_results.append(result)

                # ---- dynamic step logic ----
                days_left = (departure_date - current).days

                if days_left > 120:
                    step = 30
                elif days_left > 60:
                    step = 15
                else:
                    step = 7

                current += datetime.timedelta(days=step)
            
            # Append all dates searched for this user
            best_flights.append(target_results)

        except Exception as e:
            print("Error:", e)
            best_flights.append(target_results)
            
    return best_flights