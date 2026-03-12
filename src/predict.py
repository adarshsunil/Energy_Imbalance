import joblib
import pandas as pd
from .config import MODEL_PATH

model = joblib.load(MODEL_PATH)


def predict_price(data):

    features = [
        "niv",
        "niv_lag1",
        "price_lag1",
        "price_lag2",
        "wind_100m",
        "temp",
        "cloud",
        "hour"
    ]

    X = data[features]

    predictions = model.predict(X)

    data["predicted_price"] = predictions

    return data