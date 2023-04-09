from selenium import webdriver
from fake_useragent import UserAgent
import time

from selenium.webdriver.common.by import By

from const import url

userAgent = UserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={userAgent.random}")
driver = webdriver.Chrome(executable_path='chromedriver', options=options)
try:
    driver.get(url)
    driver.find_element(By.ID, "fgnRegNo1").send_keys("811011")
    time.sleep(1)
    driver.find_element(By.ID, "fgnRegNo2").send_keys("5780293")
    time.sleep(1)
    driver.find_element(By.ID, "regYmd").send_keys("20151120")
    time.sleep(1)
    driver.find_element(By.ID, "confirmBtn1").click()
    time.sleep(3)



    # print(fgnRegNo1)
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
