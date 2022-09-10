from selenium import webdriver
from selenium.webdriver.common.by import By
import time

imieniny = 'https://halloween.friko.net/imieniny/'
def main():
    imieniny_list = []
    date = ''
    driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
    driver.get(imieniny)
    time.sleep(3)
    date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/div[1]/table/tbody/tr[1]/th').text
    
    # print(imieniny_list)
    imieniny_list = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td').text
    print(f'{date}, imieniny obchodzą: {imieniny_list}')
    
    #Close program
    input("Press any key to exit...")
    if input:
        driver.close()
if __name__ =='__main__':
    main()

