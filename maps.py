import requests

API_KEY = "92bb04d820724e83916d627002422825"

def get_coordinates(city):

    url ="https://api.geoapify.com/v1/geocode/search"

    params = {
        "text": city,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)

    data = response.json()

    lat = data["features"][0]["properties"]["lat"]
    lon = data["features"][0]["properties"]["lon"]

    return lat,lon
