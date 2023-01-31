import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
os.environ["PATH"]+=r"c:/seleniumDriver"

driver = webdriver.Chrome()
url = "http://demo.seleniumeasy.com/basic-first-form-demo.html"
driver.get(url)
driver.implicitly_wait(10)
driver.find_element(By.ID,"sum1").send_keys(Keys.NUMPAD9,Keys.NUMPAD1)
driver.find_element(By.ID,"sum2").send_keys("15")
elmnt = driver.find_element(By.CSS_SELECTOR,'button[onclick="return total()"]')
elmnt.click()
res = driver.find_element(By.ID,'displayvalue')
print(res.text)
time.sleep(10)