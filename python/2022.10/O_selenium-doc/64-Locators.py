# 6.4. Locators
# One of the practices is to separate the locator strings from the place where they are getting used. 
# In this example, locators of the same page belong to the same class.

# The locators.py will look like this:

from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.ID, 'submit')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass