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

def get_chrome_major_version():
    try:
        result = subprocess.run(
            ["google-chrome", "--version"],
            capture_output=True, text=True
        )
        match = re.search(r'(\d+)\.', result.stdout)
        return int(match.group(1)) if match else None
    except Exception:
        return None



#********add a chrome profile********# 
# user_data_dir = os.path.join(os.getcwd(), "complaint_bot")
# chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


companies_to_check = [
    # 🌍 Global Tech & Search
    {'Google'           : 'https://downdetector.com/status/google/'},
    {'YouTube'          : 'https://downdetector.com/status/youtube/'},
    {'Facebook'         : 'https://downdetector.com/status/facebook/'},
    {'Instagram'        : 'https://downdetector.com/status/instagram/'},
    {'ChatGPT'          : 'https://downdetector.com/status/chatgpt/'},
    {'Reddit'           : 'https://downdetector.com/status/reddit/'},
    {'Wikipedia'        : 'https://downdetector.com/status/wikipedia/'},
    {'X / Twitter'      : 'https://downdetector.com/status/twitter/'},
    {'WhatsApp'         : 'https://downdetector.com/status/whatsapp/'},
    {'Yahoo'            : 'https://downdetector.com/status/yahoo/'},
    {'Amazon'           : 'https://downdetector.com/status/amazon/'},
    {'TikTok'           : 'https://downdetector.com/status/tiktok/'},
    {'Bing'             : 'https://downdetector.com/status/bing/'},
    {'LinkedIn'         : 'https://downdetector.com/status/linkedin/'},
    {'DuckDuckGo'       : 'https://downdetector.com/status/duckduckgo/'},
    {'Pinterest'        : 'https://downdetector.com/status/pinterest/'},
    {'Snapchat'         : 'https://downdetector.com/status/snapchat/'},
    {'Telegram'         : 'https://downdetector.com/status/telegram/'},
    {'Threads'          : 'https://downdetector.com/status/threads/'},

    # 🎬 Streaming
    {'Netflix'          : 'https://downdetector.com/status/netflix/'},
    {'Disney+'          : 'https://downdetector.com/status/disney-plus/'},
    {'Twitch'           : 'https://downdetector.com/status/twitch/'},
    {'Spotify'          : 'https://downdetector.com/status/spotify/'},
    {'Apple TV+'        : 'https://downdetector.com/status/apple-tv-plus/'},
    {'Amazon Prime'     : 'https://downdetector.com/status/amazon-prime-video/'},
    {'Hulu'             : 'https://downdetector.com/status/hulu/'},
    {'HBO Max'          : 'https://downdetector.com/status/hbo-now/'},

    # 🎮 Gaming
    {'Steam'            : 'https://downdetector.com/status/steam/'},
    {'PlayStation'      : 'https://downdetector.com/status/playstation-network/'},
    {'Xbox'             : 'https://downdetector.com/status/xbox-live/'},
    {'Roblox'           : 'https://downdetector.com/status/roblox/'},
    {'Apex Legends'     : 'https://downdetector.com/status/apex-legends/'},
    {'Fortnite'         : 'https://downdetector.com/status/fortnite/'},
    {'Call of Duty'     : 'https://downdetector.com/status/call-of-duty/'},
    {'Minecraft'        : 'https://downdetector.com/status/minecraft/'},
    {'League of Legends': 'https://downdetector.com/status/league-of-legends/'},
    {'EA'               : 'https://downdetector.com/status/ea/'},
    {'Nintendo'         : 'https://downdetector.com/status/nintendo/'},
    {'Valorant'         : 'https://downdetector.com/status/valorant/'},

    # 💼 Productivity & Cloud
    {'Gmail'            : 'https://downdetector.com/status/gmail/'},
    {'Google Drive'     : 'https://downdetector.com/status/google-drive/'},
    {'Google Maps'      : 'https://downdetector.com/status/google-maps/'},
    {'Microsoft 365'    : 'https://downdetector.com/status/microsoft-office-365/'},
    {'GitHub'           : 'https://downdetector.com/status/github/'},
    {'Zoom'             : 'https://downdetector.com/status/zoom/'},
    {'Slack'            : 'https://downdetector.com/status/slack/'},
    {'Dropbox'          : 'https://downdetector.com/status/dropbox/'},
    {'Cloudflare'       : 'https://downdetector.com/status/cloudflare/'},
    {'AWS'              : 'https://downdetector.com/status/amazon-web-services/'},
    {'iCloud'           : 'https://downdetector.com/status/icloud/'},
    {'Teams'            : 'https://downdetector.com/status/microsoft-teams/'},

    # 💳 Finance & Shopping
    {'PayPal'           : 'https://downdetector.com/status/paypal/'},
    {'eBay'             : 'https://downdetector.com/status/ebay/'},
    {'Coinbase'         : 'https://downdetector.com/status/coinbase/'},
    {'Robinhood'        : 'https://downdetector.com/status/robinhood/'},

    # 🇬🇧 UK Internet & Mobile
    {'Virgin Media'     : 'https://downdetector.co.uk/status/virgin-media/'},
    {'BT'               : 'https://downdetector.co.uk/status/bt/'},
    {'Sky'              : 'https://downdetector.co.uk/status/sky/'},
    {'EE'               : 'https://downdetector.co.uk/status/ee/'},
    {'Vodafone UK'      : 'https://downdetector.co.uk/status/vodafone/'},
    {'O2 UK'            : 'https://downdetector.co.uk/status/o2/'},
    {'Three UK'         : 'https://downdetector.co.uk/status/three/'},
    {'TalkTalk'         : 'https://downdetector.co.uk/status/talktalk/'},
    {'Plusnet'          : 'https://downdetector.co.uk/status/plusnet/'},
    {'Now TV'           : 'https://downdetector.co.uk/status/now-tv/'},

    # 🇬🇧 UK Banking
    {'Barclays'         : 'https://downdetector.co.uk/status/barclays/'},
    {'HSBC'             : 'https://downdetector.co.uk/status/hsbc/'},
    {'Lloyds Bank'      : 'https://downdetector.co.uk/status/lloyds-bank/'},
    {'NatWest'          : 'https://downdetector.co.uk/status/natwest/'},
    {'Monzo'            : 'https://downdetector.co.uk/status/monzo/'},
    {'Revolut'          : 'https://downdetector.co.uk/status/revolut/'},
    {'Starling Bank'    : 'https://downdetector.co.uk/status/starling-bank/'},
    {'Halifax'          : 'https://downdetector.co.uk/status/halifax/'},
    {'Nationwide'       : 'https://downdetector.co.uk/status/nationwide/'},
    {'Santander UK'     : 'https://downdetector.co.uk/status/santander/'},

    # 🇬🇧 UK Services
    {'Royal Mail'       : 'https://downdetector.co.uk/status/royal-mail/'},
    {'NHS'              : 'https://downdetector.co.uk/status/nhs/'},
    {'DVLA'             : 'https://downdetector.co.uk/status/dvla/'},
    {'Universal Credit' : 'https://downdetector.co.uk/status/universal-credit/'},
    {'BBC iPlayer'      : 'https://downdetector.co.uk/status/bbc-iplayer/'},
    {'ITV Hub'          : 'https://downdetector.co.uk/status/itv/'},
    {'Deliveroo'        : 'https://downdetector.co.uk/status/deliveroo/'},
    {'Just Eat'         : 'https://downdetector.co.uk/status/just-eat/'},
    {'Uber'             : 'https://downdetector.co.uk/status/uber/'},
    {'Trainline'        : 'https://downdetector.co.uk/status/trainline/'},

    # 🇺🇸 US Services
    {'AT&T'             : 'https://downdetector.com/status/att/'},
    {'Verizon'          : 'https://downdetector.com/status/verizon/'},
    {'T-Mobile'         : 'https://downdetector.com/status/t-mobile/'},
    {'Comcast'          : 'https://downdetector.com/status/comcast-xfinity/'},
    {'Chase Bank'       : 'https://downdetector.com/status/chase-bank/'},
    {'Bank of America'  : 'https://downdetector.com/status/bank-of-america/'},

    # 🌏 Other Regions
    {'Telstra'          : 'https://downdetector.com.au/status/telstra/'},
    {'Optus'            : 'https://downdetector.com.au/status/optus/'},
    {'Rogers'           : 'https://downdetector.ca/status/rogers/'},
    {'Bell Canada'      : 'https://downdetector.ca/status/bell/'},
    {'Deutsche Telekom' : 'https://downdetector.de/status/telekom/'},
    {'Orange France'    : 'https://downdetector.fr/status/orange/'},
]
def get_downdetector_data(list_of_companies):
    down_today = {}

    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage") 
    options.add_argument("--shm-size=2gb")           
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--lang=en-GB")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
    )

    driver = uc.Chrome(options=options, version_main=get_chrome_major_version())
    driver.set_page_load_timeout(60)
    webdriver_wait = WebDriverWait(driver,10)

    try:
        for org_data in list_of_companies:
            
            for org_name in org_data:
                driver.get(org_data.get(org_name))
                webdriver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#company-status")))

                time.sleep(2)
                try:
                    cookie_button = driver.find_element(By.CSS_SELECTOR,"button[id^='onetrust-accept-btn-handler']")
                    cookie_button.click()
                except:
                    pass

                time.sleep(2)
                banner_element = driver.find_element(By.CSS_SELECTOR,"#company-status")
                banner_element_attr_color = banner_element.get_attribute('class')

                if 'border-[var(--color-dd-red)]' in banner_element_attr_color:
                    data_card_element = driver.find_element(By.CSS_SELECTOR,"div[aria-label='Most reported problems breakdown']")
                    reported_problems = data_card_element.find_elements(By.CSS_SELECTOR,"div[role='listitem']")
                    reported_data_dict = {}
                    
                    for reports in reported_problems:
                        reported_data = reports.find_element(By.CSS_SELECTOR,".relative").text
                        reported_text = reports.find_element(By.CSS_SELECTOR,"div.text-center").text
                        reported_data_dict[reported_text] = reported_data

                    down_today[org_name] = {'report': reported_data_dict, 'desc' : banner_element.text}

                else:
                    print(org_name, "has no major outage reported. ")
        driver.quit()
    except Exception as e:
        print('Error',e)
    finally:
        driver.quit()

    return down_today

def downdetector_complainer(downdetector_data):
    downdetector_complaints = []
    for org,data in downdetector_data.items():
        reports = ",".join([" " + report + " " + data['report'].get(report) for report in data['report']])
        downdetector_complaints.append(f"{org} is down today, outage report by impact is as follows:{reports}.")
    print(downdetector_complaints)
    return downdetector_complaints

