from fastapi import APIRouter
from app.model import predict
from app.schema import PredictionInput, Coordinates
from app.displacement import get_displacement
from app.rainfall import fetch_rainfall
from app.dem import get_elevation
from app.slope import get_slope
from app.lithology import get_lithology

router = APIRouter()

@router.post("/predict")
async def get_prediction(data: Coordinates):
    lat, lon = data.lat, data.lon

    displacement = get_displacement(lat, lon)
    rainfall = await fetch_rainfall(lat, lon)  # Await async function
    elevation = get_elevation(lat, lon)
    slope = get_slope(lat, lon)
    lithology = get_lithology(lat, lon)

    input_data = PredictionInput(
        displacement=displacement,
        kriging=rainfall,
        idw=rainfall,
        elevation=elevation,
        slope=slope,
        lithology=lithology
    )

    print("Input data:")
    print(f"Latitude: {lat}, Longitude: {lon}")
    print(f"Displacement: {displacement}")
    print(f"Rainfall: {rainfall}")
    print(f"Elevation: {elevation}")
    print(f"Slope: {slope}")
    print(f"Lithology: {lithology}")

    result = predict(input_data)
    return {"risk": int(result)}