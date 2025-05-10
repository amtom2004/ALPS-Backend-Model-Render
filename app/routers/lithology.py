from fastapi import APIRouter
from app.schema import Coordinates
from app.lithology import get_lithology
router = APIRouter()

@router.post("/lithology")
def elevation(data: Coordinates):
    result = get_lithology(data.lat, data.lon)
    return {"lithology": result}