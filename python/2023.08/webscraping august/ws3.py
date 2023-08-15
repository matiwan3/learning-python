import requests
from bs4 import BeautifulSoup

URL = 'https://www.books.toscrape.com/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html5lib')

print(soup)
# venv/bin/python ws3.py