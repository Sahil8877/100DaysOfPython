from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chromium import options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import complain_writer
import os,time

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

# user_data_dir = os.path.join(os.getcwd(), "complaint_bot")
# chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

URL = "https://weather.com/en-GB/weather/today"

driver = webdriver.Chrome(options=chrome_options)
webdriver_wait = WebDriverWait(driver,10)
driver.get(URL)

uk_cities = ['London','Glasgow']

def get_weather_data(list_of_cities):
    weather_today = {}
    time.sleep(2)
    
    webdriver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input")))
    try: 
        for cities in list_of_cities:
            
            search_box = driver.find_element(By.CSS_SELECTOR,"input")
            search_box.send_keys(cities)
            time.sleep(2)

            # webdriver_wait.until(EC.visibility_of_element_located(((By.CSS_SELECTOR,"#headerSearch_LocationSearch_listbox"))))
            search_button = driver.find_element(By.CSS_SELECTOR,"button[data-testid^='ctaButton']")
            search_button.click()
            time.sleep(2)

            # webdriver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#todayDetails")))
            weather_data_section = driver.find_element(By.CSS_SELECTOR,"section[data-testid^='TodaysDetailsModule']")
            temperature = weather_data_section.find_element(By.CSS_SELECTOR,"span[data-testid^='TemperatureValue']")
            humidity = weather_data_section.find_element(By.CSS_SELECTOR,"span[data-testid^='PercentageValue']")
            weather_today[cities] = {'temp' : int(temperature.text.replace('°','')),'humi' : int(humidity.text.replace('%',''))}

    except Exception as e:
        print('Error',e)
        driver.quit()
      
    return weather_today

def weather_complainer(weather_data):
    weather_complaints = []
    for city,data in weather_data.items():
        if data['temp'] > 3:
            weather_complaints.append(f"{city}'s {data['temp']} degree temperature")
        elif data['humi'] > 7:
            weather_complaints.append(f"{city}'s {data['humi']}% humidity")
    print("hi",weather_complaints)
    return weather_complaints

webdriver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[title='Accept all']")) )

complain_writer.response(weather_complainer(get_weather_data(uk_cities)),"weather")

driver.quit()