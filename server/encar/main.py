import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

# import Fake UserAgent
from fake_useragent import UserAgent

from config import URL

import time

# создание объекта UserAgent (Фейковый Юзер-Агент)
userAgent = UserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={userAgent.random}")
options.add_argument("--disable-blink-features=AutomationControlled")


service = Service(executable_path='chromedriver')

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get(url=URL)
    time.sleep(1)
    driver.find_element(By.ID, "manufact").click()
    items = driver.find_elements(By.CLASS_NAME, "link_item")
    # time.sleep(1)
    # for item in items:
    #     print(item.text)
    time.sleep(1)
    for item in items:
        if item.text == "현대":
            time.sleep(1)
            item.click()
            time.sleep(1)
    time.sleep(2)
    driver.find_element(By.ID, "series").click()




except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()