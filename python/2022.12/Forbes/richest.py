import requests
import mysql.connector

# Send an HTTP request to the API
url = "https://forbes-worlds-billionaires-list.p.rapidapi.com/billionaires/2022"
querystring = {"page":"0","size":"100"}
headers = {
    "X-RapidAPI-Key": "5fd1ccc2a5msh1376e245b4274f8p10c9b2jsn9499fb21e8ec",
    "X-RapidAPI-Host": "forbes-worlds-billionaires-list.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)

# Parse the API response
data = response.json()

# Connect to the database
cnx = mysql.connector.connect(user='root', password='SqL25@', host='localhost', database='generaldb',)

# Create a cursor object
cursor = cnx.cursor()

# Insert each row into the table
for person in data:
    first_name = person['personName']
    net_worth = person['finalWorth']
    country = person['country']
    industries = person['industries'][0]
    query = f"INSERT INTO richest_people (first_name, net_worth, country, industries) VALUES ('{first_name}', '{net_worth}', '{country}', '{industries}')"
    cursor.execute(query)

# Commit the changes to the database
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
