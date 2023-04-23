import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

# import Fake UserAgent
from fake_useragent import UserAgent

import time

# создание объекта UserAgent (Фейковый Юзер-Агент)
userAgent = UserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={userAgent.random}")
options.add_argument("--disable-blink-features=AutomationControlled")


service = Service(executable_path='chromedriver')

driver = webdriver.Chrome(service=service, options=options)

