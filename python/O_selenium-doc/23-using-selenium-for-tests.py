# Selenium is mostly used for writing test cases. The selenium package itself doesn’t provide a testing tool/framework. You can write test cases using Python’s unittest module. The other options for a tool/framework are pytest and nose.

# In this chapter, we use unittest as the framework of choice. Here is the modified example which uses the unittest module. This is a test for the python.org search functionality:

# Initially, all the basic modules required are imported. The unittest module is a built-in Python module based on Java’s JUnit. This module provides the framework for organizing the test cases. The selenium.webdriver module provides all the WebDriver implementations. Currently supported WebDriver implementations are: Firefox, Chrome, IE and Remote. The Keys class provides keys in the keyboard like RETURN, F1, ALT etc. The By class is used to locate elements within a document
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# The test case class is inherited from unittest.TestCase. Inheriting from the TestCase class is the way to tell unittest module that this is a test case:
class PythonOrgSearch(unittest.TestCase):
    
    # The setUp method is part of initialization. This method will get called before every test function which you are going to write in this test case class. Here you are creating an instance of a Firefox WebDriver.
    def setUp(self):
        driver_path = r'geckodriver.exe'
        PATH_TO_DEV_NULL = 'nul'
        self.driver = webdriver.Firefox(executable_path=driver_path,service_log_path=PATH_TO_DEV_NULL)

    # This is the test case method. The test case method should always start with characters test. The first line inside this method creates a local reference to the driver object created in setUp method.
    def test_search_in_python_org(self):
        driver = self.driver

        # The driver.get method will navigate to a page given by the URL. WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before returning control to your test or script. Be aware that if your page uses a lot of AJAX on load then WebDriver may not know when it has completely loaded:
        driver.get("http://www.python.org")

        # The next line is an assertion to confirm that title has the word “Python” in it:
        self.asserIn("Python", driver.title)

        # WebDriver offers a number of ways to find elements using the find_element method. For example, the input text element can be located by its name attribute using the find_element method. Detailed explanation of finding elements is available in the Locating Elements chapter:
        elem = driver.find_element(By.NAME, "q")
        
        # Next, we are sending keys, this is similar to entering keys using your keyboard. Special keys can be sent using the Keys class imported from selenium.webdriver.common.keys:
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)

        # After submission of the page, you should get the result as per search if there is any. To ensure that some results are found, make an assertion:
        self.assertNotIn("No result found.", driver.page_source)

    # The tearDown method will get called after every test method. This is a place to do all cleanup actions. In the current method, the browser window is closed. You can also call the quit method instead of close. The quit method will exit the entire browser, whereas close will close a tab, but if it is the only tab opened, by default most browsers will exit entirely.:
    def tearDown(self):
        self.driver.close()

# Final lines are some boiler plate code to run the test suite:
if __name__ == "__main__":
    unittest.main()