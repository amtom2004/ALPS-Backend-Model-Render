import httpx
import os

# Directly setting your API key here (not via environment variable)
OPENWEATHER_API_KEY = os.getenv("API_KEY")

async def fetch_rainfall(lat: float, lon: float) -> float:
    if not OPENWEATHER_API_KEY:
        raise ValueError("API key is not set.")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    return data.get("rain", {}).get("1h", 0.0)
