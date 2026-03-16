import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

url = "https://jsearch.p.rapidapi.com/search"

headers = {
	"x-rapidapi-key": os.getenv("RAPID_API_KEY"),
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

def get_jobs(querystring):
    querystring = querystring
    print("Query - ", querystring)
    response = requests.get(url, headers=headers, params=querystring)
    print("Response code - ",response.status_code)
    json_data = response.json()
    json_formatted = json.dumps(json_data,indent=4)
    return json_data

    