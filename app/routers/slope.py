from fastapi import APIRouter
from app.schema import Coordinates
from app.slope import get_slope

router = APIRouter()

@router.post("/slope")
def elevation(data: Coordinates):
    result = get_slope(data.lat, data.lon)
    return {"slope": result}