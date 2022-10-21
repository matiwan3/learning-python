'''
Learning json and api
source: https://towardsdatascience.com/json-and-apis-with-python-fba329ef6ef0 
'''
import requests
import json


response = requests.get('https://api.covid19api.com/summary').text
requests.get('https://api.covid19api.com/summary').json()
response_info = json.loads(response)
# print(response)
# print(response_info)
print(type(response_info))