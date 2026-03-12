import joblib
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

from .config import MODEL_PATH


def train_model(data):

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
    y = data["price"]
    print(X.dtypes)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = XGBRegressor(
        n_estimators=400,
        learning_rate=0.05,
        max_depth=6
    )

    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)

    print("Model saved")