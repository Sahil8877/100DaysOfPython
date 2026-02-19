from parser import parse_jobs
import pyshorteners

def prepare_msg(querystring):
    data = parse_jobs(querystring)
    if data:
        message = ""
        for items in data:
            format_string = f"👉 Job Title - {items['Job Title']},\nCompany Name - {items['Company']},\nType - {items['Type']},\nLocation - {items['Location']},\nApply Here - {pyshorteners.Shortener().tinyurl.short(items['Apply Link'])}\n---------------------------------------------------------\n\n"
            message += format_string
    return message

