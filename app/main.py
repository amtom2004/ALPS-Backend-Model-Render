from fastapi import FastAPI
from app.routers import predict, elevation, dbcheck, rainfall, displacement, lithology, slope

app = FastAPI()

app.include_router(predict.router)
app.include_router(elevation.router)
app.include_router(dbcheck.router)
app.include_router(rainfall.router)
app.include_router(displacement.router)
app.include_router(lithology.router)
app.include_router(slope.router)

@app.get("/")
def root():
    return {"msg": "Landslide Risk Prediction API"}