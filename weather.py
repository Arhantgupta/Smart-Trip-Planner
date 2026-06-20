import requests
import streamlit as st
API_KEY = st.secrets["WEATHER_API_KEY"]

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    return response.json()
