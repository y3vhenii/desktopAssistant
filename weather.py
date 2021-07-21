import requests
import json

# Retrieves weather based on location 
def getWeatherAtMyLocation(latitude, longitude):
    url = "https://api.tomorrow.io/v4/timelines"
    querystring = {
    "location": str(latitude) + ", " + str(longitude),
    "location":"33, -84",
    "fields":["temperature", "cloudCover"],
    "units":"imperial",
    "timesteps":"1d",
    "apikey":"5oevdm3dlqRernOYyh74JP4ssGKYGLal"}
    response = requests.request("GET", url, params=querystring)
    results = response.json()['data']['timelines'][0]['intervals']
    for every_day in results:
        date = every_day['startTime'][0:10]
        temp = round(every_day['values']['temperature'])
        cloudCover = every_day['values']['cloudCover']
        if cloudCover > 80:
            sky = "Very cloudy"
        elif cloudCover <= 30:
            sky = "Little to no clouds"
        elif cloudCover > 30 and cloudCover <= 80:
            sky = "Cloudy"
        print("On " + date + " it will be " + str(temp) + " F. " + sky)
    