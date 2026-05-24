# Import required libraries for browser automation, waiting for elements,
# handling undetected Chrome, subprocess for version detection, and regex.
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
    # Detects the installed Chrome version on the machine
    # undetected_chromedriver needs this to match the chromedriver binary it downloads
    # Mismatch between Chrome and chromedriver causes silent failures or bot detection
    try:
        result = subprocess.run(
            ["google-chrome", "--version"],
            capture_output=True, text=True
        )
        # Extract the first number sequence before a dot (e.g., "114.0.5735.90" -> 114)
        match = re.search(r'(\d+)\.', result.stdout)
        return int(match.group(1)) if match else None
    except Exception:
        # If Chrome isn't found or command fails, return None – uc will fallback to auto-detection
        return None

#********add a chrome profile********#

# Uncommenting this would persist cookies and login sessions across runs
# Useful for avoiding repeated cookie banners but risks stale sessions
# user_data_dir = os.path.join(os.getcwd(), "complaint_bot")
# chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# Base URL for the weather today page (UK English locale)
# Choosing en-GB ensures consistent temperature units (°C) and date formats
URL = "https://weather.com/en-GB/weather/today"

# List of cities to scrape – mixed global and regional to test cross-locale behaviour
# Order is preserved in output; duplicates would cause overwrites (not prevented)
cities = [
    'London', 'Manchester',       
    'New York', 'Bengaluru',    
    'Paris', 'Berlin',           
    'Mumbai', 'Tokyo',            
    'Sydney', 'Dubai',          
]

def create_driver():
    # Creates a new Chrome instance with settings tuned for stability and anti-detection
    # Called once per scraping run; a long-lived driver sometimes crashes on certain city switches
    options = uc.ChromeOptions()
    options.page_load_strategy = 'eager'       # Stop waiting once DOM is ready, skip heavy ads/analytics
    options.add_argument("--no-sandbox")        # Required in containerised environments (GitHub Actions, Docker)
    options.add_argument("--disable-dev-shm-usage")  # Avoids shared memory crashes in low-RAM CI runners
    options.add_argument("--shm-size=2gb")      # Allocates enough memory to prevent renderer crashes
    options.add_argument("--window-size=1920,1080")  # Common resolution to avoid mobile/responsive layouts
    options.add_argument("--disable-gpu")       # Prevents graphical crashes in headless environments
    options.add_argument("--lang=en-GB")        # Forces British English – affects date format and temperature units
    options.add_argument(
        "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
    )  # Modern Chrome UA – without it some sites serve degraded or mobile versions
    driver = uc.Chrome(options=options, version_main=get_chrome_major_version())
    driver.set_page_load_timeout(90)  # Generous timeout for slow connections; avoid infinite hangs
    return driver

def get_weather_data(list_of_cities, retry=True):
    # Scrapes temperature and humidity for each city from weather.com
    # Returns a dictionary: {city: {'temp': int, 'humi': int}}
    # Implements a single retry on failure with a fresh driver (handles temp search box staleness)
    driver = None
    weather_today = {}

    try:
        driver = create_driver()
        webdriver_wait = WebDriverWait(driver, 10)  # 10s is usually enough; increase if network is slow
        driver.get(URL)

        # ---- Handle cookie consent banner (appears inside an iframe on first visit) ----
        try:
            # Wait for the consent iframe to be present and switch into it
            webdriver_wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='SP Consent Message']")))
            # Click the "Accept all" button – without this the search box may be hidden
            accept_cookie_btn = webdriver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Accept all']")))
            accept_cookie_btn.click()
        except Exception as e:
            # Cookie banner may not appear if previously accepted (e.g., with persistent profile)
            # Or if the page structure changed; we continue anyway
            print('Cookie banner not found or some error occured.\n', e)
        finally:
            # Always switch back to the main page content after handling the iframe
            # Failing to do this makes future element searches fail because they are outside the iframe
            try:
                driver.switch_to.default_content() 
            except:
                pass
            time.sleep(2)  # Allow the page to settle after cookie dismissal

        # Wait for the search input box to be clickable – this confirms the page is fully interactive
        # The input box is used repeatedly; waiting once at the start saves time per city
        webdriver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input")))

        # ---- Loop through each city and extract weather data ----
        for city in list_of_cities:
            # Locate the search input field (same element reused each iteration)
            
            # We re-fetch it each time because the DOM may be replaced after navigating to a city page
            search_box = driver.find_element(By.CSS_SELECTOR, "input")
            # Type the city name – no clearing needed because the input is replaced on page navigation
            search_box.send_keys(city)
            time.sleep(2)  # Short pause for autocomplete dropdown; 2s is empirically safe

            # Find the search button – data-testid starts with 'ctaButton' (unique selector)
            search_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid^='ctaButton']")
            search_button.click()
            time.sleep(2)  # Wait for the city weather page to load fully

            # Locate the section that contains today's weather details
            
            # 'data-testid' attribute starts with 'TodaysDetailsModule' – stable across page variants
            weather_data_section = driver.find_element(By.CSS_SELECTOR, "section[data-testid^='TodaysDetailsModule']")
            # Within that section, find the element showing temperature (remove degree symbol)
            temperature = weather_data_section.find_element(By.CSS_SELECTOR, "span[data-testid^='TemperatureValue']")
            
            # Within that section, find the element showing humidity (remove percent sign)
            humidity = weather_data_section.find_element(By.CSS_SELECTOR, "span[data-testid^='PercentageValue']")
            # Store the data as integers for easy numeric comparison later
            weather_today[city] = {'temp': int(temperature.text.replace('°', '')),'humi': int(humidity.text.replace('%', ''))}

    except Exception as e:
        print(f"Error: {e}")
        if retry:
            # If this was the first attempt (retry=True), try once more with a clean driver
            # This handles transient failures like stale element references or network glitches
            print("Retrying with fresh driver...") 
            if driver:
                try:
                    driver.quit()
                except:
                    pass
            # Recursive call with retry=False to avoid infinite loops
            return get_weather_data(list_of_cities, retry=False)

    finally:
        # Ensure the browser is closed even if an error occurred
        # Important for CI environments where leaving drivers open consumes memory
        if driver:
            try:
                driver.quit()
            except:
                pass

    return weather_today

def weather_complainer(weather_data):
    # Generate a list of complaint strings based on the scraped weather data
    # Complains if temperature > 30°C or humidity > 70% for any city
    # Returns a list of descriptive complaint messages – each is a short, human-readable string
    weather_complaints = []
    for city, data in weather_data.items():
        if data['temp'] > 30:
            weather_complaints.append(f"{city}'s {data['temp']} degree temperature")
        elif data['humi'] > 70:
            weather_complaints.append(f"{city}'s {data['humi']}% humidity")
    return weather_complaints