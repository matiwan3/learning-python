from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import getpass
import logging
import selectors
import time 

# python_site = driver.get("http://www.python.org")

options = webdriver.ChromeOptions() 
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

def accept_cookies(driver,selectors):
    try:
        driver.find_element(By.XPATH, selectors.accept_cookies).click()
    except:
        print("Accept cookies selector error")

def run_script():
    login_page(driver)
    accept_cookies(driver,selectors)
    
    # close driver
    time.sleep(5)
    driver.close()
    
if __name__ == "__main__":
    run_script()

    



