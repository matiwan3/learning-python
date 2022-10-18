import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self): # For each testcase setUp is called once
        print("setup")
        self.driver = webdriver.Firefox(executable_path=r'../geckodriver.exe') #Go back and open geckodriver
        self.driver.get("http://www.python.org")
    
    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()
    
    
    def test_example(self): # Important !! Starts always because has "test_" at the name of the function
        print("print test")
        assert False

    # def test_example_2(self):
    #     assert True
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()