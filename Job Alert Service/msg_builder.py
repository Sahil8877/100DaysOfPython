from parser import parse_jobs
import pyshorteners
def prepare_msg(querystring):
    message = ""
    try:
        data = parse_jobs(querystring)
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return "Job results could not be retrieved this time."
    if data:
        for items in data:
            try:
                short_link = pyshorteners.Shortener().tinyurl.short(items['Apply Link'])
            except Exception as e:
                print(f"Could not shorten link: {e}")
                short_link = items['Apply Link']
            format_string = f"👉 Job Title - {items['Job Title']},\nCompany Name - {items['Company']},\nType - {items['Type']},\nLocation - {items['Location']},\nApply Here - {short_link}\n---------------------------------------------------------\n\n"
            message += format_string
    return message
