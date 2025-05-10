from .db import get_connection

def get_slope(lat: float, lon: float):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT "DN"
    FROM "ALPS"."SLOPE"
    WHERE ST_Contains(
        geom,
        ST_Transform(ST_SetSRID(ST_Point(%s, %s), 4326), 32643)
    )
    """, (lon, lat))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0] if result else None