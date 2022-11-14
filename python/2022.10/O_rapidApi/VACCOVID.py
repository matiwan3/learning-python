import requests
import json
import pandas as pd

# API VACCOVID getting info from json about country, coontinent, deaths, new deaths

url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/"

headers = {
    "X-RapidAPI-Key": "5255d4bac8mshfb585a9ebad670fp1d25ecjsn8e1c0ee2018f",
    "X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
response_info = json.loads(response.text)

country_list = []

for country_info in response_info:
    country_list.append([
        country_info['Country'],
        country_info['Continent'], 
        country_info['TotalDeaths'],
        country_info['NewDeaths']])

country_df = pd.DataFrame(data=country_list, columns=['Country','Continent','TotalDeaths', 'NewDeaths'])
print(country_df.head(11))