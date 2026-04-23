from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
count = driver.find_element(by=By.ID,value='articlecount')
c = count.find_element(By.CSS_SELECTOR("a[title='Special:Statistics']"))
print(c)

driver.quit()