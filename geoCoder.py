import requests
from weather import *

# Returns location info based on input
def getMyWeatherUpdate(address):
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    api_key = 'AGkvqgTO-RKvsp3oSZGxpCa7l3x0e_jb3QM_OcB2f94' 
    PARAMS = {'apikey':api_key,'q':address} 

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()

    # Current latitude and longitude
    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']
    
    # Pass parameters to weather api
    getWeatherAtMyLocation(latitude, longitude)
    