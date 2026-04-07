import requests
from bs4 import BeautifulSoup

URL = "https://gaana.com/charts/top-songs/weekly"
session = requests.Session()
response = session.get(URL)
html_data = BeautifulSoup(response.text,'lxml')
search_list = []
data = html_data.find('div',class_="top-chart")
div_tag = data.find_all_next("div",class_= "cardDetail")
try:
    for div in div_tag:
        search_list.append(div.find("h3").text)
    print("Search list was built successfully.")
except Exception as e:
    print("Something went wrong building search list.\nDetails:\n",e,"\n")
