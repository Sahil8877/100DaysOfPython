from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chromium import options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
import subprocess
import re

def get_chrome_major_version():
    try:
        result = subprocess.run(
            ["google-chrome", "--version"],
            capture_output=True, text=True
        )
        match = re.search(r'(\d+)\.', result.stdout)
        return int(match.group(1)) if match else None
    except Exception:
        return None

#********add a chrome profile********# 
# user_data_dir = os.path.join(os.getcwd(), "complaint_bot")
# chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

URL = "https://weather.com/en-GB/weather/today"

cities = [
    # 🇬🇧 UK
    'London', 'Glasgow', 'Manchester', 'Birmingham', 'Edinburgh',
    'Liverpool', 'Leeds', 'Bristol', 'Sheffield', 'Newcastle',

    # 🇺🇸 USA
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',
    'San Francisco', 'Seattle', 'Boston', 'Dallas', 'Atlanta',

    # 🇪🇺 Europe
    'Paris', 'Berlin', 'Madrid', 'Rome', 'Amsterdam',
    'Barcelona', 'Vienna', 'Stockholm', 'Oslo', 'Zurich',

    # 🇮🇳 India
    'Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata',

    # 🇦🇺 Australia
    'Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide',

    # 🇨🇦 Canada
    'Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Ottawa',

    # 🌏 Asia
    'Tokyo', 'Seoul', 'Shanghai', 'Singapore', 'Hong Kong',
    'Bangkok', 'Kuala Lumpur', 'Jakarta', 'Dubai', 'Riyadh',

    # 🌍 Africa & Middle East
    'Cairo', 'Lagos', 'Nairobi', 'Johannesburg', 'Casablanca',

    # 🌎 Latin America
    'Sao Paulo', 'Buenos Aires', 'Mexico City', 'Bogota', 'Lima',
]

def create_driver():
    options = uc.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--shm-size=2gb")
    options.add_argument("--single-process")
    options.add_argument("--no-zygote")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-background-networking")
    options.add_argument("--lang=en-GB")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
    )
    driver = uc.Chrome(options=options, version_main=get_chrome_major_version())
    driver.set_page_load_timeout(90)
    return driver

def get_weather_data(list_of_cities, retry=True):
    driver = None
    weather_today = {}

    try:
        driver = create_driver()
        webdriver_wait = WebDriverWait(driver, 10)
        driver.get(URL)

        try:
            webdriver_wait.until(EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[title='SP Consent Message']")
            ))
            accept_cookie_btn = webdriver_wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[title='Accept all']")
            ))
            accept_cookie_btn.click()
        except Exception as e:
            print('Cookie banner not found or some error occured.\n', e)
        finally:
            try:
                driver.switch_to.default_content()  # ✅ wrapped in try in case driver is dead
            except:
                pass
            time.sleep(2)

        webdriver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input")))

        for city in list_of_cities:
            search_box = driver.find_element(By.CSS_SELECTOR, "input")
            search_box.send_keys(city)
            time.sleep(2)

            search_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid^='ctaButton']")
            search_button.click()
            time.sleep(2)

            weather_data_section = driver.find_element(By.CSS_SELECTOR, "section[data-testid^='TodaysDetailsModule']")
            temperature = weather_data_section.find_element(By.CSS_SELECTOR, "span[data-testid^='TemperatureValue']")
            humidity = weather_data_section.find_element(By.CSS_SELECTOR, "span[data-testid^='PercentageValue']")
            weather_today[city] = {
                'temp': int(temperature.text.replace('°', '')),
                'humi': int(humidity.text.replace('%', ''))
            }

    except Exception as e:
        print(f"Error: {e}")
        if retry:
            print("Retrying with fresh driver...")  # ✅ one retry on failure
            if driver:
                try:
                    driver.quit()
                except:
                    pass
            return get_weather_data(list_of_cities, retry=False)

    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass

    return weather_today

def weather_complainer(weather_data):
    weather_complaints = []
    for city, data in weather_data.items():
        if data['temp'] > 30:
            weather_complaints.append(f"{city}'s {data['temp']} degree temperature")
        elif data['humi'] > 70:
            weather_complaints.append(f"{city}'s {data['humi']}% humidity")
    return weather_complaints