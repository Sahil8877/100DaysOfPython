import platform
import subprocess
import re
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

def get_chrome_major_version():
    """
    Detect the installed Chrome major version on Windows, macOS, or Linux.
    Returns an integer (e.g., 134) or a fallback (134) if detection fails.
    """
    system = platform.system()
    commands = []

    if system == "Windows":
        # Try to read from registry (most reliable)
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon")
            version, _ = winreg.QueryValueEx(key, "version")
            return int(version.split('.')[0])
        except:
            # Fallback to common install paths
            commands = [
                [r"C:\Program Files\Google\Chrome\Application\chrome.exe", "--version"],
                [r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "--version"],
            ]
    elif system == "Darwin":
        commands = [["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"]]
    else:  # Linux and others
        commands = [
            ["google-chrome", "--version"],
            ["google-chrome-stable", "--version"],
        ]

    for cmd in commands:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, shell=(system == "Windows"))
            match = re.search(r'(\d+)\.', result.stdout)
            if match:
                return int(match.group(1))
        except:
            continue

    # Fallback to a known stable version (update as needed)
    return 134


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

        # ---- Realistic user agent based on actual Chrome version ----
        chrome_version = get_chrome_major_version()
        if chrome_version:
            user_agent = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36"
        else:
            user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        options.add_argument(f"--user-agent={user_agent}")

        # ---- Basic anti‑detection (undetected_chromedriver already handles most) ----
        options.add_argument("--disable-blink-features=AutomationControlled")

        # REMOVED the problematic experimental options:
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)

        driver = uc.Chrome(options=options, version_main=chrome_version)
        driver.set_page_load_timeout(60)

        # Remove the webdriver property (helps with detection)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        webdriver_wait = WebDriverWait(driver, 10)
        driver.get('https://x.com/')

        # ---- Step 1: Enter username/email and click "Continue" ----
        username_input = webdriver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='username']")))
        username_input.send_keys(os.getenv('X_PASS_EMAIL'))

        # The "Continue" button is now a <div role="button"> with text "Continue"
        continue_btn = webdriver_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button']//div[text()='Continue']")))
        continue_btn.click()

        # ---- Step 2: Enter password and click "Log in" ----
        password_input = webdriver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
        password_input.send_keys(os.getenv("X_PASS"))

        login_btn = webdriver_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button']//div[text()='Log in']")))
        login_btn.click()

        # ---- Step 3: Handle possible verification challenges ----
        time.sleep(3)
        if "verify" in driver.page_source.lower() or "we sent a code" in driver.page_source.lower():
            print("⚠️ Verification required (CAPTCHA, email code, etc.). Cannot proceed automatically.")
            driver.save_screenshot("verification_required.png")
            return  # Stop execution – manual intervention needed

        # ---- Debug: Save post-login state ----
        try:
            with open("after_login.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            print("Page source saved to after_login.html")
            screenshot_path = os.path.join(os.getcwd(), "after_login.png")
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
        except Exception as debug_err:
            print(f"Failed to save post-login debug artifacts: {debug_err}")

        # ---- Post each complaint ----
        for idx, complaint in enumerate(complaints):
            try:
                time.sleep(2)
                # Wait for the tweet compose box (selector may change; this is the classic one)
                textbox = webdriver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".public-DraftStyleDefault-block")))
                textbox.send_keys(complaint.strip('"'))
                time.sleep(2)
                tweet_btn = webdriver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']")))
                driver.execute_script("arguments[0].click();", tweet_btn)
                time.sleep(2)
            except Exception as tweet_err:
                print(f"Failed to post complaint {idx}: {complaint[:50]}... Error: {tweet_err}")
                try:
                    driver.save_screenshot(f"error_tweet_{idx}.png")
                    with open(f"error_tweet_{idx}.html", "w", encoding="utf-8") as f:
                        f.write(driver.page_source)
                    print(f"Saved error_tweet_{idx}.png and .html")
                except:
                    pass
                continue

    except Exception as e:
        print("Error occurred in main block:\n", e)
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