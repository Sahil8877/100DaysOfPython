import requests
import datetime

class WeatherData:
    def __init__(self):
        parameters = {            
            'lat' : 55.84911,
            'lon' : -4.22674,
            'appid' : '436342267ecf2d4b2694e0f9404073d3',
            'exclude' : 'daily,current'
        }
        self.api_call = requests.get(url=f"https://api.openweathermap.org/data/3.0/onecall",params=parameters)

    def minutely_forecast(self):
        try:
            minutely_forecast_list = []
            self.response = self.api_call.json()
            for data in self.response['minutely']:
                entry = {"date" : str(datetime.datetime.utcfromtimestamp(data['dt'])), 
                          "precipitation" : data['precipitation']}
                
                minutely_forecast_list.append(entry)
            print(minutely_forecast_list)
            return minutely_forecast_list
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  
        except Exception as err:
            print(f"Other error occurred: {err}")


    def hourly_pop(self):
        pop_values = []
        for weather_tag in self.response['hourly']:
            pop_values.append({'date' : str(datetime.datetime.utcfromtimestamp(weather_tag['dt'])) ,'pop' : weather_tag['pop']})
        return pop_values[0]

