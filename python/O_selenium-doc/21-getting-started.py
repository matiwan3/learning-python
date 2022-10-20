# The selenium.webdriver module provides all the WebDriver implementations. 
# Currently supported WebDriver implementations are Firefox, Chrome, IE and Remote.
# The Keys class provide keys in the keyboard like RETURN, F1, ALT etc. 
# The By class is used to locate elements within a document.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Adding the default driver path
driver_path = r'geckodriver.exe'

# turning off the logs
PATH_TO_DEV_NULL = 'nul'

# Next, the instance of Firefox WebDriver is created.
driver = webdriver.Firefox(executable_path=driver_path,service_log_path=PATH_TO_DEV_NULL)

# The driver.get method will navigate to a page given by the URL. 
# WebDriver will wait until the page has fully loaded 
# (that is, the “onload” event has fired) before returning control to your test or script. 
# Be aware that if your page uses a lot of AJAX on 
# load then WebDriver may not know when it has completely loaded:
driver.get("http://www.python.org")

# The next line is an assertion to confirm that title has the word “Python” in it:
assert "Python" in driver.title

# WebDriver offers a number of ways to find elements using the find_element method.
# For example, the input text element can be located by 
# its name attribute using the find_element method and using By.NAME 
# as its first parameter. 
# A detailed explanation of finding elements is available in the Locating Elements chapter:
elem = driver.find_element(By.NAME, "q")

# Next, we are sending keys, this is similar to entering keys using your keyboard. 
# Special keys can be sent using the 
# Keys class imported from selenium.webdriver.common.keys. To be safe, we’ll 
# first clear any pre-populated text in the input field (e.g. “Search”) so it 
# doesn’t affect our search results:
elem.clear()
elem.send_keys(Keys.RETURN)

# After submission of the page, you should get the result if there is any. 
# To ensure that some results are found, make an assertion:
assert "No results found." not in driver.page_source

# Finally, the browser window is closed. You can also call the 
# quit method instead of close. The quit method will exit the browser 
# whereas close will close one tab, but if just one tab was open, by 
# default most browsers will exit entirely.:
driver.close()