from config import api_key
import requests
def get_date(city):
        data = {
            "q": city,
            "appid": api_key
        }
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather", params=data)
        if response.status_code == 200:
            response = response.json()
            return response["main"]["temp"]-273.15
        return None