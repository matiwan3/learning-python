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

# The attributes available for the By class are used to locate elements on a page. 
# These are the attributes available for By class:

ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

# The ‘By’ class is used to specify which attribute is used to locate elements on a page. 
# These are the various ways the attributes are used to locate elements on a page:
driver.find_element(By.ID "id")
driver.find_element(By.NAME, "name")
driver.find_element(By.XPATH, "xpath")
driver.find_element(By.LINK_TEXT, "link text")
driver.find_element(By.PARTIAL_LINK_TEXT, "partial libk text")
driver.find_element(By.TAG_NAME, "tag name")
driver.find_element(By.CLASS_NAME, "class name")
driver.find_element(By.CSS_SELECTOR, "css selector")

# If you want to locate several elements with the same attribute replace find_element with find_elements.

# 4.1 Locating by id

# Use this when you know the id attribute of an element.
# With this strategy, the first element with a matching id attribute will be returned. 
# If no element has a matching id attribute, a NoSuchElementException will be raised.

# For instance, consider this page source:








