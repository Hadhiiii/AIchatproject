"""# importing library
import requests
from bs4 import BeautifulSoup
 
# enter city name
city = "thrissur"
 
# creating url and requests instance
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content
 
# getting raw data
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
 
# formatting data
data = str.split('\n')
time = data[0]
sky = data[1]
 
# getting all div tag
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text
 
# getting other required data
pos = strd.find('Wind')
other_data = strd[pos:]
 
# printing all data
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)"""



# Python code to display schematic weather details
import requests
#Sending requests to get the IP Location Information
res = requests.get('http://ip-api.com/json')
# Receiving the response in JSON format
data = res.json()
# Extracting the Location of the City from the response
citydata = data['city']
# Prints the Current Location
print(citydata)
# Passing the City name to the url
url = 'https://wttr.in/{}'.format(citydata)
# Getting the Weather Data of the City
res = requests.get(url)
# Printing the results!
print(res.text)
# This code is contributed by PL VISHNUPPRIYAN



"""import requests
import json

# Make a get request to get the latest weather data
response = requests.get('http://api.open-meteo.com/v1/forecast', params={'latitude': '52.52', 'longitude': '13.419998'})

# Convert the response to JSON
data = response.json()
print(data)
# Get the temperature from the data
# The keys 'weather', 'main', and 'temp' are hypothetical and might be different for your actual API
#temperature = data['weather']['main']['temp']

# Print the temperature
#print(f"The temperature is {temperature} degrees.")
print(json.dumps(data, indent=4))"""