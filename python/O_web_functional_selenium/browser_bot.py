from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass
import os
import re

redricting_text = 'Redricting...'
error_text = 'Something went wrong. Try again.\n'
process_text = 'Loading completed\n'

#URLs
weather_url = 'https://weather.com/pl-PL/pogoda/dzisiaj/l/PLXX0028:1:PL'
get_string_local = 'http://127.0.0.1:5500/O_web_functional_selenium/index.html'
wp_pilot = 'https://pilot.wp.pl/tv/'
facebook = 'https://www.facebook.com/'

def gecko_drier():
    PATH_TO_DEV_NULL = 'nul' #Turns off geckodriver log
    options = Options()
    options.add_argument('--headless') #hiding the browser
    driver = webdriver.Firefox(executable_path=r'geckodriver.exe',service_log_path=PATH_TO_DEV_NULL)
    #,options=options
    # driver.maximize_window()
    self_actions = ActionChains(driver)
    return driver,self_actions
driver,self_actions = gecko_drier();

# INSTAGRAM Liking posts
def case_a():
    profile_url = input("Enter profile url: ")
    driver.get(profile_url)
    

#Commenting posts
def case_b():
    profile_url = input("Enter profile url: ")
    driver.get(profile_url)
    

#Saving posts
def case_c():
    profile_url = input("Enter profile url: ")
    driver.get(profile_url)

def login():
    ig_email = input("Enter instagram email: ")
    ig_password = getpass.getpass(prompt="Enter instagram password: ", stream=None) 
    print(ig_password)
    print(ig_email)
    return ig_email,ig_password

def option_2():
    print(redricting_text)
    try:
        driver.get(facebook)
        print(process_text)
    except:
        print(error_text)
    
def option_3():
    print(redricting_text)
    try:
        driver.get(wp_pilot)
        print(process_text)
    except:
        print(error_text)
        
def option_5(): #Run live server before chosing this option !!!
    try:
        print(redricting_text)
        email_list = []
        driver.get(get_string_local)
        site_text = driver.find_element(By.XPATH, "/html/body/div/div[2]/p").text
        match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', site_text) #Email pattern
        email_list.append(match)
        print(f'\nemails matches in the text: {email_list}\n')
    except:
        print(error_text)

def option_6():
    user_URL = input("Enter URL: ")
    try:
        print(redricting_text)
        driver.get(user_URL)
        print(process_text)
    except:
        print(error_text)



#Main fnc
def main():
    os.system('CLS')
    print(" ----------------------------------- ")
    print(" |      WELCOME TO BROWSER BOT     | ")
    print(" ----------------------------------- \n")
    
    chosing_task = True
    while chosing_task:

        print("1. Instagram")
        print("2. Facebook")
        print("3. TV")
        print("4. Weather")
        print("5. Find emails in text") #Run live server before chosing this option !!!
        print("6. Your own URL")
        print("7. Quit")
        action_number = input("\nMake your choice: ")
        if action_number.isdigit():
            #Instagram
            if action_number == '1':
                instagram = True
                while instagram:
                    print("\na. Liking posts")
                    print("b. Commenting posts")
                    print("c. Saving posts")
                    print("d. return")
                    action_char = input("\nMake your choice: ")
                    
                    if action_char == 'a':
                        case_a()
                        
                    elif action_char == 'b':
                        case_b()
                        
                    elif action_char == 'c':
                        case_c()
                        
                    elif action_char == 'd':
                        instagram = False
                        
                    else:
                        print("Wrong choice")
                    
            #Facebook
            elif action_number == '2':
                option_2()
                    
            #TV
            elif action_number == '3':
                option_3()
            #Weather
            elif action_number == '4':
                action_4 = True
                while action_4:
                    driver.get(weather_url)
                    city = input("Enter a city: ")
                    # print("cookies accepted")
                    try:
                        driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/header/div/div[2]/div[1]/div").click()
                        driver.find_element(By.ID,'LocationSearch_input').send_keys(city)
                        self_actions.send_keys(Keys.RETURN).perform()
                    except:
                        print(error_text)
                        action_4 = False
            #Weather
            elif action_number == '5':
                option_5()
                
            #Own URL
            elif action_number == '6':
                option_6()
                
            #Quit 
            elif action_number == '7':
               chosing_task = False
               driver.close()
                
            else:
                print("Wrong task number")
        else:
            print("Invalid input")
 
    # input("Press any key to exit...")
    # if input:
    #     driver.close()
    
if __name__ == '__main__':
    main()
    