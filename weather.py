import requests

# Retrieves weather based on location 
def getWeatherAtMyLocation(latitude, lognitude):
    url = "https://api.tomorrow.io/v4/timelines"
    querystring = {
    "location":"33, -84",
    "fields":["temperature", "cloudCover"],
    "units":"imperial",
    "timesteps":"1d",
    "apikey":"5oevdm3dlqRernOYyh74JP4ssGKYGLal"}
    response = requests.request("GET", url, params=querystring)

    print(response.text)