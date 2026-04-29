from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
URL = 'https://10fastfingers.com/custom-typing-test?words=Coronavirus%7Cdisease%7C2019%7C%28COVID-19%29%7Cis%7Can%7Cinfectious%7Cdisease%7Ccaused%7Cby%7Csevere%7Cacute%7Crespiratory%7Csyndrome%7Ccoronavirus%7C2%7C%28SARS-CoV-2%29.%7CThe%7Cdisease%7Cwas%7Cfirst%7Cidentified%7Cin%7CDecember%7C2019%7Cin%7CWuhan%2C%7Cthe%7Ccapital%7Cof%7CChina%27s%7CHubei%7Cprovince%2C%7Cand%7Chas%7Csince%7Cspread%7Cglobally%2C%7Cresulting%7Cin%7Cthe%7Congoing%7C2019-20%7Ccoronavirus%7Cpandemic.%7CAs%7Cof%7C25%7CApril%7C2020%2C%7Cmore%7Cthan%7C2.89%7Cmillion%7Ccases%7Chave%7Cbeen%7Creported%7Cacross%7C185%7Ccountries%7Cand%7Cterritories%2C%7Cresulting%7Cin%7Cmore%7Cthan%7C202%2C000%7Cdeaths.%7CMore%7Cthan%7C815%2C000%7Cpeople%7Chave%7Crecovered.%7CCommon%7Csymptoms%7Cinclude%7Cfever%2C%7Ccough%2C%7Cfatigue%2C%7Cshortness%7Cof%7Cbreath%7Cand%7Closs%7Cof%7Csmell.%7CWhile%7Cthe%7Cmajority%7Cof%7Ccases%7Cresult%7Cin%7Cmild%7Csymptoms%2C%7Csome%7Cprogress%7Cto%7Cviral%7Cpneumonia%2C%7Cmulti-organ%7Cfailure%2C%7Cor%7Ccytokine%7Cstorm.%7CMore%7Cconcerning%7Csymptoms%7Cinclude%7Cdifficulty%7Cbreathing%2C%7Cpersistent%7Cchest%7Cpain%2C%7Cconfusion%2C%7Cdifficulty%7Cwaking%2C%7Cand%7Cbluish%7Cskin.%7CThe%7Ctime%7Cfrom%7Cexposure%7Cto%7Conset%7Cof%7Csymptoms%7Cis%7Ctypically%7Caround%7Cfive%7Cdays%7Cbut%7Cmay%7Crange%7Cfrom%7Ctwo%7Cto%7Cfourteen%7Cdays.%7CIndividuals%7Cmay%7Cexperience%7Cdistress%7Cfrom%7Cquarantine%2C%7Ctravel%7Crestrictions%2C%7Cside%7Ceffects%7Cof%7Ctreatment%2C%7Cor%7Cfear%7Cof%7Cthe%7Cinfection%7Citself.%7CTo%7Caddress%7Cthese%7Cconcerns%2C%7Cthe%7CNational%7CHealth%7CCommission%7Cof%7CChina%7Cpublished%7Ca%7Cnational%7Cguideline%7Cfor%7Cpsychological%7Ccrisis%7Cintervention%7Con%7C27%7CJanuary%7C2020.%7CMost%7Cof%7Cthose%7Cwho%7Cdie%7Cof%7CCOVID-19%7Chave%7Cpre-existing%7C%28underlying%29%7Cconditions%2C%7Cincluding%7Chypertension%2C%7Cdiabetes%7Cmellitus%2C%7Cand%7Ccardiovascular%7Cdisease.%5B222%5D%7CThe%7CIstituto%7CSuperiore%7Cdi%7CSanit%C3%A0%7Creported%7Cthat%7Cout%7Cof%7C8.8%25%7Cof%7Cdeaths%7Cwhere%7Cmedical%7Ccharts%7Cwere%7Cavailable%7Cfor%7Creview%2C%7C97.2%25%7Cof%7Csampled%7Cpatients%7Chad%7Cat%7Cleast%7Cone%7Ccomorbidity%7Cwith%7Cthe%7Caverage%7Cpatient%7Chaving%7C2.7%7Cdiseases.%7CAccording%7Cto%7Cthe%7Csame%7Creport%2C%7Cthe%7Cmedian%7Ctime%7Cbetween%7Cthe%7Conset%7Cof%7Csymptoms%7Cand%7Cdeath%7Cwas%7Cten%7Cdays%2C%7Cwith%7Cfive%7Cbeing%7Cspent%7Chospitalised.%7CHowever%2C%7Cpatients%7Ctransferred%7Cto%7Can%7CICU%7Chad%7Ca%7Cmedian%7Ctime%7Cof%7Cseven%7Cdays%7Cbetween%7Chospitalisation%7Cand%7Cdeath.%7CSeveral%7Cmeasures%7Care%7Ccommonly%7Cused%7Cto%7C&dur=30&rand=true'
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

def get_word_list():
    try:
        word_box = driver.find_element(By.CSS_SELECTOR, '[data-testid="WordBox-root"]')
        words = word_box.find_element(By.CSS_SELECTOR, "div")
        word_list = words.text.split(' ')
        print(word_list)
        return word_list
    except NoSuchElementException:
        return None

try:
    text_area = driver.find_element(By.TAG_NAME,"textarea")
    word_list = []
    while word_list is not None:
        try:
            word_list = get_word_list()
        except StaleElementReferenceException:
            word_list = get_word_list()

        for word in word_list:
            text_area.send_keys(word)
            text_area.send_keys(Keys.SPACE)
            time.sleep(0.1)

except TypeError as e:
    print("No More Words!!")
except NoSuchElementException as e:
    print('Element with given CSS_SELECTOR was not found.')
except Exception as e:
    print(f'Error! \n{e}')