import pandas as pd

def load_imbalance_data(path):

    df = pd.read_csv(path)

    print("Columns found:", df.columns)

    # Rename columns
    df = df.rename(columns={
        "Time": "timestamp",
        "Imbalance Settlement Price(€)": "price",
        "NIV (MWh)": "niv"
    })

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"], dayfirst=True)

    # Convert numeric columns
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["niv"] = pd.to_numeric(df["niv"], errors="coerce")

    # Remove rows with missing values
    df = df.dropna()

    df = df.sort_values("timestamp")

    return df