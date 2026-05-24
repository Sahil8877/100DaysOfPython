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
        options.add_argument(
            "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
        )

        driver = uc.Chrome(options=options, version_main=get_chrome_major_version())
        driver.set_page_load_timeout(60)
        webdriver_wait = WebDriverWait(driver, 10)
        driver.get(URL)

        username_input_element = webdriver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='username']")))
        username_input_element.send_keys(os.getenv('X_PASS_EMAIL'))

        continue_button = webdriver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        continue_button.click()
        time.sleep(5)
        password_input_element = webdriver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
        password_input_element.send_keys(os.getenv("X_PASS"))

        continue_button = webdriver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        continue_button.click()
        time.sleep(3)

        # Save post-login state (only if login succeeded)
        try:
            with open("after_login.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            print("Page source saved to after_login.html")
            screenshot_path = os.path.join(os.getcwd(), "after_login.png")
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
            print(f"File exists: {os.path.exists('after_login.png')}")
        except Exception as debug_err:
            print(f"Failed to save post-login debug artifacts: {debug_err}")

        # Post each complaint
        for idx, complaint in enumerate(complaints):
            try:
                time.sleep(2)
                textbox_element = webdriver_wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".public-DraftStyleDefault-block")
                ))
                textbox_element.send_keys(complaint.strip('"'))
                time.sleep(2)
                tweet_button = webdriver_wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']")
                ))
                driver.execute_script("arguments[0].click();", tweet_button)
                time.sleep(2)
            except Exception as tweet_err:
                print(f"Failed to post complaint {idx}: {complaint[:50]}... Error: {tweet_err}")
                # Save error state for this specific tweet failure
                try:
                    driver.save_screenshot(f"error_tweet_{idx}.png")
                    with open(f"error_tweet_{idx}.html", "w", encoding="utf-8") as f:
                        f.write(driver.page_source)
                    print(f"Saved error_tweet_{idx}.png and .html")
                except:
                    pass
                # Continue with next complaint instead of aborting entire loop
                continue

    except Exception as e:
        print("Error occurred in main block:\n", e)
        # Save critical error state with timestamp to avoid overwriting
        if driver:
            try:
                timestamp = int(time.time())
                driver.save_screenshot(f"error_{timestamp}.png")
                with open(f"error_{timestamp}.html", "w", encoding="utf-8") as f:
                    f.write(driver.page_source)
                print(f"Saved error_{timestamp}.png and .html for debugging")
            except Exception as save_err:
                print(f"Could not save error artifacts: {save_err}")

    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass