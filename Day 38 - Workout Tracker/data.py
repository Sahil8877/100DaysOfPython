import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

BASE_URL = "https://app.100daysofpython.dev"
POST_ENDPOINT = "/v1/nutrition/natural/exercise"
header = {
        "Content-Type": "application/json",
        "x-app-id" : os.getenv('NUTR_API_ID'),
        "x-app-key" :  os.getenv('NUTR_API_KEY')
    }

def get_workout_data(query):    
    parameter = {
        "query" : query
    }
    req = requests.post(url=f"{ BASE_URL}/{POST_ENDPOINT}",json=parameter,headers=header)
    return req.json()

def post_workout_data(query):
    data = get_workout_data(query)
    for item in data['exercises']:
        formatted_data = {
            "sheet1" : {
                'date' : datetime.datetime.now().date().strftime(format="%d/%m/%Y"),
                'time' : datetime.datetime.now().time().strftime(format="%H:%M"),
                'description' : item['name'],
                'duration' : item['duration_min'],
                'calories' : item['nf_calories'],
                }
        }
        post = requests.post(url=f"https://api.sheety.co/221b6249dfacca406f5e9cf4c546c8a0/workoutTracker/sheet1",json=formatted_data)
        
    print('Thank You! The Tracker has been updated!')

print("\n\n__WROKOUT TRACKING__")
query = input('Type your workout details :')
post_workout_data(query)