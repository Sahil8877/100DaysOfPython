import data
import statistics

def check_weather_for_rain():

    previous_state = None
    fetch_weather_data = data.WeatherData()
    minutely_data = fetch_weather_data.minutely_forecast()
    sum_of_precipitation = []
    send_alert = False
    light_rain_count = 0
    moderate_rain_count = 0
    heavy_rain_count = 0

    try:
        with open('previous_state.txt','r') as file:
            previous_state = file.read()
    except FileNotFoundError as exception:
        print("File doesnt exist!")

    for minute in minutely_data[:30]:
        print(minute['precipitation'])
        if minute['precipitation'] >= 0.1:
            rain_level_mm = minute['precipitation'] #for mm/hr
            print('rain_level_mm :',rain_level_mm)
            sum_of_precipitation.append(rain_level_mm)
            if 1 <= rain_level_mm < 3:
                light_rain_count += 1
            elif 3 <= rain_level_mm < 8:
                moderate_rain_count += 1
            elif rain_level_mm >= 8:
                heavy_rain_count += 1

    if len(sum_of_precipitation) > 0:
        median_intensity_over_next30 = statistics.median(sum_of_precipitation)
    else:
        median_intensity_over_next30 = 0

    pop_value = fetch_weather_data.hourly_pop()

    print(f"light_rain_count = {light_rain_count}\nmoderate_rain_count = {moderate_rain_count}\nheavy_rain_count = {heavy_rain_count}\npop = {pop_value['pop']}\navg_intensity_over_next30 = {avg_intensity_over_next30}")


    if heavy_rain_count >= 5 and median_intensity_over_next30 >= 8 and pop_value['pop'] >= 0.80:
        
        alert = "Heavy Rain Alert"
        if previous_state != alert:
            previous_state = alert
            send_alert = True
        print("Heavy Rain Alert")
    elif moderate_rain_count >= 5 and median_intensity_over_next30 >= 6 and pop_value['pop'] >= 0.50:
        
        alert = "Moderate Rain Alert"
        if previous_state != alert:
            previous_state = alert
            send_alert = True
        print("Moderate Rain Alert")
    elif light_rain_count >= 5 and median_intensity_over_next30 >= 2 and pop_value['pop'] >= 0.20:
        
        alert = "Light Rain Alert"
        if previous_state != alert:
            previous_state = alert
            send_alert = True
        print("Light Rain Alert")
    else:
        alert = "No Significant Rain"
        if previous_state != alert:
            previous_state = alert
            send_alert = True
        print("No Significant Rain")
    return alert, send_alert
