from selenium import webdriver
import time 

driver = webdriver.Chrome()

url = "https://github.com"

driver.get(url)

searchInput = driver.find_element_by_name("user_email")
time.sleep(1)

searchInput.send_keys("yakupwrc@hotmail.com")

time.sleep(2)

driver.close()