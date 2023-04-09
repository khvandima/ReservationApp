from selenium import webdriver
import time

# options
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='chromedriver', options=options)

try:
    driver.get("https://google.com")
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
