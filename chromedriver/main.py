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

import id_No_1
import id_No_2
import reg_data


# создание объекта UserAgent (Фейковый Юзер-Агент)
userAgent = UserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={userAgent.random}")
options.add_argument("--disable-blink-features=AutomationControlled")


service = Service(executable_path='chromedriver')

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get(URL)
    driver.find_element(By.ID, "fgnRegNo1").send_keys(id_No_1)
    driver.find_element(By.ID, "fgnRegNo2").send_keys(id_No_2)
    driver.find_element(By.ID, "regYmd").send_keys(reg_data)
    driver.find_element(By.ID, "confirmBtn1").click()
    time.sleep(1)
    driver.find_element(By.ID, "deskSeq738").click()
    time.sleep(1)
    driver.find_element(By.ID, 'selBusiType1_1_F01').click()
    time.sleep(1)

    # Выпадающий список для номера телефона
    dropdown = Select(driver.find_element(By.ID, "mobileTelNo1"))
    dropdown.select_by_value("010")
    time.sleep(1)

    # Выбор даты
    driver.find_element(By.ID, 'resvYmdSelect').click()
    # переход на другую вкладку
    driver.switch_to.window(driver.window_handles[1])
    data_cells = driver.find_elements(By.XPATH, "//td[@data-handler='selectDay']")
    time.sleep(2)
    if data_cells:
        print(data_cells)
    else:
        print("В этом месяце все дни заняты, ближайщие дни ")
        next_btn = driver.find_element(By.XPATH, "//a[@title='다음 달']")
        time.sleep(1)
        next_btn.click()
        time.sleep(2)
        data_cells = driver.find_elements(By.XPATH, "//td[@data-handler='selectDay']")

        for cell in data_cells:
            print(cell.text)

    time.sleep(3)

    # Переход назад на главную вкладку
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(5)




except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
