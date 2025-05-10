from .db import get_connection

def get_elevation(lat: float, lon: float):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT "DN"
        FROM "ALPS"."DEM"
        WHERE ST_Contains(geom, ST_SetSRID(ST_Point(%s, %s), 4326))
    """, (lon, lat))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0] if result else None