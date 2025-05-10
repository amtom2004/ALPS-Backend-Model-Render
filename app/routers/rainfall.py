from fastapi import APIRouter, Query, HTTPException
from app.schema import Coordinates
from app.rainfall import fetch_rainfall

router = APIRouter()

@router.post("/rainfall")
async def rainfall(data: Coordinates):
    try:
        rainfall = await fetch_rainfall(data.lat, data.lon)
        return {"rainfall": rainfall}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))