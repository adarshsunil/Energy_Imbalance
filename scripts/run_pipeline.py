from src.weather_api import fetch_weather
from src.grid_data import load_imbalance_data
from src.feature_engineering import create_features
from src.train_model import train_model

import pandas as pd


imbalance = load_imbalance_data("data/raw/Imbalance_Price_month.csv")

weather = fetch_weather()

data = pd.merge_asof(
    imbalance.sort_values("timestamp"),
    weather.sort_values("timestamp"),
    on="timestamp",
    direction="nearest"
)

data = create_features(data)

train_model(data)