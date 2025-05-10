from .db import get_connection

def get_displacement(lat: float, lon: float):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT ST_Value(rast, ST_SetSRID(ST_Point(%s, %s), 4326))
        FROM "ALPS"."DISP"
        WHERE ST_Intersects(rast, ST_SetSRID(ST_Point(%s, %s), 4326));
    """, (lon, lat, lon, lat))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0] if result else None