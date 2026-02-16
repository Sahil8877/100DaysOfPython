import smtplib
from main import check_weather_for_rain
import os

previous_state, send_alert = check_weather_for_rain()

message = f"Subject: Rain Alert\n\nLevel: {previous_state}"
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
    

