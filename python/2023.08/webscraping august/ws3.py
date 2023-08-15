<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup

URL = 'https://www.books.toscrape.com/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html5lib')

print(soup)
# venv/bin/python ws3.py
=======
import unittest
class YouCanDoEverything(unittest.TestCase):
    def test_perspective(self):
        self.assertTrue("Daily Progress" > "Daily Complaining")
             
if __name__=='__main__':
      unittest.main()
>>>>>>> refs/remotes/origin/main
