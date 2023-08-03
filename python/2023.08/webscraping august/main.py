from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_path = r'chromedriver.exe'
driver = webdriver.Chrome(executable_path = chrome_path,options=options)
time.sleep(3)

driver.quit()