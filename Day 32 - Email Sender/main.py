import smtplib,random,datetime,pytz,os
from quote import quote

sender = os.environ["SENDER_EMAIL"]
password = os.environ["SENDER_EMAIL_PASS"]
recipients_list_ind = os.environ["RECEPIENTS_LIST_IND"]
recipients_list_uk = os.environ["RECEPIENTS_LIST_UK"]

def parse_recepients(recepients_list):
    receiver_dict = {}
    for key in recepients_list.split(','):
        name, email = key.split(':')
        receiver_dict[name.strip(" '' ")] = email.strip()
    return receiver_dict

def mail_for_india():
    generate_quote = quote('Growth Motivation',limit=20)
    receiver_dict = parse_recepients(recipients_list_ind)
    for receiver in receiver_dict:
        random_quote = random.choice(generate_quote)
        message = f"Subject:Hi {receiver}, Todays Quote From {random_quote['author']}.\n\nYour Daily Motivation :\n\n\n{random_quote['quote']}\n\n\nPlease do not reply to this email."
        with smtplib.SMTP(host='smtp.gmail.com') as conn:
            conn.starttls()
            conn.login(user=sender,password=password)
            conn.sendmail(from_addr=sender, to_addrs=receiver_dict[receiver], msg=message.encode("utf-8"))

def mail_for_uk():
    generate_quote = quote('Growth Motivation',limit=20)
    receiver_dict = parse_recepients(recipients_list_uk)
    for receiver in receiver_dict:
        random_quote = random.choice(generate_quote)
        message = f"Subject:Hi {receiver}, Todays Quote From {random_quote['author']}.\n\nYour Daily Motivation :\n\n\n{random_quote['quote']}\n\n\nPlease do not reply to this email."
        with smtplib.SMTP(host='smtp.gmail.com') as conn:
            conn.starttls()
            conn.login(user=sender,password=password)
            conn.sendmail(from_addr=sender, to_addrs=receiver_dict[receiver], msg=message.encode("utf-8"))

now_utc = datetime.datetime.now(pytz.utc)

curr_time_india = now_utc.astimezone(pytz.timezone("Asia/Kolkata"))
curr_time_uk = now_utc.astimezone(pytz.timezone("Europe/London"))

print(curr_time_india,curr_time_uk.hour)

if curr_time_uk.hour == 6 and curr_time_uk.minute < 45:
    mail_for_uk()
    print('Email prepared for sending to UK')
if curr_time_india.hour == 6 and curr_time_india.minute < 45:
    mail_for_india()
    print('Email prepared for sending to India')




