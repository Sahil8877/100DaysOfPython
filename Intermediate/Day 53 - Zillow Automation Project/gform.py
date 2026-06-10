from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chromium.options import ChromiumOptions
import undetected_chromedriver as uc
import time

options = ChromiumOptions()

options.add_argument(f"--user-data-dir='Zillow Automation Project'")
options.add_argument("--profile-directory=Default")

driver = uc.Chrome(options=options)

URL = "https://forms.gle/2YzcByGjLv3rdrZU7"

def populate_sheet(data):
    try:
        driver.get(url=URL)
        wait = WebDriverWait(driver,5)
        WebDriverWait.until(wait,EC.visibility_of_element_located(((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))))
        for key,value in data.items():
            print(key,value,"\n")
            input_address = driver.find_element(By.XPATH,'/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            input_address.send_keys(key)
            time.sleep(1)
            input_price = driver.find_element(By.XPATH,'/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            input_price.send_keys(value['price'])
            time.sleep(1)
            input_link = driver.find_element(By.XPATH,'/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            input_link.send_keys(value['url'])
            time.sleep(1)
            submit_btn = driver.find_element(By.XPATH,'/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit_btn.click()
            time.sleep(1)
            driver.get(url=URL)
            wait = WebDriverWait(driver,5)
            WebDriverWait.until(wait,EC.visibility_of_element_located(((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))))
        
        driver.quit()
    except Exception as e:
        print("\nError while scraping data\n",e)