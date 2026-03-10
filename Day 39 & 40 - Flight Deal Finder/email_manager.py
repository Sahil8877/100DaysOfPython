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
    for flight in clean_flights:
        email = flight["user_email"]
        
        # HTML content
        if email not in emails:
            emails[email] = (
                "Subject: Checkout your flight deals!\n"
                "MIME-Version: 1.0\n"
                "Content-Type: text/html; charset=utf-8\n\n"
                "<h2 style='color: #2c3e50;'>✈️ Flight Deals Found For You</h2>\n"
            )

        route = f'{flight["departure"]["name"]} &rarr; {flight["arrival"]["name"]}'

        # Departure & arrival datetime objects
        dep_dt = datetime.datetime.strptime(flight["departure"]["time"], "%Y-%m-%d %H:%M")
        arr_dt = datetime.datetime.strptime(flight["arrival"]["time"], "%Y-%m-%d %H:%M")

        dep_date_time = dep_dt.strftime("%d-%b-%Y %H:%M")
        arr_date_time = arr_dt.strftime("%d-%b-%Y %H:%M")

        # ---- Layover info ----
        layover_text = ""
        if "layovers" in flight and flight["layovers"]:
            layover_text += "<p><strong>🛑 Layovers:</strong></p><ul style='list-style-type: none;'>"
            for idx, layover in enumerate(flight["layovers"], start=1):
                arr_time = datetime.datetime.strptime(layover["arrival_time"], "%Y-%m-%d %H:%M")
                dep_time = datetime.datetime.strptime(layover["departure_time"], "%Y-%m-%d %H:%M")
                duration_hrs = round((dep_time - arr_time).total_seconds()/3600, 1)
        
                # Inline HTML to show Layover Airline Logo and Name
                layover_text += (
                    f"<li style='margin-bottom: 12px;'>"
                    f"&nbsp;&nbsp;Arrival: {arr_time.strftime('%H:%M')} <br>"
                    f"&nbsp;&nbsp;&darr; <strong>{layover['airport']}</strong> (⏱ {duration_hrs} hrs) <br>"
                    f"&nbsp;&nbsp;Depart: {dep_time.strftime('%H:%M')} | "
                    f"<img src='{layover['airline_logo']}' width='20' height='20' style='vertical-align: middle; border-radius: 4px;'> "
                    f"<strong>{layover['airline']}</strong>"
                    f"</li>"
                )
            layover_text += "</ul>"
        else:
            layover_text = "<p>✈️ <strong>Direct Flight</strong></p>"

        # Build the HTML email
        emails[email] += f"""
        <hr style="border: 1px solid #eee;">
        <h4 style="margin-bottom: 5px;">&rarr; Route: {route}</h4>

        <p style="margin-top: 5px;">
        <strong>{dep_date_time}</strong><br>
        🛫 <strong>Departure:</strong> {flight['departure']['name']} <br>
        <img src='{flight['airline_logo']}' width='20' height='20' style='vertical-align: middle; border-radius: 4px;'> 
        <strong>{flight['airline']}</strong>
        </p>

        {layover_text}

        <p>🛬 <strong>Arrival:</strong> {flight['arrival']['name']}<br>
        <strong>{arr_date_time}</strong></p>

        <p style="font-size: 16px;">
        💰 <strong>&pound;{flight['price']}</strong> | ⏱ {round(flight['duration']/60,1)} hrs
        </p>

        <p style="font-size: 16px;">
        🔗 <strong><a href='{pyshorteners.Shortener().tinyurl.short(flight['booking_link'])}' style='color: #2980b9;'>Book Now</a></strong>
        </p>
        <br>
        """
        time.sleep(5)
else:
    print("No Flight Data Found To Alert!")