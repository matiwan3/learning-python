import requests
import json

url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/"

headers = {
	"X-RapidAPI-Key": "5fd1ccc2a5msh1376e245b4274f8p10c9b2jsn9499fb21e8ec",
	"X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
}
id_list = []
response = requests.request("GET", url, headers=headers)
json_response = response.json()

# save as raw json
with open('covid_api_raw.json', 'w') as f:
    f.write(response.text)

# save as readable json
json_string = json.dumps(json_response, indent=4)
with open('covid_api_wrapped.json', 'w') as f:
    f.write(json_string)
    
