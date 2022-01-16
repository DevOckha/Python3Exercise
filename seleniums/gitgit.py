from selenium import webdriver
from usps import username, password
import time



class Gihub:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
    
    def singIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()



github = Gihub(username, password)

github.singIn()
