import argparse
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

tab = []
parser = argparse.ArgumentParser(description="Scraping")
parser.add_argument('file', help='name of file')
args = parser.parse_args()
print(f'File name: {args.file}')

options = Options()
options.add_argument('--disable-notifications')

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.bbc.com/travel/columns/discovery')

time.sleep(2)

button = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[1]/div[2]/div[2]/button[1]')
button.click()

time.sleep(1)

button = driver.find_element(By.XPATH, '//*[@id="bbccookies-continue-button"]')
button.click()

elements = driver.find_elements(By.CSS_SELECTOR, 'span')

textfile = open(args.file, "w")

for element in elements:
    print(element.text)
    tab.append(element.text)
    textfile.write(element.text.strip() + "\n")

textfile.close()


time.sleep(5)
driver.close()
