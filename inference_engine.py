import pandas as pd


def decide_crop_engine_v2(temperature, rainfall, soil_type):
    # DataFrame
    df = pd.read_csv("crop_data.csv")
    
    df = df[ (df["Soil Type"]==soil_type) & (df["Rainfall"]<=rainfall) ]

    return list(df["Crop"])


# Define the rules for decision making
def decide_crop_engine(temperature, rainfall, soil_type):
    if 25 < temperature < 28 and rainfall > 750 and soil_type == "loamy":
        return "Cassava"
    elif temperature > 30 and rainfall > 1000 and soil_type == "clay":
        return "Rice"
    elif temperature > 20 and rainfall > 600 and soil_type == "sandy":
        return "Corn"
    else:
        return "Unknown"