from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time, os

URL = 'https://appbrewery.github.io/gym/'



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

user_data_dir = os.path.join(os.getcwd(), "gym_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

#click join today btn..
join_btn = driver.find_element(By.CSS_SELECTOR,".Home_heroButton__3eeI3")
join_btn.click()

#login using credentials
ACCOUNT_EMAIL = "sahil@test.com"
ACCOUNT_PASSWORD = "Sahil@@123"
#find email textbox using name attr
email_input = driver.find_element(By.CSS_SELECTOR,value="#email-input")
email_input.send_keys(ACCOUNT_EMAIL)
#find password textbox using name attr
pass_input = driver.find_element(By.CSS_SELECTOR,value="#password-input")
pass_input.send_keys(ACCOUNT_PASSWORD)
#submit login btn
login_btn = driver.find_element(By.CSS_SELECTOR,value="#submit-button")
login_btn.submit()

