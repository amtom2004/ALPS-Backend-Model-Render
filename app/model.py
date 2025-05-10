import joblib
import pandas as pd

model = joblib.load("model/landslide_model.pkl")

FEATURE_NAMES = [
    "DISPLACEMENT (cm)",
    "KRIGING (mm)",
    "IDW (mm)",
    "ELEVATION (m)",
    "SLOPE (degrees)",
    "LITHOLOGY"
]

def predict(input_data):
    df = pd.DataFrame([[
        input_data.displacement,
        input_data.kriging,
        input_data.idw,
        input_data.elevation,
        input_data.slope,
        input_data.lithology
    ]], columns=FEATURE_NAMES)

    prediction = model.predict(df)[0]
    return int(prediction)