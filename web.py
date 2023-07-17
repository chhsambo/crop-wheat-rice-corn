from flask import Flask, render_template, request
from inference_engine import decide_crop_engine_v2

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/about")
def about():
    return "Sample app for class Co2E1"

@app.post("/result")
def result():
    print(request.form)
    temperature = int(request.form.get("temperature")) 
    rainfall = int(request.form.get("rainfall"))
    soil_type = request.form.get("soil_type")

    # crop = "Unknown"
    # if temperature >= 35:
    #     crop = "Corn"
    crop = decide_crop_engine_v2(temperature, rainfall, soil_type)

    return render_template("result.html", output=crop)

app.run(debug=True)