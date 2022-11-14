from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


humna_url = 'https://humanbenchmark.com/tests/chimp'
typing_test = 'https://humanbenchmark.com/tests/typing'

path_chrome = r'driver-chrome.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(path_chrome,options=options)
driver.maximize_window()

def get_started():
    try:
        driver.get(humna_url)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]"))
        )
        driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div/button').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[2]/button').click()    
    except:
        input()
        driver.quit()
        

def typing_test():
    driver.get(typing_test)



def main():
    run = True
    while run:
        typing_test()
    
    
    
    
if __name__ == "__main__":
    main()