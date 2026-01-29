import smtplib,random,datetime,pytz,os
from quote import quote

sender = os.environ["SENDER_EMAIL"]
password = os.environ["SENDER_EMAIL_PASS"]
recipients_list_ind = os.environ["RECIPIENTS_LIST_IND"]
recipients_list_uk = os.environ["RECIPIENTS_LIST_UK"]

now_utc = datetime.datetime.now(pytz.utc)
curr_time_india = now_utc.astimezone(pytz.timezone("Asia/Kolkata"))
curr_time_uk = now_utc.astimezone(pytz.timezone("Europe/London"))

last_sent_ind = None
last_sent_uk = None
TARGET_TIME_IND = curr_time_india.replace(hour=6,minute=0)
TARGET_TIME_UK = curr_time_uk.replace(hour=6,minute=0)

try:
    with open('mail_sent_to_ind.txt','r') as file:
        last_sent_ind = file.read().strip()
except FileNotFoundError as e:
    print('File not found :',e)
try:
    with open('mail_sent_to_uk.txt','r') as file:
        last_sent_uk = file.read().strip()
except FileNotFoundError as e:
    print('File not found :',e)

def parse_recipients(recipients_list):
    receiver_dict = {}
    for key in recipients_list.split(','):
        name, email = key.split(':')
        receiver_dict[name.strip(" '' ")] = email.strip()
    return receiver_dict

def mail_for_india():
    receiver_dict = parse_recipients(recipients_list_ind)
    send_email(receiver_dict)
   
    with open('mail_sent_to_ind.txt','w') as file:
        file.write(f'{curr_time_india.date()}')
    
def mail_for_uk():
    receiver_dict = parse_recipients(recipients_list_uk)
    file_path = os.path.join(os.getcwd(),'mail_sent_to_uk.txt')
    send_email(receiver_dict)
    with open(file_path,'w') as file:
        file.write(f'{curr_time_uk.date()}')

def send_email(receiver_dict):
    generate_quote = quote('Growth Motivation',limit=20)
    with smtplib.SMTP(host='smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(user=sender,password=password)
        for receiver in receiver_dict:
            random_quote = random.choice(generate_quote)
            message = f"Subject:Hi {receiver}, Todays Quote From {random_quote['author']}.\n\nYour Daily Motivation :\n\n\n{random_quote['quote']}\n\n\nPlease do not reply to this email."
            conn.sendmail(from_addr=sender, to_addrs=receiver_dict[receiver], msg=message.encode("utf-8"))

if curr_time_uk >= TARGET_TIME_UK and last_sent_uk != str(curr_time_uk.date()):
        mail_for_uk()
        print('Email prepared for sending to UK')
"""
if curr_time_india >= TARGET_TIME_IND and last_sent_ind != str(curr_time_india.date()):
        mail_for_india()
        print('Email prepared for sending to India')"""
