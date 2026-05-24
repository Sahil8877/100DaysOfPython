from complain_writer import response
from weather_checker import weather_complainer, get_weather_data, cities
from down_detector import downdetector_complainer, get_downdetector_data, companies_to_check
from twitter import post_tweets

down_detector_data = get_downdetector_data(companies_to_check)
down_detector_complaints_list = downdetector_complainer(down_detector_data)

weather_data = get_weather_data(cities)
weather_complaints_list = weather_complainer(weather_data)

if down_detector_complaints_list:  # if there are outages
    down_detector_tweets = response(down_detector_complaints_list, "website down")
    post_tweets(down_detector_tweets)
    print(down_detector_tweets, "\n")
else:
    print("No outages detected.")

if weather_complaints_list:        # if weather thresholds are met
    weather_tweets = response(weather_complaints_list, "weather")
    post_tweets(weather_tweets)
    print(weather_tweets)
else:
    print("No notable weather conditions.")