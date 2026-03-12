import pandas as pd

def create_features(df):

    df["price"] = pd.to_numeric(df["price"])
    df["niv"] = pd.to_numeric(df["niv"])

    df["price_lag1"] = df["price"].shift(1)
    df["price_lag2"] = df["price"].shift(2)

    df["niv_lag1"] = df["niv"].shift(1)

    df["hour"] = df["timestamp"].dt.hour

    df = df.dropna()

    return df