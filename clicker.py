from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, sys

if len(sys.argv) < 2:
    print('Usage: python clicker.py "path_to_chromedriver" || In same directory add ./ before chromedriver')
    sys.exit(-1)

class cookieBot():
    def __init__(self):
        self.browser = webdriver.Chrome(sys.argv[1])
        self.browser.get("https://orteil.dashnet.org/cookieclicker/")
        WebDriverWait(self.browser, 4).until(EC.presence_of_element_located((By.ID, 'bigCookie')))


    def clickCookie(self):
        cookie = self.browser.find_element_by_id('bigCookie')
        cookie.click()

bot = cookieBot()
time.sleep(1)
while(True):
    bot.clickCookie()
        
