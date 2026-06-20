import requests
import streamlit as st
API_KEY = st.secrets["GEOAPIFY_API_KEY"]

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
