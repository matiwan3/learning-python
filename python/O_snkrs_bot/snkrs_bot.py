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
driver = webdriver.Firefox(executable_path=r'geckodriver.exe',service_log_path=PATH_TO_DEV_NULL)
self_actions = ActionChains(driver)

#login
def login_to_messenger():
    bot_mail = input("Email: ")
    bot_password = input("Password: ")
    driver.get(messenger)
    #Accepting the cookies
    try:
        # accept_cookies
        driver.find_element(By.XPATH,"//*[@title='Zezwól tylko na niezbędne pliki cookie']").click()
    except:
        # accept_cookies
        driver.find_element(By.XPATH,"//*[@title='Only allow essential cookies']").click()
    email = driver.find_element(By.ID,'email')
    email.send_keys(bot_mail) #HERE ENTER THE email for login form
    my_password = driver.find_element(By.ID, 'pass')
    my_password.send_keys(bot_password) #HERE ENTER THE password for login in
    driver.find_element(By.ID, 'loginbutton').click()
    # return bot_mail,bot_password

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
    
    find_user = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/label/input')
    find_user.send_keys(username)    
    time.sleep(2)
    try:
        find_user = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]').click()
        find_user = driver.fint_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[2]/ul/li/div')
        find_user = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div').click()
        find_user = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[2]/ul/li[1]/div').click()
    except:
        print('error')
    else:
        print('User found')


    #sending a greet
def greetings(data,imieniny):
    self_actions.send_keys(f'Botis: {data} 2022. \nImieniny obchodzą: {imieniny}\nŻyczę miłego dnia :D').perform()
    self_actions.send_keys(Keys.RETURN).perform()

def what_time():
    now = time.strftime("%H:%M:%S")
    return now

# def backspace(n):
#     self_actions.send_keys(Keys.BACK_SPACE).perform(n)

def main():
    n = 0
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
                
            # elif send_text  == '/b':
            #     n = input('How many backapces?: ')
            #     int(n)
            #     if n.isdigit():
            #         backspace(n)
            #     else:
            #         print('Wrong amount of backspaces')
                
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