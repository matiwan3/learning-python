import json
import mysql.connector


covid_file = open('covid_api_raw.json', 'r')
covid_json = json.load(covid_file)

# Connect to the database
cnx = mysql.connector.connect(
    user='root',
    password='SqL25@',
    host='localhost',
    database='generaldb'
)
cursor = cnx.cursor()

# Make a request and get the response as a json object

# Iterate over the json object and save the data to the database
for item in covid_json:
    country = item['Country']
    population = int(item['Population'])
    continent = item['Continent']
    total_recovered = int(item['TotalRecovered'])
    totalDeath = int(item['TotalDeaths'])

    # Insert the data into the covid_table table
    query = "INSERT INTO covid_table (country, population, continent, totalDeath, total_recovered) VALUES (%s, %s, %s, %s, %s)"
    values = (country, population, continent, totalDeath, total_recovered)
    cursor.execute(query, values)

# Commit the transaction and close the connection
cnx.commit()
cursor.close()
cnx.close()