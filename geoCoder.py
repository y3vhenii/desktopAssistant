import requests
import pyttsx3
from weather import *

# Returns latitude and longitude info based on input address using HERE API
def getMyWeatherUpdate(address):
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    api_key = 'AGkvqgTO-RKvsp3oSZGxpCa7l3x0e_jb3QM_OcB2f94' 
    PARAMS = {'apikey':api_key,'q':address} 

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()

    # If user entered invalid address
    if not 'items' in data or len(data['items']) == 0:
        engine = pyttsx3.init()
        engine.say("Invalid address. Try again.")
        engine.runAndWait()
    
    else:
        # Current latitude and longitude
        latitude = data['items'][0]['position']['lat']
        longitude = data['items'][0]['position']['lng']
        # Pass parameters to weather api
        getWeatherAtMyLocation(latitude, longitude)
    