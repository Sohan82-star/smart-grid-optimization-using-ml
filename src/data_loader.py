import pandas as pd
import kagglehub
import os

def load_solar_data():
    path = kagglehub.dataset_download("anikannal/solar-power-generation-data")

    for root, dirs, files in os.walk(path):
        for file in files:
            if "Plant_1_Generation_Data.csv" in file:
                file_path = os.path.join(root, file)

    df = pd.read_csv(file_path)

    df['DATE_TIME'] = pd.to_datetime(df['DATE_TIME'])
    df['Hour'] = df['DATE_TIME'].dt.hour
    df['Day'] = df['DATE_TIME'].dt.day
    df['Month'] = df['DATE_TIME'].dt.month

    return df