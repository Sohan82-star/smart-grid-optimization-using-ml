import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def solar_forecast(df):
    X = df[['Hour', 'Day', 'Month']]
    y = df['AC_POWER']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    hour_df = X.iloc[:24]
    forecast = model.predict(hour_df)

    return forecast