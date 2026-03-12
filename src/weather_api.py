import requests
import pandas as pd
from .config import LATITUDE, LONGITUDE, WEATHER_API, TIMEZONE


def fetch_weather():

    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "hourly": "wind_speed_10m,wind_speed_100m,temperature_2m,precipitation,cloudcover",
        "timezone": TIMEZONE
    }

    response = requests.get(WEATHER_API, params=params)
    data = response.json()

    weather_df = pd.DataFrame({
        "timestamp": data["hourly"]["time"],
        "wind_10m": data["hourly"]["wind_speed_10m"],
        "wind_100m": data["hourly"]["wind_speed_100m"],
        "temp": data["hourly"]["temperature_2m"],
        "precip": data["hourly"]["precipitation"],
        "cloud": data["hourly"]["cloudcover"]
    })

    weather_df["timestamp"] = pd.to_datetime(weather_df["timestamp"])

    return weather_df