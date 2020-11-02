# AIzaSyAKNCiMKEWz5NCmZ6fZnyRAqcvytb8aQ1s

import requests
import json

currentLocation = input('Search nearest restaurants in: ')

urlBase = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+"+currentLocation+"&key="
api_key = "AIzaSyDmxP_DwnglYZYFM6O_jy_7tOXJXxhNL-Y" #Create your own API key or ask me for it.

fullUrl = urlBase + api_key
response = requests.get(fullUrl)

if response.status_code == 200:
    jsonResults = response.json()
    print("Here's the nearest restaurant in {}:".format(currentLocation))
    count = 0
    while jsonResults["results"][count]["business_status"] == "CLOSED_TEMPORARILY":
        count += 1

    print(jsonResults["results"][count]["name"] + " at " + jsonResults["results"][count]["formatted_address"])