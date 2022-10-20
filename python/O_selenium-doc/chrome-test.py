from selenium import webdriver
import time
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_path = r'chromedriver.exe'
driver = webdriver.Chrome(executable_path = chrome_path,options=options)

try:
    driver.get("https://facebook.com")
    time.sleep(5)
    
except:
    os.system("CLS")
    print("error")
    
finally:
    driver.quit()