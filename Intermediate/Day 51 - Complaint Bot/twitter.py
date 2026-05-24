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
import os

def get_chrome_major_version():
    commands = [
        ["google-chrome", "--version"],
        ["google-chrome-stable", "--version"],
        ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"],
    ]
    for cmd in commands:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            match = re.search(r'(\d+)\.', result.stdout)
            if match:
                return int(match.group(1))
        except Exception:
            continue
    return None

URL = 'https://x.com/'

def post_tweets(complaints):
    driver = None
    try:
        options = uc.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--shm-size=2gb")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--lang=en-GB")

        # Realistic user agent based on actual Chrome version
        chrome_version = get_chrome_major_version()
        if chrome_version:
            user_agent = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36"
        else:
            user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        options.add_argument(f"--user-agent={user_agent}")

        # Anti-detection
        options.add_argument("--disable-blink-features=AutomationControlled")

        driver = uc.Chrome(options=options, version_main=chrome_version)
        driver.set_page_load_timeout(60)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        webdriver_wait = WebDriverWait(driver, 10)
        driver.get('https://x.com/')

        # ---- STEP 1: Enter username/email ----
        username_input = webdriver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='username']")))
        username_input.send_keys(os.getenv('X_PASS_EMAIL'))

        # ---- Click the "Continue" button (using the class 'j-pmlt8x0' from the current X login page) ----
        continue_btn = webdriver_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'j-pmlt8x0') and .//div[text()='Continue']]")))
        continue_btn.click()

        # ---- STEP 2: Enter password ----
        password_input = webdriver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
        password_input.send_keys(os.getenv("X_PASS"))

        # ---- Click the "Log in" button ----
        login_btn = webdriver_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'j-pmlt8x0') and .//div[text()='Log in']]")))
        login_btn.click()

        # ---- Wait for home page to load ----
        time.sleep(5)

        # ---- Check for verification ----
        if "verify" in driver.page_source.lower() or "we sent a code" in driver.page_source.lower():
            print("⚠️ Verification required. Cannot proceed.")
            driver.save_screenshot("verification_needed.png")
            return

        # ---- Debug save after login ----
        try:
            with open("after_login.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            driver.save_screenshot("after_login.png")
        except Exception as e:
            print(f"Could not save post-login state: {e}")

        # ---- Post complaints ----
        for idx, complaint in enumerate(complaints):
            try:
                # Wait for tweet compose box (the classic selector – may need update)
                textbox = webdriver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".public-DraftStyleDefault-block")))
                textbox.click()
                textbox.send_keys(complaint.strip('"'))
                time.sleep(2)
                tweet_btn = webdriver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']")))
                driver.execute_script("arguments[0].click();", tweet_btn)
                time.sleep(2)
            except Exception as tweet_err:
                print(f"Failed to post complaint {idx}: {complaint[:50]}... Error: {tweet_err}")
                driver.save_screenshot(f"error_tweet_{idx}.png")

    except Exception as e:
        print(f"Error in main block: {e}")
        if driver:
            timestamp = int(time.time())
            driver.save_screenshot(f"error_{timestamp}.png")
            with open(f"error_{timestamp}.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
    finally:
        if driver:
            driver.quit()