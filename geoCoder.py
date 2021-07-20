import requests

# Returns location info based on input
def getMyLocation(address):
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    location = input("Enter the location here: ") #taking user input
    api_key = 'AGkvqgTO-RKvsp3oSZGxpCa7l3x0e_jb3QM_OcB2f94' # Acquire from developer.here.com
    PARAMS = {'apikey':api_key,'q':location} 

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()

    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']