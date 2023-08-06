from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# chrome_path = r'../chrome-win64/chrome.exe'
# driver = webdriver.Chrome(executable_path = chrome_path,options=options)
browser = webdriver.Chrome()
browser.get('http://localhost:8000')
# driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(3)

browser.quit()