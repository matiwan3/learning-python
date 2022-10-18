import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'../geckodriver.exe') #Go back and open geckodriver
        self.driver.get("http://www.python.org")
        
    def test_example(self): # Important !! Starts always because has "test_" at the name of the function
        print("print test")
        assert True
        
    def not_a_test(self):
        print("this wont print")
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()