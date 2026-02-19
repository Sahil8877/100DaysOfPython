import msg_builder
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

job_queries = [
    {
        '0' : 
        {
            "query":"python developer jobs in uk",
            "page":"1",
            "num_pages":"1",
            "country":"uk",
            "date_posted":"all",
            "employment_types":"FULLTIME,INTERN",
            "job_requirements":"under_3_years_experience"
        }
    },
    {
        '1' : 
        {
            "query":"pharmacy research jobs in uk",
            "page":"1",
            "num_pages":"1",
            "country":"uk",
            "date_posted":"all",
            "employment_types":"FULLTIME,INTERN",
            "job_requirements":"under_3_years_experience"
        }
    },
    {
        '2':
        {
            "query":"marketing jobs in uk",
            "page":"1",
            "num_pages":"1",
            "country":"uk",
            "date_posted":"all",
            "employment_types":"FULLTIME,INTERN",
            "job_requirements":"under_3_years_experience"
        }
    },
    {
        '3':
        {
            "query":"law internships in bangalore",
            "page":"1",
            "num_pages":"1",
            "country":"uk",
            "date_posted":"all",
            "employment_types":"INTERN",
            "job_requirements":"under_3_years_experience"
        }
    }
]
def fetch_email_data():
    sender = os.getenv("SENDER_EMAIL")
    password = os.getenv("SENDER_EMAIL_PASS")
    recipients_list_uk_for_jobs = os.getenv("RECIPIENTS_LIST_UK_FOR_JOBS")
    return sender,password,recipients_list_uk_for_jobs

def parse_recipients(recipients_list):
    receiver_dict = {}
    for key in recipients_list.split(','):
        name, query_num, email = key.split(':')
        receiver_dict[name.strip(" '' ")] = query_num.strip(), email.strip()
    return receiver_dict

def send_mail():
    sender, password, recipients_list_uk_for_jobs = fetch_email_data()
    receiver_dict = parse_recipients(recipients_list_uk_for_jobs)
    
    with smtplib.SMTP(host='smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(user=sender,password=password)
        
        for receiver in receiver_dict:
            msg = EmailMessage()
            msg['From'] = sender
            msg['To'] = receiver_dict[receiver][1]
            msg['Subject'] = f"Morning {receiver}, Check out your fresh job postings!"
            msg.set_content(f"{prepare_jobs(receiver_dict[receiver][0])}")
            conn.send_message(msg)
            print(f"Email sent to {receiver}")

def prepare_jobs(query_num):
    for query in job_queries:
        for index in query:
            if query_num == index:
                message = msg_builder.prepare_msg(query[index])
                break
    return message
                
send_mail()
  

