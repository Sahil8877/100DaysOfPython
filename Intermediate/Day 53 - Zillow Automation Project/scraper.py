from bs4 import BeautifulSoup
import requests
import re


session = requests.Session()
URL = "https://appbrewery.github.io/Zillow-Clone/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}

webpage = session.get(url=URL,headers=headers)

soup = BeautifulSoup(webpage.text,from_encoding="html.parser")
def get_listings():
    try:
        property_list_element = soup.select("article[data-test='property-card']")

        dict_of_properties = {}

        for links in property_list_element[:5]:
            property_links = links.select_one("a[data-test='property-card-link']").get("href")

            price_value = links.select_one("span[data-test='property-card-price']").text

            format_price = re.sub(r"[^\$\d]","",price_value)

            property_address = links.select_one("address[data-test='property-card-addr']").text.strip()

            format_address = re.sub(r"\s*(?:\n|\|)+\s*",", ",property_address)
            
            dict_of_properties[format_address] = {"url":property_links,"price":format_price}

        return dict_of_properties
    except Exception as e:
        print("\nError while scraping data\n",e)


