import data_manager
import datetime
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:%(message)s"
)

clean_flights = data_manager.flight_deal_checker()
emails = {}

if clean_flights:
    
    print("\nALERT LOGS:")
    for flight in clean_flights:

        # print(flight)
        email = flight["user_email"]
        
        if email not in emails:
            emails[email] = "Subject:Checkout your flight deals!\n\n✈️ Cheap Flight Deals Found For You\n"


        route = f'{flight["departure"]["name"]} → {flight["arrival"]["name"]}'

        dep_time = datetime.datetime.strptime(
            flight["departure"]["time"], "%Y-%m-%d %H:%M"
        )

        arr_time = datetime.datetime.strptime(
            flight["arrival"]["time"], "%Y-%m-%d %H:%M"
        )

        # ---- Layover info ----
        layover_text = ""

        if "layover" in flight and flight["layovers"]:
            layover_text += "\n🛑 Layovers:\n"

            for layover in flight["layover"]:

                layover_airport = layover["airport"]
                layover_duration = round(layover["duration"]/60, 1)

                layover_text += f"   • {layover_airport} ({layover_duration} hrs)\n"

        else:
            layover_text = "\n✈️ Direct Flight\n"
        
    
        emails[email] += f"""

-> Route: {route}

    🛫 {dep_time.strftime("%H:%M")} - {flight["departure"]["name"]}
    🛬 {arr_time.strftime("%H:%M")} - {flight["arrival"]["name"]}

💰 £{flight['price']} | ⏱ {round(flight['duration']/60,1)} hrs
       {layover_text}
🔗 Book Now:
    {flight['booking_link']}

------------------------------------------------
    """
else:
    print("No Flight Data Found To Alert!")
 