# tools: BeautifulSoap, Scrapy, Selenium, Requests, PyQuery, LXML, BS4 + Requests
# venv/bin/python ws1.py
# source venv/bin/activate
# pip list

from bs4 import BeautifulSoup
import requests

URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)
counterA = 0

soup = BeautifulSoup(r.content, 'html5lib') # If this line cause an error
print(soup.prettify())

# soup = BeautifulSoup(r.text, "html.parser")
# Find all occurrences of the letter 'a' in the page content
# counterA = soup.get_text().lower().count("a")
# print(counterA)