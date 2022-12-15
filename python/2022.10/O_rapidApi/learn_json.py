'''
Introduction
In a different tutorial, we discussed how to web scrape with python. 
The goal of web scraping was to access data from a website or webpage. 
Well, sometimes a website can make it easier for a user to have direct access 
to their data with the use of an API (Application Programming Interface). 
This basically means that the company has made a set of dedicated URLs that provide this data in a pure 
form (meaning without any presentation formatting). This pure data is often in a JSON (JavaScript Object Notation) format, 
which we can then parse through and extract what we need using python.

For this tutorial, we will use the free API found at covid19api.com that provides data on the coronavirus. 
We will find the total number of confirmed cases in each country and then we will create a pandas dataframe 
that contains that information. So let's begin!

source: https://towardsdatascience.com/json-and-apis-with-python-fba329ef6ef0 
'''
import requests
import json
import pandas as pd
import matplotlib


response = requests.get('https://api.covid19api.com/summary').text
requests.get('https://api.covid19api.com/summary').json()

# print(response)
# print(response_info)
# print(type(response_info))

country_list = []

for country_info in response_info['Countries']:
    country_list.append([country_info['Country'],
    country_info['TotalConfirmed']])

country_df = pd.DataFrame(data=country_list, columns=['Country','Total_Confirmed'])
print(country_df.head(10))

# Conclusion
# In this tutorial, we had a brief introduction to what APIs and JSON are.
# We then made an HTTP request to a Coronavirus COVID19 API to get information on the number of total
# confirmed coronavirus cases in each country. We then converted this JSON response to our request into a python dictionary.
# We then parsed through this dictionary, extracting the information we were seeking, and then created
# a pandas dataframe containing this information.


