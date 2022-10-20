from selenium import webdriver
from selenium.webdriver.common.by import By


PATH_TO_DEV_NULL = "nul"
path = r'geckodriver.exe'
driver = webdriver.Firefox(executable_path=path, service_log_path=PATH_TO_DEV_NULL)

# here are various strategies to locate elements in a page. 
# You can use the most appropriate one for your case. 
# Selenium provides the following method to locate elements in a page:

# find_element
# To find multiple elements (these methods will return a list):

# find_elements
# Example usage:
    
driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_element(By.XPATH, '//button')