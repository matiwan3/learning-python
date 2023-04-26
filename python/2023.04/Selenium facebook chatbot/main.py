from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import getpass
import logging


# python_site = driver.get("http://www.python.org")

options = webdriver.ChromeOptions() 
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
driver = webdriver.Chrome()

try:
    print("Sending request to open facebook...")
    driver.get("https://m.facebook.com")
    print("Facebook login page loaded!")
except:
    print("Loading page error occurred!")

def login_page(driver):
    username = input("Username: ")
    password = getpass.getpass('Password: ')
    print(f"Your username is: {username} and password is: {password}")
    driver.close()
login_page(driver)
    



