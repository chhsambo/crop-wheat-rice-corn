from inference_engine import decide_crop_engine, decide_crop_engine_v2


print("Cron Recommendation")
print("===================")

# Take input from user
temperature = int(input("Enter average temperature (°C): "))
rainfall = int(input("Enter average rainfall (mm): "))
soil_type = input("Enter soil type (loamy, clay or sandy): ")

# Call the decision making function
crop = decide_crop_engine_v2(temperature, rainfall, soil_type)

# Print the recommended crop
print("We recommend you to grow", ",".join(crop))
