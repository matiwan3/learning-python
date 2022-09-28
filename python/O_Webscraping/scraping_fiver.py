from gettext import gettext
from pydoc import text
import bs4
import requests
import csv

fiver_url = 'https://www.fiverr.com/search/gigs?query=python&source=top-bar&ref_ctx_id=d7e70110549f3992806ba785077abc08&search_in=everywhere&search-autocomplete-original-term='
books_to_scrap_url = 'https://books.toscrape.com/catalogue/page-1.html'

csv_title_bts = ['Name','Price','Rating']

result = requests.get(books_to_scrap_url)
soup = bs4.BeautifulSoup(result.text,'lxml')
content = soup.select('.product_pod')

def get_titles(content):
    book_name = []
    for i in content:
        # name = ''
        name = i.select('a')[1].getText()
        book_name.append(name)
    return book_name

def get_prices(content):
    book_price = []
    for prices in content:
        price = prices.select('p')[1].getText() #price is displayed wrong ; cut the first two elements
        price_fixed = price[2:]
        book_price.append(price_fixed)
    return book_price  

def get_rating(content):
    book_rating = []
    for ratings in content:
        call = ratings.find_all('.star-rating Three')
        if call:
            print('found')
        
            
    return book_rating
    
    
book_title = get_titles(content)
book_prices = get_prices(content)
book_rating = get_rating(content)
print(book_title)
print(book_prices)
print(book_rating)

with open('import.csv', 'w+') as file:
    writer = csv.writer(file)
    writer.writerow(csv_title_bts)



