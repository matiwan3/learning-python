'''
SNKRS NICE BOT
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
import bs4
import time
import getpass

#URLS
messenger = 'https://www.messenger.com/'
dropsy = 'https://dropsy.app/pl'
kalendarz = 'https://halloween.friko.net/imieniny/'

PATH_TO_DEV_NULL = 'nul' #Turns off geckodriver log
path_chrome = r'driver-chrome.exe'
path_firefox = r'driver-firefox.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=path_chrome,options=options)
self_actions = ActionChains(driver)

#login
def login_to_messenger():
    BOT_MAIL = input("Email: ")
    BOT_PASSWORD = input("Password: ")
    driver.get(messenger)
    
    #Accepting the cookies
    ACCEPT_COOKIES = '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]'
    try:
        driver.find_element(By.XPATH, ACCEPT_COOKIES).click()
    except:
        print("Button not found")
            
    email = driver.find_element(By.ID,'email')
    email.send_keys(BOT_MAIL) #HERE ENTER THE email for login form
    my_password = driver.find_element(By.ID, 'pass')
    my_password.send_keys(BOT_PASSWORD) #HERE ENTER THE password for login in
    driver.find_element(By.ID, 'loginbutton').click()
    # return BOT_MAIL,BOT_PASSWORD

def get_imieniny():
    result = requests.get(kalendarz)
    result.encoding = "utf-8"
    result.text
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    dzisiejsza_data = soup.select('th')[0].getText()
    imieniny = soup.select('td')[0].getText()
    return dzisiejsza_data,imieniny
    
dzisiejsza_data,imieniny = get_imieniny()

def who_to_chat(username):
    KNOWN_USER = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li/ul/li[2]'
    NEW_USER = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[2]/ul/li[1]'
    SEARCH_BOX = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div'
    # /html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/label/input
    NOT_FOUND_TEXT = 'User not found'
    
    type_user = driver.find_element(By.XPATH, SEARCH_BOX)
    type_user.clear()
    type_user.send_keys(username)    
    time.sleep(2)
    
    try:
        find_user = driver.find_element(By.XPATH, KNOWN_USER).click()
        if "More People" in driver.page_source:
            try:
                find_user = driver.find_element(By.XPATH, NEW_USER).click()
            except:
                print(NOT_FOUND_TEXT)
    except:
        print(NOT_FOUND_TEXT)

    #sending a greet
def greetings(data,imieniny):
    self_actions.send_keys(f'Botis: {data} 2022. \nImieniny obchodzą: {imieniny}\nŻyczę miłego dnia :D').perform()
    self_actions.send_keys(Keys.RETURN).perform()

def what_time():
    now = time.strftime("%H:%M:%S")
    return now

def main():
    Botis = True
    
    while Botis:
        get_imieniny()
        login_to_messenger()
        username = input('Piszę do: ')
        who_to_chat(username)
        
        texting = True
        while texting:  
            #Wysyłanie własnych wiadomości + KOMENDY
            send_text = input("Send message: ")
            if send_text =='/quit':
                texting = False
                
            elif send_text == '/change chat': #change_chat
                username = input('Message to: ')
                who_to_chat(username)
            
            elif send_text == '/greet': #Powitanie i wysłanie wiadomości kalendarzowych
                greetings(dzisiejsza_data,imieniny)
                
            elif send_text == '/time':
                time = what_time()
                self_actions.send_keys(f'Botis: Jest godzina {time}').perform()
                self_actions.send_keys(Keys.RETURN).perform()
               
            else:
                self_actions.send_keys('Botis: ' + send_text).perform()
                self_actions.send_keys(Keys.RETURN).perform()

        #Wyjście
        input("Press any key to exit...")
        if input:
            Botis = False
            driver.close()

if __name__ == '__main__':
    main()
    
    
#https://www.youtube.com/watch?v=dwkE4e6HH9I