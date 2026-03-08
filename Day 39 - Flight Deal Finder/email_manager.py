import data_manager
import datetime
import logging
import time
import pyshorteners
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:%(message)s"
)

clean_flights = data_manager.flight_deal_checker()
emails = {}

if clean_flights:
    print("\nALERT LOGS:")
    
    for flight in clean_flights:
        email = flight["user_email"]
        
        if email not in emails:
            emails[email] = "Subject:Checkout your flight deals!\n\n✈️ Cheap Flight Deals Found For You\n"

        route = f'{flight["departure"]["name"]} → {flight["arrival"]["name"]}'

        # Departure & arrival datetime objects
        dep_dt = datetime.datetime.strptime(flight["departure"]["time"], "%Y-%m-%d %H:%M")
        arr_dt = datetime.datetime.strptime(flight["arrival"]["time"], "%Y-%m-%d %H:%M")

        dep_date_time = dep_dt.strftime("%d-%b-%Y %H:%M")
        arr_date_time = arr_dt.strftime("%d-%b-%Y %H:%M")

        # ---- Layover info ----
        layover_text = ""
        if "layovers" in flight and flight["layovers"]:
            layover_text += "  🛑 Layovers:\n"
            for layover in flight["layovers"]:
                layover_airport = layover["airport"]

                layover_arr_dt = datetime.datetime.strptime(layover["arrival_time"], "%Y-%m-%d %H:%M")
                layover_dep_dt = datetime.datetime.strptime(layover["departure_time"], "%Y-%m-%d %H:%M")

                layover_arr_time = layover_arr_dt.strftime("%H:%M")
                layover_dep_time = layover_dep_dt.strftime("%H:%M")

                layover_duration = round((layover_dep_dt - layover_arr_dt).total_seconds() / 3600, 1)

                layover_text += f"      Arrival: {layover_arr_time}\n"
                layover_text += f"    ↓ {layover_airport}: (⏱ {layover_duration} hrs)\n"
                layover_text += f"      Depart: {layover_dep_time}\n"
        else:
            layover_text = "✈️ Direct Flight\n"

        # Build the email
        emails[email] += f"""
-> Route: {route}

{dep_date_time}
🛫 Departure: {flight['departure']['name']}

{layover_text}
🛬 Arrival: {flight['arrival']['name']}
{arr_date_time}

💰 £{flight['price']} | ⏱ {round(flight['duration']/60,1)} hrs

🔗 Book Now: {pyshorteners.Shortener().tinyurl.short(f"{flight['booking_link']}")}

------------------------------------------------
"""
        time.sleep(2)
else:
    print("No Flight Data Found To Alert!")