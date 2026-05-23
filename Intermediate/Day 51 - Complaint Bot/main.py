from complain_writer import response
from weather_checker import weather_complainer, get_weather_data, uk_cities
from down_detector import downdetector_complainer, get_downdetector_data, companies_to_check

down_detector_complaints_list = downdetector_complainer(get_downdetector_data(companies_to_check))
weather_complaints_list = weather_complainer(get_weather_data(uk_cities))

down_detector_tweets = response(down_detector_complaints_list,"website down")
weather_tweets = response(weather_complaints_list,"weather")

print(down_detector_tweets,"\n")
print(weather_tweets)
