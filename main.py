from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

page_url = "https://www.speedtest.net/ru"

chrome_driver_path = "C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(page_url)

time.sleep(2)
begin = driver.find_element(By.CLASS_NAME, "start-button")
begin.click()
time.sleep(40)
results = driver.find_elements(By.CLASS_NAME, "result-data-large")

print(f"Download speed: {results[0].text}Mb/s")
print(f"Upload speed: {results[1].text}Mb/s")
