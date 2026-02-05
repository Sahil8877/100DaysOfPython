
import requests,datetime,os
from datetime import timedelta

API_KEY = os.environ['NEO_API_KEY']

START_DATE = datetime.datetime.now().date()
END_DATE = datetime.datetime.now().date() + timedelta(days=7)
MOON_DIST_KM = 384400
TIME = datetime.datetime.now().time()
curr_month = datetime.datetime.now().month

response = requests.get(url=f'https://api.nasa.gov/neo/rest/v1/feed?start_date={START_DATE}&end_date={END_DATE}&api_key={API_KEY}')
asteroid_data = response.json()
num_of_elements = asteroid_data['element_count']
passing_astr = {}

#when will an asteroid pass over earth

for date in asteroid_data['near_earth_objects']:
    for astro_info in asteroid_data['near_earth_objects'][date]:
        approach_date_time = astro_info['close_approach_data'][0]['close_approach_date_full'].split(" ")
        approach_date = astro_info['close_approach_data'][0]['close_approach_date']
        approach_time = approach_date_time[1]
        astro_name = astro_info['name']
        astro_size_in_km = astro_info['estimated_diameter']['kilometers']
        astro_speed_in_kmph = float(astro_info['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
        astro_miss_dist_in_km = float(astro_info['close_approach_data'][0]['miss_distance']['kilometers'])
        astro_is_hazardous = astro_info['is_potentially_hazardous_asteroid']
        lunar_dist_from_closest_astro = round(astro_miss_dist_in_km/MOON_DIST_KM,2)
        
       
        passing_astr[astro_name] = {
            'approach_date' : approach_date, 
            'approach_time': approach_time,
            'hazardous' : astro_is_hazardous,
            'miss_dist' : astro_miss_dist_in_km,
            'dist_from_moon' : lunar_dist_from_closest_astro,
            'velocity' : round(float(astro_speed_in_kmph),2),
            }
        
# hazardous_astro = []
closes_astro_list = []

hazardous_astro = [{
            'name': 'None',
            'miss_dist' : 0,
            'date' : 'DD:MM:YYYY',
            'time' : '00:00:00',
            'dist_from_moon' : 0,
            'velocity' : 0,
        }]
        

for name, data in passing_astr.items():
    
    if data['hazardous']:
        hazardous_astro[0] = ({
            'name':name.strip("( )"),
            'miss_dist' : round(float(data['miss_dist']),2),
            'date' : data['approach_date'],
            'time' : data['approach_time'],
            'dist_from_moon' : data['dist_from_moon'],
            'velocity' : data['velocity'],
        }
        )

print(hazardous_astro)
if hazardous_astro:
    closes_astro_list = hazardous_astro[0]
    for astro in hazardous_astro:
        if astro['miss_dist'] < closes_astro_list['miss_dist']:
            closes_astro_list = astro
else:
    closes_astro_list = None



