import smtplib
import email_manager
import os
import logging
sender = os.getenv('SENDER_EMAIL')
password = os.getenv('SENDER_EMAIL_PASS')

with smtplib.SMTP(host='smtp.gmail.com') as conn:
    conn.starttls()
    for user_msg in email_manager.emails:

        conn.login(user=sender,password=password)
           
        conn.sendmail(
            msg=email_manager.emails[user_msg].encode("utf-8"),
            from_addr=sender,
            to_addrs=user_msg,)
        logging.info(
        f"ALERTED | user={user_msg} | "
        )
