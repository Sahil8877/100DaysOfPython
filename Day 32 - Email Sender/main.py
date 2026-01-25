import smtplib,random,datetime,pytz
from quote import quote

sender = 'testeremail8877@gmail.com'
password = 'jxmg ijzb sgaw anar'
sahil_email = "sahils.8877@gmail.com"
khushi_email = "khushikhandelwal1997@gmail.com"


def mail_for_india():
    generate_quote = quote('Growth Motivation',limit=20)
    receiver_dict ={"Khushi":khushi_email}
    for receiver in receiver_dict:
        random_quote = random.choice(generate_quote)
        message = f"Subject:Hi {receiver}, Todays Quote From {random_quote['author']}.\n\nYour Monday Motivation :\n\n\n{random_quote['quote']}\n\n\nPlease do not reply to this email."
        with smtplib.SMTP(host='smtp.gmail.com') as conn:
            conn.starttls()
            conn.login(user=sender,password=password)
            conn.sendmail(from_addr=sender, to_addrs=receiver_dict[receiver], msg=message.encode("utf-8"))


def mail_for_uk():
    generate_quote = quote('Growth Motivation',limit=20)
    receiver_dict ={"Sahil":sahil_email}
    for receiver in receiver_dict:
        random_quote = random.choice(generate_quote)
        message = f"Subject:Hi {receiver}, Todays Quote From {random_quote['author']}.\n\nYour Monday Motivation :\n\n\n{random_quote['quote']}\n\n\nPlease do not reply to this email."
        with smtplib.SMTP(host='smtp.gmail.com') as conn:
            conn.starttls()
            conn.login(user=sender,password=password)
            conn.sendmail(from_addr=sender, to_addrs=receiver_dict[receiver], msg=message.encode("utf-8"))

now_utc = datetime.datetime.now(pytz.utc)

curr_time_india = now_utc.astimezone(pytz.timezone("Asia/Kolkata"))
curr_time_uk = now_utc.astimezone(pytz.timezone("Europe/London"))

print(curr_time_india,curr_time_uk.hour)

if curr_time_uk.hour == 9 and curr_time_uk.minute == 0:
    mail_for_uk()
    print('Email prepared for sending to UK')
if curr_time_india.hour == 9 and curr_time_india.minute == 0:
    mail_for_india()
    print('Email prepared for sending to India')




