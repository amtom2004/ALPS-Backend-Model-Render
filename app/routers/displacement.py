from fastapi import APIRouter
from app.schema import Coordinates
from app.displacement import get_displacement

router = APIRouter()

@router.post("/displacement")
def get_final_displacement(data: Coordinates):
    result = get_displacement(data.lat, data.lon)
    return {"displacement": float(result)}