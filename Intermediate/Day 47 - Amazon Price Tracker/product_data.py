import requests
from bs4 import BeautifulSoup

class GetProductData:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "en-GB,en;q=0.8"
        }

        response = self.session.get(self.url, headers=self.headers)

        if response.status_code != 200:
            raise Exception("Failed to fetch page")

        if "captcha" in response.text.lower():
            raise Exception("Blocked by Amazon")

        self.html_data = BeautifulSoup(response.text, "html.parser")

    def parse_price_data(self):
        try:
            price = self.html_data.select_one('.a-price .a-offscreen')
            return float(price.text.replace('£', '').replace(',', ''))
        except:
            return None

    def parse_item_name(self):
        title = self.html_data.select_one('#productTitle')
        return title.text.strip() if title else None


product = GetProductData("https://www.amazon.co.uk/PlayStation-5-Digital-Console-Slim/dp/B0CM9VKQ5N/ref=pd_vtp_d_sccl_1_1/521-8021042-6135048?pd_rd_w=CqBbb&content-id=amzn1.sym.e1b012f9-a2d8-4786-8113-bd0f31ac121d&pf_rd_p=e1b012f9-a2d8-4786-8113-bd0f31ac121d&pf_rd_r=C8WFZ5GNJPCK8JKS9FNK&pd_rd_wg=JYrwQ&pd_rd_r=af51f9ce-13af-4ec5-96f4-e7404503492b&pd_rd_i=B0CM9VKQ5N&psc=1")

print(product.parse_item_name())
print(product.parse_price_data())