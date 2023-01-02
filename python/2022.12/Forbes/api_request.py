import requests

url = "https://forbes-worlds-billionaires-list.p.rapidapi.com/billionaires/2022"

querystring = {"page":"0","size":"100"}

headers = {
	"X-RapidAPI-Key": "5fd1ccc2a5msh1376e245b4274f8p10c9b2jsn9499fb21e8ec",
	"X-RapidAPI-Host": "forbes-worlds-billionaires-list.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)