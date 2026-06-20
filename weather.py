import requests

API_KEY = "c534e7ffbe3df6c3af1ef83b6e6633c0"

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    return response.json()
