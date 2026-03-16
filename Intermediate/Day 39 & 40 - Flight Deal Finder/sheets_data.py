import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")

url = os.getenv('SHEETS_URL_FLIGHT_DEAL')

headers = {
"User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

data_json = response.json()

sheets_data_list = []

for data in data_json.get("sheet1", []):
    
    email = data.get("emailAddress", "")
    if isinstance(email, str):
        email = email.strip()

    if email:
<<<<<<< HEAD
        # 1. Grab the original form price
        original_price = data.get("priceTarget", float('inf'))
        
        # 2. Grab the dumb column price
        lowest_found = data.get("lowestPriceFound")

        # 3. YOUR LOGIC: If dumb column is blank, use original. Else, use dumb column.
        if lowest_found == "" or lowest_found is None:
            current_target = float(original_price)
        else:
            current_target = float(lowest_found)
=======
        # --- THE FIX: SMART PRICE LOGIC ---
        # Grab original form target (e.g., 900)
        original_price = data.get("priceTarget", float('inf'))
        
        # Grab the lowest price Python has found so far (e.g., 463)
        lowest_found = data.get("lowestPriceFound")

        # If we have a lower price recorded, use it! Otherwise, use the original budget.
        if lowest_found is not None and str(lowest_found).strip() != "":
            current_target = float(lowest_found)
        else:
            current_target = float(original_price)
        # ----------------------------------
>>>>>>> 7284de76a21eb6c729f654f2022bc01f5b9ea56b

        sheets_data_list.append({
            "destination_code": data["destinationCode"],
            "departure_code": data["departureCode"],
<<<<<<< HEAD
            "price_target": current_target, 
=======
            "price_target": current_target, # <--- Now passing the smartest price to the checker
>>>>>>> 7284de76a21eb6c729f654f2022bc01f5b9ea56b
            "duration_target": int(data["durationTarget"]),
            "layover_count": data["layoverCount"],
            "user_email": email,
            'departure_date': data['departureDate'],
            'row_id' : data['id'],
        })
    else:
        logging.warning(f"NO EMAIL FOUND | {data.get('departureCode', 'N/A')}->{data.get('destinationCode', 'N/A')}")
        
        sheet1_row_id = data.get('id')
        if sheet1_row_id:
            target_row_id = int(sheet1_row_id) - 1
            
            if target_row_id > 1:
                delete_url = os.getenv('SHEETS_FLIGHT_DEAL_DELETE_URL')
                try:
                    del_response = requests.delete(url=f"{delete_url}{target_row_id}")
                    if del_response.status_code in [200, 204]:
                        logging.info(f"Row {target_row_id} (Sheet1 ID: {sheet1_row_id}) deleted successfully due to missing email.")
                    else:
                        logging.warning(f"Failed to delete row {target_row_id}: {del_response.status_code} {del_response.text}")
                except Exception as e:
                    logging.error(f"Error deleting row {target_row_id}: {e}")
            else:
                logging.debug(f"Skipped deleting target row {target_row_id} (Sheet1 ID: {sheet1_row_id}) to protect sheet headers.")
