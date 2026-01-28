9import smtplib,random,datetime,pytz,os
from quote import quote

sender = os.environ["SENDER_EMAIL"]
password = os.environ["SENDER_EMAIL_PASS"]
recipients_list_ind = os.environ["RECIPIENTS_LIST_IND"]
recipients_list_uk = os.environ["RECIPIENTS_LIST_UK"]

def parse_recipients(recepients_list):
    receiver_dict = {}
    for key in recepients_list.split(','):
        name, email = key.split(':')
        receiver_dict[name.strip(" '' ")] = email.strip()
    return receiver_dict

def mail_for_india():
    receiver_dict = parse_recipients(recipients_list_ind)
    send_email(receiver_dict)
    
def send_email(receiver_dict):
    generate_quote = quote('Growth Motivation',limit=20)
    for receiver in receiver_dict:
        random_quote = random.choice(generate_quote)
        message = f"Subject:Hi {receiver}, Todays Quote From {random_quote['author']}.\n\nYour Daily Motivation :\n\n\n{random_quote['quote']}\n\n\nPlease do not reply to this email."
        with smtplib.SMTP(host='smtp.gmail.com') as conn:
            conn.starttls()
            conn.login(user=sender,password=password)
            conn.sendmail(from_addr=sender, to_addrs=receiver_dict[receiver], msg=message.encode("utf-8"))

def mail_for_uk():
    receiver_dict = parse_recipients(recipients_list_uk)
    send_email(receiver_dict)

now_utc = datetime.datetime.now(pytz.utc)
curr_time_india = now_utc.astimezone(pytz.timezone("Asia/Kolkata"))
curr_time_uk = now_utc.astimezone(pytz.timezone("Europe/London"))

print(curr_time_india,curr_time_uk.hour)

if 6 <= curr_time_uk.hour <= 7 and curr_time_uk.minute < 30:
    mail_for_uk()
    print('Email prepared for sending to UK')
if 6 <= curr_time_india.hour <= 7 and curr_time_india.minute < 30:
    mail_for_india()
    print('Email prepared for sending to India')




