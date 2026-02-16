import smtplib
from main import check_weather_for_rain
import os

previous_state, send_alert = check_weather_for_rain()

if previous_state == 'Light Rain Alert':
    message = f"Subject: Drizzle Alert! 💧 Tiny Drops Incoming\n\nLight rain ☔️ expected in the next 30 minutes ⏰. Might want to grab that umbrella!"
elif previous_state == 'Moderate Rain Alert':
    message = f"Subject: Rain Alert! 🌧️ It's Getting Wet\n\nModerate rain ☔️ coming your way in 30 minutes ⏰. Definitely grab your umbrella!"
elif previous_state == 'Heavy Rain Alert':
    message = f"Subject: Heavy Rain Alert! ⛈️ Big Drops Incoming\n\nHeavy downpour ☔️ expected in the next 30 minutes ⏰. Stay inside or gear up!"   

sender = os.environ["SENDER_EMAIL"]
password = os.environ["SENDER_EMAIL_PASS"]
recipients_list_uk_rain_alert = os.environ["RECIPIENTS_LIST_UK_RAIN_ALERT"]

def parse_recipients(recipients_list):
    receiver_dict = {}
    for key in recipients_list.split(','):
        name, email = key.split(':')
        receiver_dict[name.strip(" '' ")] = email.strip()
    return receiver_dict

receiver_dict = parse_recipients(recipients_list_uk_rain_alert)

if send_alert:
    if previous_state != 'No Significant Rain':
        with smtplib.SMTP(host='smtp.gmail.com') as conn:
            conn.starttls()
            conn.login(user=sender,password=password)
            print(receiver_dict)
            for receiver in receiver_dict:
                conn.sendmail(
                    msg=message.encode("utf-8"),
                    from_addr=sender,
                    to_addrs=receiver_dict[receiver],
                )
            print("email sent")
            
    with open('previous_state.txt','w') as file:
        file.write(previous_state)
    

