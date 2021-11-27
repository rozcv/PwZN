from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument('--disable-notifications')

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.bbc.com/travel/columns/discovery')

button = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[1]/div[2]/div[2]/button[1]')
button.click()

time.sleep(1)

button = driver.find_element(By.XPATH, '//*[@id="bbccookies-continue-button"]')
button.click()

elements = driver.find_elements(By.CSS_SELECTOR, 'span')

for element in elements:
    print(element.text)

time.sleep(5)
driver.close()
