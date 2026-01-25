import smtplib,random
from quote import quote

sender = 'testeremail8877@gmail.com'
password = 'jxmg ijzb sgaw anar'
sahil_email = "sahils.8877@gmail.com"
khushi_email = "ssuryavanshi8877@gmail.com"
receiver_dict ={"Sahil":sahil_email,"Khushi":khushi_email}
generate_quote = quote('Growth Motivation',limit=10)

for receiver in receiver_dict:
    random_quote = random.choice(generate_quote)
    message = f'Subject:Hi {receiver}, Todays Quote From {random_quote['author']}.\n\nYour Monday Motivation :\n\n\n{random_quote['quote']}\n\n\nPlease do not reply to this email.'
    with smtplib.SMTP(host='smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(user=sender,password=password)
        conn.sendmail(from_addr=sender, to_addrs=receiver_dict[receiver], msg=message.encode("utf-8"))

print('Email prepared for sending')


