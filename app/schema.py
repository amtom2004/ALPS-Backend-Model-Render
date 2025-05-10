from pydantic import BaseModel

class PredictionInput(BaseModel):
    displacement: float
    kriging: float
    idw: float
    elevation: float
    slope: float
    lithology: int

class Coordinates(BaseModel):
    lat: float
    lon: float