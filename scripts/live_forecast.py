from src.weather_api import fetch_weather
from src.predict import predict_price

import pandas as pd

weather = fetch_weather()

latest = weather.tail(10)

forecast = predict_price(latest)

print(forecast[["timestamp","predicted_price"]])