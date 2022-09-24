import requests
import bs4 #beatiful soup

imieniny = 'https://halloween.friko.net/imieniny/'

result = requests.get(imieniny)
result.encoding = "utf-8"

result.text
soup = bs4.BeautifulSoup(result.text, 'lxml')
data = soup.select('th')[0].getText()
imieniny = soup.select('td')[0].getText()

print(f"{data} imieniny obchodzą: {imieniny}")