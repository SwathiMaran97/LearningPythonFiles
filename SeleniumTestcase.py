import sys
import os
from selenium import webdriver

# path = "https://beautyproducts/login"
browser= webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
browser.get("https://beautyproducts/login")

def create():
    python_button = browser.find_elements_by_xpath("//*[@id=orangeForm-email]")[0]
    python_button.send_keys('swathi@gmail.com')
    # python_button = browser.find_elements_by_xpath("//*[@id="orangeForm-pass"]")[0]
    # python_button.send_keys('')
if __name__ == '__main__':
    create()
