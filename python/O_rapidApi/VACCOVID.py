import requests
import json
import pandas as pd

url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/"

headers = {
	"X-RapidAPI-Key": "5255d4bac8mshfb585a9ebad670fp1d25ecjsn8e1c0ee2018f",
	"X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
response_info = json.loads(response.text)
print(response_info)

country_list = []

for country_info in response_info['Country']:
    country_list.append([country_info['Country'],
    country_info['Continent']])

country_df = pd.DataFrame(data=country_list, columns=['Country','Continent'])
print(country_df.head(10))