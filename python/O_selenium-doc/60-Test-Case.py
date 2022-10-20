# This chapter is a tutorial introduction to the Page Objects design pattern. 
# A page object represents an area where the test interacts within the web application user interface.

# Benefits of using page object pattern:

# Easy to read test cases
# Creating reusable code that can share across multiple test cases
# Reducing the amount of duplicated code
# If the user interface changes, the fix needs changes in only one place

# 6.1. Test case
# Here is a test case that searches for a word on the python.org website and 
# ensures some results. The following section will introduce the page module where the page objects will be defined.

import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        self.assertTrue(main_page.is_title_matches(), "python.org title doesn't match.")
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()