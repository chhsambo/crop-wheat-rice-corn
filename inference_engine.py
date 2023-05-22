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