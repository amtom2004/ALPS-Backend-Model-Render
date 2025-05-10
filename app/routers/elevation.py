from fastapi import APIRouter
from app.schema import Coordinates
from app.dem import get_elevation
router = APIRouter()

@router.post("/elevation")
def elevation(data: Coordinates):
    elev = get_elevation(data.lat, data.lon)
    return {"elevation": elev}