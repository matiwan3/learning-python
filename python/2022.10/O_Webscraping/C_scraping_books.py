import bs4
import requests
import xlwt
import csv
import pandas as pd
import warnings

#URL
format_url = 'https://books.toscrape.com/catalogue/page-{}.html'

def main():
    
    #Lists of data
    book_name = []
    book_price = []
    book_rating = []
    
    rating_list = ['star-rating One','star-rating Two','star-rating Three','star-rating Four','star-rating Five']
    
    #Get book titles
    def get_titles(content):
        
        for i in content:
            name = i.select('a')[1].getText()
            book_name.append(name)
        return book_name
    
    #Get book prices
    def get_prices(content):
        
        for prices in content:
            price = prices.select('p')[1].getText() #price is displayed wrong ; cut the first two elements
            price_fixed = float(price[2:])
            book_price.append(price_fixed)
        return book_price
    
    #Get book rating
    def get_rating(content):
        
        
        for ratings in content:
            
            rating = str(ratings.select('p')[0])
            if rating_list[0] in rating:
                x = 1
                book_rating.append(x)
            elif rating_list[1] in rating:
                x = 2
                book_rating.append(x)
            elif rating_list[2] in rating:
                x = 3
                book_rating.append(x)
            elif rating_list[3] in rating:
                x = 4
                book_rating.append(x)
            elif rating_list[4] in rating:
                x = 5
                book_rating.append(x)
            else:
                book_rating.append('NaN')
        return book_rating
    
    for n in range(1,51):
        books_to_scrap = format_url.format(n)
        result = requests.get(books_to_scrap)
        soup = bs4.BeautifulSoup(result.text,'lxml')
        content = soup.select('.product_pod')
        warnings.filterwarnings("ignore")
        
        book_title = get_titles(content)
        book_prices = get_prices(content)
        book_rating = get_rating(content)
    
    
    raw_data = {'Name': book_title,
                'Price': book_prices,
                'Rating': book_rating 
                }

    df = pd.DataFrame(raw_data, columns= ['Name', 'Price', 'Rating'])
    # print (df)
    df.to_excel('books_data.xls', encoding='utf-8',index=False)
    
    average_price = df[['Price']].mean().to_string()
    average_rating = df[['Rating']].mean().to_string()
    
    print(f'Average {average_price}')
    print(f'Average {average_rating}')
    
# df.to_csv('raw_data.csv', index=False)

if __name__ == '__main__':
    main()
















# with open('import.csv', 'w+') as file:
#     writer = csv.writer(file)
#     writer.writerow(csv_title_bts)

# https://www.udemy.com/course/analiza-danych-w-python-i-pandas/?utm_source=adwords&utm_medium=udemyads&utm_campaign=INTL-AW-PROS-TECH-Poland-DSA-WebIndex&utm_term=_._ag_100563868518_._ad_427601021502_._de_c_._dm__._pl__._ti_dsa-93451758763_._li_1011589_._pd__._&gclid=Cj0KCQjwkOqZBhDNARIsAACsbfI_hgPnhLLV2oJkjkLiAcHKY4JnzmJUZ78SfZuYXqchX1VTjPF_wgQaAm33EALw_wcB