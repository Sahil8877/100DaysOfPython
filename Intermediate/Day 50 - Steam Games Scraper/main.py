from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

user_data_dir = os.path.join(os.getcwd(), "steam")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

URL = "https://store.steampowered.com/specials"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url = URL)

webdriver_wait = WebDriverWait(driver,timeout=10)
sales_panel_load = EC.presence_of_element_located((By.ID,"SaleSection_13268"))
webdriver_wait.until(sales_panel_load)
sales_panel = driver.find_element(By.CSS_SELECTOR,"div.sale_item_browser")

games_data_load = EC.presence_of_element_located((By.CSS_SELECTOR,"div.LibraryAssetExpandedDisplay"))
webdriver_wait.until(games_data_load)

##Scroll steam pages by clicking on 'Show more' button
MAX_SCROLL = 3
scroll_counter = 0
print("\nScrolling Pages!\n")
while scroll_counter != MAX_SCROLL:
    try:
        button_element = sales_panel.find_element(By.CSS_SELECTOR,"button.Focusable")
        button_element.click()
        scroll_counter+=1
        print(f'On Page : {scroll_counter}')
        time.sleep(1)
    except:
        break

games = sales_panel.find_elements(By.CSS_SELECTOR,"div.LibraryAssetExpandedDisplay")

scraped_data = []

##Scrape required game data
print("\nScraping Games!\n")
for titles in games:

    time.sleep(1)
    try:
        title_name = titles.find_element(By.CSS_SELECTOR,"div.ImpressionTrackedElement img")
        title_price = titles.find_element(By.XPATH,".//*[contains(@class,'StoreSalePriceWidgetContainer')]")
    
        try:
            title_review = titles.find_element(By.CSS_SELECTOR,".ReviewScore").text.split('\n')[0]
        except:
            title_review = None
        
        if title_price.text.split('\n')[0] == 'NEW':
            isNew = True
            title_price_discount = int(title_price.text.split('\n')[1].replace('-','').replace('%',''))
            title_price_old = round(float(title_price.text.split('\n')[2].replace('£','')),2)
            title_price_new = round(float(title_price.text.split('\n')[3].replace('£','')),2)
        else:
            isNew = False
            title_price_discount = int(title_price.text.split('\n')[0].replace('-','').replace('%',''))
            title_price_old = round(float(title_price.text.split('\n')[1].replace('£','')),2)
            title_price_new = round(float(title_price.text.split('\n')[2].replace('£','')),2)
    

        scraped_data.append(
            {
                'TitleName':title_name.get_attribute('alt'),
                'DiscountPercent':title_price_discount,
                'OldPrice':title_price_old,
                'NewPrice':title_price_new,
                'Review': title_review,
                'isNew' : isNew
            }
        )
        print('Scraped : ',title_name.get_attribute('alt'))
    except NoSuchElementException as e:
        print('Element was not found in DOM.',e)

driver.quit()
print(f"Total games scraped {len(scraped_data)}!")

##prepare csv with filtering
field_names = ['TitleName','DiscountPercent','OldPrice','NewPrice','Review','isNew']
final_data = [data for data in scraped_data if data['DiscountPercent'] > 80 and data['NewPrice'] <= 10 and data['Review'] in ['Very Positive','Mostly Positive','Overwhelmingly Positive']]

try:
    with open('DiscountedGames.csv','w') as file:
        writer = csv.DictWriter(file,fieldnames=field_names)
        writer.writeheader()
        writer.writerows(final_data)

    print(f"\nYour CSV file is now ready with {len(final_data)} games!")
except Exception as e:
    print("\nYour CSV file generation failed!",e)