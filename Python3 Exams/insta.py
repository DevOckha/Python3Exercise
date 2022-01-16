from selenium import webdriver
import time






class Instagram:
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
    

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        emailInput = self.browser.find_element_by_xpath("")