import selenium
from uspas import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password
    


    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
        usernameInput.send_keys(self.username)
        time.sleep(2)
        nextPage = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span")
        nextPage.click()
        time.sleep(1)
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        passwordInput.send_keys(self.password)
        time.sleep(2)
        sign = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[3]/div/div")
        sign.click()
twitter = Twitter(username,password)
twitter.signIn()