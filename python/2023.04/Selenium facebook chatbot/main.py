from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import getpass
import logging


# python_site = driver.get("http://www.python.org")

logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
logger.setLevel(logging.WARNING)
driver = webdriver.Chrome(executable_path='chromedriver.exe')
print("Sending request to open facebook...")
facebook_site = driver.get("https://m.facebook.com")
print("Facebook login page loaded!")

def login_page(driver):
    username = input("Username: ")
    password = getpass.getpass('Password: ')
    print(f"Your username is: {username} and password is: {password}")
login_page(driver)
    



