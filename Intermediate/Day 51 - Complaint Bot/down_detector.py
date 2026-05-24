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
        match = re.search(r'(\d+)\.', result.stdout)
        return int(match.group(1)) if match else None
    except Exception:
        return None

#********add a chrome profile********#
# Uncommenting this would persist cookies and login sessions across runs
# Useful for avoiding repeated cookie banners but risks stale sessions
# user_data_dir = os.path.join(os.getcwd(), "complaint_bot")
# chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# Services to monitor for outages
# Mixed between downdetector.com (global) and downdetector.co.uk (UK specific)
# Kept at 20 intentionally - GitHub Actions free runners crash Chrome beyond this
companies_to_check = [
    # Global
    # {'Google'        : 'https://downdetector.com/status/google/'},
    # {'YouTube'       : 'https://downdetector.com/status/youtube/'},
    # {'Facebook'      : 'https://downdetector.com/status/facebook/'},
    # {'Instagram'     : 'https://downdetector.com/status/instagram/'},
    # {'WhatsApp'      : 'https://downdetector.com/status/whatsapp/'},
    # {'Amazon'        : 'https://downdetector.com/status/amazon/'},
    # {'Netflix'       : 'https://downdetector.com/status/netflix/'},
    # {'Spotify'       : 'https://downdetector.com/status/spotify/'},
    # # Gaming
    # {'Steam'         : 'https://downdetector.com/status/steam/'},
    # {'Apex Legends'  : 'https://downdetector.com/status/apex-legends/'},
    # # UK
    # {'Virgin Media'  : 'https://downdetector.co.uk/status/virgin-media/'},
    # {'BT'            : 'https://downdetector.co.uk/status/bt-british-telecom/'},
    # {'Sky'           : 'https://downdetector.co.uk/status/sky/'},
    # {'Vodafone UK'   : 'https://downdetector.co.uk/status/vodafone/'},
    # {'Barclays'      : 'https://downdetector.co.uk/status/barclays/'},
    # {'Monzo'         : 'https://downdetector.co.uk/status/monzo/'},
    # {'BBC iPlayer'   : 'https://downdetector.co.uk/status/iplayer/'},
    # {'Deliveroo'     : 'https://downdetector.co.uk/status/deliveroo/'},
    # # US
    # {'AT&T'          : 'https://downdetector.com/status/att/'},
    # {'Verizon'       : 'https://downdetector.com/status/verizon/'},
]

def create_driver():
    # Creates a new Chrome instance with settings tuned for GitHub Actions
    # Called per batch so each batch starts with a clean browser state
    # A single long-running driver crashes due to memory exhaustion in CI
    options = uc.ChromeOptions()
    options.page_load_strategy = 'eager'       # Stop waiting once DOM is ready, skip ads/analytics loading
    options.add_argument("--no-sandbox")        # Required in containerised CI environments
    options.add_argument("--disable-dev-shm-usage")  # Avoids shared memory crashes in Docker/CI
    options.add_argument("--shm-size=2gb")      # Allocates enough memory to prevent renderer crashes
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")       # Prevents graphical crashes in headless environments
    options.add_argument("--lang=en-GB")        # Ensures consistent language on downdetector pages
    options.add_argument(
        "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
    )
    driver = uc.Chrome(options=options, version_main=get_chrome_major_version())
    driver.set_page_load_timeout(90)  # Generous timeout for slow CI network conditions
    return driver

def get_downdetector_data(list_of_companies):
    down_today = {}

    # Process companies in batches with a fresh driver per batch
    # Without batching, Chrome accumulates memory and crashes mid-run in GitHub Actions
    # batch_size of 10 is the safe ceiling for free runners (2 CPU, 7GB RAM)
    batch_size = 10

    for i in range(0, len(list_of_companies), batch_size):
        batch = list_of_companies[i:i + batch_size]
        driver = None
        try:
            driver = create_driver()
            webdriver_wait = WebDriverWait(driver, 10)

            for org_data in batch:
                for org_name in org_data:
                    try:
                        driver.get(org_data.get(org_name))

                        # Wait for the status banner to appear before reading it
                        # This is the main element that tells us if a service is down
                        webdriver_wait.until(EC.visibility_of_element_located(
                            (By.CSS_SELECTOR, "#company-status")
                        ))
                        time.sleep(2)

                        # Dismiss cookie banner if present
                        # Wrapped in try/except as it only appears on first visit per domain
                        try:
                            cookie_button = driver.find_element(By.CSS_SELECTOR, "button[id^='onetrust-accept-btn-handler']")
                            cookie_button.click()
                        except:
                            pass

                        time.sleep(2)

                        banner_element = driver.find_element(By.CSS_SELECTOR, "#company-status")
                        banner_element_attr_color = banner_element.get_attribute('class')

                        # Downdetector uses CSS border colour to indicate outage severity
                        # dd-red = active outage, dd-blue = normal, dd-yellow = warning
                        if 'border-[var(--color-dd-red)]' in banner_element_attr_color:
                            data_card_element = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Most reported problems breakdown']")
                            reported_problems = data_card_element.find_elements(By.CSS_SELECTOR, "div[role='listitem']")
                            reported_data_dict = {}

                            for reports in reported_problems:
                                reported_data = reports.find_element(By.CSS_SELECTOR, ".relative").text   # percentage
                                reported_text = reports.find_element(By.CSS_SELECTOR, "div.text-center").text  # label
                                reported_data_dict[reported_text] = reported_data

                            down_today[org_name] = {'report': reported_data_dict, 'desc': banner_element.text}
                        else:
                            print(org_name, "has no major outage reported.")

                    except Exception as e:
                        # Log and skip - one bad URL or crash should not stop the rest of the batch
                        print(f"Error on {org_name}: {e}")
                        continue

                    time.sleep(2)  # Brief pause between pages to reduce memory pressure

        except Exception as e:
            print(f"Batch {i // batch_size + 1} error: {e}")
        finally:
            # Always quit the driver to free memory before next batch starts
            if driver:
                try:
                    driver.quit()
                except:
                    pass

    return down_today

def downdetector_complainer(downdetector_data):
    # Converts raw outage data into readable complaint strings for the LLM
    downdetector_complaints = []
    for org, data in downdetector_data.items():
        reports = ",".join([" " + report + " " + data['report'].get(report) for report in data['report']])
        downdetector_complaints.append(f"{org} is down today, outage report by impact is as follows:{reports}.")
    print(downdetector_complaints)
    return downdetector_complaints