# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

# import Fake UserAgent
from fake_useragent import UserAgent
import time

# import URL
from const import URL

# создание объекта UserAgent
userAgent = UserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={userAgent.random}")
options.add_argument("--disable-blink-features=AutomationControlled")

# Ввод данных пользователя
# id_No_1 = input("Введите первые 6 цифр ID")
# id_No_2 = input("Введите вторые 6 цифр ID")
# reg_data = input("Введите дату получения ID")

id_No_1 = "811011"
id_No_2 = "5780293"
reg_data = "20151120"

service = Service(executable_path='chromedriver')

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get(URL)
    driver.find_element(By.ID, "fgnRegNo1").send_keys(id_No_1)
    driver.find_element(By.ID, "fgnRegNo2").send_keys(id_No_2)
    time.sleep(1)
    driver.find_element(By.ID, "regYmd").send_keys(reg_data)
    time.sleep(1)
    driver.find_element(By.ID, "confirmBtn1").click()
    time.sleep(1)
    driver.find_element(By.ID, "deskSeq738").click()
    time.sleep(3)
    driver.find_element(By.ID, 'selBusiType1_1_F01').click()
    time.sleep(3)

    # Выпадающий список для номера телефона
    dropdown = Select(driver.find_element(By.ID, "mobileTelNo1"))
    dropdown.select_by_value("010")
    time.sleep(3)

    #Выбор даты
    driver.find_element(By.ID, 'resvYmdSelect').click()

    time.sleep(5)




except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
